#!/usr/bin/env python3
"""Structure theorem for the W=0 branch of Packet A."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path


N = 7
TERM_COUNT = 49
ROOT = Path(__file__).resolve().parents[1]


def load_local(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


relation = load_local("n7_packet_a_hessian_relation_kernel")
COLUMN_PAIRS = relation.COLUMN_PAIRS


def support(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, value in enumerate(vector) if value != 0)


def classify_wzero_row_slices(
    slices: tuple[tuple[int, ...], ...]
) -> dict[str, object]:
    """Classify seven pairwise off-diagonally sym-orthogonal row slices."""

    if len(slices) != N or any(len(vector) != N for vector in slices):
        raise ValueError("seven row slices in seven columns are required")
    for first, second in itertools.combinations(range(N), 2):
        if any(relation.off_diagonal_symmetrized_pair(slices[first], slices[second])):
            raise ValueError("the row slices do not lie on W=0")
    active = tuple(index for index, vector in enumerate(slices) if any(vector))
    if len(active) <= 1:
        return {
            "type": "at_most_one_nonzero_slice",
            "active_factor_indices": list(active),
        }
    first_support = support(slices[active[0]])
    if len(first_support) == 1:
        common = first_support[0]
        if any(support(slices[index]) != (common,) for index in active):
            raise AssertionError("invalid common-column W=0 family")
        return {
            "type": "common_single_column",
            "active_factor_indices": list(active),
            "column_support": [common],
        }
    if len(first_support) != 2 or len(active) != 2:
        raise AssertionError("unclassified W=0 row family")
    if support(slices[active[1]]) != first_support:
        raise AssertionError("the exceptional pair must share its two columns")
    return {
        "type": "exceptional_two_slice_two_column",
        "active_factor_indices": list(active),
        "column_support": list(first_support),
    }


def same_column_witness_coordinates(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    if len(left) != N or len(right) != N:
        raise ValueError("two seven-column row slices are required")
    return tuple(2 * left[column] * right[column] for column in range(N))


def all_same_row_hessian_witnesses_zero(
    factors: tuple[tuple[int, ...], ...]
) -> bool:
    """Check both distinct-column W and the seven same-column witnesses."""

    if relation.general.validate_factors(factors) != N * N:
        raise ValueError("seven factors in the 49-variable ambient are required")
    if any(relation.hard_residual_equations_for_term(factors)):
        return False
    for row in range(N):
        slices = tuple(relation.row_slice(factor, row) for factor in factors)
        for first, second in itertools.combinations(range(N), 2):
            if any(same_column_witness_coordinates(slices[first], slices[second])):
                return False
    return True


def row_separation_permutation(
    factors: tuple[tuple[int, ...], ...]
) -> tuple[int, ...] | None:
    """Return factor->row assignment when each factor occupies one distinct row."""

    if relation.general.validate_factors(factors) != N * N:
        raise ValueError("seven factors in the 49-variable ambient are required")
    factor_rows = []
    for factor in factors:
        rows = tuple(row for row in range(N) if any(relation.row_slice(factor, row)))
        if len(rows) != 1:
            return None
        factor_rows.append(rows[0])
    if len(set(factor_rows)) != N:
        return None
    return tuple(factor_rows)


def flattening_rank_bound(group_size: int) -> int:
    if not 0 <= group_size <= N:
        raise ValueError("the row group size must lie between zero and seven")
    return math.comb(N, group_size)


def build_payload() -> dict[str, object]:
    distinct_witness_columns = math.comb(N, 2) * N
    same_column_witness_columns = N * N
    flattening_ranks = [flattening_rank_bound(size) for size in range(N + 1)]
    return {
        "schema_version": 1,
        "status": "PACKET_A_WZERO_CLASSIFIED_TO_ROW_SEPARATED_TENSOR_LOCUS",
        "wzero_row_slice_classification": {
            "statement": (
                "at a fixed term and row, a W=0 family is exactly one of: at most one nonzero slice; "
                "arbitrarily many slices on one common column; or two slices on the same two columns "
                "with sign-flipped proportional coefficients"
            ),
            "support_at_least_three_consequence": "every other factor slice at that row is zero",
            "support_two_consequence": (
                "at most one other slice is nonzero; it has the same two-column support and is sign-flipped proportional"
            ),
            "support_one_consequence": "all nonzero slices use that same single column",
            "characteristic": "zero (the exceptional-family exclusion uses 2 nonzero)",
        },
        "same_column_completion": {
            "formula": "W_(b,b)[(i,omit {r,s}),u] = 2 c_i a_(i,r,u,b) a_(i,s,u,b)",
            "additional_witness_columns": same_column_witness_columns,
            "all_same_row_witness_columns": distinct_witness_columns + same_column_witness_columns,
            "consequence_on_W0": (
                "if two factor slices are nonzero at one row, then some same-column witness is nonzero, "
                "hence the aggregate global K5 is nonzero"
            ),
        },
        "exact_remaining_component": {
            "name": "Z_A_row_separated_49",
            "definition": (
                "Z_A_grad_hess_W0 intersect {all same-column Hessian witnesses vanish}"
            ),
            "structure_theorem": (
                "each of the 49 terms has, after permuting its seven factors, exactly one nonzero linear factor in each matrix row"
            ),
            "pigeonhole_reason": (
                "each row supports at most one factor, while seven nonzero factors must occupy the seven available rows"
            ),
            "equality_problem_on_this_component": (
                "any true identity here is a 49-term simple-tensor decomposition of the 7 by 7 permanent tensor"
            ),
            "off_row_hessian_role": (
                "the nonzero off-row targets become the mixed flattening equations of that simple-tensor decomposition"
            ),
        },
        "flattening_boundary": {
            "row_bipartition_ranks_for_group_sizes_0_to_7": flattening_ranks,
            "maximum_rank": max(flattening_ranks),
            "consequence": (
                "ordinary row-bipartition flattenings give only the lower bound 35 and therefore do not exclude 49 terms"
            ),
        },
        "resource_bound": {
            "classification_state_per_row": N * N,
            "full_A5_materialized": False,
            "subset_enumeration": False,
            "conservative_peak_memory_mib": 16,
        },
        "smallest_remaining_invariant": (
            "either force a nontrivially paired K2 vector on the nonzero-Hessian-witness branch, "
            "or prove tensor rank(permanent_7) at least 50 on Z_A_row_separated_49 using a stronger-than-flattening invariant"
        ),
        "claim_boundary": [
            "The W=0 support classification is exact and includes the two-column sign-flip exception.",
            "The same-column completion forces nonzero aggregate K5 unless every term is row-separated.",
            "The row-separated branch is not excluded: no 49-term decomposition is constructed, and no tensor-rank lower bound 50 is proved.",
            "Simple-matroid openness and ordinary flattenings do not close either remaining branch.",
            "A-CLOSED, ordinary lower 50, and border rank remain unresolved.",
        ],
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
            raise SystemExit("Packet A W-zero JSON mismatch")
        print("PASS n7 Packet A W-zero structure")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
