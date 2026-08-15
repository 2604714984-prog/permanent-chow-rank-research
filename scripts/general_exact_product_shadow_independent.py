#!/usr/bin/env python3
"""Independent exact replay of the perm_7 product-shadow improvement.

This file intentionally does not import general_exact_product_shadow.  It
rebuilds the colex layer, lower shadows, first-container weights and a forward
Ferrers dynamic program from explicit finite sets.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_key(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def finite_data(n: int, m: int) -> tuple[list[int], list[int]]:
    layer = sorted(combinations(range(n), m), key=colex_key)
    require([colex_key(value) for value in layer] == list(range(len(layer))), layer)

    shadows: list[set[tuple[int, ...]]] = [set()]
    running: set[tuple[int, ...]] = set()
    for subset in layer:
        running = set(running)
        for position in range(m):
            running.add(subset[:position] + subset[position + 1 :])
        shadows.append(running)
    profile = [len(value) for value in shadows]

    first_index: dict[tuple[int, ...], int] = {}
    for lower in combinations(range(n), m - 1):
        containing = [
            index
            for index, upper in enumerate(layer)
            if set(lower).issubset(upper)
        ]
        first_index[lower] = min(containing)
    weights = [0] * len(layer)
    for index in first_index.values():
        weights[index] += 1
    require(sum(weights) == comb(n, m - 1), weights)
    return profile, weights


def forward_minimum(
    profile: list[int],
    weights: list[int],
    target: int,
) -> tuple[int, tuple[int, ...], int]:
    width = len(weights)
    # state (last part, sum) -> (objective, count, lexicographically first witness)
    states: dict[tuple[int, int], tuple[int, int, tuple[int, ...]]] = {
        (width, 0): (0, 1, ())
    }
    for weight in weights:
        next_states: dict[tuple[int, int], tuple[int, int, tuple[int, ...]]] = {}
        for (upper, total), (objective, count, witness) in states.items():
            for value in range(min(upper, target - total), -1, -1):
                new_total = total + value
                key = (value, new_total)
                candidate = objective + weight * profile[value]
                candidate_witness = witness + (value,)
                old = next_states.get(key)
                if old is None or candidate < old[0]:
                    next_states[key] = (candidate, count, candidate_witness)
                elif candidate == old[0]:
                    next_states[key] = (
                        old[0],
                        old[1] + count,
                        min(old[2], candidate_witness),
                    )
        states = next_states

    finals = [value for (last, total), value in states.items() if total == target]
    require(finals, target)
    optimum = min(value[0] for value in finals)
    count = sum(value[1] for value in finals if value[0] == optimum)
    witness = min(value[2] for value in finals if value[0] == optimum)
    return optimum, witness, count


def main() -> int:
    profile, weights = finite_data(7, 4)
    value_238, witness_238, count_238 = forward_minimum(profile, weights, 238)
    value_239, witness_239, count_239 = forward_minimum(profile, weights, 239)

    require(value_238 == 452, value_238)
    require(value_239 == 456, value_239)
    require(sum(witness_238) == 238, witness_238)
    require(sum(witness_239) == 239, witness_239)
    require(13 * comb(7, 3) == 455, "threshold")

    target_rank = 7**2 * comb(7, 3) ** 2 - comb(7, 4) ** 2
    one_term_cap = 7**2 * comb(7, 3) - comb(7, 4)
    residual = -(-(target_rank - 7**2 * 238) // one_term_cap)
    require((target_rank, one_term_cap, residual) == (58_800, 1_680, 29), residual)
    require(13 + residual == 42, 13 + residual)

    print(f"independent_min_238={value_238}")
    print(f"independent_min_239={value_239}")
    print(f"independent_count_238={count_238}")
    print(f"independent_count_239={count_239}")
    print("independent_perm7_lower_bound=42")
    print("GENERAL_EXACT_PRODUCT_SHADOW_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
