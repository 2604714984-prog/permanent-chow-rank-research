#!/usr/bin/env python3
"""Audit the nonuniform degree-shifted matrix-image route ceiling.

For a degree-zero graded binary matrix

    Phi: direct_sum_a R(-a)^(q_a) -> direct_sum_b R(-b)^(p_b),

split Phi into shift blocks Phi_(b,a).  Each block has one common entry
degree a-b and is therefore covered by the homogeneous-matrix theorem.  The
full image is contained in the sum of block images, while the one-term Boolean
envelope of the full map dominates the envelope of every individual block.

The resulting route ceiling is at most

    binom(n,floor(n/2)) * sum_(active blocks) p_b*q_a
    <= p*q*binom(n,floor(n/2)).

This is a ceiling for a named lower-bound mechanism, not an upper bound on
actual Chow rank.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from itertools import combinations
from math import comb
from pathlib import Path


EXPECTED_CORE_SHA256 = "8402c0aefdd9c2bde28e7b2ec631f78faaf1ac35c7f0387801e6fe7d51dc8601"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def level(n: int, degree: int) -> int:
    return comb(n, degree) if 0 <= degree <= n else 0


def positive_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    result = []
    for parts in range(1, total + 1):
        for cuts in combinations(range(1, total), parts - 1):
            values = []
            previous = 0
            for cut in (*cuts, total):
                values.append(cut - previous)
                previous = cut
            result.append(tuple(values))
    return tuple(result)


@dataclass(frozen=True)
class ShiftBlock:
    source_shift: int
    target_shift: int
    source_multiplicity: int
    target_multiplicity: int
    normal_rank: int

    @property
    def degree(self) -> int:
        return self.source_shift - self.target_shift


def block_bounds(n: int, d: int, block: ShiftBlock) -> dict[str, int]:
    source_level = level(n, d - block.source_shift)
    target_level = level(n, d - block.target_shift)
    require(block.degree >= 0, block)
    require(
        1
        <= block.normal_rank
        <= min(block.source_multiplicity, block.target_multiplicity),
        block,
    )

    if source_level == 0 or target_level == 0:
        return {
            "source_level": source_level,
            "target_level": target_level,
            "boolean_lower": 0,
            "permanent_upper": 0,
            "route_ceiling": 0,
            "central_block_ceiling": 0,
        }

    boolean_lower = block.normal_rank * min(source_level, target_level)
    permanent_upper = min(
        block.source_multiplicity * source_level**2,
        block.target_multiplicity * target_level**2,
    )
    route_ceiling = ceil_div(permanent_upper, boolean_lower)
    central = comb(n, n // 2)
    central_block_ceiling = (
        block.source_multiplicity * block.target_multiplicity * central
    )
    require(
        route_ceiling <= central_block_ceiling,
        (n, d, block, route_ceiling, central_block_ceiling),
    )
    return {
        "source_level": source_level,
        "target_level": target_level,
        "boolean_lower": boolean_lower,
        "permanent_upper": permanent_upper,
        "route_ceiling": route_ceiling,
        "central_block_ceiling": central_block_ceiling,
    }


def full_route_bounds(
    n: int,
    d: int,
    source_groups: tuple[int, ...],
    target_groups: tuple[int, ...],
    blocks: tuple[ShiftBlock, ...],
) -> dict[str, int]:
    central = comb(n, n // 2)
    active = []
    block_ceiling_sum = 0
    support_area = 0
    max_boolean_lower = 0
    sum_block_permanent_upper = 0

    for block in blocks:
        values = block_bounds(n, d, block)
        if values["boolean_lower"] == 0:
            continue
        active.append(block)
        block_ceiling_sum += values["route_ceiling"]
        support_area += block.source_multiplicity * block.target_multiplicity
        max_boolean_lower = max(max_boolean_lower, values["boolean_lower"])
        sum_block_permanent_upper += values["permanent_upper"]

    p = sum(target_groups)
    q = sum(source_groups)
    require(
        support_area <= p * q,
        (source_groups, target_groups, support_area, p * q),
    )
    require(
        block_ceiling_sum <= support_area * central,
        (n, d, block_ceiling_sum, support_area, central),
    )

    if not active:
        full_source_upper = 0
        full_target_upper = 0
        direct_ratio_ceiling = 0
    else:
        source_shifts = sorted(set(block.source_shift for block in active))
        target_shifts = sorted(set(block.target_shift for block in active))
        source_mult = {shift: source_groups[shift] for shift in source_shifts}
        target_mult = {shift: target_groups[shift] for shift in target_shifts}
        full_source_upper = sum(
            source_mult[shift] * level(n, d - shift) ** 2
            for shift in source_shifts
        )
        full_target_upper = sum(
            target_mult[shift] * level(n, d - shift) ** 2
            for shift in target_shifts
        )
        full_perm_upper = min(
            full_source_upper,
            full_target_upper,
            sum_block_permanent_upper,
        )
        direct_ratio_ceiling = ceil_div(full_perm_upper, max_boolean_lower)
        require(
            direct_ratio_ceiling <= block_ceiling_sum,
            (
                n,
                d,
                source_groups,
                target_groups,
                direct_ratio_ceiling,
                block_ceiling_sum,
            ),
        )

    return {
        "p": p,
        "q": q,
        "active_block_count": len(active),
        "support_area": support_area,
        "block_ceiling_sum": block_ceiling_sum,
        "coarse_pq_ceiling": p * q * central,
        "direct_ratio_ceiling": direct_ratio_ceiling,
        "full_source_upper": full_source_upper,
        "full_target_upper": full_target_upper,
    }


def canonical_blocks(
    source_groups: tuple[int, ...],
    target_groups: tuple[int, ...],
    selector: int,
) -> tuple[ShiftBlock, ...]:
    candidates = []
    for source_shift, source_multiplicity in enumerate(source_groups):
        for target_shift, target_multiplicity in enumerate(target_groups):
            if source_shift < target_shift:
                continue
            index = len(candidates)
            if (selector >> index) & 1:
                rank = 1 + (
                    (source_shift + 2 * target_shift + selector)
                    % min(source_multiplicity, target_multiplicity)
                )
                candidates.append(
                    ShiftBlock(
                        source_shift,
                        target_shift,
                        source_multiplicity,
                        target_multiplicity,
                        rank,
                    )
                )
            else:
                candidates.append(None)
    return tuple(block for block in candidates if block is not None)


def build_payload() -> dict[str, object]:
    pattern_checks = 0
    degree_checks = 0
    block_checks = 0
    maximum_support_ratio_num = 0
    maximum_support_ratio_den = 1
    examples = []

    for q in range(1, 5):
        for p in range(1, 5):
            for source_groups in positive_compositions(q):
                for target_groups in positive_compositions(p):
                    candidate_count = sum(
                        source_shift >= target_shift
                        for source_shift in range(len(source_groups))
                        for target_shift in range(len(target_groups))
                    )
                    for selector in range(1, 1 << candidate_count):
                        blocks = canonical_blocks(
                            source_groups,
                            target_groups,
                            selector,
                        )
                        if not blocks:
                            continue
                        pattern_checks += 1
                        support_area = sum(
                            block.source_multiplicity
                            * block.target_multiplicity
                            for block in blocks
                        )
                        require(
                            support_area <= p * q,
                            (
                                p,
                                q,
                                source_groups,
                                target_groups,
                                blocks,
                            ),
                        )
                        if (
                            support_area * maximum_support_ratio_den
                            > maximum_support_ratio_num * p * q
                        ):
                            maximum_support_ratio_num = support_area
                            maximum_support_ratio_den = p * q

                        for n in range(3, 10):
                            for d in range(
                                0,
                                n
                                + max(
                                    len(source_groups),
                                    len(target_groups),
                                ),
                            ):
                                result = full_route_bounds(
                                    n,
                                    d,
                                    source_groups,
                                    target_groups,
                                    blocks,
                                )
                                degree_checks += 1
                                block_checks += result["active_block_count"]
                                if (
                                    len(examples) < 12
                                    and result["active_block_count"] >= 2
                                    and result["direct_ratio_ceiling"] > 0
                                ):
                                    examples.append(
                                        {
                                            "n": n,
                                            "d": d,
                                            "source_groups": list(source_groups),
                                            "target_groups": list(target_groups),
                                            "active_blocks": result[
                                                "active_block_count"
                                            ],
                                            "support_area": result["support_area"],
                                            "direct_ratio_ceiling": result[
                                                "direct_ratio_ceiling"
                                            ],
                                            "block_ceiling_sum": result[
                                                "block_ceiling_sum"
                                            ],
                                            "coarse_pq_ceiling": result[
                                                "coarse_pq_ceiling"
                                            ],
                                        }
                                    )

    require(
        maximum_support_ratio_num == maximum_support_ratio_den,
        (maximum_support_ratio_num, maximum_support_ratio_den),
    )

    complexity_thresholds = []
    for n in range(3, 65):
        central = comb(n, n // 2)
        glynn = 2 ** (n - 1)
        minimum_square_size = 1
        while minimum_square_size**2 * central < glynn:
            minimum_square_size += 1
        complexity_thresholds.append(
            {
                "n": n,
                "central_binomial": central,
                "glynn": glynn,
                "minimum_K_from_coarse_bound": minimum_square_size,
            }
        )

    core: dict[str, object] = {
        "status": [
            "GENERAL_NONUNIFORM_SHIFT_BLOCK_DECOMPOSITION",
            "GENERAL_GRADED_MATRIX_IMAGE_CEILING",
            "N_QUARTER_MATRIX_SIZE_NECESSITY",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "graded_map": (
                "Phi: direct_sum_a R(-a)^(q_a) -> "
                "direct_sum_b R(-b)^(p_b), with block Phi_(b,a) "
                "in Mat_(p_b x q_a)(R_(a-b))."
            ),
            "block_envelope": (
                "The full permanent image is contained in the sum of "
                "shift-block images, while the full Boolean term envelope "
                "dominates every block envelope."
            ),
            "exact_block_sum": (
                "R_(Phi,n,d) <= sum_(active b,a) ceil(U_(b,a)/L_(b,a)), "
                "where U=min(q_a H_s^2,p_b H_t^2) and "
                "L=r_(b,a) min(H_s,H_t)."
            ),
            "support_area_ceiling": (
                "R_(Phi,n,d) <= omega_d(Phi)*binom(n,floor(n/2)), "
                "omega_d=sum_(active b,a) p_b q_a <= p q."
            ),
            "matrix_size_necessity": (
                "If p,q<=K_n, then the route proves at most "
                "K_n^2*binom(n,floor(n/2)); reaching Glynn requires "
                "K_n >= (1+o(1))*(pi*n/8)^(1/4)."
            ),
        },
        "finite_replay": {
            "pattern_checks": pattern_checks,
            "degree_checks": degree_checks,
            "active_block_checks": block_checks,
            "maximum_support_area_ratio": [
                maximum_support_ratio_num,
                maximum_support_ratio_den,
            ],
            "examples": examples,
            "complexity_thresholds": complexity_thresholds,
        },
        "claim_boundary": (
            "The theorem closes every bounded-size degree-zero graded "
            "matrix-image route over a binary differential plane, including "
            "arbitrary nonuniform shifts. It is a ceiling on one matrix-image "
            "rank invariant, not an upper bound on actual Chow rank. It does "
            "not cover joint Fitting/minor profiles, kernel or Betti data "
            "without monotonicity, higher syzygy modules, "
            "representation-valued invariants, matrix families whose total "
            "support area is large enough, Chow-realizability defects, "
            "border rank, or exact rank for n>=6. Literature novelty is not "
            "established."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(
        payload["core_sha256"] == EXPECTED_CORE_SHA256,
        payload["core_sha256"],
    )
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
    print("GENERAL_NONUNIFORM_SHIFTED_MATRIX_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
