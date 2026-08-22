#!/usr/bin/env python3
"""Uniform exact certificate for the 73--76 to 90 equality plateau."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b73_76_equality_locus.json"
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


def bounded_partitions(total: int, length: int, bound: int, ceiling: int | None = None):
    if length == 0:
        if total == 0:
            yield ()
        return
    ceiling = bound if ceiling is None else min(bound, ceiling)
    for first in range(min(total, ceiling), -1, -1):
        for tail in bounded_partitions(total - first, length - 1, bound, first):
            yield (first,) + tail


def expected_profiles(dimension: int) -> set[tuple[int, ...]]:
    deleted = 80 - dimension
    row = {
        tuple(sorted((20 - value for value in part), reverse=True)) + (0,) * 16
        for part in bounded_partitions(deleted, 4, 20)
    }
    transpose = {
        tuple(sorted((4 - value for value in part), reverse=True))
        for part in bounded_partitions(deleted, 20, 4)
    }
    return row | transpose


def coordinate_certificate(b49, b50, parent: set[tuple[int, int]], shadow: set[tuple[int, int]]):
    rows = []
    for dimension in range(73, 77):
        minimum, profiles = b49.minimum_ferrers_partitions(dimension)
        expected = expected_profiles(dimension)
        require(minimum == 90 and set(profiles) == expected, (dimension, minimum, profiles))
        deleted = 80 - dimension
        rows.append(
            {
                "dimension": dimension,
                "deleted_cell_count": deleted,
                "minimum_first_product_shadow": minimum,
                "minimizing_ferrers_profile_count": len(profiles),
                "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
                "coordinate_fixed_point_count": 30 * comb(80, deleted),
            }
        )

    source_multiplicity = Counter()
    for target in shadow:
        source_multiplicity[
            sum(target in b50.product_shadow({source}) for source in parent)
        ] += 1
    require(source_multiplicity == Counter({8: 90}), source_multiplicity)
    johnson_adjacency = {
        left: {
            right
            for right in range(20)
            if right != left
            and len(set(b49.TRIPLES[left]) & set(b49.TRIPLES[right])) == 2
        }
        for left in range(20)
    }
    connected_after_seven_deletions = True
    for deleted in combinations(range(20), 7):
        remaining = set(range(20)) - set(deleted)
        reached = {next(iter(remaining))}
        stack = list(reached)
        while stack:
            vertex = stack.pop()
            for neighbor in johnson_adjacency[vertex] & remaining:
                if neighbor not in reached:
                    reached.add(neighbor)
                    stack.append(neighbor)
        if reached != remaining:
            connected_after_seven_deletions = False
            break
    require(connected_after_seven_deletions, deleted)
    require(b49.small_equalities_have_expected_forms(3, 6), None)
    require(b49.small_equalities_have_expected_forms(4, 6), None)
    return {
        "dimensions": rows,
        "parent_dimension": 80,
        "parent_shadow_dimension": 90,
        "source_multiplicity_histogram": {
            str(key): value for key, value in sorted(source_multiplicity.items())
        },
        "johnson_J_6_3_remains_connected_after_any_seven_vertex_deletions": True,
        "three_or_four_triples_with_pair_shadow_six_lie_in_one_C_U4_3": True,
        "deleting_at_most_seven_cells_preserves_the_parent_coordinate_shadow": True,
        "every_coordinate_equality_support_has_a_unique_product_parent": True,
        "original_support_classification_proved_without_reverse_compression": True,
    }


class Dinic:
    def __init__(self, size: int):
        self.graph: list[list[list[int]]] = [[] for _ in range(size)]

    def add(self, left: int, right: int, capacity: int) -> None:
        self.graph[left].append([right, capacity, len(self.graph[right])])
        self.graph[right].append([left, 0, len(self.graph[left]) - 1])

    def flow(self, source: int, sink: int) -> int:
        answer = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = deque([source])
            while queue:
                vertex = queue.popleft()
                for target, capacity, _ in self.graph[vertex]:
                    if capacity and level[target] < 0:
                        level[target] = level[vertex] + 1
                        queue.append(target)
            if level[sink] < 0:
                return answer
            cursor = [0] * len(self.graph)

            def augment(vertex: int, amount: int) -> int:
                if vertex == sink:
                    return amount
                while cursor[vertex] < len(self.graph[vertex]):
                    edge = self.graph[vertex][cursor[vertex]]
                    target, capacity, reverse = edge
                    if capacity and level[target] == level[vertex] + 1:
                        pushed = augment(target, min(amount, capacity))
                        if pushed:
                            edge[1] -= pushed
                            self.graph[target][reverse][1] += pushed
                            return pushed
                    cursor[vertex] += 1
                return 0

            while True:
                pushed = augment(source, 10**6)
                if not pushed:
                    break
                answer += pushed


def equation_events(b49, support: set[tuple[int, int]], shadow: set[tuple[int, int]]):
    sources = sorted(support)
    outside_cubics = sorted(b49.ALL_CUBICS - support)
    quotients = sorted(b49.ALL_QUADRICS - shadow)
    tangent_set = {(source, outside) for source in sources for outside in outside_cubics}
    eta_set = {(target, quotient) for target in shadow for quotient in quotients}
    edges: set[tuple[object, object]] = set()
    tangent_zero: dict[object, set[tuple[int, int]]] = defaultdict(set)
    eta_zero: dict[object, set[tuple[int, int]]] = defaultdict(set)
    for source in sources:
        row_triple, column_triple = b49.TRIPLES[source[0]], b49.TRIPLES[source[1]]
        for row_vertex in range(6):
            for column_vertex in range(6):
                target = None
                if row_vertex in row_triple and column_vertex in column_triple:
                    target = (
                        b49.I2[tuple(value for value in row_triple if value != row_vertex)],
                        b49.I2[tuple(value for value in column_triple if value != column_vertex)],
                    )
                for quotient in quotients:
                    row_pair, column_pair = b49.PAIRS[quotient[0]], b49.PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            b49.I3[tuple(sorted(row_pair + (row_vertex,)))],
                            b49.I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    tangent = (source, outside) if (source, outside) in tangent_set else None
                    eta = (target, quotient) if (target, quotient) in eta_set else None
                    if tangent is not None and eta is not None:
                        edges.add((tangent, eta))
                    elif tangent is not None:
                        tangent_zero[tangent].add(source)
                    elif eta is not None:
                        eta_zero[eta].add(source)
    return tangent_set, eta_set, edges, tangent_zero, eta_zero


def restricted_tangent_cut(tangents: list[object], etas: list[object], edges: list[tuple[object, object]]) -> int:
    eta_index = {eta: index for index, eta in enumerate(etas)}
    offset = len(etas)
    tangent_index = {
        tangent: (offset + 2 * index, offset + 2 * index + 1)
        for index, tangent in enumerate(tangents)
    }
    size = offset + 2 * len(tangents)
    values = []
    for sink in range(1, len(etas)):
        flow = Dinic(size)
        for entry, exit_ in tangent_index.values():
            flow.add(entry, exit_, 1)
        for tangent, eta in edges:
            entry, exit_ = tangent_index[tangent]
            target = eta_index[eta]
            flow.add(exit_, target, 1000)
            flow.add(target, entry, 1000)
        values.append(flow.flow(0, sink))
    return min(values)


def linear_stability_certificate(b49, parent: set[tuple[int, int]], shadow: set[tuple[int, int]]):
    data = b49.incidence_data(parent, shadow)
    tangent_set, eta_set, edges, tangent_zero, eta_zero = equation_events(b49, parent, shadow)
    free_tangent = set(data["tangent_component"])
    free_eta = set(data["eta_component"])
    ground_tangent = tangent_set - free_tangent
    ground_eta = eta_set - free_eta
    by_tangent: dict[int, list[object]] = defaultdict(list)
    by_eta: dict[int, list[object]] = defaultdict(list)
    for tangent, component in data["tangent_component"].items():
        by_tangent[int(component)].append(tangent)
    for eta, component in data["eta_component"].items():
        by_eta[int(component)].append(eta)

    signatures = []
    cuts = []
    for component in sorted(by_tangent):
        tangents = by_tangent[component]
        etas = by_eta[component]
        component_edges = [(left, right) for left, right in edges if left in set(tangents) and right in set(etas)]
        tangent_degrees = Counter(left for left, _ in component_edges)
        eta_degrees = Counter(right for _, right in component_edges)
        require(len({left[0] for left in tangents}) == 60, component)
        signature = (
            len(tangents),
            len(etas),
            len(component_edges),
            tuple(sorted(set(tangent_degrees.values()))),
            tuple(sorted(set(eta_degrees.values()))),
        )
        signatures.append(signature)
        cuts.append(restricted_tangent_cut(tangents, etas, component_edges))
    require(set(signatures) == {(60, 45, 360, (6,), (8,))}, signatures)
    require(cuts == [8] * 8, cuts)
    require(all(tangent_zero[tangent] for tangent in ground_tangent), None)
    grounded_neighbor_sources: dict[object, set[tuple[int, int]]] = defaultdict(set)
    for tangent, eta in edges:
        if tangent in ground_tangent:
            grounded_neighbor_sources[eta].add(tangent[0])
    witness_counts = Counter()
    for eta in ground_eta:
        witnesses = set(eta_zero[eta])
        witnesses.update(grounded_neighbor_sources[eta])
        witness_counts[len(witnesses)] += 1
    require(witness_counts == Counter({8: len(ground_eta)}), witness_counts)
    relative = {
        str(dimension): dimension * (80 - dimension) for dimension in range(73, 77)
    }
    free_dimensions = {
        str(dimension): 8 + relative[str(dimension)] for dimension in range(73, 77)
    }
    return {
        "parent_free_component_count": data["free_dimension"],
        "free_component_signature": {
            "tangent_vertices": 60,
            "eta_vertices": 45,
            "incidence_edges": 360,
            "tangent_degree": 6,
            "eta_degree": 8,
        },
        "restricted_tangent_vertex_cut_for_each_parent_component": cuts,
        "grounded_tangent_count": len(ground_tangent),
        "every_grounded_tangent_has_a_direct_zero_equation": True,
        "grounded_eta_count": len(ground_eta),
        "grounded_eta_source_witness_histogram": {
            str(key): value for key, value in sorted(witness_counts.items())
        },
        "deleting_at_most_seven_sources_preserves_exactly_eight_parent_roots": True,
        "relative_grassmann_dimensions": relative,
        "complete_linear_dimensions": free_dimensions,
        "eta_only_root_count": 0,
    }


def quadratic_stability_certificate(n6082, b49, parent: set[tuple[int, int]], shadow: set[tuple[int, int]]):
    child = b49.incidence_data(parent, shadow)
    groups, _ = n6082.component_groups(b49, child, False)
    forbidden = {tuple(sorted(pair)) for group in groups for pair in combinations(group, 2)}
    parent_grounded = n6082.grounded_certificate(b49, child, forbidden)
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

    occurrence_sources: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    occurrence_rows: Counter[tuple[int, int]] = Counter()
    relative_contexts: set[tuple[int, int, tuple[int, int]]] = set()
    grounded_inside_parent_occurrences = 0
    parent_set = set(parent)
    free_eta = set(eta_component)
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
                for quotient in child["target_complement"]:
                    row_pair, column_pair = b49.PAIRS[quotient[0]], b49.PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            b49.I3[tuple(sorted(row_pair + (row_vertex,)))],
                            b49.I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    if (outside is not None and outside not in parent_set) or target is not None:
                        continue
                    grounded_inside_parent_occurrences += int(outside in parent_set)
                    terms: Counter[tuple[int, int]] = Counter()
                    for derivative_target, right in derivative_components.get(
                        (source, row_vertex, column_vertex), ()
                    ):
                        left = eta_component.get((derivative_target, quotient))
                        if left is not None:
                            terms[tuple(sorted((left, right)))] += 1
                    if terms:
                        require(len(terms) == 1, terms)
                        monomial = next(iter(terms))
                        occurrence_sources[monomial].add(source)
                        occurrence_rows[monomial] += 1

                    if outside is None and target is None:
                        relative_contexts.add((row_vertex, column_vertex, quotient))
    relative_potential = 0
    for row_vertex, column_vertex, quotient in relative_contexts:
        for deleted in parent:
            deleted_row, deleted_column = b49.TRIPLES[deleted[0]], b49.TRIPLES[deleted[1]]
            if row_vertex in deleted_row and column_vertex in deleted_column:
                derivative_target = (
                    b49.I2[tuple(value for value in deleted_row if value != row_vertex)],
                    b49.I2[
                        tuple(value for value in deleted_column if value != column_vertex)
                    ],
                )
                relative_potential += int((derivative_target, quotient) in free_eta)
    require(set(occurrence_sources) == forbidden, occurrence_sources)
    source_histogram = Counter(len(value) for value in occurrence_sources.values())
    row_histogram = Counter(occurrence_rows.values())
    require(source_histogram == Counter({40: 12}), source_histogram)
    require(row_histogram == Counter({120: 12}), row_histogram)
    require(grounded_inside_parent_occurrences == 0, grounded_inside_parent_occurrences)
    require(relative_potential == 0, relative_potential)
    return {
        "parent_grounded_quadratic_initial_forms": parent_grounded,
        "forbidden_generator_count": len(forbidden),
        "distinct_source_support_histogram_per_forbidden_generator": {
            str(key): value for key, value in sorted(source_histogram.items())
        },
        "raw_occurrence_histogram_per_forbidden_generator": {
            str(key): value for key, value in sorted(row_histogram.items())
        },
        "potential_relative_variable_grounded_monomial_count": relative_potential,
        "grounded_equation_with_an_inside_parent_outside_count": grounded_inside_parent_occurrences,
        "deleting_at_most_seven_sources_preserves_the_full_parent_initial_ideal": True,
        "initial_ideal": "I(K4)+I(K4)",
    }


def build_payload() -> dict[str, object]:
    n6082 = load_module(N6082_SCRIPT, "n6082_for_n6090")
    n6082_data = json.loads(N6082_DATA.read_text(encoding="utf-8"))
    require(
        n6082_data["formal_germ"]["initial_ideal"] == "I(K4)+I(K4)"
        and n6082_data["formal_germ"]["boolean_component_count_at_each_fixed_point"] == 16
        and n6082_data["second_product_shadow"]["every_equality_point_has_second_shadow_dimension"] == 24,
        N6082_DATA,
    )
    b49 = n6082.load_module(n6082.B49_SCRIPT, "b49_for_n6090")
    b50 = n6082.load_module(n6082.B50_SCRIPT, "b50_for_n6090")
    parent, shadow = n6082.standard_support(b49, False)
    coordinate = coordinate_certificate(b49, b50, parent, shadow)
    linear = linear_stability_certificate(b49, parent, shadow)
    quadratic = quadratic_stability_certificate(n6082, b49, parent, shadow)
    branches = {}
    for dimension in range(73, 77):
        relative = dimension * (80 - dimension)
        branches[str(dimension)] = {
            "relative_grassmann_dimension": relative,
            "formal_linear_dimension": 8 + relative,
            "boolean_component_count": 16,
            "component_dimension": 2 + relative,
        }
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B73_TO_B76_EQUALITY_LOCUS_EXTENSION",
            "EXACT_UNIFORM_SEVEN_DELETION_LINEAR_AND_QUADRATIC_STABILITY",
            "N6-090",
        ],
        "coordinate_fixed_points": coordinate,
        "uniform_linear_stability": linear,
        "uniform_quadratic_stability": quadratic,
        "formal_germs": branches,
        "projective_globalization": {
            "every_73_to_76_plane_with_first_shadow_90_extends_to_an_80_plane_with_the_same_shadow": True,
            "every_equality_plane_has_second_shadow_dimension": 24,
            "second_shadow_is_partitioned_4_by_6_product_or_transpose": True,
        },
        "claim_boundary": (
            "This proves the same-shadow extension only for dimensions 73 through 76 at first "
            "shadow 90. It does not treat dimension 72, whose minimum shadow is 89; it does not "
            "by itself exclude an actual packet, exclude global b=34, prove ordinary lower 29, "
            "or make a border-rank claim."
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
    print("dimensions=73..76 first_shadow=90 uniform_deletion_cut=8")
    print("parent_quadratic_rank=12 source_support_per_generator=40 relative_terms=0")
    print("N6_PRODUCT_SHADOW_B73_76_EQUALITY_LOCUS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
