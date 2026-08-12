#!/usr/bin/env python3
"""Exact QQ regression for the N6 near-extremal star quotient theorem."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTREMAL = ROOT / "scripts" / "n6_extremal_six_plane_audit.py"
STATE_DATA = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_extremal():
    spec = importlib.util.spec_from_file_location("n6_extremal_star_local", EXTREMAL)
    require(spec is not None and spec.loader is not None, EXTREMAL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rational_rref(matrix: list[list[int | Fraction]]) -> tuple[tuple[Fraction, ...], ...]:
    data = [[Fraction(value) for value in row] for row in matrix if any(row)]
    rows = len(data)
    columns = len(data[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if data[row][column]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        scale = data[rank][column]
        data[rank] = [value / scale for value in data[rank]]
        for row in range(rows):
            if row == rank or not data[row][column]:
                continue
            scale = data[row][column]
            data[row] = [
                left - scale * right
                for left, right in zip(data[row], data[rank])
            ]
        rank += 1
        if rank == rows:
            break
    return tuple(tuple(row) for row in data[:rank])


def standard_row_star_factors(extremal, sources: tuple[int, ...], parameter: int):
    factors = []
    for row in (0, 1):
        for column in (0, 1, 2):
            vector = {extremal.variable(row, column): 1}
            if column in sources:
                vector[extremal.variable(row, 3)] = parameter
            factors.append(vector)
    return factors


def product_row(extremal, left, right, quotient: bool) -> list[int]:
    width = (
        len(extremal.QUOTIENT_MONOMIALS)
        if quotient
        else len(extremal.SYMMETRIC_PAIRS)
    )
    answer = [0] * width
    for left_variable, left_coefficient in left.items():
        for right_variable, right_coefficient in right.items():
            monomial = extremal.SYMMETRIC_INDEX[
                tuple(sorted((left_variable, right_variable)))
            ]
            coefficient = left_coefficient * right_coefficient
            if quotient:
                for index, value in extremal.quotient_image(monomial).items():
                    answer[index] += coefficient * value
            else:
                answer[monomial] += coefficient
    return answer


def term_spaces(extremal, factors):
    full_rows = []
    quotient_rows = []
    for first, second in combinations(range(6), 2):
        full_rows.append(
            product_row(extremal, factors[first], factors[second], False)
        )
        quotient_rows.append(
            product_row(extremal, factors[first], factors[second], True)
        )
    return rational_rref(full_rows), rational_rref(quotient_rows)


def exact_qq_regression() -> dict[str, object]:
    extremal = load_extremal()
    cases = []
    source_sets = ((0, 1), (0, 2), (1, 2), (0, 1, 2))
    for sources in source_sets:
        for parameter in (-2, -1, 1, 2):
            full, quotient = term_spaces(
                extremal,
                standard_row_star_factors(extremal, sources, parameter),
            )
            require(len(full) == 15, (sources, parameter, len(full)))
            require(len(quotient) == 13, (sources, parameter, len(quotient)))
            cases.append((sources, parameter, full, quotient))

    quotient_signatures = {row[3] for row in cases}
    require(len(quotient_signatures) == 16, len(quotient_signatures))
    quotient_histogram: Counter[int] = Counter()
    full_histogram: Counter[int] = Counter()
    for left, right in combinations(cases, 2):
        quotient_sum_rank = len(rational_rref(list(left[3]) + list(right[3])))
        full_sum_rank = len(rational_rref(list(left[2]) + list(right[2])))
        quotient_histogram[26 - quotient_sum_rank] += 1
        full_histogram[30 - full_sum_rank] += 1

    require(quotient_histogram == {5: 78, 7: 42}, quotient_histogram)
    require(full_histogram == {4: 78, 6: 42}, full_histogram)
    return {
        "standard_support_case_count": len(cases),
        "source_subsets": [list(sources) for sources in source_sets],
        "nonzero_parameters": [-2, -1, 1, 2],
        "distinct_quotient_spaces": len(quotient_signatures),
        "full_quadratic_dimensions": sorted({len(row[2]) for row in cases}),
        "quotient_dimensions": sorted({len(row[3]) for row in cases}),
        "pairwise_quotient_intersection_histogram": {
            str(key): value for key, value in sorted(quotient_histogram.items())
        },
        "pairwise_full_intersection_histogram": {
            str(key): value for key, value in sorted(full_histogram.items())
        },
    }


def state_contingent_counts() -> list[dict[str, object]]:
    payload = json.loads(STATE_DATA.read_text(encoding="utf-8"))
    rows = []
    for layer in payload["layers"]:
        states = layer["states"]
        require(
            all(
                state["fixed_quadratic_quotient_t2"] <= 14
                and state["quadratic_relation_dimension_kappa2"] <= 2
                for state in states
            ),
            layer["middle_intersection_b"],
        )
        selected = [
            state
            for state in states
            if sum(
                pair == [0, 1] for pair in state["epsilon_alpha_pairs"]
            )
            >= 2
        ]
        histogram = Counter(
            state["fixed_quadratic_quotient_t2"] for state in selected
        )
        rows.append(
            {
                "b": layer["middle_intersection_b"],
                "all_canonical_scalar_states": len(states),
                "states_with_at_least_two_epsilon0_alpha1_entries": len(selected),
                "selected_t2_histogram": {
                    str(key): value for key, value in sorted(histogram.items())
                },
                "excluded_only_under_condition": (
                    "At least two of those epsilon-zero alpha-one terms belong "
                    "to the explicit N6-043 row/column star family."
                ),
            }
        )
    expected = [
        (61, 73, 37, {"13": 22, "14": 15}),
        (62, 11, 5, {"13": 5}),
        (63, 11, 5, {"13": 5}),
    ]
    actual = [
        (
            row["b"],
            row["all_canonical_scalar_states"],
            row["states_with_at_least_two_epsilon0_alpha1_entries"],
            row["selected_t2_histogram"],
        )
        for row in rows
    ]
    require(actual == expected, actual)
    return rows


def build_payload() -> dict[str, object]:
    return {
        "status": "N6_045_NEAR_EXTREMAL_STAR_QUOTIENT_RIGIDITY",
        "arithmetic": "exact rational elimination; no finite field or random input",
        "pure_theorem": (
            "Distinct thirteen-dimensional quotient spaces of explicit row- or "
            "column-star terms intersect in dimension at most eleven. Equality "
            "of quotient spaces determines the fifteen-dimensional Chow "
            "quadratic space."
        ),
        "coupling_consequence": (
            "A global quotient of dimension at most fourteen cannot contain two "
            "explicit star quotients while the six-term quadratic relation "
            "kernel has dimension at most two: their intersection would have "
            "dimension at least twelve, forcing equal fifteen-dimensional "
            "quadratic spaces and hence a relation kernel of dimension at least "
            "fifteen."
        ),
        "exact_qq_regression": exact_qq_regression(),
        "state_contingent_sublocus_counts": state_contingent_counts(),
        "strict_boundary": (
            "The counts do not exclude complete scalar states. They exclude only "
            "the subloci in which at least two epsilon-zero alpha-one terms lie "
            "in the explicit N6-043 star family. The general alpha-one component "
            "classification remains open."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print("N6_NEAR_EXTREMAL_STAR_QUOTIENT_RIGIDITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
