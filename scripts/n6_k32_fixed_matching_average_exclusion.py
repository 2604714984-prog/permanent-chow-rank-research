#!/usr/bin/env python3
"""N6-134: exclude nonzero average in a fixed K3,2 matching graph.

The theorem is deliberately restricted to the relative operator T=I after
normalizing one fixed 2+2 column matching.  It is an exact characteristic-zero
certificate for the full average graph chart, not a classification of general
invertible graph operators.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_fixed_matching_average_exclusion.json"


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def zero_diagonal_row_basis() -> tuple[sp.Matrix, ...]:
    basis = []
    for i, j in combinations(range(3), 2):
        matrix = sp.zeros(6)
        matrix[2 * i, 2 * j + 1] = 1
        matrix[2 * i + 1, 2 * j] = 1
        matrix[2 * j, 2 * i + 1] = 1
        matrix[2 * j + 1, 2 * i] = 1
        basis.append(matrix)
    return tuple(basis)


def block_symmetric_row_basis() -> tuple[sp.Matrix, ...]:
    basis = []
    for i, j in combinations(range(3), 2):
        for p in range(2):
            for q in range(2):
                matrix = sp.zeros(6)
                matrix[2 * i + p, 2 * j + q] = 1
                matrix[2 * j + p, 2 * i + q] = 1
                basis.append(matrix)
    return tuple(basis)


def flatten(matrix: sp.Matrix) -> list[sp.Expr]:
    return [matrix[i, j] for i in range(matrix.rows) for j in range(matrix.cols)]


def pair_matrix(
    trace: sp.Expr,
    upper: sp.Expr,
    lower: sp.Expr,
    delta_i: sp.Expr,
    delta_j: sp.Expr,
) -> sp.Matrix:
    """Return the 8x6 row-edge block after the skew reduction.

    The exceptional average blocks have the form
      S_i = [[(trace+delta_i)/2, upper],
             [lower, (trace-delta_i)/2]].
    Columns are the one A variable, four B variables, and one C variable.
    The two 2x2 output blocks are the (i,j) and (j,i) row blocks.
    """

    identity = sp.eye(2)
    exchange = sp.Matrix([[0, 1], [1, 0]])

    def block(delta: sp.Expr) -> sp.Matrix:
        return sp.Matrix(
            [
                [(trace + delta) / 2, upper],
                [lower, (trace - delta) / 2],
            ]
        )

    si = block(delta_i)
    sj = block(delta_j)
    xi, xj = identity + si, identity + sj
    yi, yj = -identity + si, -identity + sj

    columns: list[list[sp.Expr]] = []
    columns.append(flatten(exchange) + flatten(exchange))
    for p in range(2):
        for q in range(2):
            b = sp.zeros(2)
            b[p, q] = 1
            first = b * yj + xi.T * b.T
            second = b * yi + xj.T * b.T
            columns.append(flatten(first) + flatten(second))
    first = xi.T * exchange * yj
    second = xj.T * exchange * yi
    columns.append(flatten(first) + flatten(second))
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))


def skew_constraint_matrix() -> sp.Matrix:
    """Linear equations for skew(S^T C) in skew(B), with S flattened."""

    c_basis = zero_diagonal_row_basis()
    pairs = list(combinations(range(6), 2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}

    # A skew(B) row-edge block is a scalar multiple of [[0,1],[-1,0]].
    constraints: list[list[int]] = []
    for r, s in combinations(range(3), 2):
        constraints.extend(
            [
                [pair_index[(2 * r, 2 * s)]],
                [pair_index[(2 * r + 1, 2 * s + 1)]],
                [pair_index[(2 * r, 2 * s + 1)], pair_index[(2 * r + 1, 2 * s)]],
            ]
        )
    for r in range(3):
        constraints.append([pair_index[(2 * r, 2 * r + 1)]])

    rows: list[list[sp.Expr]] = []
    for c in c_basis:
        for constraint in constraints:
            row = [sp.Integer(0)] * 36
            for output_index in constraint:
                i, j = pairs[output_index]
                for a in range(6):
                    row[a * 6 + i] += c[a, j]
                    row[a * 6 + j] -= c[a, i]
            rows.append(row)
    return sp.Matrix(rows)


def exceptional_form_certificate() -> dict[str, object]:
    matrix = skew_constraint_matrix()
    require(matrix.shape == (36, 36), matrix.shape)
    rank = matrix.rank()
    require(rank == 30, rank)
    return {
        "matrix_shape": list(matrix.shape),
        "exact_QQ_rank": rank,
        "exact_QQ_nullity": 36 - rank,
        "exceptional_form": (
            "S is block diagonal with S_i=[[ (tau+delta_i)/2,u ],"
            "[v,(tau-delta_i)/2]], i=0,1,2; tau,u,v are common."
        ),
    }


def minor_value(
    matrix: sp.Matrix, rows: tuple[int, ...], columns: tuple[int, ...]
) -> sp.Expr:
    return sp.factor(matrix.extract(rows, columns).det())


def pair_minor_certificate() -> dict[str, object]:
    t, u, v, d, e = sp.symbols("tau u v delta_i delta_j")
    matrix = pair_matrix(t, u, v, d, e)
    require(matrix.shape == (8, 6), matrix.shape)
    zero_rank = matrix.subs({t: 0, u: 0, v: 0, d: 0, e: 0}).rank()
    require(zero_rank == 2, zero_rank)

    constant_rows = (1, 6)
    constant_columns = (0, 2)
    constant = minor_value(matrix, constant_rows, constant_columns)
    require(constant == 2, constant)

    certificates = (
        ((0, 1, 6), (0, 2, 3), 4 * v),
        ((1, 6, 7), (0, 2, 3), 4 * u),
        ((1, 2, 6), (0, 2, 3), 2 * (d - e)),
        ((0, 1, 6), (0, 1, 3), d + e + 2 * t),
        ((1, 3, 6), (0, 2, 4), d + e - 2 * t),
    )
    minor_rows = []
    for rows, columns, expected in certificates:
        actual = minor_value(matrix, rows, columns)
        require(sp.expand(actual - expected) == 0, (rows, columns, actual, expected))
        minor_rows.append(
            {
                "rows": list(rows),
                "columns": list(columns),
                "polynomial": str(expected),
            }
        )
    return {
        "matrix_shape": list(matrix.shape),
        "rank_at_zero": zero_rank,
        "constant_rank_two_minor": {
            "rows": list(constant_rows),
            "columns": list(constant_columns),
            "value": int(constant),
        },
        "rank_three_minors": minor_rows,
        "rank_le_two_implication": "u=v=delta_i=delta_j=tau=0",
    }


def build_payload() -> dict[str, object]:
    skew = exceptional_form_certificate()
    pair = pair_minor_certificate()
    return {
        "certificate": "N6-134",
        "status": [
            "PURE_CHARACTERISTIC_ZERO_FIXED_MATCHING_AVERAGE_EXCLUSION",
            "EXACT_QQ_SYMBOLIC_MINORS",
        ],
        "ambient": "A3 tensor P2 to A3 tensor Q2 with one fixed 2+2 matching",
        "graph_pair": "L=graph(I+S), M=graph(S-I)",
        "rank_identity": (
            "The rank of the 18-variable annihilator map equals the cross rank; "
            "cross rank <=6 forces the skew subsystem to have rank <=3."
        ),
        "skew_exceptional_subspace": skew,
        "row_edge_pair_certificate": pair,
        "pure_conclusion": (
            "If the complementary fixed-matching graph pair has E34 cross rank "
            "at most 6, then S=0. Hence its average vanishes and it is the "
            "N6-115 matching product family after diagonal normalization."
        ),
        "claim_boundary": (
            "This is a pure theorem only for the fixed relative matching T=I "
            "up to diagonal/monomial normalization. It does not prove that an "
            "arbitrary invertible relative graph T has a matching, does not "
            "cover non-graph charts or K2,3 transpose components, and does not "
            "exclude the resulting relaxed product pair from an actual Chow "
            "section difference. It does not prove lower 29 or exact ChowRank(perm_6)."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == frozen, args.verify_json)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
