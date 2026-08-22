#!/usr/bin/env python3
"""Exact barrier to a central-only lower-27 argument for ``perm_6``.

The displayed twenty Chow terms are not a decomposition of the permanent.
They reproduce the numerical central conditions forced by N6-032, while
their middle third-Koszul image loses at least 286260 dimensions relative to
twenty one-term caps.  The default replay is lightweight.  Pass
``--replay-central`` to reconstruct the integer middle catalectic matrices
and verify the displayed characteristic-zero determinants by Bareiss
elimination.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path


VARIABLES = 36
ACTIVE = 6
INACTIVE = VARIABLES - ACTIVE

FACTOR_FAMILIES = (
    (
        (1, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    (
        (1, 1, 0, 0, 0, 0),
        (1, 0, 1, 0, 0, 0),
        (0, 1, 1, 0, 0, 0),
        (0, 0, 0, 1, 1, 0),
        (0, 0, 0, 1, 0, 1),
        (0, 0, 0, 0, 1, 1),
    ),
    (
        (-1, 1, 0, -1, 1, -1),
        (1, 1, -1, 1, 1, 1),
        (1, -1, 1, 0, -1, 1),
        (-1, 0, 0, 0, -1, 1),
        (1, 1, -1, 1, -1, 1),
        (1, 0, -1, 1, -1, 0),
    ),
)

COORDINATE_SUPPORTS = (
    (0, 4, 9, 20, 29, 35),
    (0, 10, 27, 28, 33, 34),
    (4, 6, 16, 18, 32, 34),
    (2, 17, 19, 33, 34, 35),
    (14, 23, 25, 26, 31, 35),
    (3, 7, 14, 15, 22, 25),
    (4, 7, 9, 16, 28, 30),
    (7, 10, 12, 15, 28, 31),
)

PAIR_MINOR_INDICES = {
    (0, 1): (
        1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38,
        39, 40, 41, 42, 43, 44, 45, 47, 50,
    ),
    (0, 2): (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 32,
        33, 34, 38, 41, 42, 43, 44, 45, 50,
    ),
    (1, 2): (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 38, 40, 41, 43, 47,
    ),
}

PAIR_MINOR_DETERMINANTS = {
    (0, 1): 4_294_967_296,
    (0, 2): 633_318_697_598_976,
    (1, 2): 4_429_515_197_327_469_227_016_192,
}
TRIPLE_DETERMINANT = 6_438_146_982_013_471_831_931_322_630_144


def determinant_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant of a square integer matrix."""

    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign = -sign
        value = work[column][column]
        for row in range(column + 1, size):
            for other in range(column + 1, size):
                numerator = (
                    work[row][other] * value
                    - work[row][column] * work[column][other]
                )
                if numerator % previous:
                    raise ArithmeticError("nonexact Bareiss division")
                work[row][other] = numerator // previous
        previous = value
    return sign * work[-1][-1]


def factor_determinant(factors: tuple[tuple[int, ...], ...]) -> int:
    return determinant_bareiss([list(row) for row in factors])


def exponent_monomials(degree: int) -> list[tuple[int, ...]]:
    return [
        tuple(indices.count(variable) for variable in range(ACTIVE))
        for indices in combinations_with_replacement(range(ACTIVE), degree)
    ]


def product_polynomial(
    factors: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], int]:
    polynomial = {(0,) * ACTIVE: 1}
    for factor in factors:
        lifted: dict[tuple[int, ...], int] = defaultdict(int)
        for exponent, coefficient in polynomial.items():
            for variable, scalar in enumerate(factor):
                if not scalar:
                    continue
                new_exponent = list(exponent)
                new_exponent[variable] += 1
                lifted[tuple(new_exponent)] += coefficient * scalar
        polynomial = dict(lifted)
    return polynomial


def middle_catalectic(
    factors: tuple[tuple[int, ...], ...],
) -> list[list[int]]:
    """Integer matrix of the third derivative to cubic map."""

    cubics = exponent_monomials(3)
    polynomial = product_polynomial(factors)
    matrix = [[0] * len(cubics) for _ in cubics]
    for column, derivative in enumerate(cubics):
        for row, output in enumerate(cubics):
            exponent = tuple(
                derivative[index] + output[index]
                for index in range(ACTIVE)
            )
            coefficient = polynomial.get(exponent, 0)
            multiplier = 1
            for index in range(ACTIVE):
                for value in range(output[index] + 1, exponent[index] + 1):
                    multiplier *= value
            matrix[row][column] = coefficient * multiplier
    return matrix


