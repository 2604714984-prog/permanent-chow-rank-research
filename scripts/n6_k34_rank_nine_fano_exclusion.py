#!/usr/bin/env python3
"""Exact regression certificate for the pure N6-063 K3,4 theorem.

The script checks only finite coordinate and tangent certificates.  The
projective torus argument which promotes them to arbitrary characteristic-zero
six-planes is the pure proof in the accompanying note.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k34_rank_nine_fano_exclusion.json"
PRIME = 1_000_003
ROWS = tuple(combinations(range(3), 2))
COLS = tuple(combinations(range(4), 2))


def beta_matrix(vector: list[int]) -> list[list[int]]:
    """The 18 by 12 matrix of y -> beta(vector,y)."""
    answer = [[0 for _ in range(12)] for _ in range(18)]
    for row_index, (i, j) in enumerate(ROWS):
        for column_index, (c, d) in enumerate(COLS):
            target = 6 * row_index + column_index
            answer[target][4 * j + d] += vector[4 * i + c]
            answer[target][4 * i + c] += vector[4 * j + d]
            answer[target][4 * j + c] += vector[4 * i + d]
            answer[target][4 * i + d] += vector[4 * j + c]
    return answer


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector, strict=True)) for row in matrix]


def left_matrix_vector(vector: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        sum(vector[row] * matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    ]


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            coefficient = work[row][column]
            work[row] = [
                (entry - coefficient * pivot_entry) % prime
                for entry, pivot_entry in zip(
                    work[row], work[rank], strict=True
                )
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def coordinate_rectangles() -> list[tuple[int, ...]]:
    answer: list[tuple[int, ...]] = []
    for row_set in combinations(range(3), 2):
        for column_set in combinations(range(4), 3):
            answer.append(tuple(4 * row + column for row in row_set for column in column_set))
    for column_set in combinations(range(4), 2):
        answer.append(tuple(4 * row + column for row in range(3) for column in column_set))
    return sorted(answer)


def fixed_support_scan() -> dict[str, object]:
    """One exact rational witness point for each coordinate six-plane.

    A modular rank is a lower bound for characteristic-zero rank.  The weights
    were chosen only to make all 906 nonrectangles display rank at least ten.
    Rectangle upper bounds are supplied by the pure proof, not this scan.
    """
    weights = (1, 2, 3, 5, 7, 11)
    rectangles = set(coordinate_rectangles())
    counts: Counter[int] = Counter()
    low_supports: list[tuple[int, ...]] = []
    for support in combinations(range(12), 6):
        vector = [0] * 12
        for index, value in zip(support, weights, strict=True):
            vector[index] = value
        rank = rank_mod(beta_matrix(vector))
        counts[rank] += 1
        if rank <= 9:
            low_supports.append(support)
    if set(low_supports) != rectangles:
        raise AssertionError("fixed support scan did not isolate the rectangles")
    return {
        "total_coordinate_six_planes": 924,
        "witness_coefficients_in_support_order": list(weights),
        "modulus": PRIME,
        "rank_histogram": {str(key): counts[key] for key in sorted(counts)},
        "rank_at_most_nine_supports": [list(support) for support in low_supports],
        "rectangle_count": len(rectangles),
    }


def unit(index: int, size: int) -> list[int]:
    answer = [0] * size
    answer[index] = 1
    return answer


def tangent_pairing(
    x: list[int], kernel: list[int], cokernel: list[int], output: int, source: int
) -> int:
    direction = beta_matrix(unit(output, 12))
    return x[source] * sum(
        cokernel[row] * value
        for row, value in enumerate(matrix_vector(direction, kernel))
    )


def verify_witness(
    x_support: dict[int, int],
    kernel_support: dict[int, int],
    cokernel_support: dict[int, int],
    directions: list[tuple[int, int]],
    expected: list[int],
) -> dict[str, object]:
    x = [0] * 12
    kernel = [0] * 12
    cokernel = [0] * 18
    for index, value in x_support.items():
        x[index] = value
    for index, value in kernel_support.items():
        kernel[index] = value
    for index, value in cokernel_support.items():
        cokernel[index] = value
    matrix = beta_matrix(x)
    if rank_mod(matrix) != 9:
        raise AssertionError("tangent witness point does not have rank nine")
    if any(matrix_vector(matrix, kernel)):
        raise AssertionError("claimed kernel vector is not in the kernel")
    if any(left_matrix_vector(cokernel, matrix)):
        raise AssertionError("claimed cokernel vector is not in the left kernel")
    actual = [
        tangent_pairing(x, kernel, cokernel, output, source)
        for output, source in directions
    ]
    if actual != expected:
        raise AssertionError((actual, expected))
    return {
        "x": x,
        "kernel": kernel,
        "left_kernel": cokernel,
        "directions_output_from_source": [list(item) for item in directions],
        "pairings": actual,
    }


def tangent_certificates() -> dict[str, object]:
    two_by_three_x = [
        verify_witness({0: 1, 1: 1, 6: 1}, {4: 1, 5: -1}, {2: 1, 4: -1}, [(3, 0), (7, 4)], [2, 0]),
        verify_witness({1: 1, 4: 1, 6: 1}, {0: 1, 2: -1}, {2: 1, 5: -1}, [(3, 0), (7, 4)], [0, 2]),
    ]
    two_by_three_y = [
        verify_witness({0: 1, 1: 1, 6: 1}, {2: 1}, {7: 1, 9: -1}, [(8, 0), (9, 1), (10, 2)], [1, -1, 0]),
        verify_witness({0: 1, 1: 1, 6: 1}, {0: 1, 1: 1, 6: -1}, {6: 1, 13: -1, 15: -1}, [(8, 0), (9, 1), (10, 2)], [2, 2, 0]),
        verify_witness({0: 1, 2: 1, 5: 1}, {1: 1}, {6: 1, 9: -1}, [(8, 0), (9, 1), (10, 2)], [1, 0, -1]),
    ]
    two_by_three_singletons = [
        verify_witness({1: 1, 2: 1, 4: 1}, {5: 1, 6: -1}, {4: 1, 5: -1}, [(3, 4)], [2]),
        verify_witness({1: 1, 6: 1}, {2: 1}, {7: 1}, [(8, 1)], [1]),
        verify_witness({0: 1, 5: 1}, {1: 1}, {10: 1}, [(11, 0)], [1]),
    ]
    three_by_two_z = [
        verify_witness({0: 1, 4: 1, 9: 1}, {1: 1, 5: -1}, {3: 1}, [(2, 0), (6, 4), (10, 8)], [-1, 1, 0]),
        verify_witness({0: 1, 4: 1, 9: 1}, {0: 1, 4: 1, 9: -1}, {1: 1, 9: -1, 15: -1}, [(2, 0), (6, 4), (10, 8)], [2, 2, 0]),
        verify_witness({0: 1, 5: 1, 8: 1}, {1: 1, 9: -1}, {9: 1}, [(2, 0), (6, 4), (10, 8)], [-1, 0, 1]),
    ]
    three_by_two_singleton = verify_witness(
        {4: 1, 9: 1}, {5: 1}, {3: 1}, [(2, 4)], [1]
    )
    x_matrix = [item["pairings"] for item in two_by_three_x]
    y_matrix = [item["pairings"] for item in two_by_three_y]
    z_matrix = [item["pairings"] for item in three_by_two_z]
    if rank_mod(x_matrix) != 2 or rank_mod(y_matrix) != 3 or rank_mod(z_matrix) != 3:
        raise AssertionError("a multiple-weight tangent block was not killed")
    return {
        "two_by_three": {
            "dimension_of_grassmann_tangent": 36,
            "two_dimensional_weight_blocks": 3,
            "three_dimensional_weight_blocks": 2,
            "singleton_weight_spaces": 24,
            "representative_two_block_witnesses": two_by_three_x,
            "representative_three_block_witnesses": two_by_three_y,
            "representative_singleton_orbit_witnesses": two_by_three_singletons,
            "certified_tangent_dimension": 0,
        },
        "three_by_two": {
            "dimension_of_grassmann_tangent": 36,
            "three_dimensional_weight_blocks": 4,
            "singleton_weight_spaces": 24,
            "representative_three_block_witnesses": three_by_two_z,
            "representative_singleton_orbit_witness": three_by_two_singleton,
            "certified_tangent_dimension": 0,
        },
    }


def cross_image_dimension(first: tuple[int, ...], second: tuple[int, ...]) -> int:
    coordinates: set[tuple[int, int, int, int]] = set()
    for left in first:
        i, c = divmod(left, 4)
        for right in second:
            j, d = divmod(right, 4)
            if i == j or c == d:
                continue
            row_pair = tuple(sorted((i, j)))
            column_pair = tuple(sorted((c, d)))
            coordinates.add((*row_pair, *column_pair))
    return len(coordinates)


def pair_histogram() -> dict[str, object]:
    rectangles = coordinate_rectangles()
    counts = Counter(
        cross_image_dimension(first, second)
        for first in rectangles
        for second in rectangles
    )
    low_pairs = [
        (first_index, second_index)
        for first_index, first in enumerate(rectangles)
        for second_index, second in enumerate(rectangles)
        if cross_image_dimension(first, second) <= 3
    ]
    diagonal = [(index, index) for index in range(18)]
    if low_pairs != diagonal:
        raise AssertionError("rank-at-most-three pair incidence is not diagonal")
    return {
        "ordered_pair_count": 324,
        "cross_image_dimension_histogram": {
            str(key): counts[key] for key in sorted(counts)
        },
        "dimension_at_most_three_pairs": [list(pair) for pair in low_pairs],
        "dimension_at_most_three_is_exactly_diagonal": True,
    }


def build_payload() -> dict[str, object]:
    return {
        "schema": "n6-k34-rank-nine-fano-exclusion-v1",
        "status": "EXACT_COORDINATE_CERTIFICATE_PLUS_PURE_GLOBAL_PROOF",
        "fixed_support_scan": fixed_support_scan(),
        "tangent_certificates": tangent_certificates(),
        "rectangle_pair_incidence": pair_histogram(),
        "pure_theorem": {
            "rank_nine_fano_scheme_has_exactly_eighteen_reduced_points": True,
            "cross_image_dimension_at_most_three_pair_incidence_is_diagonal": True,
            "complementary_pair_in_fixed_K3_4_layer_is_impossible": True,
        },
        "claim_boundary": (
            "The exact replay checks coordinate supports, tangent witnesses, and "
            "rectangle pairs. The arbitrary-point classification is the projective "
            "torus proof, not a finite-field enumeration. This fixed K3,4 theorem "
            "does not control a general twelve-plane whose torus limit is K3,4, "
            "because the two complementary six-planes may collide in the limit; "
            "it does not exclude b=50 or prove ChowRank(perm_6)>=28."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen JSON does not match regenerated payload")
        print(f"verified {args.verify_json}")
    if args.write_json is not None:
        args.write_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"wrote {args.write_json}")
    if args.verify_json is None and args.write_json is None:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
