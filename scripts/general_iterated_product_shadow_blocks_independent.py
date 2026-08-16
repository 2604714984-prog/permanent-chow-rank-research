#!/usr/bin/env python3
"""Independent finite replay of the iterated-shadow block bounds.

This implementation imports none of the primary audit.  It reconstructs colex
orders, arbitrary-order lower shadows and first-container weights from explicit
finite sets, then uses a forward Ferrers dynamic program for the eight decisive
transition values.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def finite_data(n: int, m: int, order: int) -> tuple[list[int], list[int]]:
    require(1 <= order < m, (n, m, order))
    layer = sorted(combinations(range(n), m), key=colex_rank)
    require([colex_rank(value) for value in layer] == list(range(len(layer))), layer)

    lower_degree = m - order
    running: set[tuple[int, ...]] = set()
    profile = [0]
    for subset in layer:
        running = set(running)
        running.update(combinations(subset, lower_degree))
        profile.append(len(running))

    index = {subset: position for position, subset in enumerate(layer)}
    weights = [0] * len(layer)
    for lower in combinations(range(n), lower_degree):
        missing = [value for value in range(n) if value not in lower]
        first = tuple(sorted(lower + tuple(missing[:order])))
        weights[index[first]] += 1
    require(sum(weights) == comb(n, lower_degree), weights)
    return profile, weights


def forward_minimum(
    profile: list[int],
    weights: list[int],
    target: int,
) -> tuple[int, tuple[int, ...]]:
    width = len(weights)
    states: dict[tuple[int, int], tuple[int, tuple[int, ...]]] = {
        (width, 0): (0, ())
    }
    for weight in weights:
        next_states: dict[tuple[int, int], tuple[int, tuple[int, ...]]] = {}
        for (upper, total), (objective, witness) in states.items():
            for value in range(min(upper, target - total), -1, -1):
                key = (value, total + value)
                candidate = (
                    objective + weight * profile[value],
                    witness + (value,),
                )
                old = next_states.get(key)
                if old is None or candidate < old:
                    next_states[key] = candidate
        states = next_states

    finals = [value for (last, total), value in states.items() if total == target]
    require(finals, target)
    return min(finals)


def replay_value(n: int, m: int, order: int, size: int) -> int:
    profile, weights = finite_data(n, m, order)
    value, witness = forward_minimum(profile, weights, size)
    require(sum(witness) == size, (n, m, order, size, witness))
    return value


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def main() -> int:
    expected = {
        (7, 3, 1, 64): 84,
        (7, 3, 1, 65): 87,
        (7, 4, 1, 341): 586,
        (7, 4, 1, 342): 590,
        (8, 3, 2, 16): 16,
        (8, 3, 2, 17): 18,
        (8, 4, 1, 625): 850,
        (8, 4, 1, 626): 858,
    }
    observed = {
        key: replay_value(*key)
        for key in expected
    }
    require(observed == expected, observed)

    target_7 = 7**2 * comb(7, 3) ** 2 - comb(7, 4) ** 2
    cap_7 = 7**2 * comb(7, 3) - comb(7, 4)
    residual_7 = ceil_div(target_7 - 7**2 * 341, cap_7)
    require((target_7, cap_7, residual_7, 19 + residual_7) == (58_800, 1_680, 26, 45), residual_7)

    target_8 = 8**2 * comb(8, 4) ** 2 - comb(8, 5) ** 2
    cap_8 = 8**2 * comb(8, 4) - comb(8, 5)
    residual_8 = ceil_div(target_8 - 8**2 * 625, cap_8)
    require((target_8, cap_8, residual_8, 17 + residual_8) == (310_464, 4_424, 62, 79), residual_8)

    print("independent_F_7_3_order1_64=84")
    print("independent_F_7_3_order1_65=87")
    print("independent_F_7_4_order1_341=586")
    print("independent_F_7_4_order1_342=590")
    print("independent_perm7_lower_bound=45")
    print("independent_F_8_3_order2_16=16")
    print("independent_F_8_3_order2_17=18")
    print("independent_F_8_4_order1_625=850")
    print("independent_F_8_4_order1_626=858")
    print("independent_perm8_lower_bound=79")
    print("GENERAL_ITERATED_PRODUCT_SHADOW_BLOCKS_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
