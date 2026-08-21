#!/usr/bin/env python3
"""Exact local replay for coordinate regular first-order six-block closure."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

ORDER = 4
FACTOR_COUNT = 6
CELLS = tuple(range(ORDER * ORDER))
LABEL_SUBSETS = tuple(combinations(range(FACTOR_COUNT), 4))
PERMUTATIONS = tuple(permutations(range(ORDER)))
MATCHINGS = tuple(
    frozenset(row * ORDER + permutation[row] for row in range(ORDER))
    for permutation in PERMUTATIONS
)
MATCHING_INDEX = {matching: index for index, matching in enumerate(MATCHINGS)}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def envelope(support: frozenset[int]) -> frozenset[int]:
    return frozenset(
        index
        for index, matching in enumerate(MATCHINGS)
        if len(matching & support) >= 3
    )


def direct(support: frozenset[int]) -> frozenset[int]:
    return frozenset(
        index for index, matching in enumerate(MATCHINGS) if matching <= support
    )


def complete_three_matching(cells: tuple[int, int, int]) -> int | None:
    if len(set(cells)) != 3:
        return None
    rows = {cell // ORDER for cell in cells}
    columns = {cell % ORDER for cell in cells}
    if len(rows) != 3 or len(columns) != 3:
        return None
    missing_row = next(iter(set(range(ORDER)) - rows))
    missing_column = next(iter(set(range(ORDER)) - columns))
    target = frozenset(cells) | {missing_row * ORDER + missing_column}
    return MATCHING_INDEX.get(target)


def vertical_non_direct_primary(frame: tuple[int, ...]) -> frozenset[int]:
    """Reachable non-direct matchings from the specialized source-map kernel."""

    direct_set = direct(frozenset(frame))
    groups: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for subset in LABEL_SUBSETS:
        groups[tuple(sorted(frame[label] for label in subset))].append(subset)

    reachable: set[int] = set()
    for fiber in groups.values():
        if len(fiber) < 2:
            continue
        for moving_label in range(FACTOR_COUNT):
            membership = [moving_label in subset for subset in fiber]
            if not any(membership) or all(membership):
                continue
            for subset in fiber:
                if moving_label not in subset:
                    continue
                remaining = tuple(
                    frame[label] for label in subset if label != moving_label
                )
                matching_index = complete_three_matching(remaining)
                if matching_index is not None and matching_index not in direct_set:
                    reachable.add(matching_index)
    return frozenset(reachable)


def audit_supports() -> dict[str, object]:
    checked = 0
    maximum_by_size: dict[int, int] = defaultdict(int)
    two_direct_supports = 0

    for size in range(FACTOR_COUNT + 1):
        for values in combinations(CELLS, size):
            support = frozenset(values)
            checked += 1
            e = len(envelope(support))
            p = len(direct(support))
            maximum_by_size[size] = max(maximum_by_size[size], e)

            require(p <= 2, (support, p))
            if size <= 4:
                require(e <= 2, (support, e))
            elif size == 5:
                require(e <= 4, (support, e))
                if p:
                    require(p == 1 and e == 2, (support, p, e))
            elif size == 6:
                require(e <= 6, (support, e))
                if p == 1:
                    require(e <= 4, (support, p, e))
                elif p == 2:
                    require(e == 2, (support, p, e))
                    two_direct_supports += 1

    require(checked == 14893, checked)
    require(
        {size: maximum_by_size[size] for size in range(7)}
        == {0: 0, 1: 0, 2: 0, 3: 1, 4: 2, 5: 4, 6: 6},
        maximum_by_size,
    )
    require(two_direct_supports == 72, two_direct_supports)
    return {
        "supports_checked": checked,
        "maximum_envelope_by_support_size": {
            str(size): maximum_by_size[size] for size in range(7)
        },
        "two_direct_six_cell_supports": two_direct_supports,
        "support_refinements_verified": True,
    }


def audit_frames() -> dict[str, object]:
    checked = 0
    maximum_vertical = 0
    maximum_score = 0

    for frame in combinations_with_replacement(CELLS, FACTOR_COUNT):
        checked += 1
        support = frozenset(frame)
        e_set = envelope(support)
        p_set = direct(support)
        v_set = vertical_non_direct_primary(frame)
        require(v_set <= e_set - p_set, (frame, e_set, p_set, v_set))

        e, p, v = len(e_set), len(p_set), len(v_set)
        score = e + p + v
        maximum_vertical = max(maximum_vertical, v)
        maximum_score = max(maximum_score, score)
        require(score <= 6, (frame, e, p, v, score))

        distinct = len(support)
        if distinct == 6:
            require(v == 0, (frame, v_set))
        elif distinct == 5:
            require(v <= 2, (frame, v_set))
        else:
            require(e <= 2, (frame, e_set))

    require(checked == 54264, checked)
    require(maximum_vertical == 2, maximum_vertical)
    require(maximum_score == 6, maximum_score)
    return {
        "coordinate_multisets_checked": checked,
        "maximum_vertical_non_direct_support": maximum_vertical,
        "maximum_local_score_e_plus_p_plus_v": maximum_score,
    }


def payload() -> dict[str, object]:
    return {
        "schema": "general_quartic_coordinate_first_order_closure/v1",
        "field": "characteristic_zero",
        "coordinate_order": ORDER,
        "component_count": FACTOR_COUNT,
        "target_matching_count": len(MATCHINGS),
        "support_audit": audit_supports(),
        "frame_audit": audit_frames(),
        "global_incidence": {
            "target_count": 24,
            "degree_one_direct_or_vertical": True,
            "minimum_required_sum_e_plus_p_plus_v": 48,
            "maximum_available_sum_e_plus_p_plus_v": 36,
            "contradiction_margin": 12,
        },
        "conclusion": {
            "coordinate_regular_first_order_six_block_lift": "IMPOSSIBLE",
            "mu_6_4_exact_value": "OPEN_IN_[6,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
            "noncoordinate_singular_or_higher_order_lifts": "OPEN",
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print("GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_CLOSURE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
