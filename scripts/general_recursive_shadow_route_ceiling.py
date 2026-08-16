#!/usr/bin/env python3
"""Exact optimization of recursively nested one-block shadow projections.

This audit starts from the exact iterated product-shadow implementation in
``general_iterated_product_shadow_blocks.py``.  It rebuilds every direct block
cap, closes those caps under recursive block projection, and exhausts the
stated fixed counts.

The computation proves a route ceiling, not a Chow-rank upper bound:

* every valid first-Koszul output degree for ``perm_7`` gives at most 45;
* central output degree four for ``perm_8`` gives at most 79;
* output degree five for ``perm_8`` gives at most 78.

It also derives the exact five-term cubic-intersection target 146 that would
raise the central ``perm_8`` lower bound to 80.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

from general_iterated_product_shadow_blocks import (
    ExactIteratedProductShadow,
    first_koszul_data,
    require,
)

EXPECTED_CORE_SHA256 = (
    "b4a55c1f6fe331b9c43159a0d7fad991645039c5feba1f25e6e979f1e07de86c"
)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def recursive_block_caps(
    n: int,
    derivative_degree: int,
    maximum_terms: int,
) -> tuple[dict[int, int], dict[int, list[object]], dict[str, int]]:
    """Return direct-and-recursive permanent-relative block caps.

    ``maximum_terms`` is exclusive.  The direct table is keyed by ``"s,a"``
    for deterministic JSON identity.
    """

    require(derivative_degree >= 2, derivative_degree)
    require(maximum_terms >= 2, maximum_terms)
    one_term_dimension = comb(n, derivative_degree)

    direct: dict[str, int] = {}
    direct_integer: dict[tuple[int, int], int] = {}
    for order in range(1, derivative_degree):
        shadow = ExactIteratedProductShadow(n, derivative_degree, order)
        for terms in range(1, maximum_terms):
            threshold = terms * comb(n, derivative_degree - order)
            last_good, _ = shadow.transition(threshold)
            direct_integer[(terms, order)] = last_good.family_size
            direct[f"{terms},{order}"] = last_good.family_size
        del shadow
        gc.collect()

    beta: dict[int, int] = {0: 0}
    source: dict[int, list[object]] = {0: ["zero"]}
    for terms in range(1, maximum_terms):
        candidates: list[tuple[int, list[object]]] = [
            (direct_integer[(terms, order)], ["direct", order])
            for order in range(1, derivative_degree)
        ]
        candidates.extend(
            (
                (terms - retained) * one_term_dimension + beta[retained],
                ["project", retained],
            )
            for retained in range(1, terms)
        )
        beta[terms], source[terms] = min(candidates, key=lambda item: item[0])

    return beta, source, direct


def scan_all_blocks(
    n: int,
    output_degree: int,
    fixed_term_limit: int,
) -> dict[str, Any]:
    """Exhaust every fixed count and every recursive block size."""

    complement_degree = n - output_degree
    derivative_degree = complement_degree - 1
    beta, source, direct = recursive_block_caps(
        n,
        derivative_degree,
        fixed_term_limit,
    )
    one_term_dimension = comb(n, derivative_degree)
    outer = ExactIteratedProductShadow(n, complement_degree, 1)
    target, one_term_koszul, _ = first_koszul_data(n, output_degree)

    transition_cache: dict[int, int] = {}
    best = -1
    optimum_rows: list[list[object]] = []
    for fixed_terms in range(2, fixed_term_limit + 1):
        for block_terms in range(1, fixed_terms):
            block_cap = beta[block_terms]
            capacity = (
                (fixed_terms - block_terms) * one_term_dimension + block_cap
            )
            if capacity not in transition_cache:
                last_good, _ = outer.transition(capacity)
                transition_cache[capacity] = last_good.family_size
            outer_cap = transition_cache[capacity]
            numerator = target - n * n * outer_cap
            residual = (
                0
                if numerator <= 0
                else -(-numerator // one_term_koszul)
            )
            total = fixed_terms + residual
            row: list[object] = [
                total,
                fixed_terms,
                block_terms,
                block_cap,
                capacity,
                outer_cap,
                residual,
                source[block_terms],
            ]
            if total > best:
                best = total
                optimum_rows = [row]
            elif total == best:
                optimum_rows.append(row)

    del outer
    gc.collect()
    return {
        "best": best,
        "optima": optimum_rows,
        "beta": {str(index): value for index, value in beta.items()},
        "source": {str(index): value for index, value in source.items()},
        "direct": direct,
    }


def scan_minimum_capacity_by_fixed_count(
    n: int,
    output_degree: int,
    fixed_term_limit: int,
) -> dict[str, Any]:
    """Use the minimum projected capacity for each fixed count.

    This is equivalent to scanning every block size because the exact outer
    cap and the residual count are monotone in the projected capacity.
    """

    complement_degree = n - output_degree
    derivative_degree = complement_degree - 1
    beta, source, direct = recursive_block_caps(
        n,
        derivative_degree,
        fixed_term_limit,
    )
    one_term_dimension = comb(n, derivative_degree)
    outer = ExactIteratedProductShadow(n, complement_degree, 1)
    target, one_term_koszul, _ = first_koszul_data(n, output_degree)

    rows: list[list[int]] = []
    optimum_rows: list[list[int]] = []
    best = -1
    for fixed_terms in range(2, fixed_term_limit + 1):
        capacity, block_terms = min(
            (
                (fixed_terms - terms) * one_term_dimension + beta[terms],
                terms,
            )
            for terms in range(1, fixed_terms)
        )
        last_good, _ = outer.transition(capacity)
        outer_cap = last_good.family_size
        numerator = target - n * n * outer_cap
        residual = (
            0
            if numerator <= 0
            else -(-numerator // one_term_koszul)
        )
        total = fixed_terms + residual
        row = [
            fixed_terms,
            block_terms,
            capacity,
            outer_cap,
            last_good.shadow_size,
            residual,
            total,
        ]
        rows.append(row)
        if total > best:
            best = total
            optimum_rows = [row]
        elif total == best:
            optimum_rows.append(row)

    del outer
    gc.collect()
    return {
        "best": best,
        "rows": rows,
        "optima": optimum_rows,
        "beta": {str(index): value for index, value in beta.items()},
        "source": {str(index): value for index, value in source.items()},
        "direct": direct,
    }


def build_payload() -> dict[str, object]:
    n7_by_output = {
        output_degree: scan_all_blocks(7, output_degree, 43)
        for output_degree in (2, 3, 4)
    }
    require(
        {degree: row["best"] for degree, row in n7_by_output.items()}
        == {2: 44, 3: 45, 4: 43},
        n7_by_output,
    )

    n8_central = scan_minimum_capacity_by_fixed_count(8, 4, 78)
    n8_complementary = scan_all_blocks(8, 5, 78)
    require(n8_central["best"] == 79, n8_central["best"])
    require(n8_complementary["best"] == 78, n8_complementary["best"])

    n7_central_beta = [
        int(n7_by_output[3]["beta"][str(index)])
        for index in range(43)
    ]
    n8_central_beta = [
        int(n8_central["beta"][str(index)])
        for index in range(78)
    ]

    expected_n8_optima = [
        [16, 5, 776, 551, 776, 63, 79],
        [17, 5, 832, 591, 832, 62, 79],
        [18, 5, 888, 647, 888, 61, 79],
        [19, 5, 944, 710, 940, 60, 79],
        [20, 5, 1000, 825, 1000, 59, 79],
        [21, 5, 1056, 880, 1054, 58, 79],
        [29, 5, 1504, 1457, 1504, 50, 79],
    ]
    require(n8_central["optima"] == expected_n8_optima, n8_central["optima"])

    # Exact lower-80 threshold at q=20, s=5.
    target, one_term, _ = first_koszul_data(8, 4)
    required_residual = 60
    maximum_outer_cap = (
        target - 1 - (required_residual - 1) * one_term
    ) // 64
    require(maximum_outer_cap == 772, maximum_outer_cap)
    outer = ExactIteratedProductShadow(8, 4, 1)
    first_excluded_shadow = outer.minimum(maximum_outer_cap + 1).shadow_size
    require(first_excluded_shadow == 987, first_excluded_shadow)
    maximum_projected_capacity = first_excluded_shadow - 1
    outside_capacity = 15 * comb(8, 3)
    required_block_cap = maximum_projected_capacity - outside_capacity
    require(required_block_cap == 146, required_block_cap)
    del outer
    gc.collect()

    core = {
        "status": [
            "GENERAL_RECURSIVE_SHADOW_ROUTE_CEILING",
            "EXACT_INTEGER_OPTIMIZATION_REPLAYED",
            "NEXT_CHOW_REALIZABILITY_TARGET_IDENTIFIED",
        ],
        "dependency": {
            "pr": 40,
            "head": "ad92c756e42fc670325f4b498013ea4b2bc370ed",
            "theorem": (
                "general iterated product shadows and nonzero block projection"
            ),
        },
        "n7": {
            "certified_fixed_term_limit": 43,
            "all_valid_output_degrees": {
                str(degree): {
                    "ceiling": n7_by_output[degree]["best"],
                    "optimum_count": len(n7_by_output[degree]["optima"]),
                    "beta_sha256": canonical_sha256(
                        n7_by_output[degree]["beta"]
                    ),
                    "optima_sha256": canonical_sha256(
                        n7_by_output[degree]["optima"]
                    ),
                }
                for degree in (2, 3, 4)
            },
            "global_recursive_two_level_ceiling": 45,
            "central_beta": n7_central_beta,
            "representative_optimum": {
                "output_degree": 3,
                "fixed_terms": 19,
                "block_terms": 4,
                "block_cap": 64,
                "projected_capacity": 589,
                "outer_cap": 341,
                "residual_terms": 26,
                "total": 45,
            },
            "next_lower_bound": 46,
            "smallest_detected_chow_specific_cap_reduction": 35,
        },
        "n8": {
            "certified_fixed_term_limit": 78,
            "central_output_degree": 4,
            "central_recursive_two_level_ceiling": 79,
            "central_beta": n8_central_beta,
            "central_beta_sha256": canonical_sha256(n8_central["beta"]),
            "central_direct_cap_sha256": canonical_sha256(
                n8_central["direct"]
            ),
            "central_route_rows": n8_central["rows"],
            "central_route_rows_sha256": canonical_sha256(
                n8_central["rows"]
            ),
            "central_optima": n8_central["optima"],
            "central_optima_sha256": canonical_sha256(
                n8_central["optima"]
            ),
            "complementary_output_degree_5_ceiling": (
                n8_complementary["best"]
            ),
            "complementary_beta_sha256": canonical_sha256(
                n8_complementary["beta"]
            ),
            "next_lower_bound_target": {
                "desired_bound": 80,
                "output_degree": 4,
                "fixed_terms": 20,
                "block_terms": 5,
                "current_general_block_cap": 160,
                "required_chow_realizable_block_cap": 146,
                "required_cap_improvement": 14,
                "outside_capacity": outside_capacity,
                "maximum_projected_capacity": maximum_projected_capacity,
                "required_outer_intersection_cap": maximum_outer_cap,
                "first_excluded_outer_size": maximum_outer_cap + 1,
                "first_excluded_outer_shadow": first_excluded_shadow,
            },
        },
        "claim_boundary": (
            "The n=7 ceiling covers all valid output degrees in the stated "
            "recursively nested one-block exact-shadow framework. The n=8 "
            "ceiling is proved for the central output degree m=4; output "
            "degree m=5 is separately checked at 78. No claim is made for "
            "every noncentral n=8 output degree, exact rank, border rank, or "
            "general Glynn optimality."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


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
    print("GENERAL_RECURSIVE_SHADOW_ROUTE_CEILING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
