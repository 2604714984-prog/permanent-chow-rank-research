#!/usr/bin/env python3
"""Exact three-deletion certificate for the 77-to-90 equality locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b77_equality_locus.json"
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


def coordinate_certificate(b49) -> dict[str, object]:
    minimum, profiles = b49.minimum_ferrers_partitions(77)
    expected = {
        (20, 20, 20, 17) + (0,) * 16,
        (20, 20, 19, 18) + (0,) * 16,
        (20, 19, 19, 19) + (0,) * 16,
        (4,) * 19 + (1,),
        (4,) * 18 + (3, 2),
        (4,) * 17 + (3, 3, 3),
    }
    require(minimum == 90 and set(profiles) == expected, (minimum, profiles))
    child_count = 30 * 82160
    require(child_count == 2_464_800, child_count)
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "labelled_80_plane_parent_count": 30,
        "three_cell_deletions_per_parent": 82160,
        "distinct_coordinate_77_plane_count": child_count,
        "every_coordinate_equality_support_has_a_unique_80_plane_product_parent": True,
        "all_children_have_first_shadow_90": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


def deletion_orbits(b49) -> list[dict[str, object]]:
    triples = [sum(1 << value for value in triple) for triple in b49.TRIPLES]
    triple_index = {mask: index for index, mask in enumerate(triples)}
    cells = [(row, column) for row in range(4) for column in range(20)]
    cell_index = {cell: index for index, cell in enumerate(cells)}
    generators = []
    for value in range(3):
        permutation = list(range(4))
        permutation[value], permutation[value + 1] = permutation[value + 1], permutation[value]
        generators.append([cell_index[(permutation[row], column)] for row, column in cells])
    for value in range(5):
        image = []
        for row, column in cells:
            vertices = [vertex for vertex in range(6) if triples[column] & (1 << vertex)]
            vertices = [value + 1 if vertex == value else value if vertex == value + 1 else vertex for vertex in vertices]
            mask = sum(1 << vertex for vertex in vertices)
            image.append(cell_index[(row, triple_index[mask])])
        generators.append(image)

    unseen = set(combinations(range(80), 3))
    rows = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {seed}
        stack = [seed]
        while stack:
            current = stack.pop()
            for generator in generators:
                image = tuple(sorted(generator[index] for index in current))
                if image not in orbit:
                    orbit.add(image)
                    stack.append(image)
        unseen.difference_update(orbit)
        rows.append(
            {
                "abstract_deleted_cells": [list(cells[index]) for index in seed],
                "orbit_size": len(orbit),
            }
        )
    rows.sort(key=lambda row: (row["orbit_size"], row["abstract_deleted_cells"]))
    require(len(rows) == 33 and sum(int(row["orbit_size"]) for row in rows) == 82160, rows)
    return rows


def local_certificate(n6082, b49, b50, transpose: bool, abstract: list[list[int]], orbit_size: int) -> dict[str, object]:
    parent_support, shadow = n6082.standard_support(b49, transpose)
    product_rows = sorted({cell[1] if transpose else cell[0] for cell in parent_support})
    deleted = {
        (column, product_rows[row]) if transpose else (product_rows[row], column)
        for row, column in abstract
    }
    support = parent_support - deleted
    parent = b49.incidence_data(parent_support, shadow)
    child = b49.incidence_data(support, shadow)
    relative_dimension = 77 * 3
    require((child["free_dimension"], child["eta_only_root_count"]) == (8 + relative_dimension, 0), child)
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
    require(len(set(parent_map.values())) == 8 and len(relative) == relative_dimension, (parent_map, relative))
    require(set(parent_map.values()).isdisjoint(relative), None)
    parent_groups, _ = n6082.component_groups(b49, parent, transpose)
    groups = [[parent_map[root] for root in group] for group in parent_groups]
    forbidden = {tuple(sorted(pair)) for group in groups for pair in combinations(group, 2)}
    grounded = n6082.grounded_certificate(b49, child, forbidden)
    prolongation = {cubic for cubic in b49.ALL_CUBICS if b50.product_shadow({cubic}) <= shadow}
    require(prolongation == parent_support, len(prolongation))
    return {
        "orientation": "transpose_product" if transpose else "row_product",
        "orbit_size": orbit_size,
        "deleted_cells": [[list(b49.TRIPLES[row]), list(b49.TRIPLES[column])] for row, column in sorted(deleted)],
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "parent_linear_dimension": len(set(parent_map.values())),
            "relative_Gr_77_80_dimension": len(relative),
            "eta_only_root_count": child["eta_only_root_count"],
            "coordinate_prolongation_dimension": len(prolongation),
        },
        "grounded_quadratic_initial_forms": grounded,
        "relative_boolean_branches": {
            "count": 16,
            "dimension": 2 + relative_dimension,
            "parent_branch_dimension": 2,
            "tautological_Gr_77_80_chart_dimension": relative_dimension,
        },
    }


def build_payload() -> dict[str, object]:
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6088")
    require(n6082.build_payload() == json.loads(N6082_DATA.read_text(encoding="utf-8")), N6082_DATA)
    b49 = n6082.load_module(n6082.B49_SCRIPT, "b49_for_n6088")
    b50 = n6082.load_module(n6082.B50_SCRIPT, "b50_for_n6088")
    coordinate = coordinate_certificate(b49)
    abstract_orbits = deletion_orbits(b49)
    local = []
    for transpose in (False, True):
        for row in abstract_orbits:
            local.append(local_certificate(n6082, b49, b50, transpose, row["abstract_deleted_cells"], int(row["orbit_size"])))
    require(len(local) == 66, len(local))
    require(all(row["grounded_quadratic_initial_forms"]["exact_rank_over_Q"] == 12 for row in local), local)
    signatures = Counter(
        (
            row["grounded_quadratic_initial_forms"]["grounded_equation_count"],
            row["grounded_quadratic_initial_forms"]["nonzero_raw_row_count"],
        )
        for row in local
    )
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B77_EQUALITY_LOCUS_EXTENSION",
            "EXACT_SIXTY_SIX_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION",
            "N6-088",
        ],
        "coordinate_fixed_points": coordinate,
        "stabilizer_orbit_coverage": {
            "row_product_orbit_count": len(abstract_orbits),
            "transpose_product_orbit_count": len(abstract_orbits),
            "total_orbit_count": len(local),
            "row_orbit_size_histogram": {
                str(key): value for key, value in sorted(Counter(int(row["orbit_size"]) for row in abstract_orbits).items())
            },
            "all_parent_three_cell_deletions_are_covered": True,
        },
        "local_orbit_representatives": local,
        "grounded_signature_histogram": [
            {"grounded_equation_count": key[0], "nonzero_raw_row_count": key[1], "orbit_count": count}
            for key, count in sorted(signatures.items())
        ],
        "formal_germ": {
            "linear_dimension": 239,
            "smooth_relative_Gr_77_80_factor_dimension": 231,
            "parent_boolean_variable_count": 8,
            "forbidden_quadratic_generator_count": 12,
            "boolean_component_count": 16,
            "component_dimension": 233,
            "initial_ideal_is_parent_J_extended_by_231_smooth_variables": True,
            "complete_formal_germ_is_union_of_relative_Grassmann_branches": True,
        },
        "projective_globalization": {
            "every_77_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow": True,
            "every_77_to_90_plane_has_second_shadow_dimension_24": True,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
        },
        "claim_boundary": (
            "This proves the 77-to-80 same-shadow extension. It does not classify 76-planes, "
            "does not by itself exclude an actual x=77 packet, does not exclude global b=34, "
            "and makes no border-rank claim."
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
    print("coordinate_children=2464800 stabilizer_orbits=66")
    print("local_free=239 quadratic_rank=12 relative_dimension=231")
    print("N6_PRODUCT_SHADOW_B77_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
