#!/usr/bin/env python3
"""Exact fixed-point replay for the N6-044 b=64 exclusion.

The mathematical reduction to torus fixed pairs is given in the companion
note.  This script enumerates every torus-fixed 15-plane F in Sym^2(L_0)
which contains the three rectangle-permanent lines Q_(L_0), where L_0 is
the standard coordinate K_(2,3) plane.  It computes a rigorous upper bound
for dim (E_2+F)^(1) by connected components of the coefficient constraints.

Weights in derivative equations are deliberately forgotten.  This can only
remove consistency conditions, hence the reported component count is an
upper bound over every characteristic-zero field, which is all the proof
needs.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path


N = 6
VARIABLES = N * N
LOCAL_EDGES = (0, 1, 2, 6, 7, 8)


def weight_axis(left: int, right: int) -> tuple[object, ...]:
    r0, c0 = divmod(left, N)
    r1, c1 = divmod(right, N)
    if left == right:
        return ("square", left)
    if r0 == r1:
        return ("row", r0, *sorted((c0, c1)))
    if c0 == c1:
        return ("column", c0, *sorted((r0, r1)))
    return ("rectangle", *sorted((r0, r1)), *sorted((c0, c1)))


class Components:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.zero = [False] * size

    def find(self, value: int) -> int:
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def join(self, left: int, right: int) -> None:
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        self.parent[right] = left
        self.zero[left] = self.zero[left] or self.zero[right]

    def kill(self, value: int) -> None:
        self.zero[self.find(value)] = True

    def impose(self, constraint: tuple[str, int, int | None]) -> None:
        kind, left, right = constraint
        if kind == "zero":
            self.kill(left)
        else:
            assert right is not None
            self.join(left, right)

    def surviving_count(self) -> int:
        return len(
            {
                self.find(index)
                for index in range(len(self.parent))
                if not self.zero[self.find(index)]
            }
        )


def fixed_weight_blocks() -> tuple[tuple[tuple[object, ...], ...], tuple[tuple[object, ...], ...]]:
    singleton: list[tuple[object, ...]] = []
    rectangle: list[tuple[object, ...]] = []
    for left, right in combinations_with_replacement(LOCAL_EDGES, 2):
        axis = weight_axis(left, right)
        target = rectangle if axis[0] == "rectangle" else singleton
        if axis not in target:
            target.append(axis)
    assert len(singleton) == 15
    assert len(rectangle) == 3
    return tuple(singleton), tuple(rectangle)


def compressed_constraints():
    cubics = list(combinations_with_replacement(range(VARIABLES), 3))
    cubic_index = {monomial: index for index, monomial in enumerate(cubics)}
    quadratics = list(combinations_with_replacement(range(VARIABLES), 2))
    singleton, rectangle = fixed_weight_blocks()
    local_axes = set(singleton + rectangle)
    base: list[tuple[str, int, int | None]] = []
    local: dict[tuple[object, ...], list[tuple[str, int, int | None]]] = {
        axis: [] for axis in local_axes
    }

    def store(axis, constraint) -> None:
        (local[axis] if axis in local_axes else base).append(constraint)

    for direction in range(VARIABLES):
        for pair in quadratics:
            r0, c0 = divmod(pair[0], N)
            r1, c1 = divmod(pair[1], N)
            if pair[0] != pair[1] and r0 != r1 and c0 != c1:
                continue
            monomial = tuple(sorted((*pair, direction)))
            store(weight_axis(*pair), ("zero", cubic_index[monomial], None))

        for r0, r1 in combinations(range(N), 2):
            for c0, c1 in combinations(range(N), 2):
                first = tuple(sorted((r0 * N + c0, r1 * N + c1)))
                second = tuple(sorted((r0 * N + c1, r1 * N + c0)))
                first_cubic = tuple(sorted((*first, direction)))
                second_cubic = tuple(sorted((*second, direction)))
                store(
                    weight_axis(*first),
                    (
                        "equal",
                        cubic_index[first_cubic],
                        cubic_index[second_cubic],
                    ),
                )

    coarse = Components(len(cubics))
    for constraint in base:
        coarse.impose(constraint)
    roots = {coarse.find(index) for index in range(len(cubics))}
    root_index = {root: index for index, root in enumerate(roots)}
    forced_zero = {
        root_index[root] for root in roots if coarse.zero[coarse.find(root)]
    }
    compressed: dict[tuple[object, ...], set[tuple[str, int, int | None]]] = {}
    for axis, constraints in local.items():
        answer: set[tuple[str, int, int | None]] = set()
        for kind, left, right in constraints:
            new_left = root_index[coarse.find(left)]
            if kind == "zero":
                answer.add((kind, new_left, None))
                continue
            assert right is not None
            new_right = root_index[coarse.find(right)]
            if new_left != new_right:
                answer.add((kind, new_left, new_right))
        compressed[axis] = answer
    return len(roots), forced_zero, compressed


def build_payload() -> dict[str, object]:
    singleton, rectangle = fixed_weight_blocks()
    root_count, forced_zero, constraints = compressed_constraints()
    all_axes = set(singleton + rectangle)

    def prolongation_upper(included: set[tuple[object, ...]]) -> int:
        components = Components(root_count)
        for root in forced_zero:
            components.kill(root)
        for axis in all_axes - included:
            for constraint in constraints[axis]:
                components.impose(constraint)
        return components.surviving_count()

    histogram: Counter[int] = Counter()
    maximum = 0
    maximizers: list[dict[str, object]] = []
    fixed_planes = 0
    by_rectangle_count: Counter[int] = Counter()
    for rectangle_count in range(4):
        for chosen_rectangles in combinations(rectangle, rectangle_count):
            for chosen_singletons in combinations(singleton, 12 - rectangle_count):
                fixed_planes += 1
                by_rectangle_count[rectangle_count] += 1
                included = set(chosen_rectangles + chosen_singletons)
                upper = prolongation_upper(included)
                histogram[upper] += 1
                row = {
                    "full_rectangle_blocks": [list(axis) for axis in chosen_rectangles],
                    "singleton_axes": [list(axis) for axis in chosen_singletons],
                }
                if upper > maximum:
                    maximum = upper
                    maximizers = [row]
                elif upper == maximum:
                    maximizers.append(row)

    assert fixed_planes == 18_564
    assert by_rectangle_count == {0: 455, 1: 4095, 2: 9009, 3: 5005}
    assert maximum == 436
    assert len(maximizers) == 3
    assert sum(histogram.values()) == fixed_planes

    return {
        "status": "EXACT_N6_B64_FIXED_POINT_PROLONGATION_UPPER_BOUND",
        "arithmetic": "integer zero/equality component upper bound",
        "coordinate_extremal_plane": "K_(2,3)",
        "singleton_weight_blocks": len(singleton),
        "rectangle_weight_blocks": len(rectangle),
        "fixed_F_count": fixed_planes,
        "fixed_F_count_by_full_rectangle_blocks": {
            str(key): by_rectangle_count[key] for key in sorted(by_rectangle_count)
        },
        "prolongation_component_upper_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "maximum_prolongation_dimension_upper_bound": maximum,
        "maximizer_count": len(maximizers),
        "maximizers": maximizers,
        "b64_required_dimension": 456,
        "strict_gap": 456 - maximum,
        "claim_boundary": (
            "The fixed-point enumeration supplies an upper bound, not exact "
            "prolongation dimensions. Together with the projective torus-fixed-"
            "maximum argument in the companion proof it excludes only the b=64 "
            "endpoint; it does not prove ChowRank(perm_6)>=27."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_B64_PROLONGATION_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
