#!/usr/bin/env python3
"""Frozen dimension and replacement replay for q5=2,q6=1."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


POINT_COUNT = 42
AMBIENT_DIMENSION = 7
Q5 = 2
Q6 = 1
WEDGE_DIMENSION = AMBIENT_DIMENSION * (AMBIENT_DIMENSION - 1) // 2
TARGET_DIMENSION = Q5 * WEDGE_DIMENSION
GAUGE_RANK = AMBIENT_DIMENSION
CANONICAL_COKERNEL_DIMENSION = TARGET_DIMENSION - GAUGE_RANK
PERMANENT_WARING_RANK = 64


def minimum_veronese_relation_support(degree: int) -> int:
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    return degree + 2


def sparse_two_block_cost(
    first_size: int,
    second_size: int,
    first_binary: bool,
    second_binary: bool,
) -> int:
    if first_size < 7 or second_size < 7:
        raise ValueError("nonzero fifth-relation blocks have size at least 7")
    if first_size + second_size > POINT_COUNT:
        raise ValueError("disjoint supports exceed the point count")
    first_cost = 7 if first_binary else first_size
    second_cost = 7 if second_binary else second_size
    return first_cost + second_cost + POINT_COUNT - first_size - second_size


def build_payload() -> dict[str, object]:
    # There are sum(1..29)*4 = 1740 bounded arithmetic cases.  Only their
    # small integer costs are retained.
    expected_sparse_case_count = (29 * 30 // 2) * 4
    sparse_costs = []
    sparse_case_count = 0
    for first_size in range(7, POINT_COUNT + 1):
        for second_size in range(7, POINT_COUNT - first_size + 1):
            for first_binary in (False, True):
                for second_binary in (False, True):
                    sparse_case_count += 1
                    sparse_costs.append(
                        sparse_two_block_cost(
                            first_size,
                            second_size,
                            first_binary,
                            second_binary,
                        )
                    )
    if sparse_case_count != expected_sparse_case_count:
        raise AssertionError(sparse_case_count)
    branch_bounds = {
        "bivector_span_at_most_one": 42,
        "non_grassmannian_sparse_ratio": max(sparse_costs),
        "grassmannian_flag_without_p_point": 43,
        "grassmannian_flag_with_p_point": 48,
    }
    if max(branch_bounds.values()) >= PERMANENT_WARING_RANK:
        raise AssertionError(branch_bounds)
    return {
        "schema_version": 1,
        "status": "Q5-TWO-Q6-ONE-GAUGE-CLOSED",
        "point_count": POINT_COUNT,
        "q5_q6": [Q5, Q6],
        "wedge_dimension": WEDGE_DIMENSION,
        "gauge": {
            "source_dimension": AMBIENT_DIMENSION,
            "target_dimension": TARGET_DIMENSION,
            "kernel_dimension": 0,
            "rank": GAUGE_RANK,
            "cokernel_dimension": CANONICAL_COKERNEL_DIMENSION,
            "minimum_tau_support": minimum_veronese_relation_support(6),
        },
        "bounded_sparse_cases_checked": sparse_case_count,
        "branch_replacement_bounds": branch_bounds,
        "permanent_waring_rank": PERMANENT_WARING_RANK,
        "closed_signatures": [
            "F1-(33,39,40,41)",
            "F3-(34,38,40,41)",
        ],
        "claim_boundary": [
            "The bivector pencil is gauge-dependent; only its exhaustive branch union is used.",
            "All q5=2 common-graph signatures F1/F3 are closed.",
            "No conclusion is made here for q5=3, q5=4, arbitrary Packet B, lower 50, or border rank.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("Q5_TWO_Q6_ONE_GAUGE_FROZEN_REPLAY_FAIL")
            return 1
        print("Q5_TWO_Q6_ONE_GAUGE_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
