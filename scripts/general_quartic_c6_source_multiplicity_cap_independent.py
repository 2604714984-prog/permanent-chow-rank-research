#!/usr/bin/env python3
"""Independent bit-mask replay for the C6 source-multiplicity cap."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    frame_masks = set()
    for rows in combinations(range(4), 3):
        for columns in combinations(range(4), 3):
            for missing_columns in permutations(columns):
                mask = 0
                missing = {(rows[index], missing_columns[index]) for index in range(3)}
                for row in rows:
                    for column in columns:
                        if (row, column) not in missing:
                            mask |= 1 << (4 * row + column)
                require(mask.bit_count() == 6, mask)
                frame_masks.add(mask)
    require(len(frame_masks) == 96, len(frame_masks))

    sources = Counter()
    for frame in frame_masks:
        cells = [cell for cell in range(16) if frame >> cell & 1]
        for subset in combinations(cells, 4):
            source = sum(1 << cell for cell in subset)
            sources[source] += 1

    require(len(sources) == 1008, len(sources))
    require(sum(sources.values()) == 1440, sum(sources.values()))
    require(Counter(sources.values()) == Counter({1: 576, 2: 432}), Counter(sources.values()))
    require(max(sources.values()) == 2, max(sources.values()))
    print("GENERAL_QUARTIC_C6_SOURCE_MULTIPLICITY_CAP_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
