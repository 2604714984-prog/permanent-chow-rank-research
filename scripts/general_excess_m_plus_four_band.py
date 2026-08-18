#!/usr/bin/env python3
"""Exact arithmetic audit for the post-simplex small-excess zero band.

The proof is in ``docs/general_excess_m_plus_four_band.md``.  Starting from
PR #76, the new theorem closes

    q*n <= m^2+m+3  for m>=4,
    q*n <= m^2+m+4  for m>=5.

The script scans every legal divisor row, verifies the private-polar strict
descent or the exact two-plane shadow exceptions, and checks the no-private
arithmetic or the three pair-supported polar exceptions.

All calculations are exact integers.  The finite scan checks the arithmetic
interface; the written private-polar and pair-supported-polar arguments prove
the theorem for all dimensions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import ceil, isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "data" / "general_excess_m_plus_four_band_boundary.json"
EXPECTED_CORE_SHA256 = "22459deec3fadc4cff91ae9cc6aa731414dc733ade453093bdd91812d2bcb25d"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def divisors(value: int) -> tuple[int, ...]:
    require(value >= 1, value)
    low: list[int] = []
    high: list[int] = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        low.append(candidate)
        partner = value // candidate
        if partner != candidate:
            high.append(partner)
    return tuple(low + high[::-1])


def rectangle_pair_shadow(output_degree: int) -> int:
    """Order-(d-1) shadow of two extremal distinct d x d rectangles."""

    require(output_degree >= 2, output_degree)
    return output_degree * (output_degree + 1)


def legal_new_rows(maximum_m: int) -> tuple[dict[str, Any], ...]:
    require(maximum_m >= 5, maximum_m)
    rows: list[dict[str, Any]] = []
    for m in range(4, maximum_m + 1):
        largest_extra = 3 if m == 4 else 4
        for extra in range(1, largest_extra + 1):
            excess = m + extra
            total = m * m + excess
            for n in divisors(total):
                q = total // n
                if n < m or q < 2:
                    continue

                strict_private_gap = n < (m - 1) ** 2
                arithmetic_no_private = (q - 1) * excess < m * m

                private_shadow_route = (
                    (m, excess, n, q)
                    in {
                        (4, 6, 11, 2),
                        (5, 7, 16, 2),
                        (5, 9, 17, 2),
                    }
                )
                pair_supported_route = (
                    (m, excess, n, q)
                    in {
                        (6, 9, 9, 5),
                        (7, 11, 10, 6),
                        (12, 16, 16, 10),
                    }
                )

                if strict_private_gap:
                    private_route = "STRICT_PRIVATE_POLAR_DESCENT"
                elif private_shadow_route:
                    private_route = "EXACT_TWO_PLANE_ITERATED_SHADOW"
                else:
                    private_route = "UNCLASSIFIED_PRIVATE_BRANCH"

                if arithmetic_no_private:
                    no_private_route = "NO_PRIVATE_DIMENSION_ARITHMETIC"
                elif pair_supported_route:
                    no_private_route = "PAIR_SUPPORTED_POLAR_DESCENT"
                else:
                    no_private_route = "UNCLASSIFIED_NO_PRIVATE_BRANCH"

                rows.append(
                    {
                        "m": m,
                        "n": n,
                        "q": q,
                        "excess": excess,
                        "extra_above_m": extra,
                        "total": total,
                        "strict_private_gap": strict_private_gap,
                        "arithmetic_no_private": arithmetic_no_private,
                        "private_route": private_route,
                        "no_private_route": no_private_route,
                    }
                )
    return tuple(rows)


def private_shadow_exception(
    m: int,
    excess: int,
    n: int,
    q: int,
) -> dict[str, int]:
    require(q == 2, (m, excess, n, q))
    private_sum_floor = m * m - excess
    largest_private_floor = ceil(private_sum_floor / 2)
    lower_output_degree = m - 1
    two_plane_shadow = rectangle_pair_shadow(lower_output_degree)
    require(largest_private_floor >= 2, (m, excess, largest_private_floor))
    require(two_plane_shadow > n, (m, excess, n, two_plane_shadow))
    return {
        "m": m,
        "n": n,
        "q": q,
        "excess": excess,
        "private_sum_floor": private_sum_floor,
        "largest_private_floor": largest_private_floor,
        "lower_output_degree": lower_output_degree,
        "two_plane_iterated_shadow": two_plane_shadow,
        "component_variable_cap": n,
    }


def pair_supported_exception(
    m: int,
    excess: int,
    n: int,
    q: int,
) -> dict[str, int]:
    relation_defect_floor = ceil((m * m) / (q - 1))
    pair_annihilator_margin = m * m - (q - 2) * n
    two_block_support = 2 * n
    lower_shadow_floor = (m - 1) ** 2
    require(relation_defect_floor <= excess, (m, excess, relation_defect_floor))
    require(pair_annihilator_margin > 0, (m, n, q, pair_annihilator_margin))
    require(two_block_support < lower_shadow_floor, (
        m,
        n,
        two_block_support,
        lower_shadow_floor,
    ))
    return {
        "m": m,
        "n": n,
        "q": q,
        "excess": excess,
        "relation_defect_floor": relation_defect_floor,
        "relation_defect_cap": excess,
        "pair_annihilator_margin": pair_annihilator_margin,
        "two_block_support": two_block_support,
        "lower_output_shadow_floor": lower_shadow_floor,
    }


def zero_block_size(n: int, m: int) -> int:
    require(n >= m >= 4, (n, m))
    numerator = m * m + m + (3 if m == 4 else 4)
    return numerator // n


def build_payload(maximum_m: int = 128) -> dict[str, Any]:
    rows = legal_new_rows(maximum_m)
    require(rows, "empty post-simplex scan")

    private_unclassified = [
        row for row in rows if row["private_route"] == "UNCLASSIFIED_PRIVATE_BRANCH"
    ]
    no_private_unclassified = [
        row
        for row in rows
        if row["no_private_route"] == "UNCLASSIFIED_NO_PRIVATE_BRANCH"
    ]
    require(not private_unclassified, private_unclassified)
    require(not no_private_unclassified, no_private_unclassified)

    private_exception_rows = [
        row
        for row in rows
        if row["private_route"] == "EXACT_TWO_PLANE_ITERATED_SHADOW"
    ]
    expected_private = [
        (4, 6, 11, 2),
        (5, 7, 16, 2),
        (5, 9, 17, 2),
    ]
    require(
        [(row["m"], row["excess"], row["n"], row["q"]) for row in private_exception_rows]
        == expected_private,
        private_exception_rows,
    )
    private_exceptions = [
        private_shadow_exception(*values)
        for values in expected_private
    ]

    pair_exception_rows = [
        row
        for row in rows
        if row["no_private_route"] == "PAIR_SUPPORTED_POLAR_DESCENT"
    ]
    expected_pairs = [
        (6, 9, 9, 5),
        (7, 11, 10, 6),
        (12, 16, 16, 10),
    ]
    require(
        [(row["m"], row["excess"], row["n"], row["q"]) for row in pair_exception_rows]
        == expected_pairs,
        pair_exception_rows,
    )
    pair_exceptions = [pair_supported_exception(*values) for values in expected_pairs]

    require(rectangle_pair_shadow(3) == 12, rectangle_pair_shadow(3))
    require(rectangle_pair_shadow(4) == 20, rectangle_pair_shadow(4))

    by_extra = {
        str(extra): [row for row in rows if row["extra_above_m"] == extra]
        for extra in range(1, 5)
    }

    selected_zero_blocks = [
        {"n": 7, "m": 4, "guaranteed_terms": zero_block_size(7, 4)},
        {"n": 11, "m": 4, "guaranteed_terms": zero_block_size(11, 4)},
        {"n": 8, "m": 5, "guaranteed_terms": zero_block_size(8, 5)},
        {"n": 16, "m": 5, "guaranteed_terms": zero_block_size(16, 5)},
        {"n": 9, "m": 6, "guaranteed_terms": zero_block_size(9, 6)},
        {"n": 10, "m": 7, "guaranteed_terms": zero_block_size(10, 7)},
        {"n": 16, "m": 12, "guaranteed_terms": zero_block_size(16, 12)},
    ]

    core: dict[str, Any] = {
        "status": [
            "GENERAL_POST_SIMPLEX_SMALL_EXCESS_ZERO_BAND",
            "EXCESS_ZERO_THROUGH_M_PLUS_THREE_FOR_M_GE_4",
            "EXCESS_ZERO_THROUGH_M_PLUS_FOUR_FOR_M_GE_5",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "quartic_and_above": (
                "For m>=4, q>=2 and q*n<=m^2+m+3, every q-term Chow "
                "block has zero intersection with D_m(perm_n)."
            ),
            "quintic_and_above": (
                "For m>=5, q>=2 and q*n<=m^2+m+4, every q-term Chow "
                "block has zero intersection with D_m(perm_n)."
            ),
            "zero_block": (
                "zeta_post(n,4)=floor((4^2+4+3)/n); for m>=5, "
                "zeta_post(n,m)=floor((m^2+m+4)/n), whenever the count "
                "is at least two."
            ),
        },
        "private_branch": {
            "generic_route": "one private polar plus n<(m-1)^2",
            "two_plane_shadow_formula": "F^(d-1)_(n,d)(2)=d(d+1)",
            "exceptions": private_exceptions,
        },
        "no_private_branch": {
            "generic_route": "dim M<=(q-1)s<m^2",
            "pair_supported_lemma": (
                "If m^2>(q-2)n, a covector supported on two component "
                "spaces survives on the essential space; if 2n<(m-1)^2, "
                "its nonzero polar contradicts the lower-degree shadow floor."
            ),
            "exceptions": pair_exceptions,
        },
        "scan": {
            "maximum_m": maximum_m,
            "row_count": len(rows),
            "rows_by_extra": {key: len(value) for key, value in by_extra.items()},
            "private_shadow_exception_count": len(private_exceptions),
            "pair_supported_exception_count": len(pair_exceptions),
            "selected_rows": [
                row
                for row in rows
                if int(row["m"]) in {4, 5, 6, 7, 12}
            ],
        },
        "selected_zero_blocks": selected_zero_blocks,
        "next_frontier": {
            "quartic": "q*n=4^2+4+4=24",
            "m_ge_5": "q*n=m^2+m+5",
            "cubic": "(n,m,q)=(4,3,3),(6,3,2) remain open; (3,3,4) is nonzero",
        },
        "claim_boundary": (
            "This is an ordinary characteristic-zero zero-intersection "
            "theorem. It adds no exact Chow rank, optimized finite-n "
            "numerical lower bound, border-rank result or literature-novelty "
            "claim. The cubic excess-m rows are not changed."
        ),
    }
    payload = {**core, "core_sha256": canonical_hash(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload["core_sha256"])
    return payload


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
            "private_branch",
            "no_private_branch",
            "selected_zero_blocks",
            "next_frontier",
            "claim_boundary",
            "core_sha256",
        ):
            require(frozen[key] == payload[key], ("frozen mismatch", key))

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_EXCESS_M_PLUS_FOUR_BAND_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
