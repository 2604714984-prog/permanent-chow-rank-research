#!/usr/bin/env python3
"""Exact symbolic rank-five binary-tail catalectic classification."""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix, expand, factor, symbols


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


def ternary_middle_matrix(q: tuple[object, ...]) -> Matrix:
    q00, q11, q22, q01, q02, q12 = q
    return Matrix(
        [
            [0, 0, 0, 0, 0, 6 * q22, 2 * q12, 0, 2 * q02, 0],
            [0, 0, 0, 0, 3 * q22, 4 * q12, 3 * q11, 2 * q02, 2 * q01, q00],
            [0, 0, 0, 0, 2 * q12, 6 * q11, 0, 2 * q01, 0, 0],
            [0, 3 * q22, 2 * q12, q11, 0, 4 * q02, 2 * q01, 0, 3 * q00, 0],
            [q22, 2 * q12, 3 * q11, 0, 2 * q02, 4 * q01, 0, 3 * q00, 0, 0],
            [0, 2 * q02, 2 * q01, 0, 0, 6 * q00, 0, 0, 0, 0],
        ]
    )


def five_minors(matrix: Matrix) -> tuple[object, ...]:
    values = set()
    for rows in itertools.combinations(range(matrix.rows), 5):
        for columns in itertools.combinations(range(matrix.cols), 5):
            value = factor(matrix.extract(rows, columns).det())
            if value:
                values.add(value)
    return tuple(values)


def contains_scalar_multiple(
    polynomials: tuple[object, ...], target: object, substitutions: dict | None = None
) -> bool:
    substitutions = substitutions or {}
    for polynomial in polynomials:
        value = factor(polynomial.subs(substitutions))
        if value and expand(value / target).is_number:
            return True
    return False


def build() -> dict:
    matrix, a, b, c = catalectic_matrix()
    diagonal_rank = matrix.subs(c, 0).rank()
    cross_rank = matrix.subs({a: 0, b: 0, c: 1}).rank()
    generic_rank = matrix.rank()
    conic_rank = matrix.subs({a: 2, b: 1, c: 3}).rank()
    middle = binary_middle_matrix(a, b, c)
    determinant = factor(middle.det())
    q = symbols("q00 q11 q22 q01 q02 q12")
    q00, q11, q22, q01, q02, q12 = q
    ternary = ternary_middle_matrix(q)
    minors = five_minors(ternary)
    for target in (
        q00**3 * q01 * q22,
        q00**3 * q02 * q11,
        q00**3 * q12 * q22,
    ):
        assert contains_scalar_multiple(minors, target)
    assert contains_scalar_multiple(minors, q00**3 * q11 * q12)
    assert contains_scalar_multiple(minors, q00 * q02**3 * q11)
    binary_substitutions = {q22: 0, q02: 0, q12: 0}
    assert contains_scalar_multiple(
        minors,
        q00 * q01 * q11 * (9 * q00 * q11 - 2 * q01**2),
        binary_substitutions,
    )
    one_diagonal = {q11: 0, q22: 0}
    for target in (q00 * q01**4, q00**2 * q02**3, q00 * q12**4):
        assert contains_scalar_multiple(minors, target, one_diagonal)
    zero_diagonal = {q00: 0, q11: 0, q22: 0}
    for target in (q01**5, q02**5, q12**5):
        assert contains_scalar_multiple(minors, target, zero_diagonal)
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
        "ternary_middle_matrix_shape": list(ternary.shape),
        "nonzero_five_minor_polynomials": len(minors),
        "full_equality_normal_form": (
            "After a coordinate permutation, both extra factors lie in "
            "span(x1,x2) and c*(9*a*b-2*c^2)=0."
        ),
        "claim": (
            "Every rank-five middle-dimension-15 product has, after a frame "
            "permutation, both extra factors in one coordinate two-plane and "
            "lies on c*(9*a*b-2*c^2)=0."
        ),
        "claim_boundary": (
            "This classifies the full-increment middle equality forms only; "
            "intermediate quotient orientations remain outside the result."
        ),
    }


def main() -> None:
    print(json.dumps(build(), indent=2, sort_keys=True))
    print("N7_LOWER51_RANK5_BINARY_EQUALITY_PASS")


if __name__ == "__main__":
    main()
