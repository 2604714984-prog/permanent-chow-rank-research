"""Exact unit graph directions at the K3,2 collision point.

This is a deliberately small restricted calculation.  It classifies the
36 straight graph arcs T=t E_{target,source}; it does not attempt to classify
nonlinear lifts of a general tangent direction.
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
DEFAULT_JSON = ROOT / "data" / "n6_k32_unit_graph_direction.json"
ROW_EDGES = tuple(combinations(range(3), 2))
COLUMN_EDGES = tuple(combinations(range(4), 2))


def graph_pair(target: int, source: int, parameter: object) -> tuple[
    list[list[object]], list[list[object]]
]:
    left: list[list[object]] = []
    right: list[list[object]] = []
    for index in range(6):
        row, column = divmod(index, 2)
        left_vector: list[object] = [0] * 12
        right_vector: list[object] = [0] * 12
        left_vector[4 * row + column] = 1
        right_vector[4 * row + column] = 1
        if index == source:
            target_row, target_column = divmod(target, 2)
            left_vector[4 * target_row + target_column + 2] = parameter
            right_vector[4 * target_row + target_column + 2] = -parameter
        left.append(left_vector)
        right.append(right_vector)
    return left, right


def cross_matrix(target: int, source: int, parameter: object) -> sp.Matrix:
    left, right = graph_pair(target, source, parameter)
    return sp.Matrix([beta(x, y) for x in left for y in right])


def sum_rank(target: int, source: int) -> int:
    left, right = graph_pair(target, source, sp.Integer(1))
    return int(sp.Matrix.hstack(*map(sp.Matrix, left + right)).rank())


def exact_certificate() -> dict[str, object]:
    parameter = sp.symbols("t")
    representative_labels = {
        "same_row_same_column": (0, 0),
        "same_row_different_column": (1, 0),
        "different_row_same_column": (2, 0),
        "different_row_different_column": (3, 0),
    }
    representative_ranks: dict[str, int] = {}
    symbolic_ranks: dict[str, int] = {}
    representative_sum_ranks: dict[str, int] = {}
    for label, (target, source) in representative_labels.items():
        matrix = cross_matrix(target, source, parameter)
        symbolic_ranks[label] = int(matrix.rank())
        representative_ranks[label] = int(matrix.subs(parameter, 1).rank())
        representative_sum_ranks[label] = sum_rank(target, source)
    require(set(symbolic_ranks.values()) == {6, 7}, symbolic_ranks)
    require(set(representative_ranks.values()) == {6, 7}, representative_ranks)
    require(set(representative_sum_ranks.values()) == {7}, representative_sum_ranks)

    records: list[dict[str, object]] = []
    for target in range(6):
        target_row, target_column = divmod(target, 2)
        for source in range(6):
            source_row, source_column = divmod(source, 2)
            matrix = cross_matrix(target, source, sp.Integer(1))
            records.append(
                {
                    "target": target,
                    "source": source,
                    "same_row": target_row == source_row,
                    "same_column": target_column == source_column,
                    "cross_rank": int(matrix.rank()),
                    "sum_rank": sum_rank(target, source),
                }
            )
    rank_profile: dict[str, int] = {}
    for record in records:
        key = f"{record['same_row']},{record['same_column']}"
        rank_profile[key] = rank_profile.get(key, 0) + 1
    require(
        rank_profile == {"True,True": 6, "True,False": 6, "False,True": 12, "False,False": 12},
        rank_profile,
    )
    require(
        all(
            record["cross_rank"]
            == (7 if record["same_row"] else 6)
            for record in records
        ),
        records,
    )
    require(all(record["sum_rank"] == 7 for record in records), records)
    return {
        "parameter": "t",
        "nonzero_parameter_rank_is_constant": True,
        "representative_labels": {
            label: {"target": target, "source": source}
            for label, (target, source) in representative_labels.items()
        },
        "symbolic_ranks_over_Q_t": symbolic_ranks,
        "ranks_at_t_1": representative_ranks,
        "sum_ranks_at_t_1": representative_sum_ranks,
        "all_36_records_at_t_1": records,
        "orbit_profile": rank_profile,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-122",
        "status": "EXACT_QQ_RESTRICTED_K32_UNIT_GRAPH_DIRECTION_CLASSIFICATION",
        "field": "characteristic zero",
        "hypothesis": (
            "K3,2 collision W=A3 tensor P2; L=graph(t E_target,source), "
            "M=graph(-t E_target,source), t nonzero"
        ),
        "exact_certificate": exact_certificate(),
        "theorem": {
            "same_row_cross_rank": 7,
            "different_row_cross_rank": 6,
            "sum_rank_for_every_unit_direction": 7,
            "nonzero_parameter_normalized_by_row_column_torus": True,
            "consequence": (
                "Every unit straight arc with cross rank at most six is "
                "noncomplementary because rank(T)=1 and dim(L+M)=7."
            ),
        },
        "boundary": [
            "does not classify nonlinear corrections to unit directions",
            "does not classify arbitrary 6 by 6 graph operators",
            "does not close the full K2,3/K3,2 formal germ",
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
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            "frozen JSON differs from exact replay",
        )
    print("certificate=N6-122")
    print("unit_directions=36")
    print("same_row_rank=7")
    print("different_row_rank=6")
    print("status=PASS")


if __name__ == "__main__":
    main()
