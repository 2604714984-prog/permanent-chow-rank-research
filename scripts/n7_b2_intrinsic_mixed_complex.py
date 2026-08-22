#!/usr/bin/env python3
"""Exact labelled B/C complex and common-code obstruction for Packet B wave 1."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp


N = 7
FOUR_SUBSETS = tuple(itertools.combinations(range(N), 4))
THREE_SUBSETS = tuple(itertools.combinations(range(N), 3))


def exponent_basis(variable_count: int, degree: int) -> tuple[tuple[int, ...], ...]:
    """Return the lexicographically ordered exponent basis of Sym^degree."""

    return tuple(
        exponent
        for exponent in itertools.product(range(degree + 1), repeat=variable_count)
        if sum(exponent) == degree
    )


def multiply_linear_forms(
    factors: list[tuple[int, ...]], indices: tuple[int, ...]
) -> dict[tuple[int, ...], int]:
    """Multiply selected labelled linear forms over Z, retaining coefficients."""

    variable_count = len(factors[0])
    polynomial = {(0,) * variable_count: 1}
    for factor_index in indices:
        factor = factors[factor_index]
        updated: dict[tuple[int, ...], int] = {}
        for exponent, coefficient in polynomial.items():
            for variable, value in enumerate(factor):
                if not value:
                    continue
                new_exponent = list(exponent)
                new_exponent[variable] += 1
                key = tuple(new_exponent)
                updated[key] = updated.get(key, 0) + coefficient * value
        polynomial = updated
    return polynomial


def coefficient_column(
    polynomial: dict[tuple[int, ...], int],
    basis: tuple[tuple[int, ...], ...],
) -> sp.Matrix:
    return sp.Matrix([polynomial.get(exponent, 0) for exponent in basis])


def formal_labelled_maps(factors: list[tuple[int, ...]]) -> tuple[sp.Matrix, sp.Matrix]:
    """Return labelled B-hat and C-hat in divided-power coordinates.

    Columns of B-hat are four-factor products indexed by I.  Row I of C-hat
    is the complementary three-factor product, viewed as a functional on the
    divided-power cubic dual.  Their product is the rectangular catalectic.
    """

    if len(factors) != N or len({len(factor) for factor in factors}) != 1:
        raise ValueError("a term needs seven equally sized labelled factors")
    variable_count = len(factors[0])
    basis4 = exponent_basis(variable_count, 4)
    basis3 = exponent_basis(variable_count, 3)
    b_hat = sp.Matrix.hstack(
        *[
            coefficient_column(multiply_linear_forms(factors, subset), basis4)
            for subset in FOUR_SUBSETS
        ]
    )
    c_rows = []
    all_indices = set(range(N))
    for subset in FOUR_SUBSETS:
        complement = tuple(sorted(all_indices.difference(subset)))
        c_rows.append(
            list(coefficient_column(multiply_linear_forms(factors, complement), basis3))
        )
    return b_hat, sp.Matrix(c_rows)


def intrinsic_rank_factorization(
    factors: list[tuple[int, ...]],
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return a minimal factorization A_i=B_i C_i of the catalectic."""

    b_hat, c_hat = formal_labelled_maps(factors)
    catalectic = b_hat * c_hat
    _, pivots = catalectic.rref()
    b_i = catalectic[:, list(pivots)]
    pivot_rows = tuple(sp.Matrix(b_i.T).rref()[1])
    square = b_i[list(pivot_rows), :]
    c_i = square.inv() * catalectic[list(pivot_rows), :]
    if b_i * c_i != catalectic:
        raise AssertionError("intrinsic complex changed the catalectic")
    return b_i, c_i, catalectic


def rank_six_s1_factors() -> list[tuple[int, ...]]:
    factors = [tuple(int(i == j) for j in range(6)) for i in range(6)]
    return factors + [factors[0]]


def rank_six_s2_factors() -> list[tuple[int, ...]]:
    factors = [tuple(int(i == j) for j in range(6)) for i in range(6)]
    return factors + [tuple(int(j in (0, 1)) for j in range(6))]


def rank_seven_factors() -> list[tuple[int, ...]]:
    return [tuple(int(i == j) for j in range(7)) for i in range(7)]


