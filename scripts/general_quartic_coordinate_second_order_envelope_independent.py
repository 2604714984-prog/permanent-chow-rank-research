#!/usr/bin/env python3
"""Independent bit-mask replay for the corrected second-order envelope."""

from __future__ import annotations

from itertools import combinations, permutations

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


def degree_maxima(values: tuple[int, ...]) -> tuple[int, int]:
    rows = [0] * ORDER
    columns = [0] * ORDER
    for cell in values:
        rows[cell // ORDER] += 1
        columns[cell % ORDER] += 1
    return max(rows), max(columns)


def main() -> int:
    checked = 0
    maximum = -1
    equality_count = 0
    capped_maximum = -1
    capped_equality_count = 0

    for size in range(7):
        for values in combinations(range(16), size):
            checked += 1
            mask = sum(1 << cell for cell in values)
            direct_count = sum((matching & mask) == matching for matching in MATCHINGS)
            envelope_count = sum(
                (matching & mask).bit_count() >= 2 for matching in MATCHINGS
            )
            r2 = sum(
                1
                for subset in combinations(values, 2)
                if len({cell // ORDER for cell in subset}) == 2
                and len({cell % ORDER for cell in subset}) == 2
            )
            r3 = sum(
                1
                for subset in combinations(values, 3)
                if len({cell // ORDER for cell in subset}) == 3
                and len({cell % ORDER for cell in subset}) == 3
            )
            require(
                envelope_count == 2 * r2 - 2 * r3 + 3 * direct_count,
                (values, envelope_count, r2, r3, direct_count),
            )
            if envelope_count > maximum:
                maximum = envelope_count
                equality_count = 1
            elif envelope_count == maximum:
                equality_count += 1

            row_maximum, column_maximum = degree_maxima(values)
            if row_maximum <= 2 and column_maximum <= 2:
                if envelope_count > capped_maximum:
                    capped_maximum = envelope_count
                    capped_equality_count = 1
                elif envelope_count == capped_maximum:
                    capped_equality_count += 1

    require(checked == 14_893, checked)
    require((maximum, equality_count) == (18, 16), (maximum, equality_count))
    require(
        (capped_maximum, capped_equality_count) == (14, 96),
        (capped_maximum, capped_equality_count),
    )
    print("GENERAL_QUARTIC_COORDINATE_SECOND_ORDER_ENVELOPE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
