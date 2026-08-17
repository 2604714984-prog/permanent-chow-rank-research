#!/usr/bin/env python3
"""Exact finite replay for two-direction apolar power profiles.

The mathematical proof is in docs/general_two_direction_power_profiles.md.
This script uses only deterministic integer matrices and exact arithmetic over
F_1000003.  Modular rank is used only as a lower certificate; every reported
rank is matched by a characteristic-zero dimension/syzygy upper bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import ceil, comb
from pathlib import Path
from typing import Callable, Iterable


PRIME = 1_000_003
ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CORE_SHA256 = "e6086e5cb2f884adbd17135fd41738610c11185830100007a22605e03a003b47"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def subset_masks(n: int, degree: int) -> tuple[int, ...]:
    return tuple(mask for mask in range(1 << n) if mask.bit_count() == degree)


def boolean_basis(n: int, degree: int) -> tuple[int, ...]:
    return subset_masks(n, degree)


def permanent_basis(n: int, degree: int) -> tuple[tuple[int, int], ...]:
    layer = subset_masks(n, degree)
    return tuple((rows, columns) for rows in layer for columns in layer)


def boolean_transitions(
    n: int,
    coefficients: tuple[int, ...],
    degree: int,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    source = boolean_basis(n, degree)
    target = boolean_basis(n, degree + 1)
    target_index = {mask: index for index, mask in enumerate(target)}
    transitions = []
    for mask in source:
        row = []
        for variable, coefficient in enumerate(coefficients):
            if not mask & (1 << variable) and coefficient % PRIME:
                row.append(
                    (
                        target_index[mask | (1 << variable)],
                        coefficient % PRIME,
                    )
                )
        transitions.append(tuple(row))
    return tuple(transitions)


def permanent_transitions(
    n: int,
    coefficients: tuple[tuple[int, ...], ...],
    degree: int,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    source = permanent_basis(n, degree)
    target = permanent_basis(n, degree + 1)
    target_index = {cell: index for index, cell in enumerate(target)}
    transitions = []
    for rows, columns in source:
        row = []
        for i in range(n):
            if rows & (1 << i):
                continue
            for j in range(n):
                if columns & (1 << j):
                    continue
                coefficient = coefficients[i][j] % PRIME
                if coefficient:
                    row.append(
                        (
                            target_index[(rows | (1 << i), columns | (1 << j))],
                            coefficient,
                        )
                    )
        transitions.append(tuple(row))
    return tuple(transitions)


def apply_transitions(
    vector: dict[int, int],
    transitions: tuple[tuple[tuple[int, int], ...], ...],
) -> dict[int, int]:
    result: dict[int, int] = {}
    for source_index, source_coefficient in vector.items():
        for target_index, edge_coefficient in transitions[source_index]:
            value = (
                result.get(target_index, 0)
                + source_coefficient * edge_coefficient
            ) % PRIME
            if value:
                result[target_index] = value
            elif target_index in result:
                del result[target_index]
    return result


def sparse_rank(columns: Iterable[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for original in columns:
        vector = dict(original)
        while vector:
            pivot = max(vector)
            if pivot not in pivots:
                inverse = pow(vector[pivot], PRIME - 2, PRIME)
                normalized = {
                    row: coefficient * inverse % PRIME
                    for row, coefficient in vector.items()
                }
                pivots[pivot] = normalized
                break
            factor = vector[pivot]
            basis = pivots[pivot]
            for row, coefficient in basis.items():
                value = (vector.get(row, 0) - factor * coefficient) % PRIME
                if value:
                    vector[row] = value
                elif row in vector:
                    del vector[row]
    return len(pivots)


def power_columns(
    source_size: int,
    power: int,
    degree: int,
    transition_builder: Callable[[int, int], tuple[tuple[tuple[int, int], ...], ...]],
) -> list[dict[int, int]]:
    columns: list[dict[int, int]] = []
    source_degree = degree - power
    for right_count in range(power + 1):
        transition_sequence = [0] * (power - right_count) + [1] * right_count
        for source_index in range(source_size):
            vector = {source_index: 1}
            current_degree = source_degree
            for which in transition_sequence:
                vector = apply_transitions(
                    vector,
                    transition_builder(which, current_degree),
                )
                current_degree += 1
            columns.append(vector)
    return columns


def commutative_upper_cap(
    target_dimension: int,
    source_dimension: int,
    degree_one_dimension: int,
    power: int,
    source_degree: int,
) -> int:
    cap = min(target_dimension, (power + 1) * source_dimension)
    if source_degree == 1:
        # The restriction Sym^p(W) tensor W -> Sym^(p+1)(W) has a
        # p-dimensional kernel.  It sits inside the complete source.
        cap = min(cap, (power + 1) * degree_one_dimension - power)
    return cap


def deterministic_boolean_forms(n: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return tuple(1 for _ in range(n)), tuple(index + 1 for index in range(n))


def deterministic_permanent_forms(
    n: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    left = tuple(
        tuple((i + 1) * (j + 2) + (i - j) ** 2 + 1 for j in range(n))
        for i in range(n)
    )
    right = tuple(
        tuple((i + 2) ** 2 + (j + 1) ** 3 + 3 * i * j + 5 for j in range(n))
        for i in range(n)
    )
    return left, right


def boolean_rank(n: int, power: int, degree: int) -> int:
    source_degree = degree - power
    source = boolean_basis(n, source_degree)
    forms = deterministic_boolean_forms(n)
    cache: dict[tuple[int, int], tuple[tuple[tuple[int, int], ...], ...]] = {}

    def builder(which: int, current_degree: int):
        key = (which, current_degree)
        if key not in cache:
            cache[key] = boolean_transitions(n, forms[which], current_degree)
        return cache[key]

    columns = power_columns(len(source), power, degree, builder)
    return sparse_rank(columns)


def permanent_rank(n: int, power: int, degree: int) -> int:
    source_degree = degree - power
    source = permanent_basis(n, source_degree)
    forms = deterministic_permanent_forms(n)
    cache: dict[tuple[int, int], tuple[tuple[tuple[int, int], ...], ...]] = {}

    def builder(which: int, current_degree: int):
        key = (which, current_degree)
        if key not in cache:
            cache[key] = permanent_transitions(n, forms[which], current_degree)
        return cache[key]

    columns = power_columns(len(source), power, degree, builder)
    return sparse_rank(columns)


def build_payload() -> dict[str, object]:
    existing_bounds = {3: 4, 4: 8, 5: 16, 6: 28}
    tables: dict[str, object] = {}
    profile_checks = 0
    cap_checks = 0

    for n in range(3, 7):
        entries = []
        best_numerator = 0
        best_denominator = 1
        best_entry: dict[str, int] | None = None
        for power in range(1, n + 1):
            for degree in range(power, n + 1):
                source_degree = degree - power
                boolean_value = boolean_rank(n, power, degree)
                permanent_value = permanent_rank(n, power, degree)

                boolean_cap = commutative_upper_cap(
                    comb(n, degree),
                    comb(n, source_degree),
                    n,
                    power,
                    source_degree,
                )
                permanent_cap = commutative_upper_cap(
                    comb(n, degree) ** 2,
                    comb(n, source_degree) ** 2,
                    n * n,
                    power,
                    source_degree,
                )
                require(boolean_value == boolean_cap, (n, power, degree, boolean_value, boolean_cap))
                require(permanent_value == permanent_cap, (n, power, degree, permanent_value, permanent_cap))
                cap_checks += 2

                certified_bound = ceil(permanent_value / boolean_value)
                entry = {
                    "power": power,
                    "target_degree": degree,
                    "source_degree": source_degree,
                    "boolean_cap": boolean_value,
                    "permanent_rank": permanent_value,
                    "ratio_numerator": permanent_value,
                    "ratio_denominator": boolean_value,
                    "certified_lower_bound": certified_bound,
                }
                entries.append(entry)
                profile_checks += 1

                if permanent_value * best_denominator > best_numerator * boolean_value:
                    best_numerator = permanent_value
                    best_denominator = boolean_value
                    best_entry = entry

        require(best_entry is not None, n)
        best_bound = ceil(best_numerator / best_denominator)
        expected = {3: 3, 4: 6, 5: 10, 6: 20}[n]
        require(best_bound == expected, (n, best_bound, best_entry))
        require(best_bound < existing_bounds[n], (n, best_bound, existing_bounds[n]))
        tables[str(n)] = {
            "profile_entries": entries,
            "best_ratio_numerator": best_numerator,
            "best_ratio_denominator": best_denominator,
            "best_certified_lower_bound": best_bound,
            "best_power": best_entry["power"],
            "best_target_degree": best_entry["target_degree"],
            "existing_repository_lower_bound": existing_bounds[n],
        }

    require(profile_checks == 52, profile_checks)
    require(cap_checks == 104, cap_checks)

    core: dict[str, object] = {
        "status": [
            "GENERAL_TWO_DIRECTION_APOLAR_SUBQUOTIENT",
            "GENERAL_BOOLEAN_SINGLE_TERM_ENVELOPE",
            "FINITE_TWO_DIRECTION_POWER_PROFILE_BARRIER_N3_TO_N6",
            "EXACT_INTEGER_MODULAR_REPLAYED",
        ],
        "theorem": {
            "apolar_subquotient": (
                "If f=sum_i T_i, then A_f is a k[W]-subquotient of "
                "direct_sum_i A_(T_i) for every W subset S_1."
            ),
            "power_profile_monotonicity": (
                "Lambda_(p,d)(M;W)=dim((W^p M) intersect M_d) is additive "
                "on direct sums and nonincreasing under submodules and quotients."
            ),
            "boolean_envelope": (
                "For T=product_i ell_i, A_T is a k[W]-subquotient of the "
                "squarefree Boolean module B_n under D -> sum_i D(ell_i) z_i."
            ),
            "rank_bound": (
                "ChowRank(f)>=ceil(Lambda_(p,d)(A_f;W)/beta_(n,p,d)), "
                "where beta is the maximum two-direction Boolean profile."
            ),
            "finite_barrier": (
                "For n=3,4,5,6, the best possible homogeneous power-profile "
                "bounds are 3,6,10,20; they do not reach the existing "
                "repository bounds 4,8,16,28."
            ),
        },
        "finite_replay": {
            "prime": PRIME,
            "n_min": 3,
            "n_max": 6,
            "profile_checks": profile_checks,
            "rank_cap_matches": cap_checks,
            "tables": tables,
        },
        "claim_boundary": (
            "The general subquotient and monotonicity statements are exact. "
            "The route barrier is finite and applies only to homogeneous "
            "maximal-ideal powers W^p through n=6. It does not classify all "
            "homogeneous ideals in k[s,t], all two-direction module invariants, "
            "multigraded relation modules, Chow-realizability defects, border "
            "rank, or exact Chow rank for n>=6. No new numerical Chow-rank "
            "lower bound is introduced. Literature novelty is not established."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload["core_sha256"])
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
    print("GENERAL_TWO_DIRECTION_POWER_PROFILES_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
