#!/usr/bin/env python3
"""Independent permutation/edge replay of the canonical C6 reduction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations

S3 = tuple(permutations(range(3)))
S4 = tuple(permutations(range(4)))
CELLS = tuple((row, column) for row in range(3) for column in range(3))


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frame(mu: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        (row, column)
        for row in range(3)
        for column in range(3)
        if column != mu[row]
    }


def cross(cell: tuple[int, int]) -> set[tuple[int, int]]:
    row, column = cell
    return {
        (row, other) for other in range(3) if other != column
    } | {
        (other, column) for other in range(3) if other != row
    }


def main() -> int:
    frames = {mu: frame(mu) for mu in S3}
    adjacent_pairs = []
    nonadjacent_pairs = []
    shared_sources = {}

    for left, right in combinations(S3, 2):
        agreements = [(row, left[row]) for row in range(3) if left[row] == right[row]]
        intersection = frames[left] & frames[right]
        if len(agreements) == 1:
            require(len(intersection) == 4, (left, right, intersection))
            require(intersection == cross(agreements[0]), (left, right, intersection))
            adjacent_pairs.append((left, right))
            shared_sources[agreements[0]] = intersection
        else:
            require(len(agreements) == 0 and len(intersection) == 3, (left, right, agreements, intersection))
            nonadjacent_pairs.append((left, right))

    require(len(adjacent_pairs) == 9, len(adjacent_pairs))
    require(len(nonadjacent_pairs) == 6, len(nonadjacent_pairs))
    require(set(shared_sources) == set(CELLS), shared_sources)

    source_incidence = Counter()
    for mu in S3:
        for source in combinations(sorted(frames[mu]), 4):
            source_incidence[frozenset(source)] += 1
    require(Counter(source_incidence.values()) == Counter({1: 72, 2: 9}), source_incidence)

    disjoint_pairs = [
        pair
        for pair in combinations(CELLS, 2)
        if pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1]
    ]
    require(len(disjoint_pairs) == 18, len(disjoint_pairs))
    require(
        all(len(cross(left) & cross(right)) == 2 for left, right in disjoint_pairs),
        disjoint_pairs,
    )

    target_pairs = []
    fixed_count = 0
    for sigma in S4:
        target = {(row, sigma[row]) for row in range(4)}
        if sigma[3] == 3:
            fixed_count += 1
            restriction = target - {(3, 3)}
            require(sum(len(restriction & cross(cell)) == 2 for cell in CELLS) == 6, sigma)
            continue
        internal = {(row, column) for row, column in target if row < 3 and column < 3}
        owners = tuple(sorted(cell for cell in CELLS if internal <= cross(cell)))
        require(len(owners) == 2 and owners in {tuple(sorted(pair)) for pair in disjoint_pairs}, (sigma, owners))
        target_pairs.append(owners)

    require(fixed_count == 6, fixed_count)
    require(len(target_pairs) == 18, len(target_pairs))
    require(set(target_pairs) == {tuple(sorted(pair)) for pair in disjoint_pairs}, target_pairs)
    print("GENERAL_QUARTIC_C6_SECOND_ORDER_SOURCE_REDUCTION_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
