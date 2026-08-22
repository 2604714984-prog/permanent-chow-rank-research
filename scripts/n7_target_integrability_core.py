#!/usr/bin/env python3
"""Exact modular control for the corrected TI-01 through TI-03 complex."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as coupled  # noqa: E402
import n7_packet_b_curve_coupling_probe as curve  # noqa: E402


PRIME = 65521
PAIRS = tuple(combinations(range(7), 2))
FRONTIER_Q5_Q6 = (
    ("F1", 2, 1),
    ("F2", 3, 2),
    ("F3-H6-41", 2, 1),
    ("F3-H6-42", 2, 0),
    ("F4", 4, 3),
    ("F5-H6-40", 3, 2),
    ("F5-H6-41", 3, 1),
)


def mixed_partial_tensor(coefficients: np.ndarray, points: np.ndarray, prime: int) -> np.ndarray:
    coefficients = np.asarray(coefficients, dtype=np.int64) % prime
    points = np.asarray(points, dtype=np.int64) % prime
    if coefficients.shape != (7, points.shape[0]) or points.shape[1] != 7:
        raise ValueError("expected coefficients 7 x n and points n x 7")
    columns = [
        (coefficients[j] * points[:, k] - coefficients[k] * points[:, j]) % prime
        for j, k in PAIRS
    ]
    return np.column_stack(columns)


def columns_lie_in(column_vectors: np.ndarray, basis: np.ndarray, prime: int) -> bool:
    base_rank = coupled.modular_rank(basis, prime)
    return all(
        coupled.modular_rank(np.column_stack((basis, column_vectors[:, index])), prime)
        == base_rank
        for index in range(column_vectors.shape[1])
    )


def build_payload() -> dict[str, object]:
    # Eight distinct points on a projective line.  Their degree-six powers have
    # one relation and their degree-five powers have two relations.
    tails = [(parameter, 0, 0, 0, 0, 0) for parameter in range(1, 9)]
    points = np.asarray([(1, *tail) for tail in tails], dtype=np.int64) % PRIME
    degree5 = curve.point_code_matrix(tails, 5, PRIME)
    degree6 = curve.point_code_matrix(tails, 6, PRIME)
    relation5 = coupled.modular_nullspace_columns(degree5.T, PRIME)
    relation6 = coupled.modular_nullspace_columns(degree6.T, PRIME)
    if relation5.shape != (8, 2) or relation6.shape != (8, 1):
        raise AssertionError((relation5.shape, relation6.shape))

    weights = np.arange(1, 9, dtype=np.int64)
    coefficient_solution = points.T * weights[None, :] % PRIME
    targets = coefficient_solution @ degree6 % PRIME
    base_tensor = mixed_partial_tensor(coefficient_solution, points, PRIME)
    if np.any(base_tensor):
        raise AssertionError("the Waring-gradient control must integrate termwise")

    gauge_scalars = np.arange(1, 8, dtype=np.int64)[:, None]
    gauge = gauge_scalars * relation6[:, 0][None, :] % PRIME
    shifted_solution = (coefficient_solution + gauge) % PRIME
    if np.any(shifted_solution @ degree6 % PRIME != targets):
        raise AssertionError("R6 gauge changed the represented target")
    shifted_tensor = mixed_partial_tensor(shifted_solution, points, PRIME)
    gauge_tensor = mixed_partial_tensor(gauge, points, PRIME)
    if np.any((shifted_tensor - base_tensor - gauge_tensor) % PRIME):
        raise AssertionError("mixed-partial gauge law failed")
    if not np.any(shifted_tensor):
        raise AssertionError("the control gauge should change the relation tensor")
    if not columns_lie_in(shifted_tensor, relation5, PRIME):
        raise AssertionError("automatic mixed partials missed R5")

    frontier = [
        {
            "frontier": label,
            "q5": q5,
            "q6": q6,
            "gauge_source_dimension": 7 * q6,
            "relation_tensor_dimension": 21 * q5,
        }
        for label, q5, q6 in FRONTIER_Q5_Q6
    ]
    return {
        "schema_version": 1,
        "status": "TI-01-TI-03-GAUGE-CORRECTED-COMPLEX",
        "prime_control": PRIME,
        "control": {
            "point_count": 8,
            "points_are_distinct": len(set(tails)) == 8,
            "rank_e5": coupled.modular_rank(degree5, PRIME),
            "rank_e6": coupled.modular_rank(degree6, PRIME),
            "q5": relation5.shape[1],
            "q6": relation6.shape[1],
            "coefficient_fiber_preserved_by_nonzero_gauge": True,
            "base_relation_tensor_rank": coupled.modular_rank(base_tensor, PRIME),
            "shifted_relation_tensor_rank": coupled.modular_rank(shifted_tensor, PRIME),
            "shifted_tensor_columns_lie_in_r5": True,
            "gauge_difference_equals_d_a": True,
        },
        "frontier_dimensions": frontier,
        "claim_boundary": [
            "Target containment makes the quotient mixed-partial map modulo R5 identically zero; it is not an additional obstruction.",
            "The canonical datum is the relation-tensor class modulo the image of d_A from seven copies of R6.",
            "The modular line control checks orientations and the gauge law only; it is not a characteristic-zero nonexistence result.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("TI_CORE_FROZEN_REPLAY_FAIL")
            return 1
        print("TI_CORE_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
