"""Exact straight-arc exclusion for a row-changing four-clique.

The four first-Schur rays in one ordered row pair form a 2 by 2 column
coefficient block.  This certificate classifies the resulting straight graph
pair over characteristic zero; it does not classify nonlinear lifts.
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
DEFAULT_JSON = ROOT / "data" / "n6_k32_row_changing_four_clique_straight_exclusion.json"


def graph_pair_block(
    target_row: int, source_row: int, block: list[list[object]]
) -> tuple[list[list[object]], list[list[object]]]:
    left: list[list[object]] = []
    right: list[list[object]] = []
    for index in range(6):
        row, column = divmod(index, 2)
        left_vector: list[object] = [0] * 12
        right_vector: list[object] = [0] * 12
        left_vector[4 * row + column] = 1
        right_vector[4 * row + column] = 1
        if row == source_row:
            for target_column in range(2):
                left_vector[4 * target_row + target_column + 2] += block[
                    target_column
                ][column]
                right_vector[4 * target_row + target_column + 2] -= block[
                    target_column
                ][column]
        left.append(left_vector)
        right.append(right_vector)
    return left, right


def cross_matrix(block: list[list[object]]) -> sp.Matrix:
    left, right = graph_pair_block(0, 1, block)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def exact_rank(block: list[list[object]]) -> int:
    return int(cross_matrix(block).rank())


def minor_certificate(
    block: list[list[object]], rows: list[int], columns: list[int]
) -> str:
    return str(sp.factor(cross_matrix(block).extract(rows, columns).det()))


def build_payload() -> dict[str, object]:
    a, b, c, d = sp.symbols("a b c d")
    generic = [[a, b], [c, d]]
    generic_matrix = cross_matrix(generic)
    require(generic_matrix.rank() == 8, generic_matrix.rank())

    generic_rows = [3, 5, 15, 16, 17, 22, 23, 27]
    generic_columns = [0, 1, 6, 7, 8, 9, 10, 12]
    generic_minor = minor_certificate(generic, generic_rows, generic_columns)
    require(generic_minor == "-2*b*(a*d - b*c)**2", generic_minor)

    b_zero = [[a, 0], [c, d]]
    b_zero_rows = generic_rows
    b_zero_columns = [0, 2, 6, 7, 8, 9, 10, 12]
    b_zero_minor = minor_certificate(b_zero, b_zero_rows, b_zero_columns)
    require(b_zero_minor == "-2*a**2*d**3", b_zero_minor)
    require(cross_matrix(b_zero).rank() == 8, b_zero)

    determinant_zero_charts = {
        "a_nonzero": [[a, b], [c, b * c / a]],
        "a_zero_b_zero": [[0, 0], [c, d]],
        "a_zero_c_zero": [[0, b], [0, d]],
    }
    zero_ranks: dict[str, int] = {}
    for name, block in determinant_zero_charts.items():
        rank = exact_rank(block)
        zero_ranks[name] = rank
        require(rank <= 6, (name, rank))

    return {
        "certificate": "N6-136",
        "status": "EXACT_QQ_ROW_CHANGING_FOUR_CLIQUE_STRAIGHT_EXCLUSION",
        "field": "characteristic zero",
        "hypothesis": (
            "K3,2 collision W=A3 tensor P2; D is supported in one ordered "
            "source/target row pair with a 2 by 2 column block C; "
            "L=graph(D), M=graph(-D)"
        ),
        "cross_matrix_shape": [36, 18],
        "determinant_polynomial": "a*d-b*c",
        "generic_rank": 8,
        "generic_minor": {
            "rows": generic_rows,
            "columns": generic_columns,
            "factor": generic_minor,
        },
        "b_zero_rank_eight_minor": {
            "rows": b_zero_rows,
            "columns": b_zero_columns,
            "factor": b_zero_minor,
        },
        "determinant_zero_chart_ranks": zero_ranks,
        "theorem": {
            "det_nonzero_cross_rank": 8,
            "det_zero_cross_rank_at_most": 6,
            "det_zero_D_rank_at_most": 1,
            "det_zero_sum_rank_at_most": 7,
            "row_pair_symmetry_count": 12,
        },
        "consequence": (
            "Every straight graph pair supported on a row-changing four-clique "
            "which satisfies cross rank at most six is noncomplementary: "
            "det(C)=0 forces rank(D)<=1 and hence dim(L+M)<=7."
        ),
        "boundary": [
            "does not classify nonlinear corrections to the four-clique",
            "does not classify non-graph charts or coupled six-term cocycles",
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
    print("certificate=N6-136")
    print("generic_cross_rank=8")
    print("det_zero_cross_rank<=6")
    print("det_zero_sum_rank<=7")
    print("status=PASS")


if __name__ == "__main__":
    main()
