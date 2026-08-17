#!/usr/bin/env python3
"""Independent arithmetic replay for nonuniform shifted matrix ceilings.

This implementation imports none of the primary audit. It assigns shifts to
individual source and target summands, groups equal shifts only after the
assignment, and checks several support patterns with exact Fraction ratios.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from math import ceil, comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def level(n: int, degree: int) -> int:
    return comb(n, degree) if 0 <= degree <= n else 0


def grouped(values: tuple[int, ...]) -> dict[int, int]:
    return dict(sorted(Counter(values).items()))


def support_patterns(
    source_shifts: tuple[int, ...],
    target_shifts: tuple[int, ...],
):
    source = grouped(source_shifts)
    target = grouped(target_shifts)
    candidates = [
        (b, a)
        for a in source
        for b in target
        if a >= b
    ]
    if not candidates:
        return []

    patterns = []
    patterns.append(tuple(candidates))
    patterns.append(
        tuple(
            pair
            for index, pair in enumerate(candidates)
            if index % 2 == 0
        )
    )
    patterns.append(
        tuple(
            pair
            for pair in candidates
            if (pair[0] + pair[1]) % 2 == 0
        )
    )
    patterns.append((candidates[0],))
    patterns.append((candidates[-1],))
    return [pattern for pattern in patterns if pattern]


def check_case(
    n: int,
    d: int,
    source_shifts: tuple[int, ...],
    target_shifts: tuple[int, ...],
    pattern: tuple[tuple[int, int], ...],
) -> tuple[int, int]:
    source = grouped(source_shifts)
    target = grouped(target_shifts)
    central = comb(n, n // 2)

    active = []
    for b, a in pattern:
        source_level = level(n, d - a)
        target_level = level(n, d - b)
        if source_level == 0 or target_level == 0:
            continue
        q_a = source[a]
        p_b = target[b]
        normal_rank = 1 + (
            (a + 3 * b + n + d) % min(q_a, p_b)
        )
        boolean = normal_rank * min(source_level, target_level)
        permanent = min(
            q_a * source_level**2,
            p_b * target_level**2,
        )
        ratio = Fraction(permanent, boolean)
        block_integer = ceil(ratio)
        require(
            block_integer <= p_b * q_a * central,
            (
                n,
                d,
                source_shifts,
                target_shifts,
                b,
                a,
                ratio,
            ),
        )
        active.append(
            (
                b,
                a,
                q_a,
                p_b,
                boolean,
                permanent,
                block_integer,
            )
        )

    if not active:
        return 0, 0

    source_active = {a for _, a, *_ in active}
    target_active = {b for b, *_ in active}
    source_upper = sum(
        source[a] * level(n, d - a) ** 2
        for a in source_active
    )
    target_upper = sum(
        target[b] * level(n, d - b) ** 2
        for b in target_active
    )
    block_upper = sum(entry[5] for entry in active)
    full_upper = min(source_upper, target_upper, block_upper)
    full_boolean = max(entry[4] for entry in active)
    direct = ceil(Fraction(full_upper, full_boolean))
    block_sum = sum(entry[6] for entry in active)
    support_area = sum(entry[2] * entry[3] for entry in active)

    require(
        direct <= block_sum <= support_area * central,
        (
            n,
            d,
            source_shifts,
            target_shifts,
            direct,
            block_sum,
            support_area,
        ),
    )
    require(
        support_area <= len(source_shifts) * len(target_shifts),
        support_area,
    )
    return len(active), direct


def main() -> int:
    assignment_checks = 0
    pattern_checks = 0
    degree_checks = 0
    active_block_checks = 0
    positive_direct_checks = 0

    for q in range(1, 5):
        for p in range(1, 5):
            for source_shifts in product(range(3), repeat=q):
                for target_shifts in product(range(3), repeat=p):
                    assignment_checks += 1
                    for pattern in support_patterns(
                        source_shifts,
                        target_shifts,
                    ):
                        pattern_checks += 1
                        for n in range(3, 9):
                            for d in range(0, n + 3):
                                active, direct = check_case(
                                    n,
                                    d,
                                    source_shifts,
                                    target_shifts,
                                    pattern,
                                )
                                degree_checks += 1
                                active_block_checks += active
                                positive_direct_checks += direct > 0

    thresholds = []
    for n in range(3, 81):
        central = comb(n, n // 2)
        glynn = 2 ** (n - 1)
        k = 1
        while k * k * central < glynn:
            k += 1
        thresholds.append(k)
    require(thresholds[-1] >= thresholds[0], thresholds)

    print(f"independent_assignment_checks={assignment_checks}")
    print(f"independent_pattern_checks={pattern_checks}")
    print(f"independent_degree_checks={degree_checks}")
    print(f"independent_active_block_checks={active_block_checks}")
    print(f"independent_positive_direct_checks={positive_direct_checks}")
    print(f"independent_K_threshold_n80={thresholds[-1]}")
    print("GENERAL_NONUNIFORM_SHIFTED_MATRIX_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
