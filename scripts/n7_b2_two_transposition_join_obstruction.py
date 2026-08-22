#!/usr/bin/env python3
"""Exact unprojected join of two U2Q5 transposition slices."""

from __future__ import annotations

import argparse
from functools import lru_cache
import importlib.util
import itertools
import json
import math
from pathlib import Path

from flint import fmpq, fmpq_mat
import sympy as sp


HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / "n7_b2_intrinsic_mixed_complex.py"
SPEC = importlib.util.spec_from_file_location("n7_b2_intrinsic_mixed_complex", CORE_PATH)
core = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(core)


VARIABLE_COUNT = 11
WEIGHT_SCAN = (
    sp.Rational(-1),
    sp.Rational(1, 3),
    sp.Rational(1, 2),
    sp.Rational(2, 3),
    sp.Rational(2),
)
JOIN_TYPES = {
    "shared_row_01_02": ((0, 1), (0, 2)),
    "disjoint_01_23": ((0, 1), (2, 3)),
}


@lru_cache(maxsize=None)
def degree_basis(variable_count: int, degree: int) -> tuple[tuple[int, ...], ...]:
    if variable_count == 1:
        return ((degree,),)
    return tuple(
        (first,) + tail
        for first in range(degree + 1)
        for tail in degree_basis(variable_count - 1, degree - first)
    )


def pair_slice_terms(
    pair: tuple[int, int],
    u_indices: tuple[int, int],
    identity_weight: sp.Rational,
) -> list[list[tuple[sp.Rational, ...]]]:
    """Return two terms for a*M+T_pair, using rational graph rescaling."""

    if identity_weight in (0, 1):
        raise ValueError("both joined slices must have nonzero identity weight")
    left, right = pair
    forward_u, reverse_u = u_indices
    forward_scale = 1 / identity_weight
    basis = [
        tuple(sp.Integer(row == column) for column in range(VARIABLE_COUNT))
        for row in range(VARIABLE_COUNT)
    ]
    other_factors = [basis[index] for index in range(7) if index not in pair]

    def first_factor(sign: int) -> tuple[sp.Rational, ...]:
        vector = [sp.Integer(0)] * VARIABLE_COUNT
        vector[left] = 1
        vector[right] = sign
        vector[forward_u] = sign * forward_scale
        vector[reverse_u] = -1
        return tuple(identity_weight * sp.Rational(1, 2) * value for value in vector)

    second_minus = list(basis[right])
    second_minus[reverse_u] = -1
    second_plus = list(basis[right])
    second_plus[reverse_u] = 1
    return [
        [first_factor(-1), tuple(second_minus), *other_factors],
        [first_factor(1), tuple(second_plus), *other_factors],
    ]


def formal_maps(
    factors: list[tuple[sp.Rational, ...]],
) -> tuple[sp.Matrix, sp.Matrix]:
    basis4 = degree_basis(VARIABLE_COUNT, 4)
    basis3 = degree_basis(VARIABLE_COUNT, 3)
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


def flint_matrix(matrix: sp.Matrix) -> fmpq_mat:
    return fmpq_mat(
        [
            [fmpq(int(value.p), int(value.q)) for value in matrix.row(row)]
            for row in range(matrix.rows)
        ]
    )


