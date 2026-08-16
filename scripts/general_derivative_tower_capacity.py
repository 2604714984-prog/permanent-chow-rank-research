#!/usr/bin/env python3
"""Recursive permanent-relative capacities across all derivative degrees.

The exact first product-shadow theorem supplies the inverse transition from an
upper bound at degree ``d-1`` to an upper bound at degree ``d``. A
section/projection lemma supplies an independent recursion in the number of
Chow terms. Iterating the adjacent transition yields a uniform derivative
capacity tower.

The first new numerical consequence is

    ChowRank(perm_7) >= 46.

All arithmetic is exact and deterministic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

from general_exact_product_shadow import ExactProductShadow, first_koszul_data


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def inverse_shadow_capacity(
    shadow: ExactProductShadow,
    threshold: int,
) -> int:
    """Largest family size whose exact first shadow is at most threshold."""

    full_size = shadow.layer_size**2
    full = shadow.minimum(full_size)
    if full.shadow_size <= threshold:
        return full_size
    last_good, first_bad = shadow.transition(threshold)
    require(
        last_good.shadow_size <= threshold < first_bad.shadow_size,
        (threshold, last_good, first_bad),
    )
    return last_good.family_size


def derivative_tower_capacities(
    n: int,
    maximum_degree: int,
    maximum_terms: int,
) -> dict[int, list[int]]:
    """Build the adjacent recursive capacity rows.

    ``rows[d][q]`` bounds

        dim(D_d(perm_n) intersect sum_(i=1)^q D_d(T_i)).
    """

    require(n >= 3, n)
    require(1 <= maximum_degree <= n, maximum_degree)
    require(maximum_terms >= 1, maximum_terms)

    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    shadows: dict[int, ExactProductShadow] = {}

    for degree in range(2, maximum_degree + 1):
        one_term = comb(n, degree)
        ambient = one_term**2
        if degree not in shadows:
            shadows[degree] = ExactProductShadow(n, degree)
        current_shadow = shadows[degree]

        rows[degree] = [0]
        for terms in range(1, maximum_terms + 1):
            candidates = [
                min(ambient, terms * one_term),
                inverse_shadow_capacity(
                    current_shadow,
                    rows[degree - 1][terms],
                ),
            ]
            candidates.extend(
                (terms - retained_terms) * one_term
                + rows[degree][retained_terms]
                for retained_terms in range(1, terms)
            )
            rows[degree].append(min(candidates))

    return rows


def perm7_application(rows: dict[int, list[int]]) -> dict[str, int]:
    block_terms = 5
    block_cap = rows[3][block_terms]
    require(block_cap == 64, block_cap)

    fixed_terms = 20
    outside_terms = fixed_terms - block_terms
    projected_capacity = outside_terms * comb(7, 3) + block_cap
    require(projected_capacity == 589, projected_capacity)

    outer = ExactProductShadow(7, 4)
    last_good, first_bad = outer.transition(projected_capacity)
    require(
        (
            last_good.family_size,
            last_good.shadow_size,
            first_bad.family_size,
            first_bad.shadow_size,
        )
        == (341, 586, 342, 590),
        (last_good, first_bad),
    )

    target, one_term, _ = first_koszul_data(7, 3)
    numerator = target - 49 * last_good.family_size
    residual = -(-numerator // one_term)
    require(
        (target, one_term, numerator, residual)
        == (58_800, 1_680, 42_091, 26),
        (target, one_term, numerator, residual),
    )
    total = fixed_terms + residual
    require(total == 46, total)

    return {
        "fixed_terms": fixed_terms,
        "block_terms": block_terms,
        "five_term_cubic_cap": block_cap,
        "outside_term_count": outside_terms,
        "projected_first_shadow_capacity": projected_capacity,
        "outer_intersection_cap": last_good.family_size,
        "outer_shadow_at_cap": last_good.shadow_size,
        "outer_first_excluded_size": first_bad.family_size,
        "outer_shadow_at_first_excluded_size": first_bad.shadow_size,
        "first_koszul_target_rank": target,
        "one_term_koszul_cap": one_term,
        "residual_rank_numerator": numerator,
        "residual_terms": residual,
        "ordinary_lower_bound": total,
    }


def perm8_regression(rows: dict[int, list[int]]) -> dict[str, int]:
    block_terms = 5
    block_cap = rows[3][block_terms]
    require(block_cap == 112, block_cap)

    fixed_terms = 17
    outside_terms = fixed_terms - block_terms
    projected_capacity = outside_terms * comb(8, 3) + block_cap
    require(projected_capacity == 784, projected_capacity)

    outer = ExactProductShadow(8, 4)
    last_good, first_bad = outer.transition(projected_capacity)
    require(
        (
            last_good.family_size,
            last_good.shadow_size,
            first_bad.family_size,
            first_bad.shadow_size,
        )
        == (560, 784, 561, 793),
        (last_good, first_bad),
    )

    target, one_term, _ = first_koszul_data(8, 4)
    numerator = target - 64 * last_good.family_size
    residual = -(-numerator // one_term)
    require(
        (target, one_term, residual) == (310_464, 4_424, 63),
        (target, one_term, numerator, residual),
    )
    total = fixed_terms + residual
    require(total == 80, total)

    return {
        "fixed_terms": fixed_terms,
        "block_terms": block_terms,
        "five_term_cubic_cap": block_cap,
        "projected_first_shadow_capacity": projected_capacity,
        "outer_intersection_cap": last_good.family_size,
        "residual_terms": residual,
        "ordinary_lower_bound": total,
    }


def build_payload() -> dict[str, Any]:
    rows7 = derivative_tower_capacities(7, 3, 5)
    rows8 = derivative_tower_capacities(8, 3, 5)

    expected7 = {
        1: [0, 7, 14, 21, 28, 35],
        2: [0, 3, 22, 43, 64, 85],
        3: [0, 0, 4, 17, 40, 64],
    }
    expected8 = {
        1: [0, 8, 16, 24, 32, 40],
        2: [0, 6, 34, 62, 90, 118],
        3: [0, 0, 10, 40, 80, 112],
    }
    require(rows7 == expected7, rows7)
    require(rows8 == expected8, rows8)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_DERIVATIVE_TOWER_CAPACITY_PROOF_DRAFT",
            "EXACT_INTEGER_REPLAYED",
            "PERM7_LOWER_46",
        ],
        "theorem": {
            "base": "B_(n,1)(q)=min(n^2,q*n)",
            "adjacent_shadow": (
                "B_(n,d)(q) <= Gamma_(n,d)(B_(n,d-1)(q))"
            ),
            "block_projection": (
                "B_(n,d)(q) <= (q-s)*binom(n,d)+B_(n,d)(s)"
            ),
            "literal_cap": (
                "B_(n,d)(q) <= min(binom(n,d)^2,q*binom(n,d))"
            ),
        },
        "n7_capacity_rows": {str(key): value for key, value in rows7.items()},
        "n7_application": perm7_application(rows7),
        "n8_capacity_rows": {str(key): value for key, value in rows8.items()},
        "n8_regression": perm8_regression(rows8),
        "claim_boundary": (
            "The adjacent recursive theorem is valid for arbitrary n, "
            "derivative degree and block size. The finite rows prove the "
            "ordinary bound perm_7>=46 and reproduce perm_8>=80. They do not "
            "prove exact rank, border rank, asymptotic Glynn optimality or "
            "that scalar derivative-shadow capacities alone reach 2^(n-1)."
        ),
    }
    return {**core, "core_sha256": canonical_sha256(core)}


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
    print("GENERAL_DERIVATIVE_TOWER_CAPACITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
