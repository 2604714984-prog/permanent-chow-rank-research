"""Exact certificate for the special fifteen-plane Fano exclusion (N6-066)."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k34_special_d_fano_exclusion.json"
PRIME = 1_000_003
COORDS = tuple((row, column) for row in range(3) for column in range(4))
L0 = tuple(COORDS.index((row, column)) for row in range(3) for column in (0, 1))
COMPLEMENT = tuple(index for index in range(12) if index not in L0)
OUTPUTS = tuple(
    (rows, columns)
    for rows in combinations(range(3), 2)
    for columns in combinations(range(4), 2)
    if columns != (0, 1)
)
TANGENT_POINTS = (
    (0, 0, 0, 1, 1, 0),
    (0, 0, 0, 1, 1, 1),
    (0, 0, 1, 0, 0, 1),
    (0, 0, 1, 0, 1, 1),
    (0, 1, 0, 0, 1, 0),
    (1, 0, 0, 0, 0, 1),
)


def beta_matrix(vector: list[int]) -> list[list[int]]:
    matrix = [[0] * 12 for _ in range(15)]
    for output, ((i, j), (c, d)) in enumerate(OUTPUTS):
        terms = (((i, c), (j, d)), ((j, d), (i, c)),
                 ((i, d), (j, c)), ((j, c), (i, d)))
        for source, target in terms:
            matrix[output][COORDS.index(target)] += vector[COORDS.index(source)]
    return matrix


def rref_mod(matrix: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    if not matrix:
        return [], []
    work = [[value % PRIME for value in row] for row in matrix]
    row = 0
    pivots: list[int] = []
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, PRIME)
        work[row] = [(value * inverse) % PRIME for value in work[row]]
        for index in range(len(work)):
            if index != row and work[index][column]:
                scalar = work[index][column]
                work[index] = [
                    (left - scalar * right) % PRIME
                    for left, right in zip(work[index], work[row])
                ]
        pivots.append(column)
        row += 1
        if row == len(work):
            break
    return work[:row], pivots


def nullspace_mod(matrix: list[list[int]]) -> list[list[int]]:
    reduced, pivots = rref_mod(matrix)
    width = len(matrix[0])
    free = [column for column in range(width) if column not in pivots]
    result = []
    for free_column in free:
        vector = [0] * width
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column] % PRIME
        result.append(vector)
    return result


def rank_mod(matrix: list[list[int]]) -> int:
    return len(rref_mod(matrix)[1])


def coordinate_fixed_scan() -> dict[str, object]:
    pair_rank_histogram: dict[int, int] = {}
    bad_pairs: set[frozenset[int]] = set()
    for first, second in combinations(range(12), 2):
        vector = [int(index in (first, second)) for index in range(12)]
        rank = rank_mod(beta_matrix(vector))
        pair_rank_histogram[rank] = pair_rank_histogram.get(rank, 0) + 1
        if rank > 6:
            bad_pairs.add(frozenset((first, second)))

    candidates = []
    for support in combinations(range(12), 6):
        if all(frozenset(pair) not in bad_pairs for pair in combinations(support, 2)):
            candidates.append(support)
    if candidates != [L0]:
        raise AssertionError(candidates)

    # The converse for L0 is structural; this finite check is only a regression.
    l0_binary_maximum = 0
    for mask in range(1, 1 << 6):
        vector = [0] * 12
        for position, coordinate in enumerate(L0):
            vector[coordinate] = (mask >> position) & 1
        l0_binary_maximum = max(l0_binary_maximum, rank_mod(beta_matrix(vector)))
    if l0_binary_maximum != 6:
        raise AssertionError(l0_binary_maximum)
    return {
        "coordinate_six_plane_count": 924,
        "pair_sum_rank_histogram": {str(key): pair_rank_histogram[key] for key in sorted(pair_rank_histogram)},
        "bad_pair_count": len(bad_pairs),
        "compatible_six_supports": [list(L0)],
        "compatible_support_coordinates": [list(COORDS[index]) for index in L0],
        "l0_binary_point_maximum_rank": l0_binary_maximum,
    }


def tangent_certificate() -> dict[str, object]:
    equations: list[list[int]] = []
    rank_growth = []
    point_rows = []
    for values in TANGENT_POINTS:
        vector = [0] * 12
        for coordinate, value in zip(L0, values):
            vector[coordinate] = value
        beta = beta_matrix(vector)
        if rank_mod(beta) != 6:
            raise AssertionError((values, rank_mod(beta)))
        right_kernel = nullspace_mod(beta)
        left_kernel = nullspace_mod([list(column) for column in zip(*beta)])
        before = len(equations)
        for right in right_kernel:
            for left in left_kernel:
                row = [0] * 36
                for output_position, output_coordinate in enumerate(COMPLEMENT):
                    direction = beta_matrix([int(index == output_coordinate) for index in range(12)])
                    pairing = sum(
                        left[i] * sum(direction[i][j] * right[j] for j in range(12))
                        for i in range(15)
                    ) % PRIME
                    if pairing:
                        for source_position, source_coordinate in enumerate(L0):
                            row[6 * output_position + source_position] = (
                                row[6 * output_position + source_position]
                                + pairing * vector[source_coordinate]
                            ) % PRIME
                if any(row):
                    equations.append(row)
        current_rank = rank_mod(equations)
        rank_growth.append(current_rank)
        point_rows.append(len(equations) - before)
    if rank_growth != [6, 12, 18, 24, 30, 36]:
        raise AssertionError(rank_growth)
    return {
        "prime": PRIME,
        "grassmann_tangent_dimension": 36,
        "rank_six_points_in_l0_coordinates": [list(point) for point in TANGENT_POINTS],
        "nonzero_equation_counts_by_point": point_rows,
        "stacked_equation_count": len(equations),
        "stacked_rank_growth": rank_growth,
        "certified_tangent_dimension": 0,
    }


def certificate() -> dict[str, object]:
    return {
        "status": [
            "PURE_SPECIAL_D_FANO_EXCLUSION",
            "EXACT_MODULAR_TANGENT_CERTIFICATE",
            "N6-066",
        ],
        "space": {
            "ambient_dimension": 12,
            "special_quadratic_dimension": 15,
            "missing_column_pair": [0, 1],
        },
        "fixed_support_scan": coordinate_fixed_scan(),
        "tangent_certificate": tangent_certificate(),
        "pure_theorem": {
            "rank_six_fano_scheme_is_one_reduced_point": True,
            "unique_plane": "A3 tensor span(b0,b1)",
            "complementary_cross_free_pair_is_impossible": True,
            "transpose_and_coordinate_permutations_apply": True,
        },
        "claim_boundary": (
            "This excludes an actual complementary pair only for the special coordinate "
            "fifteen-plane obtained by deleting one column-pair fiber from the fixed K3,4 "
            "rectangle space. It does not classify the other vertical orbits, exclude the "
            "full b=50 endpoint, or prove ChowRank(perm_6)>=28."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    actual = certificate()
    expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit("certificate differs from frozen JSON")
    print("N6-066 PASS")


if __name__ == "__main__":
    main()
