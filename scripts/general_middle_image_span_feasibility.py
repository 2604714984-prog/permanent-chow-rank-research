#!/usr/bin/env python3
"""Exact feasibility table for extending the perm_6 middle-layer proof.

The table compares the local symbol slope required to reach Glynn's
2^(n-1) target with the one-direction capacity of a single Chow term.
It is a route ceiling, not a Chow-rank lower bound.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "general_middle_image_span_feasibility.json"


def encode(value: Fraction) -> str:
    return str(value)


def row(n: int) -> dict[str, object]:
    m = n // 2
    q = comb(n, m)
    target = 2 ** (n - 1)
    if n % 2 == 0:
        # h <= (N*q-q^2-Delta)/2 and h >= c*n^2-Delta/2.
        required = Fraction(q * (target - q), 2 * n * n)
        direction_capacity = comb(n - 1, m - 1)
        # At the full quotient d=n, the symbol rank is at most q.
        slope_capacity = Fraction(q, n)
        mode = "symmetric_one_sided"
        upper = "h <= (N*q - q^2 - Delta)/2"
        lower = "h >= c*n^2 - Delta/2"
    else:
        # h_out+h_in <= N*q-q^2-Delta and the desired two-sided lower
        # bound is c*n^2-Delta.
        required = Fraction(q * (target - q), n * n)
        direction_capacity = comb(n - 1, m - 1) + comb(n - 1, m)
        # At the full quotient d=n, the two symbol ranks total at most 2q.
        slope_capacity = Fraction(2 * q, n)
        mode = "rectangular_two_sided"
        upper = "h_out+h_in <= N*q - q^2 - Delta"
        lower = "h_out+h_in >= c*n^2 - Delta"
    return {
        "n": n,
        "middle_subset_rank_q": q,
        "glynn_target": target,
        "mode": mode,
        "required_local_slope": encode(required),
        "one_direction_capacity": direction_capacity,
        "full_quotient_average_slope_capacity": encode(slope_capacity),
        "slope_feasible": required <= slope_capacity,
        "global_upper_template": upper,
        "target_lower_template": lower,
    }


def build_payload() -> dict[str, object]:
    rows = [row(n) for n in range(3, 17)]
    feasible_odd = [entry["n"] for entry in rows if entry["n"] % 2 and entry["slope_feasible"]]
    feasible_even = [entry["n"] for entry in rows if not entry["n"] % 2 and entry["slope_feasible"]]
    assert row(6)["required_local_slope"] == "10/3"
    assert row(7)["required_local_slope"] == "145/7"
    assert row(8)["required_local_slope"] == "1015/32"
    assert row(7)["one_direction_capacity"] == 35
    assert row(7)["full_quotient_average_slope_capacity"] == "10"
    assert row(8)["one_direction_capacity"] == 35
    assert row(8)["full_quotient_average_slope_capacity"] == "35/4"
    assert row(7)["slope_feasible"] is False
    assert row(8)["slope_feasible"] is False
    assert row(9)["slope_feasible"] is False
    assert row(10)["slope_feasible"] is False
    return {
        "status": "PURE_ROUTE_FEASIBILITY_CEILING",
        "claim_boundary": (
            "This compares a required local slope with an elementary capacity; "
            "it does not prove any new Chow-rank lower bound."
        ),
        "rows": rows,
        "feasible_odd_n_in_range": feasible_odd,
        "feasible_even_n_in_range": feasible_even,
        "last_feasible_odd_n": max(feasible_odd),
        "last_feasible_even_n": max(feasible_even),
        "next_target": "perm_7 multi-degree coupled derivative module",
        "general_n_consequence": (
            "A proof for all n requires more than one middle derivative layer."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS: general middle-layer feasibility payload matches")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
