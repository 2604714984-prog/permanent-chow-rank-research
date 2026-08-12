#!/usr/bin/env python3
"""Exact G-042 audit of the individual alpha-three prolongation barrier.

The finite replay has two roles.

* It classifies coordinate six-edge supports, up to row and column
  permutations, and enumerates all fixed local fifteen-axis spaces above the
  rectangle-zero and rectangle-one supports.
* It verifies over ``Fraction`` and modulo a prime that the actual same-row
  Chow term has a 520-dimensional cubic prolongation.

The 520 example disproves an individual universal cap below 460.  It says
nothing by itself about six terms sharing one quotient space.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALPHA2_SCRIPT = ROOT / "scripts" / "n6_alpha2_prolongation_exclusion.py"
GLOBAL_CAP_SCRIPT = ROOT / "scripts" / "n6_global_quotient_prolongation_caps.py"
N6051_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
N = 6
VARIABLES = 36
PRIME = 1_000_003


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def integer_partitions(total: int, maximum: int = 6):
    if total == 0:
        yield ()
        return
    for value in range(min(maximum, total), 0, -1):
        for rest in integer_partitions(total - value, value):
            yield (value,) + rest


COLUMN_PERMUTATIONS = tuple(permutations(range(N)))
MASKS_BY_SIZE = {
    size: [sum(1 << column for column in choice) for choice in combinations(range(N), size)]
    for size in range(N + 1)
}


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(((mask >> index) & 1) << permutation[index] for index in range(N))


def canonical_row_masks(row_masks: list[int]) -> tuple[int, ...]:
    return min(
        tuple(sorted(permute_mask(mask, permutation) for mask in row_masks))
        for permutation in COLUMN_PERMUTATIONS
    )


def rectangle_count(row_masks: tuple[int, ...] | list[int]) -> int:
    return sum(
        (row_masks[first] & row_masks[second]).bit_count()
        * ((row_masks[first] & row_masks[second]).bit_count() - 1)
        // 2
        for first in range(N)
        for second in range(first)
    )


def coordinate_support_orbits() -> dict[int, list[tuple[int, ...]]]:
    orbits = {0: set(), 1: set(), 3: set()}
    raw_count: Counter[int] = Counter()
    for partition in integer_partitions(6):
        groups = [
            list(combinations_with_replacement(MASKS_BY_SIZE[size], multiplicity))
            for size, multiplicity in Counter(partition).items()
        ]
        for selected_groups in product(*groups):
            rows = [0] * (N - len(partition))
            for group in selected_groups:
                rows.extend(group)
            rectangles = rectangle_count(rows)
            raw_count[rectangles] += 1
            if rectangles in orbits:
                orbits[rectangles].add(canonical_row_masks(rows))
    require(set(raw_count) == {0, 1, 3}, raw_count)
    answer = {key: sorted(value) for key, value in orbits.items()}
    require({key: len(value) for key, value in answer.items()} == {0: 76, 1: 12, 3: 2}, answer)
    return answer


def labelled_rectangle_histogram() -> Counter[int]:
    histogram: Counter[int] = Counter()
    for support in combinations(range(VARIABLES), 6):
        rows = [0] * N
        for variable in support:
            row, column = divmod(variable, N)
            rows[row] |= 1 << column
        histogram[rectangle_count(rows)] += 1
    require(
        histogram == {0: 1_837_392, 1: 109_800, 3: 600},
        histogram,
    )
    return histogram


def support_from_masks(row_masks: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (row, column)
        for row, mask in enumerate(row_masks)
        for column in range(N)
        if mask >> column & 1
    )


def compressed_constraints(base, support: tuple[tuple[int, int], ...]):
    edges = tuple(row * N + column for row, column in support)
    cubics = list(combinations_with_replacement(range(VARIABLES), 3))
    cubic_index = {monomial: index for index, monomial in enumerate(cubics)}
    quadratics = list(combinations_with_replacement(range(VARIABLES), 2))
    local_axes = []
    for left, right in combinations_with_replacement(edges, 2):
        axis = base.weight_axis(left, right)
        if axis not in local_axes:
            local_axes.append(axis)
    local_set = set(local_axes)
    static = []
    dynamic = {axis: [] for axis in local_axes}

    def store(axis, constraint) -> None:
        (dynamic[axis] if axis in local_set else static).append(constraint)

    for direction in range(VARIABLES):
        for pair in quadratics:
            r0, c0 = divmod(pair[0], N)
            r1, c1 = divmod(pair[1], N)
            if pair[0] != pair[1] and r0 != r1 and c0 != c1:
                continue
            monomial = tuple(sorted((*pair, direction)))
            store(base.weight_axis(*pair), ("zero", cubic_index[monomial], None))
        for r0, r1 in combinations(range(N), 2):
            for c0, c1 in combinations(range(N), 2):
                first = tuple(sorted((r0 * N + c0, r1 * N + c1)))
                second = tuple(sorted((r0 * N + c1, r1 * N + c0)))
                first_cubic = tuple(sorted((*first, direction)))
                second_cubic = tuple(sorted((*second, direction)))
                store(
                    base.weight_axis(*first),
                    ("equal", cubic_index[first_cubic], cubic_index[second_cubic]),
                )

    coarse = base.Components(len(cubics))
    for constraint in static:
        coarse.impose(constraint)
    roots = {coarse.find(index) for index in range(len(cubics))}
    root_index = {root: index for index, root in enumerate(roots)}
    forced_zero = {
        root_index[root] for root in roots if coarse.zero[coarse.find(root)]
    }
    compressed = {}
    for axis, constraints in dynamic.items():
        answer = set()
        for kind, left, right in constraints:
            new_left = root_index[coarse.find(left)]
            if kind == "zero":
                answer.add((kind, new_left, None))
            else:
                new_right = root_index[coarse.find(right)]
                if new_left != new_right:
                    answer.add((kind, new_left, new_right))
        compressed[axis] = answer
    return len(roots), forced_zero, compressed


def support_cap(base, row_masks: tuple[int, ...]) -> dict[str, object]:
    rectangles = rectangle_count(row_masks)
    support = support_from_masks(row_masks)
    root_count, forced_zero, constraints = compressed_constraints(base, support)
    axes = tuple(sorted(constraints, key=repr))
    require(len(axes) == 21 - rectangles, (row_masks, rectangles, len(axes)))
    histogram: Counter[int] = Counter()
    maximum = 0
    maximizer_count = 0
    all_axes = set(axes)
    for selected in combinations(axes, 15):
        components = base.Components(root_count)
        for root in forced_zero:
            components.kill(root)
        for axis in all_axes - set(selected):
            for constraint in constraints[axis]:
                components.impose(constraint)
        value = components.surviving_count()
        histogram[value] += 1
        if value > maximum:
            maximum = value
            maximizer_count = 1
        elif value == maximum:
            maximizer_count += 1
    return {
        "rectangle_count": rectangles,
        "row_masks": list(row_masks),
        "local_quotient_axis_count": len(axes),
        "fixed_A_count": sum(histogram.values()),
        "component_upper_cap": maximum,
        "maximizer_count": maximizer_count,
    }


def worker(task: tuple[int, tuple[int, ...]]) -> dict[str, object]:
    index, row_masks = task
    alpha2 = load_module(ALPHA2_SCRIPT, f"n6_alpha3_worker_{index}")
    row = support_cap(alpha2.load_base(), row_masks)
    row["orbit_index"] = index
    return row


class WeightedComponents:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.weight = [Fraction(1)] * size
        self.zero = [False] * size

    def find(self, value: int) -> tuple[int, Fraction]:
        if self.parent[value] == value:
            return value, self.weight[value]
        root, parent_weight = self.find(self.parent[value])
        self.weight[value] *= parent_weight
        self.parent[value] = root
        return root, self.weight[value]

    def kill(self, value: int) -> None:
        root, _ = self.find(value)
        self.zero[root] = True

    def join(self, left: int, left_multiplier: int, right: int, right_multiplier: int) -> None:
        left_root, left_weight = self.find(left)
        right_root, right_weight = self.find(right)
        if left_root == right_root:
            if left_multiplier * left_weight != right_multiplier * right_weight:
                self.zero[left_root] = True
            return
        self.parent[left_root] = right_root
        self.weight[left_root] = Fraction(
            right_multiplier * right_weight,
            left_multiplier * left_weight,
        )
        self.zero[right_root] = self.zero[right_root] or self.zero[left_root]

    def nullity(self) -> int:
        roots = set()
        for index in range(len(self.parent)):
            root, _ = self.find(index)
            if not self.zero[root]:
                roots.add(root)
        return len(roots)


def same_row_exact_nullity(base) -> tuple[int, tuple[tuple[object, ...], ...]]:
    cubics = list(combinations_with_replacement(range(VARIABLES), 3))
    cubic_index = {monomial: index for index, monomial in enumerate(cubics)}
    quadratics = list(combinations_with_replacement(range(VARIABLES), 2))
    selected = {
        ("row", 5, first, second) for first, second in combinations(range(N), 2)
    }
    components = WeightedComponents(len(cubics))
    for direction in range(VARIABLES):
        for pair in quadratics:
            r0, c0 = divmod(pair[0], N)
            r1, c1 = divmod(pair[1], N)
            if pair[0] != pair[1] and r0 != r1 and c0 != c1:
                continue
            if base.weight_axis(*pair) not in selected:
                monomial = tuple(sorted((*pair, direction)))
                components.kill(cubic_index[monomial])
        for r0, r1 in combinations(range(N), 2):
            for c0, c1 in combinations(range(N), 2):
                first = tuple(sorted((r0 * N + c0, r1 * N + c1)))
                second = tuple(sorted((r0 * N + c1, r1 * N + c0)))
                if base.weight_axis(*first) in selected:
                    continue
                left = tuple(sorted((*first, direction)))
                right = tuple(sorted((*second, direction)))
                components.join(
                    cubic_index[left],
                    left.count(direction),
                    cubic_index[right],
                    right.count(direction),
                )
    return components.nullity(), tuple(sorted(selected, key=repr))


def modular_same_row_nullity(selected_axes) -> int:
    global_cap = load_module(GLOBAL_CAP_SCRIPT, "n6_alpha3_global_cap")
    quotient = global_cap.load_quotient_module()
    blocks, occurrences = global_cap.cubic_weight_blocks(quotient)
    masks = {}
    for axis in selected_axes:
        axis_index = quotient.AXIS_INDEX[axis]
        for block_index, bit in occurrences[axis_index]:
            masks[block_index] = masks.get(block_index, 0) | bit
    return sum(
        block.nullity(masks.get(block_index, 0))
        for block_index, block in enumerate(blocks)
    )


def compute(worker_count: int) -> dict[str, object]:
    require(1 <= worker_count <= 64, worker_count)
    orbits = coordinate_support_orbits()
    labelled_histogram = labelled_rectangle_histogram()
    tasks = list(enumerate(orbits[0] + orbits[1]))
    if worker_count == 1:
        rows = [worker(task) for task in tasks]
    else:
        with mp.get_context("spawn").Pool(worker_count) as pool:
            rows = pool.map(worker, tasks)
    by_rectangle = {}
    for rectangles in (0, 1):
        selected_rows = [row for row in rows if row["rectangle_count"] == rectangles]
        cap_histogram = Counter(row["component_upper_cap"] for row in selected_rows)
        by_rectangle[str(rectangles)] = {
            "support_orbit_count": len(selected_rows),
            "fixed_A_per_support": comb(21 - rectangles, 15),
            "component_upper_cap_histogram": {
                str(key): cap_histogram[key] for key in sorted(cap_histogram)
            },
            "maximum_component_upper_cap": max(
                row["component_upper_cap"] for row in selected_rows
            ),
            "maximizing_support_orbit_indices": [
                row["orbit_index"]
                for row in selected_rows
                if row["component_upper_cap"]
                == max(item["component_upper_cap"] for item in selected_rows)
            ],
        }
    require(
        by_rectangle["0"]["component_upper_cap_histogram"]
        == {
            "435": 7, "436": 4, "437": 9, "439": 4, "440": 6,
            "442": 4, "443": 13, "444": 6, "450": 3, "455": 6,
            "458": 6, "460": 2, "485": 4, "520": 2,
        },
        by_rectangle["0"],
    )
    require(
        by_rectangle["1"]["component_upper_cap_histogram"]
        == {
            "436": 1, "437": 2, "443": 2, "445": 2,
            "447": 2, "450": 1, "458": 2,
        },
        by_rectangle["1"],
    )

    alpha2 = load_module(ALPHA2_SCRIPT, "n6_alpha3_exact")
    base = alpha2.load_base()
    rational_nullity, selected_axes = same_row_exact_nullity(base)
    modular_nullity = modular_same_row_nullity(selected_axes)
    require((rational_nullity, modular_nullity) == (520, 520), (
        rational_nullity, modular_nullity
    ))
    n6051 = json.loads(N6051_DATA.read_text(encoding="utf-8"))
    require(n6051["characteristic_zero_prolongation_upper_cap_t15"] == 458, n6051)

    return {
        "status": "EXACT_N6_ALPHA3_INDIVIDUAL_PROLONGATION_BARRIER",
        "arithmetic": (
            "exact coordinate support classification, exhaustive integer "
            "component upper bounds, Fraction coefficient constraints, and "
            "an independent modular block rank"
        ),
        "worker_count": worker_count,
        "coordinate_six_edge_support_count": comb(36, 6),
        "coordinate_support_count_by_rectangle_count": {
            str(key): labelled_histogram[key] for key in sorted(labelled_histogram)
        },
        "row_column_support_orbit_count_by_rectangle_count": {
            str(key): len(orbits[key]) for key in sorted(orbits)
        },
        "fixed_local_t15_diagnostics": by_rectangle,
        "three_rectangle_t15_cap_from_N6_051": 458,
        "same_row_actual_term": {
            "term": "product_(c=0)^5 x_(5,c)",
            "factor_span_dimension": 6,
            "quadratic_derivative_dimension": 15,
            "permanent_quadratic_intersection_dimension": 0,
            "epsilon_alpha": [0, 3],
            "selected_quotient_axes": [list(axis) for axis in selected_axes],
            "pure_coefficient_block_dimension": (
                "C(6,3)^2 + 5*C(6,3) + C(6,3) = 400+100+20=520"
            ),
            "exact_fraction_prolongation_dimension": rational_nullity,
            "modular_prolongation_nullity_mod_1000003": modular_nullity,
        },
        "strict_conclusion": (
            "No universal individual alpha-three t=15 prolongation cap below "
            "460 exists: the displayed actual Chow term has exact dimension 520."
        ),
        "claim_boundary": (
            "This blocks only an individual-term prolongation argument. It does "
            "not refute or exclude a six-term coupled b=60 argument: in that "
            "state six quadratic spaces share one quotient fifteen-plane and are "
            "literal direct. A fixed-point degeneration may destroy directness."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(20, os.cpu_count() or 1))
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = compute(args.workers)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print(
        "coordinate_support_orbits="
        f"{payload['row_column_support_orbit_count_by_rectangle_count']}"
    )
    print("same_row_exact_prolongation_dimension=520")
    print("N6_ALPHA3_INDIVIDUAL_PROLONGATION_BARRIER_PASS")
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