def is_monomial(matrix: sp.Matrix) -> bool:
    if matrix.rows != matrix.cols or matrix.det() == 0:
        return False
    return all(
        sum(value != 0 for value in matrix.row(row)) == 1
        for row in range(matrix.rows)
    ) and all(
        sum(value != 0 for value in matrix.col(column)) == 1
        for column in range(matrix.cols)
    )


def projective_tail_key(tail: list[int]) -> tuple[sp.Rational, ...] | None:
    """Normalize a nonzero rational tail by its first nonzero coordinate."""

    first = next((value for value in tail if value != 0), None)
    if first is None:
        return None
    return tuple(sp.Rational(value, first) for value in tail)


def projective_tails_match(tails: list[list[int]]) -> bool:
    """Require seven nonzero tails representing one projective point."""

    if len(tails) != N:
        raise ValueError("the common-code test requires seven diagonal tails")
    keys = [projective_tail_key(tail) for tail in tails]
    return all(key is not None for key in keys) and all(
        key == keys[0] for key in keys[1:]
    )


def graph_code_conditions(graph: sp.Matrix) -> tuple[bool, bool, list[list[int]]]:
    if graph.shape != (42, N):
        raise ValueError("a graph map must be a 42 by 7 matrix")
    off_block = any(
        graph[row, column] != 0
        for row in range(42)
        for column in range(N)
        if row // 6 != column
    )
    tails = [
        [int(graph[6 * column + offset, column]) for offset in range(6)]
        for column in range(N)
    ]
    return not off_block, projective_tails_match(tails), tails


def common_code_control(
    name: str, relative_frame: sp.Matrix, graph: sp.Matrix, construction: str
) -> dict[str, object]:
    block_support, diagonal_tail_match, tails = graph_code_conditions(graph)
    frame_sync = is_monomial(relative_frame)
    return {
        "name": name,
        "construction": construction,
        "relative_frame": [
            [int(value) for value in row] for row in relative_frame.tolist()
        ],
        "relative_frame_is_monomial": frame_sync,
        "block_diagonal_graph_support_holds": block_support,
        "diagonal_tails": tails,
        "seven_diagonal_tails_match": diagonal_tail_match,
        "common_code_morphism_defined": (
            frame_sync and block_support and diagonal_tail_match
        ),
    }


def common_code_residual_controls() -> list[dict[str, object]]:
    """Exhibit three exact residual moduli of otherwise legal complements."""

    sheared_frame = sp.eye(N)
    sheared_frame[0, 1] = 1
    zero_graph = sp.zeros(42, N)

    off_block_graph = sp.zeros(42, N)
    off_block_graph[6, 0] = 1

    diagonal_mismatch = sp.zeros(42, N)
    for column in range(N):
        diagonal_mismatch[6 * column, column] = 1
    diagonal_mismatch[6, 1] = 0
    diagonal_mismatch[7, 1] = 1

    return [
        common_code_control(
            "nonmonomial_factor_frame",
            sheared_frame,
            zero_graph,
            "Inside one legal rank-seven complement plane, replace the seven factor lines by a sheared quotient frame; this is a single-plane control and supplies no 42-plane completion.",
        ),
        common_code_control(
            "off_block_graph_map",
            sp.eye(N),
            off_block_graph,
            "Use one legal complement that is the graph of a map with Q_0 to U_1; this is a single-plane control and supplies no 42-plane completion.",
        ),
        common_code_control(
            "diagonal_tail_mismatch",
            sp.eye(N),
            diagonal_mismatch,
            "Use one legal block-diagonal graph complement whose seven nonzero diagonal tails are not one projective point; this supplies no 42-plane completion.",
        ),
    ]


