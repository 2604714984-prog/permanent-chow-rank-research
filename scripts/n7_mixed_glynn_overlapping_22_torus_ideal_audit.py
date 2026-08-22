#!/usr/bin/env python3
"""Repair the overlapping-(2,2) dense-torus common-minor argument exactly."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json"
r, t, z = sp.symbols("r t z")
ROW_STATUS = "EXACT_LAURENT_UNIVARIATE_BEZOUT_EMPTY_TORUS_ZERO_SET"


def laurent_univariate_reduction(expression):
    polynomial = sp.Poly(sp.sympify(expression), r, t, domain=sp.QQ)
    terms = polynomial.terms()
    if not terms:
        raise ValueError("zero determinant cannot cover the torus")
    minimum_r = min(exponents[0] for exponents, _coefficient in terms)
    minimum_t = min(exponents[1] for exponents, _coefficient in terms)
    residual = 0
    for (r_exponent, t_exponent), coefficient in terms:
        shifted_r = r_exponent - minimum_r
        shifted_t = t_exponent - minimum_t
        if shifted_r != shifted_t:
            raise ValueError(
                "residual determinant does not factor through z=r*t"
            )
        residual += coefficient * z**shifted_r
    residual_polynomial = sp.Poly(residual, z, domain=sp.QQ).monic()
    return (minimum_r, minimum_t), residual_polynomial


def audit_row(row):
    reductions = []
    residual_gcd = None
    for minor in row["minors"]:
        monomial_exponents, residual = laurent_univariate_reduction(
            minor["determinant_factorization"]
        )
        residual_gcd = (
            residual
            if residual_gcd is None
            else sp.gcd(residual_gcd, residual).monic()
        )
        reductions.append(
            {
                "selection_point": minor["selection_point"],
                "torus_monomial_exponents_r_t": list(monomial_exponents),
                "residual_in_z_equals_r_times_t": str(residual.as_expr()),
            }
        )
    if residual_gcd is None or residual_gcd.degree() != 0:
        raise AssertionError(
            f"nonempty residual common-root candidate at {row['support']} "
            f"split {row['identity_count']}: {residual_gcd}"
        )
    return {
        "support": row["support"],
        "identity_count": row["identity_count"],
        "minor_count": row["minor_count"],
        "reductions": reductions,
        "residual_gcd_over_Q_z": "1",
        "status": ROW_STATUS,
    }


def build_payload():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    if source["status"] != "EXACT_ALL_OVERLAPPING_22_NILPOTENT_SHEAR_INVALID_TAIL_MINORS":
        raise AssertionError("unexpected source certificate status")
    rows = [audit_row(row) for row in source["rows"]]
    multi_minor_count = sum(row["minor_count"] > 1 for row in rows)
    if len(rows) != 75 or multi_minor_count != 56:
        raise AssertionError("unexpected overlapping-(2,2) inventory")
    return {
        "schema_version": 1,
        "status": "EXACT_ALL_OVERLAPPING_22_NILPOTENT_SHEAR_TORUS_IDEAL_AUDITED",
        "field": "characteristic zero",
        "source_certificate": SOURCE.relative_to(ROOT).as_posix(),
        "candidate_count": len(rows),
        "single_minor_row_count": len(rows) - multi_minor_count,
        "multi_minor_row_count": multi_minor_count,
        "torus_coordinates": ["r", "t"],
        "univariate_coordinate": "z=r*t",
        "proof_method": (
            "Remove the invertible Laurent monomial from every saved exact "
            "minor, verify that each residual lies in Q[r*t], and compute the "
            "exact univariate gcd. Gcd 1 in Q[z] is a Bezout certificate that "
            "the residual minors have no common complex root."
        ),
        "rows": rows,
        "claim_boundary": [
            "This audit repairs the dense-torus common-zero inference for all 75 rows of the coincident overlapping-(2,2) nilpotent family.",
            "It uses the saved exact determinant factorizations; it does not infer torus emptiness from a multivariate gcd alone.",
            "The result does not audit the higher-parameter overlap-two certificates and does not prove ordinary lower 50, exact rank 64, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
