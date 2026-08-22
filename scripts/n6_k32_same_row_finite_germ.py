"""Exact local germ at a same-row K3,2 finite equality point."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, rank_mod, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, rank_mod, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_same_row_finite_germ.json"
SUPPORT = (0, 1, 4, 5, 8, 9)
COMPLEMENT = (2, 3, 6, 7, 10, 11)


def unit(index: int) -> list[int]:
    return [int(i == index) for i in range(12)]


def base_pair() -> tuple[list[list[int]], list[list[int]]]:
    left = [unit(index) for index in SUPPORT]
    right = [unit(index) for index in SUPPORT]
    for row in range(3):
        basis_index = SUPPORT.index(4 * row)
        left[basis_index][4 * row + 2] = 1
        right[basis_index][4 * row + 2] = -1
    return left, right


def pivot_rows_and_columns(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    _, columns = matrix.rref()
    columns = list(columns)
    rows = list(matrix[:, columns].T.rref()[1])
    return rows, columns


def frame_sum_rank(left: list[list[object]], right: list[list[object]]) -> int:
    return int(sp.Matrix.hstack(sp.Matrix(left).T, sp.Matrix(right).T).rank())


def cross_rank(left: list[list[object]], right: list[list[object]]) -> int:
    return int(sp.Matrix([beta(x, y) for x in left for y in right]).rank())


def branch_frames(
    a: object,
    b: object,
    c: object,
    branch: str,
) -> tuple[list[list[object]], list[list[object]]]:
    left: list[list[object]] = [unit(index) for index in SUPPORT]
    right: list[list[object]] = [unit(index) for index in SUPPORT]
    if branch == "plus":
        right_b = b
    elif branch == "minus":
        right_b = -b
    elif branch == "product":
        right_b = 0
    else:
        raise ValueError(branch)
    for row in range(3):
        col0 = 2 * row
        col1 = col0 + 1
        left[col0][4 * row + 2] = 1 - a
        right[col0][4 * row + 2] = -1 + a
        left[col1][4 * row + 2] = b
        right[col1][4 * row + 2] = right_b
        left[col1][4 * row + 3] = -c
        right[col1][4 * row + 3] = c
    return left, right


def local_certificate() -> dict[str, object]:
    left, right = base_pair()
    base = sp.Matrix([beta(x, y) for x in left for y in right])
    pivot_rows, pivot_columns = pivot_rows_and_columns(base)
    lower_rows = [i for i in range(36) if i not in pivot_rows]
    right_columns = [i for i in range(18) if i not in pivot_columns]

    def blocks(matrix: sp.Matrix) -> tuple[sp.Matrix, ...]:
        return (
            matrix.extract(pivot_rows, pivot_columns),
            matrix.extract(pivot_rows, right_columns),
            matrix.extract(lower_rows, pivot_columns),
            matrix.extract(lower_rows, right_columns),
        )

    a0, b0, c0, _ = blocks(base)
    inverse0 = a0.inv()
    labels: list[tuple[str, int, int]] = []
    derivatives: list[sp.Matrix] = []
    for side in ("L", "M"):
        for basis_index, _source in enumerate(SUPPORT):
            for target in COMPLEMENT:
                labels.append((side, target, SUPPORT[basis_index]))
                target_vector = unit(target)
                rows: list[list[int]] = []
                for i in range(6):
                    for j in range(6):
                        if side == "L" and i == basis_index:
                            rows.append(beta(target_vector, right[j]))
                        elif side == "M" and j == basis_index:
                            rows.append(beta(left[i], target_vector))
                        else:
                            rows.append([0] * 18)
                derivatives.append(sp.Matrix(rows))

    def first_schur(derivative: sp.Matrix) -> sp.Matrix:
        a1, b1, c1, _ = blocks(derivative)
        inverse1 = -inverse0 * a1 * inverse0
        return derivative.extract(lower_rows, right_columns) - (
            c1 * inverse0 * b0 + c0 * inverse1 * b0 + c0 * inverse0 * b1
        )

    linear = sp.Matrix.hstack(*[
        sp.Matrix(list(first_schur(derivative))) for derivative in derivatives
    ])
    require(
        rank_mod([[int(entry) for entry in row] for row in linear.tolist()]) == 68,
        "linear rank",
    )
    kernel = linear.nullspace()
    require(len(kernel) == 4, len(kernel))
    variables = sp.symbols("x0:4")
    coefficients = [
        sum((variables[a] * kernel[a][i] for a in range(4)), sp.Integer(0))
        for i in range(72)
    ]
    first_matrix = sum(
        (coefficients[i] * derivatives[i] for i in range(72)), sp.zeros(36, 18)
    )

    second_matrix = sp.zeros(36, 18)
    for i in range(6):
        for j in range(6):
            delta_left = [0] * 12
            delta_right = [0] * 12
            for a, target in enumerate(COMPLEMENT):
                delta_left[target] = coefficients[i * 6 + a]
                delta_right[target] = coefficients[36 + j * 6 + a]
            second_matrix[i * 6 + j, :] = sp.Matrix(
                1, 18, beta(delta_left, delta_right)
            )

    a1, b1, c1, _ = blocks(first_matrix)
    a2, b2, c2, d2 = blocks(second_matrix)
    inverse1 = -inverse0 * a1 * inverse0
    inverse2 = inverse0 * a1 * inverse0 * a1 * inverse0 - inverse0 * a2 * inverse0
    second_schur = sp.expand(
        d2
        - (
            c2 * inverse0 * b0
            + c1 * inverse1 * b0
            + c1 * inverse0 * b1
            + c0 * inverse2 * b0
            + c0 * inverse1 * b1
            + c0 * inverse0 * b2
        )
    )
    monomials = [
        variables[i] * variables[j]
        for i, j in combinations_with_replacement(range(4), 2)
    ]
    quadratic = sp.Matrix([
        [sp.Poly(entry, *variables).coeff_monomial(monomial) for monomial in monomials]
        for entry in list(second_schur)
    ])
    _, pivot_linear_columns = linear.rref()
    pivot_linear_columns = list(pivot_linear_columns)
    pivot_linear_rows = list(linear[:, pivot_linear_columns].T.rref()[1])
    other_rows = [i for i in range(linear.rows) if i not in pivot_linear_rows]
    square = linear.extract(pivot_linear_rows, pivot_linear_columns)
    residual = (
        quadratic.extract(other_rows, range(len(monomials)))
        - linear.extract(other_rows, pivot_linear_columns)
        * square.inv()
        * quadratic.extract(pivot_linear_rows, range(len(monomials)))
    )
    reduced, pivots = residual.rref()
    generators = [
        sp.factor(
            sum(reduced[row, column] * monomials[column] for column in range(10))
        )
        for row in range(len(pivots))
    ]
    expected = {
        sp.expand(variables[0] ** 2 - variables[2] ** 2),
        variables[0] * variables[3],
        variables[2] * variables[3],
    }
    require({sp.expand(item) for item in generators} == expected, generators)

    a, b, c = sp.symbols("a b c")
    branches: dict[str, dict[str, int]] = {}
    for name, branch, values in (
        ("plus", "plus", (a, b, 0)),
        ("minus", "minus", (a, b, 0)),
        ("product", "product", (a, 0, c)),
    ):
        branch_left, branch_right = branch_frames(*values, branch)
        branches[name] = {
            "cross_rank": cross_rank(branch_left, branch_right),
            "sum_rank": frame_sum_rank(branch_left, branch_right),
        }
    require(
        branches == {
            "plus": {"cross_rank": 6, "sum_rank": 9},
            "minus": {"cross_rank": 6, "sum_rank": 9},
            "product": {"cross_rank": 6, "sum_rank": 12},
        },
        branches,
    )

    base_sum_rank = frame_sum_rank(left, right)
    determinant = sp.factor(
        sp.Matrix.hstack(
            sp.Matrix(branch_frames(x1 := variables[1], 0, variables[3], "product")[0]).T,
            sp.Matrix(branch_frames(x1, 0, variables[3], "product")[1]).T,
        ).det()
    )
    # The assignment above is deliberately the linear chart used by the
    # product branch; keep the displayed formula stable in the payload.
    require(
        determinant == 64 * variables[3] ** 3 * (variables[1] - 1) ** 3,
        determinant,
    )

    return {
        "base_cross_rank": int(base.rank()),
        "base_sum_rank": base_sum_rank,
        "schur_shape": [len(lower_rows) * len(right_columns), 72],
        "linear_rank": 68,
        "kernel_dimension": 4,
        "quadratic_generators": [str(item) for item in generators],
        "reduced_components": [
            "(x3=0, x0-x2=0)",
            "(x3=0, x0+x2=0)",
            "(x0=0, x2=0)",
        ],
        "branches": branches,
        "complement_determinant_on_product": str(determinant),
        "initial_ideal": "(x0^2-x2^2,x0*x3,x2*x3)",
        "formal_sandwich": True,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-125",
        "status": "EXACT_SAME_ROW_FINITE_GERM_EXCLUSION",
        "field": "characteristic zero",
        "hypothesis": (
            "the finite graph pair at the same-row K3,2 unit direction "
            "T=I3 tensor E00"
        ),
        "exact_certificate": local_certificate(),
        "consequence": (
            "The completed rank-at-most-six germ is the union of two "
            "sum-rank-nine branches and one common-A product branch. The "
            "product branch is excluded for an actual twelve-dimensional "
            "Chow section difference by the N6-119 common-A block barrier."
        ),
        "symmetry": "column permutations carry this representative to all four same-row directions",
        "boundary": [
            "does not classify arbitrary 6 by 6 graph operators",
            "does not classify mixed-weight sums at the diagonal K3,2 collision",
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
    print("certificate=N6-125")
    print("linear_rank=68")
    print("branches=3")
    print("status=PASS")


if __name__ == "__main__":
    main()
