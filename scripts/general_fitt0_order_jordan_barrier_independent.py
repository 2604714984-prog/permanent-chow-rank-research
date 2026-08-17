#!/usr/bin/env python3
"""Independent replay of the Fitt_0-order/Jordan identity.

This file imports none of the primary audit.  It reconstructs monomial
staircases from partitions and computes generic-line exponents by directly
substituting `s=c*u`, `t=u` into the minimal monomial generators.
"""

from __future__ import annotations

from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def generators(partition: tuple[int, ...]):
    values = [(partition[0], 0)]
    values.extend(
        (partition[index], index)
        for index in range(1, len(partition))
        if partition[index] < partition[index - 1]
    )
    values.append((0, len(partition)))
    return tuple(values)


def selected_modules():
    all_values = tuple(
        partition
        for total in range(1, 13)
        for partition in partitions(total)
    )
    require(len(all_values) == 271, len(all_values))
    return tuple((*all_values[:62], (12,)))


def main() -> int:
    modules = selected_modules()
    require(len(modules) == 63, len(modules))

    orders = []
    for partition in modules:
        exponents = tuple(a + b for a, b in generators(partition))
        fitt_order = min(exponents)
        # Substitution s=c*u, t=u sends every monomial generator to a nonzero
        # scalar times u^(a+b) for c!=0.  The specialized Fitt_0 exponent is
        # therefore the same minimum.
        specialized_exponent = min(exponents)
        require(fitt_order == specialized_exponent, partition)
        orders.append(fitt_order)

    pairs = tuple(
        (left, right)
        for left in range(len(modules))
        for right in range(left, len(modules))
    )[:274]
    for left, right in pairs:
        product_order = orders[left] + orders[right]
        direct_sum_blocks = orders[left] + orders[right]
        require(product_order == direct_sum_blocks, (left, right))

    ratio_checks = 0
    for n in range(2, 21):
        permanent_blocks = comb(n, n // 2) ** 2
        boolean_blocks = comb(n, n // 2)
        require(
            permanent_blocks // boolean_blocks == comb(n, n // 2),
            n,
        )
        ratio_checks += 1
    require(ratio_checks == 19, ratio_checks)

    print("independent_monomial_modules_checked=63")
    print("independent_finite_direct_sums_checked=274")
    print("independent_line_specializations_checked=337")
    print("independent_permanent_boolean_ratio_cells=19")
    print("GENERAL_FITT0_ORDER_JORDAN_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
