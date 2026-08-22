#!/usr/bin/env python3
"""Bounded finite-field search inside the two perm_7 N=49 equality packets.

This is an exploratory search, not a rank certificate.  Packet A is sampled
inside the tensor-split (column-uniform) locus, with fifth-Veronese defect
forced by projective-line packets.  Packet B uses seven direct rank-six
blocks and forty-two rank-seven graph complements.  In both cases we test
actual polynomial conditions (degree-six permanent-derivative containment,
and a direct degree-seven identity projection), rather than plane dimensions.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import math
import os
import random
import time
from pathlib import Path

import numpy as np
from flint import nmod_mat


N = 7
V_DIM = 49
PRIME = 65521
DEFAULT_EVALUATIONS = 400


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first, *tail)


MONOMIALS = {
    degree: tuple(compositions(degree, N)) for degree in (5, 6, 7)
}
MONOMIAL_INDEX_6 = {alpha: i for i, alpha in enumerate(MONOMIALS[6])}


def multinomial(alpha: tuple[int, ...]) -> int:
    result = math.factorial(sum(alpha))
    for value in alpha:
        result //= math.factorial(value)
    return result


MULTINOMIALS = {
    degree: np.asarray([multinomial(alpha) for alpha in MONOMIALS[degree]], dtype=np.int64)
    for degree in (5, 6, 7)
}


def modular_rank(rows: np.ndarray, prime: int = PRIME) -> int:
    array = np.asarray(rows, dtype=np.int64) % prime
    return nmod_mat(array.tolist(), prime).rank()


def small_rank(rows: np.ndarray, prime: int = PRIME) -> int:
    work = np.asarray(rows, dtype=np.int64).copy() % prime
    pivot = 0
    for column in range(work.shape[1]):
        choices = np.flatnonzero(work[pivot:, column])
        if choices.size == 0:
            continue
        selected = pivot + int(choices[0])
        work[[pivot, selected]] = work[[selected, pivot]]
        work[pivot] = work[pivot] * pow(int(work[pivot, column]), prime - 2, prime) % prime
        for row in range(work.shape[0]):
            if row != pivot and work[row, column]:
                work[row] = (work[row] - work[row, column] * work[pivot]) % prime
        pivot += 1
        if pivot == work.shape[0]:
            break
    return pivot


def normalize_projective(vector: np.ndarray) -> tuple[int, ...]:
    vector = np.asarray(vector, dtype=np.int64) % PRIME
    first = int(np.flatnonzero(vector)[0])
    vector = vector * pow(int(vector[first]), PRIME - 2, PRIME) % PRIME
    return tuple(int(value) for value in vector)


def random_nonzero_vector(rng: random.Random, length: int) -> np.ndarray:
    while True:
        vector = np.asarray([rng.randrange(PRIME) for _ in range(length)], dtype=np.int64)
        if np.any(vector):
            return vector


def random_line_points(rng: random.Random, count: int = 7) -> list[tuple[int, ...]]:
    while True:
        left = random_nonzero_vector(rng, N)
        right = random_nonzero_vector(rng, N)
        if small_rank(np.stack((left, right))) == 2:
            break
    parameters = rng.sample(range(PRIME), count)
    return [normalize_projective(left + parameter * right) for parameter in parameters]


def packet_a_points(seed: int, line_count: int) -> np.ndarray:
    rng = random.Random(seed)
    points: set[tuple[int, ...]] = set()
    while len(points) < 7 * line_count:
        candidate = random_line_points(rng)
        if not any(point in points for point in candidate):
            points.update(candidate)
    while len(points) < 49:
        points.add(normalize_projective(random_nonzero_vector(rng, N)))
    ordered = sorted(points)
    if len(ordered) != 49:
        raise AssertionError("packet A must have exactly 49 projective points")
    return np.asarray(ordered, dtype=np.int64)


def power_rows(points: np.ndarray, degree: int) -> np.ndarray:
    rows = np.empty((len(points), len(MONOMIALS[degree])), dtype=np.int64)
    for row_index, point in enumerate(points):
        row = MULTINOMIALS[degree].copy()
        for coordinate in range(N):
            exponents = np.asarray([alpha[coordinate] for alpha in MONOMIALS[degree]])
            row = row * np.asarray(
                [pow(int(point[coordinate]), int(exponent), PRIME) for exponent in exponents],
                dtype=np.int64,
            ) % PRIME
        rows[row_index] = row
    return rows


def packet_a_trial(seed: int, line_count: int) -> dict[str, int | str]:
    points = packet_a_points(seed, line_count)
    fifth = power_rows(points, 5)
    fifth_rank = modular_rank(fifth)
    tangent_rows = []
    for point, fifth_row in zip(points, fifth):
        for direction in range(N):
            row = np.zeros(len(MONOMIALS[6]), dtype=np.int64)
            for beta_index, beta in enumerate(MONOMIALS[5]):
                alpha = list(beta)
                alpha[direction] += 1
                coefficient = int(fifth_row[beta_index])
                row[MONOMIAL_INDEX_6[tuple(alpha)]] = coefficient
            tangent_rows.append(row)
    tangent = np.stack(tangent_rows)
    targets = np.zeros((N, len(MONOMIALS[6])), dtype=np.int64)
    for missing in range(N):
        alpha = tuple(0 if coordinate == missing else 1 for coordinate in range(N))
        targets[missing, MONOMIAL_INDEX_6[alpha]] = 1
    tangent_rank = modular_rank(tangent)
    augmented_rank = modular_rank(np.vstack((tangent, targets)))
    seventh = power_rows(points, 7)
    squarefree = np.zeros((1, len(MONOMIALS[7])), dtype=np.int64)
    squarefree[0, MONOMIALS[7].index((1,) * N)] = 1
    seventh_rank = modular_rank(seventh)
    seventh_augmented_rank = modular_rank(np.vstack((seventh, squarefree)))
    return {
        "packet": "A_tensor_split",
        "seed": seed,
        "forced_line_count": line_count,
        "fifth_power_rank": fifth_rank,
        "structural_degree_six_rank_cap": 343 - 12 * line_count,
        "degree_six_span_rank": tangent_rank,
        "degree_six_target_increment": augmented_rank - tangent_rank,
        "seventh_power_rank": seventh_rank,
        "degree_seven_target_increment": seventh_augmented_rank - seventh_rank,
    }


def permanent_dp(matrix: np.ndarray) -> int:
    size = matrix.shape[0]
    dp = {0: 1}
    for row in range(size):
        next_dp: dict[int, int] = {}
        for mask, value in dp.items():
            for column in range(size):
                if not (mask >> column) & 1:
                    new_mask = mask | (1 << column)
                    next_dp[new_mask] = (
                        next_dp.get(new_mask, 0) + value * int(matrix[row, column])
                    ) % PRIME
        dp = next_dp
    return dp[(1 << size) - 1]


def permanent_targets(evaluations: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sample_count = evaluations.shape[1]
    degree_six = np.empty((V_DIM, sample_count), dtype=np.int64)
    degree_seven = np.empty((1, sample_count), dtype=np.int64)
    for sample in range(sample_count):
        matrix = evaluations[:, sample].reshape((N, N))
        degree_seven[0, sample] = permanent_dp(matrix)
        target = 0
        for missing_row in range(N):
            retained_rows = [row for row in range(N) if row != missing_row]
            for missing_column in range(N):
                retained_columns = [column for column in range(N) if column != missing_column]
                degree_six[missing_row * N + missing_column, sample] = permanent_dp(
                    matrix[np.ix_(retained_rows, retained_columns)]
                )
    return degree_six, degree_seven


def random_invertible_mix(rng: random.Random) -> np.ndarray:
    matrix = np.eye(N, dtype=np.int64)
    for _ in range(18):
        source, target = rng.sample(range(N), 2)
        scalar = rng.randrange(1, PRIME)
        matrix[target] = (matrix[target] + scalar * matrix[source]) % PRIME
    matrix = matrix[np.asarray(rng.sample(range(N), N))]
    scales = np.asarray([rng.randrange(1, PRIME) for _ in range(N)], dtype=np.int64)
    return matrix * scales[:, None] % PRIME


def omitted_products(factor_values: np.ndarray) -> np.ndarray:
    rows, columns = factor_values.shape
    prefix = np.ones((rows + 1, columns), dtype=np.int64)
    suffix = np.ones((rows + 1, columns), dtype=np.int64)
    for index in range(rows):
        prefix[index + 1] = prefix[index] * factor_values[index] % PRIME
    for index in range(rows - 1, -1, -1):
        suffix[index] = suffix[index + 1] * factor_values[index] % PRIME
    return np.stack([prefix[index] * suffix[index + 1] % PRIME for index in range(rows)])


def modular_product_rows(factor_values: np.ndarray) -> np.ndarray:
    product = np.ones(factor_values.shape[1], dtype=np.int64)
    for row in factor_values:
        product = product * row % PRIME
    return product


def graph_packet_values(
    seed: int, evaluations: np.ndarray, family: str
) -> tuple[np.ndarray, np.ndarray]:
    rng = random.Random(seed)
    a_indices = [row * N + column for row in range(N) for column in range(1, N)]
    w_indices = [row * N for row in range(N)]
    a_values = evaluations[a_indices]
    w_values = evaluations[w_indices]
    derivative_rows = []
    term_rows = []

    for block in range(7):
        basis = a_values[6 * block : 6 * (block + 1)]
        factors = np.vstack((basis, basis[0]))
        derivative_rows.extend(omitted_products(factors))
        term_rows.append(modular_product_rows(factors))

    graphs: list[np.ndarray] = []
    if family == "glynn_graph":
        tails = rng.sample(list(itertools.product((-1, 1), repeat=6)), 42)
        for tail in tails:
            graph = np.zeros((42, N), dtype=np.int64)
            for row in range(N):
                graph[6 * row : 6 * (row + 1), row] = np.asarray(tail) % PRIME
            graphs.append(graph)
    elif family == "random_graph":
        attempts = 0
        while len(graphs) < 42:
            attempts += 1
            if attempts > 10000:
                raise RuntimeError("failed to construct pairwise transverse graph complements")
            graph = np.asarray(
                [[rng.randrange(PRIME) for _ in range(N)] for _ in range(42)],
                dtype=np.int64,
            )
            if all(small_rank(graph - previous) >= 5 for previous in graphs):
                graphs.append(graph)
    else:
        raise ValueError(f"unknown packet-B family {family}")

    for graph in graphs:
        base = (graph.T @ a_values + w_values) % PRIME
        mix = np.eye(N, dtype=np.int64) if family == "glynn_graph" else random_invertible_mix(rng)
        factors = mix @ base % PRIME
        derivative_rows.extend(omitted_products(factors))
        term_rows.append(modular_product_rows(factors))
    return np.asarray(derivative_rows, dtype=np.int64), np.asarray(term_rows, dtype=np.int64)


def packet_b_trial(
    seed: int,
    family: str,
    evaluations: np.ndarray,
    degree_six_targets: np.ndarray,
    degree_seven_target: np.ndarray,
) -> dict[str, int | str]:
    derivative_rows, term_rows = graph_packet_values(seed, evaluations, family)
    derivative_rank = modular_rank(derivative_rows)
    derivative_augmented_rank = modular_rank(
        np.vstack((derivative_rows, degree_six_targets))
    )
    term_rank = modular_rank(term_rows)
    term_augmented_rank = modular_rank(np.vstack((term_rows, degree_seven_target)))
    return {
        "packet": "B_graph_complement",
        "family": family,
        "seed": seed,
        "degree_six_generator_rows": int(derivative_rows.shape[0]),
        "degree_six_projected_rank": derivative_rank,
        "degree_six_target_increment": derivative_augmented_rank - derivative_rank,
        "degree_seven_projected_rank": term_rank,
        "degree_seven_target_increment": term_augmented_rank - term_rank,
    }


def auto_workers() -> int:
    logical = os.cpu_count() or 1
    return max(1, logical - 4)


def run(args: argparse.Namespace) -> dict[str, object]:
    workers = auto_workers() if args.workers == "auto" else int(args.workers)
    ceiling = auto_workers()
    if workers < 1 or workers > ceiling:
        raise SystemExit(f"workers must be in 1..{ceiling}; four logical CPUs stay free")
    rng = np.random.default_rng(args.seed)
    evaluations = rng.integers(
        0, PRIME, size=(V_DIM, args.evaluations), dtype=np.int64
    )
    degree_six_targets, degree_seven_target = permanent_targets(evaluations)
    jobs: list[tuple[str, int, int]] = []
    for line_count in (2, 3, 7):
        for index in range(args.a_candidates):
            jobs.append(("A", args.seed + 100000 * line_count + index, line_count))
    for index in range(args.b_candidates):
        jobs.append(("B_random", args.seed + 900000 + index, 0))
    for index in range(args.b_glynn_candidates):
        jobs.append(("B_glynn", args.seed + 1200000 + index, 0))

    started = time.perf_counter()
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = []
        for packet, seed, line_count in jobs:
            if packet == "A":
                futures.append(pool.submit(packet_a_trial, seed, line_count))
            else:
                futures.append(
                    pool.submit(
                        packet_b_trial,
                        seed,
                        "glynn_graph" if packet == "B_glynn" else "random_graph",
                        evaluations,
                        degree_six_targets,
                        degree_seven_target,
                    )
                )
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    elapsed = time.perf_counter() - started
    results.sort(key=lambda row: (str(row["packet"]), int(row["seed"])))
    packet_a = [row for row in results if row["packet"] == "A_tensor_split"]
    packet_b = [row for row in results if row["packet"] == "B_graph_complement"]
    return {
        "schema_version": 1,
        "status": "BOUNDED_FINITE_FIELD_SEARCH_NOT_A_RANK_CERTIFICATE",
        "field": f"F_{PRIME}",
        "seed": args.seed,
        "workers": workers,
        "logical_cpus_left_free": 4,
        "evaluation_columns_for_packet_B": args.evaluations,
        "candidate_count": len(jobs),
        "elapsed_seconds": elapsed,
        "candidates_per_second": len(jobs) / elapsed if elapsed else None,
        "packet_A_summary": {
            "count": len(packet_a),
            "minimum_fifth_power_rank": min((row["fifth_power_rank"] for row in packet_a), default=None),
            "minimum_degree_six_target_increment": min((row["degree_six_target_increment"] for row in packet_a), default=None),
            "zero_degree_six_increment_count": sum(row["degree_six_target_increment"] == 0 for row in packet_a),
            "zero_degree_seven_increment_count": sum(row["degree_seven_target_increment"] == 0 for row in packet_a),
        },
        "packet_B_summary": {
            "count": len(packet_b),
            "minimum_degree_six_target_increment": min((row["degree_six_target_increment"] for row in packet_b), default=None),
            "zero_degree_six_increment_count": sum(row["degree_six_target_increment"] == 0 for row in packet_b),
            "zero_degree_seven_increment_count": sum(row["degree_seven_target_increment"] == 0 for row in packet_b),
        },
        "results": results,
        "claim_boundary": [
            "Every positive target increment is a rigorous obstruction for that fixed finite-field sample.",
            "A zero increment after packet-B evaluation projection would be inconclusive and would require exact coefficient lifting.",
            "The search does not quantify over either equality packet and proves no Chow-rank or border-rank bound.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a-candidates", type=int, default=8, help="per line-count family")
    parser.add_argument("--b-candidates", type=int, default=8)
    parser.add_argument("--b-glynn-candidates", type=int, default=8)
    parser.add_argument("--evaluations", type=int, default=DEFAULT_EVALUATIONS)
    parser.add_argument("--workers", default="auto")
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if (
        args.a_candidates < 0
        or args.b_candidates < 0
        or args.b_glynn_candidates < 0
        or args.evaluations < 392
    ):
        raise SystemExit("candidate counts must be nonnegative and evaluations >= 392")
    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
