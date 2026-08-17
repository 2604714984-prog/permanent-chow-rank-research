#!/usr/bin/env python3
"""Finite interface replay for fixed m-primary two-direction ideals."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path
from typing import Any


FROZEN = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "general_two_direction_fixed_ideal_ceiling.json"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def quotient_hilbert(size: int, power: int) -> list[int]:
    require(1 <= power, power)
    result = []
    for degree in range(size + 1):
        source = comb(size, degree - power) if degree >= power else 0
        result.append(max(0, comb(size, degree) - source))
    return result


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def build_payload() -> dict[str, Any]:
    one_factor_checks = 0
    split_checks = 0
    samples: dict[str, Any] = {}

    for size in range(2, 51):
        central = comb(size, size // 2)
        for power in range(1, min(8, size) + 1):
            quotient = quotient_hilbert(size, power)
            total = sum(quotient)
            require(total <= power * central, (size, power, total, central))
            require(all(value >= 0 for value in quotient), (size, power))
            one_factor_checks += 1

    for n in range(4, 51):
        first = n // 2
        second = n - first
        first_central = comb(first, first // 2)
        second_central = comb(second, second // 2)
        for power in range(1, min(8, first, second) + 1):
            left = quotient_hilbert(first, power)
            right = quotient_hilbert(second, power)
            split = convolution(left, right)
            total = sum(split)
            bound = power * power * first_central * second_central
            require(total <= bound, (n, power, total, bound))
            require(max(split) <= total, (n, power))
            split_checks += 1

            if (n, power) in {(8, 2), (10, 3), (20, 4), (50, 8)}:
                samples[f"n{n}_N{power}"] = {
                    "total_split_quotient": total,
                    "certified_bound": bound,
                    "maximum_graded_piece": max(split),
                }

    require(one_factor_checks == 371, one_factor_checks)
    require(split_checks == 334, split_checks)

    return {
        "status": [
            "GENERAL_FIXED_M_PRIMARY_IDEAL_CEILING",
            "GENERAL_FIXED_COMPLETE_INTERSECTION_CEILING",
            "BOOLEAN_POWER_QUOTIENT_BOUND",
            "EXACT_FINITE_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "boolean_power_quotient": (
                "dim(B_m/L^N B_m)_j=[C(m,j)-C(m,j-N)]_+."
            ),
            "total_bound": (
                "dim(B_m/L^N B_m)<=N*C(m,floor(m/2))."
            ),
            "split_bound": (
                "dim B_n/(s^N,t^N)<=N^2*C(a,floor(a/2))*C(b,floor(b/2))."
            ),
            "fixed_ideal_ceiling": (
                "For every fixed homogeneous m-primary I in k[s,t], "
                "R_n^I<=(1+O_I(n^(-1/2)))*C(n,floor(n/2))."
            ),
            "glynn_gap": (
                "Every fixed m-primary ideal profile remains "
                "Omega_I(sqrt(n)) below Glynn."
            ),
        },
        "finite_replay": {
            "one_factor_total_bound_checks": one_factor_checks,
            "split_tensor_bound_checks": split_checks,
            "samples": samples,
        },
        "claim_boundary": (
            "This is a route ceiling for fixed homogeneous m-primary binary "
            "ideals. It is not an upper bound on Chow rank and does not cover "
            "ideal families whose complexity grows with n, relation-sensitive "
            "invariants, representation-valued modules, Chow-realizability "
            "defects, border rank or exact rank for n>=6. Literature novelty "
            "is not established."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_TWO_DIRECTION_FIXED_IDEAL_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
