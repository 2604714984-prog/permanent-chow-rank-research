#!/usr/bin/env python3
"""Extract the 32-block code behind the synchronized mixed Glynn packet.

The computation is bounded: 32 core tails, 32 extra tails, seven derivative
rows per tail, and 600 deterministic evaluation columns.  It identifies the
42-dimensional target quotient code with seven copies of the high-character
translate of RM(1,5).  This is a subfamily theorem, not an exclusion of the
general packet-B endpoint.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_equality_packet_crossdegree_search as base  # noqa: E402


P = base.PRIME
N = base.N
EXTRA_BLOCKS = 32
ROWS_PER_BLOCK = 7


class ModularRowBasis:
    """Small dense row basis with optional coefficient tracking."""

    def __init__(self, tracked_coordinates: int = 0):
        self.rows: dict[int, tuple[np.ndarray, np.ndarray]] = {}
        self.tracked_coordinates = tracked_coordinates

    def reduce(self, raw: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        row = np.array(raw, dtype=np.int64, copy=True) % P
        coefficients = np.zeros(self.tracked_coordinates, dtype=np.int64)
        for pivot, (basis_row, representation) in self.rows.items():
            factor = int(row[pivot])
            if factor:
                row = (row - factor * basis_row) % P
                coefficients = (coefficients + factor * representation) % P
        return row, coefficients

    def add(self, raw: np.ndarray, representation: np.ndarray | None = None) -> bool:
        row = np.array(raw, dtype=np.int64, copy=True) % P
        if representation is None:
            coefficients = np.zeros(self.tracked_coordinates, dtype=np.int64)
        else:
            coefficients = np.array(representation, dtype=np.int64, copy=True) % P
        for pivot, (basis_row, basis_representation) in self.rows.items():
            factor = int(row[pivot])
            if factor:
                row = (row - factor * basis_row) % P
                coefficients = (coefficients - factor * basis_representation) % P
        support = np.flatnonzero(row)
        if not len(support):
            return False
        pivot = int(support[0])
        inverse = pow(int(row[pivot]), P - 2, P)
        self.rows[pivot] = (row * inverse % P, coefficients * inverse % P)
        return True


def derivative_block(tail: tuple[int, ...], evaluations: np.ndarray) -> np.ndarray:
    a_indices = [row * N + column for row in range(N) for column in range(1, N)]
    w_indices = [row * N for row in range(N)]
    a_values = evaluations[a_indices]
    w_values = evaluations[w_indices]
    graph = np.zeros((42, N), dtype=np.int64)
    for row in range(N):
        graph[6 * row : 6 * (row + 1), row] = np.asarray(tail) % P
    factors = (graph.T @ a_values + w_values) % P
    return base.omitted_products(factors)


def fixed_rank_six_rows(evaluations: np.ndarray) -> np.ndarray:
    a_indices = [row * N + column for row in range(N) for column in range(1, N)]
    a_values = evaluations[a_indices]
    rows = []
    for block in range(N):
        basis = a_values[6 * block : 6 * (block + 1)]
        rows.extend(base.omitted_products(np.vstack((basis, basis[0]))))
    return np.asarray(rows, dtype=np.int64)


def expected_high_walsh_code() -> np.ndarray:
    points = list(itertools.product((-1, 1), repeat=5))
    rows = []
    for component in range(ROWS_PER_BLOCK):
        for character in range(6):
            row = np.zeros(EXTRA_BLOCKS * ROWS_PER_BLOCK, dtype=np.int64)
            for block, point in enumerate(points):
                full_character = int(np.prod(point))
                value = (
                    full_character
                    if character == 0
                    else full_character * point[character - 1]
                )
                row[block * ROWS_PER_BLOCK + component] = value
            rows.append(row % P)
    return np.asarray(rows, dtype=np.int64)


def build_payload(seed: int, evaluation_columns: int) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    evaluations = rng.integers(
        0, P, size=(base.V_DIM, evaluation_columns), dtype=np.int64
    )
    degree_six_targets, _ = base.permanent_targets(evaluations)
    core_tails = [(1, *tail) for tail in itertools.product((-1, 1), repeat=5)]
    extra_tails = [(-1, *tail) for tail in itertools.product((-1, 1), repeat=5)]

    core_rows = np.vstack(
        (
            fixed_rank_six_rows(evaluations),
            *(derivative_block(tail, evaluations) for tail in core_tails),
        )
    )
    core_basis = ModularRowBasis()
    for row in core_rows:
        core_basis.add(row)

    extra_rows = np.vstack(
        tuple(derivative_block(tail, evaluations) for tail in extra_tails)
    )
    extra_basis = ModularRowBasis(tracked_coordinates=len(extra_rows))
    for index, row in enumerate(extra_rows):
        quotient_row, _ = core_basis.reduce(row)
        unit = np.zeros(len(extra_rows), dtype=np.int64)
        unit[index] = 1
        extra_basis.add(quotient_row, unit)

    target_code_rows = []
    nonzero_remainders = 0
    for row in degree_six_targets:
        quotient_row, _ = core_basis.reduce(row)
        remainder, representation = extra_basis.reduce(quotient_row)
        nonzero_remainders += int(bool(np.count_nonzero(remainder)))
        target_code_rows.append(representation)
    target_code = np.asarray(target_code_rows, dtype=np.int64)
    expected_code = expected_high_walsh_code()

    target_code_rank = base.modular_rank(target_code)
    expected_code_rank = base.modular_rank(expected_code)
    combined_rank = base.modular_rank(np.vstack((target_code, expected_code)))
    return {
        "schema_version": 1,
        "status": "EXACT_SYNCHRONIZED_GLYNN_SUBFAMILY_CODE",
        "field": f"F_{P}",
        "seed": seed,
        "evaluation_columns": evaluation_columns,
        "core_tail_count": len(core_tails),
        "extra_tail_count": len(extra_tails),
        "core_derivative_rank": len(core_basis.rows),
        "extra_quotient_rank": len(extra_basis.rows),
        "target_quotient_code_rank": target_code_rank,
        "target_nonzero_remainders_after_all_extras": nonzero_remainders,
        "expected_high_walsh_code_rank": expected_code_rank,
        "combined_code_rank": combined_rank,
        "codes_equal": target_code_rank == expected_code_rank == combined_rank,
        "block_code": {
            "length": EXTRA_BLOCKS,
            "block_width": ROWS_PER_BLOCK,
            "dimension": 42,
            "description": "seven copies of full_character * RM(1,5)",
            "minimum_nonzero_block_support": 16,
            "available_extra_blocks_in_endpoint_packet": 10,
            "can_add_target_direction_with_ten_extras": False,
        },
        "synchronized_packet_conclusion": {
            "core_target_intersection": 7,
            "target_intersection_after_any_ten_extras": 7,
        },
        "claim_boundary": [
            "This closes all choices of ten extras in the synchronized 64-tail dictionary.",
            "It does not cover independent GL(6) transforms or arbitrary graph complements.",
            "The modular extraction is paired with the explicit high-Walsh code formula; it is not a general lower-fifty theorem.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    assert payload["core_derivative_rank"] == 266
    assert payload["extra_quotient_rank"] == 224
    assert payload["target_quotient_code_rank"] == 42
    assert payload["target_nonzero_remainders_after_all_extras"] == 0
    assert payload["expected_high_walsh_code_rank"] == 42
    assert payload["combined_code_rank"] == 42
    assert payload["codes_equal"] is True
    assert payload["synchronized_packet_conclusion"] == {
        "core_target_intersection": 7,
        "target_intersection_after_any_ten_extras": 7,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=24_681_357)
    parser.add_argument("--evaluation-columns", type=int, default=600)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.seed, args.evaluation_columns)
    validate(payload)
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS frozen payload")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
