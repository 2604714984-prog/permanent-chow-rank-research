#!/usr/bin/env python3
"""Independent arithmetic replay for the first-excess reduction.

This implementation imports none of the primary audit helpers.  It scans
integer triples directly and verifies the strict derivative inequality used by
the proof.
"""

from __future__ import annotations


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    rows: list[tuple[int, int, int]] = []
    closed = 0
    for m in range(3, 257):
        target = m * m + 1
        for n in range(m, target + 1):
            if target % n:
                continue
            q = target // n
            if q < 2:
                continue
            rows.append((n, m, q))
            if m >= 4:
                require(
                    n < (m - 1) * (m - 1),
                    ("derivative gap failed", n, m, q),
                )
                closed += 1

    cubic = [row for row in rows if row[1] == 3]
    require(cubic == [(5, 3, 2)], cubic)

    selected = {
        5: [(13, 5, 2)],
        7: [(10, 7, 5), (25, 7, 2)],
        8: [(13, 8, 5)],
        12: [(29, 12, 5)],
        13: [(17, 13, 10), (34, 13, 5), (85, 13, 2)],
    }
    for m, expected in selected.items():
        actual = [row for row in rows if row[1] == m]
        require(actual == expected, (m, actual, expected))

    print(f"independent_first_excess_rows={len(rows)}")
    print(f"independent_closed_rows_m_ge_4={closed}")
    print("independent_cubic_exception=(5,3,2)")
    print("GENERAL_FIRST_EXCESS_CIRCUIT_REDUCTION_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
