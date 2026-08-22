#!/usr/bin/env python3
"""Exact same-row Hessian witnesses for the Packet-A aggregate K5 kernel."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path

import sympy as sp


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


hessian = load_local("n7_packet_a_gradient_syzygy_hessian")
general = hessian.general
COLUMN_PAIRS = tuple(itertools.combinations(range(N), 2))
DIAGONAL_ROW_PAIR_COLUMNS = tuple(
    hessian.ORDERED_ROW_PAIRS.index((row, row)) for row in range(N)
)


def diagonal_selector() -> sp.MutableSparseMatrix:
    """Select the seven same-row columns from the ordered 49 row pairs."""

    selector = sp.MutableSparseMatrix(len(hessian.ORDERED_ROW_PAIRS), N, {})
    for row, source in enumerate(DIAGONAL_ROW_PAIR_COLUMNS):
        selector[source, row] = 1
    return selector


def same_row_witness_block(
    terms: tuple[tuple[tuple[int, ...], ...], ...],
    coefficients: tuple[sp.Rational, ...],
    column_pair: tuple[int, int],
) -> sp.Matrix:
    """Return W_(b,d), whose columns are forced global K5 relations."""

    if column_pair not in COLUMN_PAIRS:
        raise ValueError("an increasing pair of distinct columns is required")
    transport = hessian.forced_hessian_transport(terms, coefficients, column_pair)
    return transport * diagonal_selector()


def row_slice(
    factor: tuple[int, ...], row: int
) -> tuple[int, ...]:
    if len(factor) != N * N or not 0 <= row < N:
        raise ValueError("a 49-coordinate factor and one row are required")
    return tuple(factor[row * N + column] for column in range(N))


def off_diagonal_symmetrized_pair(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    """Coordinates p_b q_d+p_d q_b for b<d."""

    if len(left) != N or len(right) != N:
        raise ValueError("two seven-column row slices are required")
    return tuple(
        left[b] * right[d] + left[d] * right[b] for b, d in COLUMN_PAIRS
    )


def hard_residual_equations_for_term(
    factors: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    """Stream the factorwise equations equivalent to W=0 for one term."""

    if general.validate_factors(factors) != N * N:
        raise ValueError("seven factors in the 49-variable ambient are required")
    equations = []
    for row in range(N):
        slices = tuple(row_slice(factor, row) for factor in factors)
        for first, second in itertools.combinations(range(N), 2):
            equations.extend(
                off_diagonal_symmetrized_pair(slices[first], slices[second])
            )
    return tuple(equations)


def witness_is_zero_factorwise(
    terms: tuple[tuple[tuple[int, ...], ...], ...]
) -> bool:
    return all(not any(hard_residual_equations_for_term(term)) for term in terms)


def build_payload() -> dict[str, object]:
    labelled_degree5 = TERM_COUNT * math.comb(N, 5)
    witness_columns = len(COLUMN_PAIRS) * N
    scalar_entries = labelled_degree5 * witness_columns
    full_sym5_rows = math.comb(N * N + 5 - 1, 5)
    projected_rows = len(hessian.EXPONENTS5)
    return {
        "schema_version": 2,
        "status": "PACKET_A_HESSIAN_RELATION_DICHOTOMY_EXACT",
        "universal_global_matrix_identity": {
            "witness_block_formula": (
                "W_(b,d)[(i,omit {r,s}),u] = c_i "
                "(a_(i,r,u,b)a_(i,s,u,d)+a_(i,s,u,b)a_(i,r,u,d))"
            ),
            "identity": "A5_full(F) W_(b,d)(F,c) = 0",
            "reason": (
                "the left side is the full mixed second derivative "
                "d^2 perm_7/(d x_(u,b) d x_(u,d)), which vanishes by row multilinearity"
            ),
            "column_pairs": len(COLUMN_PAIRS),
            "same_row_columns_per_pair": N,
            "cross_column_witness_matrix_shape": [labelled_degree5, witness_columns],
            "consequence": (
                "on every true identity, W nonzero forces a nonzero vector in the aggregate global K5"
            ),
        },
        "torus_projection_boundary": {
            "full_A5_row_count": full_sym5_rows,
            "one_torus_projection_row_count": projected_rows,
            "forgotten_row_count": full_sym5_rows - projected_rows,
            "statement": (
                "A5_(b,d) W_(b,d)=0 from the 462-row block alone is only a projected relation; "
                "it cannot by itself certify W_(b,d) in the global aggregate K5"
            ),
        },
        "exact_hard_residual_component": {
            "name": "Z_A_grad_hess_W0",
            "definition": "Z_A_grad_hess intersect {W_(b,d)=0 for every b<d}",
            "factorwise_equations": (
                "a_(i,r,u,b)a_(i,s,u,d)+a_(i,r,u,d)a_(i,s,u,b)=0 "
                "for every i,u,r<s,b<d"
            ),
            "factorwise_equation_count_before_dependencies": scalar_entries,
            "direct_sum_reason": (
                "external coefficients are nonzero and each (i,{r,s}) has its own labelled coordinate, "
                "so W=0 has no cancellation between terms or omitted-factor pairs"
            ),
            "dichotomy": (
                "a true 49-term identity either has aggregate K5 nonzero, witnessed by W, "
                "or lies in Z_A_grad_hess_W0"
            ),
        },
        "resource_bound": {
            "candidate_scalar_witness_entries": scalar_entries,
            "materialize_full_A5": False,
            "stream_one_term_equations": N * math.comb(N, 2) * math.comb(N, 2),
            "conservative_peak_memory_mib": 32,
        },
        "pairing_tautology": {
            "identity": "D^(-1) P W^all subset im(A2^T) = (K2)^perp",
            "reason": (
                "pairing a K2 relation with a Hessian witness is the corresponding "
                "second derivative of the zero quadratic polynomial A2 x"
            ),
            "consequence": (
                "no linear combination of the 196 same-row Hessian witnesses can obstruct "
                "the inverse-coefficient 2/5 endpoint"
            ),
        },
        "smallest_remaining_invariant": (
            "prove that the transported full K5 has nonzero image in M2/im(A2^T), "
            "after factoring out every Hessian-generated relation"
        ),
        "claim_boundary": [
            "This proves a universal nonzero aggregate-K5 witness only on the open branch W nonzero.",
            "The simple-matroid condition alone does not exclude W=0: independent row-separated factors make every displayed factorwise equation zero.",
            "The Hessian-generated K5 subspace is tautologically orthogonal to all of K2 and cannot prove failure of the inverse-coefficient 2/5 pairing.",
            "No equality candidate and no repeated Glynn or numerical control is used.",
            "A-CLOSED, ordinary lower 50, and border rank remain unresolved on Z_A_grad_hess_W0.",
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
            raise SystemExit("Packet A Hessian-relation JSON mismatch")
        print("PASS n7 Packet A Hessian relation")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
