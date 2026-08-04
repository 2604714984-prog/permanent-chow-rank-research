#!/usr/bin/env python3
"""Exact integer diagnostic for the ``n=6`` fixed-four layer ``b=24``.

The proved fixed-four exclusion chain leaves ``20<=b<=24``.  At the top
remaining layer, the quadratic shadow is exactly 45 and the omitted-factor
defect inequalities are

    sum(epsilon_i for i != j) + alpha_j <= 3.

Here ``epsilon_i=15-dim D_2(T_i)`` and
``alpha_i=3-dim(E_2 intersect D_2(T_i))``.

This script exhaustively enumerates the labelled integer patterns, computes
the dimension-only cap on the quadratic relation kernel, removes patterns
requiring the impossible degree-six Chow-term quadratic dimension 12, and
isolates the unique cap-three equality pattern.

The result is a route diagnostic.  It does not exclude ``b=24`` or prove a
lower bound of 24 for ``ChowRank(perm_6)``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import product
from pathlib import Path

FIXED_TERMS = 4
DEFECT_BUDGET = 3
QUADRATIC_SHADOW_DIMENSION = 45
MAXIMUM_QUADRATIC_DIMENSION = 15
MAXIMUM_INDIVIDUAL_INTERSECTION = 3


def enumerate_patterns() -> list[dict[str, object]]:
    patterns: list[dict[str, object]] = []

    for epsilon in product(range(DEFECT_BUDGET + 1), repeat=FIXED_TERMS):
        for alpha in product(range(DEFECT_BUDGET + 1), repeat=FIXED_TERMS):
            if not all(
                sum(
                    epsilon[index]
                    for index in range(FIXED_TERMS)
                    if index != omitted
                )
                + alpha[omitted]
                <= DEFECT_BUDGET
                for omitted in range(FIXED_TERMS)
            ):
                continue

            individual_dimensions = [
                MAXIMUM_QUADRATIC_DIMENSION - epsilon[index]
                for index in range(FIXED_TERMS)
            ]
            quotient_dimensions = [
                (
                    MAXIMUM_QUADRATIC_DIMENSION
                    - epsilon[index]
                    - (
                        MAXIMUM_INDIVIDUAL_INTERSECTION
                        - alpha[index]
                    )
                )
                for index in range(FIXED_TERMS)
            ]
            relation_kernel_cap = (
                sum(individual_dimensions)
                - QUADRATIC_SHADOW_DIMENSION
                - max(quotient_dimensions)
            )
            if relation_kernel_cap < 0:
                raise AssertionError(
                    (epsilon, alpha, relation_kernel_cap)
                )

            patterns.append(
                {
                    "epsilon": list(epsilon),
                    "alpha": list(alpha),
                    "individual_quadratic_dimensions": individual_dimensions,
                    "individual_quotient_dimensions": quotient_dimensions,
                    "relation_kernel_cap": relation_kernel_cap,
                    "profile_realizable": max(epsilon) <= 2,
                }
            )

    return patterns


def cap_histogram(patterns: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(
        int(pattern["relation_kernel_cap"])
        for pattern in patterns
    )
    return {str(key): value for key, value in sorted(counts.items())}


def epsilon_histogram(patterns: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(
        sum(int(value) for value in pattern["epsilon"])
        for pattern in patterns
    )
    return {str(key): value for key, value in sorted(counts.items())}


def build_payload() -> dict[str, object]:
    patterns = enumerate_patterns()
    if len(patterns) != 1_153:
        raise AssertionError(len(patterns))

    all_cap_counts = cap_histogram(patterns)
    if all_cap_counts != {"0": 940, "1": 189, "2": 23, "3": 1}:
        raise AssertionError(all_cap_counts)

    impossible_dimension_twelve = [
        pattern
        for pattern in patterns
        if not bool(pattern["profile_realizable"])
    ]
    if len(impossible_dimension_twelve) != 16:
        raise AssertionError(len(impossible_dimension_twelve))
    if not all(
        12 in pattern["individual_quadratic_dimensions"]
        for pattern in impossible_dimension_twelve
    ):
        raise AssertionError("unexpected profile-impossible pattern")

    realizable = [
        pattern
        for pattern in patterns
        if bool(pattern["profile_realizable"])
    ]
    if len(realizable) != 1_137:
        raise AssertionError(len(realizable))

    realizable_cap_counts = cap_histogram(realizable)
    if realizable_cap_counts != {"0": 924, "1": 189, "2": 23, "3": 1}:
        raise AssertionError(realizable_cap_counts)

    cap_three = [
        pattern
        for pattern in realizable
        if pattern["relation_kernel_cap"] == 3
    ]
    if len(cap_three) != 1:
        raise AssertionError(cap_three)
    unique = cap_three[0]
    if unique["epsilon"] != [0, 0, 0, 0]:
        raise AssertionError(unique)
    if unique["alpha"] != [0, 0, 0, 0]:
        raise AssertionError(unique)
    if unique["individual_quadratic_dimensions"] != [15, 15, 15, 15]:
        raise AssertionError(unique)
    if unique["individual_quotient_dimensions"] != [12, 12, 12, 12]:
        raise AssertionError(unique)

    cap_two = [
        pattern
        for pattern in realizable
        if pattern["relation_kernel_cap"] == 2
    ]
    cap_two_epsilon_types = Counter(
        tuple(sorted(int(value) for value in pattern["epsilon"]))
        for pattern in cap_two
    )
    expected_cap_two_types = {
        (0, 0, 0, 0): 15,
        (0, 0, 0, 1): 8,
    }
    if dict(cap_two_epsilon_types) != expected_cap_two_types:
        raise AssertionError(cap_two_epsilon_types)

    return {
        "status": "EXACT_B24_THREE_RELATION_FRONTIER_REPLAYED",
        "scope": "dimension-only defect and quadratic-relation frontier at b=24",
        "central_intersection_b": 24,
        "quadratic_shadow_dimension": QUADRATIC_SHADOW_DIMENSION,
        "defect_budget": DEFECT_BUDGET,
        "all_labelled_pattern_count": len(patterns),
        "all_relation_kernel_cap_histogram": all_cap_counts,
        "all_total_epsilon_histogram": epsilon_histogram(patterns),
        "quadratic_dimension_twelve_pattern_count": len(
            impossible_dimension_twelve
        ),
        "profile_realizable_pattern_count": len(realizable),
        "profile_realizable_relation_kernel_cap_histogram": (
            realizable_cap_counts
        ),
        "profile_realizable_total_epsilon_histogram": epsilon_histogram(
            realizable
        ),
        "cap_two_epsilon_type_histogram": {
            ",".join(str(value) for value in key): count
            for key, count in sorted(cap_two_epsilon_types.items())
        },
        "unique_three_relation_pattern": {
            "epsilon": unique["epsilon"],
            "alpha": unique["alpha"],
            "individual_quadratic_dimensions": unique[
                "individual_quadratic_dimensions"
            ],
            "individual_intersection_dimensions": [3, 3, 3, 3],
            "individual_quotient_dimensions": unique[
                "individual_quotient_dimensions"
            ],
            "quadratic_relation_kernel_cap": 3,
        },
        "structural_interpretation": (
            "The unique cap-three pattern has four maximal quadratic "
            "derivative spaces and four maximal three-dimensional permanent "
            "intersections. The extremal six-plane theorem therefore applies "
            "to all four factor spans."
        ),
        "claim_boundary": (
            "This is a fail-closed route diagnostic. A three-dimensional "
            "quadratic relation kernel can support ternary squarefree cubics, "
            "so the one- and two-relation exclusions do not settle b=24."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_B24_THREE_RELATION_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
