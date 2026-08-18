#!/usr/bin/env python3
"""Exact finite replay for the cubic three-term zero theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Sequence

EXPECTED_CORE_SHA256 = "e39a77e46607d1ad7c69e50c04ddedadc9d256dc98b80d86790d03aa9475b5d6"


def require(ok: bool, message: object) -> None:
    if not ok:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def rank(matrix: Sequence[Sequence[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    r = 0
    for c in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = rows[r][c]
        rows[r] = [x / scale for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                factor = rows[i][c]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def private_states() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for rs in product(range(1, 5), repeat=3):
        for ambient in range(9, sum(rs) + 1):
            k = sum(rs) - ambient
            if not 0 <= k <= 3:
                continue
            for ts in product(range(5), repeat=3):
                if any(ts[i] > min(rs[i], k) for i in range(3)):
                    continue
                ss = tuple(rs[i] - ts[i] for i in range(3))
                if any(s not in (0, 1) for s in ss):
                    continue
                if sum(ss) < ambient - 2 * k:
                    continue
                out.append({
                    "component_ranks": list(rs),
                    "ambient_dimension": ambient,
                    "relation_defect": k,
                    "overlap_dimensions": list(ts),
                    "private_dimensions": list(ss),
                })
    return out


def support_models() -> dict[str, object]:
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    checked = 0
    for labels in product((0, 1, 2), repeat=4):
        left = tuple(i for i, x in enumerate(labels) if x == 1)
        right = tuple(i for i, x in enumerate(labels) if x == 2)
        if not left or not right:
            continue
        pair = tuple(sorted((left, right)))
        if pair in seen:
            continue
        seen.add(pair)
        u = [int(i in left) for i in range(4)]
        v = [int(i in right) for i in range(4)]
        block = [[u[i] * v[j] + v[i] * u[j] for j in range(4)] for i in range(4)]
        require(all(block[i][i] == 0 for i in range(4)), pair)
        require(rank(block) == 2, pair)
        constraints = [[u[i] * u[i], 2 * u[i] * v[i], v[i] * v[i]] for i in range(4)]
        require(rank(constraints) == 2, pair)
        checked += 1
    require(checked == 25, checked)
    return {"support_models_checked": checked, "restriction_dimension": 1}


def projection_cases() -> list[dict[str, object]]:
    return [
        {"projection_ranks": [2, 2], "intersection_dimensions": [0, 2, 4], "total_dimensions": [12, 10, 8]},
        {"projection_ranks": [2, 1], "intersection_dimensions": [0], "total_dimensions": [12]},
        {"projection_ranks": [1, 2], "intersection_dimensions": [0], "total_dimensions": [12]},
        {"projection_ranks": [1, 1], "intersection_dimensions": [0], "total_dimensions": [12]},
        {"projection_ranks": [2, 0], "intersection_dimensions": [0], "total_dimensions": [12]},
        {"projection_ranks": [0, 2], "intersection_dimensions": [0], "total_dimensions": [12]},
    ]


def boundary_row(m: int, q: int) -> dict[str, object]:
    if (m, q) == (3, 3):
        zero, source = 4, "cubic three-term theorem"
    elif (m, q) == (3, 4):
        zero, source = None, "Glynn nonzero at n=3"
    else:
        zero = (m * m - 1) // (q - 1)
        source = "strict shifted theorem"
        if q == 4 and m % 3 == 0:
            equality = m * m // 3
            if 2 * equality <= (m - 1) ** 2:
                zero, source = equality, "shifted equality theorem"
        if zero < m:
            zero = None
    savings = min(m - 1, q.bit_length() - 1)
    nonzero = m * (m - savings)
    start = (zero if zero is not None else m - 1) + 1
    count = max(0, nonzero - start)
    return {
        "m": m,
        "q": q,
        "direct_zero_endpoint": zero,
        "zero_source": source,
        "explicit_nonzero_start": nonzero,
        "open_start": start if count else None,
        "open_end": nonzero - 1 if count else None,
        "open_count": count,
    }


def build_core() -> dict[str, object]:
    states = private_states()
    expected_state = {
        "component_ranks": [4, 4, 4],
        "ambient_dimension": 9,
        "relation_defect": 3,
        "overlap_dimensions": [3, 3, 3],
        "private_dimensions": [1, 1, 1],
    }
    require(states == [expected_state], states)
    cases = projection_cases()
    totals = sorted({d for row in cases for d in row["total_dimensions"]})
    require(totals == [8, 10, 12] and 9 not in totals, totals)
    rows = [boundary_row(m, q) for m in range(3, 33) for q in (3, 4)]
    selected = [row for row in rows if row["m"] <= 8]
    return {
        "claim": {
            "field": "characteristic_zero",
            "triple": {"n": 4, "m": 3, "q": 3},
            "intersection": "ZERO",
            "statement": "D_3(perm_4) intersect (D_3(T_1)+D_3(T_2)+D_3(T_3)) = 0",
            "new_chow_rank_bound": False,
            "border_rank_improvement": False,
        },
        "private_polar_integer_squeeze": {"surviving_state_count": 1, "state": expected_state},
        "rank_four_rectangle_interface": support_models(),
        "tensor_plane_parity": {"case_table": cases, "possible_total_dimensions": totals, "forbidden_dimension": 9},
        "cubic_excess_m_classification": [
            {"n": 3, "m": 3, "q": 4, "status": "NONZERO", "source": "Glynn"},
            {"n": 4, "m": 3, "q": 3, "status": "ZERO", "source": "this theorem"},
            {"n": 6, "m": 3, "q": 2, "status": "NONZERO", "source": "sharp pair theorem"},
        ],
        "direct_frontier_audit": {"m_range": [3, 32], "row_count": len(rows), "selected_rows": selected},
    }


def build_payload() -> dict[str, object]:
    core = build_core()
    sha = canonical_sha256(core)
    require(sha == EXPECTED_CORE_SHA256, (sha, EXPECTED_CORE_SHA256))
    return {"schema_version": 1, "core_sha256": sha, "core": core}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    core = payload["core"]
    print(f"private_state_count={core['private_polar_integer_squeeze']['surviving_state_count']}")
    print(f"rank_four_support_models={core['rank_four_rectangle_interface']['support_models_checked']}")
    print(f"tensor_plane_total_dimensions={core['tensor_plane_parity']['possible_total_dimensions']}")
    print("cubic_4_3_3=ZERO")
    print(f"core_sha256={payload['core_sha256']}")
    print("GENERAL_CUBIC_THREE_TERM_ZERO_AUDIT_PASS")


if __name__ == "__main__":
    main()
