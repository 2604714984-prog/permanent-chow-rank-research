#!/usr/bin/env python3
"""Independent coordinate complete-intersection replay."""
from itertools import combinations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def count(r: int, a: tuple[int, ...], b: tuple[int, ...]) -> int:
    aa, bb = set(a), set(b)
    return sum(1 for i in aa & bb for j in range(r) if j not in bb)


def main() -> None:
    checked = 0
    for r in range(1, 11):
        for q in range(r + 1):
            for d in range(r + 1):
                maximum = -1
                for a in combinations(range(r), q):
                    for b in combinations(range(r), d):
                        checked += 1
                        maximum = max(maximum, count(r, a, b))
                require(maximum == (r - d) * min(q, d), (r, q, d, maximum))
    print("GENERAL_PARTIAL_QUOTIENT_REGULAR_SEQUENCE_CAP_INDEPENDENT_PASS", checked)


if __name__ == "__main__":
    main()
