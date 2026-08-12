#!/usr/bin/env python3
"""Exact G-047 squarefree-coproduct colored barrier at the b=50 endpoint."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


N = 6
PRIME = 1_000_003
PAIRS = list(combinations(range(N), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
TRIPLES = list(combinations(range(N), 3))
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_squarefree_coproduct_colored_barrier.json"

DIAGONALS = (
    (152746, 481851, 477026, 997949, 808226, 183237, 739785, 412126, 767515, 366726, 454573, 531487, 838883, 115312, 558788),
    (609383, 888268, 204215, 952504, 565421, 968860, 376098, 489831, 50878, 695700, 527980, 224944, 631288, 232466, 962104),
    (155369, 709146, 645887, 375641, 177929, 581348, 747118, 693021, 637359, 191349, 403008, 307027, 647494, 449955, 593759),
    (748993, 478464, 979589, 753766, 730305, 770585, 858009, 225341, 722559, 81829, 956686, 632023, 775048, 127842, 686113),
    (20483, 914216, 207485, 767459, 808167, 238680, 410024, 346704, 7071, 748485, 131191, 845897, 857428, 17536, 956802),
    (920754, 620050, 366078, 608932, 829134, 113695, 997812, 2081, 327386, 549493, 805644, 598186, 350958, 306954, 171745),
)

# (color, target pair index, source pair index, integer coefficient).
SHEARS = (
    (1, 11, 12, 543658),
    (3, 4, 6, 661495),
    (3, 0, 10, 360385),
    (2, 5, 13, 559236),
    (2, 3, 6, 599818),
)


def modular_rank(columns: list[list[int]], prime: int = PRIME) -> int:
    if not columns:
        return 0
    work = [[entry % prime for entry in row] for row in zip(*columns, strict=True)]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        for row in range(rank + 1, len(work)):
            if not work[row][column]:
                continue
            scale = work[row][column] * inverse % prime
            for target in range(column, len(work[0])):
                work[row][target] = (
                    work[row][target] - scale * work[rank][target]
                ) % prime
        rank += 1
        if rank == len(work):
            break
    return rank


def quotient_maps() -> list[list[list[int]]]:
    maps: list[list[list[int]]] = []
    for diagonal in DIAGONALS:
        matrix = [[0] * 15 for _ in range(15)]
        for index, value in enumerate(diagonal):
            matrix[index][index] = value
        maps.append(matrix)
    for color, target, source, coefficient in SHEARS:
        maps[color][target][source] += coefficient
    return maps


def coproduct_columns(q_map: list[list[int]]) -> list[list[int]]:
    """Columns of (id_U tensor q) composed with Delta: Lambda3 U -> U tensor W."""

    answer: list[list[int]] = []
    for triple in TRIPLES:
        column = [0] * 90
        for position, omitted in enumerate(triple):
            pair = tuple(value for value in triple if value != omitted)
            source = PAIR_INDEX[pair]
            sign = 1 if position % 2 == 0 else -1
            for target in range(15):
                column[omitted * 15 + target] += sign * q_map[target][source]
        answer.append(column)
    return answer


def subset_rows(all_columns: list[list[list[int]]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for count in range(1, N + 1):
        for colors in combinations(range(N), count):
            columns = [column for color in colors for column in all_columns[color]]
            modular_image_rank = modular_rank(columns)
            modular_nullity = 20 * count - modular_image_rank
            rows.append(
                {
                    "colors": list(colors),
                    "color_count": count,
                    "image_rank_mod_prime": modular_image_rank,
                    "modular_nullity": modular_nullity,
                    "rational_kernel_dimension_upper_bound": modular_nullity,
                }
            )
    return rows


def audit() -> dict[str, object]:
    q_maps = quotient_maps()
    individual_determinants = [
        1 if all(diagonal) else 0 for diagonal in DIAGONALS
    ]
    if individual_determinants != [1] * N:
        raise AssertionError(individual_determinants)

    all_columns = [coproduct_columns(q_map) for q_map in q_maps]
    rows = subset_rows(all_columns)
    endpoint_caps = {1: 0, 2: 2, 3: 10, 4: 20, 5: 40, 6: 50}
    grouped: dict[str, dict[str, object]] = {}
    for count in range(1, N + 1):
        selected = [row for row in rows if row["color_count"] == count]
        upper_bounds = [
            int(row["rational_kernel_dimension_upper_bound"])
            for row in selected
        ]
        if max(upper_bounds) > endpoint_caps[count]:
            raise AssertionError((count, upper_bounds, endpoint_caps[count]))
        grouped[str(count)] = {
            "number_of_subsets": len(selected),
            "modular_nullities_in_lexicographic_subset_order": upper_bounds,
            "rational_kernel_dimension_upper_bounds_in_lexicographic_subset_order": upper_bounds,
            "minimum_rational_kernel_dimension_upper_bound": min(upper_bounds),
            "maximum_rational_kernel_dimension_upper_bound": max(upper_bounds),
            "b50_subset_cap": endpoint_caps[count],
        }

    full_rank = next(
        int(row["image_rank_mod_prime"])
        for row in rows
        if row["color_count"] == N
    )
    if full_rank != 70:
        raise AssertionError(full_rank)

    return {
        "status": "EXACT_SQUAREFREE_COPRODUCT_COLORED_BARRIER_G047",
        "base_field": "Q",
        "fixed_parameters": {
            "pair_basis_lexicographic": [list(pair) for pair in PAIRS],
            "six_diagonals": [list(diagonal) for diagonal in DIAGONALS],
            "five_shears": [
                {
                    "color": color,
                    "target_pair_index": target,
                    "target_pair": list(PAIRS[target]),
                    "source_pair_index": source,
                    "source_pair": list(PAIRS[source]),
                    "coefficient": coefficient,
                }
                for color, target, source, coefficient in SHEARS
            ],
            "each_q_i_is_invertible_over_Q": True,
            "invertibility_reason": "every q_i is upper triangular with the displayed nonzero diagonal",
        },
        "construction": {
            "U_dimension": 6,
            "W": "Lambda^2 U, dimension 15",
            "each_color_domain": "Lambda^3 U, dimension 20",
            "color_map": "(id_U tensor q_i) composed with the canonical alternating coproduct Delta: Lambda^3 U -> U tensor Lambda^2 U",
        },
        "pure_seventy_support_upper_bound": {
            "diagonal_maps_have_common_60_coordinate_support": True,
            "each_disjoint_pair_shear_adds_at_most_two_new_coordinate_axes": True,
            "two_axis_reason": "for source pair bc and disjoint target pair de, the two omitted indices outside bcde already give diagonal-support axes, so only the two target endpoints d,e can give new axes",
            "number_of_shears": 5,
            "rational_full_image_rank_at_most": 70,
        },
        "exact_rank_certificate": {
            "prime": PRIME,
            "all_parameters_are_fixed_integers": True,
            "all_63_nonempty_subsets_checked": True,
            "mod_to_Q_direction": "for every displayed integer column matrix, rank over Q is at least rank modulo the prime; equivalently the rational kernel dimension is at most the displayed modular nullity",
            "full_rank_over_Q": 70,
            "full_rank_reason": "modular rank gives at least 70 and the pure coordinate-support argument gives at most 70",
        },
        "all_subset_rows": rows,
        "by_color_count": grouped,
        "strict_conclusion": "Even canonical per-color squarefree cubic coproducts followed by invertible color maps can have an exact fifty-dimensional six-color kernel while every proper-subset rational kernel has an exact modularly certified upper bound below its recorded b=50 cap. Per-color coproduct structure plus those caps cannot alone exclude the endpoint.",
        "claim_boundary": "This is not an actual six-term Chow configuration and not a b=50 or 27-term decomposition. Its six colors abstractly identify the same U; it does not realize six pairwise-transverse ambient factor spaces L_i, literal direct quadratic Chow spaces F_i, or the common-section cocycle forced by a single permanent quotient. Those cross-color ambient constraints remain available and are exactly what this barrier does not model.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = audit()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
