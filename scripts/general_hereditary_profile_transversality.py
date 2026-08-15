#!/usr/bin/env python3
"""Replay hereditary derivative-profile transversality refinements.

For every nonzero f in D_d(perm_n), every degree-j derivative space has
size at least C(d,j)^2.  A block of s Chow terms can therefore meet that
permanent derivative space only if

    s*C(n,j) >= C(d,j)^2

for every j.  The pure theorem is proved in
``docs/general_hereditary_profile_transversality.md``.  This script checks the
resulting exact certificate arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
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


def profile_safe_omission(n: int, derivative_degree: int) -> dict[str, int]:
    """Best safe block size certified by one lower derivative degree."""

    require(n >= 2, n)
    require(2 <= derivative_degree <= n, (n, derivative_degree))
    candidates = []
    for output_degree in range(1, derivative_degree):
        permanent_minimum = comb(derivative_degree, output_degree) ** 2
        one_term_cap = comb(n, output_degree)
        safe = (permanent_minimum - 1) // one_term_cap
        candidates.append(
            {
                "safe_terms": safe,
                "witness_output_degree": output_degree,
                "permanent_minimum": permanent_minimum,
                "one_term_cap": one_term_cap,
            }
        )
    best = max(
        candidates,
        key=lambda row: (row["safe_terms"], -row["witness_output_degree"]),
    )
    require(
        best["safe_terms"] * best["one_term_cap"]
        < best["permanent_minimum"],
        best,
    )
    return best


def hereditary_profile_rows(max_degree: int = 8) -> list[dict[str, object]]:
    rows = []
    for degree in range(2, max_degree + 1):
        profile = [comb(degree, output) ** 2 for output in range(degree + 1)]
        require(profile[0] == profile[-1] == 1, (degree, profile))
        require(profile[1] == profile[-2] == degree**2, (degree, profile))
        rows.append(
            {
                "degree": degree,
                "derivative_profile": profile,
                "total_profile_sum": sum(profile),
            }
        )
    return rows


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
    numerator = (
        int(certificate["permanent_koszul_rank"])
        - n * n * int(certificate["complementary_intersection_cap"])
    )
    require(numerator > 0, (n, numerator))
    return ceil_div(numerator, int(certificate["chow_term_koszul_cap"]))


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
        witness = profile_safe_omission(n, derivative_degree)
        saving = witness["safe_terms"]
        require(saving >= 1, (n, derivative_degree, witness))

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
                "intersection_degree": derivative_degree,
                "profile_witness_degree": witness["witness_output_degree"],
                "profile_permanent_minimum": witness["permanent_minimum"],
                "profile_one_term_cap": witness["one_term_cap"],
                "safe_omitted_terms": saving,
                "old_fixed_terms": old_fixed,
                "new_fixed_terms": new_fixed,
                "unchanged_shadow_threshold": old_threshold,
                "unchanged_intersection_cap": int(
                    raw["complementary_intersection_cap"]
                ),
                "residual_terms": residual,
                "former_lower_bound": old_lower,
                "hereditary_profile_lower_bound": improved,
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
        15: 6883,
        16: 13315,
    }
    require(
        {int(row["n"]): int(row["hereditary_profile_lower_bound"]) for row in rows}
        == expected,
        rows,
    )
    return rows


def exact_shadow_rows() -> list[dict[str, object]]:
    payload = load_json(EXACT_SHADOW)
    expected = {7: 43, 8: 78}
    rows: list[dict[str, object]] = []
    for n, key in ((7, "n7_application"), (8, "n8_application")):
        raw = payload.get(key)
        require(isinstance(raw, dict), key)
        derivative_degree = int(raw["complement_degree"]) - 1
        witness = profile_safe_omission(n, derivative_degree)
        saving = witness["safe_terms"]
        require(saving == 1, (n, witness))

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
        cap = int(raw["exact_intersection_cap"])
        residual = ceil_div(
            target_rank - n * n * cap,
            int(raw["one_term_koszul_cap"]),
        )
        require(residual == int(raw["residual_term_count"]), (n, residual, raw))
        improved = new_fixed + residual
        require(improved == expected[n], (n, improved))
        require(new_fixed <= int(raw["global_first_koszul_bound"]), raw)

        rows.append(
            {
                "n": n,
                "intersection_degree": derivative_degree,
                "profile_witness_degree": witness["witness_output_degree"],
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
                "hereditary_profile_exact_shadow_bound": improved,
            }
        )
    return rows


def asymptotic_diagnostics() -> list[dict[str, int]]:
    rows = []
    for n in (16, 20, 24, 32, 40, 50, 64):
        complement = n // 2 if n % 2 == 0 else (n + 1) // 2
        derivative_degree = complement - 1
        witness = profile_safe_omission(n, derivative_degree)
        rows.append(
            {
                "n": n,
                "intersection_degree": derivative_degree,
                **witness,
            }
        )
    expected = {16: 3, 20: 6, 24: 13, 32: 51, 40: 205, 50: 1199, 64: 14757}
    require({row["n"]: row["safe_terms"] for row in rows} == expected, rows)
    return rows


def build_payload() -> dict[str, object]:
    core = {
        "status": [
            "GENERAL_HEREDITARY_PERMANENT_PROFILE",
            "MULTITERM_PROFILE_TRANSVERSALITY",
            "PERM7_LOWER_43",
            "PERM8_LOWER_78",
            "PERM15_GENERAL_BOUND_6883",
        ],
        "theorem": {
            "hereditary_profile": (
                "For every nonzero f in D_d(perm_n), "
                "dim D_j(f) >= binom(d,j)^2 for all 0<=j<=d."
            ),
            "block_transversality": (
                "If s*binom(n,j) < binom(d,j)^2 for some j, then "
                "D_d(perm_n) intersects the sum of the degree-d derivative "
                "spaces of those s Chow terms trivially."
            ),
            "safe_omission_count": (
                "max_(1<=j<d) floor((binom(d,j)^2-1)/binom(n,j))"
            ),
        },
        "finite_basis_profiles": hereditary_profile_rows(),
        "general_certificate_refinements": general_certificate_rows(),
        "exact_product_shadow_refinements": exact_shadow_rows(),
        "asymptotic_diagnostics": asymptotic_diagnostics(),
        "asymptotic_statement": (
            "At central derivative degree, choosing j near "
            "((1-1/sqrt(2))/2)*n gives a safe block of order "
            "((1+sqrt(2))/2)^n/sqrt(n)."
        ),
        "claim_boundary": (
            "This theorem refines ordinary multishadow bounds. It does not "
            "determine perm_7, perm_8, or general perm_n exactly, prove a "
            "border-rank improvement, or settle unrestricted perm_6. "
            "Literature novelty is not claimed."
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
    print("GENERAL_HEREDITARY_PROFILE_TRANSVERSALITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
