#!/usr/bin/env python3
"""Independent recurrence replay for the even middle-symbol capacity ceiling."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def central_rows(max_n: int) -> list[dict[str, int | bool]]:
    # C(2m,m) recurrence: C(2m+2,m+1)=C(2m,m)*2(2m+1)/(m+1).
    c = 6  # C(4,2)
    rows = []
    for n in range(4, max_n + 1, 2):
        if n > 4:
            m = n // 2 - 1
            numerator = c * 2 * (2 * m + 1)
            require(numerator % (m + 1) == 0, (n, c))
            c = numerator // (m + 1)
        ceiling = c + 2 * n
        target = 1 << (n - 1)
        rows.append(
            {
                "n": n,
                "central": c,
                "ceiling": ceiling,
                "target": target,
                "gap": max(0, target - ceiling),
                "capacity": ceiling >= target,
            }
        )
    return rows


def replay(max_n: int) -> dict[str, object]:
    require(max_n >= 8 and max_n % 2 == 0, max_n)
    rows = central_rows(max_n)
    require(
        rows[1]
        == {
            "n": 6,
            "central": 20,
            "ceiling": 32,
            "target": 32,
            "gap": 0,
            "capacity": True,
        },
        rows[1],
    )
    require(all(not item["capacity"] for item in rows if item["n"] >= 8), rows)
    for left, right in zip(rows, rows[1:]):
        require(
            right["ceiling"] * left["target"]
            <= left["ceiling"] * right["target"],
            (left, right),
        )
    return {
        "max_n": max_n,
        "rows": rows,
        "n6_exact_capacity_match": True,
        "strict_failure_from_n8": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=64)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = replay(args.max_n)
    if args.json is not None:
        args.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_EVEN_MIDDLE_SYMBOL_CAPACITY_CEILING_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
