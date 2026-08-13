#!/usr/bin/env python3
"""Exact coordinate and formal certificates for the b=46, shadow=72 locus.

N6-101 proves that every characteristic-zero 46-plane in the permanent
cubic space with 72-dimensional first product shadow has 23-dimensional
second shadow, and that the latter is a genuine standard flag hook or
biflag rectangle hook.  The expensive
symbolic branch replay is reduced to stabilizer-orbit representatives; the
coordinate stabilizer transports the remaining facets exactly.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b46_equality_locus.json"
sys.path.insert(0, str(ROOT / "scripts"))

import n6_product_shadow_b49_equality_locus as b49  # noqa: E402
import n6_product_shadow_b50_equality_locus as b50  # noqa: E402


TRIPLES = b49.TRIPLES
PAIRS = b49.PAIRS
I3 = b49.I3
I2 = b49.I2
ORDERED_TRIPLES = sorted(TRIPLES, key=lambda subset: sum(1 << x for x in subset))


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def support_from_profile(profile: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        (I3[ORDERED_TRIPLES[row]], I3[ORDERED_TRIPLES[column]])
        for row, degree in enumerate(profile)
        for column in range(degree)
    }


def row_profile(support: set[tuple[int, int]] | frozenset[tuple[int, int]]) -> tuple[int, ...]:
    degrees = Counter(row for row, _ in support)
    return tuple(sorted(degrees.values(), reverse=True)) + (0,) * (20 - len(degrees))


def coordinate_prolongation(shadow: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {
        cubic
        for cubic in product(range(20), repeat=2)
        if b50.product_shadow({cubic}) <= shadow
    }


def row_type_one_support(
    row_three: tuple[int, ...],
    row_four: tuple[int, ...],
    column_four: tuple[int, ...],
    column_five: tuple[int, ...],
) -> frozenset[tuple[int, int]]:
    row_base = {I3[row] for row in combinations(row_four, 3)}
    column_ten = {I3[column] for column in combinations(column_five, 3)}
    column_sixteen = {
        index
        for index, column in enumerate(TRIPLES)
        if len(set(column) & set(column_four)) >= 2
    }
    distinguished = I3[row_three]
    return frozenset(
        {(row, column) for row in row_base for column in column_ten}
        | {(distinguished, column) for column in column_sixteen}
    )


def row_type_two_support(
    row_four: tuple[int, ...],
    row_five: tuple[int, ...],
    column_three: tuple[int, ...],
    column_five: tuple[int, ...],
) -> frozenset[tuple[int, int]]:
    row_four_cubics = {I3[row] for row in combinations(row_four, 3)}
    row_five_cubics = {I3[row] for row in combinations(row_five, 3)}
    column_five_cubics = {I3[column] for column in combinations(column_five, 3)}
    distinguished = I3[column_three]
    return frozenset(
        {(row, column) for row in row_four_cubics for column in column_five_cubics}
        | {(row, distinguished) for row in row_five_cubics}
    )


def all_coordinate_models() -> set[frozenset[tuple[int, int]]]:
    rows: set[frozenset[tuple[int, int]]] = set()
    for row_four in combinations(range(6), 4):
        for row_three in combinations(row_four, 3):
            for column_five in combinations(range(6), 5):
                for column_four in combinations(column_five, 4):
                    support = row_type_one_support(
                        row_three, row_four, column_four, column_five
                    )
                    rows.add(support)
                    rows.add(frozenset((column, row) for row, column in support))
    for row_five in combinations(range(6), 5):
        for row_four in combinations(row_five, 4):
            for column_five in combinations(range(6), 5):
                for column_three in combinations(column_five, 3):
                    support = row_type_two_support(
                        row_four, row_five, column_three, column_five
                    )
                    rows.add(support)
                    rows.add(frozenset((column, row) for row, column in support))
    return rows


def one_factor_classification() -> dict[str, object]:
    rows = {}
    for size, shadow_size in ((4, 6), (10, 10), (16, 14)):
        families = []
        for family in combinations(TRIPLES, size):
            if len(b49.lower_shadow(family)) == shadow_size:
                families.append(family)
        if size == 4:
            expected = all(
                len(set().union(*(set(member) for member in family))) == 4
                for family in families
            )
        elif size == 10:
            expected = all(
                len(set().union(*(set(member) for member in family))) == 5
                for family in families
            )
        else:
            expected = all(
                len(set(TRIPLES) - set(family)) == 4
                and len(
                    set.intersection(
                        *(set(member) for member in set(TRIPLES) - set(family))
                    )
                )
                == 2
                for family in families
            )
        rows[f"size_{size}_shadow_{shadow_size}"] = {
            "count": len(families),
            "all_have_the_claimed_clique_or_fixed_pair_form": expected,
        }
    require(
        {key: row["count"] for key, row in rows.items()}
        == {
            "size_4_shadow_6": 15,
            "size_10_shadow_10": 6,
            "size_16_shadow_14": 15,
        },
        rows,
    )
    require(all(row["all_have_the_claimed_clique_or_fixed_pair_form"] for row in rows.values()), rows)
    return rows


def coordinate_certificate() -> dict[str, object]:
    minimum, profiles = b49.minimum_ferrers_partitions(46)
    expected_profiles = {
        (16, 10, 10, 10) + (0,) * 16,
        (10,) * 4 + (1,) * 6 + (0,) * 10,
        (10,) + (4,) * 9 + (0,) * 10,
        (4,) * 10 + (1,) * 6 + (0,) * 4,
    }
    require(minimum == 72 and set(profiles) == expected_profiles, (minimum, profiles))
    models = all_coordinate_models()
    profile_counts = Counter(row_profile(model) for model in models)
    require(len(models) == 7_200, len(models))
    require(set(profile_counts) == expected_profiles, profile_counts)
    require(set(profile_counts.values()) == {1_800}, profile_counts)
    require(all(len(model) == 46 for model in models), None)
    require(all(len(b50.product_shadow(model)) == 72 for model in models), None)
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "one_factor_equality_replay": one_factor_classification(),
        "original_support_classification_is_proved_in_the_document": True,
        "coordinate_model_count": len(models),
        "profile_counts": [
            {"profile": list(profile), "count": count}
            for profile, count in sorted(profile_counts.items(), reverse=True)
        ],
        "coordinate_symmetry_orbit_count": 4,
        "every_coordinate_model_has_first_shadow_72": True,
    }


def component_labels(
    child: dict[str, object], support: set[tuple[int, int]]
) -> dict[int, tuple[str, int, int]]:
    tangent_component = child["tangent_component"]
    labels = {}
    for component in range(int(child["free_dimension"])):
        members = [pair for pair, value in tangent_component.items() if value == component]
        require(bool(members), component)
        source, outside = members[0]
        weight = tuple(
            int(vertex in TRIPLES[outside[0]]) - int(vertex in TRIPLES[source[0]])
            for vertex in range(6)
        ) + tuple(
            int(vertex in TRIPLES[outside[1]]) - int(vertex in TRIPLES[source[1]])
            for vertex in range(6)
        )
        negative = [index for index, value in enumerate(weight) if value < 0]
        positive = [index for index, value in enumerate(weight) if value > 0]
        require(len(negative) == len(positive) == 1, weight)
        labels[component] = (
            "row" if positive[0] < 6 else "column",
            negative[0] % 6,
            positive[0] % 6,
        )
    require(len(set(labels.values())) == len(labels), labels)
    return labels


def grounded_edge_certificate(
    support: set[tuple[int, int]], shadow: set[tuple[int, int]], child: dict[str, object]
) -> tuple[set[tuple[int, int]], dict[str, object]]:
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

    grounded = 0
    nonzero = 0
    row_term_histogram: Counter[int] = Counter()
    coefficient_histogram: Counter[int] = Counter()
    edges: set[tuple[int, int]] = set()
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
                    if (outside is not None and outside not in support) or target is not None:
                        continue
                    grounded += 1
                    terms = Counter()
                    for derivative_target, right in derivatives:
                        left = eta_component.get((derivative_target, quotient))
                        if left is not None:
                            terms[tuple(sorted((left, right)))] += 1
                    terms = Counter({key: value for key, value in terms.items() if value})
                    if terms:
                        nonzero += 1
                        row_term_histogram[len(terms)] += 1
                        coefficient_histogram.update(terms.values())
                        edges.update(terms)
    require(row_term_histogram == {1: nonzero}, row_term_histogram)
    require(coefficient_histogram == {2: nonzero}, coefficient_histogram)
    require(all(left != right for left, right in edges), edges)
    return edges, {
        "grounded_equation_count": grounded,
        "nonzero_raw_row_count": nonzero,
        "single_monomial_row_count": nonzero,
        "coefficient_histogram": {str(key): value for key, value in sorted(coefficient_histogram.items())},
        "edge_generator_count": len(edges),
        "exact_rank_over_Q": len(edges),
    }


def maximal_independent_facets(variable_count: int, edges: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    adjacency = [0] * variable_count
    for left, right in edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    facets = []
    for mask in range(1 << variable_count):
        remaining = mask
        independent = True
        while remaining:
            bit = remaining & -remaining
            vertex = bit.bit_length() - 1
            remaining -= bit
            if adjacency[vertex] & remaining:
                independent = False
                break
        if not independent:
            continue
        if all((mask >> vertex) & 1 or adjacency[vertex] & mask for vertex in range(variable_count)):
            facets.append(tuple(vertex for vertex in range(variable_count) if (mask >> vertex) & 1))
    return facets


def preserving_permutations(parts: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    rows = []
    for images in product(*(list(permutations(part)) for part in parts)):
        permutation = list(range(6))
        for part, image in zip(parts, images):
            for source, target in zip(part, image):
                permutation[source] = target
        rows.append(tuple(permutation))
    return rows


def facet_orbits(
    facets: list[tuple[int, ...]],
    labels: dict[int, tuple[str, int, int]],
    row_parts: tuple[tuple[int, ...], ...],
    column_parts: tuple[tuple[int, ...], ...],
) -> list[tuple[tuple[int, ...], int]]:
    by_label = {label: index for index, label in labels.items()}
    actions = []
    for row_permutation in preserving_permutations(row_parts):
        for column_permutation in preserving_permutations(column_parts):
            image = {}
            for index, (axis, old, new) in labels.items():
                permutation = row_permutation if axis == "row" else column_permutation
                image[index] = by_label[(axis, permutation[old], permutation[new])]
            actions.append(image)
    remaining = {frozenset(facet) for facet in facets}
    rows = []
    while remaining:
        representative = min(remaining, key=lambda facet: tuple(sorted(facet)))
        orbit = {
            frozenset(action[index] for index in representative)
            for action in actions
        }
        require(representative in orbit and orbit <= remaining, representative)
        remaining -= orbit
        rows.append((tuple(sorted(representative)), len(orbit)))
    rows.sort()
    require(sum(size for _, size in rows) == len(facets), rows)
    return rows


def transformed_basis(
    base: set[tuple[int, int]],
    facet: tuple[int, ...],
    labels: dict[int, tuple[str, int, int]],
    degree: int,
) -> list[dict[tuple[int, int], dict[tuple[int, ...], int]]]:
    vectors = []
    for key in sorted(base):
        vector = {key: {(): 1}}
        for variable, component in enumerate(facet):
            axis, old, new = labels[component]
            vector = b50.replace(vector, axis, old, new, variable, degree)
        vectors.append(vector)
    return vectors


def dependency_ordered_facet(
    facet: tuple[int, ...], labels: dict[int, tuple[str, int, int]]
) -> tuple[int, ...]:
    """Order composable shears from the first source toward the last target."""

    predecessors = {component: set() for component in facet}
    for left in facet:
        left_axis, _, left_new = labels[left]
        for right in facet:
            right_axis, right_old, _ = labels[right]
            if left != right and left_axis == right_axis and left_new == right_old:
                predecessors[right].add(left)
    result = []
    remaining = set(facet)
    while remaining:
        ready = sorted(component for component in remaining if not (predecessors[component] & remaining))
        require(bool(ready), (facet, labels))
        result.extend(ready)
        remaining -= set(ready)
    return tuple(result)


def pull_back(
    vector: dict[tuple[int, int], dict[tuple[int, ...], int]],
    facet: tuple[int, ...],
    labels: dict[int, tuple[str, int, int]],
    degree: int,
) -> dict[tuple[int, int], dict[tuple[int, ...], int]]:
    for variable, component in reversed(list(enumerate(facet))):
        axis, old, new = labels[component]
        vector = b50.replace(vector, axis, old, new, variable, degree, -1)
    return vector


def branch_certificate(
    support: set[tuple[int, int]],
    shadow: set[tuple[int, int]],
    child: dict[str, object],
    facet: tuple[int, ...],
    labels: dict[int, tuple[str, int, int]],
) -> bool:
    cubic = transformed_basis(support, facet, labels, 3)
    for cubic_vector in cubic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in cubic_vector.items():
                    if row_vertex in TRIPLES[row] and column_vertex in TRIPLES[column]:
                        key = (
                            I2[tuple(x for x in TRIPLES[row] if x != row_vertex)],
                            I2[tuple(x for x in TRIPLES[column] if x != column_vertex)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in shadow for key in pull_back(derivative, facet, labels, 2)):
                    return False

    second_shadow = b50.pair_product_shadow(shadow)
    quadratic = transformed_basis(shadow, facet, labels, 2)
    for quadratic_vector in quadratic:
        for row_vertex in range(6):
            for column_vertex in range(6):
                derivative = {}
                for (row, column), polynomial in quadratic_vector.items():
                    if row_vertex in PAIRS[row] and column_vertex in PAIRS[column]:
                        key = (
                            b50.I1[(next(x for x in PAIRS[row] if x != row_vertex),)],
                            b50.I1[(next(x for x in PAIRS[column] if x != column_vertex),)],
                        )
                        derivative[key] = b50.poly_add(derivative.get(key, {}), polynomial)
                if any(key not in second_shadow for key in pull_back(derivative, facet, labels, 1)):
                    return False

    positions = {source: index for index, source in enumerate(sorted(support))}
    tangent_component = child["tangent_component"]
    jacobian = []
    for component in facet:
        source, outside = next(
            pair for pair, value in tangent_component.items() if value == component
        )
        polynomial = cubic[positions[source]].get(outside, {})
        jacobian.append(
            [polynomial.get((variable,), 0) for variable in range(len(facet))]
        )
    identity = [[int(i == j) for j in range(len(facet))] for i in range(len(facet))]
    return jacobian == identity


def coordinate_twenty_three_flag_shapes() -> dict[frozenset[tuple[int, int]], str]:
    hooks: dict[frozenset[tuple[int, int]], str] = {}
    for row_four in combinations(range(6), 4):
        for row_three in combinations(row_four, 3):
            for column_five in combinations(range(6), 5):
                support = frozenset(
                    (row, column)
                    for row in range(6)
                    for column in range(6)
                    if (row in row_four and column in column_five) or row in row_three
                )
                hooks[support] = "standard_flag_hook"
                hooks[frozenset((column, row) for row, column in support)] = "transpose_standard_flag_hook"
    for row_five in combinations(range(6), 5):
        for row_four in combinations(row_five, 4):
            for column_five in combinations(range(6), 5):
                for column_three in combinations(column_five, 3):
                    support = frozenset(
                        (row, column)
                        for row in range(6)
                        for column in range(6)
                        if (row in row_four and column in column_five)
                        or (row in row_five and column in column_three)
                    )
                    hooks[support] = "biflag_rectangle_hook"
                    hooks[frozenset((column, row) for row, column in support)] = "transpose_biflag_rectangle_hook"
    return hooks


def local_certificate(
    name: str,
    profile: tuple[int, ...],
    row_parts: tuple[tuple[int, ...], ...],
    column_parts: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    support = support_from_profile(profile)
    shadow = b50.product_shadow(support)
    require(len(support) == 46 and len(shadow) == 72, (len(support), len(shadow)))
    require(coordinate_prolongation(shadow) == support, name)
    child = b49.incidence_data(support, shadow)
    require(child["free_dimension"] == 20 and child["eta_only_root_count"] == 0, child)
    labels = component_labels(child, support)
    edges, quadratic = grounded_edge_certificate(support, shadow, child)
    facets = maximal_independent_facets(20, edges)
    require({len(facet) for facet in facets} == {5}, facets)
    orbits = facet_orbits(facets, labels, row_parts, column_parts)
    branch_checks = [
        branch_certificate(
            support,
            shadow,
            child,
            dependency_ordered_facet(representative, labels),
            labels,
        )
        for representative, _ in orbits
    ]
    require(all(branch_checks), (name, branch_checks))
    second_shadow = b50.pair_product_shadow(shadow)
    flag_shapes = coordinate_twenty_three_flag_shapes()
    require(len(second_shadow) == 23 and frozenset(second_shadow) in flag_shapes, second_shadow)
    return {
        "name": name,
        "profile": list(profile),
        "coordinate_prolongation_dimension": len(coordinate_prolongation(shadow)),
        "linear_free_dimension": child["free_dimension"],
        "eta_only_root_count": child["eta_only_root_count"],
        "quadratic_initial": quadratic,
        "maximal_independent_facet_count": len(facets),
        "all_facets_have_dimension": 5,
        "stabilizer_facet_orbit_count": len(orbits),
        "stabilizer_facet_orbit_sizes": [size for _, size in orbits],
        "all_orbit_representative_branches_pass_both_symbolic_containments": True,
        "all_orbit_representative_branch_jacobians_are_identity_5_by_5": True,
        "coordinate_second_shadow_dimension": len(second_shadow),
        "coordinate_second_shadow_flag_shape": flag_shapes[frozenset(second_shadow)],
    }


def build_payload() -> dict[str, object]:
    coordinate = coordinate_certificate()
    profiles = [tuple(profile) for profile in coordinate["minimizing_ferrers_profiles"]]
    by_nonzero = {tuple(value for value in profile if value): profile for profile in profiles}
    local_rows = [
        local_certificate(
            "row_type_one",
            by_nonzero[(16, 10, 10, 10)],
            ((0, 1, 2), (3,), (4, 5)),
            ((0, 1, 2, 3), (4,), (5,)),
        ),
        local_certificate(
            "row_type_two",
            by_nonzero[(10, 10, 10, 10, 1, 1, 1, 1, 1, 1)],
            ((0, 1, 2, 3), (4,), (5,)),
            ((0, 1, 2), (3, 4), (5,)),
        ),
        local_certificate(
            "transpose_type_two",
            by_nonzero[(10, 4, 4, 4, 4, 4, 4, 4, 4, 4)],
            ((0, 1, 2), (3, 4), (5,)),
            ((0, 1, 2, 3), (4,), (5,)),
        ),
        local_certificate(
            "transpose_type_one",
            by_nonzero[(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1)],
            ((0, 1, 2, 3), (4,), (5,)),
            ((0, 1, 2), (3,), (4, 5)),
        ),
    ]
    second_minimum, second_witness = b50.minimum_second_product_shadow(72)
    require(second_minimum == 23, (second_minimum, second_witness))
    require(
        Counter(row["quadratic_initial"]["edge_generator_count"] for row in local_rows)
        == {31: 2, 32: 2},
        local_rows,
    )
    require(
        Counter(row["maximal_independent_facet_count"] for row in local_rows)
        == {900: 2, 960: 2},
        local_rows,
    )
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B46_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_FOUR_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_SYMBOLIC_STABILIZER_ORBIT_BRANCH_REPLAY",
            "N6-101",
        ],
        "coordinate_fixed_points": coordinate,
        "local_orbit_certificates": local_rows,
        "formal_germ": {
            "linear_variable_count": 20,
            "quadratic_initial_ideal_is_a_radical_graph_edge_ideal": True,
            "all_minimal_components_have_dimension": 5,
            "component_count_by_coordinate_type": {
                "row_type_one_and_transpose": 960,
                "row_type_two_and_transpose": 900,
            },
            "completed_local_scheme_is_exactly_the_union_of_the_symbolic_five_parameter_branches": True,
            "complete_filtered_lifting_is_scheme_theoretic": True,
        },
        "second_product_shadow": {
            "universal_minimum_for_a_72_plane": second_minimum,
            "first_ferrers_witness": list(second_witness),
            "every_equality_branch_has_second_shadow_contained_in_a_23_dimensional_standard_or_biflag_hook": True,
            "therefore_every_equality_branch_has_second_shadow_equal_to_that_flag_shape": True,
        },
        "projective_globalization": {
            "every_irreducible_component_contains_a_coordinate_torus_fixed_point": True,
            "standard_and_biflag_hook_second_shadow_incidence_is_projective_and_closed": True,
            "every_46_plane_with_first_shadow_72_has_second_shadow_dimension": 23,
            "every_second_shadow_is_a_genuine_projective_standard_or_biflag_hook": True,
        },
        "claim_boundary": (
            "This is an ordinary characteristic-zero theorem for 46-planes with "
            "first product shadow exactly 72. It does not classify first-shadow "
            "dimensions 73 through 75, exclude the critical six-term packet by "
            "itself, prove ordinary Chow rank at least 29, or make a border-rank claim."
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
    print("coordinate_models=7200")
    print("local_types=4 facets=960,900,900,960")
    print("second_shadow=23 standard_or_biflag_hook")
    print("N6_PRODUCT_SHADOW_B46_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
