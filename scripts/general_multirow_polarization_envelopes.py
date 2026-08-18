#!/usr/bin/env python3
"""Exact replay for the dyadic multirow Chow-envelope construction.

The proof is in ``docs/general_multirow_polarization_envelopes.md``.  The
script checks the Walsh-Fourier selector that extracts one occurrence of each
selected row, reconstructs the endpoint staircase, verifies Chow-envelope
factor counts, and freezes the theorem-facing payload with exact integers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
from typing import Iterable


EXPECTED_CORE_SHA256 = "88ff9229d4e176292d6211685aa3e7c901484904ea19d0578c01c073f195783e"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def sign_vectors(t: int) -> Iterable[tuple[int, ...]]:
    """Signs for rows 1,...,t-1, with the first row sign fixed to +1."""

    require(t >= 1, t)
    yield from product((-1, 1), repeat=t - 1)


def sign_for_row(epsilon: tuple[int, ...], row: int) -> int:
    return 1 if row == 0 else epsilon[row - 1]


def character(epsilon: tuple[int, ...]) -> int:
    value = 1
    for sign in epsilon:
        value *= sign
    return value


def selector_coefficient(t: int, assignment: tuple[int, ...]) -> Fraction:
    """Coefficient selected from prod_j ell_(epsilon,j).

    ``assignment[j]`` is the selected row in the factor belonging to column
    ``j``.  The normalized Walsh sum must be one exactly for bijections and
    zero otherwise.
    """

    require(len(assignment) == t, (t, assignment))
    require(all(0 <= row < t for row in assignment), (t, assignment))
    total = 0
    for epsilon in sign_vectors(t):
        term = character(epsilon)
        for row in assignment:
            term *= sign_for_row(epsilon, row)
        total += term
    return Fraction(total, 1 << (t - 1))


def weak_compositions(total: int, parts: int) -> Iterable[tuple[int, ...]]:
    """Generate all weak compositions in deterministic lexicographic order."""

    require(total >= 0 and parts >= 1, (total, parts))
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first, *tail)


def coefficient_from_counts(t: int, counts: tuple[int, ...]) -> Fraction:
    require(len(counts) == t and sum(counts) == t, (t, counts))
    total = 0
    for epsilon in sign_vectors(t):
        term = character(epsilon)
        for row, count in enumerate(counts):
            term *= sign_for_row(epsilon, row) ** count
        total += term
    return Fraction(total, 1 << (t - 1))


def threshold_degree(m: int, t: int) -> int:
    require(1 <= t <= m, (m, t))
    return m * (m - t + 1)


def dyadic_terms(t: int) -> int:
    require(t >= 1, t)
    return 1 << (t - 1)


def savings_from_terms(m: int, q: int) -> int:
    require(m >= 1 and q >= 1, (m, q))
    return min(m - 1, q.bit_length() - 1)


def construction_degree_for_terms(m: int, q: int) -> int:
    return m * (m - savings_from_terms(m, q))


def construction_terms_for_degree(n: int, m: int) -> int:
    """Dyadic term count supplied by the construction at order n/output m."""

    require(m <= n, (n, m))
    savings = max(0, m - n // m)
    savings = min(m - 1, savings)
    return 1 << savings


def verify_selector_counts(t_max: int = 9) -> dict[str, int]:
    count_vectors = 0
    sign_summands = 0
    for t in range(1, t_max + 1):
        observed = 0
        for counts in weak_compositions(t, t):
            coefficient = coefficient_from_counts(t, counts)
            expected = Fraction(1 if counts == (1,) * t else 0)
            require(coefficient == expected, (t, counts, coefficient, expected))
            count_vectors += 1
            sign_summands += 1 << (t - 1)
            observed += 1
        require(observed == comb(2 * t - 1, t - 1), (t, observed))
    return {
        "t_max": t_max,
        "count_vectors_checked": count_vectors,
        "walsh_summands_checked": sign_summands,
    }


def verify_assignments(t_max: int = 6) -> dict[str, int]:
    assignments = 0
    sign_summands = 0
    for t in range(1, t_max + 1):
        bijections = 0
        for assignment in product(range(t), repeat=t):
            coefficient = selector_coefficient(t, assignment)
            expected = Fraction(1 if len(set(assignment)) == t else 0)
            require(coefficient == expected, (t, assignment, coefficient, expected))
            assignments += 1
            sign_summands += 1 << (t - 1)
            if coefficient:
                bijections += 1
        require(bijections == factorial(t), (t, bijections))
    return {
        "assignment_t_max": t_max,
        "assignments_checked": assignments,
        "assignment_walsh_summands_checked": sign_summands,
    }


def verify_full_permanent_blocks(m_max: int = 6) -> dict[str, int]:
    """Expand the complete row-Laplace construction for small exact blocks.

    A monomial is encoded by the row selected in each matrix column.  The
    normalized envelope sum must retain exactly the permutations of
    ``range(m)`` with coefficient one.
    """

    block_pairs = 0
    expanded_terms = 0
    surviving_monomials = 0

    for m in range(1, m_max + 1):
        expected = {tuple(row_by_column) for row_by_column in permutations(range(m))}
        for t in range(1, m + 1):
            normalizer = 1 << (t - 1)
            polynomial: dict[tuple[int, ...], int] = defaultdict(int)
            selected_rows = tuple(range(t))
            tail_rows = tuple(range(t, m))

            for epsilon in sign_vectors(t):
                weight = character(epsilon)
                for selected_columns in combinations(range(m), t):
                    selected_set = set(selected_columns)
                    tail_columns = tuple(
                        column for column in range(m) if column not in selected_set
                    )
                    for selected_assignment in product(selected_rows, repeat=t):
                        selected_sign = weight
                        rows_by_column = [-1] * m
                        for column, row in zip(selected_columns, selected_assignment):
                            rows_by_column[column] = row
                            selected_sign *= sign_for_row(epsilon, row)
                        for tail_assignment in permutations(tail_rows):
                            monomial = rows_by_column.copy()
                            for column, row in zip(tail_columns, tail_assignment):
                                monomial[column] = row
                            polynomial[tuple(monomial)] += selected_sign
                            expanded_terms += 1

            observed = {
                monomial
                for monomial, coefficient in polynomial.items()
                if coefficient != 0
            }
            require(observed == expected, (m, t, len(observed), len(expected)))
            for monomial, coefficient in polynomial.items():
                expected_coefficient = normalizer if monomial in expected else 0
                require(
                    coefficient == expected_coefficient,
                    (m, t, monomial, coefficient, expected_coefficient),
                )
            block_pairs += 1
            surviving_monomials += len(observed)

    return {
        "full_block_m_max": m_max,
        "full_block_pairs_checked": block_pairs,
        "full_block_expanded_terms": expanded_terms,
        "full_block_surviving_monomials": surviving_monomials,
    }


def verify_staircase(m_max: int = 64) -> dict[str, object]:
    cells = 0
    inverse_checks = 0
    selected_rows: list[dict[str, int]] = []

    for m in range(1, m_max + 1):
        previous_degree = None
        for t in range(1, m + 1):
            q = dyadic_terms(t)
            n0 = threshold_degree(m, t)
            factors = m + m * (m - t)
            require(factors == n0, (m, t, factors, n0))
            require(n0 >= m, (m, t, n0))
            require(q == 1 << (t - 1), (m, t, q))
            if previous_degree is not None:
                require(previous_degree - n0 == m, (m, t, previous_degree, n0))
            previous_degree = n0
            cells += 1

            # At the exact staircase degree, inversion recovers the same
            # dyadic count.  At larger degrees it can only weakly improve.
            recovered = construction_terms_for_degree(n0, m)
            require(recovered == q, (m, t, n0, recovered, q))
            inverse_checks += 1

            if (m, t) in {
                (2, 1), (2, 2),
                (3, 1), (3, 2), (3, 3),
                (4, 1), (4, 2), (4, 3), (4, 4),
                (5, 2), (5, 3), (5, 5),
                (6, 2), (6, 3), (6, 4), (6, 6),
                (8, 2), (8, 4), (8, 8),
            }:
                selected_rows.append(
                    {
                        "m": m,
                        "selected_rows": t,
                        "dyadic_terms": q,
                        "first_constructed_degree": n0,
                        "factor_count_per_envelope": factors,
                        "monomials_per_envelope": factorial(m) // factorial(t),
                    }
                )

        # Endpoints: one coordinate envelope and the Glynn top-degree family.
        require(threshold_degree(m, 1) == m * m, m)
        require(dyadic_terms(1) == 1, m)
        require(threshold_degree(m, m) == m, m)
        require(dyadic_terms(m) == 1 << (m - 1), m)

    q_cells = 0
    for m in range(1, 65):
        for q in range(1, 1 << min(m, 10)):
            savings = savings_from_terms(m, q)
            degree = construction_degree_for_terms(m, q)
            require(0 <= savings <= m - 1, (m, q, savings))
            require(m <= degree <= m * m, (m, q, degree))
            require(dyadic_terms(savings + 1) <= q, (m, q, savings))
            if savings < m - 1:
                require(q < dyadic_terms(savings + 2), (m, q, savings))
            q_cells += 1

    return {
        "m_max": m_max,
        "staircase_cells_checked": cells,
        "degree_inverse_checks": inverse_checks,
        "arbitrary_q_cells_checked": q_cells,
        "selected_rows": selected_rows,
    }


def build_payload() -> dict[str, object]:
    selector_counts = verify_selector_counts()
    assignments = verify_assignments()
    full_blocks = verify_full_permanent_blocks()
    staircase = verify_staircase()

    core: dict[str, object] = {
        "status": [
            "GENERAL_MULTIROW_POLARIZATION_ENVELOPES",
            "DYADIC_NONZERO_STAIRCASE",
            "PAIR_CONSTRUCTION_EXTENDED_TO_GLYNN",
            "EXACT_INTEGER_AND_RATIONAL_REPLAYED",
        ],
        "theorem": {
            "parameters": "1<=t<=m<=n and q_t=2^(t-1)",
            "first_constructed_degree": "n_t=m*(m-t+1)",
            "fourier_identity": (
                "perm_m=2^(1-t)*sum_epsilon chi(epsilon)*G_epsilon, "
                "where epsilon ranges over {+-1}^{t-1}"
            ),
            "chow_envelopes": (
                "G_epsilon lies in D_m(T_epsilon), and T_epsilon has "
                "m*(m-t+1) independent linear factors"
            ),
            "extension": (
                "Multiplying every envelope by extra independent factors "
                "extends the same nonzero witness to all n>=m*(m-t+1)"
            ),
            "arbitrary_q": (
                "For s=min(m-1,floor(log2(q))), a q-term block is explicitly "
                "nonzero for every n>=m*(m-s)"
            ),
            "fixed_degree": (
                "For m<=n, the construction uses at most "
                "2^max(0,m-floor(n/m)) Chow derivative envelopes"
            ),
        },
        "exact_replay": {
            **selector_counts,
            **assignments,
            **full_blocks,
            **staircase,
        },
        "endpoints": {
            "t=1": "one coordinate envelope at n=m^2",
            "t=2": "the sharp two-term construction at n=m*(m-1)",
            "t=m": "the 2^(m-1)-term Glynn decomposition at n=m",
        },
        "claim_boundary": (
            "The theorem gives explicit nonzero literal derivative-space "
            "intersections. Except for the inherited one- and two-term "
            "endpoints, it does not prove that the displayed term count or "
            "degree threshold is minimal. It is not a new exact Chow-rank "
            "result for m>=6, does not improve a lower bound, makes no "
            "border-rank claim, and does not identify a literal sum with a "
            "coupled catalectic image. Literature novelty is not established."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


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
    print("GENERAL_MULTIROW_POLARIZATION_ENVELOPES_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
