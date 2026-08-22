#!/usr/bin/env python3
"""Exact symbolic rank-five binary-tail catalectic classification."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import Matrix, factor, symbols


sys.path.insert(0, str(Path(__file__).resolve().parent))
from n7_rank6_normal_form_profiles import compositions  # noqa: E402


def catalectic_matrix() -> tuple[Matrix, object, object, object]:
    a, b, c = symbols("a b c")
    # x0*x1*x2*x3*x4 * (a*x0^2 + c*x0*x1 + b*x1^2)
    terms = {
        (3, 1, 1, 1, 1): a,
        (2, 2, 1, 1, 1): c,
        (1, 3, 1, 1, 1): b,
    }
    derivatives = compositions(3, 5)
    targets = compositions(4, 5)
    target_index = {monomial: index for index, monomial in enumerate(targets)}
    rows = []
    for alpha in derivatives:
        row = [0] * len(targets)
        for exponent, coefficient in terms.items():
            beta = tuple(exponent[k] - alpha[k] for k in range(5))
            if min(beta) < 0:
                continue
            value = coefficient
            for k in range(5):
                for offset in range(alpha[k]):
                    value *= exponent[k] - offset
            row[target_index[beta]] += value
        rows.append(row)
    return Matrix(rows), a, b, c


def binary_middle_matrix(a: object, b: object, c: object) -> Matrix:
    """Second-derivative catalectic of a*x^3*y+c*x^2*y^2+b*x*y^3."""
    return Matrix(
        [
            [0, 6 * a, 2 * c],
            [3 * a, 4 * c, 3 * b],
            [2 * c, 6 * b, 0],
        ]
    )


def build() -> dict:
    matrix, a, b, c = catalectic_matrix()
    diagonal_rank = matrix.subs(c, 0).rank()
    cross_rank = matrix.subs({a: 0, b: 0, c: 1}).rank()
    generic_rank = matrix.rank()
    conic_rank = matrix.subs({a: 2, b: 1, c: 3}).rank()
    middle = binary_middle_matrix(a, b, c)
    determinant = factor(middle.det())
    assert matrix.shape == (35, 70)
    assert (diagonal_rank, conic_rank, cross_rank, generic_rank) == (15, 15, 18, 18)
    assert determinant == 8 * c * (9 * a * b - 2 * c**2)
    return {
        "schema_version": 1,
        "matrix_shape": list(matrix.shape),
        "diagonal_binary_tail_rank": diagonal_rank,
        "second_equality_component_sample_rank": conic_rank,
        "pure_cross_tail_rank": cross_rank,
        "generic_binary_tail_rank": generic_rank,
        "binary_middle_determinant": "8*c*(9*a*b-2*c^2)",
        "tensor_rank_formula": "dim D3(T) = 9 + 3*rank(C2(g))",
        "claim": (
            "For a rank-five coordinate frame and two extra factors supported "
            "on one coordinate pair, the middle dimension is 15 exactly on "
            "c*(9*a*b-2*c^2)=0, and is 18 off that divisor."
        ),
        "claim_boundary": (
            "This proves the binary-tail equality family but does not classify "
            "extra factors supported on three or more frame directions."
        ),
    }


def main() -> None:
    print(json.dumps(build(), indent=2, sort_keys=True))
    print("N7_LOWER51_RANK5_BINARY_EQUALITY_PASS")


if __name__ == "__main__":
    main()
