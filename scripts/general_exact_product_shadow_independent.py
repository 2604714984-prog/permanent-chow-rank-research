#!/usr/bin/env python3
"""Independent exact replay of the perm_7 and perm_8 product-shadow improvements.

This file intentionally does not import general_exact_product_shadow. It
rebuilds the colex layers, lower shadows, first-container weights and a
forward Ferrers dynamic program from explicit finite sets.
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


def verify_case(
    *,
    n: int,
    m: int,
    cap_size: int,
    first_bad_size: int,
    expected_cap_shadow: int,
    expected_first_bad_shadow: int,
    fixed_terms: int,
    output_degree: int,
    expected_residual: int,
    expected_total: int,
) -> tuple[int, int]:
    profile, weights = finite_data(n, m)
    cap_value, cap_witness, cap_count = forward_minimum(
        profile, weights, cap_size
    )
    first_bad_value, first_bad_witness, first_bad_count = forward_minimum(
        profile, weights, first_bad_size
    )

    require(cap_value == expected_cap_shadow, cap_value)
    require(first_bad_value == expected_first_bad_shadow, first_bad_value)
    require(sum(cap_witness) == cap_size, cap_witness)
    require(sum(first_bad_witness) == first_bad_size, first_bad_witness)

    threshold = fixed_terms * comb(n, m - 1)
    require(cap_value <= threshold < first_bad_value, threshold)

    target_rank = (
        n**2 * comb(n, output_degree) ** 2
        - comb(n, output_degree + 1) ** 2
    )
    one_term_cap = (
        n**2 * comb(n, output_degree)
        - comb(n, output_degree + 1)
    )
    residual = -(-(target_rank - n**2 * cap_size) // one_term_cap)
    require(residual == expected_residual, residual)
    require(fixed_terms + residual == expected_total, fixed_terms + residual)

    print(f"independent_n{n}_min_{cap_size}={cap_value}")
    print(f"independent_n{n}_min_{first_bad_size}={first_bad_value}")
    print(f"independent_n{n}_count_{cap_size}={cap_count}")
    print(f"independent_n{n}_count_{first_bad_size}={first_bad_count}")
    print(f"independent_perm{n}_lower_bound={expected_total}")
    return cap_count, first_bad_count


def main() -> int:
    n7_counts = verify_case(
        n=7,
        m=4,
        cap_size=238,
        first_bad_size=239,
        expected_cap_shadow=452,
        expected_first_bad_shadow=456,
        fixed_terms=13,
        output_degree=3,
        expected_residual=29,
        expected_total=42,
    )
    require(n7_counts == (2, 8), n7_counts)

    n8_counts = verify_case(
        n=8,
        m=4,
        cap_size=560,
        first_bad_size=561,
        expected_cap_shadow=784,
        expected_first_bad_shadow=793,
        fixed_terms=14,
        output_degree=4,
        expected_residual=63,
        expected_total=77,
    )
    require(n8_counts == (2, 2), n8_counts)

    print("GENERAL_EXACT_PRODUCT_SHADOW_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
