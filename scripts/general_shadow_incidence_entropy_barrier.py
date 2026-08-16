#!/usr/bin/env python3
"""Audit the incidence sandwich and entropy-scale barrier for product shadows."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

from general_shadow_complement_deficit_duality import ExactInverseShadow, require


ROOT = Path(__file__).resolve().parents[1]
FULL_TOWER_DATA = ROOT / "data" / "general_full_degree_tower_envelope.json"
EXPECTED_CORE_SHA256 = (
    "3abb3cc354c8de4511bddb75d7e3477fb5de5a7871c02adcaa038230e2754741"
)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build_payload() -> dict[str, Any]:
    shadow_checks = 0
    inverse_checks = 0

    for n in range(3, 9):
        for degree in range(2, n):
            table = ExactInverseShadow(n, degree)
            lower_degree_ambient = comb(n, degree - 1) ** 2
            upper_degree_ambient = comb(n, degree) ** 2
            lower_degree_ratio = (n - degree + 1) ** 2
            upper_degree_ratio = degree**2

            for family_size, shadow in enumerate(table.minimum):
                require(
                    shadow * lower_degree_ratio
                    >= family_size * upper_degree_ratio,
                    (n, degree, family_size, shadow),
                )
                require(
                    shadow
                    <= min(
                        lower_degree_ambient,
                        family_size * upper_degree_ratio,
                    ),
                    (n, degree, family_size, shadow),
                )
                shadow_checks += 1

            for capacity, family_size in enumerate(table.gamma):
                lower = min(
                    upper_degree_ambient,
                    capacity // upper_degree_ratio,
                )
                upper = min(
                    upper_degree_ambient,
                    capacity * lower_degree_ratio // upper_degree_ratio,
                )
                require(
                    lower <= family_size <= upper,
                    (n, degree, capacity, family_size, lower, upper),
                )
                inverse_checks += 1

    require(shadow_checks == 17_378, shadow_checks)
    require(inverse_checks == 17_378, inverse_checks)

    tower = json.loads(FULL_TOWER_DATA.read_text(encoding="utf-8"))
    diagnostics = {}
    for key, row in tower["thresholds"].items():
        n = int(key)
        theta = row["theta"]
        central = comb(n, n // 2)
        diagnostics[key] = {
            "central_binomial": central,
            "theta": theta,
            "theta_over_central_numerator": theta,
            "theta_over_central_denominator": central,
            "glynn_upper": 2 ** (n - 1),
        }

    core: dict[str, Any] = {
        "status": [
            "GENERAL_PRODUCT_SHADOW_INCIDENCE_SANDWICH",
            "GENERAL_ENTROPY_SCALE_BARRIER",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "shadow_sandwich": (
                "b*d^2/(n-d+1)^2 <= F_(n,d)(b) "
                "<= min(A_(n,d-1),b*d^2)."
            ),
            "inverse_sandwich": (
                "floor(C/d^2) <= Gamma_(n,d)(C) "
                "<= floor(C*(n-d+1)^2/d^2), with ambient caps."
            ),
            "linear_degree_rate": (
                "For d=alpha*n+O(1) and b=exp(zeta*n+o(n)), "
                "F_(n,d)(b)=exp(zeta*n+o(n))."
            ),
            "tower_rate": "log Theta_n/n -> log 2.",
            "barrier": (
                "Exponential-rate entropy alone cannot distinguish "
                "central-binomial scale from Glynn scale; second-order "
                "polynomial information is required."
            ),
        },
        "exact_replay": {
            "n_min": 3,
            "n_max": 8,
            "shadow_sandwich_checks": shadow_checks,
            "inverse_sandwich_checks": inverse_checks,
        },
        "normalization_diagnostics": diagnostics,
        "claim_boundary": (
            "The incidence sandwich is an exact general-n theorem and the "
            "entropy-rate conclusion is a route barrier, not a new lower "
            "bound. It does not determine the polynomial normalization of "
            "Theta_n, prove Theta_n=O(binom(n,floor(n/2))), establish a "
            "Chow-realizability correction, improve border rank, determine "
            "an exact rank for n>=6, or prove general Glynn optimality. "
            "Literature novelty is not established."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


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
    print("GENERAL_SHADOW_INCIDENCE_ENTROPY_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
