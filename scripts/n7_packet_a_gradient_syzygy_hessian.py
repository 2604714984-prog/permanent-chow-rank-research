#!/usr/bin/env python3
"""Universal forced-Hessian syzygy for the Packet-A residual component."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
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


general = load_local("n7_packet_a_general_operator")
gradient = load_local("n7_packet_a_equality_locus_gradient")
permanent_block = gradient.block

EXPONENTS5 = general.exponent_basis(N, 5)
EXPONENT_INDEX5 = {alpha: index for index, alpha in enumerate(EXPONENTS5)}
SUBSETS5 = general.factor_subsets(5)
OMITTED_PAIR_TO_SUBSET_INDEX = {
    tuple(sorted(set(range(N)).difference(subset))): index
    for index, subset in enumerate(SUBSETS5)
}
ORDERED_ROW_PAIRS = tuple(itertools.product(range(N), repeat=2))
TARGET_SCALE = math.factorial(5)
MAX_PROJECTED_STATE_COUNT = (1 << (N - 2)) * len(EXPONENTS5)


def projected_five_factor_column(
    factors: tuple[tuple[int, ...], ...],
    subset: tuple[int, ...],
    omitted_columns: tuple[int, int],
) -> sp.Matrix:
    """Project a five-factor product to a two-omitted-column torus block."""

    if permanent_block.general.validate_factors(factors) != N * N:
        raise ValueError("the Hessian block uses the 49 matrix-entry coordinates")
    omitted = tuple(sorted(omitted_columns))
    if len(set(omitted)) != 2:
        raise ValueError("two distinct omitted columns are required")
    allowed = tuple(column for column in range(N) if column not in omitted)
    bit = {column: 1 << index for index, column in enumerate(allowed)}
    full_mask = (1 << (N - 2)) - 1
    states: dict[tuple[int, tuple[int, ...]], int] = {(0, (0,) * N): 1}
    for factor_index in subset:
        updated: dict[tuple[int, tuple[int, ...]], int] = {}
        factor = factors[factor_index]
        for (mask, exponent), coefficient in states.items():
            for row in range(N):
                for column in allowed:
                    column_bit = bit[column]
                    if mask & column_bit:
                        continue
                    value = factor[row * N + column]
                    if value == 0:
                        continue
                    target = list(exponent)
                    target[row] += 1
                    key = (mask | column_bit, tuple(target))
                    updated[key] = updated.get(key, 0) + coefficient * value
        states = updated
        if len(states) > MAX_PROJECTED_STATE_COUNT:
            raise AssertionError("five-factor DP exceeded its precomputed state bound")
    answer = [0] * len(EXPONENTS5)
    for (mask, exponent), coefficient in states.items():
        if mask == full_mask:
            answer[EXPONENT_INDEX5[exponent]] += coefficient
    return sp.Matrix(answer)


def projected_term_hessian_block(
    factors: tuple[tuple[int, ...], ...], omitted_columns: tuple[int, int]
) -> sp.Matrix:
    return sp.Matrix.hstack(
        *[
            projected_five_factor_column(factors, subset, omitted_columns)
            for subset in SUBSETS5
        ]
    )


def forced_hessian_transport(
    terms: tuple[tuple[tuple[int, ...], ...], ...],
    coefficients: tuple[sp.Rational, ...],
    ordered_columns: tuple[int, int],
) -> sp.Matrix:
    """Coefficient transport forced by two labelled differentiations."""

    if len(terms) != len(coefficients) or ordered_columns[0] == ordered_columns[1]:
        raise ValueError("term counts must agree and the columns must be distinct")
    left_column, right_column = ordered_columns
    transport = sp.zeros(len(terms) * len(SUBSETS5), len(ORDERED_ROW_PAIRS))
    for term_index, (factors, coefficient) in enumerate(zip(terms, coefficients)):
        if coefficient == 0 or permanent_block.general.validate_factors(factors) != N * N:
            raise ValueError("nonzero weighted rank-seven terms are required")
        for omitted_factors, subset_index in OMITTED_PAIR_TO_SUBSET_INDEX.items():
            first_factor, second_factor = omitted_factors
            first = factors[first_factor]
            second = factors[second_factor]
            labelled_row = term_index * len(SUBSETS5) + subset_index
            for target_column, (left_row, right_row) in enumerate(ORDERED_ROW_PAIRS):
                transport[labelled_row, target_column] = coefficient * (
                    first[left_row * N + left_column]
                    * second[right_row * N + right_column]
                    + second[left_row * N + left_column]
                    * first[right_row * N + right_column]
                )
    return transport


def permanent_hessian_target() -> sp.Matrix:
    target = sp.zeros(len(EXPONENTS5), len(ORDERED_ROW_PAIRS))
    for column, (left_row, right_row) in enumerate(ORDERED_ROW_PAIRS):
        if left_row == right_row:
            continue
        alpha = tuple(
            0 if row in (left_row, right_row) else 1 for row in range(N)
        )
        target[EXPONENT_INDEX5[alpha], column] = TARGET_SCALE
    return target


def forced_hessian_residual(
    terms: tuple[tuple[tuple[int, ...], ...], ...],
    coefficients: tuple[sp.Rational, ...],
    ordered_columns: tuple[int, int],
) -> sp.Matrix:
    aggregate = sp.Matrix.hstack(
        *[
            projected_term_hessian_block(term, ordered_columns)
            for term in terms
        ]
    )
    return (
        aggregate * forced_hessian_transport(terms, coefficients, ordered_columns)
        - permanent_hessian_target()
    )


def swapped_row_permutation() -> sp.Matrix:
    lookup = {pair: index for index, pair in enumerate(ORDERED_ROW_PAIRS)}
    permutation = sp.zeros(len(ORDERED_ROW_PAIRS))
    for column, pair in enumerate(ORDERED_ROW_PAIRS):
        permutation[lookup[(pair[1], pair[0])], column] = 1
    return permutation


def universal_mixed_partial_control() -> dict[str, object]:
    point = (1, 2, -1, 3, 2, -2, 1)
    term = permanent_block.column_uniform_factors(point)
    perturbed = [list(factor) for factor in term]
    perturbed[6][0] += 2
    terms = (tuple(tuple(factor) for factor in perturbed),)
    coefficients = (sp.Rational(3, 5),)
    left = forced_hessian_residual(terms, coefficients, (0, 1))
    right = forced_hessian_residual(terms, coefficients, (1, 0))
    permutation = swapped_row_permutation()
    identity_holds = left == right * permutation
    if not identity_holds:
        raise AssertionError("mixed-partial symmetry failed")
    return {
        "coefficient_field": "QQ exact",
        "factor_input_is_non_column_uniform": True,
        "residual_shape": list(left.shape),
        "column_swap_requires_row_pair_swap": True,
        "mixed_partial_symmetry_holds": identity_holds,
        "identity": "E_(b,d)(u,v) = E_(d,b)(v,u)",
    }


def build_payload() -> dict[str, object]:
    control = universal_mixed_partial_control()
    sym6_unsymmetrized = N ** 6
    sym6_symmetric = len(permanent_block.EXPONENTS6)
    schema = {
        "previous_component": "Z_A_grad",
        "refined_component": "Z_A_grad_hess",
        "definition": (
            "Z_A_grad intersect all equations A5_{b,d}(F) R2_{b,d}(F,c)=T_{b,d} for unordered omitted-column pairs"
        ),
        "omitted_column_pair_count": math.comb(N, 2),
        "rows_per_forced_hessian_block": len(EXPONENTS5),
        "ordered_row_pair_target_columns": len(ORDERED_ROW_PAIRS),
        "zero_diagonal_row_pair_targets": N,
        "displayed_scalar_equations_before_dependencies": (
            math.comb(N, 2) * len(EXPONENTS5) * len(ORDERED_ROW_PAIRS)
        ),
        "labelled_degree_5_columns_for_49_terms": 49 * len(SUBSETS5),
        "maximum_DP_state_count_per_labelled_product": MAX_PROJECTED_STATE_COUNT,
        "largest_single_49_term_block_shape": [
            len(EXPONENTS5),
            49 * len(SUBSETS5),
        ],
        "conservative_peak_memory_mib": 128,
    }
    information_loss = {
        "unsymmetrized_one_omitted_column_row_assignments": sym6_unsymmetrized,
        "symmetrized_gradient_block_rows": sym6_symmetric,
        "forgotten_dimensions_before_factor_relations": sym6_unsymmetrized - sym6_symmetric,
        "consequence": (
            "the Jacobian of the 924-row gradient projection retains only column-averaged mixed partials and cannot recover a specified second omitted column"
        ),
    }
    return {
        "schema_version": 1,
        "status": "PACKET_A_GRADIENT_SYZYGY_REFINED_TO_FORCED_HESSIAN_COMPONENT",
        "universal_lemma": {
            "statement": (
                "Every Packet-A permanent identity satisfies the 21 forced-Hessian torus blocks and their exact mixed-partial swap symmetry"
            ),
            "proof_method": (
                "differentiate each labelled Chow term twice; the two orders pair the same omitted-factor pair and differ only by swapping the ordered row labels"
            ),
            "executable_QQ_control": control,
        },
        "gradient_Jacobian_information_loss": information_loss,
        "exact_minimal_residual_component": schema,
        "smallest_remaining_invariant": (
            "classify Z_A_grad_hess on the simple-matroid open set, or prove that its forced A5 transport creates a nonzero aggregate K5 relation incompatible with the inverse-coefficient 2/5 pairing"
        ),
        "claim_boundary": [
            "The forced-Hessian equations are a universal necessary lemma for a true identity, not a proof that their zero locus is empty.",
            "No Glynn-family control is added in this package.",
            "The 924-row gradient projection alone cannot yield the oriented cross-column syzygy because it forgets 116725 row-assignment dimensions per omitted-column block.",
            "No exact 49-term survivor or universal nonzero defect is produced.",
            "A-CLOSED, ordinary lower 50, and border rank remain unresolved pending classification of Z_A_grad_hess or the displayed K5 consequence.",
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
            raise SystemExit("Packet A gradient-syzygy JSON mismatch")
        print("PASS n7 Packet A forced-Hessian syzygy")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
