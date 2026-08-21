#!/usr/bin/env python3
"""Independent bit-mask replay for coordinate first-order closure."""

from __future__ import annotations

from collections import Counter
from itertools import combinations_with_replacement, permutations

ORDER = 4
MATCHINGS: list[int] = []
for permutation in permutations(range(ORDER)):
    mask = 0
    for row, column in enumerate(permutation):
        mask |= 1 << (ORDER * row + column)
    MATCHINGS.append(mask)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def support_mask(frame: tuple[int, ...] | list[int]) -> int:
    result = 0
    for cell in frame:
        result |= 1 << cell
    return result


def envelope(mask: int) -> set[int]:
    return {
        index
        for index, matching in enumerate(MATCHINGS)
        if (matching & mask).bit_count() >= 3
    }


def direct(mask: int) -> set[int]:
    return {
        index
        for index, matching in enumerate(MATCHINGS)
        if matching & mask == matching
    }


def vertical_residual(frame: tuple[int, ...]) -> set[int]:
    counts = Counter(frame)
    result: set[int] = set()
    direct_set = direct(support_mask(frame))

    for cell, multiplicity in counts.items():
        if multiplicity < 2:
            continue
        residual = list(frame)
        residual.remove(cell)
        residual.remove(cell)
        residual_mask = support_mask(residual)
        result.update(
            index
            for index, matching in enumerate(MATCHINGS)
            if (matching & residual_mask).bit_count() >= 3
        )
    return result - direct_set


def main() -> int:
    checked = 0
    maximum_score = 0
    maximum_vertical = 0

    for frame in combinations_with_replacement(range(16), 6):
        checked += 1
        mask = support_mask(frame)
        e_set = envelope(mask)
        p_set = direct(mask)
        v_set = vertical_residual(frame)
        require(v_set <= e_set - p_set, (frame, e_set, p_set, v_set))
        score = len(e_set) + len(p_set) + len(v_set)
        require(score <= 6, (frame, len(e_set), len(p_set), len(v_set), score))
        maximum_score = max(maximum_score, score)
        maximum_vertical = max(maximum_vertical, len(v_set))

    require(checked == 54264, checked)
    require(maximum_score == 6, maximum_score)
    require(maximum_vertical == 2, maximum_vertical)
    print("GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_CLOSURE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
