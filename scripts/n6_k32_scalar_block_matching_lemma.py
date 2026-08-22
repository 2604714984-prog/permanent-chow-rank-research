"""Exact certificate for a restricted scalar-block K3,2 graph lemma.

This is deliberately narrower than the Chow-rank problem.  Each of the three
row blocks is a scalar multiple of the 2-by-2 identity on the two matching
columns.  The cross beta map then splits into three independent 8-by-6
row-edge blocks.  The pure lemma in the accompanying document classifies the
rank-six case under the complementary-graph condition ``x_i-y_i != 0``.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_k32_average_relative_germ import graph_pair
    from scripts.n6_product_32_rank_six_frame_barrier import beta, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_k32_average_relative_germ import graph_pair
    from n6_product_32_rank_six_frame_barrier import beta, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_scalar_block_matching_lemma.json"
ROW_EDGES = tuple(combinations(range(3), 2))


def pair_formula(x_i: int, x_j: int, y_i: int, y_j: int) -> list[list[int]]:
    """Return the 8-by-6 row-edge matrix in variable order s,B00,B01,B10,B11,t."""

    rows: list[list[int]] = []
    for x, y, product_xy in (
        (x_i, y_j, x_i * y_j),
        (x_j, y_i, x_j * y_i),
    ):
        # vec(sJ + yB + x B^T + product_xy*tJ), row-major.
        rows.extend(
            (
                [0, x + y, 0, 0, 0, 0],
                [1, 0, y, x, 0, product_xy],
                [1, 0, x, y, 0, product_xy],
                [0, 0, 0, 0, x + y, 0],
            )
        )
    return rows


def aggregate_formula(xs: tuple[int, int, int], ys: tuple[int, int, int]) -> list[list[int]]:
    """Block-diagonal concatenation of the three row-edge maps."""

    rows: list[list[int]] = []
    for block, (i, j) in enumerate(ROW_EDGES):
        local = pair_formula(xs[i], xs[j], ys[i], ys[j])
        rows.extend(
            [[0] * (6 * block) + row + [0] * (6 * (2 - block)) for row in local]
        )
    return rows


def exact_rank(matrix: list[list[int]]) -> int:
    return int(sp.Matrix(matrix).rank())


def direct_cross_matrix(xs: tuple[int, int, int], ys: tuple[int, int, int]) -> sp.Matrix:
    diagonal_x = sp.diag(*[value for value in xs for _ in range(2)])
    diagonal_y = sp.diag(*[value for value in ys for _ in range(2)])
    left, right = graph_pair(diagonal_x, diagonal_y)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def matching_condition(xs: tuple[int, int, int], ys: tuple[int, int, int]) -> bool:
    return xs[0] == xs[1] == xs[2] and ys == tuple(-value for value in xs)


def build_payload() -> dict[str, object]:
    samples = [
        ((1, 1, 1), (-1, -1, -1)),
        ((1, 2, 3), (-1, -2, -3)),
        ((1, 1, 2), (-1, -1, -2)),
        ((1, 2, 3), (4, 5, 6)),
    ]
    sample_rows = []
    for xs, ys in samples:
        require(all(x != y for x, y in zip(xs, ys, strict=True)), (xs, ys))
        formula_rank = exact_rank(aggregate_formula(xs, ys))
        direct_rank = int(direct_cross_matrix(xs, ys).rank())
        require(formula_rank == direct_rank, (xs, ys, formula_rank, direct_rank))
        sample_rows.append(
            {"x": list(xs), "y": list(ys), "formula_rank": formula_rank, "direct_beta_rank": direct_rank}
        )

    special = (1, 1, 1), (-1, -1, -1)
    special_rank = exact_rank(aggregate_formula(*special))
    require(special_rank == 6, special_rank)

    # A small exhaustive exact check over {-1,0,1}; this is only 729 states.
    checked = 0
    theorem_failures: list[dict[str, object]] = []
    for values in product((-1, 0, 1), repeat=6):
        xs = values[:3]
        ys = values[3:]
        if any(x == y for x, y in zip(xs, ys, strict=True)):
            continue
        checked += 1
        rank = exact_rank(aggregate_formula(xs, ys))
        if (rank <= 6) != matching_condition(xs, ys):
            theorem_failures.append({"x": list(xs), "y": list(ys), "rank": rank})
    require(not theorem_failures, theorem_failures[:1])

    return {
        "status": "PURE_SCALAR_BLOCK_MATCHING_LEMMA",
        "field": "QQ",
        "row_count": 3,
        "block_size": 2,
        "pair_matrix_shape": [8, 6],
        "aggregate_matrix_shape": [24, 18],
        "relative_graph_condition": "x_i-y_i != 0 for i=0,1,2",
        "small_exhaustive_states": checked,
        "small_exhaustive_failures": len(theorem_failures),
        "samples": sample_rows,
        "special_rank_six": {"x": [1, 1, 1], "y": [-1, -1, -1], "rank": special_rank},
        "conclusion": "aggregate rank <= 6 iff x_0=x_1=x_2=lambda and y_i=-lambda, lambda!=0",
        "boundary": [
            "only scalar 2-by-2 row blocks",
            "only graph charts with x_i-y_i nonzero",
            "does not classify general 6-by-6 average/relative operators",
            "does not prove ChowRank(perm_6) or the unrestricted 2^(n-1) conjecture",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen payload mismatch")
        print(json.dumps(payload, sort_keys=True))
        return
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
