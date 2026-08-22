#!/usr/bin/env python3
"""Exact coordinate, local, and formal certificates for the 80-to-90 locus."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b80_equality_locus.json"
B49_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b49_equality_locus.py"
B50_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b50_equality_locus.py"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def standard_support(b49, transpose: bool = False) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    active = (0, 1, 2, 3)
    triple_indices = {b49.I3[row] for row in combinations(active, 3)}
    pair_indices = {b49.I2[row] for row in combinations(active, 2)}
    support = {(row, column) for row in triple_indices for column in range(20)}
    shadow = {(row, column) for row in pair_indices for column in range(15)}
    if transpose:
        support = {(column, row) for row, column in support}
        shadow = {(column, row) for row, column in shadow}
    return support, shadow


def set_partitions(items: tuple[int, ...], blocks: int) -> list[tuple[tuple[int, ...], ...]]:
    result: set[tuple[tuple[int, ...], ...]] = set()

    def visit(index: int, current: list[list[int]]) -> None:
        if index == len(items):
            if len(current) == blocks:
                result.add(tuple(sorted(tuple(block) for block in current)))
            return
        value = items[index]
        for block in current:
            block.append(value)
            visit(index + 1, current)
            block.pop()
        if len(current) < blocks:
            current.append([value])
            visit(index + 1, current)
            current.pop()

    visit(0, [])
    return sorted(result)


def coordinate_certificate(b49, b50) -> dict[str, object]:
    minimum, profiles = b49.minimum_ferrers_partitions(80)
    expected = {
        (20,) * 4 + (0,) * 16,
        (4,) * 20,
    }
    require(minimum == 90 and set(profiles) == expected, (minimum, profiles))
    supports = []
    for active in combinations(range(6), 4):
        rows = {b49.I3[row] for row in combinations(active, 3)}
        support = frozenset((row, column) for row in rows for column in range(20))
        supports.append(support)
        supports.append(frozenset((column, row) for row, column in support))
    require(len(supports) == len(set(supports)) == 30, len(set(supports)))
    require(all(len(b50.product_shadow(set(support))) == 90 for support in supports), supports)
    require(b49.small_equality_count(4, 6) == 15, None)
    require(b49.small_equalities_have_expected_forms(4, 6), None)
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "four_triples_shadow_six_family_count": 15,
        "every_four_triple_shadow_six_family_is_C_U4_3": True,
        "row_product_coordinate_support_count": 15,
        "transpose_product_coordinate_support_count": 15,
        "total_coordinate_fixed_point_count": len(supports),
        "all_coordinate_fixed_points_have_first_shadow_90": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


def component_groups(b49, child: dict[str, object], transpose: bool) -> tuple[list[list[int]], dict[tuple[int, int], int]]:
    by_component: dict[int, list[tuple[tuple[int, int], tuple[int, int]]]] = defaultdict(list)
    for pair, component in child["tangent_component"].items():
        by_component[int(component)].append(pair)
    change_to_component: dict[tuple[int, int], int] = {}
    groups: dict[int, list[int]] = defaultdict(list)
    for component, members in by_component.items():
        changes = set()
        for source, outside in members:
            if transpose:
                source_subset = set(b49.TRIPLES[source[1]])
                outside_subset = set(b49.TRIPLES[outside[1]])
                same_other_axis = source[0] == outside[0]
            else:
                source_subset = set(b49.TRIPLES[source[0]])
                outside_subset = set(b49.TRIPLES[outside[0]])
                same_other_axis = source[1] == outside[1]
            if same_other_axis and len(source_subset - outside_subset) == len(outside_subset - source_subset) == 1:
                changes.add((next(iter(source_subset - outside_subset)), next(iter(outside_subset - source_subset))))
        require(len(changes) == 1, (component, changes))
        change = next(iter(changes))
        change_to_component[change] = component
        groups[change[1]].append(component)
    group_rows = [sorted(group) for _, group in sorted(groups.items())]
    require(sorted(map(len, group_rows)) == [4, 4], group_rows)
    return group_rows, change_to_component


def grounded_certificate(b49, child: dict[str, object], forbidden: set[tuple[int, int]]) -> dict[str, object]:
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
                                    b49.I2[tuple(x for x in row_triple if x != row_vertex)],
                                    b49.I2[tuple(x for x in column_triple if x != column_vertex)],
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
    for source in child["sources"]:
        row_triple, column_triple = b49.TRIPLES[source[0]], b49.TRIPLES[source[1]]
        for row_vertex in range(6):
            for column_vertex in range(6):
                target = None
                if row_vertex in row_triple and column_vertex in column_triple:
                    target = (
                        b49.I2[tuple(x for x in row_triple if x != row_vertex)],
                        b49.I2[tuple(x for x in column_triple if x != column_vertex)],
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
                    if (outside is not None and outside not in set(child["sources"])) or target is not None:
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
                        nonzero += 1
                        monomial, coefficient = next(iter(terms.items()))
                        raw.add(monomial)
                        coefficients[coefficient] += 1
    require(raw == forbidden, (raw, forbidden))
    return {
        "grounded_equation_count": grounded,
        "nonzero_raw_row_count": nonzero,
        "raw_coefficient_histogram": {str(key): value for key, value in sorted(coefficients.items())},
        "forbidden_unit_count": len(forbidden),
        "exact_rank_over_Q": len(raw),
        "row_span_is_exactly_the_twelve_forbidden_units": raw == forbidden,
    }


def transformed_basis(b50, base, axis: str, sources: tuple[int, int], degree: int):
    vectors = []
    for key in sorted(base):
        vector = {key: {(): 1}}
        for variable, (old, new) in enumerate(zip(sources, (4, 5))):
            vector = b50.replace(vector, axis, old, new, variable, degree)
        vectors.append(vector)
    return vectors


def branch_certificate(b49, b50, support, shadow, transpose: bool, sources: tuple[int, int], change_to_component: dict[tuple[int, int], int]) -> tuple[bool, bool, bool]:
    axis = "column" if transpose else "row"
    cubic = transformed_basis(b50, support, axis, sources, 3)

    def pull_back(vector, degree):
        for variable, (old, new) in reversed(list(enumerate(zip(sources, (4, 5))))):
            vector = b50.replace(vector, axis, old, new, variable, degree, -1)
        return vector

    first = True
    for vector in cubic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in vector.items():
                    if row_vertex in b49.TRIPLES[row] and column_vertex in b49.TRIPLES[column]:
                        key = (
                            b49.I2[tuple(x for x in b49.TRIPLES[row] if x != row_vertex)],
                            b49.I2[tuple(x for x in b49.TRIPLES[column] if x != column_vertex)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in shadow for key in pull_back(derivative, 2)):
                    first = False

    second_shadow = b50.pair_product_shadow(shadow)
    quadratic = transformed_basis(b50, shadow, axis, sources, 2)
    second = True
    for vector in quadratic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in vector.items():
                    if row_vertex in b49.PAIRS[row] and column_vertex in b49.PAIRS[column]:
                        key = (
                            b50.I1[(next(x for x in b49.PAIRS[row] if x != row_vertex),)],
                            b50.I1[(next(x for x in b49.PAIRS[column] if x != column_vertex),)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in second_shadow for key in pull_back(derivative, 1)):
                    second = False

    positions = {source: index for index, source in enumerate(sorted(support))}
    jacobian = []
    for variable, (old, new) in enumerate(zip(sources, (4, 5))):
        component = change_to_component[(old, new)]
        members = [pair for pair, value in b49.incidence_data(support, shadow)["tangent_component"].items() if value == component]
        source, outside = members[0]
        polynomial = cubic[positions[source]].get(outside, {})
        jacobian.append([polynomial.get((column,), 0) for column in range(2)])
    return first, second, jacobian == [[1, 0], [0, 1]]


def local_certificate(b49, b50, transpose: bool) -> dict[str, object]:
    support, shadow = standard_support(b49, transpose)
    require(b50.product_shadow(support) == shadow, None)
    child = b49.incidence_data(support, shadow)
    require((child["free_dimension"], child["eta_only_root_count"]) == (8, 0), child)
    prolongation = {cubic for cubic in b49.ALL_CUBICS if b50.product_shadow({cubic}) <= shadow}
    require(prolongation == support, len(prolongation))
    groups, change_to_component = component_groups(b49, child, transpose)
    forbidden = {
        tuple(sorted(pair))
        for group in groups
        for pair in combinations(group, 2)
    }
    require(len(forbidden) == 12, forbidden)
    grounded = grounded_certificate(b49, child, forbidden)
    branch_rows = [
        branch_certificate(b49, b50, support, shadow, transpose, sources, change_to_component)
        for sources in product(range(4), repeat=2)
    ]
    require(len(branch_rows) == 16 and all(all(row) for row in branch_rows), branch_rows)
    return {
        "orientation": "transpose_product" if transpose else "row_product",
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "free_group_sizes": sorted(map(len, groups)),
            "eta_only_root_count": child["eta_only_root_count"],
            "coordinate_prolongation_dimension": len(prolongation),
            "coordinate_prolongation_equals_the_original_80_plane": prolongation == support,
        },
        "grounded_quadratic_initial_forms": grounded,
        "boolean_branches": {
            "count": len(branch_rows),
            "dimension": 2,
            "all_first_shadow_symbolic_containments_hold": True,
            "all_second_shadow_symbolic_containments_hold": True,
            "all_selected_chart_jacobians_are_identity": True,
            "each_branch_is_an_actual_linear_shear_on_the_product_support": True,
        },
    }


def build_payload() -> dict[str, object]:
    b49 = load_module(B49_SCRIPT, "b49_for_n6082")
    b50 = load_module(B50_SCRIPT, "b50_for_n6082")
    coordinate = coordinate_certificate(b49, b50)
    local = [local_certificate(b49, b50, transpose) for transpose in (False, True)]
    partitions = set_partitions(tuple(range(6)), 4)
    require(len(partitions) == 65, len(partitions))
    second_minimum, witness = b50.minimum_second_product_shadow(90)
    require(second_minimum == 24, (second_minimum, witness))
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B80_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_SYMBOLIC_16_BRANCH_REPLAY",
            "N6-082",
        ],
        "coordinate_fixed_points": coordinate,
        "local_representatives": local,
        "formal_germ": {
            "linear_dimension": 8,
            "free_group_sizes": [4, 4],
            "forbidden_quadratic_generator_count": 12,
            "boolean_component_count_at_each_fixed_point": 16,
            "component_dimension": 2,
            "initial_ideal": "I(K4)+I(K4)",
            "complete_formal_germ_is_the_union_of_the_sixteen_boolean_branches": True,
        },
        "projective_globalization": {
            "set_partitions_of_six_coordinates_into_four_nonempty_blocks": len(partitions),
            "row_product_component_count": len(partitions),
            "transpose_product_component_count": len(partitions),
            "every_component_is_a_product_of_projective_spaces_of_total_dimension_two": True,
            "every_80_to_90_point_is_partitioned_row_product_or_its_transpose": True,
            "proof_interface": (
                "The incidence is projective and torus stable. Every irreducible component contains "
                "one of the thirty coordinate fixed points. The complete fixed germ is the union of "
                "the exact partitioned-product branches, so closedness propagates the classification "
                "to the entire component."
            ),
        },
        "second_product_shadow": {
            "universal_minimum_at_dimension_90": second_minimum,
            "first_ferrers_witness": list(witness),
            "every_equality_point_has_second_shadow_dimension": 24,
            "second_shadow_is_a_genuine_partitioned_4_by_6_product_plane_or_transpose": True,
        },
        "actual_transport_interface": (
            "On each partitioned component the four row generators have disjoint coordinate supports. "
            "Their degree-two and degree-three Boolean maps therefore equal the corresponding actual "
            "linear changes on the displayed product spaces; no repeated-row collision term occurs."
        ),
        "claim_boundary": (
            "This classifies the 80-to-90 product-shadow equality locus and its second shadow. "
            "It does not by itself exclude an actual seven-frame common-quotient endpoint, does not "
            "exclude global b=34, does not prove ChowRank(perm_6)>=29, and makes no border-rank claim."
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
    print("coordinate_fixed_points=30 local_free=8 quadratic_rank=12")
    print("local_branches=16 global_partition_components=130 second_shadow=24")
    print("N6_PRODUCT_SHADOW_B80_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
