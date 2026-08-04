#!/usr/bin/env python3
"""Exact arithmetic audit closing the ``n=6`` fixed-four 23-term frontier.

The proof note supplies three algebraic inputs:

* a scalar quadratic space of dimension ``k`` has first prolongation
  dimension at most the degree-two Macaulay successor ``k^{<2>}``;
* for four component spaces, the cubic relation kernel has dimension at
  most three times that scalar cap; and
* the block-Sylvester inequality converts a cubic-relation cap into a
  lower bound for the coupled middle-catalectic rank.

This script exhaustively checks every labelled defect pattern in the
remaining layers ``b=22,23,24``. It deliberately assigns central rank zero
to an individual term with quadratic derivative dimension ten, so the
``b=22`` conclusion does not depend on a classification at that profile.

The arithmetic replay does not replace the algebraic lemmas in
``docs/n6_component_prolongation_exclusion.md``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path

FIXED_TERMS = 4
MAXIMUM_QUADRATIC_DIMENSION = 15
MAXIMUM_INDIVIDUAL_INTERSECTION = 3
PERMANENT_KOSZUL_RANK = 14_175
RESIDUAL_TERMS = 19
PER_TERM_KOSZUL_CAP = 705
RESIDUAL_KOSZUL_CAP = RESIDUAL_TERMS * PER_TERM_KOSZUL_CAP

# Complete for quadratic dimensions 11--15. Dimension 12 is impossible.
# Dimension 10 is assigned the deliberately conservative lower bound zero.
CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION: dict[int, int | None] = {
    15: 20,
    14: 20,
    13: 18,
    12: None,
    11: 14,
    10: 0,
}


def macaulay_successor_degree_two(value: int) -> int:
    """Return the degree-two Macaulay successor ``value^{<2>}``."""

    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0

    remaining = value
    upper = 10**9
    expansion: list[tuple[int, int]] = []
    for degree in (2, 1):
        index = degree - 1
        while index + 1 < upper and comb(index + 1, degree) <= remaining:
            index += 1
        expansion.append((index, degree))
        remaining -= comb(index, degree)
        upper = index

    if remaining != 0:
        raise AssertionError((value, expansion, remaining))
    return sum(comb(index + 1, degree + 1) for index, degree in expansion)


def enumerate_layer_patterns(b: int) -> list[dict[str, object]]:
    if b not in {22, 23, 24}:
        raise ValueError(b)

    defect_budget = 27 - b
    shadow_dimension = b + 21
    patterns: list[dict[str, object]] = []

    for epsilon in product(range(defect_budget + 1), repeat=FIXED_TERMS):
        for alpha in product(range(defect_budget + 1), repeat=FIXED_TERMS):
            if not all(
                sum(
                    epsilon[index]
                    for index in range(FIXED_TERMS)
                    if index != omitted
                )
                + alpha[omitted]
                <= defect_budget
                for omitted in range(FIXED_TERMS)
            ):
                continue

            quadratic_dimensions = [
                MAXIMUM_QUADRATIC_DIMENSION - value for value in epsilon
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
                sum(quadratic_dimensions)
                - shadow_dimension
                - max(quotient_dimensions)
            )
            if relation_kernel_cap < 0:
                raise AssertionError(
                    (b, epsilon, alpha, relation_kernel_cap)
                )
            if relation_kernel_cap > defect_budget:
                raise AssertionError(
                    (
                        b,
                        epsilon,
                        alpha,
                        relation_kernel_cap,
                        defect_budget,
                    )
                )

            profile_impossible = any(
                dimension == 12 for dimension in quadratic_dimensions
            )
            if profile_impossible:
                central_rank_lowers: list[int] | None = None
                scalar_prolongation_cap = None
                cubic_relation_cap = None
                coupled_central_rank_lower = None
            else:
                central_rank_lowers = [
                    int(
                        CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION[
                            dimension
                        ]
                    )
                    for dimension in quadratic_dimensions
                ]
                scalar_prolongation_cap = macaulay_successor_degree_two(
                    relation_kernel_cap
                )
                cubic_relation_cap = (
                    (FIXED_TERMS - 1) * scalar_prolongation_cap
                )
                coupled_central_rank_lower = (
                    sum(central_rank_lowers) - 2 * cubic_relation_cap
                )

            patterns.append(
                {
                    "epsilon": list(epsilon),
                    "alpha": list(alpha),
                    "quadratic_dimensions": quadratic_dimensions,
                    "quotient_dimensions": quotient_dimensions,
                    "quadratic_relation_kernel_cap": relation_kernel_cap,
                    "profile_impossible": profile_impossible,
                    "individual_central_rank_lowers": central_rank_lowers,
                    "scalar_component_prolongation_cap": (
                        scalar_prolongation_cap
                    ),
                    "cubic_relation_kernel_cap": cubic_relation_cap,
                    "coupled_central_rank_lower": (
                        coupled_central_rank_lower
                    ),
                }
            )

    return patterns


def histogram(
    rows: list[dict[str, object]],
    key: str,
) -> dict[str, int]:
    counts = Counter(int(row[key]) for row in rows)
    return {str(item): count for item, count in sorted(counts.items())}


def layer_payload(b: int) -> dict[str, object]:
    rows = enumerate_layer_patterns(b)
    feasible = [
        row for row in rows if not bool(row["profile_impossible"])
    ]
    impossible = [
        row for row in rows if bool(row["profile_impossible"])
    ]
    if not feasible:
        raise AssertionError(b)

    residual_central_rank_upper = 2 * b - 20
    minimum_coupled_rank = min(
        int(row["coupled_central_rank_lower"]) for row in feasible
    )
    minimizers = [
        row
        for row in feasible
        if int(row["coupled_central_rank_lower"])
        == minimum_coupled_rank
    ]
    if len(minimizers) != 1:
        raise AssertionError((b, len(minimizers)))
    minimizer = minimizers[0]
    if minimizer["epsilon"] != [0, 0, 0, 0]:
        raise AssertionError((b, minimizer))
    if minimizer["alpha"] != [0, 0, 0, 0]:
        raise AssertionError((b, minimizer))
    if minimum_coupled_rank <= residual_central_rank_upper:
        raise AssertionError(
            (b, minimum_coupled_rank, residual_central_rank_upper)
        )

    return {
        "b": b,
        "defect_budget": 27 - b,
        "quadratic_shadow_lower_bound": b + 21,
        "all_labelled_pattern_count": len(rows),
        "all_relation_kernel_cap_histogram": histogram(
            rows,
            "quadratic_relation_kernel_cap",
        ),
        "quadratic_dimension_twelve_pattern_count": len(impossible),
        "profile_feasible_pattern_count": len(feasible),
        "profile_feasible_relation_kernel_cap_histogram": histogram(
            feasible,
            "quadratic_relation_kernel_cap",
        ),
        "maximum_quadratic_relation_kernel_cap": max(
            int(row["quadratic_relation_kernel_cap"]) for row in feasible
        ),
        "maximum_scalar_component_prolongation_cap": max(
            int(row["scalar_component_prolongation_cap"])
            for row in feasible
        ),
        "maximum_cubic_relation_kernel_cap": max(
            int(row["cubic_relation_kernel_cap"]) for row in feasible
        ),
        "minimum_coupled_central_rank_lower_bound": minimum_coupled_rank,
        "residual_central_rank_upper_bound": residual_central_rank_upper,
        "strict_margin": (
            minimum_coupled_rank - residual_central_rank_upper
        ),
        "unique_worst_pattern": {
            "epsilon": minimizer["epsilon"],
            "alpha": minimizer["alpha"],
            "quadratic_dimensions": minimizer[
                "quadratic_dimensions"
            ],
            "quadratic_relation_kernel_cap": minimizer[
                "quadratic_relation_kernel_cap"
            ],
            "scalar_component_prolongation_cap": minimizer[
                "scalar_component_prolongation_cap"
            ],
            "cubic_relation_kernel_cap": minimizer[
                "cubic_relation_kernel_cap"
            ],
            "coupled_central_rank_lower": minimizer[
                "coupled_central_rank_lower"
            ],
        },
    }


def automatic_low_layers() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for b, d in ((20, 0), (21, 0), (21, 1)):
        lower = PERMANENT_KOSZUL_RANK - 36 * b
        if lower <= RESIDUAL_KOSZUL_CAP:
            raise AssertionError((b, d, lower))
        rows.append(
            {
                "b": b,
                "d": d,
                "residual_koszul_rank_lower_bound": lower,
                "nineteen_term_koszul_cap": RESIDUAL_KOSZUL_CAP,
                "strict_margin": lower - RESIDUAL_KOSZUL_CAP,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    expected_macaulay = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 4,
        "4": 5,
        "5": 7,
    }
    live_macaulay = {
        str(value): macaulay_successor_degree_two(value)
        for value in range(6)
    }
    if live_macaulay != expected_macaulay:
        raise AssertionError(live_macaulay)

    layers = [layer_payload(b) for b in (22, 23, 24)]
    expected_layer_summary = {
        22: (14_877, 1_716, 13_161, 38, 24),
        23: (4_599, 256, 4_343, 50, 26),
        24: (1_153, 16, 1_137, 56, 28),
    }
    for layer in layers:
        b = int(layer["b"])
        observed = (
            int(layer["all_labelled_pattern_count"]),
            int(layer["quadratic_dimension_twelve_pattern_count"]),
            int(layer["profile_feasible_pattern_count"]),
            int(layer["minimum_coupled_central_rank_lower_bound"]),
            int(layer["residual_central_rank_upper_bound"]),
        )
        if observed != expected_layer_summary[b]:
            raise AssertionError((b, observed))

    return {
        "status": (
            "EXACT_N6_FIXED_FOUR_FRONTIER_CLOSED_THROUGH_LOWER_24"
        ),
        "macaulay_degree_two_successors": live_macaulay,
        "individual_central_rank_lower_table": {
            str(key): value
            for key, value in sorted(
                CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION.items(),
                reverse=True,
            )
        },
        "conservative_profile_policy": (
            "Quadratic dimension 12 is rejected as impossible. "
            "Quadratic dimension 10 receives central-rank lower bound zero, "
            "so the b=22 exclusion does not depend on classifying that "
            "profile."
        ),
        "layers": layers,
        "remaining_low_layers": automatic_low_layers(),
        "conclusion": (
            "Every fixed-four state under a hypothetical 23-term "
            "decomposition is contradictory. Therefore "
            "ChowRank(perm_6)>=24 over characteristic zero."
        ),
        "certified_interval": [24, 32],
        "claim_boundary": (
            "This closes only the 23-term exclusion and does not prove "
            "ChowRank(perm_6)>=25, border Chow rank 24, or the conjectural "
            "exact value 32."
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
    print("N6_COMPONENT_PROLONGATION_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
