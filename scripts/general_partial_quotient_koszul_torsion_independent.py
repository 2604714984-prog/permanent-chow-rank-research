#!/usr/bin/env python3
"""Independent ordered-monomial replay for partial quotient Koszul torsion."""
from itertools import combinations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def direct_count(
    r: int,
    quadratic_axes: tuple[int, ...],
    quotient_axes: tuple[int, ...],
) -> int:
    a = frozenset(quadratic_axes)
    b = frozenset(quotient_axes)
    vi2 = {(i, j) for i in a for j in range(r)}
    intersection = {(i, j) for i, j in vi2 if i in b or j in b}
    wi2 = {(i, j) for i, j in vi2 if j in b}
    return len(intersection - wi2)


def main() -> None:
    flags_checked = 0
    for r in range(1, 9):
        for q in range(r + 1):
            for d in range(r + 1):
                maximum = -1
                for a in combinations(range(r), q):
                    for b in combinations(range(r), d):
                        flags_checked += 1
                        maximum = max(maximum, direct_count(r, a, b))
                require(maximum == (r - d) * min(q, d), (r, q, d, maximum))

    for r in range(2, 13):
        for support_size in range(1, r + 1):
            q = r - support_size + (1 if support_size == 2 else 0)
            for d in range(r + 1):
                require((r - d) * min(q, d) <= d * (r - d), (r, support_size, d))

    print(
        "GENERAL_PARTIAL_QUOTIENT_KOSZUL_TORSION_INDEPENDENT_PASS",
        flags_checked,
    )


if __name__ == "__main__":
    main()
