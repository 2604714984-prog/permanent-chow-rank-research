#!/usr/bin/env python3
"""Exact modular certificate for a full quotient Koszul gain at ``n=6``.

The chosen Chow term is the diagonal monomial

    T = x_00 x_11 x_22 x_33 x_44 x_55.

Its central derivative space has dimension 20 and is derivative-transverse to
the permanent central derivative space. The script rebuilds the first-Koszul
columns from definitions and proves that the combined image rank is
``14,175 + 705 = 14,880`` modulo ``1,000,003``. Subadditivity supplies the
matching characteristic-zero upper bound, so the quotient gain is exactly 705.

This is an existence and route diagnostic. It is not a uniform statement for
all Chow terms and does not improve the current universal ``n=6`` lower bound
by itself.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable

N = 6
VARIABLES = N * N
PRIME = 1_000_003
Monomial = tuple[int, int, int]
SparseColumn = dict[int, int]


def require_equal(label: str, actual: int, expected: int) -> None:
    """Fail closed when a proof-relevant exact invariant changes."""
    if actual != expected:
        raise RuntimeError(
            f"{label} mismatch: expected {expected}, observed {actual}"
        )


def triples() -> list[tuple[int, int, int]]:
    return list(combinations(range(N), 3))


def build_pair_maps() -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
    sym: dict[tuple[int, int], int] = {}
    index = 0
    for a in range(VARIABLES):
        for b in range(a, VARIABLES):
            sym[(a, b)] = index
            index += 1

    wedge: dict[tuple[int, int], int] = {}
    index = 0
    for a in range(VARIABLES):
        for b in range(a + 1, VARIABLES):
            wedge[(a, b)] = index
            index += 1

    require_equal("symmetric-pair basis dimension", len(sym), 666)
    require_equal("exterior-pair basis dimension", len(wedge), 630)
    return sym, wedge


def permanent_basis_monomials(
    rows: tuple[int, int, int],
    columns: tuple[int, int, int],
) -> list[Monomial]:
    out: list[Monomial] = []
    for sigma in permutations(range(3)):
        monomial = tuple(sorted(rows[i] * N + columns[sigma[i]] for i in range(3)))
        out.append(monomial)
    return out


def delta_column(
    monomials: Iterable[Monomial],
    tensor_variable: int,
    sym_index: dict[tuple[int, int], int],
    wedge_index: dict[tuple[int, int], int],
) -> SparseColumn:
    entries: Counter[int] = Counter()
    for monomial in monomials:
        for position, variable in enumerate(monomial):
            if variable == tensor_variable:
                continue
            remaining = [monomial[i] for i in range(3) if i != position]
            remaining.sort()
            a, b = sorted((variable, tensor_variable))
            sign = 1 if variable < tensor_variable else -1
            row = sym_index[(remaining[0], remaining[1])] * 630 + wedge_index[(a, b)]
            entries[row] += sign
    return {row: value % PRIME for row, value in entries.items() if value % PRIME}


def add_column_to_echelon(
    raw_column: SparseColumn,
    pivots: dict[int, SparseColumn],
) -> bool:
    column = dict(raw_column)
    while column:
        pivot = min(column)
        if pivot not in pivots:
            inverse = pow(column[pivot], PRIME - 2, PRIME)
            normalized = {
                row: value * inverse % PRIME
                for row, value in column.items()
                if value * inverse % PRIME
            }
            pivots[pivot] = normalized
            return True

        factor = column[pivot]
        for row, value in pivots[pivot].items():
            updated = (column.get(row, 0) - factor * value) % PRIME
            if updated:
                column[row] = updated
            else:
                column.pop(row, None)
    return False


def add_space(
    basis: Iterable[list[Monomial]],
    pivots: dict[int, SparseColumn],
    sym_index: dict[tuple[int, int], int],
    wedge_index: dict[tuple[int, int], int],
) -> int:
    gain = 0
    for polynomial in basis:
        for tensor_variable in range(VARIABLES):
            if add_column_to_echelon(
                delta_column(polynomial, tensor_variable, sym_index, wedge_index),
                pivots,
            ):
                gain += 1
    return gain


def build_payload() -> dict[str, object]:
    sym_index, wedge_index = build_pair_maps()
    matching_basis = [
        permanent_basis_monomials(rows, columns)
        for rows in triples()
        for columns in triples()
    ]
    diagonal_variables = [i * N + i for i in range(N)]
    diagonal_basis = [
        [tuple(chosen)]
        for chosen in combinations(diagonal_variables, 3)
    ]

    require_equal("permanent central dimension", len(matching_basis), 400)
    require_equal("diagonal-term central dimension", len(diagonal_basis), 20)

    pivots: dict[int, SparseColumn] = {}
    permanent_rank = add_space(matching_basis, pivots, sym_index, wedge_index)
    quotient_gain = add_space(diagonal_basis, pivots, sym_index, wedge_index)
    combined_rank = len(pivots)

    separate_pivots: dict[int, SparseColumn] = {}
    term_rank = add_space(diagonal_basis, separate_pivots, sym_index, wedge_index)

    require_equal("permanent Koszul rank modulo prime", permanent_rank, 14_175)
    require_equal("diagonal-term Koszul rank modulo prime", term_rank, 705)
    require_equal("quotient Koszul gain modulo prime", quotient_gain, 705)
    require_equal("combined Koszul rank modulo prime", combined_rank, 14_880)

    return {
        "status": "COMPUTATION_REPLAYED",
        "prime": PRIME,
        "permanent_central_dimension": 400,
        "diagonal_term_central_dimension": 20,
        "permanent_koszul_rank_mod_prime": permanent_rank,
        "diagonal_term_koszul_rank_mod_prime": term_rank,
        "combined_koszul_rank_mod_prime": combined_rank,
        "quotient_koszul_gain_mod_prime": quotient_gain,
        "characteristic_zero_conclusion": {
            "permanent_koszul_rank": 14_175,
            "diagonal_term_koszul_rank": 705,
            "combined_koszul_rank": 14_880,
            "quotient_koszul_gain": 705,
        },
        "claim_boundary": (
            "The full gain is proved for this explicit diagonal Chow term only. "
            "No uniform lower bound for arbitrary terms or term sums is claimed."
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
    print("N6_QUOTIENT_GAIN_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
