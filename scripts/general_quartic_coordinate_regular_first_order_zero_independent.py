#!/usr/bin/env python3
"""Independent duplicate-label replay for coordinate regular first-order zero."""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations

N = 4
MATCHINGS = tuple(frozenset(r * N + p[r] for r in range(N)) for p in permutations(range(N)))
SOURCE_SUBSETS = tuple(combinations(range(6), 4))


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def envelope(frame: tuple[int, ...]) -> set[int]:
    support = set(frame)
    return {
        index for index, matching in enumerate(MATCHINGS)
        if len(support & matching) >= 3
    }


def direct(frame: tuple[int, ...]) -> set[int]:
    monomials = {
        tuple(sorted(frame[label] for label in subset))
        for subset in SOURCE_SUBSETS
    }
    return {
        index for index, matching in enumerate(MATCHINGS)
        if tuple(sorted(matching)) in monomials
    }


def internal_private(frame: tuple[int, ...]) -> set[int]:
    positions: dict[int, list[int]] = defaultdict(list)
    for label, cell in enumerate(frame):
        positions[cell].append(label)
    duplicate_pairs = tuple(
        pair
        for labels in positions.values()
        for pair in combinations(labels, 2)
    )
    result: set[int] = set()
    for matching_index, matching in enumerate(MATCHINGS):
        for left, right in duplicate_pairs:
            remaining = [label for label in range(6) if label not in (left, right)]
            if any(
                len({frame[label] for label in triple}) == 3
                and {frame[label] for label in triple} < matching
                for triple in combinations(remaining, 3)
            ):
                result.add(matching_index)
                break
    return result


def main() -> int:
    count = 0
    maximum_private = 0
    envelope_six = 0
    envelope_six_private: Counter[int] = Counter()
    two_direct_envelopes: set[int] = set()

    for frame in combinations_with_replacement(range(16), 6):
        count += 1
        frame_envelope = envelope(frame)
        direct_set = direct(frame)
        private = direct_set | internal_private(frame)
        require(private <= frame_envelope, (frame, private, frame_envelope))
        maximum_private = max(maximum_private, len(private))
        if len(frame_envelope) == 6:
            envelope_six += 1
            envelope_six_private[len(private)] += 1
        if len(direct_set) == 2:
            two_direct_envelopes.add(len(frame_envelope))

    require(count == 54264, count)
    require(maximum_private == 2, maximum_private)
    require(envelope_six == 288, envelope_six)
    require(envelope_six_private == Counter({0: 288}), envelope_six_private)
    require(two_direct_envelopes == {2}, two_direct_envelopes)
    print("GENERAL_QUARTIC_COORDINATE_REGULAR_FIRST_ORDER_ZERO_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
