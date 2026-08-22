#!/usr/bin/env python3
"""Exact v6 audit for the section caps used in the lower-50 candidate.

This bounded computation does not assert ChowRank(perm_7) >= 50.  It
constructs one-dimensional Kruskal--Katona tables in two ways, constructs
every two-dimensional Ferrers capacity in two DP orientations, extends the
recursive section caps through 49 selected terms, and exhaustively checks a
small coordinate model independently of the dynamic programs.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


N = 7
NUMBER_OF_TERMS = 49


def kk_shadow(size: int, uniformity: int) -> int:
    """Kruskal--Katona lower shadow via the canonical binomial expansion."""

    if size == 0:
        return 0
    remainder = size
    upper = N + 1
    shadow = 0
    for degree in range(uniformity, 0, -1):
        choices = [
            value
            for value in range(degree, upper)
            if math.comb(value, degree) <= remainder
        ]
        value = max(choices)
        remainder -= math.comb(value, degree)
        shadow += math.comb(value, degree - 1)
        upper = value
        if remainder == 0:
            break
    assert remainder == 0
    return shadow


def colex_key(subset: tuple[int, ...]) -> int:
    return sum(
        math.comb(value - 1, index)
        for index, value in enumerate(subset, start=1)
    )


def enumerated_shadow_table(uniformity: int) -> tuple[int, ...]:
    """Independent check by explicit colex initial segments."""

    ordered = sorted(
        itertools.combinations(range(1, N + 1), uniformity), key=colex_key
    )
    answer = []
    for size in range(len(ordered) + 1):
        shadow = {
            member[:index] + member[index + 1 :]
            for member in ordered[:size]
            for index in range(uniformity)
        }
        answer.append(len(shadow))
    return tuple(answer)


def shadow_table(uniformity: int) -> tuple[int, ...]:
    formula = tuple(
        kk_shadow(size, uniformity)
        for size in range(math.comb(N, uniformity) + 1)
    )
    assert formula == enumerated_shadow_table(uniformity)
    return formula


def min_cost_by_area(table: tuple[int, ...]) -> tuple[int, ...]:
    """Minimum Ferrers product-shadow cost at every exact area."""

    width = len(table) - 1
    infinity = 10**9
    states: dict[tuple[int, int], int] = {(width, 0): 0}
    for row in range(1, width + 1):
        delta = table[row] - table[row - 1]
        following: dict[tuple[int, int], int] = {}
        for (previous, area), cost in states.items():
            for height in range(previous + 1):
                key = (height, area + height)
                new_cost = cost + delta * table[height]
                following[key] = min(following.get(key, infinity), new_cost)
        states = following
    costs = [infinity] * (width * width + 1)
    for (_, area), cost in states.items():
        costs[area] = min(costs[area], cost)
    assert all(cost < infinity for cost in costs)
    return tuple(costs)


def max_area_by_budget(table: tuple[int, ...], maximum_budget: int) -> tuple[int, ...]:
    """Same Ferrers problem with cost and area interchanged in the state."""

    width = len(table) - 1
    states: dict[tuple[int, int], int] = {(width, 0): 0}
    for row in range(1, width + 1):
        delta = table[row] - table[row - 1]
        following: dict[tuple[int, int], int] = {}
        for (previous, cost), area in states.items():
            for height in range(previous + 1):
                new_cost = cost + delta * table[height]
                if new_cost > maximum_budget:
                    continue
                key = (height, new_cost)
                following[key] = max(following.get(key, -1), area + height)
        states = following
    exact = [-1] * (maximum_budget + 1)
    for (_, cost), area in states.items():
        exact[cost] = max(exact[cost], area)
    capacities = []
    running = 0
    for area in exact:
        running = max(running, area)
        capacities.append(running)
    return tuple(capacities)


def ferrers_capacities() -> dict[int, tuple[int, ...]]:
    answer = {}
    for degree in range(2, 7):
        table = shadow_table(degree)
        maximum_budget = math.comb(N, degree - 1) ** 2
        costs = min_cost_by_area(table)
        from_costs = tuple(
            max(area for area, cost in enumerate(costs) if cost <= budget)
            for budget in range(maximum_budget + 1)
        )
        from_budgets = max_area_by_budget(table, maximum_budget)
        assert from_costs == from_budgets
        answer[degree] = from_costs
    return answer


def recursive_section_caps(
    ferrers: dict[int, tuple[int, ...]],
) -> tuple[dict[int, list[int]], dict[int, list[dict[str, int] | None]]]:
    """Universal caps C_d(q), now for every 0 <= q <= 49."""

    caps: dict[int, list[int]] = {
        1: [0]
        + [min(N * q, N**2) for q in range(1, NUMBER_OF_TERMS + 1)]
    }
    witnesses: dict[int, list[dict[str, int] | None]] = {
        1: [None] * (NUMBER_OF_TERMS + 1)
    }
    for degree in range(2, 7):
        one_term_cap = math.comb(N, degree)
        previous_ambient = math.comb(N, degree - 1) ** 2
        caps[degree] = [0]
        witnesses[degree] = [None]
        for q in range(1, NUMBER_OF_TERMS + 1):
            choices = []
            for local in range(1, q + 1):
                budget = min(caps[degree - 1][local], previous_ambient)
                local_cap = ferrers[degree][budget]
                aggregate = (q - local) * one_term_cap + local_cap
                choices.append((aggregate, local, budget, local_cap))
            aggregate, local, budget, local_cap = min(choices)
            caps[degree].append(aggregate)
            witnesses[degree].append(
                {
                    "q": q,
                    "local_terms": local,
                    "previous_degree_budget": budget,
                    "local_ferrers_cap": local_cap,
                    "aggregate_cap": aggregate,
                }
            )
            assert 0 <= aggregate <= math.comb(N, degree) ** 2
    return caps, witnesses


def partition_dp(weights: list[int]) -> tuple[int, tuple[int, ...]]:
    """Unordered-block optimum, computed first as an ordered composition DP."""

    negative = -10**9
    values = [0] + [negative] * NUMBER_OF_TERMS
    choices = [0] * (NUMBER_OF_TERMS + 1)
    for total in range(1, NUMBER_OF_TERMS + 1):
        for block in range(1, total + 1):
            candidate = values[total - block] + weights[block]
            if candidate > values[total]:
                values[total] = candidate
                choices[total] = block
    blocks = []
    remaining = NUMBER_OF_TERMS
    while remaining:
        block = choices[remaining]
        assert block > 0
        blocks.append(block)
        remaining -= block
    return values[NUMBER_OF_TERMS], tuple(sorted(blocks))


def exhaustive_partition_optimum(
    weights: list[int],
) -> tuple[int, tuple[tuple[int, ...], ...], int]:
    """Independent audit over all 173,525 integer partitions of 49."""

    best = -1
    maximizers: list[tuple[int, ...]] = []
    count = 0

    def visit(
        remaining: int, minimum_part: int, parts: tuple[int, ...], value: int
    ) -> None:
        nonlocal best, maximizers, count
        if remaining == 0:
            count += 1
            if value > best:
                best = value
                maximizers = [parts]
            elif value == best:
                maximizers.append(parts)
            return
        for part in range(minimum_part, remaining + 1):
            visit(remaining - part, part, parts + (part,), value + weights[part])

    visit(NUMBER_OF_TERMS, 1, (), 0)
    return best, tuple(maximizers), count


def small_coordinate_control() -> dict[str, object]:
    """Exhaust all 2^9 families in binom([3],2) x binom([3],2)."""

    pairs = tuple(itertools.combinations(range(1, 4), 2))
    cells = tuple(itertools.product(pairs, repeat=2))
    infinity = 10**9
    brute_minimum = [infinity] * (len(cells) + 1)
    for mask in range(1 << len(cells)):
        area = mask.bit_count()
        shadow = {
            (left_vertex, right_vertex)
            for index, (left, right) in enumerate(cells)
            if mask & (1 << index)
            for left_vertex in left
            for right_vertex in right
        }
        brute_minimum[area] = min(brute_minimum[area], len(shadow))

    ordered = sorted(pairs, key=colex_key)
    one_dimensional = []
    for size in range(len(ordered) + 1):
        shadow = {
            vertex
            for pair in ordered[:size]
            for vertex in pair
        }
        one_dimensional.append(len(shadow))
    ferrers_minimum = [infinity] * (len(cells) + 1)
    for heights in itertools.product(range(len(pairs) + 1), repeat=len(pairs)):
        if any(heights[index] < heights[index + 1] for index in range(len(pairs) - 1)):
            continue
        area = sum(heights)
        cost = sum(
            (one_dimensional[row] - one_dimensional[row - 1])
            * one_dimensional[heights[row - 1]]
            for row in range(1, len(pairs) + 1)
        )
        ferrers_minimum[area] = min(ferrers_minimum[area], cost)

    assert brute_minimum == ferrers_minimum
    return {
        "n": 3,
        "uniformity": 2,
        "families_checked": 1 << len(cells),
        "minimum_simultaneous_shadow_by_area": brute_minimum,
    }


def build_certificate() -> dict[str, object]:
    ferrers = ferrers_capacities()
    caps, witnesses = recursive_section_caps(ferrers)
    degrees = {}
    for degree in range(2, 7):
        ambient = math.comb(N, degree) ** 2
        # A block J of s erased terms has complement size 49-s.  If the
        # complement section is at most C_d(49-s), its codimension in E_d is
        # c_d(s)=ambient-C_d(49-s).
        weights = [0] + [
            ambient - caps[degree][NUMBER_OF_TERMS - block]
            for block in range(1, NUMBER_OF_TERMS + 1)
        ]
        dp_value, dp_blocks = partition_dp(weights)
        exact_value, maximizers, partition_count = exhaustive_partition_optimum(
            weights
        )
        assert dp_value == exact_value
        assert dp_blocks in maximizers
        # For every fixed block size s, take all s-subsets.  Each coordinate
        # occurs in binom(48,s-1) blocks.  The linear projection form of
        # Shearer's inequality then gives
        #
        #   dim H >= (49/s) * c_d(s).
        #
        # Dimensions are integral, so we round the best rational bound up.
        shearer_rows = [
            (Fraction(NUMBER_OF_TERMS * weights[block], block), block)
            for block in range(1, NUMBER_OF_TERMS + 1)
        ]
        best_shearer, best_block = max(shearer_rows)
        shearer_dimension = math.ceil(best_shearer)
        degrees[str(degree)] = {
            "ambient_E_degree": ambient,
            "best_disjoint_partition_dimension": exact_value,
            "best_forced_sum_dimension": max(exact_value, shearer_dimension),
            "forced_excess_over_E": max(exact_value, shearer_dimension) - ambient,
            "maximizing_block_partitions": [list(row) for row in maximizers],
            "maximizer_block_weights": [weights[part] for part in dp_blocks],
            "integer_partitions_checked": partition_count,
            "selected_section_caps": {
                str(NUMBER_OF_TERMS - part): caps[degree][NUMBER_OF_TERMS - part]
                for part in sorted(set(dp_blocks))
            },
            "best_shearer_block_size": best_block,
            "best_shearer_block_codimension": weights[best_block],
            "best_shearer_rational_bound": {
                "numerator": best_shearer.numerator,
                "denominator": best_shearer.denominator,
            },
            "best_shearer_integral_dimension": shearer_dimension,
        }

    return {
        "schema_version": 1,
        "n": N,
        "hypothetical_terms": NUMBER_OF_TERMS,
        "method": (
            "exact recursive section caps plus the block erasure relation lemma; "
            "two Ferrers DPs and exhaustive integer-partition audit"
        ),
        "degree_results": degrees,
        "recursive_cap_spot_checks": {
            "C4_20": caps[4][20],
            "C4_25": caps[4][25],
            "C4_29": caps[4][29],
            "C5_39": caps[5][39],
            "C5_41": caps[5][41],
            "C5_42": caps[5][42],
            "C5_46": caps[5][46],
            "C6_46": caps[6][46],
            "C6_47": caps[6][47],
            "C6_48": caps[6][48],
            "C6_49": caps[6][49],
        },
        "full_section_cap_table": {
            str(degree): caps[degree] for degree in range(1, 7)
        },
        "small_coordinate_control": small_coordinate_control(),
        "claim": (
            "If 49 actual Chow terms sum to perm_7, their derivative-space "
            "sums H_d have dimensions at least 448, 1293, 1494, 853, and "
            "294 in degrees d=2,3,4,5,6 respectively."
        ),
        "claim_boundary": (
            "These lower bounds do not alone contradict the complementary "
            "catalectic relation inequalities and therefore do not prove "
            "ordinary Chow rank at least 50."
        ),
        "proof_formula": (
            "For X=direct_sum U_i, K=ker(X->H), W=E_d subset H, and a "
            "block J with complement S, dim(W intersect U_S) >= "
            "dim(W)-r_J+dim(proj_J K). Hence a section cap dim(W intersect "
            "U_S)<=dim(W)-c(J) gives dim(proj_J K)<=r_J-c(J). Summing over "
            "a partition of the 49 indices gives dim H>=sum_J c(J). More "
            "strongly, if a family of blocks covers each coordinate t times, "
            "the block row-echelon (linear Shearer) inequality gives "
            "t*dim(K)<=sum_J dim(proj_J K), hence "
            "dim(H)>=(sum_J c(J))/t."
        ),
        "witness_rows": {
            "C4_29": witnesses[4][29],
            "C4_20": witnesses[4][20],
            "C5_42": witnesses[5][42],
            "C5_41": witnesses[5][41],
            "C5_39": witnesses[5][39],
            "C6_48": witnesses[6][48],
            "C6_47": witnesses[6][47],
        },
    }


def validate(certificate: dict[str, object]) -> None:
    assert certificate["recursive_cap_spot_checks"] == {
        "C4_20": 341,
        "C4_25": 516,
        "C4_29": 656,
        "C5_39": 267,
        "C5_41": 302,
        "C5_42": 321,
        "C5_46": 405,
        "C6_46": 33,
        "C6_47": 37,
        "C6_48": 44,
        "C6_49": 49,
    }
    assert certificate["small_coordinate_control"] == {
        "n": 3,
        "uniformity": 2,
        "families_checked": 512,
        "minimum_simultaneous_shadow_by_area": [0, 4, 6, 6, 8, 8, 9, 9, 9, 9],
    }
    assert len(certificate["full_section_cap_table"]) == 6
    assert all(len(row) == 50 for row in certificate["full_section_cap_table"].values())
    degrees = certificate["degree_results"]
    expected = {
        "2": (448, 7, [[49]]),
        "3": (1293, 68, [[1, 48], [49]]),
        "4": (
            1494,
            269,
            [[20, 29], [21, 28], [22, 27], [23, 26], [24, 25]],
        ),
        "5": (853, 412, [[7, 8, 8, 8, 8, 10]]),
        "6": (294, 245, [[1] + [2] * 24]),
    }
    for degree, (dimension, excess, partitions) in expected.items():
        row = degrees[degree]
        assert row["best_forced_sum_dimension"] == dimension
        assert row["forced_excess_over_E"] == excess
        assert row["maximizing_block_partitions"] == partitions
        assert row["integer_partitions_checked"] == 173_525
    assert {
        degree: (
            row["best_shearer_block_size"],
            row["best_shearer_block_codimension"],
            row["best_shearer_rational_bound"],
        )
        for degree, row in degrees.items()
    } == {
        "2": (48, 438, {"numerator": 3577, "denominator": 8}),
        "3": (44, 1161, {"numerator": 56889, "denominator": 44}),
        "4": (29, 884, {"numerator": 43316, "denominator": 29}),
        "5": (10, 174, {"numerator": 4263, "denominator": 5}),
        "6": (2, 12, {"numerator": 294, "denominator": 1}),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    validate(certificate)
    if args.json is not None:
        args.json.write_text(
            json.dumps(certificate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.verify_json is None and args.json is None:
        print(json.dumps(certificate, indent=2, sort_keys=True))
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if certificate != frozen:
            raise SystemExit("lower-50 section-cap certificate JSON mismatch")
        print("SECTION_CAPS_AUDIT_PASS")


if __name__ == "__main__":
    main()
