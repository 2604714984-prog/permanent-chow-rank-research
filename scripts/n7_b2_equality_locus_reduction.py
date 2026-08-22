#!/usr/bin/env python3
"""Bounded exact reduction of the Packet-B equality locus by U-degree."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / "n7_b2_intrinsic_mixed_complex.py"
SPEC = importlib.util.spec_from_file_location("n7_b2_intrinsic_mixed_complex", CORE_PATH)
core = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(core)


def derangement(number: int) -> int:
    if number == 0:
        return 1
    if number == 1:
        return 0
    previous_two, previous_one = 1, 0
    for size in range(2, number + 1):
        current = (size - 1) * (previous_one + previous_two)
        previous_two, previous_one = previous_one, current
    return previous_one


def permanent_u_degree_profile() -> list[dict[str, int]]:
    rows = []
    for u_degree in range(8):
        rows.append(
            {
                "u_degree": u_degree,
                "q_degree": 7 - u_degree,
                "target_monomials": math.comb(7, u_degree) * derangement(u_degree),
            }
        )
    if sum(row["target_monomials"] for row in rows) != math.factorial(7):
        raise AssertionError("permanent U-degree profile failed to sum to 7!")
    return rows


def scaled_shear_factors(parameter: int, weight: sp.Rational) -> list[tuple[sp.Rational, ...]]:
    factors = [
        tuple(sp.Integer(i == j) for j in range(7)) for i in range(7)
    ]
    factors[0] = tuple(
        weight * (sp.Integer(j == 0) + parameter * sp.Integer(j == 1))
        for j in range(7)
    )
    return factors


def degree_seven_column(factors: list[tuple[sp.Rational, ...]]) -> sp.Matrix:
    basis = core.exponent_basis(7, 7)
    polynomial = core.multiply_linear_forms(factors, tuple(range(7)))
    return core.coefficient_column(polynomial, basis)


def shear_pencil_control(parameters: list[int], weights: list[sp.Rational]) -> dict[str, object]:
    if len(parameters) != len(weights) or len(parameters) < 2:
        raise ValueError("a shear control needs at least two matched parameters and weights")
    if sum(weights) != 1 or sum(a * w for a, w in zip(parameters, weights)) != 0:
        raise ValueError("weights must reproduce M and cancel the shear monomial")
    factors = [scaled_shear_factors(a, w) for a, w in zip(parameters, weights)]
    target_factors = core.rank_seven_factors()
    polynomial_sum = sum(
        (degree_seven_column(term) for term in factors),
        sp.zeros(math.comb(13, 7), 1),
    )
    target_polynomial = degree_seven_column(target_factors)
    if polynomial_sum != target_polynomial:
        raise AssertionError("quotient polynomial identity failed")

    local = [core.intrinsic_rank_factorization(term) for term in factors]
    global_b = sp.Matrix.hstack(*(row[0] for row in local))
    global_c = sp.Matrix.vstack(*(row[1] for row in local))
    composite = global_b * global_c
    target_b, target_c, target_composite = core.intrinsic_rank_factorization(
        target_factors
    )
    if composite != target_composite or target_b * target_c != target_composite:
        raise AssertionError("catalectic identity failed")
    rank_b = global_b.rank()
    rank_c = global_c.rank()
    rank_bc = composite.rank()
    middle = global_b.cols
    defect = middle - rank_b - rank_c + rank_bc
    return {
        "parameters": parameters,
        "weights": [str(weight) for weight in weights],
        "term_count": len(parameters),
        "all_quotient_frames_invertible": True,
        "contains_nonmonomial_frame": any(parameter != 0 for parameter in parameters),
        "quotient_polynomial_identity_holds": True,
        "quotient_catalectic_identity_holds": True,
        "formal_local_middle_dimension": 35 * len(parameters),
        "rank_B": rank_b,
        "rank_C": rank_c,
        "rank_BC": rank_bc,
        "kernel_image_defect": defect,
        "projected_sylvester_equality_holds": defect == 0,
    }


def shear_u1_operator(parameters: list[int], weights: list[sp.Rational]) -> dict[str, object]:
    """Return the U1_Q6 zero-target operator for one scalar U coordinate."""

    if len(parameters) != len(weights):
        raise ValueError("parameters and weights must have equal length")
    basis6 = core.exponent_basis(7, 6)
    columns = []
    for parameter, weight in zip(parameters, weights):
        factors = scaled_shear_factors(parameter, weight)
        for omitted in range(7):
            polynomial = core.multiply_linear_forms(
                factors, tuple(index for index in range(7) if index != omitted)
            )
            column = core.coefficient_column(polynomial, basis6)
            # The first labelled factor carries the term weight in both its
            # quotient and graph parts; omitting it removes that weight.
            if omitted == 0:
                column *= weight
            columns.append(column)
    operator = sp.Matrix.hstack(*columns)
    nullspace = operator.nullspace()
    return {
        "term_count": len(parameters),
        "operator_shape": list(operator.shape),
        "rank_per_U_coordinate": operator.rank(),
        "nullity_per_U_coordinate": len(nullspace),
        "total_nullity_across_42_U_coordinates": 42 * len(nullspace),
        "nullspace_supports": [
            [[index, str(value)] for index, value in enumerate(vector) if value]
            for vector in nullspace
        ],
    }


def build_payload() -> dict[str, object]:
    profile = permanent_u_degree_profile()
    controls = [
        shear_pencil_control([-1, 1], [sp.Rational(1, 2), sp.Rational(1, 2)]),
        shear_pencil_control([1, 2, 3], [sp.Integer(3), sp.Integer(-3), sp.Integer(1)]),
    ]
    if [(row["rank_B"], row["rank_C"], row["rank_BC"], row["kernel_image_defect"]) for row in controls] != [
        (45, 40, 35, 20),
        (45, 40, 35, 55),
    ]:
        raise AssertionError("unexpected shear-pencil ranks")
    u1_controls = [
        shear_u1_operator([-1, 1], [sp.Rational(1, 2), sp.Rational(1, 2)]),
        shear_u1_operator([1, 2, 3], [sp.Integer(3), sp.Integer(-3), sp.Integer(1)]),
    ]
    if [(row["rank_per_U_coordinate"], row["nullity_per_U_coordinate"]) for row in u1_controls] != [(12, 2), (12, 9)]:
        raise AssertionError("unexpected U1 shear residual")
    return {
        "schema_version": 1,
        "status": "B2_05_EQUALITY_LOCUS_REDUCED_NOT_DECIDED",
        "full_operator_scale_not_materialized": {
            "parameter_upper_bound_before_gauges": 42 * (7 * 7 + 42 * 7 + 1),
            "degree_seven_ambient_monomials": math.comb(55, 7),
            "sym4_V_dimension": math.comb(52, 4),
            "sym3_V_dimension": math.comb(51, 3),
            "minimal_middle_dimension": 1645,
            "B_shape": [math.comb(52, 4), 1645],
            "C_shape": [1645, math.comb(51, 3)],
            "required_endpoint_ranks": {
                "rank_B_plus_rank_C": 2870,
                "rank_BC": 1225,
            },
        },
        "permanent_U_degree_profile": profile,
        "first_bounded_equations": {
            "U0_Q7": "sum_t lambda_t product_r p_(t,r) = product_r q_r",
            "U1_Q6": "sum_t lambda_t sum_s u_(t,s) product_(r!=s) p_(t,r) = 0",
            "U2_Q5": "the target has exactly 21 transposition monomials",
        },
        "raw_residual_blocks_per_graph_term": {
            "quotient_frame_off_monomial_big_cell_dimension": 42,
            "off_block_graph_entries": 252,
            "diagonal_projective_tail_mismatch_dimension": 30,
            "warning": "These are raw diagnostic blocks, not independent moduli after the equality equations and gauges.",
        },
        "quotient_shear_pencil_controls": controls,
        "shear_U1_Q6_zero_target_controls": u1_controls,
        "candidate_cardinality_checked_before_materialization": {
            "maximum_shear_terms": 3,
            "labelled_middle_columns": 105,
            "quotient_degree_seven_monomials": math.comb(13, 7),
            "full_degree_seven_monomials_skipped": math.comb(55, 7),
        },
        "conservative_peak_memory_mib": 64,
        "decision": "UNRESOLVED_FULL_EQUALITY_LOCUS",
        "claim_boundary": [
            "The U-degree profile is an exact characteristic-zero decomposition of the permanent target and gives a bounded hierarchy of necessary equations.",
            "The quotient-only polynomial identity admits nonmonomial frame decompositions, so target projection alone does not force frame synchronization.",
            "The displayed shear controls fail the projected kernel-image condition; they are diagnostics, not survivors of the full Sylvester equality locus.",
            "Full Sylvester equality does not imply projected Sylvester equality after setting U=0, because output projection can enlarge ker(B); the positive projected defects do not exclude or construct a full packet.",
            "No generic 42-plane completion, permanent decomposition, B2-CLOSED, lower-50, or border-rank claim is made.",
        ],
        "next_exact_gate": "Stream the U1_Q6 zero equations and U2_Q5 transposition equations into the full labelled B/C rank conditions, branch first on quotient-frame monomiality, and test radical containment of each synchronization defect without materializing Sym7(V).",
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
            raise SystemExit("n7 B2 equality-locus reduction JSON mismatch")
        print("PASS n7 B2 equality-locus reduction")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