def target_column(pairs: tuple[tuple[int, int], tuple[int, int]]) -> sp.Matrix:
    basis7 = degree_basis(VARIABLE_COUNT, 7)
    answer = sp.zeros(len(basis7), 1)
    identity = (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
    answer[basis7.index(identity)] = 1
    for pair, u_indices in zip(pairs, ((7, 8), (9, 10))):
        exponent = [0] * VARIABLE_COUNT
        for coordinate in range(7):
            if coordinate not in pair:
                exponent[coordinate] = 1
        exponent[u_indices[0]] = 1
        exponent[u_indices[1]] = 1
        answer[basis7.index(tuple(exponent))] = 1
    return answer


def join_control(
    name: str,
    pairs: tuple[tuple[int, int], tuple[int, int]],
    first_identity_weight: sp.Rational,
) -> dict[str, object]:
    second_identity_weight = 1 - first_identity_weight
    factors = pair_slice_terms(pairs[0], (7, 8), first_identity_weight)
    factors += pair_slice_terms(pairs[1], (9, 10), second_identity_weight)
    if [sp.Matrix(term).rank() for term in factors] != [7] * 4:
        raise AssertionError("a joined term lost factor rank seven")

    basis7 = degree_basis(VARIABLE_COUNT, 7)
    polynomial = sum(
        (
            core.coefficient_column(
                core.multiply_linear_forms(term, tuple(range(7))), basis7
            )
            for term in factors
        ),
        sp.zeros(len(basis7), 1),
    )
    if polynomial != target_column(pairs):
        raise AssertionError("two-transposition polynomial join failed")

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
    return {
        "join_type": name,
        "transpositions": [list(pair) for pair in pairs],
        "identity_weights": [str(first_identity_weight), str(second_identity_weight)],
        "term_count": 4,
        "target_monomial_count": sum(value != 0 for value in polynomial),
        "polynomial_identity_holds": True,
        "all_factor_ranks": [7, 7, 7, 7],
        "unprojected_11_variable_complex": {
            "B_shape": list(global_b.shape),
            "C_shape": list(global_c.shape),
            "middle_dimension": middle,
            "rank_B": rank_b,
            "rank_C": rank_c,
            "rank_BC": rank_bc,
            "kernel_image_defect": defect,
            "sylvester_equality_holds": defect == 0,
        },
    }


def build_payload() -> dict[str, object]:
    rows = [
        join_control(name, pairs, weight)
        for name, pairs in JOIN_TYPES.items()
        for weight in WEIGHT_SCAN
    ]
    canonical = {
        row["join_type"]: row["unprojected_11_variable_complex"]
        for row in rows
        if row["identity_weights"] == ["1/2", "1/2"]
    }
    expected = {
        "shared_row_01_02": (111, 94, 75, 10),
        "disjoint_01_23": (114, 95, 81, 12),
    }
    for name, ranks in expected.items():
        row = canonical[name]
        if (row["rank_B"], row["rank_C"], row["rank_BC"], row["kernel_image_defect"]) != ranks:
            raise AssertionError(("unexpected canonical join ranks", name, row))
    if any(row["unprojected_11_variable_complex"]["sylvester_equality_holds"] for row in rows):
        raise AssertionError("the bounded rational scan found an unexpected join survivor")
    return {
        "schema_version": 1,
        "status": "TWO_TRANSPOSITION_CANONICAL_JOIN_FAMILY_OBSTRUCTED",
        "weight_scan": [str(weight) for weight in WEIGHT_SCAN],
        "rows": rows,
        "canonical_half_half_ranks": canonical,
        "candidate_cardinality_checked_before_materialization": {
            "join_types": len(JOIN_TYPES),
            "identity_weight_choices": len(WEIGHT_SCAN),
            "exact_join_controls": len(rows),
            "terms_per_control": 4,
            "labelled_middle_columns_per_control": 4 * math.comb(7, 4),
            "degree_seven_monomials_in_11_variables": math.comb(17, 7),
            "full_degree_seven_monomials_skipped": math.comb(55, 7),
        },
        "conservative_peak_memory_mib": 96,
        "nonzero_weight_equivalence": "For a not in {0,1}, normalizing the first factor replaces u_ij by a^(-1)u_ij. Independent invertible diagonal rescalings of the two slices' forward-U coordinates, together with nonzero factor rescalings, identify every weight a with the half-half factor-plane arrangement for rank purposes.",
        "decision": "NO_SURVIVOR_IN_CANONICAL_TWO_SLICE_JOIN_FAMILY_FOR_ANY_NONZERO_IDENTITY_WEIGHTS",
        "claim_boundary": [
            "Every row is one exact four-term polynomial identity for the identity permutation and two specified transpositions.",
            "B, C, and BC are assembled once in the common unprojected 11-variable space; no local ranks are added.",
            "The half-half shared-row join has defect 10 and the half-half disjoint join has defect 12.",
            "Invertible diagonal coordinate and factor rescalings prove these ranks for every nonzero identity-weight split a+(1-a)=1; the rational scan is a frozen control of that equivalence.",
            "This does not classify noncanonical four-term factorizations or graph couplings between the two slices.",
            "A positive join defect may be repaired by images from additional terms in a full packet, so these controls do not exclude a 42-complement completion.",
            "No full B2-CLOSED, B2-SURVIVOR, lower-50, or border-rank claim is made.",
        ],
        "global_rank_join_rule": "A full completion must append all remaining term blocks in the original 49-variable maps and recompute, not add, ranks until rank(B)+rank(C)=2870 and rank(BC)=1225.",
        "next_exact_gate": "Compute the defect-killing subspace required from one additional rank-seven term for the shared-row defect 10 and disjoint defect 12; test whether its factor-plane constraints can supply that image without creating a new kernel.",
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
            raise SystemExit("n7 B2 two-transposition join JSON mismatch")
        print("PASS n7 B2 two-transposition join obstruction")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
