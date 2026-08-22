#!/usr/bin/env python3
"""Exact Laurent-torus audit for overlapping (2,3)/(3,2) nilpotent minors."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json"
r, t, w, z = sp.symbols("r t w z")
ROW_STATUS = "EXACT_LAURENT_UNIVARIATE_BEZOUT_EMPTY_TORUS_ZERO_SET"


def laurent_univariate_reduction(expression):
    polynomial = sp.Poly(sp.sympify(expression), r, t, w, domain=sp.QQ)
    terms = polynomial.terms()
    if not terms:
        raise ValueError("zero determinant cannot cover the torus")
    minima = tuple(
        min(exponents[index] for exponents, _coefficient in terms)
        for index in range(3)
    )
    residual = 0
    for exponents, coefficient in terms:
        shifted = tuple(value - minimum for value, minimum in zip(exponents, minima))
        if shifted[0] != shifted[1] or shifted[2] != 0:
            raise ValueError(
                "residual determinant does not factor through z=r*t"
            )
        residual += coefficient * z**shifted[0]
    return minima, sp.Poly(residual, z, domain=sp.QQ).monic()


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
                "torus_monomial_exponents_r_t_w": list(monomial_exponents),
                "residual_in_z_equals_r_times_t": str(residual.as_expr()),
            }
        )
    if residual_gcd is None or residual_gcd.degree() != 0:
        raise AssertionError(
            f"nonempty residual common-root candidate at {row['core_support']} "
            f"extra {row['extra_coordinate']} split {row['identity_count']}"
        )
    return {
        "shape": row["shape"],
        "core_support": row["core_support"],
        "extra_coordinate": row["extra_coordinate"],
        "identity_count": row["identity_count"],
        "minor_count": row["minor_count"],
        "reductions": reductions,
        "residual_gcd_over_Q_z": "1",
        "status": ROW_STATUS,
    }


def build_payload():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    if source["status"] != "EXACT_ALL_OVERLAPPING_23_32_NILPOTENT_SHEAR_INVALID_TAIL_MINORS":
        raise AssertionError("unexpected source certificate status")
    rows = [audit_row(row) for row in source["rows"]]
    multi_minor_count = sum(row["minor_count"] > 1 for row in rows)
    if len(rows) != 600 or multi_minor_count != 330:
        raise AssertionError("unexpected overlapping-(2,3)/(3,2) inventory")
    return {
        "schema_version": 1,
        "status": "EXACT_ALL_OVERLAPPING_23_32_NILPOTENT_SHEAR_TORUS_IDEAL_AUDITED",
        "field": "characteristic zero",
        "source_certificate": SOURCE.relative_to(ROOT).as_posix(),
        "candidate_count": len(rows),
        "single_minor_row_count": len(rows) - multi_minor_count,
        "multi_minor_row_count": multi_minor_count,
        "torus_coordinates": ["r", "t", "w"],
        "univariate_coordinate": "z=r*t",
        "proof_method": (
            "Remove the invertible Laurent monomial, verify that w disappears "
            "from every residual and that the residual lies in Q[r*t], then "
            "compute the exact univariate gcd. Gcd 1 supplies the Bezout "
            "certificate for an empty common zero set on the torus."
        ),
        "rows": rows,
        "claim_boundary": [
            "This audit repairs the dense-torus common-zero inference for all 600 overlapping (2,3)/(3,2) nilpotent rows.",
            "It uses saved exact determinant factorizations and does not infer torus emptiness from a multivariate gcd alone.",
            "It does not audit higher-parameter overlap-two certificates and does not prove ordinary lower 50, exact rank 64, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
