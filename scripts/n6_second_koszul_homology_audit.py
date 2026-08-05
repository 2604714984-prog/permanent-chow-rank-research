#!/usr/bin/env python3
"""Close the output-degree-two second-Koszul rank window for ``perm_6``.

The characteristic-zero homology at

    D_3(f) tensor V -> D_2(f) tensor Lambda^2(V)
        -> D_1(f) tensor Lambda^3(V)

is dual to ``Tor_2(A_f, k)_4`` for the apolar algebra ``A_f``.  The permanent
Betti number is the published formula

    beta_2,4(S / perm_n^perp) = 2 * C(n, 2) * C(n, 4).

For one independent degree-n Chow term in an n^2-dimensional ambient space,
the apolar algebra is a complete intersection of the inactive linear forms and
n active squares, so ``beta_2,4 = C(n, 2)``.

The script verifies the resulting exact ranks and independently replays a
common-factor family showing that scalar homology dimension is not
subadditive under addition of Chow terms.  Modular ranks are used only as
lower-bound cross-checks; the characteristic-zero equalities come from the
written homology and intersection proofs.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable

N = 6
VARIABLES = N * N
PRIME = 1_000_003
COMMON_FACTOR = 0
BLOCK_SIZE = N - 1
WEDGE_TWO = tuple(combinations(range(VARIABLES), 2))
WEDGE_THREE = tuple(combinations(range(VARIABLES), 3))
WEDGE_THREE_INDEX = {value: index for index, value in enumerate(WEDGE_THREE)}
WEDGE_THREE_COUNT = len(WEDGE_THREE)

SparseVector = dict[int, int]


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def insertion_sign(variable: int, wedge: tuple[int, int]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def sparse_rank_mod(
    columns: Iterable[SparseVector],
    prime: int = PRIME,
) -> int:
    pivots: dict[int, SparseVector] = {}
    rank = 0
    for raw in columns:
        vector = {row: value % prime for row, value in raw.items() if value % prime}
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(coefficient, prime - 2, prime)
                if coefficient != 1:
                    vector = {
                        row: value * inverse % prime
                        for row, value in vector.items()
                    }
                pivots[pivot] = vector
                rank += 1
                break
            for row, value in existing.items():
                updated = (vector.get(row, 0) - coefficient * value) % prime
                if updated:
                    vector[row] = updated
                else:
                    vector.pop(row, None)
    return rank


def permanent_quadratic_homology_dimension(n: int) -> int:
    return 2 * comb(n, 2) * comb(n, 4)


def independent_chow_quadratic_homology_dimension(n: int) -> int:
    return comb(n, 2)


def second_koszul_domain_dimension(
    derivative_dimension: int,
    ambient_dimension: int,
) -> int:
    return derivative_dimension * comb(ambient_dimension, 2)


def preceding_first_koszul_permanent_rank(n: int) -> int:
    ambient = n * n
    return ambient * comb(n, 3) ** 2 - comb(n, 4) ** 2


def preceding_first_koszul_chow_rank(n: int) -> int:
    ambient = n * n
    return ambient * comb(n, 3) - comb(n, 4)


def exact_permanent_second_koszul_rank(n: int) -> int:
    ambient = n * n
    domain = second_koszul_domain_dimension(comb(n, 2) ** 2, ambient)
    return (
        domain
        - preceding_first_koszul_permanent_rank(n)
        - permanent_quadratic_homology_dimension(n)
    )


def exact_independent_chow_second_koszul_rank(n: int) -> int:
    ambient = n * n
    domain = second_koszul_domain_dimension(comb(n, 2), ambient)
    return (
        domain
        - preceding_first_koszul_chow_rank(n)
        - independent_chow_quadratic_homology_dimension(n)
    )


def family_supports(term_count: int) -> tuple[tuple[int, ...], ...]:
    if term_count < 1:
        raise ValueError("term_count must be positive")
    last_variable = COMMON_FACTOR + BLOCK_SIZE * term_count
    if last_variable >= VARIABLES:
        raise ValueError("common-factor family exceeds the ambient dimension")
    return tuple(
        (COMMON_FACTOR,)
        + tuple(
            range(
                1 + BLOCK_SIZE * index,
                1 + BLOCK_SIZE * (index + 1),
            )
        )
        for index in range(term_count)
    )


def family_second_derivative_basis(
    term_count: int,
) -> tuple[tuple[int, int], ...]:
    return tuple(
        pair
        for support in family_supports(term_count)
        for pair in combinations(support, 2)
    )


def second_koszul_column(
    pair: tuple[int, int],
    wedge: tuple[int, int],
) -> SparseVector:
    values: SparseVector = {}
    wedge_set = set(wedge)
    for offset, variable in enumerate(pair):
        if variable in wedge_set:
            continue
        output_variable = pair[1 - offset]
        output_wedge = tuple(sorted((variable,) + wedge))
        row = (
            output_variable * WEDGE_THREE_COUNT
            + WEDGE_THREE_INDEX[output_wedge]
        )
        values[row] = (
            values.get(row, 0) + insertion_sign(variable, wedge)
        ) % PRIME
    return {row: value for row, value in values.items() if value}


def common_factor_family_modular_rank(term_count: int) -> int:
    basis = family_second_derivative_basis(term_count)
    return sparse_rank_mod(
        second_koszul_column(pair, wedge)
        for pair in basis
        for wedge in WEDGE_TWO
    )


def common_factor_pair_intersection_dimension(n: int) -> int:
    return (n - 1) ** 2


def common_factor_family_exact_rank(term_count: int, n: int = N) -> int:
    single_rank = exact_independent_chow_second_koszul_rank(n)
    pair_loss = common_factor_pair_intersection_dimension(n)
    return single_rank * term_count - pair_loss * comb(term_count, 2)


def common_factor_family_homology_dimension(
    term_count: int,
    n: int = N,
) -> int:
    single_homology = independent_chow_quadratic_homology_dimension(n)
    pair_gain = common_factor_pair_intersection_dimension(n)
    return single_homology * term_count + pair_gain * comb(term_count, 2)


def family_payload(term_count: int) -> dict[str, int]:
    modular_rank = common_factor_family_modular_rank(term_count)
    exact_rank = common_factor_family_exact_rank(term_count)
    if modular_rank != exact_rank:
        raise AssertionError((term_count, modular_rank, exact_rank))

    derivative_dimension = comb(N, 2) * term_count
    domain_dimension = second_koszul_domain_dimension(
        derivative_dimension,
        VARIABLES,
    )
    preceding_rank = preceding_first_koszul_chow_rank(N) * term_count
    homology = common_factor_family_homology_dimension(term_count)
    if domain_dimension - preceding_rank - exact_rank != homology:
        raise AssertionError(term_count)

    return {
        "term_count": term_count,
        "active_variable_count": 1 + BLOCK_SIZE * term_count,
        "second_derivative_dimension": derivative_dimension,
        "second_koszul_domain_dimension": domain_dimension,
        "preceding_first_koszul_rank": preceding_rank,
        "modular_second_koszul_rank": modular_rank,
        "exact_characteristic_zero_second_koszul_rank": exact_rank,
        "exact_quadratic_homology_dimension": homology,
    }


def build_payload() -> dict[str, object]:
    permanent_homology = permanent_quadratic_homology_dimension(N)
    chow_homology = independent_chow_quadratic_homology_dimension(N)
    permanent_rank = exact_permanent_second_koszul_rank(N)
    chow_rank = exact_independent_chow_second_koszul_rank(N)
    family = [family_payload(term_count) for term_count in range(1, 7)]

    if permanent_homology != 450:
        raise AssertionError(permanent_homology)
    if chow_homology != 15:
        raise AssertionError(chow_homology)
    if permanent_rank != 127_125:
        raise AssertionError(permanent_rank)
    if chow_rank != 8_730:
        raise AssertionError(chow_rank)
    if ceil_div(permanent_rank, chow_rank) != 15:
        raise AssertionError((permanent_rank, chow_rank))

    expected_family_homology = [15, 55, 120, 210, 325, 465]
    observed_family_homology = [
        int(row["exact_quadratic_homology_dimension"])
        for row in family
    ]
    if observed_family_homology != expected_family_homology:
        raise AssertionError(observed_family_homology)
    if observed_family_homology[-1] <= permanent_homology:
        raise AssertionError(observed_family_homology[-1])

    return {
        "status": "N6_SECOND_KOSZUL_HOMOLOGY_CLOSED",
        "prime": PRIME,
        "literature_source": {
            "authors": "Jarod Alper and Rowan Rowlands",
            "title": (
                "Syzygies of the apolar ideals of the determinant and "
                "permanent"
            ),
            "arxiv": "1709.09286",
            "result": "Proposition 5.4",
            "formula": "beta_2_4=2*C(n,2)*C(n,4)",
            "verification_scope": (
                "The formula is treated as an external theorem; this audit "
                "checks its n=6 arithmetic and the resulting ranks."
            ),
        },
        "permanent": {
            "quadratic_homology_dimension_beta_2_4": permanent_homology,
            "second_koszul_domain_dimension": second_koszul_domain_dimension(
                comb(N, 2) ** 2,
                VARIABLES,
            ),
            "preceding_first_koszul_rank": (
                preceding_first_koszul_permanent_rank(N)
            ),
            "exact_characteristic_zero_second_koszul_rank": permanent_rank,
        },
        "single_independent_chow_term": {
            "quadratic_homology_dimension_beta_2_4": chow_homology,
            "second_koszul_domain_dimension": second_koszul_domain_dimension(
                comb(N, 2),
                VARIABLES,
            ),
            "preceding_first_koszul_rank": (
                preceding_first_koszul_chow_rank(N)
            ),
            "exact_characteristic_zero_second_koszul_rank": chow_rank,
        },
        "certified_integer_rank_ratio_lower_bound": ceil_div(
            permanent_rank,
            chow_rank,
        ),
        "common_factor_family": {
            "definition": (
                "T_i=c*product(B_i), where the five-element B_i are pairwise "
                "disjoint in the 36-dimensional ambient variable space."
            ),
            "pairwise_image_intersection_dimension": (
                common_factor_pair_intersection_dimension(N)
            ),
            "rows": family,
        },
        "route_decision": {
            "output_degree_two_rank_window": "closed_exactly",
            "base_rank_ratio": "no_improvement_over_15",
            "scalar_homology_dimension": (
                "rejected_as_a_standalone_lower_26_invariant"
            ),
            "multigraded_or_representation_structure": "open_not_promoted",
            "route_selected": "none",
        },
        "claim_boundary": (
            "The exact permanent homology dimension uses the published "
            "beta_2,4 formula for the apolar algebra. The common-factor rank "
            "formula is proved from coupled derivative-space isolation and "
            "explicit pairwise image intersections. The six-term example "
            "rejects only scalar homology dimension as a standalone lower-bound "
            "route; it does not rule out multigraded, representation-theoretic, "
            "or quotient-coupled homology obstructions."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_SECOND_KOSZUL_HOMOLOGY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
