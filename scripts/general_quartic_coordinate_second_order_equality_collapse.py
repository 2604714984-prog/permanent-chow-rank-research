#!/usr/bin/env python3
"""Exact finite replay for the coordinate second-order equality-state collapse."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

ORDER = 4
MATCHINGS = tuple(
    frozenset(row * ORDER + permutation[row] for row in range(ORDER))
    for permutation in permutations(range(ORDER))
)
LABEL_SUBSETS = tuple(combinations(range(6), 4))
MOVE_SETS = tuple(
    move
    for size in (1, 2)
    for move in combinations(range(6), size)
)
ALL_MATCHINGS_MASK = (1 << len(MATCHINGS)) - 1
EXPECTED_CORE = "938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def containment_mask(cells: tuple[int, ...], cache: dict[tuple[int, ...], int]) -> int:
    if len(set(cells)) != len(cells):
        return 0
    key = tuple(sorted(cells))
    if key not in cache:
        mask = 0
        support = frozenset(key)
        for index, matching in enumerate(MATCHINGS):
            if support <= matching:
                mask |= 1 << index
        cache[key] = mask
    return cache[key]


def local_masks(
    gamma: tuple[int, ...],
    support_cache: dict[frozenset[int], tuple[int, int]],
    containment_cache: dict[tuple[int, ...], int],
) -> tuple[int, int, int, int]:
    support = frozenset(gamma)
    if support not in support_cache:
        envelope = direct = 0
        for index, matching in enumerate(MATCHINGS):
            intersection = len(support & matching)
            if intersection >= 2:
                envelope |= 1 << index
            if matching <= support:
                direct |= 1 << index
        support_cache[support] = (envelope, direct)
    envelope, direct = support_cache[support]

    fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for subset in LABEL_SUBSETS:
        fibers[tuple(sorted(gamma[label] for label in subset))].append(subset)

    internal = 0
    for fiber in fibers.values():
        if len(fiber) < 2:
            continue
        fiber_sets = [set(subset) for subset in fiber]
        for move in MOVE_SETS:
            move_set = set(move)
            masks = []
            for subset, subset_set in zip(fiber, fiber_sets, strict=True):
                if not move_set <= subset_set:
                    masks.append(0)
                    continue
                unchanged = tuple(gamma[label] for label in subset if label not in move_set)
                masks.append(containment_mask(unchanged, containment_cache))
            union = 0
            intersection = ALL_MATCHINGS_MASK
            for mask in masks:
                union |= mask
                intersection &= mask
            internal |= union & ~intersection & ALL_MATCHINGS_MASK
    return envelope, direct, internal, direct | internal


def row_column_key(gamma: tuple[int, ...]) -> tuple[int, ...]:
    candidates = []
    for row_permutation in permutations(range(ORDER)):
        for column_permutation in permutations(range(ORDER)):
            candidates.append(
                tuple(
                    sorted(
                        row_permutation[cell // ORDER] * ORDER
                        + column_permutation[cell % ORDER]
                        for cell in gamma
                    )
                )
            )
    return min(candidates)


def degree_sequences(gamma: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rows = [0] * ORDER
    columns = [0] * ORDER
    for cell in set(gamma):
        rows[cell // ORDER] += 1
        columns[cell % ORDER] += 1
    return tuple(sorted(rows, reverse=True)), tuple(sorted(columns, reverse=True))


def build_core() -> dict[str, object]:
    support_cache: dict[frozenset[int], tuple[int, int]] = {}
    containment_cache: dict[tuple[int, ...], int] = {}
    profile_histogram: Counter[tuple[int, int, int, int]] = Counter()
    maximum = -1
    equality = []
    checked = 0

    for gamma in combinations_with_replacement(range(ORDER * ORDER), 6):
        envelope, direct, internal, unshared = local_masks(
            gamma, support_cache, containment_cache
        )
        profile = (
            envelope.bit_count(),
            direct.bit_count(),
            internal.bit_count(),
            unshared.bit_count(),
        )
        profile_histogram[profile] += 1
        value = profile[0] + profile[3]
        if value > maximum:
            maximum = value
            equality = [gamma]
        elif value == maximum:
            equality.append(gamma)
        checked += 1

    require(checked == 54264, checked)
    require(maximum == 20, maximum)
    require(len(profile_histogram) == 27, len(profile_histogram))
    require(len(equality) == 288, len(equality))
    require(
        all(
            local_masks(gamma, support_cache, containment_cache)[0].bit_count() == 12
            and local_masks(gamma, support_cache, containment_cache)[1].bit_count() == 0
            and local_masks(gamma, support_cache, containment_cache)[2].bit_count() == 8
            for gamma in equality
        ),
        "equality profile",
    )
    require(all(len(set(gamma)) == 5 for gamma in equality), "five distinct cells")
    require(
        all(sorted(Counter(gamma).values(), reverse=True) == [2, 1, 1, 1, 1] for gamma in equality),
        "multiplicity pattern",
    )

    first_order_zero = []
    for gamma in equality:
        support = set(gamma)
        count = sum(len(support & matching) >= 3 for matching in MATCHINGS)
        first_order_zero.append(count)
    require(set(first_order_zero) == {0}, set(first_order_zero))

    orbit_histogram = Counter(row_column_key(gamma) for gamma in equality)
    require(len(orbit_histogram) == 2, orbit_histogram)
    require(sorted(orbit_histogram.values()) == [144, 144], orbit_histogram)
    representatives = sorted(orbit_histogram)
    require(
        [degree_sequences(value) for value in representatives]
        == [
            ((3, 1, 1, 0), (2, 1, 1, 1)),
            ((2, 1, 1, 1), (3, 1, 1, 0)),
        ],
        representatives,
    )

    return {
        "schema": "general_quartic_coordinate_second_order_equality_collapse/v1",
        "classification": "ROUTE_DIAGNOSTIC_AND_EQUALITY_STATE_LEMMA",
        "field": "characteristic_zero",
        "local_over_envelope": {
            "unordered_coordinate_frames_checked": checked,
            "profile_count": len(profile_histogram),
            "maximum_E2_plus_S2_tilde": maximum,
            "equality_frames": len(equality),
            "equality_row_column_orbits": len(orbit_histogram),
            "equality_orbit_sizes": sorted(orbit_histogram.values()),
            "equality_profile": {"E2": 12, "D": 0, "K2_tilde": 8, "S2_tilde": 8},
            "representatives": [list(value) for value in representatives],
        },
        "equality_structure": {
            "distinct_cells": 5,
            "multiplicity_pattern": [2, 1, 1, 1, 1],
            "E1_matching_support": 0,
            "representative_degree_sequences": [
                {"row": [3, 1, 1, 0], "column": [2, 1, 1, 1]},
                {"row": [2, 1, 1, 1], "column": [3, 1, 1, 0]},
            ],
        },
        "integrability_lemma": {
            "statement": "For every equality frame, if one component has g0=0 and g1=0 internally, then the perfect-matching projection of g2 is zero.",
            "kernel_form": "(l0-l1) H with H in span of the four triple products of the other four distinct factors",
            "first_order_condition": "delta*H lies in the coordinate source image",
            "matching_consequence": "Every second-order matching would retain at least three distinct frame cells; equality frames have E1=empty.",
        },
        "claim_boundary": {
            "single_component_internal_two_jet_on_equality_frames": "MATCHING_ZERO",
            "global_six_component_second_order": "OPEN",
            "coordinate_second_order_over_envelope": "DIAGNOSTIC_ONLY",
            "mu_6_4": "OPEN_IN_[6,8]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    core = build_core()
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    require(digest == EXPECTED_CORE, digest)
    payload = dict(core)
    payload["core_sha256"] = digest
    if arguments.json is not None:
        arguments.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("GENERAL_QUARTIC_COORDINATE_SECOND_ORDER_EQUALITY_COLLAPSE_PASS")
    print(digest)


if __name__ == "__main__":
    main()
