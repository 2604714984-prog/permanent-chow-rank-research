#!/usr/bin/env python3
"""Exact scalar-frontier scan for an ordinary perm_8 lower bound of 78.

The script imports the exact product-shadow implementation, scans every
standard first-Koszul output degree 2..6 and every fixed count authorized by
the global first-Koszul lower bound, then selects the smallest residual rank
deficit under a hypothetical 77-term decomposition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path

import general_exact_product_shadow as exact_shadow


N = 8
TOTAL_TERMS = 77


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def conjugate(partition: tuple[int, ...]) -> tuple[int, ...]:
    width = len(partition)
    return tuple(
        sum(value >= column for value in partition)
        for column in range(1, width + 1)
    )


def run_length(partition: tuple[int, ...]) -> list[list[int]]:
    require(partition, "empty partition")
    output: list[list[int]] = []
    value = partition[0]
    count = 0
    for current in partition:
        if current == value:
            count += 1
        else:
            output.append([value, count])
            value = current
            count = 1
    output.append([value, count])
    return output


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def scan_all() -> tuple[list[dict[str, int]], dict[str, object]]:
    global_bound = exact_shadow.global_first_koszul_bound(N)
    require(global_bound == 71, global_bound)

    rows: list[dict[str, int]] = []
    per_output: dict[str, object] = {}

    for output_degree in range(2, N - 1):
        complement_degree = N - output_degree
        shadow = exact_shadow.ExactProductShadow(N, complement_degree)
        target_rank, one_term_cap, selected_bound = (
            exact_shadow.first_koszul_data(N, output_degree)
        )
        full_shadow = comb(N, complement_degree - 1) ** 2
        local_rows: list[dict[str, int]] = []

        for fixed_count in range(1, global_bound + 1):
            threshold = fixed_count * comb(N, complement_degree - 1)
            if threshold >= full_shadow:
                continue
            _, cap, first_bad = exact_shadow.exact_intersection_cap(
                shadow,
                fixed_count,
            )
            numerator = target_rank - N * N * cap.family_size
            if numerator <= 0:
                continue
            residual_count = ceil_div(numerator, one_term_cap)
            bound = fixed_count + residual_count
            residual_capacity_for_77 = (
                TOTAL_TERMS - fixed_count
            ) * one_term_cap
            deficit = residual_capacity_for_77 - numerator
            row = {
                "output_degree": output_degree,
                "complement_degree": complement_degree,
                "fixed_count": fixed_count,
                "threshold": threshold,
                "intersection_cap": cap.family_size,
                "shadow_at_cap": cap.shadow_size,
                "first_excluded_size": first_bad.family_size,
                "shadow_at_first_excluded_size": first_bad.shadow_size,
                "target_rank": target_rank,
                "one_term_cap": one_term_cap,
                "selected_output_first_koszul_bound": selected_bound,
                "residual_rank_lower_bound": numerator,
                "residual_term_count": residual_count,
                "exact_shadow_lower_bound": bound,
                "residual_capacity_for_77": residual_capacity_for_77,
                "deficit_to_77_term_contradiction": deficit,
            }
            rows.append(row)
            local_rows.append(row)

        require(local_rows, output_degree)
        maximum = max(row["exact_shadow_lower_bound"] for row in local_rows)
        maximizing_counts = [
            row["fixed_count"]
            for row in local_rows
            if row["exact_shadow_lower_bound"] == maximum
        ]
        per_output[str(output_degree)] = {
            "complement_degree": complement_degree,
            "evaluated_nonvacuous_count": len(local_rows),
            "maximum_exact_shadow_lower_bound": maximum,
            "maximizing_fixed_counts": maximizing_counts,
        }

    return rows, {
        "global_first_koszul_bound": global_bound,
        "evaluated_nonvacuous_rows": len(rows),
        "per_output_degree": per_output,
    }


def selected_minimizers(shadow: exact_shadow.ExactProductShadow) -> dict[str, object]:
    cap = shadow.minimum(725)
    first_bad = shadow.minimum(726)
    require((cap.shadow_size, cap.partition_count) == (950, 4), cap)
    require((first_bad.shadow_size, first_bad.partition_count) == (956, 4), first_bad)

    cap_a = (15,) * 45 + (5,) * 10 + (0,) * 15
    cap_b = (35,) * 5 + (25,) * 10 + (15,) * 20 + (0,) * 35
    cap_profiles = {
        cap_a,
        conjugate(cap_a),
        cap_b,
        conjugate(cap_b),
    }
    require(len(cap_profiles) == 4, cap_profiles)
    for profile in cap_profiles:
        require(sum(profile) == 725, profile)
        require(shadow.objective(profile) == 950, profile)

    bad_a = (15,) * 45 + (6,) + (5,) * 9 + (0,) * 15
    bad_b = (
        (35,) * 5
        + (26,)
        + (25,) * 9
        + (15,) * 20
        + (0,) * 35
    )
    bad_profiles = {
        bad_a,
        conjugate(bad_a),
        bad_b,
        conjugate(bad_b),
    }
    require(len(bad_profiles) == 4, bad_profiles)
    for profile in bad_profiles:
        require(sum(profile) == 726, profile)
        require(shadow.objective(profile) == 956, profile)

    return {
        "cap_size": 725,
        "cap_shadow": 950,
        "cap_minimizer_count": 4,
        "cap_minimizer_profiles": sorted(
            (run_length(profile) for profile in cap_profiles),
            reverse=True,
        ),
        "first_excluded_size": 726,
        "first_excluded_shadow": 956,
        "first_excluded_minimizer_count": 4,
        "first_excluded_minimizer_profiles": sorted(
            (run_length(profile) for profile in bad_profiles),
            reverse=True,
        ),
    }


def build_payload() -> dict[str, object]:
    rows, scan_summary = scan_all()
    maximum = max(row["exact_shadow_lower_bound"] for row in rows)
    require(maximum == 77, maximum)

    active_rows = [
        row for row in rows if row["exact_shadow_lower_bound"] == maximum
    ]
    require(
        [(row["output_degree"], row["fixed_count"]) for row in active_rows]
        == [(4, value) for value in range(14, 20)],
        active_rows,
    )

    selected = min(
        active_rows,
        key=lambda row: row["deficit_to_77_term_contradiction"],
    )
    require(
        (
            selected["output_degree"],
            selected["fixed_count"],
            selected["intersection_cap"],
            selected["deficit_to_77_term_contradiction"],
        )
        == (4, 17, 725, 1376),
        selected,
    )

    central_shadow = exact_shadow.ExactProductShadow(8, 4)
    minimizers = selected_minimizers(central_shadow)

    active_table = [
        {
            "fixed_count": row["fixed_count"],
            "threshold": row["threshold"],
            "intersection_cap": row["intersection_cap"],
            "shadow_at_cap": row["shadow_at_cap"],
            "first_excluded_size": row["first_excluded_size"],
            "shadow_at_first_excluded_size": row[
                "shadow_at_first_excluded_size"
            ],
            "residual_rank_lower_bound": row["residual_rank_lower_bound"],
            "residual_term_count": row["residual_term_count"],
            "deficit_to_77_term_contradiction": row[
                "deficit_to_77_term_contradiction"
            ],
        }
        for row in active_rows
    ]

    core = {
        "status": [
            "EXACT_PRODUCT_SHADOW_ROUTE_FRONTIER",
            "NO_LOWER_78_CLAIM",
            "SELECTED_Q17_B725_GAIN1377",
        ],
        "scan_summary": scan_summary,
        "scan_rows_sha256": canonical_hash(rows),
        "maximum_exact_shadow_lower_bound": maximum,
        "active_central_rows": active_table,
        "selected_frontier": {
            **selected,
            "required_additional_integer_gain": 1377,
            "sufficient_realizable_intersection_cap": 703,
        },
        "selected_ferrers_minimizers": minimizers,
        "decision": {
            "primary_route": "m=4, q=17, b<=725, additional gain >=1377",
            "q14_flag_orbit": "retain as structural laboratory",
            "other_scalar_choices": "dominated for lower 78",
        },
        "claim_boundary": (
            "The complete exact scalar scan stops at 77. It selects the "
            "smallest additional-rank frontier but does not prove lower 78, "
            "classify noncoordinate equality loci, establish Chow "
            "realizability, or make a border-rank claim."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_PRODUCT_SHADOW_N8_LOWER78_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
