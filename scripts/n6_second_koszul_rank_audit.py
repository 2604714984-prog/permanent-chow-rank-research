#!/usr/bin/env python3
"""Exact finite audit of the first higher-wedge Koszul ranks for ``perm_6``.

For output degrees ``m=2,3,4``, the script reconstructs

    delta_2: D_m(f) tensor Lambda^2(V)
             -> D_(m-1)(f) tensor Lambda^3(V)

for ``f=perm_6`` and for one independent six-factor Chow term. Matrices are
split by torus weight and ranked over ``F_1000003`` with sparse elimination.

A modular rank is used only as a characteristic-zero lower bound. The upper
bound is the domain dimension minus the already-proved rank of the preceding
first-Koszul image, because consecutive Koszul differentials compose to zero.
At ``m=3,4`` the bounds agree and give exact characteristic-zero ranks. At
``m=2`` the script records a rank window and does not promote the modular
value to an equality.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
from typing import Iterable

N = 6
VARIABLES = N * N
PRIME = 1_000_003
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
        vector = dict(raw)
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot] % prime
            if coefficient == 0:
                del vector[pivot]
                continue
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


def subpermanent_monomials(degree: int) -> tuple[tuple[int, ...], ...]:
    monomials: set[tuple[int, ...]] = set()
    for rows in combinations(range(N), degree):
        for columns in combinations(range(N), degree):
            for permuted in permutations(columns):
                monomials.add(
                    tuple(
                        sorted(
                            row * N + column
                            for row, column in zip(rows, permuted, strict=True)
                        )
                    )
                )
    return tuple(sorted(monomials))


def row_column_weight(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    wedge: tuple[int, int],
) -> tuple[int, ...]:
    row_weight = [0] * N
    column_weight = [0] * N
    for row in rows:
        row_weight[row] += 1
    for column in columns:
        column_weight[column] += 1
    for variable in wedge:
        row, column = divmod(variable, N)
        row_weight[row] += 1
        column_weight[column] += 1
    return tuple(row_weight + column_weight)


def canonical_weight(weight: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical labeled weight under independent row/column permutations."""

    return tuple(sorted(weight[:N])) + tuple(sorted(weight[N:]))


def weight_orbit_size(weight: tuple[int, ...]) -> int:
    """Size of the S_6 x S_6 orbit of one row-column weight."""

    size = 1
    for half in (weight[:N], weight[N:]):
        half_size = factorial(N)
        for multiplicity in Counter(half).values():
            half_size //= factorial(multiplicity)
        size *= half_size
    return size


def full_variable_weight(
    monomial: tuple[int, ...],
    wedge: tuple[int, int],
) -> tuple[int, ...]:
    weight = [0] * VARIABLES
    for variable in monomial:
        weight[variable] += 1
    for variable in wedge:
        weight[variable] += 1
    return tuple(weight)


