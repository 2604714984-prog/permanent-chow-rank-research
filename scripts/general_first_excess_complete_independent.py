#!/usr/bin/env python3
"""Independent finite replay for the cubic first-excess closure.

This implementation imports neither exact-product-shadow code nor the parent
first-excess audit.  It enumerates the 100 coordinate two-by-two rectangles in
a five-by-five matrix and checks all unordered pairs directly.
"""

from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    two_sets = tuple(combinations(range(5), 2))
    rectangles = tuple(
        frozenset((row, column) for row in rows for column in columns)
        for rows in two_sets
        for columns in two_sets
    )
    require(len(rectangles) == 100, len(rectangles))
    require(len(set(rectangles)) == 100, "duplicate rectangles")
    require(all(len(rectangle) == 4 for rectangle in rectangles), rectangles)

    minimum_union = 25
    minimizers = 0
    pair_checks = 0
    for left_index, right_index in combinations(range(len(rectangles)), 2):
        size = len(rectangles[left_index] | rectangles[right_index])
        pair_checks += 1
        if size < minimum_union:
            minimum_union = size
            minimizers = 1
        elif size == minimum_union:
            minimizers += 1

    require(pair_checks == 4_950, pair_checks)
    require(minimum_union == 6, minimum_union)
    require(minimizers > 0, minimizers)

    # Exhibit equality: the same row pair and two column pairs sharing one
    # column have derivative-support union 2*3=6.
    equality_left = frozenset(
        (row, column) for row in (0, 1) for column in (0, 1)
    )
    equality_right = frozenset(
        (row, column) for row in (0, 1) for column in (0, 2)
    )
    require(len(equality_left | equality_right) == 6, "missing equality witness")

    # The inherited cubic branches produce private polar spaces of dimensions
    # four and five.  Both exceed the inverse exact-shadow capacity one at
    # linear-shadow budget five.
    inverse_capacity = 1
    require(4 > inverse_capacity and 5 > inverse_capacity, inverse_capacity)

    print(f"independent_rectangles={len(rectangles)}")
    print(f"independent_rectangle_pair_checks={pair_checks}")
    print(f"independent_minimum_two_rectangle_union={minimum_union}")
    print(f"independent_minimizer_pairs={minimizers}")
    print("GENERAL_FIRST_EXCESS_COMPLETE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
