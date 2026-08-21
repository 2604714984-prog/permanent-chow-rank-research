#!/usr/bin/env python3
"""Exact matrix-level checker for the perm_7 endpoint coupling condition.

For maps ``B: K -> H4`` and ``C: H3* -> K`` the Sylvester-equality
condition is ``ker(B) <= im(C)``.  This script checks that inclusion exactly
over two finite fields and freezes small positive and negative controls.  It
does not construct the full perm_7 endpoint maps yet.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from flint import nmod_mat


PRIMES = (65521, 65519)


def modular_rank(matrix: np.ndarray, prime: int) -> int:
    array = np.asarray(matrix, dtype=np.int64) % prime
    if array.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    return nmod_mat(array.tolist(), prime).rank()


def modular_nullspace_columns(matrix: np.ndarray, prime: int) -> np.ndarray:
    array = np.asarray(matrix, dtype=np.int64) % prime
    if array.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    basis, nullity = nmod_mat(array.tolist(), prime).nullspace()
    if nullity == 0:
        return np.zeros((array.shape[1], 0), dtype=np.int64)
    columns = np.asarray(basis.tolist(), dtype=np.int64)[:, :nullity]
    if np.any(array @ columns % prime):
        raise AssertionError("FLINT nullspace basis failed reconstruction")
    return columns


def kernel_image_defect(
    output_map: np.ndarray, input_map: np.ndarray, prime: int
) -> dict[str, int | bool]:
    """Return the exact defect of ``ker(output_map) <= im(input_map)``."""

    output_map = np.asarray(output_map, dtype=np.int64) % prime
    input_map = np.asarray(input_map, dtype=np.int64) % prime
    if output_map.ndim != 2 or input_map.ndim != 2:
        raise ValueError("both maps must be two-dimensional")
    if output_map.shape[1] != input_map.shape[0]:
        raise ValueError("the maps do not share the same middle space")

    middle_dimension = output_map.shape[1]
    rank_b = modular_rank(output_map, prime)
    rank_c = modular_rank(input_map, prime)
    rank_bc = modular_rank(output_map @ input_map % prime, prime)
    kernel = modular_nullspace_columns(output_map, prime)
    joint = np.column_stack((kernel, input_map))
    joint_rank = modular_rank(joint, prime)

    kernel_dimension = middle_dimension - rank_b
    defect_from_kernel = joint_rank - rank_c
    defect_from_ranks = middle_dimension - rank_b - rank_c + rank_bc
    if defect_from_kernel != defect_from_ranks:
        raise AssertionError(
            ("coupling defect formulas disagree", defect_from_kernel, defect_from_ranks)
        )
    intersection_dimension = kernel_dimension - defect_from_kernel
    return {
        "middle_dimension": int(middle_dimension),
        "rank_b": int(rank_b),
        "rank_c": int(rank_c),
        "rank_bc": int(rank_bc),
        "kernel_b_dimension": int(kernel_dimension),
        "kernel_b_intersection_image_c_dimension": int(intersection_dimension),
        "coupling_defect": int(defect_from_kernel),
        "condition_holds": defect_from_kernel == 0,
    }


def kernel_image_defect_from_kernel(
    output_map: np.ndarray, input_map: np.ndarray, prime: int
) -> dict[str, int | bool]:
    """Check the inclusion without materializing the potentially large BC."""

    output_map = np.asarray(output_map, dtype=np.int64) % prime
    input_map = np.asarray(input_map, dtype=np.int64) % prime
    if output_map.ndim != 2 or input_map.ndim != 2:
        raise ValueError("both maps must be two-dimensional")
    if output_map.shape[1] != input_map.shape[0]:
        raise ValueError("the maps do not share the same middle space")
    middle_dimension = output_map.shape[1]
    rank_b = modular_rank(output_map, prime)
    rank_c = modular_rank(input_map, prime)
    kernel = modular_nullspace_columns(output_map, prime)
    joint_rank = modular_rank(np.column_stack((kernel, input_map)), prime)
    kernel_dimension = middle_dimension - rank_b
    defect = joint_rank - rank_c
    return {
        "middle_dimension": int(middle_dimension),
        "rank_b": int(rank_b),
        "rank_c": int(rank_c),
        "kernel_b_dimension": int(kernel_dimension),
        "kernel_b_intersection_image_c_dimension": int(kernel_dimension - defect),
        "coupling_defect": int(defect),
        "condition_holds": defect == 0,
    }


def quadratic_product(left: np.ndarray, right: np.ndarray, prime: int) -> np.ndarray:
    """Coefficient vector of a product of linear forms in i<=j coordinates."""

    left = np.asarray(left, dtype=np.int64) % prime
    right = np.asarray(right, dtype=np.int64) % prime
    if left.shape != right.shape or left.ndim != 1:
        raise ValueError("linear forms must be vectors of the same length")
    answer = []
    for i in range(len(left)):
        for j in range(i, len(left)):
            coefficient = left[i] * right[j]
            if i != j:
                coefficient += left[j] * right[i]
            answer.append(int(coefficient % prime))
    return np.asarray(answer, dtype=np.int64)


def five_plane_factors() -> list[np.ndarray]:
    """The five non-tensor-split three-planes from the slope-ten note."""

    factors: list[np.ndarray] = []
    for block in range(3):
        matrix = np.zeros((3, 9), dtype=np.int64)
        matrix[:, 3 * block : 3 * (block + 1)] = np.eye(3, dtype=np.int64)
        factors.append(matrix)

    diagonal = np.zeros((3, 9), dtype=np.int64)
    graph = np.zeros((3, 9), dtype=np.int64)
    first_diagonal = (2, 3, 4)
    second_diagonal = (6, 8, 10)
    for row in range(3):
        diagonal[row, row] = 1
        diagonal[row, 3 + row] = 1
        diagonal[row, 6 + row] = 1
        graph[row, row] = 1
        graph[row, 3 + row] = first_diagonal[row]
        graph[row, 6 + row] = second_diagonal[row]
    factors.extend((diagonal, graph))
    return factors


def catalectic_maps_for_cubic_products(
    factor_packets: list[np.ndarray], prime: int
) -> tuple[np.ndarray, np.ndarray]:
    """Build B and C for a sum of products of three labelled linear forms."""

    output_blocks = []
    input_blocks = []
    for factors in factor_packets:
        factors = np.asarray(factors, dtype=np.int64) % prime
        if factors.shape[0] != 3:
            raise ValueError("each cubic product must have three factors")
        output_blocks.append(
            np.column_stack(
                tuple(
                    quadratic_product(
                        factors[(omitted + 1) % 3],
                        factors[(omitted + 2) % 3],
                        prime,
                    )
                    for omitted in range(3)
                )
            )
        )
        input_blocks.append(factors)
    return np.column_stack(output_blocks), np.vstack(input_blocks)


def small_kernel_controls(prime: int) -> dict[str, dict[str, int | bool]]:
    output_map = np.asarray([[1, 0, 0], [0, 1, 0]], dtype=np.int64)
    contained_input = np.asarray([[1, 0], [0, 0], [0, 1]], dtype=np.int64)
    missing_input = np.asarray([[1], [0], [0]], dtype=np.int64)
    return {
        "nontrivial_kernel_contained": kernel_image_defect(
            output_map, contained_input, prime
        ),
        "one_kernel_direction_missing": kernel_image_defect(
            output_map, missing_input, prime
        ),
    }


def invert_matrix(matrix: np.ndarray, prime: int) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=np.int64) % prime
    size = matrix.shape[0]
    if matrix.shape != (size, size):
        raise ValueError("matrix must be square")
    work = np.column_stack((matrix, np.eye(size, dtype=np.int64)))
    for column in range(size):
        choices = np.flatnonzero(work[column:, column])
        if choices.size == 0:
            raise ValueError("matrix is singular")
        pivot = column + int(choices[0])
        work[[column, pivot]] = work[[pivot, column]]
        work[column] = work[column] * pow(int(work[column, column]), prime - 2, prime) % prime
        for row in range(size):
            if row != column and work[row, column]:
                work[row] = (work[row] - work[row, column] * work[column]) % prime
    return work[:, size:]


def basis_invariance_control(prime: int) -> dict[str, object]:
    output_map = np.asarray([[1, 0, 0], [0, 1, 0]], dtype=np.int64)
    input_map = np.asarray([[1, 0], [0, 0], [0, 1]], dtype=np.int64)
    middle_change = np.asarray([[0, 2, 0], [3, 0, 0], [0, 0, 5]], dtype=np.int64)
    ambient_output_change = np.asarray([[1, 4], [2, 9]], dtype=np.int64)
    ambient_input_change = np.asarray([[1, 7], [3, 5]], dtype=np.int64)
    transformed_b = ambient_output_change @ output_map @ middle_change % prime
    transformed_c = (
        invert_matrix(middle_change, prime) @ input_map @ ambient_input_change
    ) % prime
    original = kernel_image_defect(output_map, input_map, prime)
    transformed = kernel_image_defect(transformed_b, transformed_c, prime)
    if original["coupling_defect"] != transformed["coupling_defect"]:
        raise AssertionError("coupling defect changed under basis transformations")
    return {"original": original, "transformed": transformed}


def build_payload() -> dict[str, object]:
    rows = []
    for prime in PRIMES:
        five_b, five_c = catalectic_maps_for_cubic_products(
            five_plane_factors(), prime
        )
        five_plane = kernel_image_defect(five_b, five_c, prime)
        if (five_plane["rank_b"], five_plane["rank_c"], five_plane["rank_bc"]) != (
            15,
            9,
            9,
        ):
            raise AssertionError(("unexpected five-plane ranks", five_plane))
        if not five_plane["condition_holds"]:
            raise AssertionError("five-plane Sylvester equality control failed")
        controls = small_kernel_controls(prime)
        if not controls["nontrivial_kernel_contained"]["condition_holds"]:
            raise AssertionError("contained-kernel control failed")
        if controls["one_kernel_direction_missing"]["coupling_defect"] != 1:
            raise AssertionError("missing-kernel control failed")
        rows.append(
            {
                "prime": prime,
                "five_plane_non_tensor_split_control": {
                    **five_plane,
                    "tensor_split": False,
                },
                "small_kernel_controls": controls,
                "basis_invariance_control": basis_invariance_control(prime),
            }
        )
    return {
        "schema_version": 1,
        "status": "EXACT_ABSTRACT_SYLVESTER_COUPLING_CHECKER",
        "primes": list(PRIMES),
        "rows": rows,
        "next_gate": (
            "Construct labelled K_i, B, and C for packet B before computing "
            "the 252 general GL(6)^7 tangent directions."
        ),
        "claim_boundary": [
            "The checker proves the displayed matrix kernel-image inclusions exactly over the listed finite fields.",
            "The five-plane control shows that Sylvester equality alone does not force a tensor split.",
            "No perm_7 endpoint packet is classified and no lower-50 or border-rank conclusion is made.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 coupled-obstruction JSON mismatch")
        print("PASS n7 equality-packet coupled obstruction")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
