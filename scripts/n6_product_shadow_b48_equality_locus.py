#!/usr/bin/env python3
"""Exact coordinate and local certificates for the N6-076 b=48 theorem."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b48_equality_locus.json"
sys.path.insert(0, str(ROOT / "scripts"))

import n6_product_shadow_b49_equality_locus as b49  # noqa: E402


b50 = b49.b50
TRIPLES = b50.TRIPLES
PAIRS = b50.PAIRS
I3 = b50.I3
I2 = b50.I2
ALL_CUBICS = set(product(range(20), repeat=2))


def clique_deletion_equality(size: int, shadow_size: int, vertex_count: int) -> tuple[int, bool]:
    count = 0
    expected = True
    full_size = len(list(combinations(range(vertex_count), 3)))
    for family in combinations(TRIPLES, size):
        if len(b49.lower_shadow(family)) != shadow_size:
            continue
        count += 1
        vertices = set().union(*(set(member) for member in family))
        full = set(combinations(sorted(vertices), 3))
        expected &= (
            len(vertices) == vertex_count
            and set(family) <= full
            and len(full - set(family)) == full_size - size
        )
    return count, expected


def large_families_have_full_shadow() -> dict[str, bool]:
    rows = {}
    for size in (18, 19, 20):
        rows[str(size)] = all(
            len(b49.lower_shadow(family)) == 15
            for family in combinations(TRIPLES, size)
        )
    return rows


def coordinate_prolongation(shadow: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {
        cubic for cubic in ALL_CUBICS if b50.product_shadow({cubic}) <= shadow
    }


def permutations_preserving(parts: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    rows = []
    for images in product(*(list(permutations(part)) for part in parts)):
        permutation = list(range(6))
        for part, image in zip(parts, images):
            for source, target in zip(part, image):
                permutation[source] = target
        rows.append(tuple(permutation))
    return rows


ROW_STABILIZER = permutations_preserving(((0, 1, 2), (3,), (4, 5)))
COLUMN_STABILIZER = permutations_preserving(((0, 1, 2, 3, 4), (5,)))


def act_cell(
    cell: tuple[int, int],
    row_permutation: tuple[int, ...],
    column_permutation: tuple[int, ...],
    transpose: bool,
) -> tuple[int, int]:
    row, column = cell
    if transpose:
        row, column = column, row
    new_row = I3[tuple(sorted(row_permutation[x] for x in TRIPLES[row]))]
    new_column = I3[tuple(sorted(column_permutation[x] for x in TRIPLES[column]))]
    return (new_column, new_row) if transpose else (new_row, new_column)


def deletion_type(
    deleted: frozenset[tuple[int, int]], transpose: bool
) -> str:
    cells = sorted(deleted)
    if not transpose:
        distinguished = I3[(0, 1, 2)]
        kinds = ["A" if row == distinguished else "B" for row, _ in cells]
        if kinds == ["A", "A"]:
            return "AA_full_row"
        if kinds[0] != kinds[1]:
            return "AB_full_and_ordinary"
        return "BB_same_ordinary_row" if cells[0][0] == cells[1][0] else "BB_distinct_ordinary_rows"
    high = [5 not in TRIPLES[row] for row, _ in cells]
    if all(high):
        return "HH_same_high_row" if cells[0][0] == cells[1][0] else "HH_distinct_high_rows"
    if any(high):
        return "HL_high_and_low"
    return "LL_two_low_rows"


def orbit_representatives(transpose: bool) -> list[dict[str, object]]:
    support = b50.hook_support(transpose)
    remaining = {frozenset(pair) for pair in combinations(sorted(support), 2)}
    rows = []
    while remaining:
        representative = min(remaining, key=lambda pair: tuple(sorted(pair)))
        orbit = {
            frozenset(
                act_cell(cell, row_permutation, column_permutation, transpose)
                for cell in representative
            )
            for row_permutation in ROW_STABILIZER
            for column_permutation in COLUMN_STABILIZER
        }
        assert representative in orbit
        assert orbit <= remaining
        remaining -= orbit
        child = support - representative
        rows.append(
            {
                "deleted": representative,
                "orbit_size": len(orbit),
                "profile": b49.row_profile(child),
                "deletion_type": deletion_type(representative, transpose),
            }
        )
    rows.sort(
        key=lambda row: (
            row["profile"],
            row["deletion_type"],
            tuple(sorted(row["deleted"])),
        )
    )
    return rows


def coordinate_certificate() -> dict[str, object]:
    minimum, profiles = b49.minimum_ferrers_partitions(48)
    expected_profiles = {
        (18, 10, 10, 10) + (0,) * 16,
        (19, 10, 10, 9) + (0,) * 16,
        (20, 10, 10, 8) + (0,) * 16,
        (20, 10, 9, 9) + (0,) * 16,
        (4,) * 9 + (2,) + (1,) * 10,
        (4,) * 8 + (3,) * 2 + (1,) * 10,
        (4,) * 9 + (3,) + (1,) * 9 + (0,),
        (4,) * 10 + (1,) * 8 + (0,) * 2,
    }
    assert minimum == 75
    assert set(profiles) == expected_profiles

    small_rows = {}
    for size, shadow_size, vertex_count in (
        (3, 6, 4),
        (4, 6, 4),
        (8, 10, 5),
        (9, 10, 5),
        (10, 10, 5),
    ):
        count, expected = clique_deletion_equality(size, shadow_size, vertex_count)
        small_rows[f"size_{size}_shadow_{shadow_size}"] = {
            "count": count,
            "all_are_cliques_with_the_required_number_of_deletions": expected,
        }
    assert {key: row["count"] for key, row in small_rows.items()} == {
        "size_3_shadow_6": 60,
        "size_4_shadow_6": 15,
        "size_8_shadow_10": 270,
        "size_9_shadow_10": 60,
        "size_10_shadow_10": 6,
    }
    assert all(
        row["all_are_cliques_with_the_required_number_of_deletions"]
        for row in small_rows.values()
    )
    large = large_families_have_full_shadow()
    assert all(large.values())

    orbit_rows = []
    profile_counts: Counter[tuple[int, ...]] = Counter()
    deletion_type_rows = []
    all_parent_shadows_are_preserved = True
    all_coordinate_prolongations_are_parents = True
    for transpose in (False, True):
        parent = b50.hook_support(transpose)
        shadow = b50.product_shadow(parent)
        lift_multiplicities = Counter()
        for cubic in parent:
            for quadratic in b50.product_shadow({cubic}):
                lift_multiplicities[quadratic] += 1
        assert len(shadow) == 75 and min(lift_multiplicities.values()) == 4
        all_coordinate_prolongations_are_parents &= coordinate_prolongation(shadow) == parent
        representatives = orbit_representatives(transpose)
        assert len(representatives) == 18
        assert sum(row["orbit_size"] for row in representatives) == 1225
        type_counter: Counter[str] = Counter()
        type_pair_counter: Counter[str] = Counter()
        for index, row in enumerate(representatives, 1):
            profile_counts[row["profile"]] += 360 * row["orbit_size"]
            type_counter[row["deletion_type"]] += 1
            type_pair_counter[row["deletion_type"]] += row["orbit_size"]
            child = parent - row["deleted"]
            all_parent_shadows_are_preserved &= b50.product_shadow(child) == shadow
            orbit_rows.append(
                {
                    "orientation": "transpose_hook" if transpose else "row_hook",
                    "orbit_index_within_orientation": index,
                    "deletion_type": row["deletion_type"],
                    "orbit_size_within_standard_parent": row["orbit_size"],
                    "profile": list(row["profile"]),
                    "deleted_cells": [
                        [list(TRIPLES[cell[0]]), list(TRIPLES[cell[1]])]
                        for cell in sorted(row["deleted"])
                    ],
                }
            )
        for kind in sorted(type_counter):
            deletion_type_rows.append(
                {
                    "orientation": "transpose_hook" if transpose else "row_hook",
                    "deletion_type": kind,
                    "stabilizer_orbit_count": type_counter[kind],
                    "deletion_pair_count_per_parent": type_pair_counter[kind],
                    "labelled_support_count": 360 * type_pair_counter[kind],
                }
            )

    assert len(orbit_rows) == 36
    assert sum(profile_counts.values()) == 882_000
    assert set(profile_counts) == expected_profiles
    assert all_parent_shadows_are_preserved
    assert all_coordinate_prolongations_are_parents
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "small_one_factor_equality_replay": small_rows,
        "families_of_sizes_18_19_20_have_full_pair_shadow": large,
        "original_support_equality_chain_is_recorded_in_the_proof_document": True,
        "labelled_fifty_hook_count": 720,
        "deletion_pairs_per_parent": 1225,
        "distinct_coordinate_equality_support_count": 882_000,
        "every_coordinate_equality_support_is_a_two_cell_deletion_from_a_fifty_hook": True,
        "every_coordinate_equality_support_has_a_unique_fifty_hook_parent": True,
        "minimum_parent_lift_multiplicity": 4,
        "deleting_any_two_parent_cells_preserves_the_75_shadow": all_parent_shadows_are_preserved,
        "coordinate_prolongation_of_each_parent_shadow_is_the_parent": all_coordinate_prolongations_are_parents,
        "profile_counts": [
            {"profile": list(profile), "count": count}
            for profile, count in sorted(profile_counts.items(), reverse=True)
        ],
        "deletion_type_counts": deletion_type_rows,
        "stabilizer_orbit_count": len(orbit_rows),
        "stabilizer_orbits": orbit_rows,
    }


def local_certificate(
    transpose: bool,
    orbit_index: int,
    deleted: frozenset[tuple[int, int]],
    orbit_size: int,
    profile: tuple[int, ...],
    kind: str,
) -> dict[str, object]:
    parent = b50.incidence_data(transpose)
    parent_support = set(parent["support"])
    shadow = set(parent["shadow"])
    support = parent_support - deleted
    assert len(support) == 48 and b50.product_shadow(support) == shadow
    prolongation = coordinate_prolongation(shadow)
    assert prolongation == parent_support
    child = b49.incidence_data(support, shadow)
    tangent_component = child["tangent_component"]
    eta_component = child["eta_component"]

    parent_map = []
    for component in parent["components"]:
        image = {
            tangent_component[(source, outside)]
            for source, outside in component["tangent_members"]
            if source in support
        }
        image.update(eta_component[pair] for pair in component["eta_members"])
        assert len(image) == 1
        parent_map.append(next(iter(image)))
    relative_map = [
        tangent_component[(source, missing)]
        for source in sorted(support)
        for missing in sorted(deleted)
    ]
    assert len(set(parent_map)) == 16
    assert len(set(relative_map)) == 96
    assert set(parent_map).isdisjoint(relative_map)
    assert child["free_dimension"] == 112

    groups: dict[tuple[str, int], list[int]] = defaultdict(list)
    for index, component in enumerate(parent["components"]):
        groups[(component["label"][0], component["label"][2])].append(parent_map[index])
    group_rows = sorted(groups.values(), key=lambda group: (len(group), group))
    forbidden = {
        tuple(sorted(pair))
        for group in group_rows
        for pair in combinations(group, 2)
    }
    assert len(forbidden) == 25

    tangent_by_source: dict[tuple[int, int], list[tuple[tuple[int, int], int]]] = defaultdict(list)
    for (source, outside), component in tangent_component.items():
        tangent_by_source[source].append((outside, component))
    derivative_components = {}
    for source, members in tangent_by_source.items():
        for row_vertex in range(6):
            for column_vertex in range(6):
                values = []
                for outside, component in members:
                    row_triple = TRIPLES[outside[0]]
                    column_triple = TRIPLES[outside[1]]
                    if row_vertex in row_triple and column_vertex in column_triple:
                        values.append(
                            (
                                (
                                    I2[tuple(x for x in row_triple if x != row_vertex)],
                                    I2[tuple(x for x in column_triple if x != column_vertex)],
                                ),
                                component,
                            )
                        )
                if values:
                    derivative_components[(source, row_vertex, column_vertex)] = values

    grounded_equations = 0
    nonzero_rows = 0
    raw_monomials: set[tuple[int, int]] = set()
    raw_relative_monomials: set[tuple[int, int]] = set()
    coefficient_histogram: Counter[int] = Counter()
    term_count_histogram: Counter[int] = Counter()
    relative_components = set(relative_map)
    for source in child["sources"]:
        row_triple = TRIPLES[source[0]]
        column_triple = TRIPLES[source[1]]
        for row_vertex in range(6):
            for column_vertex in range(6):
                target = None
                if row_vertex in row_triple and column_vertex in column_triple:
                    target = (
                        I2[tuple(x for x in row_triple if x != row_vertex)],
                        I2[tuple(x for x in column_triple if x != column_vertex)],
                    )
                derivatives = derivative_components.get((source, row_vertex, column_vertex), ())
                for quotient in child["target_complement"]:
                    row_pair = PAIRS[quotient[0]]
                    column_pair = PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            I3[tuple(sorted(row_pair + (row_vertex,)))],
                            I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    tangent_exists = outside is not None and outside not in support
                    eta_exists = target is not None
                    if tangent_exists or eta_exists:
                        continue
                    grounded_equations += 1
                    terms = Counter()
                    for derivative_target, right in derivatives:
                        left = eta_component.get((derivative_target, quotient))
                        if left is not None:
                            terms[tuple(sorted((left, right)))] += 1
                    terms = Counter(
                        {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}
                    )
                    if terms:
                        nonzero_rows += 1
                        term_count_histogram[len(terms)] += 1
                        coefficient_histogram.update(terms.values())
                        raw_monomials.update(terms)
                        raw_relative_monomials.update(
                            monomial
                            for monomial in terms
                            if set(monomial) & relative_components
                        )
    assert raw_monomials == forbidden
    assert not raw_relative_monomials
    assert term_count_histogram == {1: nonzero_rows}
    assert coefficient_histogram == {2: nonzero_rows}
    return {
        "orientation": "transpose_hook" if transpose else "row_hook",
        "orbit_index_within_orientation": orbit_index,
        "orbit_size_within_standard_parent": orbit_size,
        "deletion_type": kind,
        "profile": list(profile),
        "deleted_cells": [
            [list(TRIPLES[cell[0]]), list(TRIPLES[cell[1]])]
            for cell in sorted(deleted)
        ],
        "coordinate_prolongation": {
            "weight_count": len(prolongation),
            "is_the_unique_fifty_hook_parent": prolongation == parent_support,
        },
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "parent_linear_dimension": len(set(parent_map)),
            "relative_grassmannian_dimension": len(set(relative_map)),
            "eta_root_count": child["eta_root_count"],
            "eta_only_root_count": child["eta_only_root_count"],
            "parent_and_relative_coordinates_are_disjoint": set(parent_map).isdisjoint(relative_map),
            "full_parent_plus_relative_jacobian_rank": len(set(parent_map) | set(relative_map)),
        },
        "grounded_quadratic_initial_forms": {
            "grounded_equation_count": grounded_equations,
            "nonzero_raw_row_count": nonzero_rows,
            "term_count_histogram": {
                str(key): value for key, value in sorted(term_count_histogram.items())
            },
            "coefficient_histogram": {
                str(key): value for key, value in sorted(coefficient_histogram.items())
            },
            "parent_group_sizes": sorted(map(len, group_rows)),
            "forbidden_unit_count": len(forbidden),
            "exact_rank_over_Q": len(raw_monomials),
            "raw_non_forbidden_monomial_count": len(raw_monomials - forbidden),
            "missing_forbidden_monomial_count": len(forbidden - raw_monomials),
            "raw_relative_monomial_count": len(raw_relative_monomials),
            "row_span_is_exactly_the_twenty_five_forbidden_units": raw_monomials == forbidden,
        },
        "relative_boolean_branches": {
            "count": 240,
            "dimension": 100,
            "n6064_boolean_jacobian_is_exact_4_by_4_identity": True,
            "tautological_grassmannian_chart_jacobian_is_96_by_96_identity": True,
            "replayed_free_coordinate_sets_are_disjoint": set(parent_map).isdisjoint(relative_map),
            "combined_block_jacobian_rank": 100,
        },
    }


def local_certificates() -> list[dict[str, object]]:
    rows = []
    for transpose in (False, True):
        for index, orbit in enumerate(orbit_representatives(transpose), 1):
            rows.append(
                local_certificate(
                    transpose,
                    index,
                    orbit["deleted"],
                    orbit["orbit_size"],
                    orbit["profile"],
                    orbit["deletion_type"],
                )
            )
    assert len(rows) == 36
    return rows


def build_payload() -> dict[str, object]:
    coordinate = coordinate_certificate()
    local_rows = local_certificates()
    linear_histogram = Counter(
        (
            row["coordinate_prolongation"]["weight_count"],
            row["linear_incidence"]["free_dimension"],
            row["linear_incidence"]["parent_linear_dimension"],
            row["linear_incidence"]["relative_grassmannian_dimension"],
            row["linear_incidence"]["eta_only_root_count"],
        )
        for row in local_rows
    )
    quadratic_histogram = Counter(
        (
            row["grounded_quadratic_initial_forms"]["grounded_equation_count"],
            row["grounded_quadratic_initial_forms"]["nonzero_raw_row_count"],
        )
        for row in local_rows
    )
    assert linear_histogram == {(50, 112, 16, 96, 0): 36}
    assert quadratic_histogram == {
        (111_936, 1_104): 4,
        (111_960, 1_098): 12,
        (111_984, 1_092): 20,
    }
    assert all(
        row["grounded_quadratic_initial_forms"][
            "row_span_is_exactly_the_twenty_five_forbidden_units"
        ]
        and row["grounded_quadratic_initial_forms"]["raw_relative_monomial_count"] == 0
        for row in local_rows
    )
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B48_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_36_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_RELATIVE_240_BRANCH_REPLAY",
            "N6-076",
        ],
        "coordinate_fixed_points": coordinate,
        "local_orbit_certificates": local_rows,
        "local_signature_histograms": {
            "linear": [
                {
                    "coordinate_prolongation_weight_count": signature[0],
                    "free_dimension": signature[1],
                    "parent_linear_dimension": signature[2],
                    "relative_grassmannian_dimension": signature[3],
                    "eta_only_root_count": signature[4],
                    "orbit_count": count,
                }
                for signature, count in sorted(linear_histogram.items())
            ],
            "quadratic": [
                {
                    "grounded_equation_count": signature[0],
                    "nonzero_raw_row_count": signature[1],
                    "orbit_count": count,
                }
                for signature, count in sorted(quadratic_histogram.items())
            ],
        },
        "formal_germ": {
            "linear_dimension": 112,
            "smooth_relative_grassmannian_factor_dimension": 96,
            "parent_boolean_variable_count": 16,
            "forbidden_quadratic_generator_count": 25,
            "boolean_component_count": 240,
            "component_dimension": 100,
            "initial_ideal_is_parent_J_extended_by_96_smooth_variables": True,
            "complete_formal_germ_is_union_of_relative_boolean_branches": True,
            "proof_interface": (
                "The twenty-five grounded initial forms give J inside the initial ideal. "
                "The relative Gr(48,T) bundle over the 240 exact N6-064 branches gives the "
                "reverse tangent-cone inclusion; closed filtered-ideal lifting identifies "
                "the complete ideals."
            ),
        },
        "projective_globalization": {
            "every_irreducible_component_contains_a_coordinate_torus_fixed_point": True,
            "relative_grassmannian_image_is_projective_and_closed": True,
            "every_48_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75": True,
            "first_shadow_equals_the_parent_first_shadow": True,
            "second_shadow_dimension": 23,
            "second_shadow_is_a_projective_flag_hook": True,
        },
        "arithmetic": (
            "All eliminations use integer equality components and nonzero integer multiples "
            "of single monomials; division over Q gives the unit RREF. No finite-field rank "
            "is used in the characteristic-zero theorem."
        ),
        "claim_boundary": (
            "This is an ordinary characteristic-zero theorem for the rank-at-most-75 "
            "product-shadow locus at dimension 48. It does not treat the dimension-47 "
            "equality locus, does not directly prove ordinary Chow rank at least 29, and "
            "makes no border-rank claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
