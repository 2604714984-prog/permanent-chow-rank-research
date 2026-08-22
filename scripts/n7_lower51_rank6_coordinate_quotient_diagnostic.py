#!/usr/bin/env python3
"""Exact-Q coordinate-quotient diagnostic for rank-six normal forms.

This computes the two unquotiented local polarization ranks (R=0) on every
coordinate quotient of every support normal form.  It is a bounded diagnostic,
not the arbitrary-orientation R6 surplus atlas required by v7.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from sympy import Matrix

from n7_rank6_normal_form_profiles import catalectic_rows, compositions


VARIABLES = 6


def derivative_space_basis(support_size: int, degree: int) -> tuple[tuple[tuple[int, ...], ...], Matrix]:
    rows, _, _ = catalectic_rows(support_size, degree)
    matrix = Matrix(rows)
    _, independent_rows = matrix.T.rref()
    basis = Matrix([list(matrix.row(index)) for index in independent_rows])
    monomials = compositions(degree, VARIABLES)
    assert basis.rank() == len(independent_rows)
    return monomials, basis


def polarization_rank(monomials: tuple[tuple[int, ...], ...], basis: Matrix, active: tuple[int, ...]) -> int:
    target = compositions(sum(monomials[0]) - 1, VARIABLES)
    target_index = {monomial: index for index, monomial in enumerate(target)}
    image_rows = []
    for source_row in range(basis.rows):
        image = [0] * (len(active) * len(target))
        for source_column, exponent in enumerate(monomials):
            coefficient = basis[source_row, source_column]
            if not coefficient:
                continue
            for block, variable in enumerate(active):
                if not exponent[variable]:
                    continue
                child = list(exponent)
                child[variable] -= 1
                column = block * len(target) + target_index[tuple(child)]
                image[column] += coefficient * exponent[variable]
        image_rows.append(image)
    return Matrix(image_rows).rank()


def support_row(support_size: int) -> dict:
    monomials4, basis4 = derivative_space_basis(support_size, 4)
    monomials3, basis3 = derivative_space_basis(support_size, 3)
    middle = basis3.rows
    delta = 35 - middle
    quotient_rows = []
    for quotient_rank in range(VARIABLES + 1):
        witnesses = []
        for active in itertools.combinations(range(VARIABLES), quotient_rank):
            plus = polarization_rank(monomials4, basis4, active) if active else 0
            minus = polarization_rank(monomials3, basis3, active) if active else 0
            witnesses.append((plus + minus + delta - 10 * quotient_rank, active, plus, minus))
        best = min(witnesses)
        quotient_rows.append(
            {
                "quotient_rank": quotient_rank,
                "minimum_R0_surplus": best[0],
                "active_coordinates": list(best[1]),
                "plus_rank": best[2],
                "minus_rank": best[3],
            }
        )
    return {
        "support_size": support_size,
        "middle_dimension": middle,
        "delta": delta,
        "quotient_rows": quotient_rows,
    }


def build() -> dict:
    rows = [support_row(support) for support in range(1, 7)]
    assert sum(len(row["quotient_rows"]) for row in rows) == 42
    return {
        "schema_version": 1,
        "field": "Q",
        "candidate_coordinate_quotients": 6 * (2**VARIABLES),
        "claim": (
            "Exact ranks of the unquotiented plus/minus symbols on all coordinate "
            "quotients of all six rank-six normal forms."
        ),
        "claim_boundary": (
            "R is fixed to zero and quotient orientations are coordinate in the "
            "normal-form frame. The rows do not prove arbitrary-orientation surplus "
            "floors and are not used to close a v7 packet branch."
        ),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    summary = {
        row["support_size"]: [
            cell["minimum_R0_surplus"] for cell in row["quotient_rows"]
        ]
        for row in payload["rows"]
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("N7_LOWER51_RANK6_COORDINATE_QUOTIENT_DIAGNOSTIC_PASS")


if __name__ == "__main__":
    main()
