#!/usr/bin/env python3
"""Exact arithmetic replay for the first-excess circuit reduction.

The mathematical proof is in docs/general_first_excess_circuit_reduction.md.
The script checks every divisor interface with

    q*n = m^2 + 1,
    3 <= m <= n,
    q >= 2,

through a configurable output-degree range.  It verifies that the derivative
step used by the proof is strict for every m >= 4 and isolates the unique
cubic exception (n,m,q)=(5,3,2).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any, Iterable


FROZEN = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "general_first_excess_circuit_reduction.json"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def positive_divisors(value: int) -> tuple[int, ...]:
    require(value >= 1, value)
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        partner = value // divisor
        if partner != divisor:
            upper.append(partner)
    return tuple(lower + upper[::-1])


def first_excess_rows(maximum_m: int) -> tuple[dict[str, int | bool], ...]:
    require(maximum_m >= 3, maximum_m)
    rows: list[dict[str, int | bool]] = []
    for m in range(3, maximum_m + 1):
        total = m * m + 1
        for n in positive_divisors(total):
            q = total // n
            if n < m or q < 2:
                continue
            derivative_gap = n < (m - 1) ** 2
            rows.append(
                {
                    "n": n,
                    "m": m,
                    "q": q,
                    "first_excess": total,
                    "derivative_gap": derivative_gap,
                }
            )
    return tuple(rows)


def rows_for_m(rows: Iterable[dict[str, int | bool]], m: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (int(row["n"]), int(row["q"]))
        for row in rows
        if int(row["m"]) == m
    )


def zeta_plus(n: int, m: int) -> int:
    require(n >= m >= 4, (n, m))
    return (m * m + 1) // n


def exact_ledger_branches() -> dict[str, dict[str, int | str]]:
    """The four one-hot branches of a+b+c+d=1 and their disposition."""

    return {
        "factor_rank_deficit": {
            "a": 1,
            "b": 0,
            "c": 0,
            "d": 0,
            "status": "EXCLUDED_BY_CLOSED_ENDPOINT",
        },
        "factor_span_overlap": {
            "a": 0,
            "b": 1,
            "c": 0,
            "d": 0,
            "status": "FULL_SUPPORT_CIRCUIT_THEN_DERIVATIVE_DESCENT",
        },
        "unused_joint_span": {
            "a": 0,
            "b": 0,
            "c": 1,
            "d": 0,
            "status": "EXCLUDED_BY_HYPERPLANE_ANNIHILATOR",
        },
        "permanent_shadow_excess": {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 1,
            "status": "DIRECT_SUM_THEN_DERIVATIVE_DESCENT",
        },
    }


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_payload(maximum_m: int = 128) -> dict[str, Any]:
    rows = first_excess_rows(maximum_m)

    cubic_rows = tuple(row for row in rows if int(row["m"]) == 3)
    require(
        cubic_rows
        == (
            {
                "n": 5,
                "m": 3,
                "q": 2,
                "first_excess": 10,
                "derivative_gap": False,
            },
        ),
        cubic_rows,
    )

    closed_rows = tuple(row for row in rows if int(row["m"]) >= 4)
    require(closed_rows, "no m>=4 first-excess rows")
    require(
        all(bool(row["derivative_gap"]) for row in closed_rows),
        tuple(row for row in closed_rows if not bool(row["derivative_gap"])),
    )

    expected_selected = {
        3: ((5, 2),),
        4: (),
        5: ((13, 2),),
        6: (),
        7: ((10, 5), (25, 2)),
        8: ((13, 5),),
        9: ((41, 2),),
        10: (),
        11: ((61, 2),),
        12: ((29, 5),),
        13: ((17, 10), (34, 5), (85, 2)),
    }
    for m, expected in expected_selected.items():
        require(rows_for_m(rows, m) == expected, (m, rows_for_m(rows, m), expected))

    branches = exact_ledger_branches()
    for name, branch in branches.items():
        require(
            sum(int(branch[key]) for key in ("a", "b", "c", "d")) == 1,
            (name, branch),
        )

    core = {
        "status": [
            "GENERAL_FIRST_POSITIVE_EXCESS_ZERO_THEOREM",
            "FULL_SUPPORT_CIRCUIT_REDUCTION",
            "DERIVATIVE_DESCENT",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "first_excess": (
                "For m>=4, q>=2 and q*n=m^2+1, every q-term Chow block "
                "has zero intersection with D_m(perm_n)."
            ),
            "closed_range": (
                "For m>=4 and q>=2, q*n<=m^2+1 implies zero intersection."
            ),
            "zero_block": "zeta_plus(n,m)=floor((m^2+1)/n), when zeta_plus>=2.",
            "cubic_exception": "The only unresolved first-excess triple is (n,m,q)=(5,3,2).",
        },
        "ledger_branches": branches,
        "selected_rows": {
            str(m): [{"n": n, "q": q} for n, q in values]
            for m, values in expected_selected.items()
        },
        "scan": {
            "maximum_m": maximum_m,
            "first_excess_rows": len(rows),
            "closed_rows_m_ge_4": len(closed_rows),
            "cubic_exception_rows": len(cubic_rows),
            "rows": list(rows),
        },
        "claim_boundary": (
            "This is an ordinary characteristic-zero zero-intersection theorem "
            "for the first positive factor-span excess in output degree at "
            "least four. It does not resolve (5,3,2), prove a new exact Chow "
            "rank, improve border rank or establish literature novelty."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-m", type=int, default=128)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload(args.maximum_m)

    if FROZEN.exists() and args.maximum_m == 128:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        for key in ("status", "theorem", "ledger_branches", "selected_rows", "claim_boundary"):
            require(frozen[key] == payload[key], ("frozen mismatch", key))

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_FIRST_EXCESS_CIRCUIT_REDUCTION_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
