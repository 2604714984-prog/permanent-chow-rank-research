#!/usr/bin/env python3
"""Exact gap-aligned rank-one fifth-term chart for the B2 joins."""

from __future__ import annotations

import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
GAP_PATH = HERE / "n7_b2_join_completion_gap.py"
SPEC = importlib.util.spec_from_file_location("n7_b2_join_completion_gap", GAP_PATH)
gap = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(gap)


CHARTS = {
    "shared_row_01_02": {
        "factor_orbit_representatives": (0, 1, 3),
        "w_directions": {
            "single_u01": (1, 0, 0, 0),
            "reciprocal_pair_01": (1, 1, 0, 0),
            "all_four_join_directions": (1, 1, 1, 1),
        },
        "required_defect": 10,
    },
    "disjoint_01_23": {
        "factor_orbit_representatives": (0, 2, 4),
        "w_directions": {
            "single_u01": (1, 0, 0, 0),
            "reciprocal_pair_23": (0, 0, 1, 1),
            "all_four_join_directions": (1, 1, 1, 1),
        },
        "required_defect": 12,
    },
}


def rank_one_term(
    w_direction: tuple[int, int, int, int], factor_index: int
) -> list[tuple[sp.Integer, ...]]:
    """The one-factor-support chart q_i -> q_i+w, other factors fixed."""

    if factor_index not in range(7) or not any(w_direction):
        raise ValueError("the rank-one chart needs one factor and nonzero w")
    basis = [
        tuple(sp.Integer(row == column) for column in range(11))
        for row in range(11)
    ]
    factors = []
    for column in range(7):
        vector = list(basis[column])
        if column == factor_index:
            for row, coefficient in enumerate(w_direction):
                vector[7 + row] = coefficient
        factors.append(tuple(vector))
    return factors


def operator_control(
    join_name: str,
    factor_index: int,
    w_name: str,
    w_direction: tuple[int, int, int, int],
) -> dict[str, object]:
    pairs = gap.join.JOIN_TYPES[join_name]
    sympy_b, sympy_c, old_b, old_c = gap.base_complex(pairs)
    extra_b, extra_c = gap.join.formal_maps(rank_one_term(w_direction, factor_index))
    new_b = gap.join.flint_matrix(sp.Matrix.hstack(sympy_b, extra_b))
    new_c = gap.join.flint_matrix(sp.Matrix.vstack(sympy_c, extra_c))
    old_ranks = (old_b.rank(), old_c.rank(), (old_b * old_c).rank())
    new_ranks = (new_b.rank(), new_c.rank(), (new_b * new_c).rank())
    increments = tuple(new - old for new, old in zip(new_ranks, old_ranks))
    old_defect = CHARTS[join_name]["required_defect"]
    new_defect = new_b.ncols() - new_ranks[0] - new_ranks[1] + new_ranks[2]
    repair_score = increments[0] + increments[1] - increments[2]
    required_score = 35 + old_defect
    return {
        "join_type": join_name,
        "factor_index": factor_index,
        "w_direction_name": w_name,
        "w_direction": list(w_direction),
        "rank_increments_B_C_BC": list(increments),
        "delta_C_minus_delta_BC": increments[1] - increments[2],
        "repair_score_delta_B_plus_delta_C_minus_delta_BC": repair_score,
        "required_repair_score": required_score,
        "new_defect": new_defect,
        "operator_gap_repaired": repair_score == required_score and new_defect == 0,
    }


@lru_cache(maxsize=1)
def build_payload() -> dict[str, object]:
    rows = []
    for join_name, chart in CHARTS.items():
        for factor_index in chart["factor_orbit_representatives"]:
            for w_name, w_direction in chart["w_directions"].items():
                rows.append(
                    operator_control(
                        join_name, factor_index, w_name, w_direction
                    )
                )
    if any(row["operator_gap_repaired"] for row in rows):
        raise AssertionError("the minimal rank-one chart unexpectedly repaired a gap")
    extrema = {}
    for join_name in CHARTS:
        selected = [row for row in rows if row["join_type"] == join_name]
        extrema[join_name] = {
            "maximum_delta_C_minus_delta_BC": max(
                row["delta_C_minus_delta_BC"] for row in selected
            ),
            "maximum_repair_score": max(
                row["repair_score_delta_B_plus_delta_C_minus_delta_BC"]
                for row in selected
            ),
            "required_repair_score": selected[0]["required_repair_score"],
            "minimum_new_defect": min(row["new_defect"] for row in selected),
        }
    if extrema != {
        "shared_row_01_02": {
            "maximum_delta_C_minus_delta_BC": 9,
            "maximum_repair_score": 25,
            "required_repair_score": 45,
            "minimum_new_defect": 20,
        },
        "disjoint_01_23": {
            "maximum_delta_C_minus_delta_BC": 12,
            "maximum_repair_score": 31,
            "required_repair_score": 47,
            "minimum_new_defect": 16,
        },
    }:
        raise AssertionError(("unexpected rank-one chart extrema", extrema))
    return {
        "schema_version": 1,
        "status": "GAP_ALIGNED_ONE_FACTOR_RANK_ONE_CHART_EMPTY",
        "chart_definition": "The fifth graph term has factors q_j for j!=i and q_i+w for one selected i. The selected i and w directions are the join-incidence representatives listed in CHARTS.",
        "rows": rows,
        "extrema": extrema,
        "polynomial_joint_deformation_obstruction": {
            "canonical_four_term_U1_layer": "identically zero for every identity-weight and graph-rescaling parameter in the canonical two-slice family",
            "rank_one_fifth_term_U1_layer": "w * sum_i v_i * product_(j!=i) q_j",
            "independence": "The seven squarefree degree-six quotient monomials product_(j!=i) q_j are linearly independent, so this layer vanishes only when v=0 or the fifth coefficient is zero.",
            "conclusion": "No nonzero rank-one fifth graph term can be joined while the first four terms remain in the canonical two-slice deformation family.",
        },
        "candidate_cardinality_checked_before_materialization": {
            "join_types": 2,
            "factor_incidence_representatives_per_join": 3,
            "gap_aligned_w_directions_per_join": 3,
            "exact_operator_controls": len(rows),
            "maximum_middle_dimension": 175,
            "full_degree_seven_monomials_skipped": 202927725,
        },
        "conservative_peak_memory_mib": 128,
        "decision": "MINIMAL_GAP_ALIGNED_RANK_ONE_CHART_EMPTY",
        "claim_boundary": [
            "The rank rows are exact rational computations in the common unprojected 11-variable joins.",
            "The disjoint all-four direction reaches delta_C-delta_BC=12 but still fails because delta_B drops to 19 and the total repair score is only 31 instead of 47.",
            "The polynomial obstruction proves emptiness only when the first four terms remain in the canonical two-slice deformation family.",
            "Multi-factor v support, rank-one directions outside the displayed incidence chart, and noncanonical joint deformations of the first four terms remain open.",
            "No full Packet-B, lower-50, or border-rank conclusion is made.",
        ],
        "next_exact_gate": "Allow two-factor v support and the smallest noncanonical U1 deformation of one original slice pair, then solve cancellation of the seven U1 monomials before recomputing the repair score.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 B2 gap-aligned rank-one JSON mismatch")
        print("PASS n7 B2 gap-aligned rank-one chart")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
