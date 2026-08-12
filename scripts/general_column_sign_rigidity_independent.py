#!/usr/bin/env python3
"""Independent ``n=6`` replay of full column-sign rigidity.

This implementation does not import the primary audit.  It constructs the
32-by-32 Walsh matrix, verifies its exact Gram matrix, solves the Boolean-slice
coefficient system, and checks independent full-sign and anchored-rational
representatives for every diagonal signature.
"""

from __future__ import annotations

import json
from fractions import Fraction

N = 6
DIMENSION = 32
TARGET = 31


def require(condition: bool, message: object) -> None:
    if not condition:
        raise AssertionError(message)


def character(mask: int, signature: int) -> int:
    return -1 if (mask & signature).bit_count() % 2 else 1


def walsh_matrix() -> list[list[int]]:
    return [
        [character(mask, signature) for signature in range(DIMENSION)]
        for mask in range(DIMENSION)
    ]


def gram(matrix: list[list[int]]) -> list[list[int]]:
    return [
        [
            sum(matrix[row][left] * matrix[row][right] for row in range(DIMENSION))
            for right in range(DIMENSION)
        ]
        for left in range(DIMENSION)
    ]


def independent_sign_matrix(signature: int) -> list[list[int]]:
    matrix = [[1 for _ in range(N)] for _ in range(N)]
    for column in range(N):
        for row in range(1, N):
            if column and row == column:
                matrix[row][column] = character(1 << (column - 1), signature)
            else:
                bit = (
                    signature
                    ^ (row << 1)
                    ^ (column << 3)
                    ^ (row * column * 5)
                ).bit_count() & 1
                matrix[row][column] = -1 if bit else 1
    return matrix


def independent_anchored_matrix(signature: int) -> list[list[Fraction]]:
    matrix = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for column in range(N):
        anchor = Fraction(2 * column + 3, column + 2)
        matrix[0][column] = anchor
        for row in range(1, N):
            if column and row == column:
                matrix[row][column] = (
                    anchor * character(1 << (column - 1), signature)
                )
            else:
                matrix[row][column] = Fraction(
                    2 + 19 * row + 7 * column + signature,
                    3 + ((row + column + signature) % 11),
                )
    return matrix


def normalized_slice(matrix: list[list[int | Fraction]]) -> list[Fraction]:
    anchors = [Fraction(matrix[0][column]) for column in range(N)]
    require(all(anchor != 0 for anchor in anchors), anchors)
    result: list[Fraction] = []
    for mask in range(DIMENSION):
        coefficient = Fraction(matrix[0][0], anchors[0])
        for column in range(1, N):
            row = column if (mask >> (column - 1)) & 1 else 0
            coefficient *= Fraction(matrix[row][column], anchors[column])
        result.append(coefficient)
    return result


def build_payload() -> dict[str, object]:
    matrix = walsh_matrix()
    observed_gram = gram(matrix)
    expected_gram = [
        [DIMENSION if left == right else 0 for right in range(DIMENSION)]
        for left in range(DIMENSION)
    ]
    require(observed_gram == expected_gram, "Walsh Gram matrix mismatch")

    coefficients = [
        Fraction(matrix[TARGET][signature], DIMENSION)
        for signature in range(DIMENSION)
    ]
    require(all(coefficient != 0 for coefficient in coefficients), coefficients)
    reconstruction = [
        sum(
            coefficients[signature] * matrix[mask][signature]
            for signature in range(DIMENSION)
        )
        for mask in range(DIMENSION)
    ]
    expected = [Fraction(0) for _ in range(DIMENSION)]
    expected[TARGET] = Fraction(1)
    require(reconstruction == expected, (reconstruction, expected))

    sign_checks = 0
    anchored_checks = 0
    for signature in range(DIMENSION):
        expected_character = [
            Fraction(character(mask, signature)) for mask in range(DIMENSION)
        ]
        sign_slice = normalized_slice(independent_sign_matrix(signature))
        anchored_slice = normalized_slice(independent_anchored_matrix(signature))
        require(sign_slice == expected_character, (signature, "sign"))
        require(anchored_slice == expected_character, (signature, "anchored"))
        sign_checks += DIMENSION
        anchored_checks += DIMENSION

    return {
        "status": "GENERAL_COLUMN_SIGN_RIGIDITY_INDEPENDENT_PASS",
        "n": N,
        "walsh_matrix_shape": [DIMENSION, DIMENSION],
        "walsh_gram_diagonal": DIMENSION,
        "walsh_gram_off_diagonal": 0,
        "target_mask": TARGET,
        "unique_nonzero_aggregate_coefficients": DIMENSION,
        "coefficient_denominator": DIMENSION,
        "independent_sign_slice_checks": sign_checks,
        "independent_anchored_slice_checks": anchored_checks,
        "normalized_family_size": 1 << 30,
        "terms_per_diagonal_signature": 1 << 25,
        "exact_restricted_rank": DIMENSION,
        "claim_boundary": (
            "This independent replay checks the n=6 Boolean-slice theorem. "
            "It does not address arbitrary complex row-homogeneous or "
            "unrestricted Chow decompositions."
        ),
    }


def main() -> int:
    payload = build_payload()
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("GENERAL_COLUMN_SIGN_RIGIDITY_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
