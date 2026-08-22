#!/usr/bin/env python3
"""Exact U2Q5 transposition-slice survivor for Packet-B synchronization."""

from __future__ import annotations

import argparse
from functools import lru_cache
import importlib.util
import itertools
import json
import math
from pathlib import Path

import sympy as sp
from flint import fmpq, fmpq_mat


HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / "n7_b2_intrinsic_mixed_complex.py"
SPEC = importlib.util.spec_from_file_location("n7_b2_intrinsic_mixed_complex", CORE_PATH)
core = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(core)


def vector(*entries: int | sp.Rational) -> tuple[sp.Rational, ...]:
    return tuple(sp.Rational(entry) for entry in entries)


@lru_cache(maxsize=None)
def degree_basis(variable_count: int, degree: int) -> tuple[tuple[int, ...], ...]:
    """Generate weak compositions without scanning (degree+1)^variable_count."""

    if variable_count == 1:
        return ((degree,),)
    return tuple(
        (first,) + tail
        for first in range(degree + 1)
        for tail in degree_basis(variable_count - 1, degree - first)
    )


def formal_maps(factors: list[tuple[sp.Rational, ...]]) -> tuple[sp.Matrix, sp.Matrix]:
    basis4 = degree_basis(9, 4)
    basis3 = degree_basis(9, 3)
    subsets = tuple(itertools.combinations(range(7), 4))
    all_indices = set(range(7))
    b_hat = sp.Matrix.hstack(
        *[
            core.coefficient_column(core.multiply_linear_forms(factors, subset), basis4)
            for subset in subsets
        ]
    )
    c_hat = sp.Matrix(
        [
            list(
                core.coefficient_column(
                    core.multiply_linear_forms(
                        factors, tuple(sorted(all_indices.difference(subset)))
                    ),
                    basis3,
                )
            )
            for subset in subsets
        ]
    )
    return b_hat, c_hat


def transposition_survivor_factors() -> list[list[tuple[sp.Rational, ...]]]:
    """Return two rank-seven products in q0..q6,u01,u10 coordinates."""

    basis = [
        tuple(sp.Integer(i == j) for j in range(9)) for i in range(9)
    ]
    plus = [
        vector(
            sp.Rational(1, 2),
            sp.Rational(-1, 2),
            0,
            0,
            0,
            0,
            0,
            sp.Rational(-1, 2),
            sp.Rational(-1, 2),
        ),
        vector(0, 1, 0, 0, 0, 0, 0, 0, -1),
        *basis[2:7],
    ]
    minus = [
        vector(
            sp.Rational(1, 2),
            sp.Rational(1, 2),
            0,
            0,
            0,
            0,
            0,
            sp.Rational(1, 2),
            sp.Rational(-1, 2),
        ),
        vector(0, 1, 0, 0, 0, 0, 0, 0, 1),
        *basis[2:7],
    ]
    return [plus, minus]


def target_column() -> sp.Matrix:
    basis = degree_basis(9, 7)
    answer = sp.zeros(len(basis), 1)
    identity = (1, 1, 1, 1, 1, 1, 1, 0, 0)
    transposition = (0, 0, 1, 1, 1, 1, 1, 1, 1)
    answer[basis.index(identity)] = 1
    answer[basis.index(transposition)] = 1
    return answer


def product_column(factors: list[tuple[sp.Rational, ...]]) -> sp.Matrix:
    basis = degree_basis(9, 7)
    polynomial = core.multiply_linear_forms(factors, tuple(range(7)))
    return core.coefficient_column(polynomial, basis)


def u_degree_histogram(column: sp.Matrix) -> dict[int, int]:
    basis = degree_basis(9, 7)
    histogram = {degree: 0 for degree in range(8)}
    for exponent, coefficient in zip(basis, column):
        if coefficient:
            histogram[sum(exponent[7:])] += 1
    return histogram


def bilinear_residual_form(left: tuple[int, int], right: tuple[int, int]) -> int:
    """The two-shear U2 coefficient x0*y1+x1*y0+2*x1*y1."""

    return left[0] * right[1] + left[1] * right[0] + 2 * left[1] * right[1]


def flint_matrix(matrix: sp.Matrix) -> fmpq_mat:
    return fmpq_mat(
        [
            [fmpq(int(value.p), int(value.q)) for value in matrix.row(row)]
            for row in range(matrix.rows)
        ]
    )


