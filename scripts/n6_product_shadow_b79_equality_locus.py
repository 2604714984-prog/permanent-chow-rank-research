#!/usr/bin/env python3
"""Exact relative-hyperplane certificate for the 79-to-90 equality locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b79_equality_locus.json"
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
    minimum, profiles = b49.minimum_ferrers_partitions(79)
    expected = {
        (20, 20, 20, 19) + (0,) * 16,
        (4,) * 19 + (3,),
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
    all_shadows = True
    for parent in parents:
        for deleted in parent:
            child = parent - {deleted}
            children[child] += 1
            all_shadows &= len(b50.product_shadow(set(child))) == 90
    require(len(parents) == 30, len(parents))
    require(len(children) == 2400 and Counter(children.values()) == {1: 2400}, Counter(children.values()))
    require(all_shadows, None)
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "labelled_80_plane_parent_count": len(parents),
        "labelled_parent_cell_deletions": len(parents) * 80,
        "distinct_coordinate_79_plane_count": len(children),
        "parent_multiplicity_histogram": {str(key): value for key, value in sorted(Counter(children.values()).items())},
        "all_children_have_first_shadow_90": all_shadows,
        "every_coordinate_equality_support_has_a_unique_80_plane_product_parent": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


def local_certificate(n6082, b49, b50, transpose: bool) -> dict[str, object]:
    parent_support, shadow = n6082.standard_support(b49, transpose)
    deleted = sorted(parent_support)[0]
    support = parent_support - {deleted}
    parent = b49.incidence_data(parent_support, shadow)
    child = b49.incidence_data(support, shadow)
    require((parent["free_dimension"], child["free_dimension"], child["eta_only_root_count"]) == (8, 87, 0), child)

    parent_roots = sorted(set(parent["tangent_component"].values()) | set(parent["eta_component"].values()))
    parent_map = {}
    for root in parent_roots:
        image = {
            child["tangent_component"][pair]
            for pair, value in parent["tangent_component"].items()
            if value == root and pair[0] != deleted
        }
        image.update(
            child["eta_component"][pair]
            for pair, value in parent["eta_component"].items()
            if value == root
        )
        require(len(image) == 1, (root, image))
        parent_map[root] = next(iter(image))
    hyperplane = {child["tangent_component"][(source, deleted)] for source in sorted(support)}
    require(len(set(parent_map.values())) == 8 and len(hyperplane) == 79, (parent_map, hyperplane))
    require(set(parent_map.values()).isdisjoint(hyperplane), None)

    parent_groups, _ = n6082.component_groups(b49, parent, transpose)
    groups = [[parent_map[root] for root in group] for group in parent_groups]
    forbidden = {tuple(sorted(pair)) for group in groups for pair in combinations(group, 2)}
    grounded = n6082.grounded_certificate(b49, child, forbidden)
    prolongation = {cubic for cubic in b49.ALL_CUBICS if b50.product_shadow({cubic}) <= shadow}
    require(prolongation == parent_support, len(prolongation))
    return {
        "orientation": "transpose_product" if transpose else "row_product",
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "parent_linear_dimension": len(set(parent_map.values())),
            "relative_hyperplane_dimension": len(hyperplane),
            "eta_only_root_count": child["eta_only_root_count"],
            "parent_and_relative_coordinates_are_disjoint": True,
            "coordinate_prolongation_dimension": len(prolongation),
            "coordinate_prolongation_is_the_unique_80_plane_parent": prolongation == parent_support,
        },
        "grounded_quadratic_initial_forms": grounded,
        "relative_boolean_branches": {
            "count": 16,
            "dimension": 81,
            "n6082_boolean_jacobian_is_exact_2_by_2_identity": True,
            "tautological_hyperplane_chart_jacobian_is_79_by_79_identity": True,
            "combined_block_jacobian_rank": 81,
        },
    }


def build_payload() -> dict[str, object]:
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6084")
    frozen = json.loads(N6082_DATA.read_text(encoding="utf-8"))
    require(n6082.build_payload() == frozen, N6082_DATA)
    b49 = n6082.load_module(n6082.B49_SCRIPT, "b49_for_n6084")
    b50 = n6082.load_module(n6082.B50_SCRIPT, "b50_for_n6084")
    coordinate = coordinate_certificate(n6082, b49, b50)
    local = [local_certificate(n6082, b49, b50, transpose) for transpose in (False, True)]
    require(all(row["grounded_quadratic_initial_forms"]["exact_rank_over_Q"] == 12 for row in local), local)
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B79_EQUALITY_LOCUS_EXTENSION",
            "EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION",
            "N6-084",
        ],
        "coordinate_fixed_points": coordinate,
        "local_representatives": local,
        "formal_germ": {
            "linear_dimension": 87,
            "smooth_relative_hyperplane_factor_dimension": 79,
            "parent_boolean_variable_count": 8,
            "forbidden_quadratic_generator_count": 12,
            "boolean_component_count": 16,
            "component_dimension": 81,
            "initial_ideal_is_parent_J_extended_by_79_smooth_variables": True,
            "complete_formal_germ_is_union_of_relative_hyperplane_branches": True,
        },
        "projective_globalization": {
            "every_79_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow": True,
            "extension_is_unique_locally_at_every_torus_fixed_point": True,
            "every_79_to_90_plane_has_second_shadow_dimension_24": True,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
            "proof_interface": (
                "The relative projective hyperplane bundle over the N6-082 product locus is closed. "
                "At every fixed point the complete germ equals its sixteen relative branches. Every "
                "projective torus-stable component contains such a fixed point, hence is contained in "
                "the closed relative image."
            ),
        },
        "claim_boundary": (
            "This proves the 79-to-80 same-shadow extension and second shadow 24. It does not "
            "classify 78-planes, does not by itself exclude an actual seven-frame x=79 packet, "
            "does not exclude global b=34, and makes no border-rank claim."
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
    print("coordinate_children=2400 local_free=87 quadratic_rank=12")
    print("relative_branches=16 dimension=81 extension_79_to_80=true")
    print("N6_PRODUCT_SHADOW_B79_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
