#!/usr/bin/env python3
"""Exact finite replay for the selected perm_8 q=17 coordinate equality locus.

The converse theorem is proved in
`docs/general_product_shadow_n8_q17_coordinate_equality.md`.  This script
rebuilds every finite incidence interface used there and verifies full
representative shadows for the three orbit types.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


GROUND = tuple(range(8))
FOURS = tuple(combinations(GROUND, 4))
THREES = tuple(combinations(GROUND, 3))
FOUR_INDEX = {value: index for index, value in enumerate(FOURS)}
THREE_INDEX = {value: index for index, value in enumerate(THREES)}
ROW_COUNT = len(FOURS)
LOWER_COUNT = len(THREES)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def shadow(family: frozenset[tuple[int, ...]]) -> frozenset[tuple[int, ...]]:
    return frozenset(
        lower
        for value in family
        for lower in combinations(value, 3)
    )


def complete_family(vertices: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    return frozenset(combinations(vertices, 4))


def extremal_45(z: int, five: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    complement = tuple(sorted(set(GROUND) - {z}))
    return frozenset(
        list(combinations(complement, 4))
        + [tuple(sorted((z,) + triple)) for triple in combinations(five, 3)]
    )


def extremal_55(z: int, six: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    complement = tuple(sorted(set(GROUND) - {z}))
    return frozenset(
        list(combinations(complement, 4))
        + [tuple(sorted((z,) + triple)) for triple in combinations(six, 3)]
    )


def extremal_25(
    five: tuple[int, ...],
    a: int,
    b: int,
) -> frozenset[tuple[int, ...]]:
    return frozenset(
        list(combinations(five, 4))
        + [tuple(sorted((a,) + triple)) for triple in combinations(five, 3)]
        + [tuple(sorted((b,) + triple)) for triple in combinations(five, 3)]
    )


def connected_component_sizes(
    nodes: frozenset[tuple[int, ...]],
    lower_labels: frozenset[tuple[int, ...]],
) -> tuple[int, ...]:
    adjacency = {node: set() for node in nodes}
    for lower in lower_labels:
        containing = [node for node in nodes if set(lower).issubset(node)]
        for left in containing:
            adjacency[left].update(right for right in containing if right != left)

    unseen = set(nodes)
    sizes: list[int] = []
    while unseen:
        root = unseen.pop()
        component = {root}
        stack = [root]
        while stack:
            current = stack.pop()
            for neighbour in adjacency[current]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    stack.append(neighbour)
        sizes.append(len(component))
    return tuple(sorted(sizes, reverse=True))


def lower_indices(four_set: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        THREE_INDEX[four_set[:position] + four_set[position + 1 :]]
        for position in range(4)
    )


LOWER_INDICES = tuple(lower_indices(value) for value in FOURS)
PAIR_SHADOW = tuple(
    tuple(
        sum(
            1 << (row_lower * LOWER_COUNT + column_lower)
            for row_lower in LOWER_INDICES[row]
            for column_lower in LOWER_INDICES[column]
        )
        for column in range(ROW_COUNT)
    )
    for row in range(ROW_COUNT)
)


def product_family(
    strata: tuple[
        tuple[
            frozenset[tuple[int, ...]],
            frozenset[tuple[int, ...]],
        ],
        ...,
    ],
) -> int:
    family = 0
    for rows, columns in strata:
        for row in rows:
            row_index = FOUR_INDEX[row]
            for column in columns:
                column_index = FOUR_INDEX[column]
                family |= 1 << (row_index * ROW_COUNT + column_index)
    return family


def product_shadow(family: int) -> int:
    output = 0
    remaining = family
    while remaining:
        least = remaining & -remaining
        position = least.bit_length() - 1
        row, column = divmod(position, ROW_COUNT)
        output |= PAIR_SHADOW[row][column]
        remaining ^= least
    return output


def row_profile(family: int) -> tuple[int, ...]:
    row_mask = (1 << ROW_COUNT) - 1
    return tuple(
        sorted(
            (
                ((family >> (row * ROW_COUNT)) & row_mask).bit_count()
                for row in range(ROW_COUNT)
            ),
            reverse=True,
        )
    )


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def enumerate_profile_a_rows() -> tuple[list[dict[str, object]], dict[str, int]]:
    families_45: list[tuple[int, tuple[int, ...], frozenset[tuple[int, ...]]]] = []
    for z in GROUND:
        available = tuple(sorted(set(GROUND) - {z}))
        for five in combinations(available, 5):
            family = extremal_45(z, five)
            require((len(family), len(shadow(family))) == (45, 45), (z, five))
            families_45.append((z, five, family))

    families_55: list[tuple[int, tuple[int, ...], frozenset[tuple[int, ...]]]] = []
    for z in GROUND:
        available = tuple(sorted(set(GROUND) - {z}))
        for six in combinations(available, 6):
            family = extremal_55(z, six)
            require((len(family), len(shadow(family))) == (55, 50), (z, six))
            families_55.append((z, six, family))

    require(len({family for _, _, family in families_45}) == 168, "45 duplicates")
    require(len({family for _, _, family in families_55}) == 56, "55 duplicates")

    records: list[dict[str, object]] = []
    type_counts: Counter[str] = Counter()
    connectivity_counts: Counter[tuple[object, ...]] = Counter()

    for z45, five, high in families_45:
        residue = set(GROUND) - {z45} - set(five)
        require(len(residue) == 2, residue)
        for z55, six, medium in families_55:
            if not high.issubset(medium):
                continue
            if z55 == z45:
                route = "A1_common_apex"
                require(set(six) == set(five) | (residue & set(six)), (five, six))
                require(len(set(six) - set(five)) == 1, (five, six))
            else:
                route = "A2_exchanged_apex"
                require(z55 in residue, (z45, z55, residue))
                require(set(six) == set(five) | (residue - {z55}), (five, six))

            difference = medium - high
            high_shadow = shadow(high)
            medium_shadow = shadow(medium)
            new_shadow = medium_shadow - high_shadow
            high_components = connected_component_sizes(high, high_shadow)
            difference_components = connected_component_sizes(
                frozenset(difference),
                frozenset(new_shadow),
            )
            cross_minimum = min(
                sum(1 for lower in high_shadow if set(lower).issubset(row))
                for row in difference
            )
            require(high_components == (45,), high_components)
            require(difference_components == (10,), difference_components)
            require(cross_minimum >= 1, cross_minimum)

            type_counts[route] += 1
            connectivity_counts[
                (route, high_components, difference_components, cross_minimum)
            ] += 1
            records.append(
                {
                    "route": route,
                    "z45": z45,
                    "five": list(five),
                    "z55": z55,
                    "six": list(six),
                }
            )

    require(len(records) == 672, len(records))
    require(type_counts == {"A1_common_apex": 336, "A2_exchanged_apex": 336}, type_counts)
    return records, {
        "extremal_45_family_count": 168,
        "extremal_55_family_count": 56,
        "nested_pair_count": 672,
        "A1_common_apex_count": 336,
        "A2_exchanged_apex_count": 336,
        "connectivity_signature_count": len(connectivity_counts),
    }


def enumerate_profile_b_rows() -> dict[str, int]:
    count = 0
    signature_counts: Counter[tuple[object, ...]] = Counter()
    for seven in combinations(GROUND, 7):
        for six in combinations(seven, 6):
            for five in combinations(six, 5):
                count += 1
                high = complete_family(five)
                medium = complete_family(six)
                low = complete_family(seven)
                medium_difference = medium - high
                low_difference = low - medium
                high_shadow = shadow(high)
                medium_shadow = shadow(medium)
                low_shadow = shadow(low)
                medium_new = medium_shadow - high_shadow
                low_new = low_shadow - medium_shadow

                signature = (
                    connected_component_sizes(high, high_shadow),
                    connected_component_sizes(
                        frozenset(medium_difference),
                        frozenset(medium_new),
                    ),
                    connected_component_sizes(
                        frozenset(low_difference),
                        frozenset(low_new),
                    ),
                    min(
                        sum(1 for lower in high_shadow if set(lower).issubset(row))
                        for row in medium_difference
                    ),
                    min(
                        sum(1 for lower in medium_shadow if set(lower).issubset(row))
                        for row in low_difference
                    ),
                )
                require(signature == ((5,), (10,), (20,), 1, 1), signature)
                signature_counts[signature] += 1

    require(count == 336, count)
    return {
        "row_flag_count": count,
        "connectivity_signature_count": len(signature_counts),
    }


def enumerate_column_structures() -> dict[str, int]:
    profile_a_flags = {
        (six, five)
        for six in combinations(GROUND, 6)
        for five in combinations(six, 5)
    }
    require(len(profile_a_flags) == 168, len(profile_a_flags))

    profile_b_structures: set[
        tuple[
            frozenset[tuple[int, ...]],
            frozenset[tuple[int, ...]],
            frozenset[tuple[int, ...]],
        ]
    ] = set()
    for seven in combinations(GROUND, 7):
        for five in combinations(seven, 5):
            endpoints = tuple(sorted(set(seven) - set(five)))
            require(len(endpoints) == 2, endpoints)
            a, b = endpoints
            family_35 = complete_family(seven)
            family_25 = extremal_25(five, a, b)
            require((len(family_25), len(shadow(family_25))) == (25, 30), (seven, five))
            require(shadow(family_25).issubset(shadow(family_35)), (seven, five))
            for endpoint in endpoints:
                family_15 = complete_family(
                    tuple(sorted(set(five) | {endpoint}))
                )
                require(len(family_15) == 15, family_15)
                require(shadow(family_15).issubset(shadow(family_25)), (seven, five, endpoint))
                profile_b_structures.add((family_35, family_25, family_15))

    require(len(profile_b_structures) == 336, len(profile_b_structures))
    return {
        "profile_A_column_flag_count": 168,
        "profile_B_column_biflag_count": 336,
    }


def representative_families() -> dict[str, object]:
    high_same = extremal_45(0, (1, 2, 3, 4, 5))
    medium_same = extremal_55(0, (1, 2, 3, 4, 5, 6))
    high_swapped = high_same
    medium_swapped = extremal_55(6, (1, 2, 3, 4, 5, 7))

    column_15 = complete_family((0, 1, 2, 3, 4, 5))
    column_5 = complete_family((0, 1, 2, 3, 4))

    family_a1 = product_family(
        (
            (high_same, column_15),
            (frozenset(medium_same - high_same), column_5),
        )
    )
    family_a2 = product_family(
        (
            (high_swapped, column_15),
            (frozenset(medium_swapped - high_swapped), column_5),
        )
    )

    row_5 = complete_family((0, 1, 2, 3, 4))
    row_6 = complete_family((0, 1, 2, 3, 4, 5))
    row_7 = complete_family((0, 1, 2, 3, 4, 5, 6))
    column_35 = complete_family((0, 1, 2, 3, 4, 5, 6))
    column_25 = extremal_25((0, 1, 2, 3, 4), 5, 6)
    column_15_b = complete_family((0, 1, 2, 3, 4, 5))
    family_b = product_family(
        (
            (row_5, column_35),
            (frozenset(row_6 - row_5), column_25),
            (frozenset(row_7 - row_6), column_15_b),
        )
    )

    expected_profiles = {
        "A1_common_apex": (15,) * 45 + (5,) * 10 + (0,) * 15,
        "A2_exchanged_apex": (15,) * 45 + (5,) * 10 + (0,) * 15,
        "B_biflag": (35,) * 5 + (25,) * 10 + (15,) * 20 + (0,) * 35,
    }
    output: dict[str, object] = {}
    for name, family in (
        ("A1_common_apex", family_a1),
        ("A2_exchanged_apex", family_a2),
        ("B_biflag", family_b),
    ):
        shadow_size = product_shadow(family).bit_count()
        require((family.bit_count(), shadow_size) == (725, 950), (name, family.bit_count(), shadow_size))
        require(row_profile(family) == expected_profiles[name], (name, row_profile(family)))
        output[name] = {
            "coordinate_pair_count": family.bit_count(),
            "simultaneous_shadow_size": shadow_size,
            "row_profile": list(expected_profiles[name]),
        }
    return output


def build_payload() -> dict[str, object]:
    profile_a_records, profile_a_rows = enumerate_profile_a_rows()
    profile_b_rows = enumerate_profile_b_rows()
    columns = enumerate_column_structures()
    representatives = representative_families()

    profile_a_type_count = 336 * 168
    profile_a_total = 2 * profile_a_type_count
    profile_b_total = 336 * 336
    require(profile_a_type_count == 56_448, profile_a_type_count)
    require(profile_a_total == profile_b_total == 112_896, (profile_a_total, profile_b_total))
    all_profiles = 2 * profile_a_total + 2 * profile_b_total
    require(all_profiles == 451_584, all_profiles)

    core = {
        "status": [
            "PURE_COORDINATE_EQUALITY_THEOREM",
            "EXACT_NESTED_EXTREMAL_INCIDENCE_REPLAY",
            "N8_Q17_B725_SHADOW950",
        ],
        "profile_A_row_incidence": profile_a_rows,
        "profile_A_row_records_sha256": canonical_hash(profile_a_records),
        "profile_B_row_incidence": profile_b_rows,
        "column_incidence": columns,
        "representative_families": representatives,
        "family_counts": {
            "A1_common_apex": profile_a_type_count,
            "A2_exchanged_apex": profile_a_type_count,
            "profile_A_total": profile_a_total,
            "profile_A_transposes": profile_a_total,
            "profile_B_biflag": profile_b_total,
            "profile_B_transposes": profile_b_total,
            "all_four_profiles": all_profiles,
        },
        "orbit_counts": {
            "S8xS8": 6,
            "with_transposition": 3,
        },
        "external_equality_input": {
            "source": "Serra--Vena, arXiv:2304.05145, Theorem 4",
            "used_sizes": [5, 15, 25, 35, 45, 55],
        },
        "claim_boundary": (
            "The coordinate size-725 shadow-950 locus is classified into "
            "three orbit types up to transposition. The result does not "
            "classify noncoordinate equality loci, prove seventeen-term "
            "Chow realizability or nonrealizability, supply the missing "
            "1377 rank dimensions, prove lower 78, or make a border-rank "
            "claim."
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
    print("GENERAL_PRODUCT_SHADOW_N8_Q17_COORDINATE_EQUALITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