def add_matrices(*matrices: list[list[int]]) -> list[list[int]]:
    return [
        [sum(matrix[row][column] for matrix in matrices) for column in range(56)]
        for row in range(56)
    ]


def principal_minor(matrix: list[list[int]], indices: tuple[int, ...]) -> list[list[int]]:
    return [[matrix[row][column] for column in indices] for row in indices]


def exact_central_replay() -> dict[str, object]:
    matrices = [middle_catalectic(factors) for factors in FACTOR_FAMILIES]
    pair_determinants = {}
    for pair, indices in PAIR_MINOR_INDICES.items():
        summed = add_matrices(matrices[pair[0]], matrices[pair[1]])
        determinant = determinant_bareiss(principal_minor(summed, indices))
        if determinant != PAIR_MINOR_DETERMINANTS[pair]:
            raise AssertionError((pair, determinant))
        pair_determinants[f"{pair[0]}{pair[1]}"] = determinant
    triple = determinant_bareiss(add_matrices(*matrices))
    if triple != TRIPLE_DETERMINANT:
        raise AssertionError(triple)
    return {
        "pair_minor_determinants": pair_determinants,
        "triple_full_determinant": triple,
    }


def koszul_rank(output_degree: int, wedge_degree: int) -> int:
    """Rank in the exact polynomial Koszul complex on six variables."""

    if wedge_degree < 0 or wedge_degree > ACTIVE:
        return 0
    domain = comb(output_degree + ACTIVE - 1, ACTIVE - 1) * comb(
        ACTIVE, wedge_degree
    )
    if wedge_degree == 0:
        return domain
    return domain - koszul_rank(output_degree + 1, wedge_degree - 1)


def ambient_rank(internal: list[int], wedge_degree: int) -> int:
    return sum(
        comb(INACTIVE, inactive) * internal[wedge_degree - inactive]
        for inactive in range(wedge_degree + 1)
        if 0 <= wedge_degree - inactive < len(internal)
    )


def support_audit() -> dict[str, object]:
    groups = tuple(set(range(6 * block, 6 * block + 6)) for block in range(4))
    supports = tuple(set(support) for support in COORDINATE_SUPPORTS)
    pair_max = max(len(left & right) for left, right in combinations(supports, 2))
    group_max = max(len(support & group) for support in supports for group in groups)
    if pair_max > 2 or group_max > 2:
        raise AssertionError((pair_max, group_max))
    return {
        "coordinate_support_pair_intersection_maximum": pair_max,
        "coordinate_support_to_six_block_intersection_maximum": group_max,
        "consequence": (
            "all coordinate-term cubic divisor spaces are pairwise disjoint "
            "and disjoint from every Sym^3 of a six-variable block"
        ),
    }


def subset_rank(selected_per_block: tuple[int, int, int, int], coordinate_count: int) -> int:
    local = (0, 20, 40, 56)
    return sum(local[count] for count in selected_per_block) + 20 * coordinate_count


def exhaustive_subset_profile() -> dict[str, object]:
    histogram: dict[int, int] = defaultdict(int)
    minimum_margin = 10**9
    nonempty = 0
    full_rank_terms = 20
    for counts in (
        (a, b, c, d)
        for a in range(4)
        for b in range(4)
        for c in range(4)
        for d in range(4)
    ):
        multiplicity = 1
        for count in counts:
            multiplicity *= comb(3, count)
        for coordinate_count in range(9):
            size = sum(counts) + coordinate_count
            if size == 0:
                continue
            copies = multiplicity * comb(8, coordinate_count)
            rank = subset_rank(counts, coordinate_count)
            margin = rank - 20 * (size - 1)
            if margin <= 0:
                raise AssertionError((counts, coordinate_count, rank))
            histogram[rank - 20 * size] += copies
            minimum_margin = min(minimum_margin, margin)
            nonempty += copies
    if nonempty != 2**20 - 1:
        raise AssertionError(nonempty)
    return {
        "nonempty_subsets_checked_by_exact_count_profile": nonempty,
        "rank_formula": (
            "20*s - 4 times the number of completed three-term blocks"
        ),
        "rank_defect_histogram": {
            str(defect): count for defect, count in sorted(histogram.items())
        },
        "minimum_margin_over_twenty_times_one_fewer_term": minimum_margin,
        "full_twenty_term_middle_rank": subset_rank((3, 3, 3, 3), 8),
        "full_middle_rank_terms": full_rank_terms,
    }


