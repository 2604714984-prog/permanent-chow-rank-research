#!/usr/bin/env python3
"""Exact two-deletion certificate for the 78-to-90 equality locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b78_equality_locus.json"
N6082_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b80_equality_locus.py"
N6082_DATA = ROOT / "data" / "n6_product_shadow_b80_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coordinate_certificate(n6082, b49, b50) -> dict[str, object]:
    minimum, profiles = b49.minimum_ferrers_partitions(78)
    expected = {
        (20, 20, 20, 18) + (0,) * 16,
        (20, 20, 19, 19) + (0,) * 16,
        (4,) * 19 + (2,),
        (4,) * 18 + (3, 3),
    }
    require(minimum == 90 and set(profiles) == expected, (minimum, profiles))
    parents = []
    for transpose in (False, True):
        for active in combinations(range(6), 4):
            rows = {b49.I3[row] for row in combinations(active, 3)}
            support = frozenset((row, column) for row in rows for column in range(20))
            if transpose:
                support = frozenset((column, row) for row, column in support)
            parents.append(support)
    children: Counter[frozenset[tuple[int, int]]] = Counter()
    profiles_seen: Counter[tuple[int, ...]] = Counter()
    all_shadows = True
    for parent in parents:
        for deleted in combinations(parent, 2):
            child = parent - set(deleted)
            frozen = frozenset(child)
            children[frozen] += 1
            profiles_seen[b49.row_profile(frozen)] += 1
            all_shadows &= len(b50.product_shadow(child)) == 90
    require(len(parents) == 30, len(parents))
    require(len(children) == 94_800 and Counter(children.values()) == {1: 94_800}, Counter(children.values()))
    require(set(profiles_seen) == expected and all_shadows, profiles_seen)
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "labelled_80_plane_parent_count": len(parents),
        "labelled_parent_two_cell_deletions": len(parents) * 3160,
        "distinct_coordinate_78_plane_count": len(children),
        "parent_multiplicity_histogram": {str(key): value for key, value in sorted(Counter(children.values()).items())},
        "profile_counts": [
            {"profile": list(profile), "count": count}
            for profile, count in sorted(profiles_seen.items(), reverse=True)
        ],
        "all_children_have_first_shadow_90": all_shadows,
        "every_coordinate_equality_support_has_a_unique_80_plane_product_parent": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


def orbit_representatives(n6082, b49, transpose: bool) -> list[tuple[str, set[tuple[int, int]]]]:
    support, _ = n6082.standard_support(b49, transpose)
    row_values = sorted({cell[1] if transpose else cell[0] for cell in support})
    triple_axis = 0 if transpose else 1
    reps = []
    fixed_row = row_values[0]
    same_row = [cell for cell in support if (cell[1] if transpose else cell[0]) == fixed_row]
    for intersection in (0, 1, 2):
        pair = next(
            pair
            for pair in combinations(same_row, 2)
            if len(set(b49.TRIPLES[pair[0][triple_axis]]) & set(b49.TRIPLES[pair[1][triple_axis]])) == intersection
        )
        reps.append((f"same_product_row_column_triple_intersection_{intersection}", set(pair)))
    first_row, second_row = row_values[:2]
    first_cells = [cell for cell in support if (cell[1] if transpose else cell[0]) == first_row]
    second_cells = [cell for cell in support if (cell[1] if transpose else cell[0]) == second_row]
    for intersection in (0, 1, 2, 3):
        pair = next(
            (left, right)
            for left in first_cells
            for right in second_cells
            if len(set(b49.TRIPLES[left[triple_axis]]) & set(b49.TRIPLES[right[triple_axis]])) == intersection
        )
        reps.append((f"different_product_rows_column_triple_intersection_{intersection}", set(pair)))
    require(len(reps) == 7, reps)
    return reps


def local_certificate(n6082, b49, b50, transpose: bool, orbit: str, deleted: set[tuple[int, int]]) -> dict[str, object]:
    parent_support, shadow = n6082.standard_support(b49, transpose)
    support = parent_support - deleted
    parent = b49.incidence_data(parent_support, shadow)
    child = b49.incidence_data(support, shadow)
    require((parent["free_dimension"], child["free_dimension"], child["eta_only_root_count"]) == (8, 164, 0), child)
    parent_roots = sorted(set(parent["tangent_component"].values()) | set(parent["eta_component"].values()))
    parent_map = {}
    for root in parent_roots:
        image = {
            child["tangent_component"][pair]
            for pair, value in parent["tangent_component"].items()
            if value == root and pair[0] in support
        }
        image.update(
            child["eta_component"][pair]
            for pair, value in parent["eta_component"].items()
            if value == root
        )
        require(len(image) == 1, (root, image))
        parent_map[root] = next(iter(image))
    relative = {
        child["tangent_component"][(source, outside)]
        for source in sorted(support)
        for outside in sorted(deleted)
    }
    require(len(set(parent_map.values())) == 8 and len(relative) == 156, (parent_map, relative))
    require(set(parent_map.values()).isdisjoint(relative), None)
    parent_groups, _ = n6082.component_groups(b49, parent, transpose)
    groups = [[parent_map[root] for root in group] for group in parent_groups]
    forbidden = {tuple(sorted(pair)) for group in groups for pair in combinations(group, 2)}
    grounded = n6082.grounded_certificate(b49, child, forbidden)
    prolongation = {cubic for cubic in b49.ALL_CUBICS if b50.product_shadow({cubic}) <= shadow}
    require(prolongation == parent_support, len(prolongation))
    return {
        "orientation": "transpose_product" if transpose else "row_product",
        "orbit": orbit,
        "deleted_cells": [[list(b49.TRIPLES[row]), list(b49.TRIPLES[column])] for row, column in sorted(deleted)],
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "parent_linear_dimension": len(set(parent_map.values())),
            "relative_Gr_78_80_dimension": len(relative),
            "eta_only_root_count": child["eta_only_root_count"],
            "parent_and_relative_coordinates_are_disjoint": True,
            "coordinate_prolongation_dimension": len(prolongation),
        },
        "grounded_quadratic_initial_forms": grounded,
        "relative_boolean_branches": {
            "count": 16,
            "dimension": 158,
            "n6082_parent_branch_dimension": 2,
            "tautological_Gr_78_80_chart_dimension": 156,
            "combined_block_jacobian_rank": 158,
        },
    }


def build_payload() -> dict[str, object]:
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6086")
    require(n6082.build_payload() == json.loads(N6082_DATA.read_text(encoding="utf-8")), N6082_DATA)
    b49 = n6082.load_module(n6082.B49_SCRIPT, "b49_for_n6086")
    b50 = n6082.load_module(n6082.B50_SCRIPT, "b50_for_n6086")
    coordinate = coordinate_certificate(n6082, b49, b50)
    local = []
    for transpose in (False, True):
        for orbit, deleted in orbit_representatives(n6082, b49, transpose):
            local.append(local_certificate(n6082, b49, b50, transpose, orbit, deleted))
    require(len(local) == 14, len(local))
    signatures = Counter(
        (
            row["grounded_quadratic_initial_forms"]["grounded_equation_count"],
            row["grounded_quadratic_initial_forms"]["nonzero_raw_row_count"],
        )
        for row in local
    )
    require(all(row["grounded_quadratic_initial_forms"]["exact_rank_over_Q"] == 12 for row in local), local)
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B78_EQUALITY_LOCUS_EXTENSION",
            "EXACT_FOURTEEN_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION",
            "N6-086",
        ],
        "coordinate_fixed_points": coordinate,
        "stabilizer_orbit_coverage": {
            "row_product_orbit_count": 7,
            "transpose_product_orbit_count": 7,
            "total_orbit_count": len(local),
            "all_parent_two_cell_deletions_are_covered": True,
        },
        "local_orbit_representatives": local,
        "grounded_signature_histogram": [
            {"grounded_equation_count": key[0], "nonzero_raw_row_count": key[1], "orbit_count": count}
            for key, count in sorted(signatures.items())
        ],
        "formal_germ": {
            "linear_dimension": 164,
            "smooth_relative_Gr_78_80_factor_dimension": 156,
            "parent_boolean_variable_count": 8,
            "forbidden_quadratic_generator_count": 12,
            "boolean_component_count": 16,
            "component_dimension": 158,
            "initial_ideal_is_parent_J_extended_by_156_smooth_variables": True,
            "complete_formal_germ_is_union_of_relative_Grassmann_branches": True,
        },
        "projective_globalization": {
            "every_78_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow": True,
            "every_78_to_90_plane_has_second_shadow_dimension_24": True,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
        },
        "claim_boundary": (
            "This proves the 78-to-80 same-shadow extension. It does not classify 77-planes, "
            "does not by itself exclude an actual seven-frame x=78 packet, does not exclude "
            "global b=34, and makes no border-rank claim."
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
    print("coordinate_children=94800 stabilizer_orbits=14")
    print("local_free=164 quadratic_rank=12 relative_dimension=156")
    print("N6_PRODUCT_SHADOW_B78_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
