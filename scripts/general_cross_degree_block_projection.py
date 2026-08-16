#!/usr/bin/env python3
"""Cross-degree block projection for permanent derivative spaces.

The exact product-shadow theorem gives the minimum derivative shadow of an
arbitrary subspace of ``D_m(perm_n)``.  This audit combines that theorem with
a section/projection argument one derivative degree lower.

The resulting exact caps prove the ordinary characteristic-zero bounds

    ChowRank(perm_7) >= 45,
    ChowRank(perm_8) >= 80.

The mathematical proof is in
``docs/general_cross_degree_block_projection.md``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path

from general_exact_product_shadow import ExactProductShadow, first_koszul_data

EXPECTED_CORE_SHA256 = (
    "420bd48a269af15eccdba064f76338823708a98f1aab1af550a68e19976a0cf6"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def transition(n: int, degree: int, threshold: int) -> dict[str, int]:
    shadow = ExactProductShadow(n, degree)
    last_good, first_bad = shadow.transition(threshold)
    return {
        "cap": last_good.family_size,
        "shadow_at_cap": last_good.shadow_size,
        "first_excluded_size": first_bad.family_size,
        "shadow_at_first_excluded": first_bad.shadow_size,
    }


def block_certificate(
    *,
    n: int,
    upper_degree: int,
    terms: int,
) -> dict[str, int]:
    """One-step cross-degree cap using first derivatives.

    A single degree-``upper_degree-1`` Chow derivative space is supported on
    at most ``n`` essential variables.  The exact shadow cap at the lower
    degree is projected through the remaining ``terms-1`` literal summands,
    and the exact shadow is inverted again at the upper degree.
    """

    lower_degree = upper_degree - 1
    require(lower_degree >= 2, (n, upper_degree))

    single = transition(n, lower_degree, n)
    one_term_lower_dimension = comb(n, lower_degree)
    projected_capacity = (
        (terms - 1) * one_term_lower_dimension + single["cap"]
    )
    upper = transition(n, upper_degree, projected_capacity)

    return {
        "n": n,
        "upper_degree": upper_degree,
        "derivative_order": 1,
        "lower_degree": lower_degree,
        "terms": terms,
        "single_term_lower_cap": single["cap"],
        "single_term_shadow_at_cap": single["shadow_at_cap"],
        "single_term_first_excluded_size": single["first_excluded_size"],
        "single_term_shadow_at_first_excluded": (
            single["shadow_at_first_excluded"]
        ),
        "lower_degree_projected_capacity": projected_capacity,
        "upper_block_cap": upper["cap"],
        "upper_shadow_at_cap": upper["shadow_at_cap"],
        "upper_first_excluded_size": upper["first_excluded_size"],
        "upper_shadow_at_first_excluded": upper["shadow_at_first_excluded"],
    }


def lower_bound_application(
    *,
    n: int,
    output_degree: int,
    fixed_terms: int,
    block: dict[str, int],
) -> dict[str, int]:
    complement_degree = n - output_degree
    shadow_degree = complement_degree - 1
    require(block["upper_degree"] == shadow_degree, (block, shadow_degree))

    block_terms = block["terms"]
    outside_terms = fixed_terms - block_terms
    outside_capacity = outside_terms * comb(n, shadow_degree)
    projected_capacity = outside_capacity + block["upper_block_cap"]

    outer = transition(n, complement_degree, projected_capacity)
    target, one_term, _ = first_koszul_data(n, output_degree)
    residual_numerator = target - n * n * outer["cap"]
    require(residual_numerator > 0, residual_numerator)
    residual_terms = ceil_div(residual_numerator, one_term)

    return {
        "output_degree": output_degree,
        "complement_degree": complement_degree,
        "fixed_terms": fixed_terms,
        "block_terms": block_terms,
        "outside_terms": outside_terms,
        "outside_cubic_capacity": outside_capacity,
        "block_cap": block["upper_block_cap"],
        "projected_first_shadow_capacity": projected_capacity,
        "outer_intersection_cap": outer["cap"],
        "outer_shadow_at_cap": outer["shadow_at_cap"],
        "outer_first_excluded_size": outer["first_excluded_size"],
        "outer_shadow_at_first_excluded": outer["shadow_at_first_excluded"],
        "first_koszul_target_rank": target,
        "one_term_koszul_cap": one_term,
        "residual_rank_numerator": residual_numerator,
        "residual_terms": residual_terms,
        "ordinary_lower_bound": fixed_terms + residual_terms,
    }


def build_payload() -> dict[str, object]:
    n7_block = block_certificate(n=7, upper_degree=3, terms=4)
    require(
        (
            n7_block["single_term_lower_cap"],
            n7_block["single_term_shadow_at_cap"],
            n7_block["single_term_first_excluded_size"],
            n7_block["single_term_shadow_at_first_excluded"],
        )
        == (3, 6, 4, 8),
        n7_block,
    )
    require(
        (
            n7_block["lower_degree_projected_capacity"],
            n7_block["upper_block_cap"],
            n7_block["upper_shadow_at_cap"],
            n7_block["upper_first_excluded_size"],
            n7_block["upper_shadow_at_first_excluded"],
        )
        == (66, 41, 66, 42, 69),
        n7_block,
    )

    n7_application = lower_bound_application(
        n=7,
        output_degree=3,
        fixed_terms=17,
        block=n7_block,
    )
    require(
        (
            n7_application["projected_first_shadow_capacity"],
            n7_application["outer_intersection_cap"],
            n7_application["outer_shadow_at_cap"],
            n7_application["outer_first_excluded_size"],
            n7_application["outer_shadow_at_first_excluded"],
            n7_application["residual_rank_numerator"],
            n7_application["residual_terms"],
            n7_application["ordinary_lower_bound"],
        )
        == (496, 263, 494, 264, 497, 45_913, 28, 45),
        n7_application,
    )

    n8_block = block_certificate(n=8, upper_degree=3, terms=5)
    require(
        (
            n8_block["single_term_lower_cap"],
            n8_block["single_term_shadow_at_cap"],
            n8_block["single_term_first_excluded_size"],
            n8_block["single_term_shadow_at_first_excluded"],
        )
        == (6, 8, 7, 9),
        n8_block,
    )
    require(
        (
            n8_block["lower_degree_projected_capacity"],
            n8_block["upper_block_cap"],
            n8_block["upper_shadow_at_cap"],
            n8_block["upper_first_excluded_size"],
            n8_block["upper_shadow_at_first_excluded"],
        )
        == (118, 112, 118, 113, 120),
        n8_block,
    )

    n8_application = lower_bound_application(
        n=8,
        output_degree=4,
        fixed_terms=17,
        block=n8_block,
    )
    require(
        (
            n8_application["projected_first_shadow_capacity"],
            n8_application["outer_intersection_cap"],
            n8_application["outer_shadow_at_cap"],
            n8_application["outer_first_excluded_size"],
            n8_application["outer_shadow_at_first_excluded"],
            n8_application["residual_rank_numerator"],
            n8_application["residual_terms"],
            n8_application["ordinary_lower_bound"],
        )
        == (784, 560, 784, 561, 793, 274_624, 63, 80),
        n8_application,
    )

    next_shadow = ExactProductShadow(8, 4).minimum(773).shadow_size
    require(next_shadow == 987, next_shadow)

    core = {
        "status": [
            "GENERAL_CROSS_DEGREE_BLOCK_PROJECTION",
            "PERM7_FOUR_TERM_CAP_41",
            "PERM8_FIVE_TERM_CAP_112",
            "PERM7_ORDINARY_LOWER_45",
            "PERM8_ORDINARY_LOWER_80",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "single_term_lower_degree_cap": (
                "c(n,e)=max{b:F^(e-1)_(n,e)(b)<=n}"
            ),
            "lower_degree_projection": (
                "dim(E_e intersect sum_{i=1}^q D_e(T_i)) "
                "<= (q-1)*binom(n,e)+c(n,e)"
            ),
            "cross_degree_transfer": (
                "dim(E_d intersect sum_i D_d(T_i)) "
                "<= max{b:F^a_(n,d)(b)<=lower_degree_projection}"
            ),
        },
        "n7_block": n7_block,
        "n7_application": n7_application,
        "n8_block": n8_block,
        "n8_application": n8_application,
        "next_interface": {
            "perm8_sufficient_five_term_cap_for_lower81": 90,
            "fixed_terms": 21,
            "outside_terms": 16,
            "maximum_projected_capacity": 986,
            "required_outer_cap_at_most": 772,
            "first_excluded_outer_size": 773,
            "first_excluded_outer_shadow": next_shadow,
        },
        "claim_boundary": (
            "The block caps concern literal sums of derivative spaces. "
            "They apply to an actual coupled polynomial sum only through "
            "containment. The result proves ordinary lower bounds 45 and 80 "
            "for perm_7 and perm_8. It does not determine exact rank, improve "
            "border rank, or prove general Glynn optimality."
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
    print("GENERAL_CROSS_DEGREE_BLOCK_PROJECTION_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
