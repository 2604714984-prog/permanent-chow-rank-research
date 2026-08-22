#!/usr/bin/env python3
"""Labelled 2/5/6 schema and mandatory-control smoke for Packet A.

The large coefficient spaces are never materialized.  For the normalized
Glynn controls, every fixed row-subset block is represented by its exact
Walsh evaluation matrix.  Term labels and complementary factor subsets are
retained throughout.  This is an interface/control certificate, not a
classification of arbitrary 49-term packets.  General factor-plane matrices
and their multiplication/differentiation transport are not implemented here.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import nmod_mat


N = 7
PRIME = 65521
DEGREES = (2, 5, 6)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as sylvester  # noqa: E402


def normalized_signs(count: int) -> list[tuple[int, ...]]:
    if not 1 <= count <= 64:
        raise ValueError("the normalized n=7 sign cube has 64 points")
    return [(1,) + tail for tail in itertools.product((-1, 1), repeat=6)][:count]


def parity_characters(degree: int) -> list[tuple[int, ...]]:
    return [
        subset
        for size in range(degree % 2, degree + 1, 2)
        for subset in itertools.combinations(range(N), size)
    ]


def evaluation_matrix(
    signs: list[tuple[int, ...]], characters: list[tuple[int, ...]]
) -> list[list[int]]:
    # Aggregate map orientation: character coordinates by labelled terms.
    return [
        [math.prod(delta[index] for index in character) for delta in signs]
        for character in characters
    ]


def rational_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    work = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(rank, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][column]
        work[rank] = [entry / value for entry in work[rank]]
        for row in range(rank + 1, len(work)):
            if work[row][column]:
                value = work[row][column]
                work[row] = [
                    entry - value * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def modular_nullspace(matrix: list[list[int]]) -> np.ndarray:
    array = np.asarray(matrix, dtype=np.int64) % PRIME
    basis, nullity = nmod_mat(array.tolist(), PRIME).nullspace()
    if nullity == 0:
        return np.zeros((array.shape[1], 0), dtype=np.int64)
    answer = np.asarray(basis.tolist(), dtype=np.int64)[:, :nullity]
    if np.any(array @ answer % PRIME):
        raise AssertionError("invalid FLINT nullspace")
    return answer


def modular_rank(matrix: np.ndarray) -> int:
    array = np.asarray(matrix, dtype=np.int64) % PRIME
    return nmod_mat(array.tolist(), PRIME).rank()


def glynn_coefficients(signs: list[tuple[int, ...]]) -> np.ndarray:
    inverse = pow(64, PRIME - 2, PRIME)
    return np.asarray(
        [inverse * math.prod(delta) % PRIME for delta in signs], dtype=np.int64
    )


def inverse_diagonal(coefficients: np.ndarray) -> np.ndarray:
    coefficients = np.asarray(coefficients, dtype=np.int64) % PRIME
    if np.any(coefficients == 0):
        raise ValueError("the external term coefficients must be nonzero")
    return np.diag(
        np.asarray([pow(int(value), PRIME - 2, PRIME) for value in coefficients])
    )


def block_profile(count: int, degree: int) -> dict[str, int]:
    signs = normalized_signs(count)
    characters = parity_characters(degree)
    aggregate = evaluation_matrix(signs, characters)
    rank = rational_rank(aggregate)
    block_count = math.comb(N, degree)
    return {
        "factor_subset_count_per_term": block_count,
        "term_count": count,
        "labelled_source_dimension": count * block_count,
        "walsh_coordinate_count_per_aggregate_block": len(characters),
        "aggregate_rank_per_block": rank,
        "aggregate_image_dimension": block_count * rank,
        "aggregate_kernel_dimension": block_count * (count - rank),
    }


def complementary_pairing(count: int) -> dict[str, int | bool]:
    signs = normalized_signs(count)
    e2 = evaluation_matrix(signs, parity_characters(2))
    e5 = evaluation_matrix(signs, parity_characters(5))
    k2 = modular_nullspace(e2)
    k5 = modular_nullspace(e5)
    coefficients = glynn_coefficients(signs)
    restricted = k2.T @ inverse_diagonal(coefficients) @ k5 % PRIME
    rank = modular_rank(restricted) if restricted.size else 0
    pair_count = math.comb(N, 2)
    return {
        "complementary_factor_subset_pair_count": pair_count,
        "degree_2_kernel_per_block": int(k2.shape[1]),
        "degree_5_kernel_per_block": int(k5.shape[1]),
        "restricted_relation_pairing_rank_per_block": rank,
        "left_radical_dimension_per_block": int(k2.shape[1] - rank),
        "right_radical_dimension_per_block": int(k5.shape[1] - rank),
        "relation_orthogonality_condition_holds": rank == 0,
        "kernel_image_form": "K2 is contained in the annihilator of K5 exactly when the restricted pairing rank is zero",
        "external_coefficient_convention": "sum_i c_i T_i; relation pairing K2^T diag(c)^(-1) K5",
        "labels_preserved_by_pairing": True,
    }


def non_self_inverse_coefficient_controls() -> list[dict[str, object]]:
    rows = []
    for a, b in ((2, 3), (3, 5), (5, 7)):
        coefficients = np.asarray([a, b], dtype=np.int64)
        aggregate2 = np.asarray([[1, -1]], dtype=np.int64)
        aggregate5 = np.asarray([[b, a]], dtype=np.int64)
        k2 = modular_nullspace(aggregate2.tolist())
        k5 = modular_nullspace(aggregate5.tolist())
        correct = k2.T @ inverse_diagonal(coefficients) @ k5 % PRIME
        wrong = k2.T @ np.diag(coefficients) @ k5 % PRIME
        correct_rank = modular_rank(correct)
        wrong_rank = modular_rank(wrong)
        transported_input = np.diag(coefficients) @ aggregate5.T % PRIME
        kernel_image = sylvester.kernel_image_defect(
            aggregate2, transported_input, PRIME
        )
        if correct_rank != 0 or wrong_rank != 1:
            raise AssertionError((a, b, correct.tolist(), wrong.tolist()))
        if kernel_image["coupling_defect"] != 0 or not kernel_image["condition_holds"]:
            raise AssertionError((a, b, kernel_image))
        rows.append(
            {
                "coefficients": [a, b],
                "degree_2_aggregate_map": aggregate2.tolist(),
                "degree_5_aggregate_map": aggregate5.tolist(),
                "degree_2_kernel_column": k2[:, 0].tolist(),
                "degree_5_kernel_column": k5[:, 0].tolist(),
                "inverse_coefficient_pairing_entry": int(correct[0, 0]),
                "inverse_coefficient_pairing_rank": correct_rank,
                "wrong_coefficient_pairing_entry": int(wrong[0, 0]),
                "wrong_coefficient_pairing_rank": wrong_rank,
                "wrong_direction_changes_condition": True,
                "transported_input_map_diag_c_A5_transpose": transported_input.tolist(),
                "kernel_image_condition": kernel_image,
            }
        )
    return rows


def degree6_target_quotient(count: int) -> dict[str, int | bool | list[int]]:
    signs = normalized_signs(count)
    characters = parity_characters(6)
    aggregate_rows = list(map(list, zip(*evaluation_matrix(signs, characters))))
    selected_rank = rational_rank(aggregate_rows)
    target_rows = []
    target_character_indices = []
    for column, character in enumerate(characters):
        if len(character) == 6:
            row = [0] * len(characters)
            row[column] = 1
            target_rows.append(row)
            target_character_indices.append(column)
    joint_rank = rational_rank(aggregate_rows + target_rows)
    intersection = selected_rank + len(target_rows) - joint_rank
    quotient_rank = len(target_rows) - intersection
    # Seven omitted-row blocks are disjoint.  The 49 target generators have
    # distinct (omitted row, omitted column) torus labels before quotienting.
    return {
        "scope": "Glynn/Walsh span control only",
        "omitted_row_block_count": N,
        "target_dimension_per_block": len(target_rows),
        "target_character_indices": target_character_indices,
        "aggregate_rank_per_block": selected_rank,
        "target_intersection_dimension_per_block": intersection,
        "target_quotient_rank_per_block": quotient_rank,
        "total_target_dimension": N * len(target_rows),
        "total_target_quotient_rank": N * quotient_rank,
        "target_torus_weight_labels": [
            [omitted_row, omitted_column]
            for omitted_row in range(N)
            for omitted_column in range(N)
        ],
        "target_contained": quotient_rank == 0,
    }


def non_tensor_sylvester_control() -> dict[str, int | bool]:
    factors = sylvester.five_plane_factors()
    output_map, input_map = sylvester.catalectic_maps_for_cubic_products(
        factors, PRIME
    )
    row = sylvester.kernel_image_defect(output_map, input_map, PRIME)
    return {**row, "tensor_split": False}


def control(count: int) -> dict[str, object]:
    return {
        "term_count": count,
        "degree_profiles": {
            str(degree): block_profile(count, degree) for degree in DEGREES
        },
        "complementary_2_5_relation_pairing": complementary_pairing(count),
        "degree_6_permanent_target_quotient": degree6_target_quotient(count),
    }


def build_payload() -> dict[str, object]:
    candidate_count = 64
    labelled_columns = candidate_count * sum(math.comb(N, d) for d in DEGREES)
    if labelled_columns != 3136:
        raise AssertionError(labelled_columns)
    truncation = control(49)
    full = control(64)
    non_tensor = non_tensor_sylvester_control()
    coefficient_direction_controls = non_self_inverse_coefficient_controls()
    if truncation["degree_6_permanent_target_quotient"]["total_target_quotient_rank"] != 35:
        raise AssertionError("49-term target quotient control changed")
    if not full["degree_6_permanent_target_quotient"]["target_contained"]:
        raise AssertionError("64-term Glynn positive control failed")
    if not non_tensor["condition_holds"] or non_tensor["tensor_split"]:
        raise AssertionError("non-tensor Sylvester control failed")
    return {
        "schema_version": 1,
        "status": "PACKET_A_LABELLED_SCHEMA_AND_MANDATORY_CONTROLS_SMOKE",
        "rank_fields": {
            "Walsh_aggregate_and_target_span_ranks": "Q exact elimination",
            "relation_pairing_and_Sylvester_ranks": f"F_{PRIME}",
        },
        "candidate_cardinality_preflight": candidate_count,
        "largest_materialized_matrix_shape": [64, 64],
        "estimated_peak_memory_mib": 8,
        "one_term_module": {
            "factor_rank": N,
            "D2_dimension": math.comb(N, 2),
            "D5_dimension": math.comb(N, 5),
            "D6_dimension": math.comb(N, 6),
            "retained_labelled_dimension_per_term": sum(
                math.comb(N, degree) for degree in DEGREES
            ),
            "coordinate_formula": "D_d(prod_j l_j) has columns prod_{j in I} l_j, |I|=d, labelled by (term,I)",
            "coefficient_degree_in_factor_coordinates": {"2": 2, "5": 5, "6": 6},
            "ambient_basis_action": "Sym^d(g) on the degree-d aggregate target",
            "factor_relabelling_action": "the induced permutation of factor-subset columns",
            "factor_rescaling_action": "column I is multiplied by the product of the scalars indexed by I",
        },
        "mandatory_controls": {
            "glynn_49_truncation_negative_control": truncation,
            "non_tensor_sylvester_equality_control": non_tensor,
            "known_glynn_64_identity_span_positive_control": full,
            "non_self_inverse_external_coefficient_direction_controls": coefficient_direction_controls,
        },
        "claim_boundary": [
            "This is a labelled schema plus mandatory-controls smoke, not completion or freezing of A-01 through A-05.",
            "General factor-plane matrices, multiplication/differentiation transport, general K2/K5/K6, and the general permanent target operator remain unimplemented.",
            "The 49-term Glynn truncation has degree-six target quotient rank 35 and is not a permanent decomposition.",
            "The non-tensor Sylvester control forbids inferring tensor split from kernel-image equality alone.",
            "Walsh compression is used only for the displayed Glynn controls; it is not imposed on arbitrary Packet A terms.",
            "The known 64-term Glynn identity is used only as a span control; this artifact does not verify the degree-seven polynomial identity.",
            "This certificate proves no A-CLOSED result and no ordinary or border Chow-rank bound.",
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
            raise SystemExit("Packet A labelled operator JSON mismatch")
        print("PASS n7 Packet A labelled 2/5/6 operator")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
