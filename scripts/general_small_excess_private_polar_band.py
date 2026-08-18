#!/usr/bin/env python3
"""Exact arithmetic replay for the private-polar small-excess band.

The proof is in docs/general_small_excess_private_polar_band.md.  This script
scans every legal divisor row with

    3 <= m <= maximum_m,
    q >= 2,
    0 <= s = q*n-m^2 <= m-1,

checks the private-direction dimension inequality, verifies the strict
one-derivative gap for m>=5, and freezes the unique quartic order-two shadow
boundary.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "data" / "general_small_excess_private_polar_band_boundary.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def divisors(value: int) -> tuple[int, ...]:
    require(value >= 1, value)
    lower: list[int] = []
    upper: list[int] = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        lower.append(candidate)
        partner = value // candidate
        if partner != candidate:
            upper.append(partner)
    return tuple(lower + upper[::-1])


def legal_rows(maximum_m: int) -> tuple[dict[str, int | bool | str], ...]:
    require(maximum_m >= 3, maximum_m)
    rows: list[dict[str, int | bool | str]] = []
    for m in range(3, maximum_m + 1):
        for excess in range(0, m):
            total = m * m + excess
            for n in divisors(total):
                q = total // n
                if n < m or q < 2:
                    continue
                private_count_forced = q * excess < m * m
                strict_derivative_gap = n < (m - 1) ** 2
                if excess <= 1:
                    route = "INHERITED_ENDPOINT_OR_FIRST_EXCESS"
                elif strict_derivative_gap:
                    route = "PRIVATE_POLAR_STRICT_DESCENT"
                elif (n, m, q, excess) == (9, 4, 2, 2):
                    route = "QUARTIC_ORDER_TWO_SHADOW"
                else:
                    route = "UNCLASSIFIED"
                rows.append(
                    {
                        "n": n,
                        "m": m,
                        "q": q,
                        "excess": excess,
                        "total": total,
                        "private_count_forced": private_count_forced,
                        "strict_derivative_gap": strict_derivative_gap,
                        "route": route,
                    }
                )
    return tuple(rows)


def rectangle_union_minimum(
    ground_size: int,
    subset_size: int,
) -> tuple[int, int, int]:
    """Minimum union of two distinct Cartesian subset rectangles."""

    require(ground_size >= subset_size >= 1, (ground_size, subset_size))
    single = subset_size * subset_size
    maximum_intersection = 0
    for row_overlap in range(subset_size + 1):
        for column_overlap in range(subset_size + 1):
            if row_overlap == subset_size and column_overlap == subset_size:
                continue
            if 2 * subset_size - row_overlap > ground_size:
                continue
            if 2 * subset_size - column_overlap > ground_size:
                continue
            maximum_intersection = max(
                maximum_intersection,
                row_overlap * column_overlap,
            )
    return single, maximum_intersection, 2 * single - maximum_intersection


def zeta_polar(n: int, m: int) -> int:
    require(n >= m >= 3, (n, m))
    return (m * m + m - 1) // n


def canonical_hash(value: object) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_payload(maximum_m: int = 128) -> dict[str, Any]:
    rows = legal_rows(maximum_m)
    require(rows, "empty small-excess scan")

    positive = [row for row in rows if int(row["excess"]) >= 1]
    require(
        all(bool(row["private_count_forced"]) for row in positive),
        [row for row in positive if not bool(row["private_count_forced"])],
    )

    strict_new = [
        row
        for row in rows
        if int(row["m"]) >= 5 and int(row["excess"]) >= 2
    ]
    require(
        all(bool(row["strict_derivative_gap"]) for row in strict_new),
        [row for row in strict_new if not bool(row["strict_derivative_gap"])],
    )

    unclassified = [row for row in rows if row["route"] == "UNCLASSIFIED"]
    require(not unclassified, unclassified)

    quartic_boundary = [
        row
        for row in rows
        if row["route"] == "QUARTIC_ORDER_TWO_SHADOW"
    ]
    require(
        quartic_boundary
        == [
            {
                "n": 9,
                "m": 4,
                "q": 2,
                "excess": 2,
                "total": 18,
                "private_count_forced": True,
                "strict_derivative_gap": False,
                "route": "QUARTIC_ORDER_TWO_SHADOW",
            }
        ],
        quartic_boundary,
    )

    cubic_excess_two = [
        row for row in rows if int(row["m"]) == 3 and int(row["excess"]) == 2
    ]
    require(cubic_excess_two == [], cubic_excess_two)

    single, maximum_intersection, minimum_union = rectangle_union_minimum(9, 3)
    require(single == 9, single)
    require(maximum_intersection == 6, maximum_intersection)
    require(minimum_union == 12, minimum_union)

    quartic_component_floor = 8
    quartic_relation_cap = 2
    quartic_private_floor = quartic_component_floor - quartic_relation_cap
    require(quartic_private_floor == 6, quartic_private_floor)
    require(quartic_private_floor >= 2, quartic_private_floor)
    require(minimum_union > 9, minimum_union)

    selected_rows = {
        "m3": [row for row in rows if int(row["m"]) == 3],
        "m4": [row for row in rows if int(row["m"]) == 4],
        "m5": [row for row in rows if int(row["m"]) == 5],
    }

    core = {
        "status": [
            "GENERAL_PRIVATE_POLAR_SMALL_EXCESS_ZERO_BAND",
            "EXCESS_ZERO_THROUGH_M_MINUS_ONE",
            "QUARTIC_ORDER_TWO_SHADOW_BOUNDARY_CLOSED",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "closed_band": (
                "For m>=3, q>=2 and q*n<=m^2+m-1, every q-term Chow "
                "block has zero intersection with D_m(perm_n)."
            ),
            "zero_block": (
                "zeta_pol(n,m)=floor((m^2+m-1)/n), whenever the displayed "
                "integer is at least two."
            ),
            "next_open_band": "q*n=m^2+m.",
        },
        "private_polar": {
            "relation_defect_cap": "k<=s",
            "private_dimension": "dim S_i=r_i-t_i>=r_i-k",
            "large_component_condition": "some r_i>s for 0<=s<=m-1",
        },
        "quartic_boundary": {
            "n": 9,
            "m": 4,
            "q": 2,
            "excess": 2,
            "component_dimension_floor": quartic_component_floor,
            "relation_defect_cap": quartic_relation_cap,
            "private_polar_dimension_floor": quartic_private_floor,
            "single_rectangle_size": single,
            "maximum_distinct_rectangle_intersection": maximum_intersection,
            "minimum_two_rectangle_union": minimum_union,
        },
        "selected_rows": selected_rows,
        "scan": {
            "maximum_m": maximum_m,
            "row_count": len(rows),
            "positive_excess_row_count": len(positive),
            "strict_new_row_count": len(strict_new),
            "rows": list(rows),
        },
        "selected_zero_block_examples": [
            {"n": 5, "m": 3, "zeta_pol": zeta_polar(5, 3)},
            {"n": 9, "m": 4, "zeta_pol": zeta_polar(9, 4)},
            {"n": 7, "m": 5, "zeta_pol": zeta_polar(7, 5)},
            {"n": 14, "m": 5, "zeta_pol": zeta_polar(14, 5)},
            {"n": 10, "m": 7, "zeta_pol": zeta_polar(10, 7)},
        ],
        "claim_boundary": (
            "This is an ordinary characteristic-zero zero-intersection "
            "theorem for factor-span excess through m-1. It does not prove "
            "an exact Chow rank, optimize every finite-n numerical bound, "
            "improve border rank or establish literature novelty."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-m", type=int, default=128)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload(args.maximum_m)
    if BOUNDARY.exists() and args.maximum_m == 128:
        frozen = json.loads(BOUNDARY.read_text(encoding="utf-8"))
        for key in (
            "status",
            "theorem",
            "private_polar",
            "quartic_boundary",
            "selected_zero_block_examples",
            "claim_boundary",
        ):
            require(frozen[key] == payload[key], ("frozen mismatch", key))

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_SMALL_EXCESS_PRIVATE_POLAR_BAND_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
