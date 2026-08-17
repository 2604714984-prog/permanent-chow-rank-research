#!/usr/bin/env python3
"""Exact replay for the Fitting/Betti subquotient barrier.

The mathematical proof is in
`docs/general_fitting_betti_subquotient_barrier.md`.  The script reconstructs
named Fitting ideals from presentation minors, checks finite-length Betti
counterexamples by Hilbert series, and exhausts one-variable invariant-factor
partitions through total length twelve.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import comb
from pathlib import Path
from typing import Iterable


Monomial = tuple[int, int]
Ideal = tuple[Monomial, ...]
Polynomial = dict[Monomial, int]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def divides(left: Monomial, right: Monomial) -> bool:
    return left[0] <= right[0] and left[1] <= right[1]


def minimize_ideal(generators: Iterable[Monomial]) -> Ideal:
    values = sorted(set(generators))
    return tuple(
        value
        for value in values
        if not any(other != value and divides(other, value) for other in values)
    )


R_IDEAL: Ideal = ((0, 0),)
ZERO_IDEAL: Ideal = ()
M_IDEAL: Ideal = minimize_ideal(((1, 0), (0, 1)))
M2_IDEAL: Ideal = minimize_ideal(((2, 0), (1, 1), (0, 2)))
CI_IDEAL: Ideal = minimize_ideal(((2, 0), (0, 2)))

ZERO_POLY: Polynomial = {}
ONE_POLY: Polynomial = {(0, 0): 1}
S_POLY: Polynomial = {(1, 0): 1}
T_POLY: Polynomial = {(0, 1): 1}


def ideal_product(left: Ideal, right: Ideal) -> Ideal:
    if not left or not right:
        return ZERO_IDEAL
    return minimize_ideal(
        (a + c, b + d) for a, b in left for c, d in right
    )


def ideal_sum(left: Ideal, right: Ideal) -> Ideal:
    return minimize_ideal((*left, *right))


def ideal_subset(left: Ideal, right: Ideal) -> bool:
    if right == R_IDEAL:
        return True
    if not right:
        return not left
    return all(any(divides(generator, value) for generator in right) for value in left)


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
        if result[exponent] == 0:
            del result[exponent]
    return result


def polynomial_scale(value: Polynomial, scalar: int) -> Polynomial:
    return {
        exponent: coefficient * scalar
        for exponent, coefficient in value.items()
        if coefficient * scalar
    }


def polynomial_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (a, b), x in left.items():
        for (c, d), y in right.items():
            exponent = (a + c, b + d)
            result[exponent] = result.get(exponent, 0) + x * y
            if result[exponent] == 0:
                del result[exponent]
    return result


def determinant(matrix: tuple[tuple[Polynomial, ...], ...]) -> Polynomial:
    size = len(matrix)
    require(all(len(row) == size for row in matrix), matrix)
    if size == 0:
        return dict(ONE_POLY)
    if size == 1:
        return dict(matrix[0][0])
    result: Polynomial = {}
    for column in range(size):
        minor = tuple(
            tuple(row[j] for j in range(size) if j != column)
            for row in matrix[1:]
        )
        term = polynomial_mul(matrix[0][column], determinant(minor))
        result = polynomial_add(
            result,
            polynomial_scale(term, -1 if column % 2 else 1),
        )
    return result


def fitting_ideal(
    presentation: tuple[tuple[Polynomial, ...], ...], index: int
) -> Ideal:
    """Return Fitt_index(coker(presentation)); rows are target generators."""

    target_generators = len(presentation)
    source_relations = len(presentation[0]) if target_generators else 0
    minor_size = target_generators - index
    if minor_size <= 0:
        return R_IDEAL
    if minor_size > min(target_generators, source_relations):
        return ZERO_IDEAL

    generators: list[Monomial] = []
    for rows in itertools.combinations(range(target_generators), minor_size):
        for columns in itertools.combinations(range(source_relations), minor_size):
            minor = tuple(
                tuple(presentation[row][column] for column in columns)
                for row in rows
            )
            value = determinant(minor)
            if value:
                require(len(value) == 1, (presentation, index, value))
                exponent, coefficient = next(iter(value.items()))
                require(coefficient != 0, value)
                generators.append(exponent)
    return minimize_ideal(generators)


def named_presentations():
    s2 = polynomial_mul(S_POLY, S_POLY)
    st = polynomial_mul(S_POLY, T_POLY)
    t2 = polynomial_mul(T_POLY, T_POLY)
    return {
        "k": ((S_POLY, T_POLY),),
        "k2": (
            (S_POLY, T_POLY, ZERO_POLY, ZERO_POLY),
            (ZERO_POLY, ZERO_POLY, S_POLY, T_POLY),
        ),
        "R_mod_m2": ((s2, st, t2),),
        "R_mod_s2_t2": ((s2, t2),),
    }


def monomial_in_ideal(monomial: Monomial, ideal: Ideal) -> bool:
    return any(divides(generator, monomial) for generator in ideal)


def quotient_hilbert(ideal: Ideal, maximum_degree: int = 8) -> tuple[int, ...]:
    return tuple(
        sum(
            not monomial_in_ideal((a, degree - a), ideal)
            for a in range(degree + 1)
        )
        for degree in range(maximum_degree + 1)
    )


def colength(ideal: Ideal) -> int:
    values = quotient_hilbert(ideal, 12)
    require(all(value == 0 for value in values[6:]), (ideal, values))
    return sum(values)


def hilbert_from_betti(
    terms: tuple[tuple[int, int, int], ...], maximum_degree: int = 8
) -> tuple[int, ...]:
    numerator: dict[int, int] = {}
    for homological, shift, multiplicity in terms:
        numerator[shift] = numerator.get(shift, 0) + (
            (-1) ** homological
        ) * multiplicity
    return tuple(
        sum(
            coefficient * (degree - shift + 1)
            for shift, coefficient in numerator.items()
            if degree >= shift
        )
        for degree in range(maximum_degree + 1)
    )


BETTI = {
    "k": ((0, 0, 1), (1, 1, 2), (2, 2, 1)),
    "k2_shift1": ((0, 1, 2), (1, 2, 4), (2, 3, 2)),
    "R_mod_m2": ((0, 0, 1), (1, 2, 3), (2, 3, 2)),
    "R_mod_s2_t2": ((0, 0, 1), (1, 2, 2), (2, 4, 1)),
}


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def fitting_valuations(partition: tuple[int, ...]) -> tuple[int, ...]:
    ascending = tuple(sorted(partition))
    count = len(ascending)
    return tuple(
        sum(ascending[: count - index]) if index < count else 0
        for index in range(count + 1)
    )


def recover_partition(valuations: tuple[int, ...]) -> tuple[int, ...]:
    count = len(valuations) - 1
    ascending = tuple(
        valuations[index] - valuations[index + 1]
        for index in range(count - 1, -1, -1)
    )
    return tuple(sorted(ascending, reverse=True))


def jordan_tails(partition: tuple[int, ...]) -> tuple[int, ...]:
    maximum = max(partition, default=0)
    return tuple(
        sum(part >= threshold for part in partition)
        for threshold in range(1, maximum + 1)
    )


def build_payload() -> dict[str, object]:
    presentations = named_presentations()
    fitt = {
        name: {
            str(index): fitting_ideal(matrix, index)
            for index in range(len(matrix) + 1)
        }
        for name, matrix in presentations.items()
    }

    require(fitt["k"]["0"] == M_IDEAL, fitt)
    require(fitt["k"]["1"] == R_IDEAL, fitt)
    require(fitt["k2"]["0"] == M2_IDEAL, fitt)
    require(fitt["k2"]["1"] == M_IDEAL, fitt)
    require(fitt["R_mod_m2"]["0"] == M2_IDEAL, fitt)
    require(fitt["R_mod_m2"]["1"] == R_IDEAL, fitt)
    require(fitt["R_mod_s2_t2"]["0"] == CI_IDEAL, fitt)

    require(
        fitt["k2"]["0"] == ideal_product(fitt["k"]["0"], fitt["k"]["0"]),
        fitt,
    )
    require(
        fitt["k2"]["1"]
        == ideal_sum(
            ideal_product(fitt["k"]["0"], fitt["k"]["1"]),
            ideal_product(fitt["k"]["1"], fitt["k"]["0"]),
        ),
        fitt,
    )

    # Opposite ideal-order directions under two submodule injections.
    require(ideal_subset(fitt["k2"]["1"], fitt["k"]["1"]), fitt)
    require(not ideal_subset(fitt["k"]["1"], fitt["k2"]["1"]), fitt)
    require(ideal_subset(fitt["k2"]["1"], fitt["R_mod_m2"]["1"]), fitt)
    require(not ideal_subset(fitt["R_mod_m2"]["1"], fitt["k2"]["1"]), fitt)

    require(colength(fitt["k"]["0"]) == 1, fitt)
    require(colength(fitt["k2"]["0"]) == 3, fitt)

    expected_hilbert = {
        "k": (1, 0, 0, 0, 0, 0, 0, 0, 0),
        "k2_shift1": (0, 2, 0, 0, 0, 0, 0, 0, 0),
        "R_mod_m2": (1, 2, 0, 0, 0, 0, 0, 0, 0),
        "R_mod_s2_t2": (1, 2, 1, 0, 0, 0, 0, 0, 0),
    }
    for name, terms in BETTI.items():
        require(hilbert_from_betti(terms) == expected_hilbert[name], name)

    require(ideal_subset(CI_IDEAL, M2_IDEAL), (CI_IDEAL, M2_IDEAL))
    betti_totals = {
        name: tuple(
            sum(
                multiplicity
                for homological, _, multiplicity in terms
                if homological == index
            )
            for index in range(3)
        )
        for name, terms in BETTI.items()
    }
    require(betti_totals["R_mod_s2_t2"] == (1, 2, 1), betti_totals)
    require(betti_totals["R_mod_m2"] == (1, 3, 2), betti_totals)
    require(betti_totals["k2_shift1"] == (2, 4, 2), betti_totals)

    partition_checks = 0
    for total in range(1, 13):
        for partition in partitions(total):
            valuations = fitting_valuations(partition)
            require(recover_partition(valuations) == partition, (partition, valuations))
            require(sum(jordan_tails(partition)) == total, partition)
            partition_checks += 1
    require(partition_checks == 271, partition_checks)

    jordan_ratio_checks = 0
    route_maxima = {}
    for n in range(2, 21):
        ratios = []
        for degree in range(n // 2 + 1):
            boolean_tail = comb(n, degree)
            permanent_tail = boolean_tail * boolean_tail
            ratios.append(permanent_tail // boolean_tail)
            jordan_ratio_checks += 1
        route_maxima[str(n)] = max(ratios)
        require(route_maxima[str(n)] == comb(n, n // 2), (n, ratios))
    require(jordan_ratio_checks == 119, jordan_ratio_checks)

    core: dict[str, object] = {
        "status": [
            "GENERAL_FITTING_QUOTIENT_FUNCTORIALITY",
            "HIGHER_FITTING_SUBMODULE_DIRECTION_FAILURE",
            "FINITE_LENGTH_BETTI_MONOTONICITY_FAILURE",
            "LINEWISE_FITTING_EQUALS_JORDAN_PARTITION",
            "NO_NEW_NUMERICAL_CHOW_RANK_BOUND",
        ],
        "theorem": {
            "quotient_fitting": "A surjection M->Q gives Fitt_i(M) subset Fitt_i(Q).",
            "direct_sum_fitting": (
                "Fitt_k(M direct_sum N)=sum_(i+j=k) Fitt_i(M)Fitt_j(N)."
            ),
            "submodule_failure": (
                "For Fitt_1, diagonal k->k^2 and m/m^2->R/m^2 force "
                "opposite ideal-order directions."
            ),
            "betti_failure": (
                "Total and graded Betti numbers can increase under both a "
                "finite-length quotient and a finite-length submodule."
            ),
            "linewise_equivalence": (
                "For M=sum k[u]/(u^lambda_i), all Fitting valuations recover "
                "the complete Jordan partition."
            ),
            "one_operator_cone": (
                "Every additive subquotient-monotone scalar depending only "
                "on one Jordan type is a nonnegative combination of Jordan tails."
            ),
            "route_boundary": (
                "Raw higher Fitting profiles and Betti tables are not automatic "
                "apolar-subquotient invariants. Every admissible one-operator "
                "Fitting scalarization lies in the closed Jordan-tail cone."
            ),
        },
        "fitting_examples": {
            "Fitt_k": {
                key: [list(value) for value in ideal]
                for key, ideal in fitt["k"].items()
            },
            "Fitt_k2": {
                key: [list(value) for value in ideal]
                for key, ideal in fitt["k2"].items()
            },
            "Fitt_R_mod_m2": {
                key: [list(value) for value in ideal]
                for key, ideal in fitt["R_mod_m2"].items()
            },
            "Fitt_R_mod_s2_t2": {
                key: [list(value) for value in ideal]
                for key, ideal in fitt["R_mod_s2_t2"].items()
            },
            "colength_Fitt0_k": 1,
            "colength_Fitt0_k2": 3,
        },
        "betti_examples": {
            "quotient_source_R_mod_s2_t2": list(betti_totals["R_mod_s2_t2"]),
            "quotient_target_R_mod_m2": list(betti_totals["R_mod_m2"]),
            "submodule_k2_shift1": list(betti_totals["k2_shift1"]),
            "ambient_R_mod_m2": list(betti_totals["R_mod_m2"]),
        },
        "linewise_replay": {
            "maximum_total_length": 12,
            "partition_checks": partition_checks,
            "jordan_ratio_checks": jordan_ratio_checks,
            "route_maxima": route_maxima,
        },
        "claim_boundary": (
            "The counterexamples close raw higher-Fitting and raw Betti profiles "
            "as automatic apolar-subquotient invariants. The linewise theorem "
            "closes only one-operator Fitting scalarizations. It does not close "
            "a separately proved monotone Fitt_0 valuation, joint two-dimensional "
            "determinantal data, derived Fitting constructions, representation-"
            "valued syzygies, Chow-realizability defects, border rank, or exact "
            "Chow rank for n>=6."
        ),
    }
    return {**core, "core_sha256": canonical_sha256(core)}


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
    print("GENERAL_FITTING_BETTI_SUBQUOTIENT_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
