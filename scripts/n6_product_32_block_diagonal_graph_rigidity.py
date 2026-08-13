"""Exact regression for the pure block-diagonal K3,2 graph rigidity lemma."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, rank_mod, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, rank_mod, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_32_block_diagonal_graph_rigidity.json"


def commutator_system() -> dict[str, object]:
    variables = sp.symbols("s0:9")
    matrix = sp.Matrix(3, 3, variables)
    equations = []
    for i, j in combinations(range(3), 2):
        quadratic = sp.zeros(3)
        quadratic[i, j] = quadratic[j, i] = 1
        equations.extend(list(matrix.T * quadratic - quadratic * matrix))
    coefficient_matrix = sp.Matrix([
        [sp.expand(equation).coeff(variable) for variable in variables]
        for equation in equations
    ])
    nullspace = coefficient_matrix.nullspace()
    require(coefficient_matrix.rank() == 8, coefficient_matrix.rank())
    require(
        len(nullspace) == 1
        and sp.Matrix(3, 3, nullspace[0]) == sp.eye(3),
        nullspace,
    )
    return {
        "coefficient_matrix_shape": list(coefficient_matrix.shape),
        "exact_QQ_rank": int(coefficient_matrix.rank()),
        "exact_QQ_nullity": len(nullspace),
        "kernel_generator": "identity_3",
    }


def graph_pair(first: list[list[int]], second: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    left: list[list[int]] = []
    right: list[list[int]] = []
    for row in range(3):
        for column in range(2):
            vector_left = [0] * 12
            vector_right = [0] * 12
            vector_left[4 * row + column] = 1
            vector_right[4 * row + column] = 1
            operator = first if column == 0 else second
            target_column = column + 2
            for target_row in range(3):
                vector_left[4 * target_row + target_column] = operator[target_row][row]
                vector_right[4 * target_row + target_column] = -operator[target_row][row]
            left.append(vector_left)
            right.append(vector_right)
    return left, right


def exact_examples() -> dict[str, object]:
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    diagonal = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    shear = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    table = []
    for name, first, second in (
        ("scalar_scalar", identity, [[2 * entry for entry in row] for row in identity]),
        ("nonscalar_scalar", diagonal, identity),
        ("shear_scalar", shear, identity),
    ):
        left, right = graph_pair(first, second)
        table.append({
            "name": name,
            "sum_rank_over_QQ": int(sp.Matrix.hstack(*map(sp.Matrix, left + right)).rank()),
            "cross_rank_over_QQ": int(sp.Matrix([beta(x, y) for x in left for y in right]).rank()),
        })
    require(table[0]["cross_rank_over_QQ"] == 6, table)
    require(all(row["cross_rank_over_QQ"] > 6 for row in table[1:]), table)
    return {"examples": table}


def finite_field_row_twist_screen() -> dict[str, object]:
    """Complete bounded F3 diagnostic for T=S tensor identity_2."""
    histogram: dict[str, int] = {}
    invertible_count = 0
    low_count = 0
    scalar_low_count = 0
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    for entries in product(range(3), repeat=9):
        matrix = [list(entries[3 * i:3 * i + 3]) for i in range(3)]
        if rank_mod(matrix) < 3:
            continue
        invertible_count += 1
        left, right = graph_pair(matrix, matrix)
        cross_rank = rank_mod([beta(x, y) for x in left for y in right])
        key = str(cross_rank)
        histogram[key] = histogram.get(key, 0) + 1
        if cross_rank <= 6:
            low_count += 1
            scalar_low_count += int(
                all(
                    matrix[i][j] == (matrix[0][0] if i == j else 0)
                    for i in range(3)
                    for j in range(3)
                )
            )
    require(invertible_count == 12_792, invertible_count)
    require(low_count == scalar_low_count == 2, (low_count, scalar_low_count))
    return {
        "status": "COMPLETE_F3_RESTRICTED_FAMILY_DIAGNOSTIC_ONLY",
        "candidate_count": 3**9,
        "invertible_matrix_count": invertible_count,
        "cross_rank_histogram": histogram,
        "rank_at_most_six_count": low_count,
        "all_low_rank_matrices_are_nonzero_scalars": True,
        "not_used_for_characteristic_zero_proof": True,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-117",
        "status": (
            "PURE_BLOCK_DIAGONAL_K32_GRAPH_RIGIDITY; "
            "EXACT_QQ_COMMUTATOR_REPLAY; BOUNDED_F3_DIAGNOSTIC"
        ),
        "field": "algebraically closed characteristic zero",
        "commutator_scalar_lemma": commutator_system(),
        "exact_examples": exact_examples(),
        "finite_field_row_twist_screen": finite_field_row_twist_screen(),
        "pure_theorem": {
            "hypothesis": (
                "T:A3 tensor <e0,e1> to A3 tensor <e2,e3> is block diagonal "
                "with invertible row blocks S,R; L=graph(T), M=graph(-T)"
            ),
            "conclusion": (
                "E34 cross rank at most six forces S and R scalar; hence the "
                "pair is common-A3 product and its twelve-kernel block ranks are at most nine"
            ),
        },
        "boundary": {
            "not_proved": [
                "a general invertible graph T with cross rank at most six preserves a two-plus-two column matching",
                "the full K23/K32 formal germ exhaustion",
                "the kappa2=0 six-color endpoint or ordinary lower 29",
            ]
        },
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
    print("certificate=N6-117")
    print("commutator_rank=8")
    print("F3_invertible_row_twists=12792")
    print("F3_low_rank_row_twists=2")
    print("status=PASS")


if __name__ == "__main__":
    main()
