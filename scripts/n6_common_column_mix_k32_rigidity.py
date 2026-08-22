"""Pure characteristic-zero lemma for a common column-mixing K3,2 graph.

The calculation is deliberately small.  It isolates the subfamily
T=I_3 tensor H before the general 6 by 6 graph-matching problem.
"""

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
DEFAULT_JSON = ROOT / "data" / "n6_common_column_mix_k32_rigidity.json"


def graph_pair(H: sp.Matrix) -> tuple[list[list[object]], list[list[object]]]:
    """Return graph(H) and graph(-H) in the 3 by 4 ambient coordinates."""
    left: list[list[object]] = []
    right: list[list[object]] = []
    for row in range(3):
        for source_column in range(2):
            source = 2 * row + source_column
            vector_left: list[object] = [0] * 12
            vector_right: list[object] = [0] * 12
            vector_left[4 * row + source_column] = 1
            vector_right[4 * row + source_column] = 1
            for target_row in range(3):
                # T=I_3 tensor H: the row is unchanged.
                if target_row != row:
                    continue
                for target_column in range(2):
                    value = H[target_column, source_column]
                    vector_left[4 * target_row + target_column + 2] = value
                    vector_right[4 * target_row + target_column + 2] = -value
            left.append(vector_left)
            right.append(vector_right)
    return left, right


def cross_matrix(H: sp.Matrix) -> sp.Matrix:
    left, right = graph_pair(H)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def select_columns(matrix: sp.Matrix, column_edges: tuple[int, ...]) -> sp.Matrix:
    # beta orders the six column edges as 01,02,03,12,13,23 for each
    # of the three row edges.
    return matrix[:, [6 * row_edge + edge for row_edge in range(3) for edge in column_edges]]


def symbolic_certificate() -> dict[str, object]:
    a, b, c, d = sp.symbols("a b c d")
    H = sp.Matrix([[a, b], [c, d]])
    matrix = cross_matrix(H)
    mixed = select_columns(matrix, (1, 2, 3, 4))
    same = select_columns(matrix, (0, 5))
    same_block = same[:12, :2]
    # The displayed rows are the nonzero row types of one row-pair block.
    expected_same = sp.Matrix(
        [[0, -2 * a * c], [1, -(a * d + b * c)], [0, -2 * b * d]]
    )
    require(mixed.rank() == 3, mixed.rank())
    require(same.rank() == 6, same.rank())  # generic rank; the special drop is below.
    require(
        any(tuple(row) == tuple(expected_same.row(i)) for row in same_block.tolist() for i in (0, 1, 2)),
        "same-block symbolic rows were not found",
    )
    # The mixed rows are three copies (up to sign) of one nonzero vector.
    mixed_row = sp.Matrix([[-b, -d, a, c]])
    require(any(tuple(row[:4]) == tuple(mixed_row) for row in mixed.tolist()), "mixed row")
    return {
        "variables": ["a", "b", "c", "d"],
        "cross_matrix_shape": list(matrix.shape),
        "mixed_matrix_shape": list(mixed.shape),
        "same_matrix_shape": list(same.shape),
        "mixed_generic_rank": int(mixed.rank()),
        "same_generic_rank": int(same.rank()),
        "mixed_row_up_to_sign": "(-b,-d,a,c)",
        "same_block_row_types": [
            "(0,-2*a*c)",
            "(1,-a*d-b*c)",
            "(0,-2*b*d)",
        ],
        "same_rank_condition": "rank=1 iff a*c=0 and b*d=0; otherwise rank=2",
    }


def exact_examples() -> dict[str, object]:
    examples = {
        "diagonal": sp.Matrix([[2, 0], [0, 3]]),
        "anti_diagonal": sp.Matrix([[0, 2], [3, 0]]),
        "shear": sp.Matrix([[1, 1], [0, 1]]),
        "dense": sp.Matrix([[1, 2], [3, 5]]),
    }
    rows: list[dict[str, object]] = []
    for name, H in examples.items():
        require(H.det() != 0, (name, H.det()))
        matrix = cross_matrix(H)
        mixed = select_columns(matrix, (1, 2, 3, 4))
        same = select_columns(matrix, (0, 5))
        rows.append(
            {
                "name": name,
                "matrix": [[int(entry) for entry in row] for row in H.tolist()],
                "determinant": int(H.det()),
                "mixed_rank": int(mixed.rank()),
                "same_rank": int(same.rank()),
                "cross_rank": int(matrix.rank()),
            }
        )
    require([row["cross_rank"] for row in rows] == [6, 6, 9, 9], rows)
    return {"examples": rows}


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-119",
        "status": "PURE_QQ_COMMON_COLUMN_MIX_K32_RIGIDITY",
        "field": "characteristic zero",
        "hypothesis": "T=I_3 tensor H with H in GL_2; L=graph(T), M=graph(-T)",
        "symbolic_certificate": symbolic_certificate(),
        "exact_examples": exact_examples(),
        "theorem": {
            "cross_rank_formula": "6 if H is monomial, 9 otherwise",
            "rank_at_most_six": "H is monomial, hence preserves a 2+2 column matching",
        },
        "boundary": [
            "does not classify an arbitrary 6 by 6 invertible graph T",
            "does not close the full K2,3/K3,2 formal germ",
            "does not by itself prove kappa2=0 or ordinary lower 29",
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
    print("certificate=N6-119")
    print("mixed_rank=3")
    print("cross_rank_monomial=6")
    print("cross_rank_nonmonomial=9")
    print("status=PASS")


if __name__ == "__main__":
    main()
