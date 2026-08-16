#!/usr/bin/env python3
"""Audit the central-window localization of the scalar derivative tower."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FULL_TOWER_DATA = ROOT / "data" / "general_full_degree_tower_envelope.json"
EXPECTED_CORE_SHA256 = (
    "334116f082662e53f35d7f634ab75cd3106f9e96b8303901c5e9c6d7823c4749"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def n_dependent_constant(n: int, k: int) -> tuple[int, list[int]]:
    require(2 <= k <= n // 2, (n, k))
    values = [
        (
            max(0, comb(a, k - 1) - comb(a - 1, k) - 1),
            a,
        )
        for a in range(k, n + 1)
    ]
    optimum = max(value for value, _ in values)
    return optimum, [a for value, a in values if value == optimum]


def build_payload() -> dict[str, Any]:
    tower = json.loads(FULL_TOWER_DATA.read_text(encoding="utf-8"))
    thresholds = {
        int(key): value["by_degree"]
        for key, value in tower["thresholds"].items()
    }

    transition_checks = 0
    binomial_constant_checks = 0
    tail_bound_checks = 0
    table: dict[str, Any] = {}

    for n in range(3, 11):
        row = thresholds[n]
        transitions: dict[str, Any] = {}
        tails: dict[str, Any] = {}

        for k in range(2, n // 2 + 1):
            constant, maximizers = n_dependent_constant(n, k)
            previous_index = n - k - 1
            next_index = n - k
            gap = row[next_index] - row[previous_index]
            require(0 <= gap <= constant, (n, k, gap, constant))
            transition_checks += 1

            require(constant <= comb(n, k - 1), (n, k, constant))
            binomial_constant_checks += 1

            transitions[str(k)] = {
                "c_nk": constant,
                "maximizing_a": maximizers,
                "observed_gap": gap,
            }

        for cutoff in range(2, n // 2 + 1):
            start_degree_index = n - cutoff - 1
            actual_tail = row[-1] - row[start_degree_index]
            binomial_bound = sum(comb(n, j) for j in range(1, cutoff))
            require(actual_tail <= binomial_bound, (n, cutoff, actual_tail))
            tail_bound_checks += 1
            tails[str(cutoff)] = {
                "actual_top_tail": actual_tail,
                "binomial_bound": binomial_bound,
            }

        table[str(n)] = {
            "transition_constants": transitions,
            "tail_bounds": tails,
        }

    require(transition_checks == 16, transition_checks)
    require(binomial_constant_checks == 16, binomial_constant_checks)
    require(tail_bound_checks == 16, tail_bound_checks)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_N_DEPENDENT_TAIL_CONSTANT",
            "GENERAL_BINOMIAL_TAIL_LOCALIZATION",
            "GENERAL_MODERATE_DEVIATION_WINDOW",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "n_dependent_constant": (
                "c_(n,k)=max_(k<=a<=n)"
                "[binom(a,k-1)-binom(a-1,k)-1]_+."
            ),
            "increment": (
                "For 2<=k<=n/2, "
                "0<=Q_(n,n-k+1)-Q_(n,n-k)<=c_(n,k)."
            ),
            "binomial_tail": (
                "For 2<=K<=n/2, "
                "0<=Theta_n-Q_(n,n-K)<=sum_(j=1)^(K-1) binom(n,j)."
            ),
            "linear_localization": (
                "For fixed 0<alpha<1/2 and K=floor(alpha*n), "
                "the top-tail difference is exp(n*H(alpha)+o(n)) and "
                "is exponentially smaller than the central binomial."
            ),
            "moderate_deviation": (
                "If 2*w_n^2/n-log(n+1)->+infinity and "
                "K_n-1<=n/2-w_n, then "
                "Theta_n-Q_(n,n-K_n)=o(binom(n,floor(n/2)))."
            ),
            "polynomial_window": (
                "Hoeffding gives difference<=2^n*exp(-2*w^2/n); "
                "precision at any fixed inverse-polynomial multiple of the "
                "central binomial requires only an O(sqrt(n log n)) window "
                "above the center."
            ),
        },
        "finite_replay": {
            "n_min": 3,
            "n_max": 10,
            "transition_checks": transition_checks,
            "binomial_constant_checks": binomial_constant_checks,
            "tail_bound_checks": tail_bound_checks,
            "table": table,
        },
        "claim_boundary": (
            "The theorem is a general-n localization of the exact scalar "
            "derivative tower. It introduces no new numerical Chow-rank "
            "lower bound and does not determine the central-window "
            "recurrence, prove a central-binomial ceiling, establish a "
            "Chow-realizability defect, improve border rank, determine an "
            "exact rank for n>=6, or prove general Glynn optimality. The "
            "Hoeffding corollary localizes polynomial-scale analysis but "
            "does not solve it. Literature novelty is not established."
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
    print("GENERAL_TOWER_CENTRAL_WINDOW_LOCALIZATION_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
