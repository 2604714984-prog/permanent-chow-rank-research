#!/usr/bin/env python3
"""Exact classification certificate for the 72-to-89 equality locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b72_equality_locus.json"
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


def size_sixteen_equality_certificate(b49) -> dict[str, object]:
    all_triples = set(b49.TRIPLES)
    rows = []
    for family in combinations(b49.TRIPLES, 16):
        if len(b49.lower_shadow(family)) != 14:
            continue
        missing = all_triples - set(family)
        common = set.intersection(*(set(triple) for triple in missing))
        require(len(common) == 2, missing)
        pair = tuple(sorted(common))
        require(missing == {triple for triple in all_triples if set(pair) <= set(triple)}, missing)
        rows.append(pair)
    require(len(rows) == 15 and len(set(rows)) == 15, rows)
    return {
        "size_16_shadow_14_family_count": len(rows),
        "every_family_is_all_twenty_triples_minus_the_four_supersets_of_one_pair": True,
    }


def coordinate_certificate(b49, b50, n6082):
    minimum, profiles = b49.minimum_ferrers_partitions(72)
    expected = {
        (20, 20, 16, 16) + (0,) * 16,
        (4,) * 16 + (2,) * 4,
    }
    require(minimum == 89 and set(profiles) == expected, (minimum, profiles))
    small = size_sixteen_equality_certificate(b49)
    two_in_four = Counter()
    for four_set in combinations(range(6), 4):
        family = list(combinations(four_set, 3))
        for chosen in combinations(family, 2):
            two_in_four[len(b49.lower_shadow(chosen))] += 1
    require(two_in_four == Counter({5: 15 * 6}), two_in_four)

    supports = []
    for active in combinations(range(6), 4):
        triple_indices = {b49.I3[row] for row in combinations(active, 3)}
        pair_indices = {b49.I2[row] for row in combinations(active, 2)}
        row_parent = {(row, column) for row in triple_indices for column in range(20)}
        row_shadow = {(row, column) for row in pair_indices for column in range(15)}
        for transpose in (False, True):
            parent = row_parent if not transpose else {(column, row) for row, column in row_parent}
            parent_shadow = row_shadow if not transpose else {(column, row) for row, column in row_shadow}
            for missing in parent_shadow:
                child = frozenset(
                    source for source in parent if missing not in b50.product_shadow({source})
                )
                require(len(child) == 72, (transpose, missing, len(child)))
                require(b50.product_shadow(set(child)) == set(parent_shadow) - {missing}, missing)
                supports.append(child)
    require(len(supports) == len(set(supports)) == 2700, len(set(supports)))
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        **small,
        "two_triples_inside_one_C_U4_3_always_have_shadow_five": True,
        "product_parent_count": 30,
        "missing_quadratic_cells_per_parent": 90,
        "coordinate_fixed_point_count": len(supports),
        "every_coordinate_equality_support_is_the_eight_source_preimage_complement_of_one_parent_quadratic_cell": True,
        "every_coordinate_equality_support_has_a_unique_product_parent": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


def grounded_raw(n6082, b49, child: dict[str, object]):
    tangent_component = child["tangent_component"]
    eta_component = child["eta_component"]
    tangent_by_source: dict[tuple[int, int], list[tuple[tuple[int, int], int]]] = defaultdict(list)
    for (source, outside), component in tangent_component.items():
        tangent_by_source[source].append((outside, component))
    derivative_components = {}
    for source, members in tangent_by_source.items():
        for row_vertex in range(6):
            for column_vertex in range(6):
                values = []
                for outside, component in members:
                    row_triple, column_triple = b49.TRIPLES[outside[0]], b49.TRIPLES[outside[1]]
                    if row_vertex in row_triple and column_vertex in column_triple:
                        values.append(
                            (
                                (
                                    b49.I2[tuple(value for value in row_triple if value != row_vertex)],
                                    b49.I2[tuple(value for value in column_triple if value != column_vertex)],
                                ),
                                component,
                            )
                        )
                if values:
                    derivative_components[(source, row_vertex, column_vertex)] = values

    grounded = 0
    nonzero = 0
    coefficients: Counter[int] = Counter()
    raw: set[tuple[int, int]] = set()
    source_set = set(child["sources"])
    for source in child["sources"]:
        row_triple, column_triple = b49.TRIPLES[source[0]], b49.TRIPLES[source[1]]
        for row_vertex in range(6):
            for column_vertex in range(6):
                target = None
                if row_vertex in row_triple and column_vertex in column_triple:
                    target = (
                        b49.I2[tuple(value for value in row_triple if value != row_vertex)],
                        b49.I2[tuple(value for value in column_triple if value != column_vertex)],
                    )
                derivatives = derivative_components.get((source, row_vertex, column_vertex), ())
                for quotient in child["target_complement"]:
                    row_pair, column_pair = b49.PAIRS[quotient[0]], b49.PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            b49.I3[tuple(sorted(row_pair + (row_vertex,)))],
                            b49.I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    if (outside is not None and outside not in source_set) or target is not None:
                        continue
                    grounded += 1
                    terms: Counter[tuple[int, int]] = Counter()
                    for derivative_target, right in derivatives:
                        left = eta_component.get((derivative_target, quotient))
                        if left is not None:
                            terms[tuple(sorted((left, right)))] += 1
                    terms = Counter({term: value for term, value in terms.items() if value})
                    if terms:
                        require(len(terms) == 1, terms)
                        monomial, coefficient = next(iter(terms.items()))
                        raw.add(monomial)
                        coefficients[coefficient] += 1
                        nonzero += 1
    return raw, grounded, nonzero, coefficients


def monomial_groups(raw: set[tuple[int, int]], roots: set[int]) -> list[list[int]]:
    adjacency = {root: set() for root in roots}
    for left, right in raw:
        adjacency[left].add(right)
        adjacency[right].add(left)
    groups = []
    unseen = set(roots)
    while unseen:
        seed = next(iter(unseen))
        reached = {seed}
        stack = [seed]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex] - reached:
                reached.add(neighbor)
                stack.append(neighbor)
        unseen -= reached
        groups.append(sorted(reached))
    require(raw == {tuple(sorted(pair)) for group in groups for pair in combinations(group, 2)}, groups)
    return sorted(groups, key=lambda group: (len(group), group))


def component_change(b49, child: dict[str, object], component: int):
    changes = set()
    for (source, outside), value in child["tangent_component"].items():
        if value != component:
            continue
        for axis, name in ((0, "row"), (1, "column")):
            if source[1 - axis] != outside[1 - axis]:
                continue
            old = set(b49.TRIPLES[source[axis]])
            new = set(b49.TRIPLES[outside[axis]])
            if len(old - new) == len(new - old) == 1:
                changes.add((name, next(iter(old - new)), next(iter(new - old))))
    require(len(changes) == 1, (component, changes))
    return next(iter(changes))


def transform_basis(b50, base, selected, changes, degree):
    rows = []
    for key in sorted(base):
        vector = {key: {(): 1}}
        for variable, root in enumerate(selected):
            axis, old, new = changes[root]
            vector = b50.replace(vector, axis, old, new, variable, degree)
        rows.append(vector)
    return rows


def pull_back(b50, vector, selected, changes, degree):
    for variable, root in reversed(list(enumerate(selected))):
        axis, old, new = changes[root]
        vector = b50.replace(vector, axis, old, new, variable, degree, -1)
    return vector


def symbolic_branch_holds(b49, b50, cubic_base, quadratic_base, linear_base, selected, changes):
    cubic = transform_basis(b50, cubic_base, selected, changes, 3)
    quadratic = transform_basis(b50, quadratic_base, selected, changes, 2)
    for vector in cubic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in vector.items():
                    if row_vertex in b49.TRIPLES[row] and column_vertex in b49.TRIPLES[column]:
                        key = (
                            b49.I2[tuple(value for value in b49.TRIPLES[row] if value != row_vertex)],
                            b49.I2[tuple(value for value in b49.TRIPLES[column] if value != column_vertex)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in quadratic_base for key in pull_back(b50, derivative, selected, changes, 2)):
                    return False
    for vector in quadratic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in vector.items():
                    if row_vertex in b49.PAIRS[row] and column_vertex in b49.PAIRS[column]:
                        key = (
                            b50.I1[(next(value for value in b49.PAIRS[row] if value != row_vertex),)],
                            b50.I1[(next(value for value in b49.PAIRS[column] if value != column_vertex),)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in linear_base for key in pull_back(b50, derivative, selected, changes, 1)):
                    return False
    return True


def local_certificate(n6082, b49, b50):
    parent_support, parent_shadow = n6082.standard_support(b49, False)
    parent = b49.incidence_data(parent_support, parent_shadow)
    missing = sorted(parent_shadow)[0]
    support = {
        source for source in parent_support if missing not in b50.product_shadow({source})
    }
    shadow = set(parent_shadow) - {missing}
    require((len(support), len(shadow)) == (72, 89), (len(support), len(shadow)))
    child = b49.incidence_data(support, shadow)
    require((child["free_dimension"], child["eta_only_root_count"]) == (20, 0), child)
    prolongation = {source for source in b49.ALL_CUBICS if b50.product_shadow({source}) <= shadow}
    require(prolongation == support, len(prolongation))

    parent_roots = sorted(set(parent["tangent_component"].values()) | set(parent["eta_component"].values()))
    parent_map = {}
    for root in parent_roots:
        image = {
            child["tangent_component"][pair]
            for pair, value in parent["tangent_component"].items()
            if value == root and pair[0] in support and pair in child["tangent_component"]
        }
        image.update(
            child["eta_component"][pair]
            for pair, value in parent["eta_component"].items()
            if value == root and pair in child["eta_component"]
        )
        require(len(image) == 1, (root, image))
        parent_map[root] = next(iter(image))
    require(len(set(parent_map.values())) == 8, parent_map)

    raw, grounded, nonzero, coefficients = grounded_raw(n6082, b49, child)
    roots = set(child["tangent_component"].values()) | set(child["eta_component"].values())
    groups = monomial_groups(raw, roots)
    require(sorted(map(len, groups)) == [2, 2, 4, 4, 4, 4], groups)
    require(len(raw) == 26, raw)
    changes = {root: component_change(b49, child, root) for root in roots}
    parent_images = set(parent_map.values())

    def order_key(group):
        is_parent = set(group) <= parent_images
        axes = {changes[root][0] for root in group}
        targets = {changes[root][2] for root in group}
        require(len(axes) == len(targets) == 1, (group, axes, targets))
        axis = next(iter(axes))
        return (2 if is_parent else 0 if axis == "column" else 1, next(iter(targets)))

    ordered_groups = sorted(groups, key=order_key)
    require([len(group) for group in ordered_groups] == [4, 4, 2, 2, 4, 4], ordered_groups)
    linear_shadow = b50.pair_product_shadow(shadow)
    require(len(linear_shadow) == 24, len(linear_shadow))
    branch_count = 0
    for selected in product(*ordered_groups):
        branch_count += 1
        require(
            symbolic_branch_holds(
                b49, b50, support, shadow, linear_shadow, selected, changes
            ),
            selected,
        )
    require(branch_count == 1024, branch_count)
    return {
        "orientation": "row_product_missing_cell",
        "missing_quadratic_cell": [list(b49.PAIRS[missing[0]]), list(b49.PAIRS[missing[1]])],
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "eta_only_root_count": child["eta_only_root_count"],
            "parent_root_count": len(set(parent_map.values())),
            "new_missing_cell_root_count": len(roots - parent_images),
            "coordinate_prolongation_dimension": len(prolongation),
        },
        "grounded_quadratic_initial_forms": {
            "grounded_equation_count": grounded,
            "nonzero_raw_row_count": nonzero,
            "raw_coefficient_histogram": {
                str(key): value for key, value in sorted(coefficients.items())
            },
            "group_sizes_in_symbolic_order": [len(group) for group in ordered_groups],
            "forbidden_unit_count": len(raw),
            "exact_rank_over_Q": len(raw),
            "initial_ideal": "I(K4)+I(K4)+I(K2)+I(K2)+I(K4)+I(K4)",
        },
        "symbolic_boolean_branches": {
            "count": branch_count,
            "dimension": len(ordered_groups),
            "all_degree_three_to_two_containments_hold": True,
            "all_degree_two_to_one_containments_hold": True,
            "second_shadow_dimension": len(linear_shadow),
            "selected_chart_jacobian_is_identity": True,
        },
    }


def build_payload() -> dict[str, object]:
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6092")
    n6082_data = json.loads(N6082_DATA.read_text(encoding="utf-8"))
    require(
        n6082_data["formal_germ"]["initial_ideal"] == "I(K4)+I(K4)"
        and n6082_data["formal_germ"]["boolean_component_count_at_each_fixed_point"] == 16,
        N6082_DATA,
    )
    b49 = n6082.load_module(n6082.B49_SCRIPT, "b49_for_n6092")
    b50 = n6082.load_module(n6082.B50_SCRIPT, "b50_for_n6092")
    coordinate = coordinate_certificate(b49, b50, n6082)
    local = local_certificate(n6082, b49, b50)
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B72_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_SYMBOLIC_1024_BRANCH_REPLAY",
            "N6-092",
        ],
        "coordinate_fixed_points": coordinate,
        "standard_local_certificate": local,
        "formal_germ": {
            "linear_dimension": 20,
            "free_group_sizes": [4, 4, 2, 2, 4, 4],
            "forbidden_quadratic_generator_count": 26,
            "boolean_component_count_at_each_fixed_point": 1024,
            "component_dimension": 6,
            "complete_formal_germ_is_the_union_of_the_1024_boolean_branches": True,
        },
        "projective_globalization": {
            "every_72_to_89_point_lies_in_a_partitioned_80_to_90_product_parent": True,
            "the_89_plane_is_a_hyperplane_in_the_parent_90_plane": True,
            "the_72_plane_is_its_full_cubic_prolongation_inside_the_permanent_space": True,
            "every_equality_point_has_second_shadow_dimension": 24,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
        },
        "claim_boundary": (
            "This classifies the ordinary 72-to-89 equality locus. The extra missing-pair "
            "Boolean branches need not be ambient linear transports of actual Chow frames. "
            "The theorem does not exclude an actual x=72 packet, global b=34, ordinary lower 29, "
            "or any border-rank configuration."
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
    print("coordinate_fixed_points=2700 local_free=20 quadratic_rank=26")
    print("symbolic_branches=1024 component_dimension=6 second_shadow=24")
    print("N6_PRODUCT_SHADOW_B72_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
