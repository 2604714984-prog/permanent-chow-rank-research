#!/usr/bin/env python3
"""Independent mask replay for canonical C6 pair cancellation."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations

S3 = tuple(permutations(range(3)))
S4 = tuple(permutations(range(4)))
BOUNDARY = tuple(cell for cell in range(16) if cell // 4 == 3 or cell % 4 == 3)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frame(mu: tuple[int, ...]) -> set[int]:
    return {
        4 * row + column
        for row in range(3)
        for column in range(3)
        if column != mu[row]
    }


def main() -> int:
    frames = {mu: frame(mu) for mu in S3}
    source_count = Counter(
        frozenset(source)
        for mu in S3
        for source in combinations(sorted(frames[mu]), 4)
    )
    shared = {source for source, count in source_count.items() if count == 2}
    require(len(shared) == 9, shared)
    require(Counter(source_count.values()) == Counter({1: 72, 2: 9}), source_count)

    tangent_rows = Counter()
    for source in shared:
        for factor in source:
            triple = frozenset(source - {factor})
            for boundary in BOUNDARY:
                tangent_rows[(boundary, triple)] += 1
    require(len(tangent_rows) == 252, len(tangent_rows))
    require(set(tangent_rows.values()) == {1}, tangent_rows)

    target_source_counts = []
    for sigma in S4:
        target = {4 * row + sigma[row] for row in range(4)}
        if 15 in target:
            continue
        internal = frozenset(cell for cell in target if cell // 4 < 3 and cell % 4 < 3)
        require(len(internal) == 2, (sigma, internal))
        target_source_counts.append(sum(internal <= source for source in shared))
    require(target_source_counts == [2] * 18, target_source_counts)

    print("GENERAL_QUARTIC_C6_SECOND_ORDER_PAIR_CANCELLATION_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
