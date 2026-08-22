#!/usr/bin/env python3
"""Independent bit-mask audit of the two slope-ten coordinate tables."""

from __future__ import annotations

import itertools


EXPECTED = {
    (3, 1, 1, 1, 1): (0, 12, 17, 21, 24, 27),
    (2, 2, 1, 1, 1): (0, 15, 22, 24, 30, 34),
    (2, 1, 1, 1, 1, 1): (0, 22, 33, 37, 41, 44, 48),
    (1, 1, 1, 1, 1, 1, 1): (0, 32, 49, 56, 57, 64, 67, 69),
}


def compositions_with_caps(caps, total):
    for vector in itertools.product(*(range(cap + 1) for cap in caps)):
        if sum(vector) == total:
            yield vector


def audit(caps):
    n = len(caps)
    level2 = tuple(compositions_with_caps(caps, 2))
    level3 = tuple(compositions_with_caps(caps, 3))
    level4 = tuple(compositions_with_caps(caps, 4))
    index2 = {vector: index for index, vector in enumerate(level2)}
    derivatives = {}
    for cubic_index, cubic in enumerate(level3):
        for variable in range(n):
            if not cubic[variable]:
                continue
            quadratic = list(cubic)
            quadratic[variable] -= 1
            derivatives[cubic_index, variable] = index2[tuple(quadratic)]
    answer = []
    for d in range(n + 1):
        minimum = 10**9
        for active in itertools.combinations(range(n), d):
            active_mask = sum(1 << variable for variable in active)
            plus = sum(
                bool(
                    active_mask
                    & sum(
                        (1 << variable)
                        for variable, exponent in enumerate(quartic)
                        if exponent
                    )
                )
                for quartic in level4
            )
            for relation_size in range(4):
                for relation_indices in itertools.combinations(
                    range(len(level2)), relation_size
                ):
                    relation_mask = sum(
                        1 << index for index in relation_indices
                    )
                    killed = 0
                    for cubic_index, cubic in enumerate(level3):
                        survives = True
                        for variable in active:
                            if not cubic[variable]:
                                continue
                            edge = derivatives[cubic_index, variable]
                            if not relation_mask & (1 << edge):
                                survives = False
                                break
                        killed += survives
                    minimum = min(minimum, plus + len(level3) - killed)
        answer.append(minimum)
    return tuple(answer)


def main() -> None:
    for caps, expected in EXPECTED.items():
        assert audit(caps) == expected
    print("PASS independent slope-ten coordinate-table audit")


if __name__ == "__main__":
    main()
