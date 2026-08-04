#!/usr/bin/env python3
"""Exact q=6,7,8 route diagnostic for a hypothetical 25-term perm_6 decomposition."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

TOTAL_TERMS = 25
FIXED_CHOICES = (6, 7, 8)
PERM_CENTRAL = 400
PERM_KOSZUL = 14_175
TERM_CENTRAL = 20
TERM_KOSZUL = 705
TERM_QUADRATIC = 15
TERM_INTERSECTION = 3
VARIABLES = 36
CENTRAL_LOWER: dict[int, int | None] = {
    15: 20,
    14: 20,
    13: 18,
    12: None,
    11: 14,
    10: 0,
    9: 0,
    8: 0,
    7: 0,
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0,
}


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def gbinom(value: Fraction, degree: int) -> Fraction:
    out = Fraction(1)
    for index in range(degree):
        out *= value - index
    return out / factorial(degree)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def shadow_certificate(dimension: int) -> dict[str, object]:
    for integer in range(3, 30):
        value = Fraction(integer)
        if gbinom(value, 3) ** 2 == dimension:
            shadow = gbinom(value, 2) ** 2
            if shadow.denominator != 1:
                raise AssertionError((dimension, shadow))
            return {
                "dimension": dimension,
                "integer_shadow_lower_bound": int(shadow),
                "lower_separator": str(value),
                "upper_separator": str(value),
                "exact_root": True,
            }
    for denominator in (10, 100, 1_000, 10_000, 100_000, 1_000_000):
        low, high = 2 * denominator, 12 * denominator
        while low + 1 < high:
            middle = (low + high) // 2
            value = Fraction(middle, denominator)
            if gbinom(value, 3) ** 2 < dimension:
                low = middle
            else:
                high = middle
        lower = Fraction(low, denominator)
        upper = Fraction(high, denominator)
        if not gbinom(lower, 3) ** 2 < dimension < gbinom(upper, 3) ** 2:
            continue
        lower_shadow = gbinom(lower, 2) ** 2
        upper_shadow = gbinom(upper, 2) ** 2
        if floor_fraction(lower_shadow) != floor_fraction(upper_shadow):
            continue
        result = floor_fraction(lower_shadow) + 1
        if lower_shadow > result - 1 and upper_shadow < result:
            return {
                "dimension": dimension,
                "integer_shadow_lower_bound": result,
                "lower_separator": str(lower),
                "upper_separator": str(upper),
                "exact_root": False,
            }
    raise AssertionError(f"no exact shadow bracket for {dimension}")


def macaulay(value: int) -> int:
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


@lru_cache(maxsize=None)
def partition_cap(total: int, colors: int) -> int:
    best = 0

    def rec(remaining: int, slots: int, lower: int, subtotal: int) -> None:
        nonlocal best
        if slots == 1:
            if remaining >= lower:
                best = max(best, subtotal + macaulay(remaining))
            return
        for value in range(lower, remaining + 1):
            rec(remaining - value, slots - 1, value, subtotal + macaulay(value))

    rec(total, colors, 0, 0)
    return best


def projection_cap(fixed: int) -> int:
    return 15 * (fixed - 1) + 3


def residual(fixed: int) -> int:
    return TOTAL_TERMS - fixed


def b_lower(fixed: int) -> int:
    return max(0, PERM_CENTRAL - TERM_CENTRAL * residual(fixed))


def h_upper(fixed: int, b: int) -> int:
    return min(
        TERM_CENTRAL * fixed,
        TERM_CENTRAL * residual(fixed) - PERM_CENTRAL + 2 * b,
    )


@lru_cache(maxsize=None)
def epsilon_types(fixed: int, budget: int) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], lower: int) -> None:
        if len(prefix) == fixed:
            if sum(prefix) - min(prefix) <= budget:
                rows.append(prefix)
            return
        for value in range(lower, 16):
            candidate = prefix + (value,)
            if len(candidate) > 1 and sum(candidate) - min(candidate) > budget:
                break
            rec(candidate, value)

    rec((), 0)
    return tuple(rows)


def multiplicity(values: tuple[int, ...]) -> int:
    counts = Counter(values)
    result = factorial(len(values))
    for count in counts.values():
        result //= factorial(count)
    return result


def evaluate_type(epsilon: tuple[int, ...], budget: int) -> tuple[int, int] | None:
    central = 0
    for value in epsilon:
        lower = CENTRAL_LOWER[15 - value]
        if lower is None:
            return None
        central += lower
    relation = budget - sum(epsilon) + min(epsilon)
    if relation < 0:
        raise AssertionError((epsilon, budget, relation))
    return central - 2 * macaulay(relation), relation


def layer(fixed: int, b: int, certificate: dict[str, object]) -> dict[str, object]:
    shadow = int(certificate["integer_shadow_lower_bound"])
    budget = projection_cap(fixed) - shadow
    types = epsilon_types(fixed, budget)
    feasible: list[tuple[int, tuple[int, ...], int, int]] = []
    labelled = 0
    impossible = 0
    for epsilon in types:
        count = multiplicity(epsilon)
        labelled += count
        result = evaluate_type(epsilon, budget)
        if result is None:
            impossible += count
            continue
        raw, relation = result
        feasible.append((raw, epsilon, relation, count))
    minimum_raw = min(row[0] for row in feasible)
    minimum = max(0, minimum_raw)
    minimizers = [list(row[1]) for row in feasible if row[0] == minimum_raw]
    maximum_h = h_upper(fixed, b)
    initial = maximum_h - b + 1
    excluded = max(0, min(maximum_h + 1, minimum) - b)
    return {
        "b": b,
        "shadow": shadow,
        "shadow_lower_separator": certificate["lower_separator"],
        "shadow_upper_separator": certificate["upper_separator"],
        "defect_budget": budget,
        "symmetric_epsilon_type_count": len(types),
        "labelled_epsilon_count": labelled,
        "impossible_dimension_twelve_labelled_count": impossible,
        "minimum_raw_central_lower": minimum_raw,
        "minimum_coupled_central_lower": minimum,
        "minimizer_epsilon_profiles": minimizers,
        "maximum_relation_cap": max(row[2] for row in feasible),
        "maximum_cubic_relation_cap": max(macaulay(row[2]) for row in feasible),
        "h_upper": maximum_h,
        "initial_state_count": initial,
        "central_excluded_state_count": excluded,
        "surviving_state_count": initial - excluded,
    }


def state(fixed: int, b: int, h: int, central_lower: int) -> dict[str, object]:
    d = h - b
    capacity = TERM_KOSZUL * residual(fixed)
    base = PERM_KOSZUL - VARIABLES * b
    required = max(0, capacity + 1 - base)
    maximum = VARIABLES * d
    if h < central_lower:
        route, cap = "vector_macaulay_central_exclusion", None
    elif required == 0:
        route, cap = "quotient_koszul_already_strict", None
    elif maximum < required:
        route, cap = "structural_exclusion_or_stronger_invariant_required", None
    else:
        route, cap = "relative_prolongation_cap_can_close", maximum - required
    return {
        "b": b,
        "h": h,
        "d": d,
        "central_lower": central_lower,
        "required_quotient_gain": required,
        "maximum_quotient_gain": maximum,
        "relative_prolongation_cap": cap,
        "route": route,
    }


def fixed_payload(fixed: int, certificates: dict[int, dict[str, object]]) -> dict[str, object]:
    lower = b_lower(fixed)
    upper = lower
    while int(certificates[upper + 1]["integer_shadow_lower_bound"]) <= projection_cap(fixed):
        upper += 1
    layers = [layer(fixed, b, certificates[b]) for b in range(lower, upper + 1)]
    states = [
        state(fixed, row["b"], h, int(row["minimum_coupled_central_lower"]))
        for row in layers
        for h in range(row["b"], int(row["h_upper"]) + 1)
    ]
    routes = Counter(str(row["route"]) for row in states)
    survivors = [row for row in states if row["route"] != "vector_macaulay_central_exclusion"]
    caps = Counter(
        int(row["relative_prolongation_cap"])
        for row in survivors
        if row["relative_prolongation_cap"] is not None
    )
    max_relation = max(int(row["defect_budget"]) for row in layers)
    for total in range(max_relation + 1):
        if partition_cap(total, fixed) != macaulay(total):
            raise AssertionError((fixed, total))
    zero = [0] * fixed
    policy = Counter()
    for row in layers:
        if row["surviving_state_count"] == 0:
            continue
        profiles = row["minimizer_epsilon_profiles"]
        if profiles == [zero]:
            policy["all_zero_unique"] += 1
        elif zero in profiles:
            policy["all_zero_tied"] += 1
        else:
            policy["all_zero_absent"] += 1
    summary = {
        "fixed_terms": fixed,
        "residual_terms": residual(fixed),
        "projection_cap": projection_cap(fixed),
        "central_intersection_range": [lower, upper],
        "first_shadow_excluded_b": upper + 1,
        "first_shadow_excluded_lower_bound": int(
            certificates[upper + 1]["integer_shadow_lower_bound"]
        ),
        "maximum_quadratic_relation_kernel_cap": max_relation,
        "module_partition_identity_verified_through": max_relation,
        "initial_state_count": len(states),
        "vector_macaulay_central_excluded_state_count": routes[
            "vector_macaulay_central_exclusion"
        ],
        "state_count_after_central_pruning": len(survivors),
        "surviving_b_range": [
            min(int(row["b"]) for row in survivors),
            max(int(row["b"]) for row in survivors),
        ],
        "fully_central_excluded_layer_count": sum(
            int(row["surviving_state_count"]) == 0 for row in layers
        ),
        "quotient_koszul_already_strict_state_count": routes[
            "quotient_koszul_already_strict"
        ],
        "relative_prolongation_state_count": routes[
            "relative_prolongation_cap_can_close"
        ],
        "structural_state_count": routes[
            "structural_exclusion_or_stronger_invariant_required"
        ],
        "relative_prolongation_cap_histogram": {
            str(key): value for key, value in sorted(caps.items())
        },
        "surviving_layer_minimizer_policy": {
            key: policy[key]
            for key in ("all_zero_unique", "all_zero_tied", "all_zero_absent")
        },
        "full_layer_table_sha256": digest(layers),
        "full_state_table_sha256": digest(states),
    }
    return {"summary": summary, "layers": layers, "states": states}


def build_full_payload() -> dict[str, object]:
    certificates: dict[int, dict[str, object]] = {}
    dimension = min(b_lower(q) for q in FIXED_CHOICES)
    maximum_cap = max(projection_cap(q) for q in FIXED_CHOICES)
    while True:
        certificates[dimension] = shadow_certificate(dimension)
        if dimension > 60 and int(
            certificates[dimension]["integer_shadow_lower_bound"]
        ) > maximum_cap:
            break
        dimension += 1
    fixed = [fixed_payload(q, certificates) for q in FIXED_CHOICES]
    summaries = [row["summary"] for row in fixed]
    if min(summaries, key=lambda row: row["state_count_after_central_pruning"])[
        "fixed_terms"
    ] != 6:
        raise AssertionError(summaries)
    return {
        "status": "EXACT_N6_LOWER26_FIXED_Q_DIAGNOSTIC_REPLAYED",
        "hypothetical_total_terms": TOTAL_TERMS,
        "fixed_term_choices": list(FIXED_CHOICES),
        "shadow_certificates": [certificates[key] for key in sorted(certificates)],
        "fixed_q": fixed,
        "route_decision": {
            "arithmetically_smallest_fixed_count": 6,
            "selected_for_proof_program": None,
            "reason": (
                "All tested fixed counts leave broad structural frontiers. "
                "The smallest case has 327 surviving states and 269 structural states, "
                "so the central first-Koszul relation-module route is suspended for lower 26."
            ),
            "next_research_class": (
                "a different flattening or a coupled invariant acting on many states at once; "
                "no registry, SAT layer, or geometric classification is authorized"
            ),
        },
        "claim_boundary": (
            "This computation does not exclude a 25-term decomposition, does not prove "
            "ChowRank(perm_6)>=26, and does not establish a border-rank lower bound."
        ),
    }


def compact_payload(full: dict[str, object]) -> dict[str, object]:
    shadows = full["shadow_certificates"]
    return {
        "status": full["status"],
        "hypothetical_total_terms": full["hypothetical_total_terms"],
        "fixed_term_choices": full["fixed_term_choices"],
        "shadow_dimension_range": [shadows[0]["dimension"], shadows[-1]["dimension"]],
        "shadow_certificate_table_sha256": digest(shadows),
        "fixed_q_summaries": [row["summary"] for row in full["fixed_q"]],
        "route_decision": full["route_decision"],
        "claim_boundary": full["claim_boundary"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--full-json", type=Path)
    args = parser.parse_args()
    full = build_full_payload()
    compact = compact_payload(full)
    text = json.dumps(compact, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    if args.full_json:
        args.full_json.parent.mkdir(parents=True, exist_ok=True)
        args.full_json.write_text(
            json.dumps(full, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print(text, end="")
    print("N6_LOWER26_FIXED_Q_DIAGNOSTIC_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
