#!/usr/bin/env python3
"""Exact audit of the standard Koszul--Young ceiling for ``perm_6``.

This is an exact matrix constructor followed by Gaussian elimination over the
prime field F_1000003.  Hence every reported modular rank is a rigorous lower
bound for the characteristic-zero rank of the same integer matrix.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import ceil, comb, factorial
from pathlib import Path


N = 6
VARIABLES = N * N
PRIME = 1_000_003

# These three entries are independently reconstructed by ``--replay-heavy``.
HEAVY_EXPECTED = {
    (5, 2): 22_644,
    (4, 3): 1_583_856,
    (2, 3): 1_347_444,
}

HEAVY_CERTIFICATES = {
    (5, 2): {
        "domain_dimension": 22_680,
        "weight_block_count": 8_316,
        "maximum_block_column_count": 60,
        "modular_rank": 22_644,
        "histogram_entries": 5,
    },
    (4, 3): {
        "domain_dimension": 1_606_500,
        "weight_block_count": 128_016,
        "maximum_block_column_count": 925,
        "modular_rank": 1_583_856,
        "histogram_entries": 16,
    },
    (2, 3): {
        "domain_dimension": 1_606_500,
        "weight_block_count": 54_216,
        "maximum_block_column_count": 600,
        "modular_rank": 1_347_444,
        "histogram_entries": 17,
    },
}


def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def sparse_rank_mod(columns, prime: int = PRIME) -> int:
    pivots = {}
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


def sparse_rank_fraction(columns) -> int:
    """Rank a small sparse integer matrix exactly over Q."""

    pivots = {}
    rank = 0
    for raw in columns:
        vector = {row: Fraction(value) for row, value in raw.items() if value}
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                vector = {
                    row: value / coefficient for row, value in vector.items()
                }
                pivots[pivot] = vector
                rank += 1
                break
            for row, value in existing.items():
                updated = vector.get(row, Fraction(0)) - coefficient * value
                if updated:
                    vector[row] = updated
                else:
                    vector.pop(row, None)
    return rank


def row_column_weight(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    wedge: tuple[int, ...],
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
    """Canonical representative under independent row/column permutations."""

    return tuple(sorted(weight[:N])) + tuple(sorted(weight[N:]))


def weight_orbit_size(weight: tuple[int, ...]) -> int:
    """Exact size of the S_6 x S_6 orbit of one weight block."""

    size = 1
    for half in (weight[:N], weight[N:]):
        half_size = factorial(N)
        for multiplicity in Counter(half).values():
            half_size //= factorial(multiplicity)
        size *= half_size
    return size


def descriptor_blocks(
    output_degree: int,
    wedge_degree: int,
    *,
    orbit_compression: bool,
):
    subsets = tuple(combinations(range(N), output_degree))
    wedges = tuple(combinations(range(VARIABLES), wedge_degree))
    blocks = defaultdict(list)
    for rows in subsets:
        for columns in subsets:
            for wedge in wedges:
                weight = row_column_weight(rows, columns, wedge)
                if orbit_compression and weight != canonical_weight(weight):
                    continue
                blocks[weight].append(
                    (rows, columns, wedge)
                )
    return blocks


def permanent_rank(
    output_degree: int,
    wedge_degree: int,
    *,
    orbit_compression: bool = True,
) -> dict[str, int]:
    subsets = tuple(combinations(range(N), output_degree))
    wedges = tuple(combinations(range(VARIABLES), wedge_degree))
    domain_dimension = len(subsets) ** 2 * len(wedges)
    blocks = descriptor_blocks(
        output_degree,
        wedge_degree,
        orbit_compression=orbit_compression,
    )
    represented_domain = sum(
        (weight_orbit_size(weight) if orbit_compression else 1)
        * len(descriptors)
        for weight, descriptors in blocks.items()
    )
    if represented_domain != domain_dimension:
        raise AssertionError((represented_domain, domain_dimension))

    total_rank = 0
    histogram = Counter()
    represented_block_count = 0
    for weight, descriptors in blocks.items():
        multiplicity = weight_orbit_size(weight) if orbit_compression else 1
        represented_block_count += multiplicity

        def block_columns():
            for rows, columns, wedge in descriptors:
                wedge_set = set(wedge)
                values = {}
                for row in rows:
                    for column in columns:
                        variable = row * N + column
                        if variable in wedge_set:
                            continue
                        output_rows = tuple(x for x in rows if x != row)
                        output_columns = tuple(x for x in columns if x != column)
                        output_wedge = tuple(sorted((variable,) + wedge))
                        row_key = (output_rows, output_columns, output_wedge)
                        values[row_key] = (
                            values.get(row_key, 0)
                            + insertion_sign(variable, wedge)
                        ) % PRIME
                yield {key: value for key, value in values.items() if value}

        block_rank = sparse_rank_mod(block_columns())
        total_rank += multiplicity * block_rank
        histogram[(len(descriptors), block_rank)] += multiplicity

    return {
        "domain_dimension": domain_dimension,
        "weight_block_count": represented_block_count,
        "maximum_block_column_count": max(map(len, blocks.values())),
        "modular_rank": total_rank,
        "histogram_entries": len(histogram),
    }


def coordinate_term_internal_rank(
    output_degree: int,
    wedge_degree: int,
) -> int:
    """Exact rank inside the six-dimensional factor span of a Chow term."""

    monomials = tuple(combinations(range(N), output_degree))
    wedges = tuple(combinations(range(N), wedge_degree))

    def matrix_columns():
        for monomial in monomials:
            for wedge in wedges:
                wedge_set = set(wedge)
                values = {}
                for variable in monomial:
                    if variable in wedge_set:
                        continue
                    output_monomial = tuple(
                        entry for entry in monomial if entry != variable
                    )
                    output_wedge = tuple(sorted((variable,) + wedge))
                    row = (output_monomial, output_wedge)
                    values[row] = values.get(row, 0) + insertion_sign(
                        variable,
                        wedge,
                    )
                yield values

    return sparse_rank_fraction(matrix_columns())


def internal_rank_table() -> dict[int, list[int]]:
    return {
        output_degree: [
            coordinate_term_internal_rank(output_degree, wedge_degree)
            for wedge_degree in range(N + 1)
        ]
        for output_degree in range(1, N + 1)
    }


def ambient_term_rank(
    output_degree: int,
    wedge_degree: int,
    internal: dict[int, list[int]],
) -> int:
    """Maximum rank of one degree-six Chow term in 36 variables."""

    inactive = VARIABLES - N
    return sum(
        comb(inactive, inactive_wedge)
        * internal[output_degree][wedge_degree - inactive_wedge]
        for inactive_wedge in range(
            max(0, wedge_degree - N),
            min(inactive, wedge_degree) + 1,
        )
        if 0 <= wedge_degree - inactive_wedge <= N
    )


def permanent_dimension_upper(output_degree: int, wedge_degree: int) -> int:
    return min(
        comb(N, output_degree) ** 2 * comb(VARIABLES, wedge_degree),
        comb(N, output_degree - 1) ** 2
        * comb(VARIABLES, wedge_degree + 1),
    )


def exterior_shadow_lower(
    rank: int,
    source_wedge_degree: int,
    target_wedge_degree: int,
) -> int:
    """Double-counting lower bound for an exterior upper shadow."""

    value = Fraction(
        rank
        * comb(
            VARIABLES - source_wedge_degree,
            target_wedge_degree - source_wedge_degree,
        ),
        comb(target_wedge_degree, source_wedge_degree),
    )
    return ceil(value)


def candidate_upper_rows(internal: dict[int, list[int]]) -> list[dict[str, int | str]]:
    """Refine the only five cases up to transpose duality."""

    rows = []
    for wedge_degree in range(10, 15):
        term_rank = ambient_term_rank(3, wedge_degree, internal)
        if wedge_degree == 10:
            side = "domain"
            shadow_rank = exterior_shadow_lower(8_064, 2, wedge_degree)
            ambient_dimension = (
                comb(N, 3) ** 2 * comb(VARIABLES, wedge_degree)
            )
            source = "exact rank delta_(4,1)=8064"
        elif wedge_degree == 11:
            side = "domain"
            shadow_rank = exterior_shadow_lower(
                HEAVY_EXPECTED[(4, 3)],
                4,
                wedge_degree,
            )
            ambient_dimension = (
                comb(N, 3) ** 2 * comb(VARIABLES, wedge_degree)
            )
            source = "exact rank delta_(4,3)=1583856"
        elif wedge_degree == 12:
            side = "target"
            shadow_rank = exterior_shadow_lower(
                HEAVY_EXPECTED[(2, 3)],
                4,
                wedge_degree + 2,
            )
            ambient_dimension = (
                comb(N, 2) ** 2 * comb(VARIABLES, wedge_degree + 1)
            )
            source = "modular lower rank delta_(2,3)>=1347444"
        else:
            side = "target"
            shadow_rank = exterior_shadow_lower(
                7_700,
                2,
                wedge_degree + 2,
            )
            ambient_dimension = (
                comb(N, 2) ** 2 * comb(VARIABLES, wedge_degree + 1)
            )
            source = "exact rank delta_(2,1)=7700"

        rank_upper = ambient_dimension - shadow_rank
        ceiling_margin = 26 * term_rank - rank_upper
        if ceiling_margin <= 0:
            raise AssertionError((wedge_degree, rank_upper, term_rank))
        rows.append(
            {
                "output_degree": 3,
                "wedge_degree": wedge_degree,
                "bounding_side": side,
                "shadow_source": source,
                "shadow_rank_lower": shadow_rank,
                "permanent_rank_upper": rank_upper,
                "single_term_rank": term_rank,
                "margin_below_26_terms": ceiling_margin,
            }
        )
    return rows


def build_payload(replay_heavy: bool) -> dict[str, object]:
    internal = internal_rank_table()
    expected_internal = {
        1: [6, 15, 20, 15, 6, 1, 0],
        2: [15, 70, 105, 84, 35, 6, 0],
        3: [20, 105, 216, 190, 84, 15, 0],
        4: [15, 84, 190, 216, 105, 20, 0],
        5: [6, 35, 84, 105, 70, 15, 0],
        6: [1, 6, 15, 20, 15, 6, 0],
    }
    if internal != expected_internal:
        raise AssertionError(internal)

    heavy = {}
    if replay_heavy:
        for key in HEAVY_EXPECTED:
            result = permanent_rank(*key)
            if result != HEAVY_CERTIFICATES[key]:
                raise AssertionError((key, result))
            heavy[f"m{key[0]}_p{key[1]}"] = result

    # Exactness of the two ranks used as equalities follows from delta^2=0.
    if HEAVY_EXPECTED[(5, 2)] != 36 * comb(VARIABLES, 2) - 36:
        raise AssertionError("delta_(5,2) exact upper mismatch")
    if (
        HEAVY_EXPECTED[(4, 3)]
        != comb(N, 4) ** 2 * comb(VARIABLES, 3)
        - HEAVY_EXPECTED[(5, 2)]
    ):
        raise AssertionError("delta_(4,3) exact upper mismatch")

    raw_candidates = []
    noncandidate_max = Fraction(0)
    for output_degree in range(1, N + 1):
        for wedge_degree in range(VARIABLES):
            term_rank = ambient_term_rank(
                output_degree,
                wedge_degree,
                internal,
            )
            if not term_rank:
                continue
            raw_upper = permanent_dimension_upper(
                output_degree,
                wedge_degree,
            )
            ratio = Fraction(raw_upper, term_rank)
            if ratio > 26:
                raw_candidates.append((output_degree, wedge_degree))
            else:
                noncandidate_max = max(noncandidate_max, ratio)

    expected_candidates = [
        (3, value) for value in range(10, 15)
    ] + [
        (4, value) for value in range(21, 26)
    ]
    if raw_candidates != expected_candidates:
        raise AssertionError(raw_candidates)

    refined = candidate_upper_rows(internal)
    refined_max = max(
        Fraction(row["permanent_rank_upper"], row["single_term_rank"])
        for row in refined
    )
    global_ratio_upper = max(noncandidate_max, refined_max)
    if global_ratio_upper >= 26:
        raise AssertionError(global_ratio_upper)

    return {
        "status": "N6_ALL_STANDARD_KOSZUL_YOUNG_CEILING_REPLAYED",
        "prime": PRIME,
        "internal_coordinate_term_ranks": internal,
        "raw_dimension_candidates_above_26": [
            {"output_degree": m, "wedge_degree": p}
            for m, p in raw_candidates
        ],
        "transpose_duality": "(m,p) <-> (7-m,35-p)",
        "refined_representatives": refined,
        "noncandidate_max_ratio": [
            noncandidate_max.numerator,
            noncandidate_max.denominator,
        ],
        "global_strict_ratio_upper": [
            global_ratio_upper.numerator,
            global_ratio_upper.denominator,
        ],
        "heavy_replay_performed": replay_heavy,
        "heavy_certificate_summaries": {
            f"m{key[0]}_p{key[1]}": value
            for key, value in HEAVY_CERTIFICATES.items()
        },
        "heavy_replay": heavy,
        "theorem": (
            "Every standard Koszul--Young flattening of perm_6 has rank "
            "strictly less than 26 times the maximum rank of one Chow term; "
            "therefore this entire family cannot certify Chow rank at least 27."
        ),
        "claim_boundary": (
            "This is a route ceiling, not an upper bound on ChowRank(perm_6). "
            "The ordinary interval remains 26 <= ChowRank(perm_6) <= 32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-heavy", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.replay_heavy)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_ALL_STANDARD_KOSZUL_YOUNG_CEILING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