def permanent_rank_audit(
    output_degree: int,
    *,
    orbit_compression: bool = True,
) -> dict[str, object]:
    row_subsets = tuple(combinations(range(N), output_degree))
    basis = tuple(
        (rows, columns)
        for rows in row_subsets
        for columns in row_subsets
    )
    output_monomials = subpermanent_monomials(output_degree - 1)
    monomial_index = {
        monomial: index for index, monomial in enumerate(output_monomials)
    }

    blocks: dict[
        tuple[int, ...],
        list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, int]]],
    ] = defaultdict(list)
    for rows, columns in basis:
        for wedge in WEDGE_TWO:
            weight = row_column_weight(rows, columns, wedge)
            if orbit_compression and weight != canonical_weight(weight):
                continue
            blocks[weight].append(
                (rows, columns, wedge)
            )

    represented_domain = sum(
        (weight_orbit_size(weight) if orbit_compression else 1)
        * len(descriptors)
        for weight, descriptors in blocks.items()
    )
    if represented_domain != len(basis) * len(WEDGE_TWO):
        raise AssertionError((represented_domain, len(basis) * len(WEDGE_TWO)))

    def column(
        descriptor: tuple[
            tuple[int, ...],
            tuple[int, ...],
            tuple[int, int],
        ]
    ) -> SparseVector:
        rows, columns, wedge = descriptor
        wedge_set = set(wedge)
        values: SparseVector = {}
        for row in rows:
            for column_value in columns:
                variable = row * N + column_value
                if variable in wedge_set:
                    continue
                remaining_rows = tuple(value for value in rows if value != row)
                remaining_columns = tuple(
                    value for value in columns if value != column_value
                )
                for permuted in permutations(remaining_columns):
                    monomial = tuple(
                        sorted(
                            current_row * N + current_column
                            for current_row, current_column in zip(
                                remaining_rows,
                                permuted,
                                strict=True,
                            )
                        )
                    )
                    output_wedge = tuple(sorted((variable,) + wedge))
                    row_id = (
                        monomial_index[monomial] * WEDGE_THREE_COUNT
                        + WEDGE_THREE_INDEX[output_wedge]
                    )
                    values[row_id] = (
                        values.get(row_id, 0)
                        + insertion_sign(variable, wedge)
                    ) % PRIME
        return {row: value for row, value in values.items() if value}

    total_rank = 0
    block_histogram: Counter[tuple[int, int]] = Counter()
    weight_block_count = 0
    for weight, descriptors in blocks.items():
        multiplicity = weight_orbit_size(weight) if orbit_compression else 1
        block_rank = sparse_rank_mod(column(value) for value in descriptors)
        total_rank += multiplicity * block_rank
        block_histogram[(len(descriptors), block_rank)] += multiplicity
        weight_block_count += multiplicity

    return {
        "basis_dimension": len(basis),
        "domain_dimension": len(basis) * len(WEDGE_TWO),
        "weight_block_count": weight_block_count,
        "maximum_block_column_count": max(map(len, blocks.values())),
        "modular_rank": total_rank,
        "block_histogram": {
            f"{columns}/{rank}": count
            for (columns, rank), count in sorted(block_histogram.items())
        },
    }


def chow_rank_audit(output_degree: int) -> dict[str, object]:
    active_variables = tuple(range(N))
    basis = tuple(combinations(active_variables, output_degree))
    output_monomials = tuple(
        combinations(active_variables, output_degree - 1)
    )
    monomial_index = {
        monomial: index for index, monomial in enumerate(output_monomials)
    }

    blocks: dict[
        tuple[int, ...],
        list[tuple[tuple[int, ...], tuple[int, int]]],
    ] = defaultdict(list)
    for monomial in basis:
        for wedge in WEDGE_TWO:
            blocks[full_variable_weight(monomial, wedge)].append(
                (monomial, wedge)
            )

    def column(
        descriptor: tuple[tuple[int, ...], tuple[int, int]]
    ) -> SparseVector:
        monomial, wedge = descriptor
        wedge_set = set(wedge)
        values: SparseVector = {}
        for variable in monomial:
            if variable in wedge_set:
                continue
            output_monomial = tuple(
                value for value in monomial if value != variable
            )
            output_wedge = tuple(sorted((variable,) + wedge))
            row_id = (
                monomial_index[output_monomial] * WEDGE_THREE_COUNT
                + WEDGE_THREE_INDEX[output_wedge]
            )
            values[row_id] = (
                values.get(row_id, 0)
                + insertion_sign(variable, wedge)
            ) % PRIME
        return {row: value for row, value in values.items() if value}

    total_rank = 0
    block_histogram: Counter[tuple[int, int]] = Counter()
    for descriptors in blocks.values():
        block_rank = sparse_rank_mod(column(value) for value in descriptors)
        total_rank += block_rank
        block_histogram[(len(descriptors), block_rank)] += 1

    return {
        "basis_dimension": len(basis),
        "domain_dimension": len(basis) * len(WEDGE_TWO),
        "weight_block_count": len(blocks),
        "maximum_block_column_count": max(map(len, blocks.values())),
        "modular_rank": total_rank,
        "block_histogram": {
            f"{columns}/{rank}": count
            for (columns, rank), count in sorted(block_histogram.items())
        },
    }


def first_koszul_permanent_rank(output_degree: int) -> int:
    return (
        VARIABLES * comb(N, output_degree) ** 2
        - comb(N, output_degree + 1) ** 2
    )


