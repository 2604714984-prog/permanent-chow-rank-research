#!/usr/bin/env python3
"""Independent arithmetic replay for the private-polar zero band.

This implementation imports none of the primary helpers.  It scans all legal
integer rows directly through m=256 and independently checks the quartic
three-by-three rectangle interface.
"""

from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    rows: list[tuple[int, int, int, int]] = []
    strict_new = 0
    quartic_boundary: list[tuple[int, int, int, int]] = []

    for m in range(3, 257):
        for excess in range(m):
            total = m * m + excess
            for n in range(m, total + 1):
                if total % n:
                    continue
                q = total // n
                if q < 2:
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

    triples = tuple(combinations(range(9), 3))
    maximum_distinct_product = 0
    overlap_checks = 0
    for left_rows in triples:
        left_rows_set = set(left_rows)
        for right_rows in triples:
            row_overlap = len(left_rows_set.intersection(right_rows))
            for left_columns in triples:
                left_columns_set = set(left_columns)
                for right_columns in triples:
                    if left_rows == right_rows and left_columns == right_columns:
                        continue
                    column_overlap = len(
                        left_columns_set.intersection(right_columns)
                    )
                    maximum_distinct_product = max(
                        maximum_distinct_product,
                        row_overlap * column_overlap,
                    )
                    overlap_checks += 1

    # The full four-loop replay has 84^4-84^2 labelled ordered pairs.
    require(overlap_checks == 84**4 - 84**2, overlap_checks)
    require(maximum_distinct_product == 6, maximum_distinct_product)
    require(18 - maximum_distinct_product == 12, maximum_distinct_product)

    print(f"independent_small_excess_rows={len(rows)}")
    print(f"independent_strict_new_rows={strict_new}")
    print("independent_quartic_boundary=(9,4,2,2)")
    print(f"independent_quartic_overlap_checks={overlap_checks}")
    print("independent_quartic_minimum_two_rectangle_union=12")
    print("GENERAL_SMALL_EXCESS_PRIVATE_POLAR_BAND_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
