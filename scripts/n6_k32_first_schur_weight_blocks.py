"""Exact first-Schur weight-block profiles at the K3,2 collision."""

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
DEFAULT_JSON = ROOT / "data" / "n6_k32_first_schur_weight_blocks.json"


def graph_cross(T: sp.Matrix) -> sp.Matrix:
    left: list[list[object]] = []
    right: list[list[object]] = []
    for source in range(6):
        row, column = divmod(source, 2)
        left_vector: list[object] = [0] * 12
        right_vector: list[object] = [0] * 12
        left_vector[4 * row + column] = 1
        right_vector[4 * row + column] = 1
        for target in range(6):
            target_row, target_column = divmod(target, 2)
            left_vector[4 * target_row + target_column + 2] = T[target, source]
            right_vector[4 * target_row + target_column + 2] = -T[target, source]
        left.append(left_vector)
        right.append(right_vector)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def exact_first_schur_columns() -> tuple[list[int], list[int], list[sp.Matrix]]:
    zero = sp.zeros(6)
    base = graph_cross(zero)
    _, pivot_columns = base.rref()
    _, pivot_rows = base.T.rref()
    pivot_columns = list(pivot_columns)
    pivot_rows = list(pivot_rows)
    rows_out = [i for i in range(36) if i not in pivot_rows]
    columns_out = [j for j in range(18) if j not in pivot_columns]
    pivot = base.extract(pivot_rows, pivot_columns)
    inverse = pivot.inv()
    columns: list[sp.Matrix] = []
    for target in range(6):
        for source in range(6):
            direction = sp.zeros(6)
            direction[target, source] = 1
            derivative = (
                graph_cross(direction) - graph_cross(-direction)
            ) / 2
            dpp = derivative.extract(pivot_rows, pivot_columns)
            dpq = derivative.extract(pivot_rows, columns_out)
            drp = derivative.extract(rows_out, pivot_columns)
            base_pq = base.extract(pivot_rows, columns_out)
            base_rp = base.extract(rows_out, pivot_columns)
            columns.append(
                derivative.extract(rows_out, columns_out)
                - drp * inverse * base_pq
                - base_rp * inverse * dpq
                + base_rp * inverse * dpp * inverse * base_pq
            )
    return pivot_rows, pivot_columns, columns


def weight_groups() -> dict[tuple[int, ...], list[tuple[int, int]]]:
    """Group first-order columns by their full torus character.

    For a row-preserving direction, the row part of the character is zero
    for every diagonal row, so the three row choices must be kept in one
    block.  Row-changing directions retain the ordered target/source rows.
    The leading tag keeps these two character shapes disjoint.
    """
    groups: dict[tuple[int, ...], list[tuple[int, int]]] = {}
    for target in range(6):
        target_row, target_column = divmod(target, 2)
        for source in range(6):
            source_row, source_column = divmod(source, 2)
            if target_row == source_row:
                key = (0, target_column, source_column)
            else:
                key = (1, target_row, source_row, target_column, source_column)
            groups.setdefault(key, []).append((target, source))
    return groups


def same_row_locus(
    columns: list[sp.Matrix],
    items: list[tuple[int, int]],
) -> dict[str, object]:
    symbols = sp.symbols("a0:3")
    matrix = sp.zeros(columns[0].rows, columns[0].cols)
    for symbol, (target, source) in zip(symbols, items, strict=True):
        matrix += symbol * columns[6 * target + source]
    nonzero_rows = [
        i for i in range(matrix.rows) if any(matrix[i, j] != 0 for j in range(matrix.cols))
    ]
    nonzero_columns = [
        j for j in range(matrix.cols) if any(matrix[i, j] != 0 for i in range(matrix.rows))
    ]
    minors: set[sp.Expr] = set()
    for rows in combinations(nonzero_rows, 4):
        for cols in combinations(nonzero_columns, 4):
            determinant = sp.factor(matrix.extract(rows, cols).det())
            if determinant != 0:
                minors.add(sp.expand(determinant))
    groebner = sp.groebner(sorted(minors, key=str), *symbols, order="grevlex")
    basis = [sp.factor(item.as_expr()) for item in groebner.polys]
    require(matrix.subs({symbol: 1 for symbol in symbols}).rank() == 3, items)
    require(matrix.rank() == 6, items)
    return {
        "items": [list(item) for item in items],
        "generic_rank": 6,
        "equal_coefficient_rank": 3,
        "nonzero_4x4_minor_count": len(minors),
        "groebner_basis": [str(item) for item in basis],
        "rank_at_most_three_locus": "a0=a1=a2",
        "locus_argument": (
            "The basis contains c^3(a-c), c^3(b-c), and with c=0 "
            "also a^4,b^4; hence its zero set is a=b=c."
        ),
    }


def exact_certificate() -> dict[str, object]:
    _, _, columns = exact_first_schur_columns()
    groups = weight_groups()
    singleton_profiles = []
    same_row_profiles = []
    for key, items in sorted(groups.items()):
        if len(items) == 1:
            target, source = items[0]
            singleton_profiles.append(
                {
                    "weight_key": list(key),
                    "target": target,
                    "source": source,
                    "schur_rank": int(columns[6 * target + source].rank()),
                }
            )
        else:
            require(key[0] == 0 and len(items) == 3, (key, items))
            same_row_profiles.append(
                {
                    "weight_key": list(key),
                    "locus": same_row_locus(columns, items),
                }
            )
    require(len(singleton_profiles) == 24, len(singleton_profiles))
    require(all(item["schur_rank"] == 3 for item in singleton_profiles), singleton_profiles)
    require(len(same_row_profiles) == 4, len(same_row_profiles))
    return {
        "base_cross_rank": int(graph_cross(sp.zeros(6)).rank()),
        "first_schur_shape": [33, 15],
        "weight_convention": "(target_row,source_row,target_Q_column,source_P_column)",
        "singleton_count": len(singleton_profiles),
        "singleton_profiles": singleton_profiles,
        "same_row_group_count": len(same_row_profiles),
        "same_row_profiles": same_row_profiles,
        "candidate_rank_three_lines": 28,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-124",
        "status": "EXACT_QQ_FIRST_SCHUR_WEIGHT_BLOCK_PROFILES",
        "field": "characteristic zero",
        "hypothesis": (
            "relative graph direction T at the coordinate K3,2 collision "
            "L=M=A3 tensor P2"
        ),
        "exact_certificate": exact_certificate(),
        "consequence": (
            "The 24 row-changing singleton weight blocks have Schur rank 3. "
            "Each of the four same-row three-variable blocks has generic "
            "rank 6 and rank at most 3 exactly on its equal-coefficient line."
        ),
        "boundary": [
            "does not classify sums of different torus-weight blocks",
            "does not classify the full first tangent cone",
            "does not classify nonlinear lifts or arbitrary 6 by 6 graph T",
            "does not prove ordinary lower 29 or exact Chow rank 32",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
    if args.verify_json:
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            "frozen JSON differs from exact replay",
        )
    print("certificate=N6-124")
    print("singleton_blocks=24")
    print("same_row_blocks=4")
    print("status=PASS")


if __name__ == "__main__":
    main()
