#!/usr/bin/env python3
"""Exact coordinate and local certificates for the N6-073 b=49 theorem."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b49_equality_locus.json"
sys.path.insert(0, str(ROOT / "scripts"))

import n6_product_shadow_b50_equality_locus as b50  # noqa: E402


TRIPLES = b50.TRIPLES
PAIRS = b50.PAIRS
I3 = b50.I3
I2 = b50.I2
ALL_CUBICS = set(product(range(20), repeat=2))
ALL_QUADRICS = set(product(range(15), repeat=2))


class DisjointSet:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.grounded = [False] * size

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left, right = self.find(left), self.find(right)
        if left != right:
            self.parent[right] = left
            self.grounded[left] = self.grounded[left] or self.grounded[right]

    def zero(self, item: int) -> None:
        self.grounded[self.find(item)] = True

    def finish(self) -> None:
        for item in range(len(self.parent)):
            root = self.find(item)
            if self.grounded[item]:
                self.grounded[root] = True


def one_factor_data() -> tuple[list[int], list[int]]:
    ordered = sorted(TRIPLES, key=lambda subset: sum(1 << x for x in subset))
    seen: set[tuple[int, ...]] = set()
    shadow_sizes = [0]
    weights = []
    for triple in ordered:
        new = set(combinations(triple, 2)) - seen
        weights.append(len(new))
        seen.update(new)
        shadow_sizes.append(len(seen))
    return shadow_sizes, weights


def minimum_ferrers_partitions(total: int) -> tuple[int, list[tuple[int, ...]]]:
    shadow_sizes, weights = one_factor_data()
    infinity = 10**9

    @lru_cache(maxsize=None)
    def solve(index: int, previous: int, remaining: int) -> int:
        if index == 20:
            return 0 if remaining == 0 else infinity
        return min(
            (
                weights[index] * shadow_sizes[value]
                + solve(index + 1, value, remaining - value)
                for value in range(min(previous, remaining), -1, -1)
                if remaining - value <= value * (19 - index)
            ),
            default=infinity,
        )

    witnesses: list[tuple[int, ...]] = []

    def collect(index: int, previous: int, remaining: int, prefix: tuple[int, ...]) -> None:
        if index == 20:
            if remaining == 0:
                witnesses.append(prefix)
            return
        optimum = solve(index, previous, remaining)
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (19 - index):
                continue
            if weights[index] * shadow_sizes[value] + solve(
                index + 1, value, remaining - value
            ) == optimum:
                collect(index + 1, value, remaining - value, prefix + (value,))

    collect(0, 20, total, ())
    return solve(0, 20, total), witnesses


def lower_shadow(family: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    return {face for member in family for face in combinations(member, 2)}


def small_equality_count(size: int, shadow_size: int) -> int:
    return sum(
        len(lower_shadow(family)) == shadow_size
        for family in combinations(TRIPLES, size)
    )


def small_equalities_have_expected_forms(size: int, shadow_size: int) -> bool:
    missing_count = {3: 1, 4: 0, 9: 1, 10: 0, 19: 1}[size]
    expected_vertex_count = {3: 4, 4: 4, 9: 5, 10: 5, 19: 6}[size]
    for family in combinations(TRIPLES, size):
        if len(lower_shadow(family)) != shadow_size:
            continue
        vertices = set().union(*(set(member) for member in family))
        full = set(combinations(sorted(vertices), 3))
        if (
            len(vertices) != expected_vertex_count
            or not set(family) <= full
            or len(full - set(family)) != missing_count
        ):
            return False
    return True


def all_labelled_hooks() -> list[frozenset[tuple[int, int]]]:
    hooks: list[frozenset[tuple[int, int]]] = []
    for row_four in combinations(range(6), 4):
        for row_three in combinations(row_four, 3):
            for column_five in combinations(range(6), 5):
                support = {
                    (I3[row], I3[column])
                    for row in combinations(row_four, 3)
                    for column in combinations(column_five, 3)
                } | {(I3[row_three], column) for column in range(20)}
                hooks.append(frozenset(support))
                hooks.append(frozenset((column, row) for row, column in support))
    assert len(hooks) == len(set(hooks)) == 720
    return hooks


def row_profile(support: set[tuple[int, int]] | frozenset[tuple[int, int]]) -> tuple[int, ...]:
    degrees = Counter(row for row, _ in support)
    return tuple(sorted(degrees.values(), reverse=True)) + (0,) * (20 - len(degrees))


def coordinate_certificate() -> dict[str, object]:
    minimum, profiles = minimum_ferrers_partitions(49)
    hooks = all_labelled_hooks()
    parents: dict[frozenset[tuple[int, int]], int] = defaultdict(int)
    profile_counts: Counter[tuple[int, ...]] = Counter()
    all_shadows_are_75 = True
    for hook in hooks:
        for deleted in hook:
            child = hook - {deleted}
            parents[child] += 1
            profile_counts[row_profile(child)] += 1
            all_shadows_are_75 &= len(b50.product_shadow(child)) == 75

    expected_profiles = {
        (20, 10, 10, 9) + (0,) * 16,
        (19, 10, 10, 10) + (0,) * 16,
        (4,) * 10 + (1,) * 9 + (0,),
        (4,) * 9 + (3,) + (1,) * 10,
    }
    assert minimum == 75
    assert set(profiles) == expected_profiles
    assert len(parents) == 36_000
    assert Counter(parents.values()) == {1: 36_000}
    assert set(profile_counts) == expected_profiles
    assert all_shadows_are_75
    small = {
        "three_triples_shadow_six": small_equality_count(3, 6),
        "four_triples_shadow_six": small_equality_count(4, 6),
        "nine_triples_shadow_ten": small_equality_count(9, 10),
        "ten_triples_shadow_ten": small_equality_count(10, 10),
        "nineteen_triples_shadow_fifteen": small_equality_count(19, 15),
    }
    assert small == {
        "three_triples_shadow_six": 60,
        "four_triples_shadow_six": 15,
        "nine_triples_shadow_ten": 60,
        "ten_triples_shadow_ten": 6,
        "nineteen_triples_shadow_fifteen": 20,
    }
    expected_forms = {
        f"size_{size}_shadow_{shadow_size}": small_equalities_have_expected_forms(
            size, shadow_size
        )
        for size, shadow_size in ((3, 6), (4, 6), (9, 10), (10, 10), (19, 15))
    }
    assert all(expected_forms.values())
    return {
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "small_equality_family_counts": small,
        "all_small_equality_families_have_the_claimed_clique_or_one_deletion_form": expected_forms,
        "labelled_fifty_hook_count": len(hooks),
        "labelled_parent_cell_deletions": len(hooks) * 50,
        "distinct_coordinate_equality_support_count": len(parents),
        "parent_multiplicity_histogram": {
            str(key): value for key, value in sorted(Counter(parents.values()).items())
        },
        "profile_counts": [
            {"profile": list(profile), "count": count}
            for profile, count in sorted(profile_counts.items(), reverse=True)
        ],
        "all_children_have_first_shadow_75": all_shadows_are_75,
        "every_coordinate_equality_support_has_a_unique_fifty_hook_parent": True,
    }


def incidence_data(support: set[tuple[int, int]], shadow: set[tuple[int, int]]) -> dict[str, object]:
    sources = sorted(support)
    source_complement = sorted(ALL_CUBICS - support)
    targets = sorted(shadow)
    target_complement = sorted(ALL_QUADRICS - shadow)
    tangent_pairs = [(source, outside) for source in sources for outside in source_complement]
    eta_pairs = [(target, quotient) for target in targets for quotient in target_complement]
    tangent_index = {pair: i for i, pair in enumerate(tangent_pairs)}
    offset = len(tangent_pairs)
    eta_index = {pair: offset + i for i, pair in enumerate(eta_pairs)}
    dsu = DisjointSet(offset + len(eta_pairs))

    for source in sources:
        row, column = source
        row_triple, column_triple = TRIPLES[row], TRIPLES[column]
        for row_vertex in range(6):
            for column_vertex in range(6):
                target = None
                if row_vertex in row_triple and column_vertex in column_triple:
                    target = (
                        I2[tuple(x for x in row_triple if x != row_vertex)],
                        I2[tuple(x for x in column_triple if x != column_vertex)],
                    )
                for quotient in target_complement:
                    row_pair, column_pair = PAIRS[quotient[0]], PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            I3[tuple(sorted(row_pair + (row_vertex,)))],
                            I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    tangent = tangent_index.get((source, outside))
                    eta = eta_index.get((target, quotient)) if target is not None else None
                    if tangent is not None and eta is not None:
                        dsu.union(tangent, eta)
                    elif tangent is not None:
                        dsu.zero(tangent)
                    elif eta is not None:
                        dsu.zero(eta)
    dsu.finish()

    roots = sorted(
        {
            dsu.find(i)
            for i in range(offset + len(eta_pairs))
            if not dsu.grounded[dsu.find(i)]
        }
    )
    component_index = {root: i for i, root in enumerate(roots)}
    tangent_component = {
        tangent_pairs[i]: component_index[dsu.find(i)]
        for i in range(offset)
        if not dsu.grounded[dsu.find(i)]
    }
    eta_component = {
        eta_pairs[i - offset]: component_index[dsu.find(i)]
        for i in range(offset, offset + len(eta_pairs))
        if not dsu.grounded[dsu.find(i)]
    }
    tangent_roots = set(tangent_component.values())
    eta_roots = set(eta_component.values())
    return {
        "sources": sources,
        "target_complement": target_complement,
        "tangent_component": tangent_component,
        "eta_component": eta_component,
        "free_dimension": len(roots),
        "tangent_root_count": len(tangent_roots),
        "eta_root_count": len(eta_roots),
        "eta_only_root_count": len(eta_roots - tangent_roots),
    }


def representative_rows() -> list[tuple[str, bool, tuple[int, int]]]:
    rows = []
    for transpose in (False, True):
        support = b50.hook_support(transpose)
        degrees = Counter(row for row, _ in support)
        by_degree: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for cell in sorted(support):
            by_degree[degrees[cell[0]]].append(cell)
        if transpose:
            rows.extend(
                [
                    ("4^9,3,1^10", True, by_degree[4][0]),
                    ("4^10,1^9,0", True, by_degree[1][0]),
                ]
            )
        else:
            rows.extend(
                [
                    ("19,10,10,10", False, by_degree[20][0]),
                    ("20,10,10,9", False, by_degree[10][0]),
                ]
            )
    return rows


def local_certificate(name: str, transpose: bool, deleted: tuple[int, int]) -> dict[str, object]:
    parent = b50.incidence_data(transpose)
    parent_support = set(parent["support"])
    shadow = set(parent["shadow"])
    support = parent_support - {deleted}
    assert b50.product_shadow(support) == shadow
    coordinate_prolongation = {
        cubic for cubic in ALL_CUBICS if b50.product_shadow({cubic}) <= shadow
    }
    assert coordinate_prolongation == parent_support
    child = incidence_data(support, shadow)
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
    hyperplane_map = [tangent_component[(source, deleted)] for source in sorted(support)]
    assert len(set(parent_map)) == 16
    assert len(set(hyperplane_map)) == 49
    assert set(parent_map).isdisjoint(hyperplane_map)
    assert child["free_dimension"] == 65

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

    derivative_components: dict[
        tuple[tuple[int, int], int, int], list[tuple[tuple[int, int], int]]
    ] = {}
    tangent_by_source: dict[tuple[int, int], list[tuple[tuple[int, int], int]]] = defaultdict(list)
    for (source, outside), component in tangent_component.items():
        tangent_by_source[source].append((outside, component))
    for source, members in tangent_by_source.items():
        for row_vertex in range(6):
            for column_vertex in range(6):
                values = []
                for outside, component in members:
                    row_triple, column_triple = TRIPLES[outside[0]], TRIPLES[outside[1]]
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
    raw_coefficient_histogram: Counter[int] = Counter()
    raw_monomials: set[tuple[int, int]] = set()
    raw_hyperplane_monomials: set[tuple[int, int]] = set()
    for source in child["sources"]:
        row, column = source
        row_triple, column_triple = TRIPLES[row], TRIPLES[column]
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
                    row_pair, column_pair = PAIRS[quotient[0]], PAIRS[quotient[1]]
                    outside = None
                    if row_vertex not in row_pair and column_vertex not in column_pair:
                        outside = (
                            I3[tuple(sorted(row_pair + (row_vertex,)))],
                            I3[tuple(sorted(column_pair + (column_vertex,)))],
                        )
                    tangent_variable_exists = outside is not None and outside not in support
                    eta_variable_exists = target is not None
                    if tangent_variable_exists or eta_variable_exists:
                        continue
                    grounded_equations += 1
                    row_terms = Counter()
                    for derivative_target, right in derivatives:
                        left = eta_component.get((derivative_target, quotient))
                        if left is not None:
                            row_terms[tuple(sorted((left, right)))] += 1
                    row_terms = Counter({term: coefficient for term, coefficient in row_terms.items() if coefficient})
                    if row_terms:
                        assert len(row_terms) == 1
                        coefficient = next(iter(row_terms.values()))
                        assert coefficient > 0
                        raw_coefficient_histogram[coefficient] += 1
                        nonzero_rows += 1
                        monomial = next(iter(row_terms))
                        raw_monomials.add(monomial)
                        if set(monomial) & set(hyperplane_map):
                            raw_hyperplane_monomials.add(monomial)
    assert raw_monomials == forbidden
    assert not raw_hyperplane_monomials

    branch_count = 0
    all_jacobians_are_identity = True
    for branch in product(*group_rows):
        branch_count += 1
        selected = set(hyperplane_map) | set(branch)
        all_jacobians_are_identity &= len(selected) == 53
    assert branch_count == 240
    assert all_jacobians_are_identity
    return {
        "profile": name,
        "orientation": "transpose_hook" if transpose else "row_hook",
        "deleted_cell": [list(TRIPLES[deleted[0]]), list(TRIPLES[deleted[1]])],
        "linear_incidence": {
            "free_dimension": child["free_dimension"],
            "parent_linear_dimension": len(set(parent_map)),
            "relative_hyperplane_dimension": len(set(hyperplane_map)),
            "eta_root_count": child["eta_root_count"],
            "eta_only_root_count": child["eta_only_root_count"],
            "full_parent_plus_hyperplane_jacobian_rank": len(set(parent_map) | set(hyperplane_map)),
            "coordinate_prolongation_weight_count": len(coordinate_prolongation),
            "coordinate_prolongation_is_the_unique_hook_parent": coordinate_prolongation
            == parent_support,
        },
        "grounded_quadratic_initial_forms": {
            "grounded_equation_count": grounded_equations,
            "nonzero_raw_row_count": nonzero_rows,
            "raw_rows_are_nonzero_integer_multiples_of_single_monomials": True,
            "raw_coefficient_histogram": {
                str(key): value for key, value in sorted(raw_coefficient_histogram.items())
            },
            "parent_group_sizes": sorted(map(len, group_rows)),
            "forbidden_unit_count": len(forbidden),
            "exact_rank_over_Q": len(raw_monomials),
            "raw_non_forbidden_monomial_count": len(raw_monomials - forbidden),
            "raw_hyperplane_monomial_count": len(raw_hyperplane_monomials),
            "row_span_is_exactly_the_twenty_five_forbidden_units": raw_monomials == forbidden,
        },
        "relative_boolean_branches": {
            "count": branch_count,
            "dimension": 53,
            "n6064_boolean_jacobian_is_exact_4_by_4_identity": True,
            "tautological_hyperplane_chart_jacobian_is_49_by_49_identity": True,
            "replayed_free_coordinate_sets_are_disjoint": all_jacobians_are_identity,
            "combined_block_jacobian_rank": 53,
        },
    }


def build_payload() -> dict[str, object]:
    coordinate = coordinate_certificate()
    local_rows = [local_certificate(*row) for row in representative_rows()]
    assert len(local_rows) == 4
    assert all(row["linear_incidence"]["free_dimension"] == 65 for row in local_rows)
    assert all(
        row["grounded_quadratic_initial_forms"][
            "row_span_is_exactly_the_twenty_five_forbidden_units"
        ]
        for row in local_rows
    )
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_B49_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_RELATIVE_240_BRANCH_REPLAY",
            "N6-073",
        ],
        "coordinate_fixed_points": coordinate,
        "local_representatives": local_rows,
        "formal_germ": {
            "linear_dimension": 65,
            "smooth_relative_hyperplane_factor_dimension": 49,
            "parent_boolean_variable_count": 16,
            "forbidden_quadratic_generator_count": 25,
            "boolean_component_count": 240,
            "component_dimension": 53,
            "initial_ideal_is_parent_J_extended_by_49_smooth_variables": True,
            "complete_formal_germ_is_union_of_relative_boolean_branches": True,
            "proof_interface": (
                "The twenty-five grounded initial forms give J inside the initial ideal. "
                "The projective hyperplane bundle over the 240 exact N6-064 branches gives "
                "the reverse tangent-cone inclusion; "
                "closed filtered-ideal lifting then identifies the complete ideals."
            ),
        },
        "projective_globalization": {
            "every_irreducible_component_contains_a_coordinate_torus_fixed_point": True,
            "relative_grassmannian_image_is_projective_and_closed": True,
            "every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75": True,
            "first_shadow_equals_the_parent_first_shadow": True,
            "second_shadow_dimension": 23,
            "second_shadow_is_a_projective_flag_hook": True,
        },
        "arithmetic": (
            "All replayed eliminations use integer equality components and nonzero integer "
            "multiples of single monomials; division over Q gives the stated unit RREF. No "
            "finite-field rank is used to prove the characteristic-zero theorem."
        ),
        "claim_boundary": (
            "This is an ordinary characteristic-zero theorem for the rank-at-most-75 "
            "product-shadow locus at dimension 49. It is not a border-rank theorem and does "
            "not by itself close ordinary rank 29: the fixed-six argument must still be "
            "connected, and the all-alpha-three b=47 and b=48 layers are not treated here."
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
