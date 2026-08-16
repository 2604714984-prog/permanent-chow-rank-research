#!/usr/bin/env python3
"""Audit fixed-codimension tails of the permanent derivative tower.

This module proves and replays four general structural statements.

1. Saturation thresholds are nondecreasing in derivative degree, so the
   complete scalar tower bound is always the degree-(n-1) threshold.
2. Every tower row is one-term Lipschitz.
3. The last fixed-codimension transitions have universal additive constants.
4. The final transition is governed exactly by bipartite C4 supersaturation.

The proof document contains the mathematical arguments.  This script rebuilds
all exact shadow and tower interfaces for n<=8, checks the published n<=10
threshold table, and exhausts all 3-by-3 and 4-by-4 bipartite graphs for the C4
interpretation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb, sqrt
from pathlib import Path
from typing import Any

from general_shadow_complement_deficit_duality import (
    ExactInverseShadow,
    direct_tower_rows,
    require,
)


ROOT = Path(__file__).resolve().parents[1]
FULL_TOWER_DATA = ROOT / "data" / "general_full_degree_tower_envelope.json"
EXPECTED_CORE_SHA256 = (
    "562ef480c5c3b9c95112ea5c3a3dab9ef36be019489251611e5f4855a6df0bf7"
)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def tail_constant(k: int) -> tuple[int, list[int]]:
    """Return c_k and every maximizing a.

    For a>=3k the binomial difference is nonpositive, so the finite range
    k<=a<3k is exact.
    """

    require(k >= 2, k)
    rows = [
        (
            a,
            max(0, comb(a, k - 1) - comb(a - 1, k) - 1),
        )
        for a in range(k, 3 * k)
    ]
    value = max(row[1] for row in rows)
    return value, [a for a, candidate in rows if candidate == value]


def c4_minimum_edge_profile(n: int) -> list[int]:
    """Minimum edges in an n-by-n bipartite graph with at least z C4s."""

    require(2 <= n <= 4, n)
    maximum_cycles = comb(n, 2) ** 2
    exact = [10**9] * (maximum_cycles + 1)
    row_mask = (1 << n) - 1

    for graph in range(1 << (n * n)):
        neighborhoods = [
            (graph >> (row * n)) & row_mask
            for row in range(n)
        ]
        cycles = 0
        for left in range(n):
            for right in range(left + 1, n):
                common = (neighborhoods[left] & neighborhoods[right]).bit_count()
                cycles += comb(common, 2)
        exact[cycles] = min(exact[cycles], graph.bit_count())

    profile = [0] * (maximum_cycles + 1)
    running = 10**9
    for cycles in range(maximum_cycles, -1, -1):
        running = min(running, exact[cycles])
        profile[cycles] = running
    require(profile[0] == 0, profile)
    return profile


def load_thresholds() -> dict[str, list[int]]:
    payload = json.loads(FULL_TOWER_DATA.read_text(encoding="utf-8"))
    return {
        key: value["by_degree"]
        for key, value in payload["thresholds"].items()
    }


def top_row_criterion(
    n: int,
    rows: dict[int, list[int]],
    tables: dict[int, ExactInverseShadow],
    thresholds: list[int],
) -> dict[str, Any]:
    previous_threshold = thresholds[-2]
    previous_degree = n - 2
    previous_ambient = comb(n, previous_degree) ** 2
    candidates = []

    for retained_terms in range(previous_threshold + 1):
        previous_deficit = (
            previous_ambient - rows[previous_degree][retained_terms]
        )
        c4_shadow = tables[2].minimum[previous_deficit]
        candidate = retained_terms + ceil_div(c4_shadow, n)
        candidates.append(
            (
                candidate,
                retained_terms,
                previous_deficit,
                c4_shadow,
            )
        )

    criterion_value = max(n, *(row[0] for row in candidates))
    witnesses = [
        {
            "t": retained_terms,
            "previous_deficit": previous_deficit,
            "c4_shadow": c4_shadow,
        }
        for candidate, retained_terms, previous_deficit, c4_shadow in candidates
        if candidate == criterion_value
    ]
    require(criterion_value == thresholds[-1], (n, criterion_value, thresholds))

    return {
        "previous_threshold": previous_threshold,
        "top_threshold": thresholds[-1],
        "criterion_value": criterion_value,
        "top_gap": thresholds[-1] - previous_threshold,
        "maximizing_witnesses": witnesses,
    }


def build_payload() -> dict[str, Any]:
    published_thresholds = load_thresholds()
    expected_keys = {str(n) for n in range(3, 11)}
    require(set(published_thresholds) == expected_keys, published_thresholds)

    tail_constants = {}
    for k in range(2, 9):
        value, maximizers = tail_constant(k)
        tail_constants[str(k)] = {
            "value": value,
            "maximizing_a": maximizers,
        }
    require(
        [tail_constants[str(k)]["value"] for k in range(2, 9)]
        == [1, 5, 20, 83, 362, 1572, 7513],
        tail_constants,
    )

    capacity_lipschitz_checks = 0
    threshold_monotonicity_checks = 0
    rectangular_shadow_checks = 0
    tail_transport_checks = 0
    tail_threshold_checks = 0
    top_row_criteria: dict[str, Any] = {}
    c4_profiles: dict[str, list[int]] = {}

    for n in range(3, 9):
        thresholds = published_thresholds[str(n)]
        maximum_terms = max(thresholds)
        tables = {
            degree: ExactInverseShadow(n, degree)
            for degree in range(2, n)
        }
        rows = direct_tower_rows(n, tables, maximum_terms)

        observed = []
        for degree in range(1, n):
            row = rows[degree]
            one_term = comb(n, degree)
            ambient = one_term**2
            observed.append(next(q for q, value in enumerate(row) if value == ambient))
            for left, right in zip(row, row[1:]):
                require(0 <= right - left <= one_term, (n, degree, left, right))
                capacity_lipschitz_checks += 1
        require(observed == thresholds, (n, observed, thresholds))

        for left, right in zip(thresholds, thresholds[1:]):
            require(left <= right, (n, thresholds))
            threshold_monotonicity_checks += 1

        for degree in range(2, n):
            minimum = tables[degree].minimum
            for a in range(degree, n + 1):
                family_limit = comb(a, degree) * comb(n, degree)
                shadow_bound = (
                    comb(a, degree - 1) * comb(n, degree - 1)
                )
                for family_size in range(family_limit + 1):
                    require(
                        minimum[family_size] <= shadow_bound,
                        (n, degree, a, family_size),
                    )
                    rectangular_shadow_checks += 1

        for k in range(2, n):
            if n < 2 * k:
                continue
            previous_degree = n - k
            next_degree = previous_degree + 1
            previous_threshold = thresholds[previous_degree - 1]
            next_threshold = thresholds[next_degree - 1]
            constant = tail_constants[str(k)]["value"]
            require(
                0 <= next_threshold - previous_threshold <= constant,
                (n, k, previous_threshold, next_threshold, constant),
            )
            tail_threshold_checks += 1

            previous_ambient = comb(n, k) ** 2
            next_one_term = comb(n, k - 1)
            next_ambient = next_one_term**2
            complementary_shadow = tables[k].minimum
            for retained_terms in range(previous_threshold + 1):
                distance = previous_threshold - retained_terms
                previous_deficit = (
                    previous_ambient
                    - rows[previous_degree][retained_terms]
                )
                direct_deficit = max(
                    0,
                    next_ambient - retained_terms * next_one_term,
                    complementary_shadow[previous_deficit],
                )
                require(
                    direct_deficit
                    <= (distance + constant) * next_one_term,
                    (
                        n,
                        k,
                        retained_terms,
                        direct_deficit,
                        (distance + constant) * next_one_term,
                    ),
                )
                tail_transport_checks += 1

        top_row_criteria[str(n)] = top_row_criterion(
            n,
            rows,
            tables,
            thresholds,
        )

        if n in (3, 4):
            graph_profile = c4_minimum_edge_profile(n)
            require(graph_profile == list(tables[2].minimum), (n, graph_profile))
            c4_profiles[str(n)] = graph_profile

    for n in range(3, 11):
        thresholds = published_thresholds[str(n)]
        require(
            all(left <= right for left, right in zip(thresholds, thresholds[1:])),
            (n, thresholds),
        )
        require(0 <= thresholds[-1] - thresholds[-2] <= 1, (n, thresholds))

        for k in range(2, n):
            if n < 2 * k:
                continue
            previous_index = n - k - 1
            next_index = n - k
            constant = tail_constants.get(str(k))
            if constant is None:
                value, maximizers = tail_constant(k)
                constant = {"value": value, "maximizing_a": maximizers}
            require(
                thresholds[next_index] - thresholds[previous_index]
                <= constant["value"],
                (n, k, thresholds),
            )

    require(capacity_lipschitz_checks == 1151, capacity_lipschitz_checks)
    require(threshold_monotonicity_checks == 21, threshold_monotonicity_checks)
    require(rectangular_shadow_checks == 32_373, rectangular_shadow_checks)
    require(tail_transport_checks == 430, tail_transport_checks)
    require(tail_threshold_checks == 9, tail_threshold_checks)

    phi = (1 + sqrt(5)) / 2
    beta = phi ** (phi + 2)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_TOWER_THRESHOLD_MONOTONICITY",
            "GENERAL_FIXED_CODIMENSION_TAIL_BOUND",
            "TOP_ROW_GAP_AT_MOST_ONE",
            "C4_TOP_ROW_CRITERION",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "threshold_monotonicity": (
                "Q_(n,d)>=Q_(n,d-1), so Theta_n=Q_(n,n-1)."
            ),
            "row_lipschitz": (
                "0<=B_(n,d)(q+1)-B_(n,d)(q)<=binom(n,d)."
            ),
            "tail_constant": (
                "c_k=max_(a>=k)[binom(a,k-1)-binom(a-1,k)-1]_+."
            ),
            "tail_increment": (
                "For n>=2k, "
                "0<=Q_(n,n-k+1)-Q_(n,n-k)<=c_k."
            ),
            "fixed_tail": (
                "For n>=2K, "
                "0<=Theta_n-Q_(n,n-K)<=sum_(k=2)^K c_k."
            ),
            "top_row": (
                "Q_(n,n-2)<=Theta_n<=Q_(n,n-2)+1."
            ),
            "c4_interpretation": (
                "F_(n,2)(z) is the minimum edge count of an n-by-n "
                "bipartite graph containing at least z copies of K_(2,2)."
            ),
            "tail_asymptotic": (
                "lim_(k->infinity) c_k^(1/k)=phi^(phi+2), "
                "phi=(1+sqrt(5))/2."
            ),
        },
        "tail_constants": tail_constants,
        "tail_asymptotic": {
            "phi_expression": "(1+sqrt(5))/2",
            "beta_expression": "phi^(phi+2)",
            "beta_decimal": round(beta, 15),
        },
        "threshold_replay": {
            key: {
                "by_degree": row,
                "adjacent_gaps": [
                    right - left for left, right in zip(row, row[1:])
                ],
                "theta": row[-1],
                "top_gap": row[-1] - row[-2],
            }
            for key, row in published_thresholds.items()
        },
        "top_row_criteria": top_row_criteria,
        "c4_profiles": c4_profiles,
        "exhaustive_replay": {
            "n_min": 3,
            "n_max": 8,
            "capacity_lipschitz_checks": capacity_lipschitz_checks,
            "threshold_monotonicity_checks": threshold_monotonicity_checks,
            "rectangular_shadow_checks": rectangular_shadow_checks,
            "tail_transport_checks": tail_transport_checks,
            "tail_threshold_checks": tail_threshold_checks,
            "bipartite_graphs_enumerated": (1 << 9) + (1 << 16),
        },
        "claim_boundary": (
            "The monotonicity, tail constants, asymptotic constant and C4 "
            "criterion are general statements about the exact scalar "
            "derivative tower. The finite replay reproduces the existing "
            "PR #51 thresholds and introduces no new ordinary Chow-rank "
            "number. The result does not determine the scalar tower's "
            "linear-codimension asymptotic, prove a Chow-realizability "
            "defect, improve border rank, determine an exact rank for n>=6, "
            "or prove general Glynn optimality. Literature novelty is not "
            "established."
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
    print("GENERAL_TOWER_TAIL_CONSTANTS_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
