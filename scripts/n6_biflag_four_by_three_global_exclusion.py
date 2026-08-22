#!/usr/bin/env python3
"""Exact 4 x 3 biflag charts and the global product reduction (N6-107)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_biflag_four_by_three_global_exclusion.json"
BASE_SCRIPT = ROOT / "scripts" / "n6_biflag_three_by_four_chart.py"
SPEC = importlib.util.spec_from_file_location("n6106_base", BASE_SCRIPT)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BASE)


def orbit_data() -> tuple[tuple[str, set[tuple[int, int]], set[tuple[int, int]], str], ...]:
    return (
        (
            "4x3_two_core_columns",
            {(row, column) for row in (0, 1, 2, 3) for column in (0, 1, 3)},
            {(4, 2)},
            "column",
        ),
        (
            "4x3_one_core_column",
            {(row, column) for row in (0, 1, 2, 3) for column in (0, 3, 4)},
            {(4, 1), (4, 2)},
            "column",
        ),
        (
            "4x3_tail_row",
            {(row, column) for row in (0, 1, 2, 4) for column in (0, 1, 2)},
            {(3, 3), (3, 4)},
            "row",
        ),
    )


def expected_normal_form_vectors(
    support_cells: set[tuple[int, int]],
    exception_targets: set[tuple[int, int]],
    mode: str,
    variables: tuple[tuple[int, int], ...],
) -> tuple[list[tuple[int, ...]], int, int]:
    cells = BASE.canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    variable_index = {variable: position for position, variable in enumerate(variables)}
    selected_rows = sorted({row for row, _ in support_cells})
    selected_columns = sorted({column for _, column in support_cells})
    answer = []

    if mode == "column":
        missing_columns = [column for column in range(5) if column not in selected_columns]
        for source_column in selected_columns:
            for target_column in missing_columns:
                vector = [0] * len(variables)
                for row in selected_rows:
                    vector[
                        variable_index[index[row, source_column], index[row, target_column]]
                    ] = 1
                answer.append(tuple(vector))
    elif mode == "row":
        missing_row = next(row for row in range(5) if row not in selected_rows)
        for source_row in selected_rows:
            vector = [0] * len(variables)
            for column in selected_columns:
                vector[
                    variable_index[index[source_row, column], index[missing_row, column]]
                ] = 1
            answer.append(tuple(vector))
    else:
        raise AssertionError(mode)
    factor_count = len(answer)

    for source in sorted(support_cells):
        for target in sorted(exception_targets):
            vector = [0] * len(variables)
            vector[variable_index[index[source], index[target]]] = 1
            answer.append(tuple(vector))
    return answer, factor_count, len(answer) - factor_count


def linear_reduction_certificate(
    name: str,
    support_cells: set[tuple[int, int]],
    exception_targets: set[tuple[int, int]],
    mode: str,
) -> dict[str, object]:
    cells = BASE.canonical_biflag_cells()
    variables, quadrics, columns = BASE.graph_linear_expansion(support_cells)
    all_keys = set().union(*(set(column) for column in columns))
    quadratic_keys = {
        key
        for column in columns
        for key, polynomial in column.items()
        if any(len(monomial) == 2 for monomial in polynomial)
    }
    linear_keys = all_keys - quadratic_keys
    exception_variables = {
        variable
        for variable, (_, target) in enumerate(variables)
        if cells[target] in exception_targets
    }
    exception_touched_keys = {
        key
        for key in linear_keys
        if any(
            column.get(key, {}).get((variable,), 0)
            for column in columns
            for variable in exception_variables
        )
    }
    effective_keys = linear_keys - exception_touched_keys

    coefficient_rows = []
    for column in columns:
        for key in sorted(effective_keys):
            row = tuple(
                column.get(key, {}).get((variable,), 0)
                for variable in range(len(variables))
            )
            if any(row):
                coefficient_rows.append(row)
    linear_rank = BASE.rational_rank(coefficient_rows)

    expected, factor_count, exception_count = expected_normal_form_vectors(
        support_cells, exception_targets, mode, variables
    )
    assert BASE.rational_rank(expected) == len(expected)
    assert all(
        sum(row[index] * vector[index] for index in range(len(variables))) == 0
        for row in coefficient_rows
        for vector in expected
    )
    assert linear_rank == len(variables) - len(expected)

    weight_groups: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = defaultdict(list)
    for variable, (source, target) in enumerate(variables):
        weight_groups[BASE.tangent_weight(cells[source], cells[target])].append(variable)
    signatures = []
    for members in weight_groups.values():
        rows = []
        for column in columns:
            nonzero_rows = []
            for key in effective_keys:
                row = tuple(
                    column.get(key, {}).get((variable,), 0) for variable in members
                )
                if any(row):
                    nonzero_rows.append(row)
            assert len(nonzero_rows) <= 1
            if nonzero_rows:
                rows.append(nonzero_rows[0])
        if rows:
            minimum, kernel_dimension = BASE.minimum_nonzero_support(rows)
        else:
            minimum, kernel_dimension = 0, len(members)
        signatures.append((len(members), len(rows), kernel_dimension, minimum))
    minimum_rank = min(signature[3] for signature in signatures if signature[3])
    assert sum(signature[2] for signature in signatures) == len(expected)
    assert minimum_rank == 6

    return {
        "name": name,
        "mode": mode,
        "graph_variable_count": len(variables),
        "base_rectangle_dimension": len(quadrics),
        "linear_only_weight_count": len(linear_keys),
        "discarded_exception_touched_weight_count": len(exception_touched_keys),
        "effective_linear_weight_count": len(effective_keys),
        "linear_equation_rank_over_Q": linear_rank,
        "kernel_dimension": len(variables) - linear_rank,
        "factor_parameter_count": factor_count,
        "exception_parameter_count": exception_count,
        "minimum_rank_outside_kernel": minimum_rank,
        "weight_group_signature_histogram": [
            {
                "variable_count": signature[0],
                "independent_output_weight_count": signature[1],
                "kernel_dimension": signature[2],
                "minimum_rank_outside_kernel": signature[3],
                "group_count": count,
            }
            for signature, count in sorted(Counter(signatures).items())
        ],
    }


def exception_certificate(
    name: str,
    support_cells: set[tuple[int, int]],
    exception_targets: set[tuple[int, int]],
    mode: str,
) -> dict[str, object]:
    cells = BASE.canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    support = frozenset(index[cell] for cell in support_cells)
    selected_rows = sorted({row for row, _ in support_cells})
    selected_columns = sorted({column for _, column in support_cells})
    quadrics = tuple(
        quadric
        for quadric in BASE.rectangle_quadrics(cells)
        if frozenset(quadric[0] + quadric[1]) <= support
    )

    next_variable = 0
    if mode == "column":
        missing_columns = [column for column in range(5) if column not in selected_columns]
        factor_variables = {
            (source_column, target_column): position
            for position, (source_column, target_column) in enumerate(
                (source_column, target_column)
                for source_column in selected_columns
                for target_column in missing_columns
            )
        }
        next_variable = len(factor_variables)
    else:
        missing_row = next(row for row in range(5) if row not in selected_rows)
        factor_variables = {
            source_row: position for position, source_row in enumerate(selected_rows)
        }
        next_variable = len(factor_variables)

    exception_variables = {}
    for source in sorted(support_cells):
        for target in sorted(exception_targets):
            exception_variables[source, target] = next_variable
            next_variable += 1
    exception_indices = set(exception_variables.values())

    vectors: dict[int, dict[int, BASE.Polynomial]] = {}
    for source in sorted(support_cells):
        row, column = source
        vector: dict[int, BASE.Polynomial] = {index[source]: {(): 1}}
        if mode == "column":
            for target_column in missing_columns:
                vector[index[row, target_column]] = {
                    (factor_variables[column, target_column],): 1
                }
        else:
            vector[index[missing_row, column]] = {(factor_variables[row],): 1}
        for target in sorted(exception_targets):
            vector[index[target]] = {(exception_variables[source, target],): 1}
        vectors[index[source]] = vector

    columns = []
    for quadric in quadrics:
        column: dict[tuple[int, int], BASE.Polynomial] = {}
        for first, second in quadric:
            for first_cell, first_polynomial in vectors[first].items():
                for second_cell, second_polynomial in vectors[second].items():
                    BASE.add_vector_product(
                        column,
                        first_cell,
                        first_polynomial,
                        second_cell,
                        second_polynomial,
                        support,
                        cells,
                        index,
                    )
        columns.append(column)

    all_keys = set().union(*(set(column) for column in columns))
    pure_exception_keys = []
    for key in sorted(all_keys):
        monomials = set().union(*(set(column.get(key, {})) for column in columns))
        if monomials and all(
            len(monomial) == 1 and monomial[0] in exception_indices
            for monomial in monomials
        ):
            pure_exception_keys.append(key)
    coordinate_ranks = []
    for variable in sorted(exception_indices):
        matrix = [
            tuple(column.get(key, {}).get((variable,), 0) for column in columns)
            for key in pure_exception_keys
        ]
        coordinate_ranks.append(BASE.rational_rank(matrix))
    assert len(pure_exception_keys) == len(exception_indices)
    assert coordinate_ranks == [6] * len(exception_indices)
    return {
        "name": name,
        "mode": mode,
        "factor_parameter_count": len(factor_variables),
        "exception_parameter_count": len(exception_indices),
        "pure_exception_weight_count": len(pure_exception_keys),
        "coordinate_exception_ranks_over_Q": coordinate_ranks,
        "minimum_fixed_weight_rank": min(coordinate_ranks),
        "rank_allowed_by_retaining_13_of_18_rectangles": 5,
        "conclusion": "Every rank-at-most-five leakage point has zero exception parameters.",
    }


def build_payload() -> dict[str, object]:
    linear = [
        linear_reduction_certificate(name, support, targets, mode)
        for name, support, targets, mode in orbit_data()
    ]
    exception = [
        exception_certificate(name, support, targets, mode)
        for name, support, targets, mode in orbit_data()
    ]
    assert [row["kernel_dimension"] for row in linear] == [18, 30, 28]
    assert [row["factor_parameter_count"] for row in linear] == [6, 6, 4]
    assert [row["exception_parameter_count"] for row in linear] == [12, 24, 24]
    return {
        "status": [
            "EXACT_QQ_BIFLAG_4X3_GRAPH_REDUCTION",
            "PURE_PROJECTIVE_BIFLAG_PRODUCT_GLOBALIZATION",
            "CERTIFIED_A72_KAPPA3_BIFLAG_BRANCH_EXCLUSION",
            "N6-107",
        ],
        "ambient": {
            "biflag": "M=R4 tensor C5 + R5 tensor C3",
            "intrinsic_quadratic_space": "K=E2 intersect Sym^2(M)",
            "dimension_of_K": 72,
        },
        "linear_graph_reduction": {
            "orbit_certificates": linear,
            "minimum_rank_outside_every_kernel": 6,
            "rank_allowed_by_retaining_13_of_18_rectangles": 5,
        },
        "exception_reduction": {
            "orbit_certificates": exception,
            "minimum_fixed_weight_rank": 6,
            "conclusion": (
                "The two noncore R4 tensor B3 charts contain only column-factor products; "
                "the tail-row chart contains only row-factor products A4' tensor C3."
            ),
        },
        "product_dimension_gate": {
            "noncore_R4_tensor_B3": {
                "row_quadratic_dimension": 6,
                "required_column_quadratic_dimension": 3,
                "branch_count": 9,
                "branch_dimension": 2,
            },
            "tail_A4_tensor_C3": {
                "column_quadratic_dimension": 3,
                "row_quadratic_dimensions": [5, 6],
                "branch_count": 1,
                "branch_dimension": 4,
            },
        },
        "globalization": {
            "projective_locus": (
                "Z={U in Gr(12,M): dim(K intersect Sym^2(U)) at least 13}"
            ),
            "coordinate_fixed_point_count": 34,
            "coordinate_orbit_count": 6,
            "local_chart_coverage": {
                "N6-105_core_4x3": 1,
                "N6-106_3x4": 2,
                "N6-107_remaining_4x3": 3,
            },
            "closed_product_locus": (
                "Gr(3,R) x Gr(4,C) union Gr(4,R) x Gr(3,C)"
            ),
            "conclusion": (
                "Every U with dim(K intersect Sym^2(U)) at least 13 is a product "
                "A3 tensor B4 or A4 tensor B3."
            ),
        },
        "actual_pair_consequence": (
            "N6-068 excludes an actual complementary Chow pair on every product U in Z. "
            "Therefore the biflag second-shadow branch at "
            "(a2,kappa2,t2)=(72,3,15) is impossible."
        ),
        "partial_section_difference_consequence": (
            "At the a2=72 states with kappa2=1 or 2, every complementary-edge pair "
            "shadow carrying a 13- or 14-dimensional section difference is also a product. "
            "Excluding such partial actual section differences is a new open interface; "
            "N6-068 requires the full dimension fifteen."
        ),
        "remaining_lower29_frontier": (
            "The other nine N6-102 scalar states remain. In particular this theorem does "
            "not prove ordinary lower 29, exact Chow rank 32, or a border-rank bound."
        ),
        "claim_boundary": (
            "The three affine 4x3 chart reductions are exact characteristic-zero "
            "certificates over Q. The component globalization is pure projective torus "
            "geometry and uses the N6-105 coordinate enumeration and the N6-105/N6-106 "
            "local chart theorems. Only the N6-103 biflag branch is excluded here."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen JSON does not match exact replay")
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
