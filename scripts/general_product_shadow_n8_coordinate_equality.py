#!/usr/bin/env python3
"""Exact replay of the coordinate perm_8 product-shadow equality orbit.

The theorem is proved in docs/general_product_shadow_n8_coordinate_equality.md.
This script exhausts all flag parameters, reconstructs the 560 coordinate
pairs and their full simultaneous lower shadows, verifies injectivity and
normalizes every family into one S_8 x S_8 orbit.  Transposition supplies the
second orientation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
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


def family_from_parameters(
    z: int,
    column_six: tuple[int, ...],
    column_four: tuple[int, ...],
) -> tuple[int, tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    require(z in GROUND, z)
    require(len(column_six) == 6, column_six)
    require(len(column_four) == 4, column_four)
    require(set(column_four).issubset(column_six), (column_six, column_four))

    high_rows = tuple(
        index for index, row in enumerate(FOURS) if z not in row
    )
    low_rows = tuple(
        index for index, row in enumerate(FOURS) if z in row
    )
    high_columns = tuple(
        FOUR_INDEX[value] for value in combinations(column_six, 4)
    )
    low_column = FOUR_INDEX[column_four]

    require((len(high_rows), len(low_rows), len(high_columns)) == (35, 35, 15),
            (len(high_rows), len(low_rows), len(high_columns)))

    family = 0
    for row in high_rows:
        for column in high_columns:
            family |= 1 << (row * ROW_COUNT + column)
    for row in low_rows:
        family |= 1 << (row * ROW_COUNT + low_column)
    require(family.bit_count() == 560, family.bit_count())
    return family, high_rows, low_rows, high_columns


def explicit_product_shadow(family: int) -> int:
    shadow = 0
    remaining = family
    while remaining:
        least = remaining & -remaining
        position = least.bit_length() - 1
        row, column = divmod(position, ROW_COUNT)
        shadow |= PAIR_SHADOW[row][column]
        remaining ^= least
    return shadow


def permutation_for_flag(
    z: int,
    column_six: tuple[int, ...],
    column_four: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    row_map = [0] * 8
    row_map[z] = 7
    for image, value in enumerate(sorted(set(GROUND) - {z})):
        row_map[value] = image

    column_map = [0] * 8
    for image, value in enumerate(sorted(column_four)):
        column_map[value] = image
    middle = sorted(set(column_six) - set(column_four))
    outside = sorted(set(GROUND) - set(column_six))
    for offset, value in enumerate(middle, start=4):
        column_map[value] = offset
    for offset, value in enumerate(outside, start=6):
        column_map[value] = offset
    require(sorted(row_map) == list(GROUND), row_map)
    require(sorted(column_map) == list(GROUND), column_map)
    return tuple(row_map), tuple(column_map)


def permuted_four_index(
    index: int,
    permutation: tuple[int, ...],
) -> int:
    image = tuple(sorted(permutation[value] for value in FOURS[index]))
    return FOUR_INDEX[image]


def transform_family(
    family: int,
    row_permutation: tuple[int, ...],
    column_permutation: tuple[int, ...],
) -> int:
    row_images = tuple(
        permuted_four_index(index, row_permutation)
        for index in range(ROW_COUNT)
    )
    column_images = tuple(
        permuted_four_index(index, column_permutation)
        for index in range(ROW_COUNT)
    )
    transformed = 0
    remaining = family
    while remaining:
        least = remaining & -remaining
        position = least.bit_length() - 1
        row, column = divmod(position, ROW_COUNT)
        transformed |= 1 << (
            row_images[row] * ROW_COUNT + column_images[column]
        )
        remaining ^= least
    return transformed


def transpose_family(family: int) -> int:
    transposed = 0
    remaining = family
    while remaining:
        least = remaining & -remaining
        position = least.bit_length() - 1
        row, column = divmod(position, ROW_COUNT)
        transposed |= 1 << (column * ROW_COUNT + row)
        remaining ^= least
    return transposed


def row_profile(family: int) -> tuple[int, ...]:
    mask = (1 << ROW_COUNT) - 1
    values = tuple(
        ((family >> (row * ROW_COUNT)) & mask).bit_count()
        for row in range(ROW_COUNT)
    )
    return tuple(sorted(values, reverse=True))


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_payload() -> dict[str, object]:
    reference, _, _, _ = family_from_parameters(
        7,
        tuple(range(6)),
        tuple(range(4)),
    )
    reference_shadow = explicit_product_shadow(reference)
    require(reference_shadow.bit_count() == 784, reference_shadow.bit_count())

    oriented_families: set[int] = set()
    normalized_families: set[int] = set()
    shadow_histogram: dict[int, int] = {}

    parameter_count = 0
    for z in GROUND:
        for column_six in combinations(GROUND, 6):
            for column_four in combinations(column_six, 4):
                parameter_count += 1
                family, _, _, _ = family_from_parameters(
                    z,
                    column_six,
                    column_four,
                )
                shadow_size = explicit_product_shadow(family).bit_count()
                shadow_histogram[shadow_size] = (
                    shadow_histogram.get(shadow_size, 0) + 1
                )
                require(shadow_size == 784, (z, column_six, column_four, shadow_size))
                oriented_families.add(family)

                row_permutation, column_permutation = permutation_for_flag(
                    z,
                    column_six,
                    column_four,
                )
                normalized = transform_family(
                    family,
                    row_permutation,
                    column_permutation,
                )
                require(normalized == reference, (z, column_six, column_four))
                normalized_families.add(normalized)

    require(parameter_count == 8 * 28 * 15 == 3360, parameter_count)
    require(len(oriented_families) == parameter_count, len(oriented_families))
    require(normalized_families == {reference}, len(normalized_families))
    require(shadow_histogram == {784: 3360}, shadow_histogram)

    transposed_families = {transpose_family(value) for value in oriented_families}
    require(len(transposed_families) == 3360, len(transposed_families))
    require(oriented_families.isdisjoint(transposed_families), "orientation collision")

    high_profile = (15,) * 35 + (1,) * 35
    conjugate_profile = (70,) + (35,) * 14 + (0,) * 55
    require(row_profile(reference) == high_profile, row_profile(reference))
    require(
        row_profile(transpose_family(reference)) == conjugate_profile,
        row_profile(transpose_family(reference)),
    )

    core = {
        "status": [
            "PURE_COORDINATE_EQUALITY_THEOREM",
            "EXACT_FLAG_FAMILY_REPLAY",
            "N8_SIZE560_SHADOW784",
        ],
        "parameter_counts": {
            "row_labels_z": 8,
            "column_six_sets": 28,
            "column_four_sets_inside_six": 15,
            "families_per_orientation": 3360,
            "families_with_transposes": 6720,
        },
        "family_invariants": {
            "coordinate_pair_count": 560,
            "simultaneous_shadow_size": 784,
            "row_profile": list(high_profile),
            "transposed_row_profile": list(conjugate_profile),
            "shadow_histogram": {str(key): value for key, value in shadow_histogram.items()},
        },
        "orbit_invariants": {
            "S8xS8_orbits_per_orientation": 1,
            "orbits_after_adjoining_transpose": 1,
            "parameter_map_injective": True,
            "orientation_sets_disjoint": True,
        },
        "reference_parameters": {
            "z": 7,
            "column_six": list(range(6)),
            "column_four": list(range(4)),
        },
        "external_equality_input": {
            "source": "Serra--Vena, arXiv:2304.05145, Theorem 4",
            "instances": [
                "35 four-sets with shadow 35 are C(U,4), |U|=7",
                "15 four-sets with shadow 20 are C(V,4), |V|=6",
            ],
        },
        "claim_boundary": (
            "The script replays every family in the proved coordinate flag "
            "classification. The converse classification uses the written "
            "compression, equality and Johnson-connectivity proof plus the "
            "source-bound one-dimensional Kruskal--Katona equality theorem. "
            "No noncoordinate or Chow-realizability claim is made."
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
    print("GENERAL_PRODUCT_SHADOW_N8_COORDINATE_EQUALITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