def first_koszul_chow_rank(output_degree: int) -> int:
    return (
        VARIABLES * comb(N, output_degree)
        - comb(N, output_degree + 1)
    )


def degree_payload(output_degree: int) -> dict[str, object]:
    permanent = permanent_rank_audit(output_degree)
    chow = chow_rank_audit(output_degree)

    preceding_permanent_rank = first_koszul_permanent_rank(
        output_degree + 1
    )
    preceding_chow_rank = first_koszul_chow_rank(output_degree + 1)
    permanent_upper = (
        int(permanent["domain_dimension"]) - preceding_permanent_rank
    )
    chow_upper = int(chow["domain_dimension"]) - preceding_chow_rank
    permanent_lower = int(permanent["modular_rank"])
    chow_lower = int(chow["modular_rank"])

    if permanent_lower > permanent_upper or chow_lower > chow_upper:
        raise AssertionError(
            (
                output_degree,
                permanent_lower,
                permanent_upper,
                chow_lower,
                chow_upper,
            )
        )

    exact = (
        permanent_lower == permanent_upper
        and chow_lower == chow_upper
    )
    ratio_lower = ceil_div(permanent_lower, chow_upper)
    first_ratio = ceil_div(
        first_koszul_permanent_rank(output_degree),
        first_koszul_chow_rank(output_degree),
    )

    return {
        "output_degree": output_degree,
        "permanent": permanent,
        "single_independent_chow_term": chow,
        "preceding_first_koszul_permanent_rank": preceding_permanent_rank,
        "preceding_first_koszul_chow_rank": preceding_chow_rank,
        "characteristic_zero_permanent_rank_window": [
            permanent_lower,
            permanent_upper,
        ],
        "characteristic_zero_chow_rank_window": [
            chow_lower,
            chow_upper,
        ],
        "rank_exact_in_characteristic_zero": exact,
        "certified_second_koszul_rank_ratio_lower_bound": ratio_lower,
        "first_koszul_integer_rank_ratio_lower_bound": first_ratio,
    }


def build_payload() -> dict[str, object]:
    degrees = [degree_payload(value) for value in (2, 3, 4)]
    expected = {
        2: {
            "permanent": [127_125, 127_575],
            "chow": [8_730, 8_745],
            "ratio": 15,
            "exact": False,
        },
        3: {
            "permanent": [243_936, 243_936],
            "chow": [12_066, 12_066],
            "ratio": 21,
            "exact": True,
        },
        4: {
            "permanent": [140_455, 140_455],
            "chow": [9_235, 9_235],
            "ratio": 16,
            "exact": True,
        },
    }
    for row in degrees:
        degree = int(row["output_degree"])
        target = expected[degree]
        if row["characteristic_zero_permanent_rank_window"] != target[
            "permanent"
        ]:
            raise AssertionError(row)
        if row["characteristic_zero_chow_rank_window"] != target["chow"]:
            raise AssertionError(row)
        if (
            row["certified_second_koszul_rank_ratio_lower_bound"]
            != target["ratio"]
        ):
            raise AssertionError(row)
        if row["rank_exact_in_characteristic_zero"] != target["exact"]:
            raise AssertionError(row)
        if (
            row["certified_second_koszul_rank_ratio_lower_bound"]
            != row["first_koszul_integer_rank_ratio_lower_bound"]
        ):
            raise AssertionError(row)

    return {
        "status": "N6_SECOND_KOSZUL_RANKS_REPLAYED",
        "prime": PRIME,
        "degrees": degrees,
        "route_decision": (
            "For output degrees 2, 3, and 4, the first higher-wedge "
            "Koszul rank ratio has exactly the same integer lower-bound "
            "ceiling as the ordinary first-Koszul ratio."
        ),
        "claim_boundary": (
            "The modular ranks are characteristic-zero lower bounds. "
            "Exactness is claimed only where the preceding-image upper "
            "bound agrees. The audit does not rule out higher wedge order, "
            "quotient refinements, or additional intersection geometry."
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
    print("N6_SECOND_KOSZUL_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
