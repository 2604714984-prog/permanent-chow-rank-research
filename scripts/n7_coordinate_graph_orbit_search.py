#!/usr/bin/env python3
"""Orbit-reduced exact search over every loopless coordinate graph map.

Exploratory endpoint computation.  It uses SciPy only to find connected
components of the finite S_7 action; the resulting linear system is exact
over a prime field.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
from flint import fmpq_mat


N = 7
BASE = 7
STATE_COUNT = BASE**N
PRIME = 65521


def state_digits() -> np.ndarray:
    codes = np.arange(STATE_COUNT, dtype=np.int32)
    powers = (BASE ** np.arange(N, dtype=np.int64)).reshape(1, -1)
    return ((codes.reshape(-1, 1) // powers) % BASE).astype(np.uint8)


def target_tables() -> tuple[np.ndarray, np.ndarray]:
    target = np.full((N, BASE), -1, dtype=np.int8)
    inverse = np.zeros((N, N + 1), dtype=np.uint8)
    for domain in range(N):
        choices = [value for value in range(N) if value != domain]
        for digit, value in enumerate(choices, start=1):
            target[domain, digit] = value
            inverse[domain, value + 1] = digit
    return target, inverse


def action_components(digits: np.ndarray) -> np.ndarray:
    target, inverse = target_tables()
    powers = BASE ** np.arange(N, dtype=np.int64)
    permutations = np.asarray(list(itertools.permutations(range(N))), dtype=np.int8)
    labels = np.full(STATE_COUNT, -1, dtype=np.int32)
    next_code = 0
    orbit = 0
    while next_code < STATE_COUNT:
        while next_code < STATE_COUNT and labels[next_code] >= 0:
            next_code += 1
        if next_code == STATE_COUNT:
            break
        actual = np.asarray(
            [target[domain, digits[next_code, domain]] for domain in range(N)],
            dtype=np.int8,
        )
        orbit_codes = np.zeros(len(permutations), dtype=np.int64)
        for domain in range(N):
            new_domain = permutations[:, domain]
            old_target = int(actual[domain])
            if old_target < 0:
                new_target = np.full(len(permutations), -1, dtype=np.int8)
            else:
                new_target = permutations[:, old_target]
            new_digit = inverse[new_domain, new_target + 1]
            orbit_codes += new_digit.astype(np.int64) * powers[new_domain]
        orbit_codes = np.unique(orbit_codes)
        assert np.all((labels[orbit_codes] == -1) | (labels[orbit_codes] == orbit))
        labels[orbit_codes] = orbit
        orbit += 1
    assert np.all(labels >= 0)
    return labels


def compact_labels(labels: np.ndarray, selection: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    unique = np.unique(labels[selection])
    lookup = np.full(int(labels.max()) + 1, -1, dtype=np.int32)
    lookup[unique] = np.arange(len(unique), dtype=np.int32)
    return lookup[labels], unique


def target_vector(digits: np.ndarray, partial_labels: np.ndarray, partial_count: int) -> np.ndarray:
    target, _ = target_tables()
    actual = np.empty_like(digits, dtype=np.int8)
    selected = digits != 0
    for domain in range(N):
        actual[:, domain] = target[domain, digits[:, domain]]
    values = np.zeros(STATE_COUNT, dtype=np.uint8)
    proper = np.any(~selected, axis=1)
    for code in np.flatnonzero(proper):
        domain = np.flatnonzero(selected[code])
        image = actual[code, domain]
        values[code] = int(np.array_equal(np.sort(image), domain))
    orbit_min = np.full(partial_count, 2, dtype=np.uint8)
    orbit_max = np.zeros(partial_count, dtype=np.uint8)
    np.minimum.at(orbit_min, partial_labels[proper], values[proper])
    np.maximum.at(orbit_max, partial_labels[proper], values[proper])
    assert np.array_equal(orbit_min, orbit_max)
    return orbit_min.astype(np.int64)


def orbit_system(
    digits: np.ndarray,
    labels: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, int]]:
    full = np.all(digits != 0, axis=1)
    proper = ~full
    full_labels, full_unique = compact_labels(labels, full)
    partial_labels, partial_unique = compact_labels(labels, proper)
    full_count = len(full_unique)
    partial_count = len(partial_unique)
    matrix = np.zeros((partial_count, full_count), dtype=np.int32)
    full_codes = np.flatnonzero(full)
    full_digits = digits[full]
    column_ids = full_labels[full]
    powers = BASE ** np.arange(N, dtype=np.int64)
    for mask in range(1 << N):
        if mask == (1 << N) - 1:
            continue
        selected = np.asarray([(mask >> index) & 1 for index in range(N)], dtype=np.uint8)
        partial_codes = ((full_digits * selected).astype(np.int64) @ powers).astype(np.int32)
        row_ids = partial_labels[partial_codes]
        np.add.at(matrix, (row_ids, column_ids), 1)
    target = target_vector(digits, partial_labels, partial_count)
    degrees = np.full(partial_count, -1, dtype=np.int8)
    np.maximum.at(degrees, partial_labels[proper], np.count_nonzero(digits[proper], axis=1))
    assert np.all(degrees >= 0)
    return matrix, target, degrees, {
        "full_function_count": int(full.sum()),
        "proper_partial_map_count": int(proper.sum()),
        "full_function_orbit_count": full_count,
        "proper_partial_map_orbit_count": partial_count,
    }


def modular_rank(matrix: np.ndarray) -> int:
    work = np.asarray(matrix, dtype=np.int64).copy() % PRIME
    row = 0
    for column in range(work.shape[1]):
        candidates = np.flatnonzero(work[row:, column])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        work[[row, pivot]] = work[[pivot, row]]
        work[row] = work[row] * pow(int(work[row, column]), PRIME - 2, PRIME) % PRIME
        active = np.flatnonzero(work[:, column])
        active = active[active != row]
        for start in range(0, len(active), 128):
            indices = active[start : start + 128]
            work[indices] = (
                work[indices] - work[indices, column, None] * work[row][None, :]
            ) % PRIME
        row += 1
        if row == work.shape[0]:
            break
    return row


def degree_two_certificate(
    digits: np.ndarray,
    labels: np.ndarray,
    matrix: np.ndarray,
    target_vector_: np.ndarray,
    degrees: np.ndarray,
) -> dict[str, object]:
    proper = np.any(digits == 0, axis=1)
    partial_labels, _ = compact_labels(labels, proper)
    orbit_sizes = np.bincount(partial_labels[proper])
    target, _ = target_tables()
    named_rows: dict[str, tuple[int, dict[str, object]]] = {}
    for orbit_id in np.flatnonzero(degrees == 2):
        candidates = np.flatnonzero(
            (partial_labels == orbit_id) & (np.count_nonzero(digits, axis=1) == 2)
        )
        code = int(candidates[0])
        domain = tuple(map(int, np.flatnonzero(digits[code])))
        image = tuple(int(target[index, digits[code, index]]) for index in domain)
        if image == tuple(reversed(domain)):
            name = "two_cycle"
        elif image[0] == image[1]:
            name = "common_target_collision"
        elif any(value in domain for value in image):
            name = "length_two_path"
        else:
            name = "disjoint_edges"
        named_rows[name] = (
            int(orbit_id),
            {
                "name": name,
                "representative_domain": list(domain),
                "representative_image": list(image),
                "labelled_orbit_size": int(orbit_sizes[orbit_id]),
            },
        )
    order = ("two_cycle", "length_two_path", "common_target_collision", "disjoint_edges")
    row_ids = [named_rows[name][0] for name in order]
    left_relation = np.asarray([-5, -2, 1, 1], dtype=np.int64)
    assert np.all(left_relation @ matrix[row_ids] == 0)
    target_evaluation = int(left_relation @ target_vector_[row_ids])
    assert target_evaluation == -5
    return {
        "row_orbits": [named_rows[name][1] for name in order],
        "left_kernel_coefficients": left_relation.tolist(),
        "coefficient_matrix_evaluation_is_zero": True,
        "target_evaluation": target_evaluation,
        "combinatorial_identity": "collision+disjoint-2*path-5*two_cycle=0",
    }


def build_payload() -> dict[str, object]:
    digits = state_digits()
    labels = action_components(digits)
    matrix, target, degrees, counts = orbit_system(digits, labels)
    coefficient_rank = modular_rank(matrix)
    augmented_rank = modular_rank(np.column_stack((matrix, target)))
    rational_coefficient_rank = fmpq_mat(matrix.tolist()).rank()
    rational_augmented_rank = fmpq_mat(np.column_stack((matrix, target)).tolist()).rank()
    cumulative = []
    degreewise = []
    for maximum_degree in range(7):
        selected = degrees <= maximum_degree
        coefficient = matrix[selected]
        augmented = np.column_stack((coefficient, target[selected]))
        cumulative.append(
            {
                "maximum_A_degree": maximum_degree,
                "orbit_equation_count": int(selected.sum()),
                "coefficient_rank": fmpq_mat(coefficient.tolist()).rank(),
                "augmented_rank": fmpq_mat(augmented.tolist()).rank(),
            }
        )
        exact = degrees == maximum_degree
        exact_coefficient = matrix[exact]
        exact_augmented = np.column_stack((exact_coefficient, target[exact]))
        degreewise.append(
            {
                "A_degree": maximum_degree,
                "orbit_equation_count": int(exact.sum()),
                "coefficient_rank": fmpq_mat(exact_coefficient.tolist()).rank(),
                "augmented_rank": fmpq_mat(exact_augmented.tolist()).rank(),
            }
        )
    inconsistent = rational_augmented_rank > rational_coefficient_rank
    assert coefficient_rank == rational_coefficient_rank
    assert augmented_rank == rational_augmented_rank
    assert inconsistent
    return {
        "schema_version": 1,
        "status": "EXACT_COORDINATE_GRAPH_FAMILY_EXCLUDED_NOT_A_CHOW_RANK_BOUND",
        "field": f"F_{PRIME}",
        "candidate_cardinality_checked_before_enumeration": {
            "loopless_full_functions": 6**7,
            "proper_partial_maps": 7**7 - 6**7,
        },
        **counts,
        "coefficient_matrix_shape": list(matrix.shape),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "rational_coefficient_rank": rational_coefficient_rank,
        "rational_augmented_rank": rational_augmented_rank,
        "cumulative_jet_ranks": cumulative,
        "degreewise_relaxed_moment_ranks": degreewise,
        "degree_two_combinatorial_certificate": degree_two_certificate(
            digits, labels, matrix, target, degrees
        ),
        "inconsistent_over_Q": inconsistent,
        "claim_boundary": [
            "All loopless coordinate graph maps are covered after exact S7 orbit reduction.",
            "Exact rational elimination proves the characteristic-zero rank jump; the modular ranks independently agree.",
            "The separate degree-two rank jump still excludes arbitrary common graph scalings after relaxing their moments degree by degree.",
            "Arbitrary noncoordinate graph complements are outside this finite family.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify_json:
        assert json.loads(args.verify_json.read_text(encoding="utf-8")) == payload
        print("N7_COORDINATE_GRAPH_ORBIT_SEARCH_VERIFY_PASS")
    elif args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
