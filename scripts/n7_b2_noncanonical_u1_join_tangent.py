#!/usr/bin/env python3
"""Exact noncanonical Chow-tangent test for the B2 rank-one join chart."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

from flint import fmpq, fmpq_mat
import sympy as sp


HERE = Path(__file__).resolve().parent
JOIN_PATH = HERE / "n7_b2_two_transposition_join_obstruction.py"
SPEC = importlib.util.spec_from_file_location(
    "n7_b2_two_transposition_join_obstruction", JOIN_PATH
)
join = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(join)

RANK_CERTIFICATE = HERE.parent / "data" / "n7_b2_gap_aligned_rank_one_chart.json"


def rational(value: object) -> fmpq:
    value = sp.Rational(value)
    return fmpq(int(value.p), int(value.q))


def multiply_forms(forms: list[tuple[sp.Rational, ...]]) -> dict[tuple[int, ...], sp.Rational]:
    return join.core.multiply_linear_forms(forms, tuple(range(len(forms))))


def tangent_columns(
    terms: list[list[tuple[sp.Rational, ...]]],
) -> list[dict[tuple[int, ...], sp.Rational]]:
    columns = []
    for term in terms:
        for omitted in range(7):
            other = [term[index] for index in range(7) if index != omitted]
            for variable in range(11):
                coordinate = tuple(sp.Integer(index == variable) for index in range(11))
                columns.append(multiply_forms([coordinate, *other]))
    return columns


def rank_one_polynomial(
    factor_index: int, w_direction: tuple[int, int, int, int]
) -> dict[tuple[int, ...], sp.Rational]:
    basis = [
        tuple(sp.Integer(row == column) for column in range(11))
        for row in range(11)
    ]
    factors = []
    for column in range(7):
        vector = list(basis[column])
        if column == factor_index:
            for row, coefficient in enumerate(w_direction):
                vector[7 + row] = coefficient
        factors.append(tuple(vector))
    return multiply_forms(factors)


def compressed_matrix(
    columns: list[dict[tuple[int, ...], sp.Rational]],
    extras: list[dict[tuple[int, ...], sp.Rational]],
) -> tuple[list[tuple[int, ...]], fmpq_mat]:
    keys = sorted(set().union(*(set(column) for column in columns + extras)))
    matrix = fmpq_mat(
        [
            [rational(column.get(key, 0)) for column in columns]
            for key in keys
        ]
    )
    return keys, matrix


def append_column(
    matrix: fmpq_mat,
    keys: list[tuple[int, ...]],
    polynomial: dict[tuple[int, ...], sp.Rational],
) -> fmpq_mat:
    return fmpq_mat(
        [
            [matrix[row, column] for column in range(matrix.ncols())]
            + [rational(polynomial.get(key, 0))]
            for row, key in enumerate(keys)
        ]
    )


def tangent_membership(
    factor_index: int, w_direction: tuple[int, int, int, int]
) -> dict[str, object]:
    # Both join types have the same first (0,1) slice, so one tangent matrix
    # controls the polynomial question for shared and disjoint joins.
    terms = join.pair_slice_terms((0, 1), (7, 8), sp.Rational(1, 2))
    columns = tangent_columns(terms)
    target = rank_one_polynomial(factor_index, w_direction)
    keys, matrix = compressed_matrix(columns, [target])
    augmented = append_column(matrix, keys, target)
    return {
        "factor_index": factor_index,
        "w_direction": list(w_direction),
        "compressed_monomial_rows": len(keys),
        "tangent_columns": len(columns),
        "tangent_rank": matrix.rank(),
        "augmented_rank": augmented.rank(),
        "full_degree_seven_tangent_membership": matrix.rank() == augmented.rank(),
    }


def one_solution_and_second_order() -> dict[str, object]:
    terms = join.pair_slice_terms((0, 1), (7, 8), sp.Rational(1, 2))
    columns = tangent_columns(terms)
    target = rank_one_polynomial(0, (1, 1, 1, 1))
    keys, matrix = compressed_matrix(columns, [target])
    augmented = fmpq_mat(
        [
            [matrix[row, column] for column in range(matrix.ncols())]
            + [-rational(target.get(key, 0))]
            for row, key in enumerate(keys)
        ]
    )
    reduced, rank = augmented.rref()
    solution = [fmpq(0)] * matrix.ncols()
    for row in range(rank):
        pivot = next(
            (column for column in range(matrix.ncols()) if reduced[row, column]),
            None,
        )
        if pivot is not None:
            solution[pivot] = reduced[row, matrix.ncols()]
    sparse_solution = []
    variations = [
        [[sp.Integer(0) for _ in range(11)] for _ in range(7)]
        for _ in range(2)
    ]
    for index, value in enumerate(solution):
        if not value:
            continue
        term = index // 77
        factor = (index % 77) // 11
        variable = index % 11
        variations[term][factor][variable] = sp.Rational(str(value))
        sparse_solution.append(
            {
                "term": term,
                "factor": factor,
                "variable": variable,
                "coefficient": str(value),
            }
        )

    second_order: dict[tuple[int, ...], sp.Rational] = {}
    for term in range(2):
        for first in range(7):
            for second in range(first + 1, 7):
                factors = [tuple(variations[term][first]), tuple(variations[term][second])]
                factors += [
                    terms[term][index]
                    for index in range(7)
                    if index not in (first, second)
                ]
                contribution = multiply_forms(factors)
                for exponent, coefficient in contribution.items():
                    second_order[exponent] = second_order.get(exponent, 0) + coefficient
    second_keys, second_matrix = compressed_matrix(columns, [second_order])
    second_augmented = append_column(second_matrix, second_keys, second_order)
    return {
        "representative": "factor_0_all_four_w",
        "first_order_sparse_solution": sparse_solution,
        "second_order_residual_support": sum(value != 0 for value in second_order.values()),
        "second_order_tangent_rank": second_matrix.rank(),
        "second_order_augmented_rank": second_augmented.rank(),
        "second_order_obstruction_vanishes": second_matrix.rank()
        == second_augmented.rank(),
    }


def load_rank_certificate() -> dict[str, object]:
    payload = json.loads(RANK_CERTIFICATE.read_text(encoding="utf-8"))
    if payload.get("status") != "GAP_ALIGNED_ONE_FACTOR_RANK_ONE_CHART_EMPTY":
        raise AssertionError("unexpected rank-certificate status")
    return payload


def build_payload() -> dict[str, object]:
    w_directions = {
        "single_u01": (1, 0, 0, 0),
        "reciprocal_pair_01": (1, 1, 0, 0),
        "reciprocal_pair_23": (0, 0, 1, 1),
        "all_four": (1, 1, 1, 1),
    }
    memberships = []
    for factor_index in (0, 1, 3):
        for name, direction in w_directions.items():
            row = tangent_membership(factor_index, direction)
            row["w_direction_name"] = name
            memberships.append(row)
    if any(
        row["full_degree_seven_tangent_membership"] != (row["factor_index"] in (0, 1))
        for row in memberships
    ):
        raise AssertionError("unexpected Chow-tangent membership pattern")
    second_order = one_solution_and_second_order()
    if not second_order["second_order_obstruction_vanishes"]:
        raise AssertionError("representative acquired an unexpected second-order obstruction")

    rank_certificate = load_rank_certificate()
    rank_rows = rank_certificate["rows"]
    tangent_and_operator_survivors = []
    for tangent_row in memberships:
        for rank_row in rank_rows:
            if (
                rank_row["factor_index"] == tangent_row["factor_index"]
                and rank_row["w_direction"] == tangent_row["w_direction"]
                and tangent_row["full_degree_seven_tangent_membership"]
                and rank_row["operator_gap_repaired"]
            ):
                tangent_and_operator_survivors.append(
                    {
                        "join_type": rank_row["join_type"],
                        "factor_index": tangent_row["factor_index"],
                        "w_direction": tangent_row["w_direction"],
                    }
                )
    if tangent_and_operator_survivors:
        raise AssertionError("the coupled tangent chart unexpectedly survived")
    return {
        "schema_version": 1,
        "status": "NONCANONICAL_U1_TANGENT_COUPLED_OBSTRUCTION",
        "tangent_memberships": memberships,
        "second_order_representative": second_order,
        "rank_certificate_source": "data/n7_b2_gap_aligned_rank_one_chart.json",
        "tangent_and_operator_survivors": tangent_and_operator_survivors,
        "candidate_cardinality_checked_before_materialization": {
            "factor_incidence_representatives": 3,
            "w_direction_representatives": 4,
            "exact_tangent_controls": len(memberships),
            "tangent_columns": 154,
            "compressed_rows": 328,
            "full_sym7_11_dimension_skipped": 19448,
            "full_sym7_49_dimension_skipped": 202927725,
        },
        "conservative_peak_memory_mib": 32,
        "decision": "NO_SURVIVOR_IN_MINIMAL_NONCANONICAL_TANGENT_PLUS_OPERATOR_CHART",
        "claim_boundary": [
            "For factors 0 and 1, the entire rank-one fifth-term polynomial lies in the exact Chow tangent span of the first transposition slice; all U-degrees are imposed simultaneously at first order.",
            "For untouched factor 3, the augmented tangent rank rises from 138 to 139, giving an exact first-order polynomial obstruction.",
            "One factor-0 all-four representative has a four-monomial second-order residual which still lies in the tangent span, so polynomial obstruction alone does not close that branch at second order.",
            "No tangent-solvable row also satisfies the previously frozen operator repair score; the coupled minimal chart is empty.",
            "Rank jumps under a broader finite noncanonical deformation and higher-order integration beyond the displayed representative remain open.",
            "No full Packet-B, lower-50, or border-rank conclusion is made.",
        ],
        "next_exact_gate": "Integrate the factor-0 all-four branch through the next nonzero order while imposing a determinantal rank-drop equation, rather than treating polynomial tangent membership and operator repair independently.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 B2 noncanonical U1 join tangent JSON mismatch")
        print("PASS n7 B2 noncanonical U1 join tangent")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
