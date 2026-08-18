#!/usr/bin/env python3
"""Independent integer replay for the post-simplex small-excess band.

This implementation imports no primary helper.  It scans term counts rather
than divisors, reconstructs the complete exceptional-row lists through
m=256, enumerates the extremal d-subset rectangles on a (d+1)-element ground
set, and checks the pair-supported-polar margins directly.
"""

from __future__ import annotations

from itertools import combinations
from math import ceil


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rectangle_minimum(d: int) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    ground = tuple(range(d + 1))
    subsets = tuple(combinations(ground, d))
    rectangles = tuple((rows, columns) for rows in subsets for columns in subsets)
    best = 10**9
    witnesses: list[tuple[tuple[int, ...], ...]] = []
    for left_index, left in enumerate(rectangles):
        left_cells = {(i, j) for i in left[0] for j in left[1]}
        for right in rectangles[left_index + 1 :]:
            right_cells = {(i, j) for i in right[0] for j in right[1]}
            union = len(left_cells | right_cells)
            if union < best:
                best = union
                witnesses = [(left[0], left[1], right[0], right[1])]
            elif union == best:
                witnesses.append((left[0], left[1], right[0], right[1]))
    return len(rectangles), best, tuple(witnesses)


def scan(maximum_m: int = 256):
    private_exceptions = []
    pair_exceptions = []
    row_count = 0
    counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for m in range(4, maximum_m + 1):
        largest_extra = 3 if m == 4 else 4
        for extra in range(1, largest_extra + 1):
            excess = m + extra
            total = m * m + excess
            for q in range(2, total // m + 1):
                if total % q:
                    continue
                n = total // q
                if n < m:
                    continue
                row_count += 1
                counts[extra] += 1

                private_ok = n < (m - 1) ** 2
                no_private_ok = (q - 1) * excess < m * m
                if not private_ok:
                    private_exceptions.append((m, excess, n, q))
                if not no_private_ok:
                    pair_exceptions.append((m, excess, n, q))

    return row_count, counts, private_exceptions, pair_exceptions


def main() -> int:
    row_count, counts, private_exceptions, pair_exceptions = scan()
    require(
        private_exceptions
        == [
            (4, 6, 11, 2),
            (5, 7, 16, 2),
            (5, 9, 17, 2),
        ],
        private_exceptions,
    )
    require(
        pair_exceptions
        == [
            (6, 9, 9, 5),
            (7, 11, 10, 6),
            (12, 16, 16, 10),
        ],
        pair_exceptions,
    )

    rectangle_checks = 0
    for d, expected in ((3, 12), (4, 20)):
        rectangle_count, minimum, witnesses = rectangle_minimum(d)
        require(rectangle_count == (d + 1) ** 2, (d, rectangle_count))
        require(minimum == expected, (d, minimum, expected))
        require(witnesses, d)
        rectangle_checks += rectangle_count * (rectangle_count - 1) // 2

    private_rows = {
        (4, 6, 11, 2): (5, 12),
        (5, 7, 16, 2): (9, 20),
        (5, 9, 17, 2): (8, 20),
    }
    for (m, excess, n, q), (private_floor, shadow) in private_rows.items():
        require(q == 2, (m, excess, n, q))
        reconstructed = ceil((m * m - excess) / 2)
        require(reconstructed == private_floor, (m, reconstructed, private_floor))
        require(private_floor >= 2 and shadow > n, (m, private_floor, shadow, n))

    for m, excess, n, q in pair_exceptions:
        relation_floor = ceil(m * m / (q - 1))
        margin = m * m - (q - 2) * n
        support = 2 * n
        require(relation_floor <= excess, (m, relation_floor, excess))
        require(margin > 0, (m, margin))
        require(support < (m - 1) ** 2, (m, support, (m - 1) ** 2))

    print(f"independent_row_count={row_count}")
    print(
        "independent_rows_by_extra="
        + ",".join(f"{key}:{counts[key]}" for key in sorted(counts))
    )
    print(f"independent_rectangle_pair_checks={rectangle_checks}")
    print("independent_private_exceptions=3")
    print("independent_pair_supported_exceptions=3")
    print("GENERAL_EXCESS_M_PLUS_FOUR_BAND_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
