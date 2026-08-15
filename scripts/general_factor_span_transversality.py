#!/usr/bin/env python3
"""Replay the factor-span transversality refinement of multishadow bounds.

The mathematical theorem is proved in
``docs/general_factor_span_transversality.md``.  This script checks the finite
consequences against the repository's frozen multishadow and exact
product-shadow certificates.

All arithmetic is exact integer arithmetic.  No finite-field or random result
carries theorem responsibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import permutations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MULTISHADOW = ROOT / "data" / "multishadow_bounds.json"
EXACT_SHADOW = ROOT / "data" / "general_exact_product_shadow.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def safe_omission_count(n: int, derivative_degree: int) -> int:
    """Largest s with s*n < derivative_degree**2."""

    require(n >= 2, n)
    require(2 <= derivative_degree <= n, (n, derivative_degree))
    value = (derivative_degree * derivative_degree - 1) // n
    require(value * n < derivative_degree * derivative_degree, value)
    require((value + 1) * n >= derivative_degree * derivative_degree, value)
    return value


def verify_perfect_matching_union(max_degree: int = 8) -> dict[str, int]:
    """Finite sanity check for the support lemma used in the pure proof."""

    checked_cells = 0
    checked_matchings = 0
    for degree in range(2, max_degree + 1):
        used: set[tuple[int, int]] = set()
        count = 0
        for permutation in permutations(range(degree)):
            count += 1
            for row, column in enumerate(permutation):
                used.add((row, column))
        require(len(used) == degree * degree, (degree, len(used)))
        require(count > 0, degree)
        checked_cells += len(used)
        checked_matchings += count
    return {
        "maximum_degree": max_degree,
        "checked_cells": checked_cells,
        "checked_matchings": checked_matchings,
    }


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def recompute_residual(certificate: dict[str, object]) -> int:
    n = int(certificate["n"])
    target_rank = int(certificate["permanent_koszul_rank"])
    cap = int(certificate["complementary_intersection_cap"])
    one_term_cap = int(certificate["chow_term_koszul_cap"])
    numerator = target_rank - n * n * cap
    require(numerator > 0, (n, numerator))
    return ceil_div(numerator, one_term_cap)


def general_certificate_rows() -> list[dict[str, object]]:
    payload = load_json(MULTISHADOW)
    certificates = payload.get("certificates")
    require(isinstance(certificates, list), "missing multishadow certificates")
    rows: list[dict[str, object]] = []
    for raw in certificates:
        require(isinstance(raw, dict), raw)
        n = int(raw["n"])
        if n < 7 or n > 16:
            continue
        complement = int(raw["complementary_degree"])
        derivative_degree = complement - 1
        saving = safe_omission_count(n, derivative_degree)
        require(saving >= 1, (n, derivative_degree, saving))

        old_fixed = int(raw["fixed_terms"])
        new_fixed = old_fixed + saving
        global_bound = int(raw["global_koszul_bound"])
        require(new_fixed <= global_bound, (n, new_fixed, global_bound))

        old_threshold = old_fixed * comb(n, derivative_degree)
        new_threshold = (new_fixed - saving) * comb(n, derivative_degree)
        require(old_threshold == new_threshold, (n, old_threshold, new_threshold))

        residual = recompute_residual(raw)
        require(residual == int(raw["residual_term_count"]), (n, residual, raw))
        old_lower = int(raw["lower_bound"])
        require(old_fixed + residual == old_lower, (n, old_fixed, residual, old_lower))
        improved = new_fixed + residual
        require(improved == old_lower + saving, (n, improved, old_lower, saving))

        rows.append(
            {
                "n": n,
                "output_degree": int(raw["output_degree"]),
                "complementary_degree": complement,
                "shadow_degree": derivative_degree,
                "safe_omitted_terms": saving,
                "factor_span_dimension_cap": saving * n,
                "square_support_requirement": derivative_degree**2,
                "old_fixed_terms": old_fixed,
                "new_fixed_terms": new_fixed,
                "unchanged_shadow_threshold": old_threshold,
                "unchanged_intersection_cap": int(
                    raw["complementary_intersection_cap"]
                ),
                "residual_terms": residual,
                "former_lower_bound": old_lower,
                "factor_span_refined_lower_bound": improved,
                "global_first_koszul_bound": global_bound,
            }
        )

    require([row["n"] for row in rows] == list(range(7, 17)), rows)
    expected = {
        7: 42,
        8: 77,
        9: 142,
        10: 268,
        11: 508,
        12: 970,
        13: 1855,
        14: 3570,
        15: 6882,
        16: 13315,
    }
    require(
        {int(row["n"]): int(row["factor_span_refined_lower_bound"]) for row in rows}
        == expected,
        rows,
    )
    return rows


def exact_shadow_rows() -> list[dict[str, object]]:
    payload = load_json(EXACT_SHADOW)
    rows: list[dict[str, object]] = []
    expected = {7: 43, 8: 78}
    for n, key in ((7, "n7_application"), (8, "n8_application")):
        raw = payload.get(key)
        require(isinstance(raw, dict), key)
        complement = int(raw["complement_degree"])
        derivative_degree = complement - 1
        saving = safe_omission_count(n, derivative_degree)
        require(saving == 1, (n, saving))

        old_fixed = int(raw["fixed_term_count"])
        new_fixed = old_fixed + saving
        threshold = int(raw["derivative_shadow_threshold"])
        require(
            threshold == (new_fixed - saving) * comb(n, derivative_degree),
            (n, threshold, new_fixed, saving),
        )
        require(
            int(raw["shadow_at_cap"]) <= threshold
            < int(raw["shadow_at_first_excluded_size"]),
            raw,
        )

        target_rank = int(raw["first_koszul_target_rank"])
        one_term_cap = int(raw["one_term_koszul_cap"])
        cap = int(raw["exact_intersection_cap"])
        residual = ceil_div(target_rank - n * n * cap, one_term_cap)
        require(residual == int(raw["residual_term_count"]), (n, residual, raw))
        improved = new_fixed + residual
        require(improved == expected[n], (n, improved))
        require(new_fixed <= int(raw["global_first_koszul_bound"]), raw)

        rows.append(
            {
                "n": n,
                "output_degree": int(raw["output_degree"]),
                "complementary_degree": complement,
                "shadow_degree": derivative_degree,
                "safe_omitted_terms": saving,
                "old_fixed_terms": old_fixed,
                "new_fixed_terms": new_fixed,
                "shadow_threshold": threshold,
                "exact_intersection_cap": cap,
                "shadow_at_cap": int(raw["shadow_at_cap"]),
                "first_excluded_size": int(raw["first_excluded_size"]),
                "shadow_at_first_excluded_size": int(
                    raw["shadow_at_first_excluded_size"]
                ),
                "residual_terms": residual,
                "former_exact_shadow_bound": int(
                    raw["exact_multishadow_lower_bound"]
                ),
                "factor_span_exact_shadow_bound": improved,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    finite_support_check = verify_perfect_matching_union()
    general_rows = general_certificate_rows()
    exact_rows = exact_shadow_rows()
    core = {
        "status": [
            "GENERAL_SUBSQUARE_FACTOR_SPAN_TRANSVERSALITY",
            "MULTITERM_OMITTED_FACTOR_PROJECTION",
            "PERM7_LOWER_43",
            "PERM8_LOWER_78",
        ],
        "theorem": {
            "single_subspace": (
                "If dim(L)<d^2, then D_d(perm_n) intersect Sym^d(L)=0."
            ),
            "chow_block": (
                "If s*n<d^2, the degree-d derivative spaces of any s "
                "degree-n Chow terms have sum disjoint from D_d(perm_n)."
            ),
            "projection_cap": (
                "For q fixed terms and s*n<d^2, "
                "dim(D_d(perm_n) intersect sum_i D_d(T_i)) "
                "<= (q-s)*binom(n,d)."
            ),
            "safe_omission_count": "floor((d^2-1)/n)",
        },
        "finite_support_sanity_check": finite_support_check,
        "general_certificate_refinements": general_rows,
        "exact_product_shadow_refinements": exact_rows,
        "central_asymptotic_saving": (
            "For the reviewed central/lower-central complementary degree, "
            "the number of terms saved is n/4+O(1)."
        ),
        "claim_boundary": (
            "The theorem improves ordinary multishadow lower bounds and "
            "does not determine perm_7, perm_8, or general perm_n exactly. "
            "It gives no border-rank improvement and no exact unrestricted "
            "perm_6 conclusion. Literature novelty is not claimed."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


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
    print("GENERAL_FACTOR_SPAN_TRANSVERSALITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