def build_payload(replay_central: bool = False) -> dict[str, object]:
    factor_determinants = [factor_determinant(factors) for factors in FACTOR_FAMILIES]
    if factor_determinants != [1, 4, 2]:
        raise AssertionError(factor_determinants)
    supports = support_audit()
    profile = exhaustive_subset_profile()
    if profile["full_twenty_term_middle_rank"] != 384:
        raise AssertionError(profile)

    internal_full = [koszul_rank(3, wedge) for wedge in range(7)]
    if internal_full != [56, 210, 336, 280, 120, 21, 0]:
        raise AssertionError(internal_full)
    triple_ambient = ambient_rank(internal_full, 3)
    if triple_ambient != 329_070:
        raise AssertionError(triple_ambient)
    one_term_internal = [20, 105, 216, 190, 84, 15, 0]
    one_term = ambient_rank(one_term_internal, 3)
    if one_term != 133_545:
        raise AssertionError(one_term)
    twenty_cap = 20 * one_term
    aggregate_upper = 4 * triple_ambient + 8 * one_term
    collision_lower = twenty_cap - aggregate_upper
    if collision_lower != 286_260:
        raise AssertionError(collision_lower)

    central_replay = exact_central_replay() if replay_central else None
    return {
        "status": "G034_HEREDITARY_CENTRAL_KOSZUL_BARRIER",
        "field": "characteristic zero",
        "factor_families": FACTOR_FAMILIES,
        "factor_matrix_determinants": factor_determinants,
        "three_term_central_rank_profile": [0, 20, 40, 56],
        "pair_minor_indices": {
            f"{left}{right}": indices
            for (left, right), indices in PAIR_MINOR_INDICES.items()
        },
        "pair_minor_determinants": {
            f"{left}{right}": determinant
            for (left, right), determinant in PAIR_MINOR_DETERMINANTS.items()
        },
        "triple_full_determinant": TRIPLE_DETERMINANT,
        "coordinate_supports": COORDINATE_SUPPORTS,
        "support_audit": supports,
        "twenty_term_subset_profile": profile,
        "full_symmetric_cubic_internal_koszul_ranks": internal_full,
        "one_term_internal_koszul_ranks": one_term_internal,
        "completed_three_term_block_ambient_middle_third_koszul_rank": triple_ambient,
        "single_term_ambient_middle_third_koszul_cap": one_term,
        "twenty_single_term_cap": twenty_cap,
        "twenty_term_aggregate_rank_upper": aggregate_upper,
        "aggregate_collision_lower": collision_lower,
        "two_sided_defect_example": {
            "ambient_polynomial": "sum of four completed three-term blocks",
            "six_term_subsum": "sum of any two completed blocks",
            "six_term_rank": 2 * triple_ambient,
            "column_intersection_c": 2 * triple_ambient,
            "row_intersection_s": 2 * triple_ambient,
            "c_plus_s_minus_r": 2 * triple_ambient,
            "reason": "the four variable blocks make both matrices block diagonal",
        },
        "central_replay_performed": replay_central,
        "central_replay": central_replay,
        "theorem": (
            "Hereditary central minimality, full residual middle rank 384, "
            "and twenty full-rank terms do not by themselves bound middle "
            "third-Koszul aggregate collision or two-sided overlap defect."
        ),
        "claim_boundary": (
            "The twenty terms do not decompose perm_6 and do not satisfy the "
            "permanent-specific identity Q=perm_6-H or its high-incidence "
            "colored quotient-relation geometry. This barrier does not change "
            "26 <= ChowRank(perm_6) <= 32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-central", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.replay_central)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_HEREDITARY_CENTRAL_KOSZUL_BARRIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
