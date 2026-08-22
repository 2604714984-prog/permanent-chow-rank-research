#!/usr/bin/env python3
"""Exact fixed-point audit for the N6-049 all-alpha-two exclusion."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_b64_prolongation_exclusion.py"
N6047_DATA = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"
N6041_DATA = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"
N = 6
VARIABLES = 36
STANDARD_RECTANGLE = frozenset(((0, 0), (0, 1), (1, 0), (1, 1)))


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_base():
    spec = importlib.util.spec_from_file_location("n6_b64_base", BASE_SCRIPT)
    require(spec is not None and spec.loader is not None, BASE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rectangle_count(edges: frozenset[tuple[int, int]]) -> int:
    return sum(
        frozenset(((r, c), (r, d), (s, c), (s, d))).issubset(edges)
        for r, s in combinations(range(N), 2)
        for c, d in combinations(range(N), 2)
    )


def marked_rectangle_stabilizer():
    actions = []
    for row_inside in permutations((0, 1)):
        for row_outside in permutations((2, 3, 4, 5)):
            row_permutation = row_inside + row_outside
            for column_inside in permutations((0, 1)):
                for column_outside in permutations((2, 3, 4, 5)):
                    actions.append(
                        (row_permutation, column_inside + column_outside)
                    )
    require(len(actions) == 2_304, len(actions))
    return tuple(actions)


STABILIZER = marked_rectangle_stabilizer()


def canonical_support(
    edges: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    return min(
        tuple(sorted((rows[r], columns[c]) for r, c in edges))
        for rows, columns in STABILIZER
    )


def one_rectangle_support_orbits():
    outside = [
        (row, column)
        for row in range(N)
        for column in range(N)
        if (row, column) not in STANDARD_RECTANGLE
    ]
    orbit_sizes: Counter[tuple[tuple[int, int], ...]] = Counter()
    for extra in combinations(outside, 2):
        support = STANDARD_RECTANGLE | frozenset(extra)
        if rectangle_count(support) == 1:
            orbit_sizes[canonical_support(support)] += 1
    require(len(orbit_sizes) == 12, orbit_sizes)
    require(sum(orbit_sizes.values()) == 488, orbit_sizes)
    return sorted(orbit_sizes), orbit_sizes


def coefficient_constraints(base, support):
    edges = tuple(row * N + column for row, column in support)
    cubics = list(combinations_with_replacement(range(VARIABLES), 3))
    cubic_index = {monomial: index for index, monomial in enumerate(cubics)}
    quadratics = list(combinations_with_replacement(range(VARIABLES), 2))
    local_axes = []
    for left, right in combinations_with_replacement(edges, 2):
        axis = base.weight_axis(left, right)
        if axis not in local_axes:
            local_axes.append(axis)
    require(len(local_axes) == 20, (support, local_axes))
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
            store(
                base.weight_axis(*pair),
                ("zero", cubic_index[monomial], None),
            )
        for r0, r1 in combinations(range(N), 2):
            for c0, c1 in combinations(range(N), 2):
                first = tuple(sorted((r0 * N + c0, r1 * N + c1)))
                second = tuple(sorted((r0 * N + c1, r1 * N + c0)))
                first_cubic = tuple(sorted((*first, direction)))
                second_cubic = tuple(sorted((*second, direction)))
                store(
                    base.weight_axis(*first),
                    (
                        "equal",
                        cubic_index[first_cubic],
                        cubic_index[second_cubic],
                    ),
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


def support_cap(base, support):
    root_count, forced_zero, constraints = coefficient_constraints(base, support)
    axes = tuple(sorted(constraints, key=repr))
    histogram: Counter[int] = Counter()
    maximum = 0
    maximizer_count = 0
    for selected in combinations(axes, 14):
        components = base.Components(root_count)
        for root in forced_zero:
            components.kill(root)
        for axis in set(axes) - set(selected):
            for constraint in constraints[axis]:
                components.impose(constraint)
        value = components.surviving_count()
        histogram[value] += 1
        if value > maximum:
            maximum = value
            maximizer_count = 1
        elif value == maximum:
            maximizer_count += 1
    require(sum(histogram.values()) == 38_760, (support, histogram))
    return maximum, maximizer_count, histogram


def state_certificate() -> dict[str, object]:
    payload = json.loads(N6041_DATA.read_text(encoding="utf-8"))
    layer = next(row for row in payload["layers"] if row["middle_intersection_b"] == 61)
    state = layer["states"][72]
    require(
        state["epsilon_alpha_pairs"] == [[0, 2]] * 6
        and state["fixed_quadratic_quotient_t2"] == 14
        and state["fixed_middle_rank_h"] == 120,
        state,
    )
    required = 400 + 120 - 61
    return {
        "state_identifier": "b61_state_072",
        "epsilon_alpha_pairs": state["epsilon_alpha_pairs"],
        "global_quotient_dimension_t2": 14,
        "fixed_middle_rank_h": 120,
        "middle_intersection_b": 61,
        "required_prolongation_dimension": required,
    }


def build_payload() -> dict[str, object]:
    base = load_base()
    supports, orbit_sizes = one_rectangle_support_orbits()
    rows = []
    maximum = 0
    for index, support in enumerate(supports):
        cap, maximizers, histogram = support_cap(base, support)
        maximum = max(maximum, cap)
        rows.append(
            {
                "support_orbit_identifier": f"one_rectangle_shape_{index:02d}",
                "support": [list(edge) for edge in support],
                "marked_support_count": orbit_sizes[support],
                "local_quotient_axis_count": 20,
                "fixed_A_count": 38_760,
                "prolongation_upper_cap": cap,
                "maximizer_count": maximizers,
                "upper_bound_histogram": {
                    str(key): histogram[key] for key in sorted(histogram)
                },
            }
        )
    require(maximum == 453, maximum)

    n6047 = json.loads(N6047_DATA.read_text(encoding="utf-8"))
    extremal_cap = int(
        n6047["fixed_point_cap_audit"][
            "characteristic_zero_prolongation_upper_caps"
        ]["14"]
    )
    require(extremal_cap == 448, extremal_cap)
    state = state_certificate()
    require(int(state["required_prolongation_dimension"]) > maximum, state)

    return {
        "status": "EXACT_N6_ALPHA2_PROLONGATION_EXCLUSION",
        "arithmetic": "exact integer coefficient-component upper bounds",
        "coordinate_six_edge_graph_rectangle_counts": [0, 1, 3],
        "one_rectangle_marked_support_count": 109_800,
        "one_rectangle_marked_orbit_input_count": 488,
        "one_rectangle_support_orbit_count": len(rows),
        "one_rectangle_support_rows": rows,
        "one_rectangle_universal_prolongation_cap": maximum,
        "three_rectangle_extremal_t14_cap_from_N6_047": extremal_cap,
        "three_rectangle_limit_intersection_dimensions_covered": [1, 2, 3],
        "three_rectangle_N6_047_interface": (
            "For r=dim(E2 intersection F)=1,2,3, q(F) has dimension "
            "14,13,12 and the fixed A/E2 adds 0,1,2 arbitrary axes; all are "
            "covered by the N6-047 t=14 cap 448."
        ),
        "all_alpha2_state_certificate": state,
        "strict_conclusion": (
            "The all-alpha-two state b61_state_072 is impossible: its "
            "prolongation dimension is at least 459, whereas every torus-fixed "
            "limit has upper bound at most max(453,448)=453."
        ),
        "claim_boundary": (
            "This excludes only the all-alpha-two scalar state b61_state_072. "
            "It does not by itself exclude the other b=61 states, a hypothetical "
            "26-term decomposition, prove ChowRank(perm_6)>=27, or make a "
            "border-rank claim."
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
    print(f"one_rectangle_support_orbits={payload['one_rectangle_support_orbit_count']}")
    print(f"one_rectangle_cap={payload['one_rectangle_universal_prolongation_cap']}")
    print("all_alpha2_required=459")
    print("N6_ALPHA2_PROLONGATION_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
