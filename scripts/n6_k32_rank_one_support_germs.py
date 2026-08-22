"""Exact local quadratic germs for two rank-one row-changing supports."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_rank_one_support_germs.json"


def graph_pair(
    left_operator: sp.Matrix, right_operator: sp.Matrix
) -> tuple[list[list[object]], list[list[object]]]:
    left: list[list[object]] = []
    right: list[list[object]] = []
    for source in range(6):
        source_row, source_column = divmod(source, 2)
        left_vector: list[object] = [0] * 12
        right_vector: list[object] = [0] * 12
        left_vector[4 * source_row + source_column] = 1
        right_vector[4 * source_row + source_column] = 1
        for target in range(6):
            target_row, target_column = divmod(target, 2)
            left_vector[4 * target_row + target_column + 2] = left_operator[
                target, source
            ]
            right_vector[4 * target_row + target_column + 2] = right_operator[
                target, source
            ]
        left.append(left_vector)
        right.append(right_vector)
    return left, right


def cross_pair(left_operator: sp.Matrix, right_operator: sp.Matrix) -> sp.Matrix:
    left, right = graph_pair(left_operator, right_operator)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def cross_matrix(operator: sp.Matrix) -> sp.Matrix:
    return cross_pair(operator, -operator)


def pivot_data(
    base: sp.Matrix,
) -> tuple[list[int], list[int], list[int], list[int], sp.Matrix]:
    _, pivot_columns = base.rref()
    _, pivot_rows = base.T.rref()
    pivot_columns = list(pivot_columns)
    pivot_rows = list(pivot_rows)
    rows_out = [row for row in range(base.rows) if row not in pivot_rows]
    columns_out = [column for column in range(base.cols) if column not in pivot_columns]
    pivot = base.extract(pivot_rows, pivot_columns)
    require(pivot.det() != 0, pivot.det())
    return pivot_rows, pivot_columns, rows_out, columns_out, pivot


def support_operator(pattern: str) -> sp.Matrix:
    block = {
        "same_source_column": [[1, 0], [1, 0]],
        "full": [[1, 1], [1, 1]],
    }[pattern]
    operator = sp.zeros(6)
    for target_column in range(2):
        for source_column in range(2):
            operator[target_column, 2 + source_column] = block[
                target_column
            ][source_column]
    return operator


def schur_jacobian(
    base_operator: sp.Matrix,
) -> tuple[sp.Matrix, list[sp.Matrix], tuple[list[int], list[int], list[int], list[int], sp.Matrix]]:
    base = cross_matrix(base_operator)
    pivot_rows, pivot_columns, rows_out, columns_out, pivot = pivot_data(base)
    pivot_inverse = pivot.inv()
    base_pq = base.extract(pivot_rows, columns_out)
    base_rp = base.extract(rows_out, pivot_columns)
    base_rr = base.extract(rows_out, columns_out)
    derivatives: list[sp.Matrix] = []
    schur_columns: list[sp.Matrix] = []
    for side in ("L", "M"):
        for source in range(6):
            for target in range(6):
                direction = sp.zeros(6)
                direction[target, source] = 1
                perturbed = (
                    cross_pair(base_operator + direction, -base_operator)
                    if side == "L"
                    else cross_pair(base_operator, -base_operator + direction)
                )
                derivative = perturbed - base
                derivatives.append(derivative)
                dpp = derivative.extract(pivot_rows, pivot_columns)
                dpq = derivative.extract(pivot_rows, columns_out)
                drp = derivative.extract(rows_out, pivot_columns)
                drq = derivative.extract(rows_out, columns_out)
                schur_columns.append(
                    drq
                    - drp * pivot_inverse * base_pq
                    - base_rp * pivot_inverse * dpq
                    + base_rp * pivot_inverse * dpp * pivot_inverse * base_pq
                )
    jacobian = sp.Matrix.hstack(
        *[sp.Matrix(list(column)) for column in schur_columns]
    )
    return jacobian, derivatives, (
        pivot_rows,
        pivot_columns,
        rows_out,
        columns_out,
        pivot,
    )


def kernel_operator(
    vector: sp.Matrix,
) -> sp.Matrix:
    operator = sp.zeros(6)
    for source in range(6):
        for target in range(6):
            left_value = vector[source * 6 + target]
            right_value = vector[36 + source * 6 + target]
            require(right_value == -left_value, (source, target, vector))
            operator[target, source] = left_value
    return operator


def quadratic_initial_generators(
    base_operator: sp.Matrix,
    jacobian: sp.Matrix,
    derivatives: list[sp.Matrix],
    pivot_info: tuple[list[int], list[int], list[int], list[int], sp.Matrix],
    kernel: list[sp.Matrix],
) -> tuple[list[sp.Expr], tuple[sp.Symbol, ...], sp.Matrix]:
    pivot_rows, pivot_columns, rows_out, columns_out, pivot = pivot_info
    pivot_inverse = pivot.inv()
    base = cross_matrix(base_operator)
    base_pq = base.extract(pivot_rows, columns_out)
    base_rp = base.extract(rows_out, pivot_columns)
    variables = sp.symbols(f"x0:{len(kernel)}")
    coefficients = [
        sum(variables[index] * kernel[index][coordinate] for index in range(len(kernel)))
        for coordinate in range(72)
    ]
    first_matrix = sum(
        (coefficients[index] * derivatives[index] for index in range(72)),
        sp.zeros(36, 18),
    )
    second_matrix = sp.zeros(36, 18)
    for left_source in range(6):
        for right_source in range(6):
            delta_left = [0] * 12
            delta_right = [0] * 12
            for target in range(6):
                target_row, target_column = divmod(target, 2)
                delta_left[4 * target_row + target_column + 2] = coefficients[
                    left_source * 6 + target
                ]
                delta_right[4 * target_row + target_column + 2] = coefficients[
                    36 + right_source * 6 + target
                ]
            second_matrix[left_source * 6 + right_source, :] = sp.Matrix(
                1, 18, beta(delta_left, delta_right)
            )
    a1 = first_matrix.extract(pivot_rows, pivot_columns)
    b1 = first_matrix.extract(pivot_rows, columns_out)
    c1 = first_matrix.extract(rows_out, pivot_columns)
    a2 = second_matrix.extract(pivot_rows, pivot_columns)
    b2 = second_matrix.extract(pivot_rows, columns_out)
    c2 = second_matrix.extract(rows_out, pivot_columns)
    d2 = second_matrix.extract(rows_out, columns_out)
    inverse1 = -pivot_inverse * a1 * pivot_inverse
    inverse2 = (
        pivot_inverse * a1 * pivot_inverse * a1 * pivot_inverse
        - pivot_inverse * a2 * pivot_inverse
    )
    second_schur = sp.expand(
        d2
        - (
            c2 * pivot_inverse * base_pq
            + c1 * inverse1 * base_pq
            + c1 * pivot_inverse * b1
            + base_rp * inverse2 * base_pq
            + base_rp * inverse1 * b1
            + base_rp * pivot_inverse * b2
        )
    )
    monomials = [
        variables[left] * variables[right]
        for left, right in combinations_with_replacement(range(len(kernel)), 2)
    ]
    rows: list[list[sp.Expr]] = []
    for entry in list(second_schur):
        polynomial = sp.Poly(entry, *variables)
        row = [polynomial.coeff_monomial(monomial) for monomial in monomials]
        if any(row):
            rows.append(row)
    quadratic = sp.Matrix(rows)
    reduced, pivots = quadratic.rref()
    generators = [
        sp.factor(
            sum(reduced[row, column] * monomials[column] for column in range(len(monomials)))
        )
        for row in range(len(pivots))
    ]
    return generators, variables, quadratic


def branch_data(
    operator: sp.Matrix,
    variables: tuple[sp.Symbol, ...],
    pattern: str,
) -> list[dict[str, object]]:
    parameters = dict(zip(variables, variables, strict=True))
    if pattern == "same_source_column":
        substitutions = [
            {variables[1]: variables[0]},
            {variables[2]: 0, variables[3]: 0, variables[4]: 0},
        ]
        equations = [
            ["x1-x0"],
            ["x2", "x3", "x4"],
        ]
    else:
        substitutions = [
            {variables[1]: variables[2]},
            {variables[0]: variables[2], variables[3]: 0, variables[4]: 0},
        ]
        equations = [
            ["x1-x2"],
            ["x0-x2", "x3", "x4"],
        ]
    result: list[dict[str, object]] = []
    for equation_list, substitution in zip(equations, substitutions, strict=True):
        branch_operator = operator.subs(substitution)
        cross_rank = int(cross_matrix(branch_operator).rank())
        operator_rank = int(branch_operator.rank())
        require(cross_rank <= 6, (pattern, equation_list, cross_rank))
        require(operator_rank <= 1, (pattern, equation_list, operator_rank))
        result.append(
            {
                "equations": equation_list,
                "cross_rank": cross_rank,
                "operator_rank": operator_rank,
                "sum_rank": 6 + operator_rank,
            }
        )
    return result


def one_pattern(pattern: str) -> dict[str, object]:
    operator = support_operator(pattern)
    jacobian, derivatives, pivot_info = schur_jacobian(operator)
    kernel = jacobian.nullspace()
    require(jacobian.rank() == 67, (pattern, jacobian.rank()))
    require(len(kernel) == 5, (pattern, len(kernel)))
    generators, variables, quadratic = quadratic_initial_generators(
        operator, jacobian, derivatives, pivot_info, kernel
    )
    expected = {
        "same_source_column": {
            sp.expand(variables[2] * (variables[0] - variables[1])),
            sp.expand(variables[3] * (variables[0] - variables[1])),
            sp.expand(variables[4] * (variables[0] - variables[1])),
        },
        "full": {
            sp.expand((variables[0] - variables[2]) * (variables[1] - variables[2])),
            sp.expand(variables[3] * (variables[1] - variables[2])),
            sp.expand(variables[4] * (variables[1] - variables[2])),
        },
    }[pattern]
    require({sp.expand(item) for item in generators} == expected, generators)
    operator_family = operator + sum(
        (variables[index] * kernel_operator(vector) for index, vector in enumerate(kernel)),
        sp.zeros(6),
    )
    branches = branch_data(operator_family, variables, pattern)
    return {
        "base_cross_rank": int(cross_matrix(operator).rank()),
        "base_operator_rank": int(operator.rank()),
        "jacobian_shape": list(jacobian.shape),
        "jacobian_rank": int(jacobian.rank()),
        "kernel_dimension": len(kernel),
        "kernel_operator_supports": [
            [
                {
                    "target": target,
                    "source": source,
                    "coefficient": int(vector[target + source * 6]),
                }
                for source in range(6)
                for target in range(6)
                if vector[target + source * 6]
            ]
            for vector in kernel
        ],
        "quadratic_generator_count": len(generators),
        "quadratic_initial_generators": [str(item) for item in generators],
        "quadratic_coefficient_rank": int(quadratic.rank()),
        "branches": branches,
        "formal_sandwich": True,
    }


def build_payload() -> dict[str, object]:
    patterns = {
        pattern: one_pattern(pattern)
        for pattern in ("same_source_column", "full")
    }
    return {
        "certificate": "N6-137",
        "status": "EXACT_QQ_RANK_ONE_SUPPORT_GERMS",
        "field": "characteristic zero",
        "hypothesis": (
            "finite K3,2 graph pairs L=graph(D), M=graph(-D) with D a "
            "rank-one row-changing coefficient support"
        ),
        "patterns": patterns,
        "consequence": (
            "For the same-source-column and full rank-one support types, the "
            "completed rank-at-most-six graph germ is contained in the two "
            "explicit noncomplementary branches given by the quadratic initial "
            "ideal; the branch sandwich is exact in the completed graph chart."
        ),
        "boundary": [
            "does not cover the single-cell type already treated by N6-123",
            "does not cover the same-target-row type",
            "does not cover non-graph charts or coupled six-term cocycles",
            "does not close the full K3,2 or K2,3 normal cone",
            "does not prove ordinary lower 29 or exact Chow rank 32",
            "does not make a border-rank claim",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen payload mismatch")
    print("certificate=N6-137")
    print("patterns=2")
    print("jacobian_rank=67")
    print("quadratic_generators=3+3")
    print("status=PASS")


if __name__ == "__main__":
    main()
