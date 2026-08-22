#!/usr/bin/env python3
"""Deterministic Plucker replay for the gauge-free q5=2 dichotomy."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


N = 7
PAIRS = tuple(combinations(range(N), 2))
QUADRUPLES = tuple(combinations(range(N), 4))


def basis_bivector(first: int, second: int) -> tuple[int, ...]:
    if not 0 <= first < second < N:
        raise ValueError("bivector indices must be increasing")
    return tuple(1 if pair == (first, second) else 0 for pair in PAIRS)


def multiply_linear(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int, int]:
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[1] * right[1],
    )


def restricted_plucker_quadrics(
    beta0: tuple[int, ...], beta1: tuple[int, ...]
) -> dict[tuple[int, int, int, int], tuple[int, int, int]]:
    if len(beta0) != len(PAIRS) or len(beta1) != len(PAIRS):
        raise ValueError("bivectors must have twenty-one coordinates")
    coordinate = {
        pair: (beta0[index], beta1[index]) for index, pair in enumerate(PAIRS)
    }
    answer = {}
    for i, j, k, ell in QUADRUPLES:
        first = multiply_linear(coordinate[i, j], coordinate[k, ell])
        second = multiply_linear(coordinate[i, k], coordinate[j, ell])
        third = multiply_linear(coordinate[i, ell], coordinate[j, k])
        answer[i, j, k, ell] = tuple(
            first[index] - second[index] + third[index] for index in range(3)
        )
    return answer


def line_is_contained(beta0: tuple[int, ...], beta1: tuple[int, ...]) -> bool:
    return not any(
        any(coefficients)
        for coefficients in restricted_plucker_quadrics(beta0, beta1).values()
    )


def build_payload() -> dict[str, object]:
    flag = (basis_bivector(0, 1), basis_bivector(0, 2))
    transverse = (basis_bivector(0, 1), basis_bivector(2, 3))
    flag_quadrics = restricted_plucker_quadrics(*flag)
    transverse_quadrics = restricted_plucker_quadrics(*transverse)
    nonzero_transverse = {
        "".join(str(index) for index in key): list(value)
        for key, value in transverse_quadrics.items()
        if any(value)
    }
    if nonzero_transverse != {"0123": [0, 1, 0]}:
        raise AssertionError(nonzero_transverse)
    return {
        "schema_version": 1,
        "status": "TI-08A-Q5-TWO-PENCIL-DICHOTOMY",
        "ambient_dimension": N,
        "bivector_coordinate_count": len(PAIRS),
        "plucker_quadric_count": len(QUADRUPLES),
        "flag_line": {
            "basis_pairs": [[0, 1], [0, 2]],
            "contained_in_grassmannian": line_is_contained(*flag),
            "nonzero_restricted_quadrics": sum(
                any(value) for value in flag_quadrics.values()
            ),
        },
        "transverse_line": {
            "basis_pairs": [[0, 1], [2, 3]],
            "contained_in_grassmannian": line_is_contained(*transverse),
            "nonzero_restricted_quadrics": nonzero_transverse,
            "intersection_equation": "s*t=0",
            "distinct_projective_intersection_points": 2,
        },
        "exhaustive_branches": [
            "BIVECTOR-SPAN-RANK-AT-MOST-ONE",
            "NON-GRASSMANNIAN-LINE-AT-MOST-TWO-NONZERO-RATIOS",
            "GRASSMANNIAN-FLAG-LINE",
        ],
        "claim_boundary": [
            "The three branches are exhaustive for the gauge-free q5=2 relation pencil F3,H6=42.",
            "Zero relation columns are retained as a separate support stratum.",
            "The dichotomy does not close F3, weighted coupling, Packet B, lower 50, or border rank.",
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
            print("Q5_TWO_PENCIL_FROZEN_REPLAY_FAIL")
            return 1
        print("Q5_TWO_PENCIL_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
