#!/usr/bin/env python3
"""Exact coordinate and local certificates for the N6-078 b=47 theorem."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b47_equality_locus.json"
sys.path.insert(0, str(ROOT / "scripts"))

import n6_product_shadow_b48_equality_locus as b48  # noqa: E402


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def orbit_representatives(transpose: bool) -> list[dict[str, object]]:
    support = b48.b50.hook_support(transpose)
    remaining = {frozenset(row) for row in combinations(sorted(support), 3)}
    rows = []
    while remaining:
        representative = min(remaining, key=lambda row: tuple(sorted(row)))
        orbit = {
            frozenset(
                b48.act_cell(cell, row_permutation, column_permutation, transpose)
                for cell in representative
            )
            for row_permutation in b48.ROW_STABILIZER
            for column_permutation in b48.COLUMN_STABILIZER
        }
        require(representative in orbit and orbit <= remaining, representative)
        remaining -= orbit
        child = support - representative
        require(len(child) == 47, len(child))
        require(b48.b50.product_shadow(child) == b48.b50.product_shadow(support), representative)
        rows.append(
            {
                "deleted": representative,
                "orbit_size": len(orbit),
                "profile": b48.b49.row_profile(child),
            }
        )
    rows.sort(key=lambda row: (row["profile"], tuple(sorted(row["deleted"]))))
    return rows


def build_payload() -> dict[str, object]:
    minimum, profiles = b48.b49.minimum_ferrers_partitions(47)
    expected_profiles = {
        (20, 10, 10, 7) + (0,) * 16,
        (20, 10, 9, 8) + (0,) * 16,
        (20, 9, 9, 9) + (0,) * 16,
        (19, 10, 10, 8) + (0,) * 16,
        (19, 10, 9, 9) + (0,) * 16,
        (18, 10, 10, 9) + (0,) * 16,
        (17, 10, 10, 10) + (0,) * 16,
        (4,) * 10 + (1,) * 7 + (0,) * 3,
        (4,) * 9 + (3,) + (1,) * 8 + (0,) * 2,
        (4,) * 9 + (2,) + (1,) * 9 + (0,),
        (4,) * 9 + (1,) * 11,
        (4,) * 8 + (3,) * 2 + (1,) * 9 + (0,),
        (4,) * 8 + (3,) + (2,) + (1,) * 10,
        (4,) * 7 + (3,) * 3 + (1,) * 10,
    }
    require(minimum == 75 and set(profiles) == expected_profiles, (minimum, profiles))

    parent = b48.b50.hook_support(False)
    parent_shadow = b48.b50.product_shadow(parent)
    multiplicities = Counter()
    for cubic in parent:
        multiplicities.update(b48.b50.product_shadow({cubic}))
    require(len(parent_shadow) == 75 and min(multiplicities.values()) == 4, multiplicities)

    orbit_rows = []
    profile_counts: Counter[tuple[int, ...]] = Counter()
    orbit_size_histogram: Counter[int] = Counter()
    linear_histogram: Counter[tuple[int, ...]] = Counter()
    quadratic_histogram: Counter[tuple[int, ...]] = Counter()
    for transpose in (False, True):
        representatives = orbit_representatives(transpose)
        require(len(representatives) == 112, len(representatives))
        require(sum(int(row["orbit_size"]) for row in representatives) == comb(50, 3), representatives)
        for index, orbit in enumerate(representatives, 1):
            profile_counts[orbit["profile"]] += 360 * int(orbit["orbit_size"])
            orbit_size_histogram[int(orbit["orbit_size"])] += 1
            certificate = b48.local_certificate(
                transpose,
                index,
                orbit["deleted"],
                int(orbit["orbit_size"]),
                orbit["profile"],
                "three_cell_deletion",
                child_dimension=47,
            )
            linear = certificate["linear_incidence"]
            quadratic = certificate["grounded_quadratic_initial_forms"]
            branch = certificate["relative_boolean_branches"]
            linear_histogram[
                (
                    int(linear["free_dimension"]),
                    int(linear["parent_linear_dimension"]),
                    int(linear["relative_grassmannian_dimension"]),
                    int(linear["eta_only_root_count"]),
                    int(linear["full_parent_plus_relative_jacobian_rank"]),
                )
            ] += 1
            quadratic_histogram[
                (
                    int(quadratic["grounded_equation_count"]),
                    int(quadratic["nonzero_raw_row_count"]),
                    int(quadratic["exact_rank_over_Q"]),
                    int(quadratic["raw_non_forbidden_monomial_count"]),
                    int(quadratic["missing_forbidden_monomial_count"]),
                    int(quadratic["raw_relative_monomial_count"]),
                )
            ] += 1
            require(
                branch["dimension"] == 145
                and branch["combined_block_jacobian_rank"] == 145,
                branch,
            )
            orbit_rows.append(
                {
                    "orientation": "transpose_hook" if transpose else "row_hook",
                    "orbit_index_within_orientation": index,
                    "orbit_size": int(orbit["orbit_size"]),
                    "profile": list(orbit["profile"]),
                    "deleted_cells": [
                        [list(b48.TRIPLES[cell[0]]), list(b48.TRIPLES[cell[1]])]
                        for cell in sorted(orbit["deleted"])
                    ],
                }
            )

    generated_support_count = 720 * comb(50, 3)
    require(len(orbit_rows) == 224, len(orbit_rows))
    require(sum(profile_counts.values()) == generated_support_count, profile_counts)
    require(set(profile_counts) == expected_profiles, profile_counts)
    require(linear_histogram == {(157, 16, 141, 0, 157): 224}, linear_histogram)
    require(
        all(key[2:] == (25, 0, 0, 0) for key in quadratic_histogram)
        and sum(quadratic_histogram.values()) == 224,
        quadratic_histogram,
    )
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B47_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_224_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_RELATIVE_240_BRANCH_REPLAY",
            "N6-078",
        ],
        "arithmetic": (
            "All local eliminations use integer equality components and nonzero "
            "integer multiples of single monomials; division over Q gives the "
            "unit RREF. No finite-field rank is used in the theorem."
        ),
        "ferrers_minimum_first_shadow": minimum,
        "ferrers_minimizing_profile_count": len(profiles),
        "ferrers_minimizing_profiles": [list(profile) for profile in profiles],
        "coordinate_fixed_points": {
            "labelled_fifty_hook_count": 720,
            "deleted_cells_per_child": 3,
            "deletions_per_parent": comb(50, 3),
            "distinct_coordinate_equality_support_count": generated_support_count,
            "minimum_parent_shadow_lift_multiplicity": min(multiplicities.values()),
            "original_support_equality_chain_is_recorded_in_the_proof_document": True,
            "every_coordinate_equality_support_is_a_three_cell_deletion_from_a_fifty_hook": True,
            "every_coordinate_equality_support_preserves_the_parent_75_shadow": True,
            "every_coordinate_equality_support_has_coordinate_prolongation_equal_to_its_unique_parent": True,
            "stabilizer_orbit_count": len(orbit_rows),
            "orbit_size_histogram": {str(key): value for key, value in sorted(orbit_size_histogram.items())},
            "profile_counts": [
                {"profile": list(profile), "count": count}
                for profile, count in sorted(profile_counts.items(), reverse=True)
            ],
            "stabilizer_orbits": orbit_rows,
        },
        "linear_signature_histogram": [
            {
                "free_dimension": key[0],
                "parent_linear_dimension": key[1],
                "relative_Gr_47_50_dimension": key[2],
                "eta_only_root_count": key[3],
                "parent_plus_relative_rank": key[4],
                "orbit_count": count,
            }
            for key, count in sorted(linear_histogram.items())
        ],
        "quadratic_signature_histogram": [
            {
                "grounded_equation_count": key[0],
                "nonzero_raw_row_count": key[1],
                "exact_forbidden_unit_rank": key[2],
                "raw_non_forbidden_monomial_count": key[3],
                "missing_forbidden_monomial_count": key[4],
                "raw_relative_monomial_count": key[5],
                "orbit_count": count,
            }
            for key, count in sorted(quadratic_histogram.items())
        ],
        "formal_germ": {
            "free_dimension": 157,
            "relative_Gr_47_50_dimension": 141,
            "forbidden_quadratic_generator_count": 25,
            "relative_variable_quadratic_generator_count": 0,
            "relative_boolean_branch_count": 240,
            "relative_boolean_branch_dimension": 145,
            "completed_local_scheme_is_the_union_of_the_240_relative_branches": True,
            "complete_filtered_lifting_is_scheme_theoretic": True,
        },
        "projective_globalization": {
            "every_47_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75": True,
            "relative_grassmannian_image_is_projective_and_closed": True,
            "every_irreducible_component_contains_a_coordinate_torus_fixed_point": True,
            "first_shadow_equals_the_parent_first_shadow": True,
            "second_shadow_dimension": 23,
            "second_shadow_is_a_projective_flag_hook": True,
        },
        "claim_boundary": (
            "This is an ordinary characteristic-zero theorem for the rank-at-most-75 "
            "product-shadow locus at dimension 47. It does not treat the dimension-46 "
            "locus, does not by itself prove ChowRank(perm_6)>=29, and makes no "
            "border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        require(payload == json.loads(args.verify_json.read_text(encoding="utf-8")), args.verify_json)
    print("orbits=224")
    print("linear_free_dimension=157")
    print("quadratic_forbidden_rank=25")
    print("N6_B47_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
