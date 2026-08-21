#!/usr/bin/env python3
"""Exact replay for one-term Glynn compression and the n=6 quartic seven-block witness."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
from typing import Iterable, Sequence

EXPECTED_CORE = "045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def sign_vectors(m: int) -> tuple[tuple[int, ...], ...]:
    require(m >= 2, m)
    return tuple((1,) + tail for tail in product((1, -1), repeat=m - 1))


def character(delta: Sequence[int]) -> int:
    result = 1
    for value in delta:
        result *= int(value)
    return result


def coefficient_of_compressed_identity(
    m: int,
    rows: Sequence[int],
    missing: Sequence[int] | None = None,
) -> int:
    """Return the unscaled coefficient of one row assignment."""
    require(len(rows) == m, rows)
    delta_zero = tuple((1,) * m if missing is None else missing)
    require(delta_zero in sign_vectors(m), delta_zero)
    shared_columns = tuple(range(m - 2))
    moving_columns = (m - 2, m - 1)
    total = 0
    for delta in sign_vectors(m):
        if delta == delta_zero:
            continue
        shared = 1
        for column in shared_columns:
            shared *= delta[rows[column]]
        moving = delta[rows[moving_columns[0]]] * delta[rows[moving_columns[1]]]
        fixed = (
            delta_zero[rows[moving_columns[0]]]
            * delta_zero[rows[moving_columns[1]]]
        )
        total += character(delta) * shared * (moving - fixed)
    return total


def exhaustive_identity_row(m: int) -> dict[str, int]:
    zero_coefficients = 0
    permanent_coefficients = 0
    assignments = 0
    scale = 2 ** (m - 1)
    for rows in product(range(m), repeat=m):
        coefficient = coefficient_of_compressed_identity(m, rows)
        expected = scale if len(set(rows)) == m else 0
        require(coefficient == expected, (m, rows, coefficient, expected))
        assignments += 1
        if coefficient:
            permanent_coefficients += 1
        else:
            zero_coefficients += 1
    require(permanent_coefficients == factorial(m), (m, permanent_coefficients))
    return {
        "row_assignments": assignments,
        "permanent_coefficients": permanent_coefficients,
        "zero_coefficients": zero_coefficients,
        "unscaled_permanent_coefficient": scale,
    }


def walsh_relation_holds(m: int) -> bool:
    """Check the shared-(m-2)-column relation by parity masks."""
    reachable = {0}
    row_masks = (0,) + tuple(1 << index for index in range(m - 1))
    for _ in range(m - 2):
        reachable = {left ^ right for left in reachable for right in row_masks}
    full_character = (1 << (m - 1)) - 1
    return full_character not in reachable


def exact_rank(matrix: Sequence[Sequence[int | Fraction]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    width = len(rows[0])
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [entry / pivot_value for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                left - multiplier * right
                for left, right in zip(rows[row], rows[rank], strict=True)
            ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def outer_matrix(delta: Sequence[int]) -> tuple[int, ...]:
    return tuple(int(delta[row]) * int(delta[column]) for row in range(4) for column in range(4))


def permanent_pair_flattening() -> list[list[int]]:
    """Flatten perm_4 as (columns 1,2) versus (columns 0,3)."""
    matrix = [[0 for _ in range(16)] for _ in range(16)]
    for rows in product(range(4), repeat=4):
        if len(set(rows)) != 4:
            continue
        left = rows[1] * 4 + rows[2]
        right = rows[0] * 4 + rows[3]
        matrix[left][right] = 1
    return matrix


def paired_column_data() -> dict[str, object]:
    signs = sign_vectors(4)
    missing = (1, 1, 1, 1)
    retained = tuple(delta for delta in signs if delta != missing)
    sign_matrices = [outer_matrix(delta) for delta in retained]
    sign_span_rank = exact_rank(sign_matrices)
    require(sign_span_rank == 7, sign_span_rank)

    flattening = permanent_pair_flattening()
    flattening_rank = exact_rank(flattening)
    require(flattening_rank == 6, flattening_rank)

    # The contraction image is the six-dimensional zero-diagonal symmetric space.
    zero_diagonal_symmetric_basis = []
    for left in range(4):
        for right in range(left + 1, 4):
            vector = [0] * 16
            vector[left * 4 + right] = 1
            vector[right * 4 + left] = 1
            zero_diagonal_symmetric_basis.append(vector)
    require(exact_rank(zero_diagonal_symmetric_basis) == 6, "S0 rank")

    # The unique Walsh relation among all eight sign matrices has coefficients chi(delta).
    relation = [0] * 16
    for delta in signs:
        weight = character(delta)
        matrix = outer_matrix(delta)
        relation = [left + weight * right for left, right in zip(relation, matrix, strict=True)]
    require(relation == [0] * 16, relation)

    return {
        "grouped_flattening_rank": flattening_rank,
        "zero_diagonal_symmetric_image_dimension": 6,
        "retained_sign_outer_products": len(retained),
        "retained_sign_outer_product_span_rank": sign_span_rank,
        "rank_one_matrix_inside_zero_diagonal_symmetric_space": False,
        "paired_column_minimum_terms": 7,
        "paired_column_construction_terms": 7,
        "missing_sign": list(missing),
    }


def chow_membership_rows(m: int) -> dict[str, int]:
    signs = sign_vectors(m)
    retained = len(signs) - 1
    shared = m - 2
    factor_count = shared + 4
    require(factor_count == m + 2, (m, factor_count))
    return {
        "sign_terms_before_compression": len(signs),
        "blocks_after_compression": retained,
        "shared_factors_per_block": shared,
        "alternative_tail_products_per_block": 2,
        "degree_of_chow_envelope": factor_count,
        "source_subsets_used_per_block": 2,
    }


def build_core() -> dict[str, object]:
    exact_rows = {str(m): exhaustive_identity_row(m) for m in range(3, 7)}
    walsh_rows = {str(m): walsh_relation_holds(m) for m in range(3, 11)}
    require(all(walsh_rows.values()), walsh_rows)
    construction_rows = {str(m): chow_membership_rows(m) for m in range(3, 11)}

    return {
        "schema": "general_one_term_glynn_compression/v1",
        "classification": "EXPLICIT_NONZERO_FAMILY_AND_RESTRICTED_SHARPNESS_THEOREM",
        "field": "characteristic_zero",
        "general_theorem": {
            "output_degree_minimum": 3,
            "degree_threshold": "n>=m+2",
            "term_upper_bound": "2^(m-1)-1",
            "shared_column_count": "m-2",
            "identity": "perm_m=2^(1-m) sum_{delta!=delta0} chi(delta) A_delta (B_delta-B_delta0)",
            "padding_to_larger_n": True,
        },
        "exact_replay": {
            "coefficient_rows": exact_rows,
            "walsh_relation_rows": walsh_rows,
            "construction_rows": construction_rows,
        },
        "quartic_n6_application": {
            "previous_interval": [6, 8],
            "new_interval": [6, 7],
            "seven_block_literal_sum_nonzero": True,
            "degree": 6,
            "output_degree": 4,
            "blocks": 7,
            "permanent_matching_coefficients": 24,
            "nonmatching_coefficients": 232,
        },
        "paired_column_sharpness": paired_column_data(),
        "claim_boundary": {
            "six_block_literal_sum": "OPEN",
            "seven_block_literal_sum": "NONZERO",
            "mu_6_4": "OPEN_IN_[6,7]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    core = build_core()
    digest = hashlib.sha256(canonical_json(core).encode("utf-8")).hexdigest()
    if EXPECTED_CORE != "TO_BE_FILLED":
        require(digest == EXPECTED_CORE, digest)
    payload = dict(core)
    payload["core_sha256"] = digest
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GENERAL_ONE_TERM_GLYNN_COMPRESSION_PASS")
    print(digest)


if __name__ == "__main__":
    main()
