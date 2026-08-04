#!/usr/bin/env python3
"""Exact arithmetic audit of the realizability-aware ``n=6`` fixed-four frontier.

Assume hypothetically that ``perm_6`` has a 23-term Chow decomposition and
fix four terms with sum ``R``. The proof notes establish:

* the raw projection-shadow frontier has ``20<=b<=27`` and 36 states;
* common-quotient rigidity excludes every state with ``b=27``;
* the ``b=26`` layer has exactly 24 labelled defect patterns;
* a maximal 15-dimensional quadratic derivative space has a 20-dimensional
  cubic derivative space and contains no pure cube;
* directness or a one-relation coupling argument excludes every ``b=26``
  state; and
* the current frontier has ``20<=b<=25`` and 21 states.

This script checks the exact arithmetic, derivative profiles, and state
partitions. It does not replace the projection, Bukh-shadow, common-quotient,
or coupling arguments in the proof notes.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path

PERMANENT_KOSZUL_RANK = 14_175
PER_TERM_KOSZUL_CAP = 705
PER_TERM_CENTRAL_CAP = 20
PER_TERM_QUADRATIC_CAP = 15
PER_TERM_QUADRATIC_INTERSECTION_CAP = 3
FIXED_TERMS = 4
RESIDUAL_TERMS = 19
RESIDUAL_KOSZUL_CAP = RESIDUAL_TERMS * PER_TERM_KOSZUL_CAP
RESIDUAL_CENTRAL_CAP = RESIDUAL_TERMS * PER_TERM_CENTRAL_CAP
AMBIENT_VARIABLES = 36
BUKH_SEPARATOR = Fraction(427, 100)
SHADOW_SEPARATORS: dict[int, Fraction] = {
    20: Fraction(41, 10),
    21: Fraction(103, 25),
    22: Fraction(207, 50),
    23: Fraction(104, 25),
    24: Fraction(209, 50),
    25: Fraction(21, 5),
    26: Fraction(211, 50),
    27: Fraction(106, 25),
}

Exponent = tuple[int, ...]


def generalized_binomial(value: Fraction, order: int) -> Fraction:
    result = Fraction(1)
    for index in range(order):
        result *= value - index
    return result / factorial(order)


def compositions(total: int, variables: int) -> list[Exponent]:
    out: list[Exponent] = []

    def rec(prefix: tuple[int, ...], remaining: int) -> None:
        if len(prefix) == variables - 1:
            out.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            rec(prefix + (value,), remaining - value)

    rec((), total)
    return out


def exact_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("ragged matrix")

    data = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(data))
                if data[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        scale = data[pivot_row][column]
        data[pivot_row] = [value / scale for value in data[pivot_row]]
        for row in range(len(data)):
            if row == pivot_row:
                continue
            coefficient = data[row][column]
            if coefficient == 0:
                continue
            data[row] = [
                data[row][index]
                - coefficient * data[pivot_row][index]
                for index in range(columns)
            ]
        pivot_row += 1
        if pivot_row == len(data):
            break
    return pivot_row


def catalectic_matrix(
    polynomial: dict[Exponent, int],
    output_degree: int,
) -> tuple[list[list[int]], list[Exponent]]:
    variables = len(next(iter(polynomial)))
    operator_degree = 6 - output_degree
    rows = compositions(operator_degree, variables)
    columns = compositions(output_degree, variables)
    matrix: list[list[int]] = []

    for operator in rows:
        row: list[int] = []
        for output in columns:
            source = tuple(
                operator[index] + output[index]
                for index in range(variables)
            )
            coefficient = polynomial.get(source, 0)
            if coefficient:
                multiplier = 1
                for source_power, output_power in zip(
                    source,
                    output,
                    strict=True,
                ):
                    multiplier *= factorial(source_power) // factorial(
                        output_power
                    )
                coefficient *= multiplier
            row.append(coefficient)
        matrix.append(row)
    return matrix, columns


def five_variable_term(support_size: int) -> dict[Exponent, int]:
    """Return ``x0...x4 * (x0+...+x_{s-1})`` as an exponent map."""

    if not 1 <= support_size <= 5:
        raise ValueError(support_size)
    polynomial: dict[Exponent, int] = {}
    for extra in range(support_size):
        exponent = [1] * 5
        exponent[extra] += 1
        polynomial[tuple(exponent)] = 1
    return polynomial


def independent_six_variable_term() -> dict[Exponent, int]:
    return {(1, 1, 1, 1, 1, 1): 1}


def maximal_quadratic_term_profile() -> dict[str, object]:
    expected = {
        1: (11, 14),
        2: (11, 14),
        3: (13, 18),
        4: (14, 20),
        5: (15, 20),
    }
    table: dict[str, dict[str, object]] = {}

    for support_size in range(1, 6):
        polynomial = five_variable_term(support_size)
        quadratic_matrix, _ = catalectic_matrix(polynomial, 2)
        cubic_matrix, cubic_columns = catalectic_matrix(polynomial, 3)
        quadratic_rank = exact_rank(quadratic_matrix)
        cubic_rank = exact_rank(cubic_matrix)
        if (quadratic_rank, cubic_rank) != expected[support_size]:
            raise AssertionError(
                (support_size, quadratic_rank, cubic_rank)
            )

        pure_cube_columns_zero = all(
            all(row[column] == 0 for row in cubic_matrix)
            for column, exponent in enumerate(cubic_columns)
            if max(exponent) == 3
        )
        if not pure_cube_columns_zero:
            raise AssertionError((support_size, "pure cube column"))

        table[str(support_size)] = {
            "quadratic_dimension": quadratic_rank,
            "cubic_dimension": cubic_rank,
            "pure_cube_columns_zero": True,
        }

    independent = independent_six_variable_term()
    independent_quadratic, _ = catalectic_matrix(independent, 2)
    independent_cubic, independent_cubic_columns = catalectic_matrix(
        independent,
        3,
    )
    independent_profile = {
        "quadratic_dimension": exact_rank(independent_quadratic),
        "cubic_dimension": exact_rank(independent_cubic),
        "pure_cube_columns_zero": all(
            all(row[column] == 0 for row in independent_cubic)
            for column, exponent in enumerate(independent_cubic_columns)
            if max(exponent) == 3
        ),
    }
    if independent_profile != {
        "quadratic_dimension": 15,
        "cubic_dimension": 20,
        "pure_cube_columns_zero": True,
    }:
        raise AssertionError(independent_profile)

    return {
        "factor_span_five_support_table": table,
        "factor_span_six_independent": independent_profile,
        "conclusion": (
            "If a degree-six Chow term has quadratic derivative dimension "
            "15, then its cubic derivative dimension is 20 and that cubic "
            "space contains no nonzero pure cube."
        ),
    }


def bukh_separator_certificate() -> dict[str, object]:
    cubic_size = generalized_binomial(BUKH_SEPARATOR, 3) ** 2
    quadratic_shadow = generalized_binomial(BUKH_SEPARATOR, 2) ** 2

    if not cubic_size < 28:
        raise AssertionError(cubic_size)
    if not quadratic_shadow > 48:
        raise AssertionError(quadratic_shadow)

    return {
        "separator": str(BUKH_SEPARATOR),
        "binom_separator_3_squared": str(cubic_size),
        "binom_separator_3_squared_is_less_than_28": True,
        "binom_separator_2_squared": str(quadratic_shadow),
        "binom_separator_2_squared_is_greater_than_48": True,
        "conclusion": (
            "A subspace of D_3(perm_6) with first-derivative shadow at most "
            "48 has dimension at most 27."
        ),
    }


def exact_shadow_lower_table() -> dict[str, dict[str, object]]:
    table: dict[str, dict[str, object]] = {}
    for dimension, separator in SHADOW_SEPARATORS.items():
        cubic_size = generalized_binomial(separator, 3) ** 2
        quadratic_shadow = generalized_binomial(separator, 2) ** 2
        target_shadow = dimension + 20

        if not cubic_size < dimension:
            raise AssertionError((dimension, cubic_size))
        if not quadratic_shadow > target_shadow:
            raise AssertionError((dimension, quadratic_shadow))

        table[str(dimension)] = {
            "separator": str(separator),
            "binom_separator_3_squared": str(cubic_size),
            "binom_separator_2_squared": str(quadratic_shadow),
            "integer_shadow_lower_bound": dimension + 21,
            "per_omitted_factor_defect_budget": 27 - dimension,
        }
    return table


def build_b26_defect_patterns() -> list[dict[str, object]]:
    patterns: list[dict[str, object]] = []

    for index in range(FIXED_TERMS):
        for alpha_value in (0, 1):
            epsilon = [0] * FIXED_TERMS
            alpha = [0] * FIXED_TERMS
            epsilon[index] = 1
            alpha[index] = alpha_value
            patterns.append(
                {
                    "family": "one_quadratic_dimension_defect",
                    "epsilon": epsilon,
                    "alpha": alpha,
                }
            )

    for mask in range(1 << FIXED_TERMS):
        alpha = [
            (mask >> index) & 1
            for index in range(FIXED_TERMS)
        ]
        patterns.append(
            {
                "family": "maximal_quadratic_dimensions",
                "epsilon": [0] * FIXED_TERMS,
                "alpha": alpha,
            }
        )

    for pattern in patterns:
        epsilon = [int(value) for value in pattern["epsilon"]]
        alpha = [int(value) for value in pattern["alpha"]]
        for omitted in range(FIXED_TERMS):
            left = sum(
                epsilon[index]
                for index in range(FIXED_TERMS)
                if index != omitted
            ) + alpha[omitted]
            if left > 1:
                raise AssertionError((pattern, omitted, left))

    if len(patterns) != 24:
        raise AssertionError(len(patterns))
    family_histogram = Counter(str(pattern["family"]) for pattern in patterns)
    if dict(family_histogram) != {
        "one_quadratic_dimension_defect": 8,
        "maximal_quadratic_dimensions": 16,
    }:
        raise AssertionError(family_histogram)
    return patterns


def build_raw_states() -> list[dict[str, object]]:
    states: list[dict[str, object]] = []

    for intersection_dimension in range(20, 28):
        shadow_lower = intersection_dimension + 21
        defect_budget = 27 - intersection_dimension
        for quotient_dimension in range(
            0,
            intersection_dimension - 20 + 1,
        ):
            central_rank = intersection_dimension + quotient_dimension
            required_gain = max(
                0,
                RESIDUAL_KOSZUL_CAP
                + 1
                - (
                    PERMANENT_KOSZUL_RANK
                    - AMBIENT_VARIABLES * intersection_dimension
                ),
            )
            maximum_gain = AMBIENT_VARIABLES * quotient_dimension

            if required_gain == 0:
                route = "rank_budget_already_strict"
                prolongation_cap = None
            elif maximum_gain < required_gain:
                route = "structural_exclusion_or_stronger_invariant_required"
                prolongation_cap = None
            else:
                route = "relative_prolongation_cap_can_close"
                prolongation_cap = maximum_gain - required_gain
                if prolongation_cap not in {23, 59}:
                    raise AssertionError(prolongation_cap)

            states.append(
                {
                    "central_intersection_b": intersection_dimension,
                    "central_quotient_dimension_d": quotient_dimension,
                    "central_rank_h": central_rank,
                    "central_rank_upper_from_residual": (
                        2 * intersection_dimension - 20
                    ),
                    "quadratic_shadow_lower_bound": shadow_lower,
                    "per_omitted_factor_defect_budget": defect_budget,
                    "minimum_quotient_gain_for_strict_koszul_budget": required_gain,
                    "maximum_possible_quotient_gain": maximum_gain,
                    "relative_prolongation_cap_sufficient_for_closure": prolongation_cap,
                    "route": route,
                }
            )

    if len(states) != 36:
        raise AssertionError(len(states))
    return states


def histogram(states: list[dict[str, object]]) -> dict[str, int]:
    return dict(sorted(Counter(row["route"] for row in states).items()))


def prolongation_histogram(states: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(
        row["relative_prolongation_cap_sufficient_for_closure"]
        for row in states
        if row["relative_prolongation_cap_sufficient_for_closure"] is not None
    )
    return {str(key): value for key, value in sorted(counts.items())}


def state_frontier(states: list[dict[str, object]]) -> dict[str, object]:
    if not states:
        raise ValueError("empty state frontier")
    return {
        "central_intersection_range": [
            min(int(row["central_intersection_b"]) for row in states),
            max(int(row["central_intersection_b"]) for row in states),
        ],
        "state_count": len(states),
        "route_histogram": histogram(states),
        "relative_prolongation_cap_histogram": prolongation_histogram(states),
    }


def build_payload() -> dict[str, object]:
    projection_cap = (
        (FIXED_TERMS - 1) * PER_TERM_QUADRATIC_CAP
        + PER_TERM_QUADRATIC_INTERSECTION_CAP
    )
    if projection_cap != 48:
        raise AssertionError(projection_cap)

    shadow_table = exact_shadow_lower_table()
    derivative_profile = maximal_quadratic_term_profile()
    defect_patterns = build_b26_defect_patterns()
    raw_states = build_raw_states()
    excluded_b27 = [
        row for row in raw_states if row["central_intersection_b"] == 27
    ]
    after_b27 = [
        row for row in raw_states if row["central_intersection_b"] <= 26
    ]
    excluded_b26 = [
        row for row in after_b27 if row["central_intersection_b"] == 26
    ]
    states = [
        row for row in after_b27 if row["central_intersection_b"] <= 25
    ]

    expected_frontiers = (
        (
            raw_states,
            36,
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 12,
                "structural_exclusion_or_stronger_invariant_required": 21,
            },
            {"23": 6, "59": 6},
        ),
        (
            after_b27,
            28,
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 10,
                "structural_exclusion_or_stronger_invariant_required": 15,
            },
            {"23": 5, "59": 5},
        ),
        (
            states,
            21,
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 8,
                "structural_exclusion_or_stronger_invariant_required": 10,
            },
            {"23": 4, "59": 4},
        ),
    )
    for rows, count, routes, caps in expected_frontiers:
        if len(rows) != count:
            raise AssertionError((len(rows), count))
        if histogram(rows) != routes:
            raise AssertionError(histogram(rows))
        if prolongation_histogram(rows) != caps:
            raise AssertionError(prolongation_histogram(rows))

    if len(excluded_b27) != 8 or len(excluded_b26) != 7:
        raise AssertionError((len(excluded_b27), len(excluded_b26)))

    maximum_remaining_requirement = max(
        int(row["minimum_quotient_gain_for_strict_koszul_budget"])
        for row in states
    )
    if maximum_remaining_requirement != 121:
        raise AssertionError(maximum_remaining_requirement)

    defect_family_histogram = dict(
        sorted(Counter(str(row["family"]) for row in defect_patterns).items())
    )

    return {
        "status": "EXACT_INTEGER_FRONTIER_THROUGH_B26_EXCLUSION_REPLAYED",
        "hypothesis": "a 23-term Chow decomposition of perm_6",
        "fixed_terms": FIXED_TERMS,
        "residual_terms": RESIDUAL_TERMS,
        "residual_koszul_cap": RESIDUAL_KOSZUL_CAP,
        "residual_central_catalectic_cap": RESIDUAL_CENTRAL_CAP,
        "quadratic_intersection_projection_cap": projection_cap,
        "bukh_separator_certificate": bukh_separator_certificate(),
        "exact_shadow_lower_table": shadow_table,
        "maximal_quadratic_term_profile": derivative_profile,
        "raw_projection_frontier": state_frontier(raw_states),
        "common_quotient_b27_exclusion": {
            "excluded_central_intersection": 27,
            "excluded_state_count": len(excluded_b27),
            "individual_quadratic_dimensions": [15, 15, 15, 15],
            "individual_intersection_dimensions": [3, 3, 3, 3],
            "common_quotient_dimension": 12,
            "forced_quadratic_sum_dimension": 60,
            "forced_central_catalectic_rank": 80,
            "residual_inequality_upper_bound_on_central_rank": 34,
            "contradiction": "80>34",
        },
        "frontier_after_b27": state_frontier(after_b27),
        "b26_defect_patterns": {
            "pattern_count": len(defect_patterns),
            "family_histogram": defect_family_histogram,
            "patterns": defect_patterns,
        },
        "b26_coupling_exclusion": {
            "excluded_central_intersection": 26,
            "excluded_state_count": len(excluded_b26),
            "quadratic_shadow_dimension": 47,
            "residual_inequality_upper_bound_on_central_rank": 32,
            "family_a_pattern_count": 8,
            "family_a_quadratic_sum_is_direct": True,
            "family_a_central_rank_lower_bound": 60,
            "family_b_nonzero_alpha_pattern_count": 15,
            "family_b_nonzero_alpha_quadratic_sum_is_direct": True,
            "family_b_nonzero_alpha_central_rank": 80,
            "family_b_zero_alpha_pattern_count": 1,
            "family_b_zero_alpha_quadratic_relation_kernel_cap": 1,
            "one_relation_pure_cube_obstruction": True,
            "family_b_zero_alpha_central_rank": 80,
            "contradictions": ["60>32", "80>32"],
        },
        "central_intersection_range": [20, 25],
        "state_count": len(states),
        "route_histogram": histogram(states),
        "relative_prolongation_cap_histogram": prolongation_histogram(states),
        "maximum_remaining_gain_requirement": maximum_remaining_requirement,
        "states": states,
        "excluded_b27_states": excluded_b27,
        "excluded_b26_states": excluded_b26,
        "claim_boundary": (
            "The audit replays the 21-state frontier after the proved b=27 "
            "and b=26 exclusions. It does not exclude the 10 remaining "
            "structural states or establish the p<=23 and p<=59 caps."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_FIXED_FOUR_COUPLED_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
