#!/usr/bin/env python3
"""Exact tangent-space diagnostic at the 64-term Glynn consistent point."""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from flint import nmod_mat


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_column_uniform_mixed_catalectic as mixed  # noqa: E402


P = mixed.PRIME


def modular_rank(matrix: np.ndarray) -> int:
    return nmod_mat((np.asarray(matrix, dtype=np.int64) % P).tolist(), P).rank()


def point_product(point: np.ndarray) -> int:
    value = 1
    for coordinate in point:
        value = value * int(coordinate) % P
    return value


def glynn_coefficients(points: np.ndarray) -> np.ndarray:
    inv64 = pow(64, P - 2, P)
    return np.asarray(
        [inv64 * point_product(point) % P for point in points],
        dtype=np.int64,
    )


def exponent_table() -> np.ndarray:
    rows = []
    for triple, quad in mixed.PAIR_ROWS:
        exponent = np.zeros(mixed.N, dtype=np.int64)
        exponent[list(triple)] += 1
        exponent[list(quad)] += 1
        rows.append(exponent)
    return np.stack(rows)


def jacobian() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    points = mixed.glynn_points()
    coefficients = glynn_coefficients(points)
    columns = mixed.coefficient_matrix(points)
    exponents = exponent_table()
    point_blocks = []
    # Coordinate zero is the affine normalization a_0=1.  All other Glynn
    # coordinates are +/-1, so division below is exact and non-singular.
    for term, point in enumerate(points):
        for coordinate in range(1, mixed.N):
            derivative = (
                coefficients[term]
                * exponents[:, coordinate]
                * columns[:, term]
                * pow(int(point[coordinate]), P - 2, P)
            ) % P
            point_blocks.append(derivative)
    point_jacobian = np.stack(point_blocks, axis=1)
    coefficient_jacobian = columns
    full = np.column_stack((point_jacobian, coefficient_jacobian))
    return point_jacobian, coefficient_jacobian, full


def full_waring_jacobian() -> tuple[np.ndarray, np.ndarray, np.ndarray, bool]:
    """Jacobian of the complete degree-seven coefficient identity."""
    points = mixed.glynn_points()
    monomials = mixed.base.MONOMIALS[7]
    multinomials = mixed.base.MULTINOMIALS[7]
    columns = np.empty((len(monomials), len(points)), dtype=np.int64)
    for row, alpha in enumerate(monomials):
        values = np.full(len(points), int(multinomials[row]), dtype=np.int64)
        for coordinate, exponent in enumerate(alpha):
            if exponent:
                values = values * np.asarray(
                    [pow(int(point[coordinate]), exponent, P) for point in points],
                    dtype=np.int64,
                ) % P
        columns[row] = values
    scale = pow((64 * math.factorial(7)) % P, P - 2, P)
    coefficients = np.asarray(
        [scale * point_product(point) % P for point in points],
        dtype=np.int64,
    )
    target = np.zeros(len(monomials), dtype=np.int64)
    target[monomials.index((1,) * mixed.N)] = 1
    residual_is_zero = bool(np.all((columns @ coefficients - target) % P == 0))
    point_blocks = []
    for term, point in enumerate(points):
        for coordinate in range(1, mixed.N):
            exponents = np.asarray([alpha[coordinate] for alpha in monomials], dtype=np.int64)
            derivative = (
                coefficients[term]
                * exponents
                * columns[:, term]
                * pow(int(point[coordinate]), P - 2, P)
            ) % P
            point_blocks.append(derivative)
    point_jacobian = np.stack(point_blocks, axis=1)
    coefficient_jacobian = columns
    full = np.column_stack((point_jacobian, coefficient_jacobian))
    return point_jacobian, coefficient_jacobian, full, residual_is_zero


def run() -> dict[str, object]:
    started = time.perf_counter()
    point_jacobian, coefficient_jacobian, full = jacobian()
    point_rank = modular_rank(point_jacobian)
    coefficient_rank = modular_rank(coefficient_jacobian)
    full_rank = modular_rank(full)
    variable_count = full.shape[1]
    tangent_dimension = variable_count - full_rank
    coefficient_projection_dimension = coefficient_jacobian.shape[1] - (full_rank - point_rank)
    waring_points, waring_coefficients, waring_full, waring_residual_is_zero = full_waring_jacobian()
    waring_point_rank = modular_rank(waring_points)
    waring_coefficient_rank = modular_rank(waring_coefficients)
    waring_full_rank = modular_rank(waring_full)
    elapsed = time.perf_counter() - started
    return {
        "schema_version": 1,
        "status": "EXACT_FINITE_FIELD_TANGENT_DIAGNOSTIC_NOT_A_GLOBAL_RANK_PROOF",
        "field": f"F_{P}",
        "consistent_point": "normalized_64_term_Glynn_decomposition",
        "jacobian_shape": list(full.shape),
        "point_coordinate_variable_count": int(point_jacobian.shape[1]),
        "coefficient_variable_count": int(coefficient_jacobian.shape[1]),
        "point_jacobian_rank": point_rank,
        "coefficient_jacobian_rank": coefficient_rank,
        "full_jacobian_rank": full_rank,
        "tangent_dimension": tangent_dimension,
        "coefficient_projection_dimension": coefficient_projection_dimension,
        "full_waring_system": {
            "identity_residual_is_zero": waring_residual_is_zero,
            "jacobian_shape": list(waring_full.shape),
            "point_jacobian_rank": waring_point_rank,
            "coefficient_jacobian_rank": waring_coefficient_rank,
            "full_jacobian_rank": waring_full_rank,
            "tangent_dimension": int(waring_full.shape[1] - waring_full_rank),
            "coefficient_projection_dimension": int(
                waring_coefficients.shape[1] - (waring_full_rank - waring_point_rank)
            ),
        },
        "estimated_peak_memory_gib": 0.15,
        "elapsed_seconds": elapsed,
        "claim_boundary": [
            "The ranks and tangent dimensions are exact over the displayed finite field.",
            "A small tangent space is only a local statement at the Glynn point.",
            "It does not exclude disconnected 49-point components or prove a characteristic-zero rank bound.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
