"""Exact full graph germ at the K3,2 matching pair (average plus relative charts)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_average_relative_germ.json"


def graph_pair(
    left_operator: sp.Matrix, right_operator: sp.Matrix
) -> tuple[list[list[object]], list[list[object]]]:
    left: list[list[object]] = []
    right: list[list[object]] = []
    for row in range(3):
        for source_column in range(2):
            source = 2 * row + source_column
            vector_left: list[object] = [0] * 12
            vector_right: list[object] = [0] * 12
            vector_left[4 * row + source_column] = 1
            vector_right[4 * row + source_column] = 1
            for target in range(6):
                target_row, target_column = divmod(target, 2)
                vector_left[4 * target_row + target_column + 2] = (
                    left_operator[target, source]
                )
                vector_right[4 * target_row + target_column + 2] = (
                    right_operator[target, source]
                )
            left.append(vector_left)
            right.append(vector_right)
    return left, right


def cross_matrix(left_operator: sp.Matrix, right_operator: sp.Matrix) -> sp.Matrix:
    left, right = graph_pair(left_operator, right_operator)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def pivot_data(
    base: sp.Matrix,
) -> tuple[list[int], list[int], list[int], list[int], sp.Matrix]:
    _, pivot_columns = base.rref()
    _, pivot_rows = base.T.rref()
    pivot_columns = list(pivot_columns)
    pivot_rows = list(pivot_rows)
    rows_out = [i for i in range(base.rows) if i not in pivot_rows]
    columns_out = [j for j in range(base.cols) if j not in pivot_columns]
    pivot = base.extract(pivot_rows, pivot_columns)
    require(pivot.det() != 0, pivot.det())
    return pivot_rows, pivot_columns, rows_out, columns_out, pivot


def exact_certificate() -> dict[str, object]:
    identity = sp.eye(6)
    base = cross_matrix(identity, -identity)
    pivot_rows, pivot_columns, rows_out, columns_out, pivot = pivot_data(base)
    pivot_inverse = pivot.inv()
    base_pq = base.extract(pivot_rows, columns_out)
    base_rp = base.extract(rows_out, pivot_columns)

    derivative_columns: list[list[sp.Expr]] = []
    for kind in ("average", "relative"):
        for target in range(6):
            for source in range(6):
                direction = sp.zeros(6)
                direction[target, source] = 1
                if kind == "average":
                    plus_left = identity + direction
                    plus_right = -identity + direction
                    minus_left = identity - direction
                    minus_right = -identity - direction
                else:
                    plus_left = identity + direction
                    plus_right = -identity - direction
                    minus_left = identity - direction
                    minus_right = -identity + direction
                derivative = (
                    cross_matrix(plus_left, plus_right)
                    - cross_matrix(minus_left, minus_right)
                ) / 2
                dpp = derivative.extract(pivot_rows, pivot_columns)
                dpq = derivative.extract(pivot_rows, columns_out)
                drp = derivative.extract(rows_out, pivot_columns)
                drq = derivative.extract(rows_out, columns_out)
                schur_derivative = (
                    drq
                    - drp * pivot_inverse * base_pq
                    - base_rp * pivot_inverse * dpq
                    + base_rp * pivot_inverse * dpp * pivot_inverse * base_pq
                )
                derivative_columns.append(list(schur_derivative))

    jacobian = sp.Matrix.hstack(
        *[sp.Matrix(column) for column in derivative_columns]
    )
    free_columns = [36, 43]  # relative T[0,0] and T[1,1].
    normal_columns = [i for i in range(72) if i not in free_columns]
    normal_jacobian = jacobian[:, normal_columns]
    _, minor_rows = normal_jacobian.T.rref()
    minor_rows = list(minor_rows)
    minor = normal_jacobian.extract(minor_rows, range(70))

    require(base.rank() == 6, base.rank())
    require(jacobian.rank() == 70, jacobian.rank())
    require(normal_jacobian.rank() == 70, normal_jacobian.rank())
    require(minor.det() == -70368744177664, minor.det())
    nullspace = jacobian.nullspace()
    require(len(nullspace) == 2, len(nullspace))
    expected_first = sp.zeros(72, 1)
    expected_second = sp.zeros(72, 1)
    for index in (36, 50, 64):
        expected_first[index] = 1
    for index in (43, 57, 71):
        expected_second[index] = 1
    require(
        sp.Matrix.hstack(*nullspace).columnspace()
        == sp.Matrix.hstack(expected_first, expected_second).columnspace(),
        nullspace,
    )

    x, y = sp.symbols("x y")
    relative = sp.diag(x, y, x, y, x, y)
    diagonal = cross_matrix(relative, -relative)
    diagonal_pivot = diagonal.extract(pivot_rows, pivot_columns)
    diagonal_schur = (
        diagonal.extract(rows_out, columns_out)
        - diagonal.extract(rows_out, pivot_columns)
        * diagonal_pivot.inv()
        * diagonal.extract(pivot_rows, columns_out)
    )
    require(all(sp.simplify(entry) == 0 for entry in diagonal_schur), "diagonal")
    require(sp.factor(diagonal_pivot.det()) == -8 * y**3, diagonal_pivot.det())

    return {
        "base_cross_matrix_shape": list(base.shape),
        "base_cross_rank": int(base.rank()),
        "pivot_rows": pivot_rows,
        "pivot_columns": pivot_columns,
        "pivot_determinant": int(pivot.det()),
        "schur_shape": [len(rows_out), len(columns_out)],
        "jacobian_shape": list(jacobian.shape),
        "jacobian_rank": int(jacobian.rank()),
        "tangent_dimension": 72 - int(jacobian.rank()),
        "average_variable_count": 36,
        "relative_variable_count": 36,
        "free_coordinates": ["T[0,0]", "T[1,1]"],
        "normal_minor_rows": minor_rows,
        "normal_minor_determinant": int(minor.det()),
        "nullspace_generators": ["relative_column_0_scaling", "relative_column_1_scaling"],
        "diagonal_family": "A=0; T=diag(x,y,x,y,x,y)",
        "diagonal_pivot_determinant": "-8*y^3",
        "diagonal_schur_identically_zero": True,
    }


def examples() -> dict[str, object]:
    rows = []
    for x, y in ((1, 1), (2, 3), (1, 2)):
        relative = sp.diag(x, y, x, y, x, y)
        matrix = cross_matrix(relative, -relative)
        rows.append({"x": x, "y": y, "cross_rank": int(matrix.rank())})
    require([row["cross_rank"] for row in rows] == [6, 6, 6], rows)
    return {"diagonal_relative_family": rows}


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-121",
        "status": "PURE_FORMAL_LOCAL_K32_AVERAGE_RELATIVE_GERM",
        "field": "characteristic zero",
        "hypothesis": (
            "L=graph(A+T), M=graph(A-T), with A,T in Mat_6 and T near I_6"
        ),
        "exact_certificate": exact_certificate(),
        "examples": examples(),
        "pure_consequence": (
            "The complete 72-variable rank-at-most-six graph germ at "
            "(A,T)=(0,I) is exactly A=0 and "
            "T=diag(x,y,x,y,x,y)."
        ),
        "blowup_interpretation": (
            "This is the full average-relative chart over the full-rank "
            "exceptional direction T=I in the diagonal K3,2 collision."
        ),
        "boundary": [
            "does not classify lower-rank exceptional directions",
            "does not classify arbitrary invertible T globally",
            "does not supply the six-term Chow cocycle by itself",
            "does not prove ordinary lower 29 or exact rank 32",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            "frozen JSON differs from exact replay",
        )
    print("certificate=N6-121")
    print("base_rank=6")
    print("jacobian_rank=70")
    print("normal_minor=-70368744177664")
    print("status=PASS")


if __name__ == "__main__":
    main()
