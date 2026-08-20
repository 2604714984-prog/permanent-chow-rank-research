"""Pure annihilator reduction for the general K3,2 graph operator.

For L=graph(T), M=graph(-T), the 18-dimensional cross target splits into
PP, PQ, and QQ column blocks.  The cross annihilator splits accordingly into
an independent B-kernel and C-kernel.  This script replays the reduction over
QQ on small exact examples; the reduction itself is the algebraic statement.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_annihilator_reduction.json"
ROW_EDGES = tuple(combinations(range(3), 2))
COLUMN_EDGES = tuple(combinations(range(4), 2))


def grouped_index(row: int, column: int) -> int:
    if column < 2:
        return 2 * row + column
    return 6 + 2 * row + column - 2


def row_major_vector(grouped: list[object]) -> list[object]:
    vector = [0] * 12
    for row in range(3):
        for column in range(2):
            vector[4 * row + column] = grouped[2 * row + column]
            vector[4 * row + column + 2] = grouped[6 + 2 * row + column]
    return vector


def diagonal_block_b_dimension(entries: tuple[object, ...]) -> int:
    """Closed b(T) formula for T=diag(D0,D1,D2), Di=diag(ai,bi)."""

    require(len(entries) == 6, entries)
    answer = 0
    for first, second in ROW_EDGES:
        a_i, b_i = entries[2 * first : 2 * first + 2]
        a_j, b_j = entries[2 * second : 2 * second + 2]
        answer += int(a_i == a_j) + int(b_i == b_j)
        answer += int(a_i * b_i == a_j * b_j)
    return answer


def embedded_basis(row_edge: tuple[int, int], column_edge: tuple[int, int]) -> sp.Matrix:
    """Embed one E_A tensor E_C coordinate in Sym^2(A tensor B)."""

    matrix = sp.zeros(12, 12)
    i, j = row_edge
    c, d = column_edge
    for first, second in (
        (grouped_index(i, c), grouped_index(j, d)),
        (grouped_index(i, d), grouped_index(j, c)),
    ):
        matrix[first, second] += 1
        matrix[second, first] += 1
    return matrix


def basis_matrices() -> tuple[list[sp.Matrix], list[sp.Matrix], list[sp.Matrix]]:
    a_basis: list[sp.Matrix] = []
    b_basis: list[sp.Matrix] = []
    c_basis: list[sp.Matrix] = []
    for row_edge in ROW_EDGES:
        for column_edge in COLUMN_EDGES:
            matrix = embedded_basis(row_edge, column_edge)
            if column_edge == (0, 1):
                a_basis.append(matrix)
            elif column_edge == (2, 3):
                c_basis.append(matrix)
            else:
                b_basis.append(matrix)
    require(len(a_basis) == 3, len(a_basis))
    require(len(b_basis) == 12, len(b_basis))
    require(len(c_basis) == 3, len(c_basis))
    return a_basis, b_basis, c_basis


def graph_pair(T: sp.Matrix, sign: int) -> list[list[object]]:
    vectors: list[list[object]] = []
    for source in range(6):
        grouped = [
            int(index == source) if index < 6 else sign * T[index - 6, source]
            for index in range(12)
        ]
        vectors.append(row_major_vector(grouped))
    return vectors


def cross_matrix(T: sp.Matrix) -> sp.Matrix:
    left = graph_pair(T, 1)
    right = graph_pair(T, -1)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def flatten_square(matrix: sp.Matrix) -> sp.Matrix:
    """Flatten a grouped 6-by-6 matrix in the fixed row-major order."""

    return sp.Matrix(
        [matrix[row, column] for row in range(matrix.rows) for column in range(matrix.cols)]
    )


def off_diagonal_projection_map(T: sp.Matrix) -> sp.Matrix:
    """Return the skew-part map projected to the three off-diagonal blocks.

    The domain is the 12-dimensional ``mathcal B`` space, with one arbitrary
    2-by-2 block for each row edge.  The target is the direct sum of the
    (0,1), (0,2), and (1,2) 2-by-2 blocks, so a nonzero rank-one block in one
    of the six off-diagonal positions contributes a two-dimensional image in
    the indicated component.  This small map is useful for the cycle
    obstruction below; it is not a replacement for the full 15-equation map.
    """

    _, b_basis, _ = basis_matrices()
    columns: list[sp.Matrix] = []
    for basis in b_basis:
        mixed = basis.extract(range(6), range(6, 12))
        skew = mixed * T - (mixed * T).T
        output: list[object] = []
        for first, second in ((0, 1), (0, 2), (1, 2)):
            output.extend(
                skew[2 * first + row, 2 * second + column]
                for row in range(2)
                for column in range(2)
            )
        columns.append(sp.Matrix(output))
    return sp.Matrix.hstack(*columns)


def off_diagonal_projection_rank(T: sp.Matrix) -> int:
    """Exact rank of :func:`off_diagonal_projection_map` over QQ."""

    return int(off_diagonal_projection_map(T).rank())


def reduction_dimensions(T: sp.Matrix) -> tuple[int, int, int, int]:
    a_basis, b_basis, c_basis = basis_matrices()

    # Membership in the PP target is a 3-dimensional linear condition, not
    # merely a support condition.  A permuted Q-block can occupy allowed
    # positions belonging to several different row edges without belonging to
    # their specific S0(A3) linear span.  Use the left-nullspace of the exact
    # A-space basis as a quotient map, so c(T) remains valid for arbitrary T.
    a_columns = sp.Matrix.hstack(*(flatten_square(b.extract(range(6), range(6))) for b in a_basis))
    a_quotient = sp.Matrix.vstack(*(vector.T for vector in a_columns.T.nullspace()))

    c_columns: list[sp.Matrix] = []
    for basis in c_basis:
        qq = basis.extract(range(6, 12), range(6, 12))
        transformed = T.T * qq * T
        c_columns.append(a_quotient * flatten_square(transformed))
    c_map = sp.Matrix.hstack(*c_columns)
    c_dimension = 3 - int(c_map.rank())

    b_columns: list[sp.Matrix] = []
    for basis in b_basis:
        mixed = basis.extract(range(6), range(6, 12))
        skew = mixed * T - (mixed * T).T
        b_columns.append(sp.Matrix(list(skew)))
    b_map = sp.Matrix.hstack(*b_columns)
    b_dimension = 12 - int(b_map.rank())

    cross_rank = int(cross_matrix(T).rank())
    annihilator_dimension = 18 - cross_rank
    require(annihilator_dimension == b_dimension + c_dimension, (T, cross_rank, b_dimension, c_dimension))
    return cross_rank, annihilator_dimension, b_dimension, c_dimension


def examples() -> list[dict[str, object]]:
    identity = sp.eye(6)
    matching_diagonal = sp.diag(1, 2, 1, 2, 1, 2)
    shear = identity.copy()
    shear[0, 1] = 1
    permutation = sp.Matrix(
        [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
        ]
    )
    table: list[dict[str, object]] = []
    for name, matrix in (
        ("identity", identity),
        ("matching_diagonal", matching_diagonal),
        ("row_shear", shear),
        ("column_row_permutation", permutation),
    ):
        cross_rank, annihilator, b_dimension, c_dimension = reduction_dimensions(matrix)
        table.append(
            {
                "name": name,
                "determinant": int(matrix.det()),
                "cross_rank_over_QQ": cross_rank,
                "annihilator_dimension": annihilator,
                "b_dimension": b_dimension,
                "c_dimension": c_dimension,
            }
        )
    require(table[0]["cross_rank_over_QQ"] == 6, table)
    require(table[1]["cross_rank_over_QQ"] == 6, table)
    require(table[2]["cross_rank_over_QQ"] == 12, table)
    require(table[3]["cross_rank_over_QQ"] == 14, table)
    return table


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-129",
        "status": "PURE_K32_CROSS_ANNIHILATOR_REDUCTION",
        "field": "characteristic zero",
        "target_dimension": 18,
        "spaces": {
            "A": "S0(A3) tensor S0(P2), dimension 3",
            "B": "S0(A3) tensor (P2 tensor Q2), dimension 12",
            "C": "S0(A3) tensor S0(Q2), dimension 3",
        },
        "exact_formula": (
            "rank cross(L,M) = 18 - b(T) - c(T), where b(T) is the dimension "
            "of {B in B-space: B*T is symmetric} and c(T) is the dimension "
            "of {C in C-space: T^T*C*T lies in A-space}."
        ),
        "rank_six_necessary_condition": "cross rank <= 6 implies b(T) + c(T) >= 12, hence b(T) >= 9",
        "examples": examples(),
        "pure_consequence": (
            "In this K3,2 graph slice, b(T)>=9 forces acyclic off-diagonal "
            "block support, hence a common diagonal block and a 2+2 column "
            "matching; the remaining obstruction is the full incidence "
            "argument outside this graph-pair slice."
        ),
        "boundary": [
            "does not classify arbitrary invertible graph operators outside this slice",
            "does not by itself prove ordinary lower 29 or exact Chow rank 32",
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
        require(payload == json.loads(args.verify_json.read_text(encoding="utf-8")), "frozen payload mismatch")
    print("certificate=N6-129")
    print("formula=rank_cross=18-b-c")
    print("rank_six_requires=b+c>=12")
    print("status=PASS")


if __name__ == "__main__":
    main()
