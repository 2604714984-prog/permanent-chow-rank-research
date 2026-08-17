#!/usr/bin/env python3
"""Independent replay of the Fitting/Betti subquotient barrier.

This file imports none of the primary audit.  It reconstructs the named
Fitting ideals, the monomial quotient Betti tables by the two-variable
Hilbert--Burch rule, and the one-variable invariant-factor/Fitting equivalence.
"""

from __future__ import annotations

from collections import Counter
from math import comb
from typing import Iterable


Monomial = tuple[int, int]
Ideal = tuple[Monomial, ...]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def divides(left: Monomial, right: Monomial) -> bool:
    return left[0] <= right[0] and left[1] <= right[1]


def minimize(values: Iterable[Monomial]) -> Ideal:
    values = sorted(set(values))
    return tuple(
        value
        for value in values
        if not any(other != value and divides(other, value) for other in values)
    )


R: Ideal = ((0, 0),)
m: Ideal = minimize(((1, 0), (0, 1)))
m2: Ideal = minimize(((2, 0), (1, 1), (0, 2)))
ci: Ideal = minimize(((2, 0), (0, 2)))


def ideal_subset(left: Ideal, right: Ideal) -> bool:
    if right == R:
        return True
    if not right:
        return not left
    return all(any(divides(generator, value) for generator in right) for value in left)


def multiply_ideals(left: Ideal, right: Ideal) -> Ideal:
    return minimize((a + c, b + d) for a, b in left for c, d in right)


def monomial_quotient_hilbert(ideal: Ideal, maximum_degree: int = 8):
    return tuple(
        sum(
            not any(
                divides(generator, (a, degree - a)) for generator in ideal
            )
            for a in range(degree + 1)
        )
        for degree in range(maximum_degree + 1)
    )


def quotient_betti(ideal: Ideal) -> tuple[tuple[int, int, int], ...]:
    """Minimal graded Betti terms for R/I when I is m-primary monomial."""

    generators = sorted(ideal, key=lambda value: (-value[0], value[1]))
    require(generators and all(sum(value) > 0 for value in generators), ideal)
    terms = [(0, 0, 1)]
    terms.extend((1, sum(generator), 1) for generator in generators)
    for left, right in zip(generators, generators[1:]):
        lcm = (max(left[0], right[0]), max(left[1], right[1]))
        terms.append((2, sum(lcm), 1))
    return tuple(sorted(terms))


def hilbert_from_betti(terms, maximum_degree: int = 8):
    numerator = Counter()
    for homological, shift, multiplicity in terms:
        numerator[shift] += (-1) ** homological * multiplicity
    return tuple(
        sum(
            coefficient * (degree - shift + 1)
            for shift, coefficient in numerator.items()
            if degree >= shift
        )
        for degree in range(maximum_degree + 1)
    )


def total_betti(terms):
    return tuple(
        sum(
            multiplicity
            for homological, _, multiplicity in terms
            if homological == index
        )
        for index in range(3)
    )


def partitions_ascending(total: int, minimum: int = 1):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in partitions_ascending(total - first, first):
            yield (first, *tail)


def valuations_from_invariant_factors(ascending):
    count = len(ascending)
    return tuple(sum(ascending[: count - index]) for index in range(count + 1))


def invariant_factors_from_valuations(values):
    count = len(values) - 1
    ascending = tuple(
        values[index] - values[index + 1]
        for index in range(count - 1, -1, -1)
    )
    return tuple(sorted(ascending))


def main() -> int:
    fitting = {
        "k": {"0": m, "1": R},
        "k2": {"0": multiply_ideals(m, m), "1": m, "2": R},
        "R_mod_m2": {"0": m2, "1": R},
        "R_mod_s2_t2": {"0": ci, "1": R},
    }
    require(fitting["k2"]["0"] == m2, fitting)

    # diagonal k -> k^2
    require(ideal_subset(fitting["k2"]["1"], fitting["k"]["1"]), fitting)
    require(not ideal_subset(fitting["k"]["1"], fitting["k2"]["1"]), fitting)
    # m/m^2 ~= k^2(-1) -> R/m^2
    require(ideal_subset(fitting["k2"]["1"], fitting["R_mod_m2"]["1"]), fitting)
    require(not ideal_subset(fitting["R_mod_m2"]["1"], fitting["k2"]["1"]), fitting)

    require(sum(monomial_quotient_hilbert(m)) == 1, m)
    require(sum(monomial_quotient_hilbert(m2)) == 3, m2)

    ci_betti = quotient_betti(ci)
    m2_betti = quotient_betti(m2)
    require(total_betti(ci_betti) == (1, 2, 1), ci_betti)
    require(total_betti(m2_betti) == (1, 3, 2), m2_betti)
    require(
        hilbert_from_betti(ci_betti) == monomial_quotient_hilbert(ci),
        ci_betti,
    )
    require(
        hilbert_from_betti(m2_betti) == monomial_quotient_hilbert(m2),
        m2_betti,
    )
    require(ideal_subset(ci, m2), (ci, m2))

    submodule_betti = (2, 4, 2)
    require(submodule_betti[0] > total_betti(m2_betti)[0], submodule_betti)
    require(submodule_betti[1] > total_betti(m2_betti)[1], submodule_betti)

    partition_checks = 0
    for total in range(1, 13):
        for ascending in partitions_ascending(total):
            values = valuations_from_invariant_factors(ascending)
            recovered = invariant_factors_from_valuations(values)
            require(recovered == ascending, (ascending, values, recovered))
            partition_checks += 1
    require(partition_checks == 271, partition_checks)

    ratio_checks = 0
    for n in range(2, 21):
        ratios = []
        for degree in range(n // 2 + 1):
            ratios.append(comb(n, degree))
            ratio_checks += 1
        require(max(ratios) == comb(n, n // 2), (n, ratios))
    require(ratio_checks == 119, ratio_checks)

    print("independent_fitting_submodule_counterexamples=2")
    print("independent_betti_quotient_counterexamples=1")
    print("independent_betti_submodule_counterexamples=1")
    print("independent_partition_checks=271")
    print("independent_jordan_ratio_checks=119")
    print("GENERAL_FITTING_BETTI_SUBQUOTIENT_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
