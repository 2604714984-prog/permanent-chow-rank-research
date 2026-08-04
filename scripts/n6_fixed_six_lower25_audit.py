#!/usr/bin/env python3
"""Exact arithmetic audit for the fixed-six lower-25 route for ``perm_6``.

Assume hypothetically that ``perm_6`` has a 24-term Chow decomposition and
fix six terms. The accompanying proof note supplies the algebraic inputs:

* the quadratic projection cap is 78;
* Bukh's two-dimensional shadow theorem constrains the central intersection;
* a vector-valued quadratic relation space of dimension ``k<=16`` has first
  prolongation at most the degree-two Macaulay successor ``k^{<2>}``;
* the block-Sylvester inequality converts the cubic-relation cap into a
  coupled middle-catalectic rank lower bound.

This script uses only exact integer/rational arithmetic. It validates rational
shadow separators and exhaustively checks the symmetric epsilon-defect types.
It deliberately assigns central rank zero to individual terms with quadratic
derivative dimension at most ten.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path

FIXED_TERMS = 6
RESIDUAL_TERMS = 18
PERMANENT_CENTRAL_RANK = 400
PERMANENT_KOSZUL_RANK = 14_175
PER_TERM_CENTRAL_CAP = 20
PER_TERM_KOSZUL_CAP = 705
RESIDUAL_CENTRAL_CAP = RESIDUAL_TERMS * PER_TERM_CENTRAL_CAP
RESIDUAL_KOSZUL_CAP = RESIDUAL_TERMS * PER_TERM_KOSZUL_CAP
AMBIENT_VARIABLES = 36
PER_TERM_QUADRATIC_CAP = 15
PER_TERM_QUADRATIC_INTERSECTION_CAP = 3
PROJECTION_CAP = (
    (FIXED_TERMS - 1) * PER_TERM_QUADRATIC_CAP
    + PER_TERM_QUADRATIC_INTERSECTION_CAP
)

SHADOW_CERTIFICATES: dict[int, tuple[int, Fraction]] = {
    40: (60, Fraction(4459, 1000)),
    41: (61, Fraction(4473, 1000)),
    42: (62, Fraction(2243, 500)),
    43: (62, Fraction(4499, 1000)),
    44: (63, Fraction(4511, 1000)),
    45: (64, Fraction(1131, 250)),
    46: (65, Fraction(567, 125)),
    47: (66, Fraction(1137, 250)),
    48: (66, Fraction(114, 25)),
    49: (67, Fraction(4571, 1000)),
    50: (68, Fraction(4583, 1000)),
    51: (69, Fraction(2297, 500)),
    52: (69, Fraction(921, 200)),
    53: (70, Fraction(577, 125)),
    54: (71, Fraction(4627, 1000)),
    55: (72, Fraction(4637, 1000)),
    56: (72, Fraction(581, 125)),
    57: (73, Fraction(2329, 500)),
    58: (74, Fraction(1167, 250)),
    59: (75, Fraction(2339, 500)),
    60: (75, Fraction(586, 125)),
    61: (76, Fraction(4697, 1000)),
    62: (77, Fraction(4707, 1000)),
    63: (77, Fraction(1179, 250)),
    64: (78, Fraction(189, 40)),
}
B65_CAP_SEPARATOR = Fraction(947, 200)

Exponent = tuple[int, ...]


def compositions(total: int, variables: int) -> list[Exponent]:
    rows: list[Exponent] = []

    def rec(prefix: tuple[int, ...], remaining: int) -> None:
        if len(prefix) == variables - 1:
            rows.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            rec(prefix + (value,), remaining - value)

    rec((), total)
    return rows


def exact_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    columns = len(matrix[0])
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
) -> list[list[int]]:
    variables = len(next(iter(polynomial)))
    operator_degree = 6 - output_degree
    operators = compositions(operator_degree, variables)
    outputs = compositions(output_degree, variables)
    matrix: list[list[int]] = []

    for operator in operators:
        row: list[int] = []
        for output in outputs:
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
    return matrix


def reconstruct_term_profiles() -> dict[str, object]:
    expected = {
        1: (11, 14),
        2: (11, 14),
        3: (13, 18),
        4: (14, 20),
        5: (15, 20),
    }
    table: dict[str, list[int]] = {}
    for support_size in range(1, 6):
        polynomial: dict[Exponent, int] = {}
        for extra in range(support_size):
            exponent = [1] * 5
            exponent[extra] += 1
            polynomial[tuple(exponent)] = 1
        quadratic_rank = exact_rank(catalectic_matrix(polynomial, 2))
        central_rank = exact_rank(catalectic_matrix(polynomial, 3))
        observed = (quadratic_rank, central_rank)
        if observed != expected[support_size]:
            raise AssertionError((support_size, observed))
        table[str(support_size)] = [quadratic_rank, central_rank]

    independent = {(1, 1, 1, 1, 1, 1): 1}
    independent_profile = [
        exact_rank(catalectic_matrix(independent, 2)),
        exact_rank(catalectic_matrix(independent, 3)),
    ]
    if independent_profile != [15, 20]:
        raise AssertionError(independent_profile)

    return {
        "factor_span_five_support_table": table,
        "factor_span_six_independent": independent_profile,
        "factor_span_at_most_four_quadratic_cap": 10,
        "quadratic_dimension_twelve_impossible": True,
    }


CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION: dict[int, int | None] = {
    15: 20,
    14: 20,
    13: 18,
    12: None,
    11: 14,
    10: 0,
    9: 0,
    8: 0,
    7: 0,
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0,
}


def generalized_binomial(value: Fraction, order: int) -> Fraction:
    result = Fraction(1)
    for index in range(order):
        result *= value - index
    return result / factorial(order)


def macaulay_successor_degree_two(value: int) -> int:
    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    if not 0 <= remainder < largest:
        raise AssertionError((value, largest, remainder))
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def module_partition_cap(total: int, colors: int = FIXED_TERMS) -> int:
    if total < 0 or colors <= 0:
        raise ValueError((total, colors))
    best = 0

    def rec(remaining: int, slots: int, lower: int, subtotal: int) -> None:
        nonlocal best
        if slots == 1:
            if remaining < lower:
                return
            best = max(best, subtotal + macaulay_successor_degree_two(remaining))
            return
        for value in range(lower, remaining + 1):
            rec(
                remaining - value,
                slots - 1,
                value,
                subtotal + macaulay_successor_degree_two(value),
            )

    rec(total, colors, 0, 0)
    return best


def validate_shadow_certificates() -> dict[str, object]:
    if PROJECTION_CAP != 78:
        raise AssertionError(PROJECTION_CAP)
    table: dict[str, object] = {}
    for b, (shadow_lower, separator) in SHADOW_CERTIFICATES.items():
        cubic_size = generalized_binomial(separator, 3) ** 2
        quadratic_shadow = generalized_binomial(separator, 2) ** 2
        if not cubic_size < b:
            raise AssertionError((b, separator, cubic_size))
        if not quadratic_shadow > shadow_lower - 1:
            raise AssertionError((b, separator, quadratic_shadow, shadow_lower))
        table[str(b)] = {
            "separator": str(separator),
            "binom_separator_3_squared": str(cubic_size),
            "binom_separator_2_squared": str(quadratic_shadow),
            "integer_shadow_lower_bound": shadow_lower,
        }

    cubic_65 = generalized_binomial(B65_CAP_SEPARATOR, 3) ** 2
    shadow_65 = generalized_binomial(B65_CAP_SEPARATOR, 2) ** 2
    if not cubic_65 < 65:
        raise AssertionError(cubic_65)
    if not shadow_65 > PROJECTION_CAP:
        raise AssertionError(shadow_65)

    return {
        "projection_cap": PROJECTION_CAP,
        "b65_separator": str(B65_CAP_SEPARATOR),
        "b65_binom_separator_3_squared": str(cubic_65),
        "b65_binom_separator_2_squared": str(shadow_65),
        "b65_forces_shadow_at_least_79": True,
        "per_b_certificates": table,
    }


def nondecreasing_epsilon_types(defect_budget: int) -> list[tuple[int, ...]]:
    rows: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], lower: int) -> None:
        if len(prefix) == FIXED_TERMS:
            if sum(prefix) - min(prefix) <= defect_budget:
                rows.append(prefix)
            return
        for value in range(lower, PER_TERM_QUADRATIC_CAP + 1):
            candidate = prefix + (value,)
            if len(candidate) >= 2:
                lower_bound = sum(candidate) - min(candidate)
                if lower_bound > defect_budget:
                    break
            rec(candidate, value)

    rec((), 0)
    return rows


def labelled_multiplicity(values: tuple[int, ...]) -> int:
    counts = Counter(values)
    result = factorial(len(values))
    for count in counts.values():
        result //= factorial(count)
    return result


def evaluate_epsilon_type(
    epsilon: tuple[int, ...],
    defect_budget: int,
) -> dict[str, object] | None:
    quadratic_dimensions = [
        PER_TERM_QUADRATIC_CAP - value for value in epsilon
    ]
    if any(dimension < 0 for dimension in quadratic_dimensions):
        return None
    central_lowers: list[int] = []
    for dimension in quadratic_dimensions:
        lower = CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION[dimension]
        if lower is None:
            return None
        central_lowers.append(lower)

    relation_cap = defect_budget - sum(epsilon) + min(epsilon)
    if relation_cap < 0:
        raise AssertionError((epsilon, defect_budget, relation_cap))
    cubic_relation_cap = macaulay_successor_degree_two(relation_cap)
    coupled_rank_lower = sum(central_lowers) - 2 * cubic_relation_cap

    return {
        "epsilon": list(epsilon),
        "quadratic_dimensions": quadratic_dimensions,
        "individual_central_rank_lowers": central_lowers,
        "quadratic_relation_kernel_cap": relation_cap,
        "cubic_relation_kernel_cap": cubic_relation_cap,
        "coupled_central_rank_lower": coupled_rank_lower,
        "labelled_multiplicity": labelled_multiplicity(epsilon),
    }


def layer_payload(b: int) -> dict[str, object]:
    shadow_lower, separator = SHADOW_CERTIFICATES[b]
    defect_budget = PROJECTION_CAP - shadow_lower
    if not 0 <= defect_budget <= 16:
        raise AssertionError((b, defect_budget))

    types = nondecreasing_epsilon_types(defect_budget)
    feasible: list[dict[str, object]] = []
    impossible_labelled_count = 0
    all_labelled_count = 0

    for epsilon in types:
        multiplicity = labelled_multiplicity(epsilon)
        all_labelled_count += multiplicity
        row = evaluate_epsilon_type(epsilon, defect_budget)
        if row is None:
            impossible_labelled_count += multiplicity
        else:
            feasible.append(row)

    if not feasible:
        raise AssertionError(b)

    minimum = min(int(row["coupled_central_rank_lower"]) for row in feasible)
    minimizers = [
        row
        for row in feasible
        if int(row["coupled_central_rank_lower"]) == minimum
    ]
    residual_upper = 2 * b - 40
    if minimum <= residual_upper:
        raise AssertionError((b, minimum, residual_upper, minimizers))

    return {
        "b": b,
        "shadow_separator": str(separator),
        "quadratic_shadow_lower_bound": shadow_lower,
        "defect_budget": defect_budget,
        "symmetric_epsilon_type_count": len(types),
        "all_labelled_epsilon_count": all_labelled_count,
        "impossible_dimension_twelve_labelled_count": impossible_labelled_count,
        "profile_feasible_symmetric_type_count": len(feasible),
        "maximum_quadratic_relation_kernel_cap": max(
            int(row["quadratic_relation_kernel_cap"]) for row in feasible
        ),
        "maximum_cubic_relation_kernel_cap": max(
            int(row["cubic_relation_kernel_cap"]) for row in feasible
        ),
        "minimum_coupled_central_rank_lower_bound": minimum,
        "residual_central_rank_upper_bound": residual_upper,
        "strict_margin": minimum - residual_upper,
        "minimizers": minimizers,
    }


def automatic_layers() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for b in (40, 41):
        lower = PERMANENT_KOSZUL_RANK - AMBIENT_VARIABLES * b
        if lower <= RESIDUAL_KOSZUL_CAP:
            raise AssertionError((b, lower, RESIDUAL_KOSZUL_CAP))
        rows.append(
            {
                "b": b,
                "residual_koszul_rank_lower_bound": lower,
                "eighteen_term_koszul_cap": RESIDUAL_KOSZUL_CAP,
                "strict_margin": lower - RESIDUAL_KOSZUL_CAP,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    shadow = validate_shadow_certificates()
    term_profiles = reconstruct_term_profiles()
    module_caps = {str(value): module_partition_cap(value) for value in range(17)}
    scalar_caps = {
        str(value): macaulay_successor_degree_two(value)
        for value in range(17)
    }
    if module_caps != scalar_caps:
        raise AssertionError((module_caps, scalar_caps))

    layers = [layer_payload(b) for b in range(42, 65)]
    expected_minima = {
        42: 48,
        43: 48,
        44: 50,
        45: 60,
        46: 68,
        47: 74,
        48: 74,
        49: 78,
        50: 80,
        51: 88,
        52: 88,
        53: 92,
        54: 96,
        55: 98,
        56: 98,
        57: 100,
        58: 110,
        59: 112,
        60: 112,
        61: 116,
        62: 118,
        63: 118,
        64: 120,
    }
    for layer in layers:
        b = int(layer["b"])
        observed = int(layer["minimum_coupled_central_rank_lower_bound"])
        if observed != expected_minima[b]:
            raise AssertionError((b, observed, expected_minima[b]))

    return {
        "status": "EXACT_N6_FIXED_SIX_24_TERM_EXCLUSION_REPLAYED",
        "hypothetical_total_terms": 24,
        "fixed_terms": FIXED_TERMS,
        "residual_terms": RESIDUAL_TERMS,
        "projection_cap": PROJECTION_CAP,
        "central_intersection_range_after_shadow_and_catalectic": [40, 64],
        "shadow_certificates": shadow,
        "reconstructed_term_profiles": term_profiles,
        "macaulay_degree_two_successors": scalar_caps,
        "vector_valued_module_partition_caps": module_caps,
        "module_partition_identity_verified_through": 16,
        "conservative_profile_policy": (
            "Quadratic dimension 12 is rejected as impossible. "
            "Quadratic dimensions at most 10 receive central-rank lower "
            "bound zero."
        ),
        "automatic_low_layers": automatic_layers(),
        "component_relation_layers": layers,
        "conclusion": (
            "Every fixed-six state under a hypothetical 24-term "
            "decomposition is contradictory. Therefore "
            "ChowRank(perm_6)>=25 over characteristic zero."
        ),
        "certified_interval_if_algebraic_lemmas_are_accepted": [25, 32],
        "claim_boundary": (
            "This exact arithmetic payload does not by itself prove the "
            "vector-valued Macaulay degeneration lemma, the Bukh shadow "
            "theorem, the block-Sylvester inequality, or the individual "
            "term profiles. It does not prove lower 26, border lower 25, "
            "or exact rank 32."
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
    print("N6_FIXED_SIX_LOWER25_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
