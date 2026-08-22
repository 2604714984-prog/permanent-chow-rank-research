#!/usr/bin/env python3
"""Streamed torus-weight projection of the Packet-A degree-six incidence."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path

import numpy as np
from flint import nmod_mat


N = 7
PRIME = 65521
ROOT = Path(__file__).resolve().parents[1]


def load_local(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


general = load_local("n7_packet_a_general_operator")
smoke = load_local("n7_packet_a_labelled_256_operator")

EXPONENTS6 = general.exponent_basis(N, 6)
EXPONENT_INDEX6 = {alpha: index for index, alpha in enumerate(EXPONENTS6)}
SUBSETS6 = general.factor_subsets(6)
OMITTED_FACTOR_TO_SUBSET_INDEX = {
    next(iter(set(range(N)).difference(subset))): index
    for index, subset in enumerate(SUBSETS6)
}
TARGET_SCALE = math.factorial(6)
MAX_PROJECTED_STATE_COUNT = (1 << (N - 1)) * len(EXPONENTS6)


def multinomial(alpha: tuple[int, ...]) -> int:
    value = math.factorial(sum(alpha))
    for exponent in alpha:
        value //= math.factorial(exponent)
    return value


def column_uniform_factors(point: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if len(point) != N:
        raise ValueError("a column-uniform point needs seven row coordinates")
    factors = []
    for column in range(N):
        row = [0] * (N * N)
        for source_row, value in enumerate(point):
            row[source_row * N + column] = value
        factors.append(tuple(row))
    return tuple(factors)


def projected_product_column(
    factors: tuple[tuple[int, ...], ...],
    subset: tuple[int, ...],
    omitted_column: int,
) -> np.ndarray:
    """Project one six-factor product to one column-torus block and symmetrize rows."""

    if general.validate_factors(factors) != N * N:
        raise ValueError("permanent blocks use the 49 matrix-entry coordinates")
    allowed_columns = tuple(column for column in range(N) if column != omitted_column)
    column_bit = {column: 1 << index for index, column in enumerate(allowed_columns)}
    full_mask = (1 << (N - 1)) - 1
    states: dict[tuple[int, tuple[int, ...]], int] = {(0, (0,) * N): 1}
    for factor_index in subset:
        updated: dict[tuple[int, tuple[int, ...]], int] = {}
        factor = factors[factor_index]
        for (mask, exponent), coefficient in states.items():
            for row in range(N):
                for column in allowed_columns:
                    bit = column_bit[column]
                    if mask & bit:
                        continue
                    value = factor[row * N + column]
                    if value == 0:
                        continue
                    target = list(exponent)
                    target[row] += 1
                    key = (mask | bit, tuple(target))
                    updated[key] = updated.get(key, 0) + coefficient * value
        states = updated
        if len(states) > MAX_PROJECTED_STATE_COUNT:
            raise AssertionError("projected DP exceeded its precomputed state bound")
    answer = np.zeros(len(EXPONENTS6), dtype=np.int64)
    for (mask, exponent), coefficient in states.items():
        if mask == full_mask:
            answer[EXPONENT_INDEX6[exponent]] += coefficient
    return answer


def projected_term_block(
    factors: tuple[tuple[int, ...], ...], omitted_column: int
) -> np.ndarray:
    return np.column_stack(
        [projected_product_column(factors, subset, omitted_column) for subset in SUBSETS6]
    )


def power6_columns(points: list[tuple[int, ...]]) -> np.ndarray:
    columns = np.empty((len(EXPONENTS6), len(points)), dtype=np.int64)
    for row, alpha in enumerate(EXPONENTS6):
        values = np.full(len(points), multinomial(alpha), dtype=np.int64)
        for coordinate, exponent in enumerate(alpha):
            if exponent:
                values *= np.asarray(
                    [int(point[coordinate]) ** exponent for point in points],
                    dtype=np.int64,
                )
        columns[row] = values
    return columns


def column_uniform_aggregate_block(
    points: list[tuple[int, ...]], omitted_column: int
) -> np.ndarray:
    block = np.zeros((len(EXPONENTS6), len(points) * N), dtype=np.int64)
    subset_index = OMITTED_FACTOR_TO_SUBSET_INDEX[omitted_column]
    block[:, subset_index::N] = power6_columns(points)
    return block


def permanent_target_block(omitted_column: int) -> np.ndarray:
    block = np.zeros((len(EXPONENTS6), N * N), dtype=np.int64)
    for missing_row in range(N):
        alpha = tuple(0 if row == missing_row else 1 for row in range(N))
        block[EXPONENT_INDEX6[alpha], omitted_column * N + missing_row] = TARGET_SCALE
    return block


def modular_nullspace(matrix: np.ndarray, prime: int) -> np.ndarray:
    array = np.asarray(matrix, dtype=np.int64) % prime
    basis, nullity = nmod_mat(array.tolist(), prime).nullspace()
    if nullity == 0:
        return np.zeros((array.shape[1], 0), dtype=np.int64)
    answer = np.asarray(basis.tolist(), dtype=np.int64)[:, :nullity]
    if np.any(array @ answer % prime):
        raise AssertionError("invalid streamed nullspace")
    return answer


def update_common_kernel(
    kernel: np.ndarray, block: np.ndarray, prime: int
) -> np.ndarray:
    restricted = np.asarray(block, dtype=np.int64) @ kernel % prime
    local = modular_nullspace(restricted, prime)
    return kernel @ local % prime


def streamed_target_quotient(points: list[tuple[int, ...]], prime: int = PRIME) -> dict[str, object]:
    term_columns = len(points) * N
    target_columns = N * N
    base_kernel = np.eye(term_columns, dtype=np.int64)
    augmented_kernel = np.eye(term_columns + target_columns, dtype=np.int64)
    block_rows = []
    for omitted_column in range(N):
        aggregate = column_uniform_aggregate_block(points, omitted_column) % prime
        target = permanent_target_block(omitted_column) % prime
        base_kernel = update_common_kernel(base_kernel, aggregate, prime)
        augmented = np.column_stack((aggregate, target)) % prime
        augmented_kernel = update_common_kernel(augmented_kernel, augmented, prime)
        block_rows.append(
            {
                "omitted_column": omitted_column,
                "aggregate_nonzero_column_count": int(np.count_nonzero(np.any(aggregate, axis=0))),
                "target_nonzero_column_count": int(np.count_nonzero(np.any(target, axis=0))),
                "base_common_kernel_dimension_after_block": int(base_kernel.shape[1]),
                "augmented_common_kernel_dimension_after_block": int(augmented_kernel.shape[1]),
            }
        )
    base_rank = term_columns - base_kernel.shape[1]
    augmented_rank = term_columns + target_columns - augmented_kernel.shape[1]
    quotient_rank = augmented_rank - base_rank
    return {
        "field": f"F_{prime}",
        "term_count": len(points),
        "labelled_degree_6_column_count": term_columns,
        "permanent_target_column_count": target_columns,
        "torus_block_count": N,
        "rows_per_symmetrized_block": len(EXPONENTS6),
        "base_rank": int(base_rank),
        "augmented_rank": int(augmented_rank),
        "target_quotient_rank": int(quotient_rank),
        "projected_survivor": quotient_rank == 0,
        "streamed_without_vertical_materialization": True,
        "blocks": block_rows,
    }


def general_block_control() -> dict[str, object]:
    point = (1, 2, -1, 3, 1, -2, 2)
    factors = column_uniform_factors(point)
    direct = projected_term_block(factors, 6)
    analytic = column_uniform_aggregate_block([point], 6)
    if not np.array_equal(direct, analytic):
        raise AssertionError("general block projection disagrees with the column-uniform formula")
    nonzero_columns = np.flatnonzero(np.any(direct, axis=0)).tolist()
    perturbed = [list(factor) for factor in factors]
    # Give factor six an off-column coefficient.  In the block omitting
    # column six, the product omitting factor zero can now use column zero.
    perturbed[6][0] += 1
    nonuniform = projected_term_block(
        tuple(tuple(factor) for factor in perturbed), 6
    )
    nonuniform_columns = np.flatnonzero(np.any(nonuniform, axis=0)).tolist()
    if nonuniform_columns != [0, 6]:
        raise AssertionError(nonuniform_columns)
    return {
        "ambient_factor_coordinate_count": N * N,
        "factor_count": N,
        "omitted_column": 6,
        "projected_block_shape": list(direct.shape),
        "nonzero_labelled_subset_columns": nonzero_columns,
        "non_column_uniform_nonzero_subset_columns": nonuniform_columns,
        "column_uniform_formula_matches_general_projection": True,
        "off_column_factor_coefficient_exercised": True,
        "maximum_projected_DP_state_count": MAX_PROJECTED_STATE_COUNT,
        "coefficient_ring": "ZZ exact",
    }


def equality_incidence(points: list[tuple[int, ...]]) -> dict[str, object]:
    count = len(points)
    smoke_control = smoke.control(count)
    pairing = smoke_control["complementary_2_5_relation_pairing"]
    exact_target = smoke_control["degree_6_permanent_target_quotient"]
    streamed = streamed_target_quotient(points)
    if streamed["target_quotient_rank"] != exact_target["total_target_quotient_rank"]:
        raise AssertionError((streamed, exact_target))
    return {
        "term_count": count,
        "QQ_exact_Walsh_target_quotient_rank": exact_target["total_target_quotient_rank"],
        "finite_field_streamed_target_incidence": streamed,
        "finite_field_inverse_coefficient_relation_pairing_rank_per_block": pairing[
            "restricted_relation_pairing_rank_per_block"
        ],
        "finite_field_relation_orthogonality_holds": pairing[
            "relation_orthogonality_condition_holds"
        ],
        "decision": (
            "PERMANENT_SPECIFIC_NONZERO_TARGET_DEFECT"
            if exact_target["total_target_quotient_rank"]
            else "PROJECTED_EXACT_CONTROL_SURVIVOR"
        ),
    }


def build_payload() -> dict[str, object]:
    general_control = general_block_control()
    glynn49 = equality_incidence(smoke.normalized_signs(49))
    glynn64 = equality_incidence(smoke.normalized_signs(64))
    non_tensor = smoke.non_tensor_sylvester_control()
    if glynn49["decision"] != "PERMANENT_SPECIFIC_NONZERO_TARGET_DEFECT":
        raise AssertionError(glynn49)
    if glynn64["decision"] != "PROJECTED_EXACT_CONTROL_SURVIVOR":
        raise AssertionError(glynn64)
    return {
        "schema_version": 1,
        "status": "PACKET_A_PERMANENT_BLOCK_A03_A05_BOUNDED_CONTROLS",
        "resource_preflight": {
            "full_Sym6_Q49_dimension_not_materialized": math.comb(49 + 6 - 1, 6),
            "torus_block_count": N,
            "symmetrized_rows_per_block": len(EXPONENTS6),
            "largest_streamed_control_shape": [len(EXPONENTS6), 64 * N + N * N],
            "largest_streamed_dense_entry_count": len(EXPONENTS6) * (64 * N + N * N),
            "conservative_peak_memory_mib": 128,
            "vertical_6468_row_matrix_materialized": False,
        },
        "general_factor_plane_projection_control": general_control,
        "labelled_equality_incidence_controls": {
            "glynn49_truncation": glynn49,
            "glynn64_positive_span_control": glynn64,
            "non_tensor_sylvester_control": non_tensor,
        },
        "rank_fields": {
            "Walsh_target_quotient": "QQ exact",
            "streamed_full_labelled_block_incidence": f"F_{PRIME}",
            "relation_pairing_and_non_tensor_Sylvester_control": f"F_{PRIME}",
            "general_projection_coefficients": "ZZ exact",
        },
        "claim_boundary": [
            "The seven omitted-column torus blocks are streamed through common-kernel updates; the 25,827,165-dimensional full Sym6(Q49) basis is never materialized.",
            "A nonzero projected target quotient is a valid obstruction for the displayed candidate; a zero quotient is only a survivor of this projection.",
            "The Glynn49 truncation has QQ-exact permanent target quotient rank 35 and is excluded; it is not a permanent decomposition.",
            "The Glynn64 control survives with quotient rank zero, but this package does not reprove the degree-seven Glynn identity.",
            "The non-tensor control concerns Sylvester equality only and is not a Packet-A permanent solution.",
            "No arbitrary 49-term factor-plane classification, A-CLOSED result, ordinary lower 50, or border-rank theorem is proved.",
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
            raise SystemExit("Packet A permanent block JSON mismatch")
        print("PASS n7 Packet A permanent block operator")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
