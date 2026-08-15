#!/usr/bin/env python3
"""Exact simultaneous product-shadow minimization for permanent derivatives.

For 1 <= m <= n-1, the degree-m derivative space of perm_n has a basis
indexed by pairs of m-subsets.  The first derivative shadow of a coordinate
family is the simultaneous lower shadow in

    C([n], m) x C([n], m).

Two coordinatewise Kruskal--Katona compressions reduce the exact minimum to a
Ferrers partition.  This module implements the resulting integer dynamic
program and the induced exact refinement of the general multishadow Chow-rank
bound.

The code uses only Python's standard library and exact integer arithmetic.
It is a deterministic finite replay; the compression theorem itself is proved
in docs/general_exact_product_shadow.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable


def require(condition: bool, message: object) -> None:
    """Fail closed independently of Python optimization mode."""

    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, ("nonpositive denominator", denominator))
    return -(-numerator // denominator)


def colex_rank(subset: tuple[int, ...]) -> int:
    """Zero-based colex rank via the combinatorial number system."""

    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def colex_subsets(n: int, m: int) -> tuple[tuple[int, ...], ...]:
    require(1 <= m <= n - 1, ("invalid layer", n, m))
    values = tuple(sorted(combinations(range(n), m), key=colex_rank))
    require(len(values) == comb(n, m), (n, m, len(values)))
    require(
        tuple(colex_rank(value) for value in values) == tuple(range(len(values))),
        ("colex ranks are not contiguous", n, m),
    )
    return values


def initial_shadow_profile(
    n: int,
    m: int,
    subsets: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[int, ...]:
    """k(t): shadow size of the first t m-subsets in colex order."""

    layer = subsets if subsets is not None else colex_subsets(n, m)
    shadow: set[tuple[int, ...]] = set()
    profile = [0]
    for subset in layer:
        for position in range(m):
            shadow.add(subset[:position] + subset[position + 1 :])
        profile.append(len(shadow))
    require(profile[-1] == comb(n, m - 1), (n, m, profile[-1]))
    require(all(left <= right for left, right in zip(profile, profile[1:])), profile)
    return tuple(profile)


def first_container_weights(
    n: int,
    m: int,
    subsets: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[int, ...]:
    """Count lower subsets by their first containing colex m-subset.

    If A is an m-subset and c is its least missing ground element, then its
    weight is c (with the ground set indexed by 0,...,n-1).
    """

    layer = subsets if subsets is not None else colex_subsets(n, m)
    weights = []
    for subset in layer:
        present = set(subset)
        least_missing = next(value for value in range(n) if value not in present)
        weights.append(least_missing)

    # Independent finite verification of the closed formula.
    index = {subset: position for position, subset in enumerate(layer)}
    enumerated = [0] * len(layer)
    for lower in combinations(range(n), m - 1):
        missing = next(value for value in range(n) if value not in lower)
        first = tuple(sorted(lower + (missing,)))
        enumerated[index[first]] += 1
    require(tuple(weights) == tuple(enumerated), (n, m, weights, enumerated))
    require(sum(weights) == comb(n, m - 1), (n, m, sum(weights)))
    return tuple(weights)


@dataclass(frozen=True)
class ShadowMinimum:
    n: int
    m: int
    family_size: int
    shadow_size: int
    minimizing_partition: tuple[int, ...]
    partition_count: int
    dynamic_state_count: int


class ExactProductShadow:
    """Exact Ferrers dynamic program for one (n,m) product layer."""

    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.subsets = colex_subsets(n, m)
        self.layer_size = len(self.subsets)
        self.k = initial_shadow_profile(n, m, self.subsets)
        self.weights = first_container_weights(n, m, self.subsets)
        self._infinity = 10**30

        @lru_cache(maxsize=None)
        def solve(index: int, upper: int, remaining: int) -> tuple[int, int]:
            if index == self.layer_size:
                return (0, 1) if remaining == 0 else (self._infinity, 0)

            rows_left = self.layer_size - index
            if remaining < 0 or remaining > upper * rows_left:
                return self._infinity, 0

            minimum_x = ceil_div(remaining, rows_left)
            maximum_x = min(upper, remaining, self.layer_size)
            best = self._infinity
            count = 0
            for value in range(minimum_x, maximum_x + 1):
                tail_sum = remaining - value
                if tail_sum > value * (rows_left - 1):
                    continue
                tail_value, tail_count = solve(index + 1, value, tail_sum)
                candidate = self.weights[index] * self.k[value] + tail_value
                if candidate < best:
                    best = candidate
                    count = tail_count
                elif candidate == best:
                    count += tail_count
            return best, count

        self._solve = solve

    def objective(self, partition: Iterable[int]) -> int:
        values = tuple(partition)
        require(len(values) == self.layer_size, ("partition length", len(values)))
        require(
            all(
                self.layer_size >= values[index] >= values[index + 1] >= 0
                for index in range(self.layer_size - 1)
            )
            and 0 <= values[-1] <= self.layer_size,
            ("not a Ferrers partition", values),
        )
        return sum(
            weight * self.k[value]
            for weight, value in zip(self.weights, values, strict=True)
        )

    def minimum(self, family_size: int) -> ShadowMinimum:
        require(
            0 <= family_size <= self.layer_size**2,
            ("family size outside product layer", family_size),
        )
        best, count = self._solve(0, self.layer_size, family_size)
        require(best < self._infinity and count > 0, (family_size, best, count))

        partition: list[int] = []
        index = 0
        upper = self.layer_size
        remaining = family_size
        while index < self.layer_size:
            target, _ = self._solve(index, upper, remaining)
            rows_left = self.layer_size - index
            minimum_x = ceil_div(remaining, rows_left)
            maximum_x = min(upper, remaining, self.layer_size)
            selected: int | None = None
            for value in range(minimum_x, maximum_x + 1):
                tail_sum = remaining - value
                if tail_sum > value * (rows_left - 1):
                    continue
                tail_value, _ = self._solve(index + 1, value, tail_sum)
                candidate = self.weights[index] * self.k[value] + tail_value
                if candidate == target:
                    selected = value
                    break
            require(selected is not None, ("missing witness choice", index, remaining))
            partition.append(selected)
            remaining -= selected
            upper = selected
            index += 1

        witness = tuple(partition)
        require(sum(witness) == family_size, (family_size, sum(witness)))
        require(self.objective(witness) == best, (family_size, best, witness))
        return ShadowMinimum(
            n=self.n,
            m=self.m,
            family_size=family_size,
            shadow_size=best,
            minimizing_partition=witness,
            partition_count=count,
            dynamic_state_count=self._solve.cache_info().currsize,
        )


def first_koszul_data(n: int, output_degree: int) -> tuple[int, int, int]:
    require(2 <= output_degree <= n - 2, (n, output_degree))
    dimension = n * n
    target_rank = (
        dimension * comb(n, output_degree) ** 2
        - comb(n, output_degree + 1) ** 2
    )
    one_term_cap = (
        dimension * comb(n, output_degree)
        - comb(n, output_degree + 1)
    )
    base_bound = ceil_div(target_rank, one_term_cap)
    return target_rank, one_term_cap, base_bound


def exact_intersection_cap(
    shadow: ExactProductShadow,
    fixed_term_count: int,
) -> tuple[int, ShadowMinimum, ShadowMinimum | None]:
    """Largest b whose exact product shadow fits the q-term derivative cap."""

    require(fixed_term_count >= 1, fixed_term_count)
    threshold = fixed_term_count * comb(shadow.n, shadow.m - 1)
    last_good = shadow.minimum(0)
    first_bad: ShadowMinimum | None = None
    for family_size in range(1, shadow.layer_size**2 + 1):
        current = shadow.minimum(family_size)
        if current.shadow_size <= threshold:
            last_good = current
            continue
        first_bad = current
        break
    require(first_bad is not None, ("threshold reaches full layer", threshold))
    require(last_good.family_size + 1 == first_bad.family_size, (last_good, first_bad))
    return threshold, last_good, first_bad


def exact_multishadow_bound(
    n: int,
    output_degree: int,
    fixed_term_count: int,
) -> dict[str, object]:
    complement_degree = n - output_degree
    shadow = ExactProductShadow(n, complement_degree)
    target_rank, one_term_cap, base_bound = first_koszul_data(n, output_degree)
    require(fixed_term_count <= base_bound, (fixed_term_count, base_bound))
    threshold, last_good, first_bad = exact_intersection_cap(
        shadow,
        fixed_term_count,
    )
    residual_numerator = target_rank - n * n * last_good.family_size
    require(residual_numerator > 0, residual_numerator)
    residual_terms = ceil_div(residual_numerator, one_term_cap)
    total_bound = fixed_term_count + residual_terms
    return {
        "n": n,
        "output_degree": output_degree,
        "complement_degree": complement_degree,
        "fixed_term_count": fixed_term_count,
        "derivative_shadow_threshold": threshold,
        "exact_intersection_cap": last_good.family_size,
        "shadow_at_cap": last_good.shadow_size,
        "shadow_at_first_excluded_size": first_bad.shadow_size,
        "first_excluded_size": first_bad.family_size,
        "first_koszul_target_rank": target_rank,
        "one_term_koszul_cap": one_term_cap,
        "base_first_koszul_bound": base_bound,
        "residual_rank_numerator": residual_numerator,
        "residual_term_count": residual_terms,
        "exact_multishadow_lower_bound": total_bound,
        "cap_partition_count": last_good.partition_count,
        "cap_partition": list(last_good.minimizing_partition),
        "first_excluded_partition": list(first_bad.minimizing_partition),
        "dynamic_state_count": first_bad.dynamic_state_count,
    }


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_payload() -> dict[str, object]:
    # Regression against the specialized N6-056 product-shadow table.
    n6_shadow = ExactProductShadow(6, 3)
    n6_rows = [
        {
            "family_size": value,
            "minimum_shadow": n6_shadow.minimum(value).shadow_size,
        }
        for value in range(40, 66)
    ]
    expected_n6 = {
        40: 60,
        41: 66,
        42: 69,
        43: 69,
        44: 72,
        45: 72,
        46: 72,
        47: 75,
        48: 75,
        49: 75,
        50: 75,
        51: 78,
        52: 78,
        53: 81,
        54: 81,
        55: 81,
        56: 83,
        57: 83,
        58: 83,
        59: 84,
        60: 84,
        61: 84,
        62: 84,
        63: 84,
        64: 84,
        65: 87,
    }
    require(
        {row["family_size"]: row["minimum_shadow"] for row in n6_rows}
        == expected_n6,
        n6_rows,
    )

    n7 = exact_multishadow_bound(7, 3, 13)
    require(n7["exact_intersection_cap"] == 238, n7)
    require(n7["shadow_at_cap"] == 452, n7)
    require(n7["first_excluded_size"] == 239, n7)
    require(n7["shadow_at_first_excluded_size"] == 456, n7)
    require(n7["derivative_shadow_threshold"] == 455, n7)
    require(n7["first_koszul_target_rank"] == 58_800, n7)
    require(n7["one_term_koszul_cap"] == 1_680, n7)
    require(n7["residual_term_count"] == 29, n7)
    require(n7["exact_multishadow_lower_bound"] == 42, n7)

    core = {
        "status": [
            "GENERAL_EXACT_PRODUCT_SHADOW_PROOF_DRAFT",
            "EXACT_INTEGER_DP_REPLAYED",
            "PERM7_LOWER_42",
        ],
        "theorem": {
            "coordinate_specialization": (
                "Every b-plane in D_m(perm_n) specializes to a coordinate "
                "b-plane with no larger first-derivative shadow."
            ),
            "ferrers_reduction": (
                "Two coordinatewise colex compressions reduce the exact "
                "minimum simultaneous product shadow to Ferrers partitions."
            ),
            "objective": "F_n,m(b)=min_lambda sum_i w_i*k(lambda_i)",
            "weight_formula": "w_i=min([n]\\A_i) for the i-th colex m-subset A_i",
        },
        "n6_regression": n6_rows,
        "n7_application": n7,
        "claim_boundary": (
            "This is an exact ordinary-rank refinement of the finite "
            "multishadow cap. It does not prove the conjectural value "
            "2^(n-1), an unrestricted exact value for perm_6 or perm_7, "
            "or a new border-Chow-rank bound. Literature novelty is not "
            "claimed."
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
    print("GENERAL_EXACT_PRODUCT_SHADOW_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
