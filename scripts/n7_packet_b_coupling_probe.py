#!/usr/bin/env python3
"""Projected exact B/C coupling probe for the synchronized perm_7 packet B.

The output evaluation enlarges ker(B), while the pure-cube input sampling
shrinks im(C).  Therefore a zero projected coupling defect is a rigorous
sufficient certificate for the true inclusion.  A positive defect is only a
diagnostic and must not be promoted to a global obstruction.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sys
import time

import numpy as np
from flint import fmpz_mat, nmod_mat


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as coupled  # noqa: E402
import n7_mixed_glynn_graph_search as mixed  # noqa: E402


N = 7
V_DIM = 49
SUBSET_COUNT = 35
EXPECTED_MIDDLE_DIMENSION = 7 * 25 + 42 * 35


def common_graph_packet_factor_coefficients(
    tails: list[tuple[int, ...]] | list[list[int]], prime: int
) -> np.ndarray:
    """Return a common-graph packet B as a (49,7,49) coefficient tensor."""

    if len(tails) != 42 or any(len(tail) != 6 for tail in tails):
        raise ValueError("a common-graph packet requires forty-two six-vectors")
    terms: list[np.ndarray] = []
    for block in range(N):
        factors = np.zeros((N, V_DIM), dtype=np.int64)
        coordinates = [block * N + column for column in range(1, N)]
        for index, coordinate in enumerate(coordinates):
            factors[index, coordinate] = 1
        factors[N - 1, coordinates[0]] = 1
        terms.append(factors)

    for tail in tails:
        factors = np.zeros((N, V_DIM), dtype=np.int64)
        for block in range(N):
            factors[block, block * N] = 1
            for coordinate, value in enumerate(tail, start=1):
                factors[block, block * N + coordinate] = value
        terms.append(factors % prime)
    if len(terms) != 49:
        raise AssertionError("packet B must have 49 terms")
    return np.asarray(terms, dtype=np.int64) % prime


def identity_packet_b_factor_coefficients(
    prime: int, extra_offset: int = 0
) -> np.ndarray:
    """Return the synchronized mixed-Glynn common-graph packet."""

    return common_graph_packet_factor_coefficients(
        mixed.tail_dictionary(extra_offset), prime
    )


def subset_product_rows(
    factor_values: np.ndarray, subset_size: int, prime: int
) -> tuple[tuple[tuple[int, ...], ...], np.ndarray]:
    subsets = tuple(itertools.combinations(range(N), subset_size))
    rows = np.empty((len(subsets), factor_values.shape[1]), dtype=np.int64)
    for row, subset in enumerate(subsets):
        value = np.ones(factor_values.shape[1], dtype=np.int64)
        for index in subset:
            value = value * factor_values[index] % prime
        rows[row] = value
    return subsets, rows


def walsh_dictionary_rank(maximum_degree: int) -> int:
    tails = mixed.tail_dictionary(0)
    characters = tuple(
        subset
        for degree in range(maximum_degree + 1)
        for subset in itertools.combinations(range(6), degree)
    )
    matrix = [
        [
            int(np.prod([tail[index] for index in subset], dtype=np.int64))
            if subset
            else 1
            for subset in characters
        ]
        for tail in tails
    ]
    return fmpz_mat(matrix).rank()


def modular_composite_rank(
    output_map: np.ndarray, input_map: np.ndarray, prime: int
) -> int:
    left = nmod_mat((np.asarray(output_map, dtype=np.int64) % prime).tolist(), prime)
    right = nmod_mat((np.asarray(input_map, dtype=np.int64) % prime).tolist(), prime)
    return (left * right).rank()


def independent_columns(matrix: np.ndarray, prime: int) -> list[int]:
    """Select a deterministic column basis by modular streaming elimination."""

    matrix = np.asarray(matrix, dtype=np.int64) % prime
    basis: dict[int, np.ndarray] = {}
    selected: list[int] = []
    for column in range(matrix.shape[1]):
        vector = matrix[:, column].copy()
        for pivot, old in basis.items():
            if vector[pivot]:
                vector = (vector - vector[pivot] * old) % prime
        support = np.flatnonzero(vector)
        if support.size == 0:
            continue
        pivot = int(support[0])
        vector = vector * pow(int(vector[pivot]), prime - 2, prime) % prime
        basis[pivot] = vector
        selected.append(column)
    return selected


def rank_factor_coordinates(
    columns: np.ndarray, selected: list[int], prime: int
) -> tuple[np.ndarray, np.ndarray]:
    """Write all columns in the selected column basis."""

    basis = np.asarray(columns[:, selected], dtype=np.int64) % prime
    pivot_rows = independent_columns(basis.T, prime)
    if len(pivot_rows) != len(selected):
        raise AssertionError("failed to select a square pivot submatrix")
    square = basis[pivot_rows, :]
    inverse = coupled.invert_matrix(square, prime)
    coordinates = inverse @ (columns[pivot_rows, :] % prime) % prime
    if np.any((basis @ coordinates - columns) % prime):
        raise AssertionError("rank-factor coordinates failed reconstruction")
    return basis, coordinates


def labelled_middle_maps(
    factors: np.ndarray,
    output_evaluations: np.ndarray,
    input_evaluations: np.ndarray,
    prime: int,
) -> tuple[np.ndarray, np.ndarray, list[int]]:
    """Construct projected rank-space factorizations for all 49 terms."""

    quadruples = tuple(itertools.combinations(range(N), 4))
    triples = tuple(itertools.combinations(range(N), 3))
    triple_index = {subset: index for index, subset in enumerate(triples)}
    complement_indices = [
        triple_index[tuple(index for index in range(N) if index not in subset)]
        for subset in quadruples
    ]
    output_blocks = []
    input_blocks = []
    local_dimensions = []
    for term in factors:
        output_values = term @ output_evaluations % prime
        input_values = term @ input_evaluations % prime
        _, products4 = subset_product_rows(output_values, 4, prime)
        _, products3 = subset_product_rows(input_values, 3, prime)
        formal_output = products4.T
        selected = independent_columns(formal_output, prime)
        output_basis, output_coordinates = rank_factor_coordinates(
            formal_output, selected, prime
        )
        input_map = output_coordinates @ products3[complement_indices] % prime
        local_dimension = len(selected)
        if coupled.modular_rank(input_map, prime) != local_dimension:
            raise AssertionError("input samples did not retain the local term rank")
        output_blocks.append(output_basis)
        input_blocks.append(input_map)
        local_dimensions.append(local_dimension)
    return np.column_stack(output_blocks), np.vstack(input_blocks), local_dimensions


def run_prime(prime: int, seed: int, evaluation_columns: int) -> dict[str, object]:
    rng = np.random.default_rng(seed + prime)
    output_evaluations = rng.integers(
        0, prime, size=(V_DIM, evaluation_columns), dtype=np.int64
    )
    input_evaluations = rng.integers(
        0, prime, size=(V_DIM, evaluation_columns), dtype=np.int64
    )
    factors = identity_packet_b_factor_coefficients(prime)
    started = time.perf_counter()
    output_map, input_map, local_dimensions = labelled_middle_maps(
        factors, output_evaluations, input_evaluations, prime
    )
    if local_dimensions != [25] * 7 + [35] * 42:
        raise AssertionError(("unexpected local middle dimensions", local_dimensions))
    if output_map.shape[1] != EXPECTED_MIDDLE_DIMENSION:
        raise AssertionError("wrong packet-B middle dimension")
    inclusion = coupled.kernel_image_defect_from_kernel(
        output_map, input_map, prime
    )
    rank_bc = modular_composite_rank(output_map, input_map, prime)
    rank3_dictionary = walsh_dictionary_rank(3)
    rank4_dictionary = walsh_dictionary_rank(4)
    structural_rank_c = 7 * 25 + 35 * rank3_dictionary
    structural_rank_b = 7 * 25 + 35 * rank4_dictionary
    if (rank3_dictionary, rank4_dictionary) != (35, 41):
        raise AssertionError("unexpected exact Walsh dictionary ranks")
    if (inclusion["rank_b"], inclusion["rank_c"]) != (
        structural_rank_b,
        structural_rank_c,
    ):
        raise AssertionError("evaluation maps did not retain the structural ranks")
    if rank_bc != structural_rank_c:
        raise AssertionError("the sampled input image was not injected by B")
    exact_defect = (
        EXPECTED_MIDDLE_DIMENSION
        - structural_rank_b
        - structural_rank_c
        + rank_bc
    )
    if exact_defect != inclusion["coupling_defect"]:
        raise AssertionError("projected and exact coupling defects disagree")
    return {
        "prime": prime,
        "evaluation_columns": evaluation_columns,
        "factor_tensor_shape": list(factors.shape),
        "output_map_shape": list(output_map.shape),
        "input_map_shape": list(input_map.shape),
        "local_middle_dimension_histogram": {"25": 7, "35": 42},
        "exact_walsh_dictionary_ranks": {
            "degree_at_most_3": rank3_dictionary,
            "degree_at_most_4": rank4_dictionary,
        },
        "structural_middle_sum_ranks": {
            "rank_b": structural_rank_b,
            "rank_c": structural_rank_c,
            "rank_bc": rank_bc,
        },
        "projected_inclusion": inclusion,
        "exact_characteristic_zero_coupling_defect": exact_defect,
        "elapsed_seconds": time.perf_counter() - started,
    }


def build_payload(seed: int, evaluation_columns: int) -> dict[str, object]:
    if evaluation_columns < EXPECTED_MIDDLE_DIMENSION:
        raise ValueError(
            f"evaluation-columns must be at least {EXPECTED_MIDDLE_DIMENSION}"
        )
    rows = [
        run_prime(prime, seed, evaluation_columns) for prime in coupled.PRIMES
    ]
    defects = [row["exact_characteristic_zero_coupling_defect"] for row in rows]
    if len(set(defects)) != 1:
        raise AssertionError("the two primes disagree on the coupling defect")
    return {
        "schema_version": 1,
        "status": "EXACT_SYNCHRONIZED_PACKET_B_COUPLING_DEFECT_35",
        "seed": seed,
        "packet": "B_synchronized_mixed_Glynn_identity_control",
        "term_count": 49,
        "middle_dimension": EXPECTED_MIDDLE_DIMENSION,
        "candidate_cardinality_checked_before_materialization": {
            "rank_six_terms": 7,
            "rank_seven_terms": 42,
            "formal_subsets_per_term": SUBSET_COUNT,
        },
        "conservative_peak_memory_mib": 320,
        "rows": rows,
        "claim_boundary": [
            "Exact integer Walsh ranks prove the true H3 and H4 dimensions of this fixed synchronized packet.",
            "The modular composite reaches the structural rank-C upper bound over both primes, so the characteristic-zero coupling defect is exactly 35.",
            "This packet is not a 49-term permanent identity; the result excludes only this synchronized packet from the Sylvester-equality locus.",
            "No arbitrary-packet, lower-50, or border-rank conclusion is made.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260822)
    parser.add_argument(
        "--evaluation-columns", type=int, default=EXPECTED_MIDDLE_DIMENSION
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.seed, args.evaluation_columns)
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        for row in payload["rows"]:
            row.pop("elapsed_seconds", None)
        for row in frozen["rows"]:
            row.pop("elapsed_seconds", None)
        if payload != frozen:
            raise SystemExit("n7 packet-B coupling probe JSON mismatch")
        print("PASS n7 packet-B coupling probe")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
