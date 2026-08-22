#!/usr/bin/env python3
"""Forced-gradient reduction of the Packet-A equality locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import sympy as sp


N = 7
ROOT = Path(__file__).resolve().parents[1]


def load_local(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


block = load_local("n7_packet_a_permanent_block_operator")
smoke = load_local("n7_packet_a_labelled_256_operator")


def forced_transport_block(
    terms: tuple[tuple[tuple[int, ...], ...], ...],
    coefficients: tuple[sp.Rational, ...],
    omitted_column: int,
) -> sp.Matrix:
    """Return the derivative coefficients forced by the labelled factors."""

    if len(terms) != len(coefficients):
        raise ValueError("one nonzero external coefficient is required per term")
    rows = len(terms) * N
    transport = sp.zeros(rows, N)
    for term_index, (factors, coefficient) in enumerate(zip(terms, coefficients)):
        if coefficient == 0 or block.general.validate_factors(factors) != N * N:
            raise ValueError("rank-seven terms in the 49-variable ambient are required")
        for factor_index, factor in enumerate(factors):
            subset_index = block.OMITTED_FACTOR_TO_SUBSET_INDEX[factor_index]
            labelled_row = term_index * N + subset_index
            for source_row in range(N):
                transport[labelled_row, source_row] = (
                    coefficient * factor[source_row * N + omitted_column]
                )
    return transport


def forced_gradient_residual_block(
    terms: tuple[tuple[tuple[int, ...], ...], ...],
    coefficients: tuple[sp.Rational, ...],
    omitted_column: int,
) -> sp.Matrix:
    aggregate = sp.Matrix.hstack(
        *[
            sp.Matrix(block.projected_term_block(term, omitted_column).tolist())
            for term in terms
        ]
    )
    transport = forced_transport_block(terms, coefficients, omitted_column)
    target = sp.Matrix(block.permanent_target_block(omitted_column).tolist())[
        :, omitted_column * N : (omitted_column + 1) * N
    ]
    return aggregate * transport - target


def glynn_forced_residual(count: int) -> dict[str, object]:
    points = smoke.normalized_signs(count)
    powers = sp.Matrix(block.power6_columns(points).tolist())
    coefficients = sp.diag(
        *[sp.Rational(math.prod(point), 64) for point in points]
    )
    point_matrix = sp.Matrix(points)
    target = sp.zeros(len(block.EXPONENTS6), N)
    for missing_row in range(N):
        alpha = tuple(0 if row == missing_row else 1 for row in range(N))
        target[block.EXPONENT_INDEX6[alpha], missing_row] = block.TARGET_SCALE
    residual = powers * coefficients * point_matrix - target
    rank = residual.rank()
    nonzero_entries = sum(value != 0 for value in residual)
    per_column_ranks = [residual[:, column].rank() for column in range(N)]
    return {
        "term_count": count,
        "coefficient_field": "QQ exact",
        "one_omitted_column_residual_shape": list(residual.shape),
        "one_omitted_column_residual_rank": rank,
        "one_omitted_column_nonzero_entry_count": nonzero_entries,
        "one_omitted_column_residual_column_ranks": per_column_ranks,
        "seven_disjoint_column_blocks_total_residual_rank": N * rank,
        "forced_gradient_equations_hold": rank == 0,
        "decision": (
            "FORCED_GRADIENT_EXCLUDED"
            if rank
            else "EXACT_FORCED_GRADIENT_SURVIVOR"
        ),
    }


def incidence_schema() -> dict[str, object]:
    term_count = 49
    factor_variables = term_count * N * (N * N)
    coefficient_variables = term_count
    labelled_columns = term_count * N
    sym2_rows = math.comb(49 + 2 - 1, 2)
    sym5_rows = math.comb(49 + 5 - 1, 5)
    return {
        "factor_coordinate_variables_before_quotients": factor_variables,
        "external_coefficient_variables": coefficient_variables,
        "total_affine_variables_before_open_conditions_and_symmetries": (
            factor_variables + coefficient_variables
        ),
        "simple_multilinear_matroid_condition": (
            "an open collection of nonvanishing Plucker/rank minors; it supplies no fixed torus-weight equation"
        ),
        "forced_gradient_component": {
            "name": "Z_A_grad",
            "equations": "A6_b(F) R_b(F,c) = T_b for b=0,...,6",
            "omitted_column_blocks": N,
            "rows_per_block": len(block.EXPONENTS6),
            "target_columns_per_block": N,
            "displayed_scalar_equation_count_before_dependencies": (
                N * len(block.EXPONENTS6) * N
            ),
            "labelled_degree_6_middle_columns": labelled_columns,
            "coefficient_transport": (
                "R_b[(i,omit r),(s,b)] = c_i times coefficient of x_(s,b) in ell_(i,r)"
            ),
        },
        "aggregate_relation_capacity": {
            "A2_shape": [sym2_rows, term_count * math.comb(N, 2)],
            "A5_shape": [sym5_rows, term_count * math.comb(N, 5)],
            "both_maps_can_be_injective_by_dimension": True,
            "consequence": (
                "simple-matroid ranks plus dimensions do not force K2 or K5 nonzero; on K2=K5=0 the complementary pairing is vacuous"
            ),
        },
        "smallest_missing_invariant": (
            "a permanent-specific syzygy proving that Z_A_grad intersect the simple-matroid open set forces a nonzero 2/5 relation incompatible with inverse-coefficient pairing, or is empty"
        ),
    }


def build_payload() -> dict[str, object]:
    schema = incidence_schema()
    glynn49 = glynn_forced_residual(49)
    glynn64 = glynn_forced_residual(64)
    if glynn49["one_omitted_column_residual_rank"] != 5:
        raise AssertionError(glynn49)
    if not glynn64["forced_gradient_equations_hold"]:
        raise AssertionError(glynn64)
    return {
        "schema_version": 1,
        "status": "PACKET_A_EQUALITY_LOCUS_REDUCED_TO_FORCED_GRADIENT_COMPONENT",
        "universal_block_defect_decision": "NOT_DERIVED_FROM_CURRENT_HYPOTHESES",
        "exact_incidence_schema": schema,
        "mandatory_existing_controls": {
            "glynn49_truncation": glynn49,
            "glynn64_identity_control": glynn64,
            "non_tensor_control_role": (
                "Sylvester kernel-image equality alone cannot replace the forced-gradient equations or imply tensor split"
            ),
        },
        "structural_conclusion": [
            "Target containment must be strengthened to the forced coefficient transport A6_b(F) R_b(F,c)=T_b.",
            "The same factors and external coefficients occur in all seven blocks; arbitrary target-span coefficients are not allowed.",
            "The simple multilinear matroid condition is open and GL(49)-invariant, whereas an omitted-column block is tied to the permanent torus; the former alone gives no universal fixed-block defect.",
            "The 2/5 pairing does not give a universal defect without a theorem forcing nonzero K2 or K5 on Z_A_grad.",
        ],
        "claim_boundary": [
            "This is an exact reduction of the remaining Packet-A component, not a classification of that component.",
            "The Glynn49 truncation is excluded by forced-gradient residual rank 5 per omitted-column block, total 35 across the seven disjoint blocks.",
            "The 64-term Glynn identity is an exact forced-gradient survivor and prevents treating the equations themselves as contradictory.",
            "No exact 49-term survivor is produced, and no universal nonzero block defect is proved.",
            "A-CLOSED, ordinary lower 50, and border rank remain unresolved until the displayed missing syzygy or an equivalent component classification is proved.",
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
            raise SystemExit("Packet A equality-locus gradient JSON mismatch")
        print("PASS n7 Packet A equality-locus gradient reduction")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
