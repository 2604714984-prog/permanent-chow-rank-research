#!/usr/bin/env python3
"""Exact iterated product shadows and block-projection Chow bounds.

The permanent derivative space ``D_m(perm_n)`` has a basis indexed by
``C([n],m) x C([n],m)``.  For every derivative order ``a``, torus
specialization and two coordinatewise colex compressions reduce the exact
minimum simultaneous ``a``-th lower shadow to a Ferrers partition.

This module combines those exact higher shadows with a linear section and
block-projection lemma.  A selected block of Chow terms need not have zero
intersection with the permanent derivative space: its exact intersection cap
is retained as an additive defect.  The resulting two-level bounds prove the
ordinary characteristic-zero lower bounds

    ChowRank(perm_7) >= 45,
    ChowRank(perm_8) >= 79.

All computation is deterministic exact integer arithmetic.  The companion
mathematical proof is ``docs/general_iterated_product_shadow_blocks.md``.
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
    """Fail closed even under ``python -O``."""

    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def colex_subsets(n: int, m: int) -> tuple[tuple[int, ...], ...]:
    require(1 <= m <= n - 1, (n, m))
    values = tuple(sorted(combinations(range(n), m), key=colex_rank))
    require(len(values) == comb(n, m), (n, m, len(values)))
    require(
        tuple(colex_rank(value) for value in values) == tuple(range(len(values))),
        ("noncontiguous colex ranks", n, m),
    )
    return values


def iterated_initial_shadow_profile(
    n: int,
    m: int,
    order: int,
    layer: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[int, ...]:
    """Size of the order-``a`` shadow of every colex initial segment."""

    require(1 <= order < m, (n, m, order))
    source = layer if layer is not None else colex_subsets(n, m)
    lower_degree = m - order
    shadow: set[tuple[int, ...]] = set()
    profile = [0]
    for subset in source:
        shadow.update(combinations(subset, lower_degree))
        profile.append(len(shadow))
    require(profile[-1] == comb(n, lower_degree), (n, m, order, profile[-1]))
    require(all(left <= right for left, right in zip(profile, profile[1:])), profile)
    return tuple(profile)


def iterated_first_container_weights(
    n: int,
    m: int,
    order: int,
    layer: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[int, ...]:
    """Weights for lower subsets grouped by their first colex container.

    If ``A_i`` is the i-th colex m-subset and ``c_i`` is its least missing
    ground element, the exact weight is ``binom(c_i, order)``.
    """

    require(1 <= order < m, (n, m, order))
    source = layer if layer is not None else colex_subsets(n, m)
    closed = []
    for subset in source:
        present = set(subset)
        least_missing = next(value for value in range(n) if value not in present)
        closed.append(comb(least_missing, order))

    # Independent finite verification of the closed form.
    lower_degree = m - order
    index = {subset: position for position, subset in enumerate(source)}
    enumerated = [0] * len(source)
    for lower in combinations(range(n), lower_degree):
        missing = [value for value in range(n) if value not in lower]
        first = tuple(sorted(lower + tuple(missing[:order])))
        enumerated[index[first]] += 1
    require(tuple(closed) == tuple(enumerated), (n, m, order, closed, enumerated))
    require(sum(closed) == comb(n, lower_degree), (n, m, order, sum(closed)))
    return tuple(closed)


@dataclass(frozen=True)
class ShadowMinimum:
    n: int
    m: int
    order: int
    family_size: int
    shadow_size: int
    minimizing_partition: tuple[int, ...]
    partition_count: int
    dynamic_state_count: int


class ExactIteratedProductShadow:
    """Exact Ferrers DP for an arbitrary derivative order."""

    def __init__(self, n: int, m: int, order: int) -> None:
        self.n = n
        self.m = m
        self.order = order
        self.layer = colex_subsets(n, m)
        self.layer_size = len(self.layer)
        self.profile = iterated_initial_shadow_profile(n, m, order, self.layer)
        self.weights = iterated_first_container_weights(n, m, order, self.layer)
        self._infinity = 10**30

        @lru_cache(maxsize=None)
        def solve(index: int, upper: int, remaining: int) -> tuple[int, int]:
            if index == self.layer_size:
                return (0, 1) if remaining == 0 else (self._infinity, 0)

            rows_left = self.layer_size - index
            if remaining < 0 or remaining > upper * rows_left:
                return self._infinity, 0

            minimum_part = ceil_div(remaining, rows_left)
            maximum_part = min(upper, remaining, self.layer_size)
            best = self._infinity
            count = 0
            for value in range(minimum_part, maximum_part + 1):
                tail_sum = remaining - value
                if tail_sum > value * (rows_left - 1):
                    continue
                tail_value, tail_count = solve(index + 1, value, tail_sum)
                candidate = self.weights[index] * self.profile[value] + tail_value
                if candidate < best:
                    best = candidate
                    count = tail_count
                elif candidate == best:
                    count += tail_count
            return best, count

        self._solve = solve

    def objective(self, partition: Iterable[int]) -> int:
        values = tuple(partition)
        require(len(values) == self.layer_size, len(values))
        require(
            all(
                self.layer_size >= values[index] >= values[index + 1] >= 0
                for index in range(self.layer_size - 1)
            )
            and 0 <= values[-1] <= self.layer_size,
            values,
        )
        return sum(
            weight * self.profile[value]
            for weight, value in zip(self.weights, values, strict=True)
        )

    def minimum(self, family_size: int) -> ShadowMinimum:
        require(0 <= family_size <= self.layer_size**2, family_size)
        best, count = self._solve(0, self.layer_size, family_size)
        require(best < self._infinity and count > 0, (family_size, best, count))

        witness: list[int] = []
        index = 0
        upper = self.layer_size
        remaining = family_size
        while index < self.layer_size:
            target, _ = self._solve(index, upper, remaining)
            rows_left = self.layer_size - index
            minimum_part = ceil_div(remaining, rows_left)
            maximum_part = min(upper, remaining, self.layer_size)
            selected: int | None = None
            for value in range(minimum_part, maximum_part + 1):
                tail_sum = remaining - value
                if tail_sum > value * (rows_left - 1):
                    continue
                tail_value, _ = self._solve(index + 1, value, tail_sum)
                if self.weights[index] * self.profile[value] + tail_value == target:
                    selected = value
                    break
            require(selected is not None, (index, remaining, target))
            witness.append(selected)
            remaining -= selected
            upper = selected
            index += 1

        partition = tuple(witness)
        require(sum(partition) == family_size, (family_size, partition))
        require(self.objective(partition) == best, (family_size, best, partition))
        return ShadowMinimum(
            n=self.n,
            m=self.m,
            order=self.order,
            family_size=family_size,
            shadow_size=best,
            minimizing_partition=partition,
            partition_count=count,
            dynamic_state_count=self._solve.cache_info().currsize,
        )

    def transition(self, threshold: int) -> tuple[ShadowMinimum, ShadowMinimum]:
        """Last family at or below ``threshold`` and the first above it."""

        full = self.minimum(self.layer_size**2)
        require(full.shadow_size > threshold, (threshold, full.shadow_size))
        lower = 0
        upper = self.layer_size**2
        while lower + 1 < upper:
            midpoint = (lower + upper) // 2
            if self.minimum(midpoint).shadow_size <= threshold:
                lower = midpoint
            else:
                upper = midpoint
        last_good = self.minimum(lower)
        first_bad = self.minimum(upper)
        require(last_good.family_size + 1 == first_bad.family_size, (last_good, first_bad))
        require(last_good.shadow_size <= threshold < first_bad.shadow_size, (threshold, last_good, first_bad))
        return last_good, first_bad


def first_koszul_data(n: int, output_degree: int) -> tuple[int, int, int]:
    require(2 <= output_degree <= n - 1, (n, output_degree))
    target = n * n * comb(n, output_degree) ** 2 - comb(n, output_degree + 1) ** 2
    one_term = n * n * comb(n, output_degree) - comb(n, output_degree + 1)
    return target, one_term, ceil_div(target, one_term)


def global_first_koszul_bound(n: int) -> int:
    return max(first_koszul_data(n, degree)[2] for degree in range(2, n))


def block_intersection_transition(
    n: int,
    derivative_degree: int,
    block_terms: int,
    derivative_order: int,
) -> dict[str, object]:
    shadow = ExactIteratedProductShadow(n, derivative_degree, derivative_order)
    threshold = block_terms * comb(n, derivative_degree - derivative_order)
    last_good, first_bad = shadow.transition(threshold)
    return {
        "n": n,
        "derivative_degree": derivative_degree,
        "block_terms": block_terms,
        "derivative_order": derivative_order,
        "block_derivative_capacity": threshold,
        "block_intersection_cap": last_good.family_size,
        "block_shadow_at_cap": last_good.shadow_size,
        "block_first_excluded_size": first_bad.family_size,
        "block_shadow_at_first_excluded_size": first_bad.shadow_size,
        "block_cap_partition_count": last_good.partition_count,
        "block_cap_partition": list(last_good.minimizing_partition),
        "block_first_excluded_partition_count": first_bad.partition_count,
        "block_first_excluded_partition": list(first_bad.minimizing_partition),
    }


def two_level_bound(
    n: int,
    output_degree: int,
    fixed_terms: int,
    block_terms: int,
    block_derivative_order: int,
) -> dict[str, object]:
    complement_degree = n - output_degree
    shadow_degree = complement_degree - 1
    require(2 <= shadow_degree, (n, output_degree))
    require(1 <= block_terms < fixed_terms, (block_terms, fixed_terms))

    block = block_intersection_transition(
        n,
        shadow_degree,
        block_terms,
        block_derivative_order,
    )
    projected_capacity = (
        (fixed_terms - block_terms) * comb(n, shadow_degree)
        + int(block["block_intersection_cap"])
    )

    outer = ExactIteratedProductShadow(n, complement_degree, 1)
    last_good, first_bad = outer.transition(projected_capacity)
    target, one_term, selected_bound = first_koszul_data(n, output_degree)
    global_bound = global_first_koszul_bound(n)
    require(fixed_terms <= global_bound, (fixed_terms, global_bound))

    residual_numerator = target - n * n * last_good.family_size
    require(residual_numerator > 0, residual_numerator)
    residual_terms = ceil_div(residual_numerator, one_term)
    total = fixed_terms + residual_terms

    return {
        **block,
        "output_degree": output_degree,
        "complement_degree": complement_degree,
        "shadow_degree": shadow_degree,
        "fixed_terms": fixed_terms,
        "projected_first_shadow_capacity": projected_capacity,
        "outer_intersection_cap": last_good.family_size,
        "outer_shadow_at_cap": last_good.shadow_size,
        "outer_first_excluded_size": first_bad.family_size,
        "outer_shadow_at_first_excluded_size": first_bad.shadow_size,
        "outer_cap_partition_count": last_good.partition_count,
        "outer_cap_partition": list(last_good.minimizing_partition),
        "outer_first_excluded_partition_count": first_bad.partition_count,
        "outer_first_excluded_partition": list(first_bad.minimizing_partition),
        "first_koszul_target_rank": target,
        "one_term_koszul_cap": one_term,
        "selected_output_first_koszul_bound": selected_bound,
        "global_first_koszul_bound": global_bound,
        "residual_rank_numerator": residual_numerator,
        "residual_terms": residual_terms,
        "two_level_lower_bound": total,
    }


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def build_payload() -> dict[str, object]:
    n7 = two_level_bound(7, 3, 19, 4, 1)
    require(n7["block_intersection_cap"] == 64, n7)
    require(n7["block_shadow_at_cap"] == 84, n7)
    require(n7["block_first_excluded_size"] == 65, n7)
    require(n7["block_shadow_at_first_excluded_size"] == 87, n7)
    require(n7["projected_first_shadow_capacity"] == 589, n7)
    require(n7["outer_intersection_cap"] == 341, n7)
    require(n7["outer_shadow_at_cap"] == 586, n7)
    require(n7["outer_first_excluded_size"] == 342, n7)
    require(n7["outer_shadow_at_first_excluded_size"] == 590, n7)
    require(n7["residual_rank_numerator"] == 42_091, n7)
    require(n7["residual_terms"] == 26, n7)
    require(n7["two_level_lower_bound"] == 45, n7)

    n8 = two_level_bound(8, 4, 17, 2, 2)
    require(n8["block_intersection_cap"] == 16, n8)
    require(n8["block_shadow_at_cap"] == 16, n8)
    require(n8["block_first_excluded_size"] == 17, n8)
    require(n8["block_shadow_at_first_excluded_size"] == 18, n8)
    require(n8["projected_first_shadow_capacity"] == 856, n8)
    require(n8["outer_intersection_cap"] == 625, n8)
    require(n8["outer_shadow_at_cap"] == 850, n8)
    require(n8["outer_first_excluded_size"] == 626, n8)
    require(n8["outer_shadow_at_first_excluded_size"] == 858, n8)
    require(n8["residual_rank_numerator"] == 270_464, n8)
    require(n8["residual_terms"] == 62, n8)
    require(n8["two_level_lower_bound"] == 79, n8)

    core = {
        "status": [
            "GENERAL_ITERATED_PRODUCT_SHADOW_PROOF_DRAFT",
            "BLOCK_INTERSECTION_PROJECTION_PROOF_DRAFT",
            "EXACT_INTEGER_REPLAYED",
            "PERM7_LOWER_45",
            "PERM8_LOWER_79",
        ],
        "theorem": {
            "iterated_shadow": (
                "For every derivative order a, arbitrary subspaces of "
                "D_m(perm_n) specialize and compress to Ferrers families; "
                "the exact objective uses weights binom(c_i,a)."
            ),
            "block_projection": (
                "A section of the literal summation map projected away from "
                "an s-term block has kernel bounded by the exact permanent-"
                "relative intersection cap of that block."
            ),
            "coupled_boundary": (
                "Only D_d(sum T_i) subset sum D_d(T_i) is used; no coupled "
                "image is identified with the literal sum."
            ),
        },
        "n7_application": n7,
        "n8_application": n8,
        "claim_boundary": (
            "These are ordinary characteristic-zero lower bounds. They do "
            "not determine perm_7 or perm_8 exactly, change the perm_6 "
            "status, prove a border-rank bound, or establish general Glynn "
            "optimality. Literature novelty is not claimed."
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
    print("GENERAL_ITERATED_PRODUCT_SHADOW_BLOCKS_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
