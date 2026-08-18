#!/usr/bin/env python3
"""Independent arithmetic replay for the private-polar zero band.

This implementation imports none of the primary helpers.  It scans legal rows
by term count through m=256 and reconstructs the quartic rectangle minimum
from the complete labelled overlap distribution of three-subsets.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    rows: list[tuple[int, int, int, int]] = []
    strict_new = 0
    quartic_boundary: list[tuple[int, int, int, int]] = []
    arithmetic_checks = 0

    for m in range(3, 257):
        for excess in range(m):
            total = m * m + excess
            maximum_q = total // m
            for q in range(2, maximum_q + 1):
                arithmetic_checks += 1
                if total % q:
                    continue
                n = total // q
                if n < m:
                    continue
                rows.append((n, m, q, excess))

                if excess >= 1:
                    require(q * excess < m * m, (n, m, q, excess))

                if m >= 5 and excess >= 2:
                    require(n < (m - 1) ** 2, (n, m, q, excess))
                    strict_new += 1

                if excess >= 2 and not n < (m - 1) ** 2:
                    require((n, m, q, excess) == (9, 4, 2, 2), (n, m, q, excess))
                    quartic_boundary.append((n, m, q, excess))

    require(quartic_boundary == [(9, 4, 2, 2)], quartic_boundary)
    require(
        [row for row in rows if row[1] == 3 and row[3] == 2] == [],
        "unexpected cubic excess-two row",
    )

    triples = tuple(frozenset(value) for value in combinations(range(9), 3))
    overlap_histogram: Counter[tuple[int, bool]] = Counter()
    labelled_subset_pair_checks = 0
    for left_index, left in enumerate(triples):
        for right_index, right in enumerate(triples):
            overlap_histogram[(len(left & right), left_index == right_index)] += 1
            labelled_subset_pair_checks += 1

    require(labelled_subset_pair_checks == 84**2, labelled_subset_pair_checks)
    require(overlap_histogram[(3, True)] == 84, overlap_histogram)
    require((3, False) not in overlap_histogram, overlap_histogram)

    maximum_distinct_product = 0
    overlap_type_checks = 0
    for (row_overlap, row_equal), (column_overlap, column_equal) in product(
        overlap_histogram,
        repeat=2,
    ):
        if row_equal and column_equal:
            continue
        maximum_distinct_product = max(
            maximum_distinct_product,
            row_overlap * column_overlap,
        )
        overlap_type_checks += 1

    require(maximum_distinct_product == 6, maximum_distinct_product)
    require(18 - maximum_distinct_product == 12, maximum_distinct_product)

    print(f"independent_arithmetic_checks={arithmetic_checks}")
    print(f"independent_small_excess_rows={len(rows)}")
    print(f"independent_strict_new_rows={strict_new}")
    print("independent_quartic_boundary=(9,4,2,2)")
    print(f"independent_labelled_subset_pair_checks={labelled_subset_pair_checks}")
    print(f"independent_overlap_type_checks={overlap_type_checks}")
    print("independent_quartic_minimum_two_rectangle_union=12")
    print("GENERAL_SMALL_EXCESS_PRIVATE_POLAR_BAND_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
