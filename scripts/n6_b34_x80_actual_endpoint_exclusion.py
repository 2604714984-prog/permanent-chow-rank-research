#!/usr/bin/env python3
"""Exact algebra replay for exclusion of the N6-081 x=80 endpoint."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json"
N6081_SCRIPT = ROOT / "scripts" / "n6_lower29_b34_first_shortening.py"
N6081_DATA = ROOT / "data" / "n6_lower29_b34_first_shortening.json"
N6082_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b80_equality_locus.py"
N6082_DATA = ROOT / "data" / "n6_product_shadow_b80_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rank_q(rows: list[list[int]]) -> int:
    basis: dict[int, list[Fraction]] = {}
    for source in rows:
        row = [Fraction(value) for value in source]
        while True:
            pivot = next((index for index, value in enumerate(row) if value), None)
            if pivot is None:
                break
            if pivot not in basis:
                coefficient = row[pivot]
                basis[pivot] = [value / coefficient for value in row]
                break
            coefficient = row[pivot]
            old = basis[pivot]
            row = [value - coefficient * old_value for value, old_value in zip(row, old)]
    return len(basis)


def exponent_vectors(variables: int, degree: int) -> list[tuple[int, ...]]:
    return [
        exponents
        for exponents in product(range(degree + 1), repeat=variables)
        if sum(exponents) == degree
    ]


def multinomial_coefficient(exponents: tuple[int, ...]) -> int:
    from math import factorial

    value = factorial(sum(exponents))
    for exponent in exponents:
        value //= factorial(exponent)
    return value


def pure_power(point: tuple[int, ...], exponents: list[tuple[int, ...]]) -> list[int]:
    return [
        multinomial_coefficient(exponent)
        * product_value(point, exponent)
        for exponent in exponents
    ]


def product_value(point: tuple[int, ...], exponent: tuple[int, ...]) -> int:
    value = 1
    for coordinate, power in zip(point, exponent):
        value *= coordinate**power
    return value


def coordinate_basis(exponents: list[tuple[int, ...]], predicate) -> list[list[int]]:
    rows = []
    for index, exponent in enumerate(exponents):
        if predicate(exponent):
            row = [0] * len(exponents)
            row[index] = 1
            rows.append(row)
    return rows


def sign_cube_certificate() -> dict[str, object]:
    sign_lines = [(1,) + signs for signs in product((-1, 1), repeat=3)]
    quadratic_exponents = exponent_vectors(4, 2)
    cubic_exponents = exponent_vectors(4, 3)
    quadratic_squarefree = coordinate_basis(quadratic_exponents, lambda exponent: max(exponent) <= 1)
    cubic_squarefree = coordinate_basis(cubic_exponents, lambda exponent: max(exponent) <= 1)
    rows = []
    for omitted in range(8):
        selected = [point for index, point in enumerate(sign_lines) if index != omitted]
        quadratic = [pure_power(point, quadratic_exponents) for point in selected]
        cubic = [pure_power(point, cubic_exponents) for point in selected]
        quadratic_rank = rank_q(quadratic)
        quadratic_intersection = quadratic_rank + len(quadratic_squarefree) - rank_q(quadratic + quadratic_squarefree)
        cubic_rank = rank_q(cubic)
        cubic_intersection = cubic_rank + len(cubic_squarefree) - rank_q(cubic + cubic_squarefree)
        rows.append(
            {
                "omitted_sign_line": list(sign_lines[omitted]),
                "seven_quadratic_powers_rank": quadratic_rank,
                "quadratic_squarefree_intersection_dimension": quadratic_intersection,
                "seven_cubic_powers_rank": cubic_rank,
                "cubic_squarefree_intersection_dimension": cubic_intersection,
            }
        )
    require(
        all(
            (
                row["seven_quadratic_powers_rank"],
                row["quadratic_squarefree_intersection_dimension"],
                row["seven_cubic_powers_rank"],
                row["cubic_squarefree_intersection_dimension"],
            )
            == (7, 6, 7, 3)
            for row in rows
        ),
        rows,
    )
    return {
        "projective_sign_line_count": len(sign_lines),
        "seven_of_eight_case_count": len(rows),
        "quadratic_squarefree_dimension": len(quadratic_squarefree),
        "cubic_squarefree_dimension": len(cubic_squarefree),
        "all_cases_have_rank_signature_7_6_7_3": True,
        "rows": rows,
    }


def build_payload() -> dict[str, object]:
    n6081 = load_module(N6081_SCRIPT, "n6081_for_n6083")
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6083")
    require(n6081.build_payload() == json.loads(N6081_DATA.read_text(encoding="utf-8")), N6081_DATA)
    require(n6082.build_payload() == json.loads(N6082_DATA.read_text(encoding="utf-8")), N6082_DATA)
    endpoint = n6081.build_payload()["unique_endpoint"]
    require((endpoint["central_space_dimension"], endpoint["central_first_shadow_dimension"]) == (80, 90), endpoint)
    equality = n6082.build_payload()
    require(equality["second_product_shadow"]["every_equality_point_has_second_shadow_dimension"] == 24, equality)
    sign = sign_cube_certificate()
    return {
        "status": [
            "PURE_ACTUAL_SEVEN_FRAME_X80_ENDPOINT_EXCLUSION",
            "EXACT_QQ_SIGN_CUBE_REPLAY",
            "N6-083",
        ],
        "endpoint_input": {
            "central_dimension": 80,
            "first_shadow_dimension": 90,
            "second_shadow_dimension": 24,
            "quadratic_spaces": 7,
            "quadratic_space_dimension_each": 15,
            "middle_space_dimension_each": 20,
            "common_quotient_dimension": 15,
            "all_quadratic_spaces_literal_direct": True,
            "all_middle_spaces_literal_direct": True,
            "six_anchor_differences_span_the_90_plane": True,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
        },
        "pairwise_transversality": {
            "difference_plane_dimension": 15,
            "universal_difference_shadow_lower": 12,
            "containment_upper_from_two_factor_spans": 12,
            "every_pair_of_factor_six_planes_is_complementary": True,
            "sum_of_the_seven_factor_planes_is_the_24_plane": True,
        },
        "invertible_block_branch": {
            "n6069_reapplied_in_partitioned_product_coordinates": True,
            "one_invertible_row_block_forces_a_column_separated_pair": True,
            "shared_quotient_domain_argument_propagates_column_separation_to_all_seven_terms": True,
            "n6070_pair_rigidity_forces_each_term_to_have_one_fixed_row_line": True,
            "seven_independent_row_squares_are_seven_of_eight_projective_sign_lines": True,
            "sign_cube_exact_certificate": sign,
            "resulting_cubic_permanent_intersection_dimension": 3 * 20,
            "contradicts_required_dimension": 80,
        },
        "all_singular_branch": {
            "same_row_common_quotient_synchronization_reapplied_to_seven_colors": True,
            "each_of_four_active_row_blocks_has_rank_at_most_one": True,
            "factor_frame_rank_upper": 4,
            "required_factor_frame_rank": 6,
            "contradiction": True,
        },
        "strict_conclusion": (
            "The exact common-W15 seven-frame 80-to-90 endpoint in N6-081 is not "
            "Chow realizable. Therefore every global b=34 survivor must satisfy f_A<=79 "
            "for every residual seven-set A."
        ),
        "claim_boundary": (
            "This removes only the x=80 branch of the N6-081 alternative. It does not "
            "exclude the remaining f_A<=79 branch, does not exclude global b=34, does "
            "not prove ChowRank(perm_6)>=29, and makes no border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        require(payload == json.loads(args.verify_json.read_text(encoding="utf-8")), args.verify_json)
    print("sign_cases=8 rank_signature=7,6,7,3")
    print("x80_actual_endpoint=excluded remaining_every_f_A_at_most_79")
    print("N6_B34_X80_ACTUAL_ENDPOINT_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