def build_payload() -> dict[str, object]:
    controls = []
    for name, factors, expected_rank in (
        ("rank_six_s1", rank_six_s1_factors(), 25),
        ("rank_six_s2", rank_six_s2_factors(), 25),
        ("rank_seven", rank_seven_factors(), 35),
    ):
        b_hat, c_hat = formal_labelled_maps(factors)
        b_i, c_i, catalectic = intrinsic_rank_factorization(factors)
        if b_i.cols != expected_rank or b_i * c_i != catalectic:
            raise AssertionError(("unexpected local rank factorization", name))
        controls.append(
            {
                "name": name,
                "formal_B_shape": list(b_hat.shape),
                "formal_B_rank": b_hat.rank(),
                "formal_C_shape": list(c_hat.shape),
                "formal_C_rank": c_hat.rank(),
                "formal_middle_dimension": len(FOUR_SUBSETS),
                "invisible_label_overlap_dimension": c_hat.rank() - catalectic.rank(),
                "catalectic_shape": list(catalectic.shape),
                "intrinsic_B_shape": list(b_i.shape),
                "intrinsic_C_shape": list(c_i.shape),
                "minimal_middle_rank": catalectic.rank(),
            }
        )
    if [row["minimal_middle_rank"] for row in controls] != [25, 25, 35]:
        raise AssertionError("unexpected Packet-B local middle ranks")
    residuals = common_code_residual_controls()
    if any(row["common_code_morphism_defined"] for row in residuals):
        raise AssertionError("a residual-moduli control unexpectedly synchronized")
    tail_controls = {
        "identical_nonzero": projective_tails_match([[1, 2, 0, 0, 0, 0]] * N),
        "proportional_nonzero": projective_tails_match(
            [[scale, 0, 0, 0, 0, 0] for scale in range(1, N + 1)]
        ),
        "distinct_e0_e1": projective_tails_match(
            [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
            + [[1, 0, 0, 0, 0, 0]] * (N - 2)
        ),
        "all_zero_tails_match": projective_tails_match([[0, 0, 0, 0, 0, 0]] * N),
    }
    if tail_controls != {
        "identical_nonzero": True,
        "proportional_nonzero": True,
        "distinct_e0_e1": False,
        "all_zero_tails_match": False,
    }:
        raise AssertionError(("projective tail controls failed", tail_controls))
    return {
        "schema_version": 1,
        "status": "B2_WAVE1_INTRINSIC_COMPLEX_COMMON_CODE_OBSTRUCTION",
        "packet_cardinality": {
            "rank_six_terms": 7,
            "rank_seven_graph_complements": 42,
            "labelled_four_subsets_per_term": len(FOUR_SUBSETS),
            "formal_labelled_middle_dimension": 49 * len(FOUR_SUBSETS),
            "minimal_intrinsic_middle_dimension": 7 * 25 + 42 * 35,
        },
        "local_exact_controls": controls,
        "basis_actions": {
            "formal_B": "e_I maps to product_{a in I} ell_a",
            "formal_C": "theta maps to sum_I theta(product_{a notin I} ell_a)e_I",
            "intrinsic_K": "K_i=image(formal_B_i formal_C_i), equivalently image(formal_C_i)/(image(formal_C_i) intersect ker(formal_B_i))",
            "intrinsic_B_C": "a minimal rank factorization formal_B_i formal_C_i = B_i C_i",
            "global_B": "sum_i intrinsic_B_i on direct_sum_i K_i",
            "global_C": "stack_i intrinsic_C_i from Sym3(V)^dual",
            "equality_condition": "ker(global_B) subset image(global_C)",
            "target_catalectic_identity": "sum_i B_i C_i = C_(3,4)(perm_7)",
            "intrinsic_mixed_obstruction": "ker(B)/(ker(B) intersect image(C))",
        },
        "common_code_residual_controls": residuals,
        "projective_tail_controls": tail_controls,
        "b2_05_decision": "UNRESOLVED_ON_EQUALITY_LOCUS",
        "candidate_cardinality_checked_before_materialization": 49 * len(FOUR_SUBSETS),
        "conservative_peak_memory_mib": 32,
        "claim_boundary": [
            "The basis-level B/C formulas are exact and retain factor labels before taking the minimal catalectic rank space.",
            "The 1715-dimensional formal labelled middle is distinct from the 1645-dimensional minimal intrinsic middle.",
            "A common degree-three/four point code is defined only after quotient-frame synchronization, block-compatible graph support, and equality of the seven normalized diagonal tails.",
            "The three exact residual controls are single-plane replacements; they falsify a canonical reduction on one arbitrary complement but provide no generic 42-plane completion and no permanent-identity counterexample.",
            "Degree-six target containment is a separate necessary condition and is not substituted for ker(B) subset image(C).",
            "B2-05 remains unresolved on the equality locus; no B2-CLOSED, lower-50, or border-rank claim is made.",
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
            raise SystemExit("n7 B2 intrinsic mixed complex JSON mismatch")
        print("PASS n7 B2 intrinsic mixed complex")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