def build_payload() -> dict[str, object]:
    factors = transposition_survivor_factors()
    factor_ranks = [sp.Matrix(term).rank() for term in factors]
    if factor_ranks != [7, 7]:
        raise AssertionError("the survivor terms lost factor rank seven")
    polynomial_sum = product_column(factors[0]) + product_column(factors[1])
    target = target_column()
    if polynomial_sum != target:
        raise AssertionError("transposition-slice polynomial identity failed")

    # Both terms have seven independent factors, so their formal 35-space is
    # already the minimal middle; no symbolic RREF is needed.
    local = [formal_maps(term) for term in factors]
    global_b = sp.Matrix.hstack(*(row[0] for row in local))
    global_c = sp.Matrix.vstack(*(row[1] for row in local))
    flint_b = flint_matrix(global_b)
    flint_c = flint_matrix(global_c)
    rank_b = flint_b.rank()
    rank_c = flint_c.rank()
    rank_bc = (flint_b * flint_c).rank()
    middle = global_b.cols
    defect = middle - rank_b - rank_c + rank_bc
    if (rank_b, rank_c, rank_bc, defect) != (65, 60, 55, 0):
        raise AssertionError("unexpected transposition-slice Sylvester ranks")

    quotient_frames = [sp.Matrix([list(factor[:7]) for factor in term]) for term in factors]
    frame_determinants = [frame.det() for frame in quotient_frames]
    if any(value == 0 for value in frame_determinants):
        raise AssertionError("a quotient frame became singular")
    if any(core.is_monomial(frame) for frame in quotient_frames):
        raise AssertionError("the shear frames unexpectedly became monomial")

    first_line = (1, 0)
    second_line = (-1, 1)
    bilinear_controls = {
        "first_line_isotropic": bilinear_residual_form(first_line, first_line),
        "second_line_isotropic": bilinear_residual_form(second_line, second_line),
        "cross_pairing": bilinear_residual_form(first_line, second_line),
    }
    if bilinear_controls != {
        "first_line_isotropic": 0,
        "second_line_isotropic": 0,
        "cross_pairing": 1,
    }:
        raise AssertionError("the U2 residual form control failed")

    return {
        "schema_version": 1,
        "status": "EXACT_U2Q5_TRANSPOSITION_SLICE_SURVIVOR",
        "coordinate_order": [
            "q0",
            "q1",
            "q2",
            "q3",
            "q4",
            "q5",
            "q6",
            "u01",
            "u10",
        ],
        "exact_identity": "1/2(q0-q1-u01-u10)(q1-u10)prod(q2..q6) + 1/2(q0+q1+u01-u10)(q1+u10)prod(q2..q6) = (q0q1+u01u10)prod(q2..q6)",
        "term_count": 2,
        "factor_ranks": factor_ranks,
        "quotient_frame_determinants": [str(value) for value in frame_determinants],
        "quotient_frames_monomial": [False, False],
        "target_U_degree_histogram": {str(key): value for key, value in u_degree_histogram(target).items()},
        "minimal_complex": {
            "middle_dimension": middle,
            "rank_B": rank_b,
            "rank_C": rank_c,
            "rank_BC": rank_bc,
            "kernel_image_defect": defect,
            "sylvester_equality_holds": defect == 0,
        },
        "U2_residual_bilinear_form": {
            "formula": "x0*y1+x1*y0+2*x1*y1",
            "matrix": [[0, 1], [1, 2]],
            "determinant": -1,
            "isotropic_lines": ["x1=0", "x0+x1=0"],
            "controls": bilinear_controls,
        },
        "candidate_cardinality_checked_before_materialization": {
            "terms": 2,
            "labelled_four_subsets": 2 * math.comb(7, 4),
            "degree_seven_monomials_in_nine_variables": math.comb(15, 7),
            "sym4_dimension_in_nine_variables": math.comb(12, 4),
            "sym3_dimension_in_nine_variables": math.comb(11, 3),
        },
        "conservative_peak_memory_mib": 64,
        "decision": "EXACT_SURVIVOR_OF_IDENTITY_PLUS_SYLVESTER_ON_ONE_TRANSPOSITION_SLICE_ONLY",
        "claim_boundary": [
            "This is an exact characteristic-zero identity with two rank-seven Chow terms and nonmonomial quotient frames.",
            "Its unprojected nine-variable minimal B/C complex has zero kernel-image defect.",
            "It matches the U0_Q7 identity target, the zero U1_Q6 target, and one U2_Q5 transposition target exactly, with no higher-U terms.",
            "It proves that those layers plus local Sylvester equality do not force quotient-frame synchronization.",
            "It is not a 42-complement packet and does not meet or test the global ranks 2870 and 1225; compatibility among all 21 transpositions remains open.",
            "No B2-SURVIVOR for the full equality locus, B2-CLOSED, lower-50, or border-rank claim is made.",
        ],
        "global_rank_join_rule": "Any completion must assemble every term in the original 49-variable B and C, retain cross-term intersections, and finish with rank(B)+rank(C)=2870 and rank(BC)=1225; slice defects cannot be added independently.",
        "next_exact_gate": "Attempt compatible gluing of the 21 transposition-slice survivors; test the first pair of transpositions sharing a row versus a disjoint pair, while updating the original unprojected B/C ranks.",
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
            raise SystemExit("n7 B2 U2Q5 transposition survivor JSON mismatch")
        print("PASS n7 B2 U2Q5 transposition survivor")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
