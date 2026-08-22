#!/usr/bin/env python3
"""Exact replay for the coordinate-initial regular first-order six-block zero theorem."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

N = 4
LABELS = 6
SOURCE_SUBSETS = tuple(combinations(range(LABELS), 4))
MATCHINGS = tuple(tuple(r * N + p[r] for r in range(N)) for p in permutations(range(N)))
MATCHING_SETS = tuple(frozenset(value) for value in MATCHINGS)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def envelope(frame: tuple[int, ...]) -> frozenset[int]:
    support = frozenset(frame)
    return frozenset(
        index
        for index, matching in enumerate(MATCHING_SETS)
        if len(support & matching) >= 3
    )


def source_monomial(frame: tuple[int, ...], subset: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(frame[label] for label in subset))


def direct_matchings(frame: tuple[int, ...]) -> frozenset[int]:
    image = {source_monomial(frame, subset) for subset in SOURCE_SUBSETS}
    return frozenset(
        index
        for index, matching in enumerate(MATCHINGS)
        if tuple(sorted(matching)) in image
    )


def kernel_relations(frame: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    fibers: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for index, subset in enumerate(SOURCE_SUBSETS):
        fibers[source_monomial(frame, subset)].append(index)
    relations: list[tuple[int, int]] = []
    for fiber in fibers.values():
        anchor = fiber[0]
        relations.extend((index, anchor) for index in fiber[1:])
    return tuple(relations)


def derivative_signature(
    frame: tuple[int, ...], source_index: int, matching: frozenset[int]
) -> Counter[tuple[int, int]]:
    result: Counter[tuple[int, int]] = Counter()
    subset = SOURCE_SUBSETS[source_index]
    for label in subset:
        others = [frame[other] for other in subset if other != label]
        if len(set(others)) != 3:
            continue
        other_set = frozenset(others)
        if not other_set < matching:
            continue
        missing = next(iter(matching - other_set))
        result[(label, missing)] += 1
    return result


def internal_kernel_matchings(frame: tuple[int, ...]) -> frozenset[int]:
    result: set[int] = set()
    for matching_index, matching in enumerate(MATCHING_SETS):
        for positive, negative in kernel_relations(frame):
            signature = derivative_signature(frame, positive, matching)
            signature.subtract(derivative_signature(frame, negative, matching))
            if any(signature.values()):
                result.add(matching_index)
                break
    return frozenset(result)


def private_matchings(frame: tuple[int, ...]) -> frozenset[int]:
    return direct_matchings(frame) | internal_kernel_matchings(frame)


def support_orbit_key(frame: tuple[int, ...]) -> tuple[int, ...]:
    support = frozenset(frame)
    candidates = []
    for row_perm in permutations(range(N)):
        for column_perm in permutations(range(N)):
            candidates.append(
                tuple(
                    sorted(
                        row_perm[cell // N] * N + column_perm[cell % N]
                        for cell in support
                    )
                )
            )
    return min(candidates)


def payload() -> dict[str, object]:
    frame_count = 0
    maximum_envelope = 0
    maximum_private = 0
    envelope_six_frames = 0
    envelope_six_private: Counter[int] = Counter()
    envelope_six_orbits: Counter[tuple[int, ...]] = Counter()
    two_direct_envelope_sizes: set[int] = set()

    for frame in combinations_with_replacement(range(N * N), LABELS):
        frame_count += 1
        frame_envelope = envelope(frame)
        direct = direct_matchings(frame)
        private = direct | internal_kernel_matchings(frame)
        require(private <= frame_envelope, (frame, private, frame_envelope))
        maximum_envelope = max(maximum_envelope, len(frame_envelope))
        maximum_private = max(maximum_private, len(private))

        if len(frame_envelope) == 6:
            envelope_six_frames += 1
            envelope_six_private[len(private)] += 1
            envelope_six_orbits[support_orbit_key(frame)] += 1
            require(len(set(frame)) == 6, frame)
            require(not direct, (frame, direct))
            require(not private, (frame, private))

        if len(direct) == 2:
            two_direct_envelope_sizes.add(len(frame_envelope))
            require(len(frame_envelope) == 2, (frame, direct, frame_envelope))

    require(frame_count == 54264, frame_count)
    require(maximum_envelope == 6, maximum_envelope)
    require(maximum_private == 2, maximum_private)
    require(envelope_six_frames == 288, envelope_six_frames)
    require(envelope_six_private == Counter({0: 288}), envelope_six_private)
    require(len(envelope_six_orbits) == 2, envelope_six_orbits)
    require(set(envelope_six_orbits.values()) == {144}, envelope_six_orbits)
    require(two_direct_envelope_sizes == {2}, two_direct_envelope_sizes)

    incidence_cap = 6 * maximum_envelope
    private_union_cap = 6 * maximum_private
    incidence_floor = 2 * len(MATCHINGS) - private_union_cap
    require(incidence_cap == incidence_floor == 36, (incidence_cap, incidence_floor))

    return {
        "schema": "general_quartic_coordinate_regular_first_order_zero/v1",
        "theorem_id": "coordinate-regular-first-order-six-block-zero-v1",
        "field": "characteristic_zero",
        "coordinate_multiset_frames_checked": frame_count,
        "source_dimension_per_component": len(SOURCE_SUBSETS),
        "perfect_matchings": len(MATCHINGS),
        "maximum_first_order_matching_envelope": maximum_envelope,
        "maximum_private_matching_capacity": maximum_private,
        "envelope_six_frames": envelope_six_frames,
        "envelope_six_row_column_orbits": len(envelope_six_orbits),
        "envelope_six_private_histogram": {
            str(key): envelope_six_private[key] for key in sorted(envelope_six_private)
        },
        "two_direct_envelope_sizes": sorted(two_direct_envelope_sizes),
        "global_incidence": {
            "six_component_incidence_cap": incidence_cap,
            "six_component_private_union_cap": private_union_cap,
            "target_incidence_floor": incidence_floor,
            "frames_with_envelope_6_and_private_2": 0,
            "coordinate_regular_first_order_six_block_witness": "IMPOSSIBLE",
        },
        "claim_boundary": {
            "coordinate_initial_regular_first_order_six_block": "ZERO",
            "coordinate_initial_higher_order": "OPEN",
            "noncoordinate_initial": "OPEN",
            "singular_or_puiseux": "OPEN",
            "mu_6_4_exact": "OPEN_IN_[6,8]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = payload()
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("GENERAL_QUARTIC_COORDINATE_REGULAR_FIRST_ORDER_ZERO_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
