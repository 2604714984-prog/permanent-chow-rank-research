#!/usr/bin/env python3
"""Exact arithmetic replay for the excess-m simplex reduction.

The proof is in docs/general_excess_m_simplex_reduction.md.  The script scans
all divisor rows with q*n=m^2+m, identifies the cubic boundary, verifies the
strict private-polar gap for m>=5, and freezes the quartic q=2 order-two shadow
interface.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "data" / "general_excess_m_simplex_reduction_boundary.json"


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


def excess_m_rows(maximum_m: int) -> tuple[dict[str, int | bool | str], ...]:
    require(maximum_m >= 3, maximum_m)
    rows: list[dict[str, int | bool | str]] = []
    for m in range(3, maximum_m + 1):
        total = m * m + m
        for n in divisors(total):
            q = total // n
            if n < m or q < 2:
                continue
            strict_private_gap = n < (m - 1) ** 2
            simplex_support_gap = 2 * m < (m - 1) ** 2
            if m == 3:
                route = "OPEN_CUBIC_BOUNDARY"
            elif m == 4 and (n, q) == (10, 2):
                route = "QUARTIC_ORDER_TWO_PRIVATE_SHADOW"
            elif strict_private_gap:
                route = "PRIVATE_STRICT_OR_SIMPLEX_DIFFERENCE"
            else:
                route = "UNCLASSIFIED"
            rows.append(
                {
                    "n": n,
                    "m": m,
                    "q": q,
                    "total": total,
                    "strict_private_gap": strict_private_gap,
                    "simplex_support_gap": simplex_support_gap,
                    "route": route,
                }
            )
    return tuple(rows)


def rectangle_union_minimum(ground_size: int, subset_size: int) -> tuple[int, int, int]:
    require(ground_size >= subset_size >= 1, (ground_size, subset_size))
    single = subset_size**2
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


def zeta_m(n: int, m: int) -> int:
    require(n >= m >= 4, (n, m))
    return (m * m + m) // n


def canonical_hash(value: object) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_payload(maximum_m: int = 128) -> dict[str, Any]:
    rows = excess_m_rows(maximum_m)
    require(rows, "empty excess-m scan")

    cubic_rows = [row for row in rows if int(row["m"]) == 3]
    require(
        [(row["n"], row["q"]) for row in cubic_rows]
        == [(3, 4), (4, 3), (6, 2)],
        cubic_rows,
    )
    require(
        all(row["route"] == "OPEN_CUBIC_BOUNDARY" for row in cubic_rows),
        cubic_rows,
    )

    m_ge_five = [row for row in rows if int(row["m"]) >= 5]
    require(
        all(bool(row["strict_private_gap"]) for row in m_ge_five),
        [row for row in m_ge_five if not bool(row["strict_private_gap"])],
    )
    require(
        all(bool(row["simplex_support_gap"]) for row in m_ge_five),
        [row for row in m_ge_five if not bool(row["simplex_support_gap"])],
    )

    quartic_rows = [row for row in rows if int(row["m"]) == 4]
    require(
        [(row["n"], row["q"]) for row in quartic_rows]
        == [(4, 5), (5, 4), (10, 2)],
        quartic_rows,
    )
    require(
        [row for row in quartic_rows if row["route"] == "QUARTIC_ORDER_TWO_PRIVATE_SHADOW"]
        == [
            {
                "n": 10,
                "m": 4,
                "q": 2,
                "total": 20,
                "strict_private_gap": False,
                "simplex_support_gap": True,
                "route": "QUARTIC_ORDER_TWO_PRIVATE_SHADOW",
            }
        ],
        quartic_rows,
    )

    unclassified = [row for row in rows if row["route"] == "UNCLASSIFIED"]
    require(not unclassified, unclassified)

    single, maximum_intersection, minimum_union = rectangle_union_minimum(10, 3)
    require((single, maximum_intersection, minimum_union) == (9, 6, 12), (single, maximum_intersection, minimum_union))

    quartic_private_sum_floor = 12
    quartic_private_max_floor = 6
    require(quartic_private_max_floor >= 2, quartic_private_max_floor)
    require(minimum_union > 10, minimum_union)

    core = {
        "status": [
            "GENERAL_EXCESS_M_ZERO_THEOREM_ABOVE_CUBIC_DEGREE",
            "NO_PRIVATE_DIRECTION_SIMPLEX_CLASSIFIED",
            "TWO_BLOCK_POLAR_DIFFERENCE_EXCLUSION",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "closed_range": (
                "For m>=4, q>=2 and q*n<=m^2+m, every q-term Chow block "
                "has zero intersection with D_m(perm_n)."
            ),
            "zero_block": (
                "zeta_m(n,m)=floor((m^2+m)/n), for m>=4 whenever the "
                "displayed integer is at least two."
            ),
            "cubic_boundary": (
                "The excess-m cubic rows (n,q)=(6,2),(4,3),(3,4) remain open."
            ),
            "next_open_above_cubic": "q*n=m^2+m+1.",
        },
        "simplex": {
            "no_private_forces": (
                "q=m+1, n=m, relation defect k=m, every component essential "
                "dimension m and every proper subcollection direct."
            ),
            "difference_support_dimension": "2*m",
            "strict_support_gap": "2*m<(m-1)^2 for m>=4",
        },
        "quartic_boundary": {
            "n": 10,
            "m": 4,
            "q": 2,
            "relation_defect_cap": 4,
            "sum_private_polar_dimension_floor": quartic_private_sum_floor,
            "one_private_polar_dimension_floor": quartic_private_max_floor,
            "single_rectangle_size": single,
            "maximum_distinct_rectangle_intersection": maximum_intersection,
            "minimum_two_rectangle_union": minimum_union,
        },
        "cubic_rows": cubic_rows,
        "scan": {
            "maximum_m": maximum_m,
            "row_count": len(rows),
            "closed_row_count_m_ge_4": len([row for row in rows if int(row["m"]) >= 4]),
            "open_cubic_row_count": len(cubic_rows),
            "rows": list(rows),
        },
        "selected_zero_block_examples": [
            {"n": 4, "m": 4, "zeta_m": zeta_m(4, 4)},
            {"n": 5, "m": 4, "zeta_m": zeta_m(5, 4)},
            {"n": 10, "m": 4, "zeta_m": zeta_m(10, 4)},
            {"n": 6, "m": 5, "zeta_m": zeta_m(6, 5)},
            {"n": 10, "m": 5, "zeta_m": zeta_m(10, 5)},
        ],
        "claim_boundary": (
            "This is an ordinary characteristic-zero zero-intersection "
            "theorem through excess m in output degree at least four. It "
            "does not close the cubic excess-m rows, prove an exact Chow "
            "rank, optimize every finite-n numerical bound, improve border "
            "rank or establish literature novelty."
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
            "simplex",
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
    print("GENERAL_EXCESS_M_SIMPLEX_REDUCTION_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
