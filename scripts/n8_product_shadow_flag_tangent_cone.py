#!/usr/bin/env python3
"""Exact tangent and quadratic-obstruction audit at the perm_8 flag shadow point.

The reference 560-plane is the coordinate flag equality family from
``docs/general_product_shadow_n8_coordinate_equality.md``.  This script
reconstructs the Grassmann-chart tangent equations for the rank-784 first
shadow locus, identifies all 27 tangent directions, computes the mixed
second-order obstruction map, and verifies the 19-component reduced
quadratic tangent cone.

Only standard-library integer/combinatorial arithmetic is used.  A modular
rank is used in the valid direction to prove that the 256 distinct quadratic
obstruction equations are linearly independent over characteristic zero; the
matching upper bound is their explicit count.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable

N = 8
K = 4
Z = 7
U = tuple(range(7))
V = tuple(range(6))
C0 = (0, 1, 2, 3)
EXTERNAL = (6, 7)
V_MINUS_C0 = (4, 5)
PRIME = 1_000_003

Subset = tuple[int, ...]
Pair = tuple[Subset, Subset]
DomainColumn = tuple[int, int, int]
DirectionLabel = str
QuadraticTerm = tuple[DirectionLabel, DirectionLabel]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def without(subset: Subset, value: int) -> Subset:
    return tuple(item for item in subset if item != value)


def replace(subset: Subset, old: int, new: int) -> Subset:
    require(old in subset and new not in subset, (subset, old, new))
    return tuple(sorted((set(subset) - {old}) | {new}))


def canonical_hash(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def reference_data() -> tuple[list[Pair], set[Pair], list[Pair], dict[Pair, list[DomainColumn]]]:
    layer4 = list(combinations(range(N), K))
    high_rows = [row for row in layer4 if Z not in row]
    low_rows = [row for row in layer4 if Z in row]
    high_columns = [column for column in layer4 if set(column) <= set(V)]

    family = {(row, column) for row in high_rows for column in high_columns}
    family |= {(row, C0) for row in low_rows}
    ordered_family = sorted(family)
    require(len(ordered_family) == 560, len(ordered_family))

    shadow: set[Pair] = set()
    preimages: dict[Pair, list[DomainColumn]] = defaultdict(list)
    for family_index, (row, column) in enumerate(ordered_family):
        for i in row:
            for j in column:
                lower = (without(row, i), without(column, j))
                shadow.add(lower)
                preimages[lower].append((family_index, i, j))
    require(len(shadow) == 784, len(shadow))

    ambient = {(row, column) for row in layer4 for column in layer4}
    outside = sorted(ambient - family)
    require(len(outside) == 4_340, len(outside))
    return ordered_family, shadow, outside, dict(preimages)


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.weight = [1] * size

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        if self.weight[left] < self.weight[right]:
            left, right = right, left
        self.parent[right] = left
        self.weight[left] += self.weight[right]


@dataclass(frozen=True)
class TangentDirection:
    label: DirectionLabel
    variables: tuple[tuple[int, Pair], ...]
    kind: str
    source: int
    target: int


def direction_label(kind: str, source: int, target: int) -> str:
    prefix = {"ambient_column": "A", "row": "R", "line": "L"}[kind]
    return f"{prefix}{source}to{target}"


def classify_component(family: list[Pair], variables: list[tuple[int, Pair]]) -> tuple[str, int, int]:
    row_differences = set()
    column_differences = set()
    for family_index, (new_row, new_column) in variables:
        old_row, old_column = family[family_index]
        row_differences.add(
            (
                tuple(sorted(set(old_row) - set(new_row))),
                tuple(sorted(set(new_row) - set(old_row))),
            )
        )
        column_differences.add(
            (
                tuple(sorted(set(old_column) - set(new_column))),
                tuple(sorted(set(new_column) - set(old_column))),
            )
        )
    require(len(row_differences) == len(column_differences) == 1, variables[:2])
    row_difference = next(iter(row_differences))
    column_difference = next(iter(column_differences))

    if row_difference != ((), ()):
        require(column_difference == ((), ()), column_difference)
        return "row", row_difference[0][0], row_difference[1][0]

    require(column_difference != ((), ()), variables[:2])
    source = column_difference[0][0]
    target = column_difference[1][0]
    if len(variables) == 35:
        return "line", source, target
    return "ambient_column", source, target


@dataclass
class TangentAudit:
    family: list[Pair]
    shadow: set[Pair]
    outside: list[Pair]
    preimages: dict[Pair, list[DomainColumn]]
    allowed_variables: list[tuple[int, Pair]]
    directions: dict[DirectionLabel, TangentDirection]
    zero_component_size: int


def build_tangent_audit() -> TangentAudit:
    family, shadow, outside, preimages = reference_data()

    bad_cells: dict[Pair, tuple[tuple[int, int], ...]] = {}
    for new_row, new_column in outside:
        cells = []
        for i in new_row:
            for j in new_column:
                if (without(new_row, i), without(new_column, j)) not in shadow:
                    cells.append((i, j))
        bad_cells[(new_row, new_column)] = tuple(cells)

    allowed_variables: list[tuple[int, Pair]] = []
    for family_index, (old_row, old_column) in enumerate(family):
        old_rectangle = {(i, j) for i in old_row for j in old_column}
        for outside_pair in outside:
            if all(cell in old_rectangle for cell in bad_cells[outside_pair]):
                allowed_variables.append((family_index, outside_pair))
    require(len(allowed_variables) == 8_960, len(allowed_variables))

    occurrences: dict[tuple[Pair, Pair], list[tuple[DomainColumn, int]]] = defaultdict(list)
    for variable_index, (family_index, (new_row, new_column)) in enumerate(allowed_variables):
        old_row, old_column = family[family_index]
        for i in set(old_row) & set(new_row):
            for j in set(old_column) & set(new_column):
                outside_lower = (without(new_row, i), without(new_column, j))
                if outside_lower in shadow:
                    continue
                old_lower = (without(old_row, i), without(old_column, j))
                occurrences[(old_lower, outside_lower)].append(
                    ((family_index, i, j), variable_index)
                )

    zero = len(allowed_variables)
    dsu = DSU(zero + 1)
    for (old_lower, _), values in occurrences.items():
        by_preimage = {preimage: variable for preimage, variable in values}
        require(len(by_preimage) == len(values), (old_lower, values[:2]))
        variable_values = list(by_preimage.values())
        for variable in variable_values[1:]:
            dsu.union(variable_values[0], variable)
        if len(by_preimage) < len(preimages[old_lower]):
            dsu.union(variable_values[0], zero)

    zero_root = dsu.find(zero)
    components: dict[int, list[tuple[int, Pair]]] = defaultdict(list)
    for variable_index, variable in enumerate(allowed_variables):
        root = dsu.find(variable_index)
        if root != zero_root:
            components[root].append(variable)

    directions: dict[DirectionLabel, TangentDirection] = {}
    for variables in components.values():
        kind, source, target = classify_component(family, variables)
        label = direction_label(kind, source, target)
        require(label not in directions, label)
        directions[label] = TangentDirection(
            label=label,
            variables=tuple(sorted(variables)),
            kind=kind,
            source=source,
            target=target,
        )

    expected_labels = {
        *(direction_label("ambient_column", source, target) for source in V for target in EXTERNAL),
        *(direction_label("row", source, Z) for source in U),
        *(direction_label("line", source, target) for source in C0 for target in V_MINUS_C0),
    }
    require(set(directions) == expected_labels, sorted(directions))

    component_histogram = Counter(len(direction.variables) for direction in directions.values())
    require(component_histogram == Counter({385: 8, 350: 4, 280: 7, 35: 8}), component_histogram)

    zero_component_size = sum(
        1 for variable_index in range(len(allowed_variables)) if dsu.find(variable_index) == zero_root
    )
    require(zero_component_size == 2_240, zero_component_size)
    require(sum(len(direction.variables) for direction in directions.values()) == 6_720, directions)
    return TangentAudit(
        family=family,
        shadow=shadow,
        outside=outside,
        preimages=preimages,
        allowed_variables=allowed_variables,
        directions=directions,
        zero_component_size=zero_component_size,
    )


def direction_maps(audit: TangentAudit) -> tuple[
    dict[DirectionLabel, dict[int, Pair]],
    dict[DirectionLabel, dict[Pair, Pair]],
    dict[DirectionLabel, dict[DomainColumn, Pair]],
]:
    graph: dict[DirectionLabel, dict[int, Pair]] = {}
    psi: dict[DirectionLabel, dict[Pair, Pair]] = {}
    b_part: dict[DirectionLabel, dict[DomainColumn, Pair]] = {}

    for label, direction in audit.directions.items():
        by_family: dict[int, Pair] = {}
        for family_index, outside_pair in direction.variables:
            require(family_index not in by_family, (label, family_index))
            by_family[family_index] = outside_pair
        graph[label] = by_family

        current_psi: dict[Pair, Pair] = {}
        current_b_part: dict[DomainColumn, Pair] = {}
        for family_index, (old_row, old_column) in enumerate(audit.family):
            outside_pair = by_family.get(family_index)
            if outside_pair is None:
                continue
            new_row, new_column = outside_pair
            for i in new_row:
                for j in new_column:
                    new_lower = (without(new_row, i), without(new_column, j))
                    domain_column = (family_index, i, j)
                    if new_lower in audit.shadow:
                        current_b_part[domain_column] = new_lower
                        continue
                    require(i in old_row and j in old_column, (label, domain_column, new_lower))
                    old_lower = (without(old_row, i), without(old_column, j))
                    previous = current_psi.setdefault(old_lower, new_lower)
                    require(previous == new_lower, (label, old_lower, previous, new_lower))
        psi[label] = current_psi
        b_part[label] = current_b_part
    return graph, psi, b_part


def quotient_obstruction_vector(
    audit: TangentAudit,
    left: DirectionLabel,
    right: DirectionLabel,
    psi: dict[DirectionLabel, dict[Pair, Pair]],
    b_part: dict[DirectionLabel, dict[DomainColumn, Pair]],
    shadow_ids: dict[Pair, int],
    outside_ids: dict[Pair, int],
) -> dict[tuple[object, ...], int]:
    values: dict[DomainColumn, Counter[Pair]] = defaultdict(Counter)
    for family_index, (row, column) in enumerate(audit.family):
        for i in range(N):
            for j in range(N):
                domain_column = (family_index, i, j)
                lower = b_part[right].get(domain_column)
                if lower is not None and lower in psi[left]:
                    values[domain_column][psi[left][lower]] += 1
                lower = b_part[left].get(domain_column)
                if lower is not None and lower in psi[right]:
                    values[domain_column][psi[right][lower]] += 1

    vector: dict[tuple[object, ...], int] = {}
    for family_index, (row, column) in enumerate(audit.family):
        for i in range(N):
            for j in range(N):
                if i in row and j in column:
                    continue
                domain_column = (family_index, i, j)
                for outside_lower, coefficient in values.get(domain_column, {}).items():
                    vector[("zero", family_index, i, j, outside_ids[outside_lower])] = coefficient

    for old_lower, preimage_list in audit.preimages.items():
        reference = preimage_list[0]
        reference_values = values.get(reference, {})
        for preimage_index, domain_column in enumerate(preimage_list[1:], start=1):
            current_values = values.get(domain_column, {})
            for outside_lower in set(reference_values) | set(current_values):
                coefficient = current_values.get(outside_lower, 0) - reference_values.get(
                    outside_lower, 0
                )
                if coefficient:
                    vector[
                        (
                            "difference",
                            shadow_ids[old_lower],
                            preimage_index,
                            outside_ids[outside_lower],
                        )
                    ] = coefficient
    return vector


def normalize_equation(terms: dict[QuadraticTerm, int]) -> tuple[tuple[QuadraticTerm, int], ...]:
    values = [(term, coefficient) for term, coefficient in sorted(terms.items()) if coefficient]
    require(values, terms)
    divisor = 0
    from math import gcd

    for _, coefficient in values:
        divisor = gcd(divisor, abs(coefficient))
    values = [(term, coefficient // divisor) for term, coefficient in values]
    if values[0][1] < 0:
        values = [(term, -coefficient) for term, coefficient in values]
    return tuple(values)


def expected_quadratic_equations() -> set[tuple[tuple[QuadraticTerm, int], ...]]:
    equations: set[tuple[tuple[QuadraticTerm, int], ...]] = set()

    def monomial(left: str, right: str) -> None:
        term = tuple(sorted((left, right)))
        equations.add(((term, 1),))

    def binomial(left: QuadraticTerm, right: QuadraticTerm) -> None:
        equations.add(normalize_equation({tuple(sorted(left)): 1, tuple(sorted(right)): 1}))

    row_labels = [direction_label("row", source, Z) for source in U]
    ambient_labels = [
        direction_label("ambient_column", source, target)
        for source in V
        for target in EXTERNAL
    ]
    line_labels = [
        direction_label("line", source, target)
        for source in C0
        for target in V_MINUS_C0
    ]

    for left, right in combinations(row_labels, 2):
        monomial(left, right)
    for row_label in row_labels:
        for other in ambient_labels + line_labels:
            monomial(row_label, other)

    for target in EXTERNAL:
        for source_left, source_right in combinations(V, 2):
            monomial(
                direction_label("ambient_column", source_left, target),
                direction_label("ambient_column", source_right, target),
            )
    for target in V_MINUS_C0:
        for source_left, source_right in combinations(C0, 2):
            monomial(
                direction_label("line", source_left, target),
                direction_label("line", source_right, target),
            )

    for source_left, source_right in combinations(V, 2):
        binomial(
            (
                direction_label("ambient_column", source_left, 6),
                direction_label("ambient_column", source_right, 7),
            ),
            (
                direction_label("ambient_column", source_left, 7),
                direction_label("ambient_column", source_right, 6),
            ),
        )
    for source_left, source_right in combinations(C0, 2):
        binomial(
            (
                direction_label("line", source_left, 4),
                direction_label("line", source_right, 5),
            ),
            (
                direction_label("line", source_left, 5),
                direction_label("line", source_right, 4),
            ),
        )

    for source_left, source_right in combinations(C0, 2):
        for external in EXTERNAL:
            for internal in V_MINUS_C0:
                binomial(
                    (
                        direction_label("ambient_column", source_left, external),
                        direction_label("line", source_right, internal),
                    ),
                    (
                        direction_label("ambient_column", source_right, external),
                        direction_label("line", source_left, internal),
                    ),
                )

    for source in C0:
        for external in EXTERNAL:
            binomial(
                (
                    direction_label("ambient_column", 4, external),
                    direction_label("line", source, 4),
                ),
                (
                    direction_label("ambient_column", 5, external),
                    direction_label("line", source, 5),
                ),
            )

    require(len(equations) == 256, len(equations))
    require(Counter(len(equation) for equation in equations) == Counter({1: 203, 2: 53}), equations)
    return equations


def modular_rank(columns: Iterable[dict[tuple[object, ...], int]], prime: int = PRIME) -> int:
    pivots: dict[tuple[object, ...], dict[tuple[object, ...], int]] = {}
    for raw_column in columns:
        column = {key: value % prime for key, value in raw_column.items() if value % prime}
        while column:
            pivot = min(column)
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(column[pivot], prime - 2, prime)
                pivots[pivot] = {
                    key: value * inverse % prime for key, value in column.items()
                }
                break
            coefficient = column[pivot]
            for key, value in existing.items():
                updated = (column.get(key, 0) - coefficient * value) % prime
                if updated:
                    column[key] = updated
                else:
                    column.pop(key, None)
    return len(pivots)


def maximal_components() -> list[tuple[DirectionLabel, ...]]:
    components = []
    for source in C0:
        components.append(
            tuple(
                sorted(
                    (
                        direction_label("ambient_column", source, 6),
                        direction_label("ambient_column", source, 7),
                        direction_label("line", source, 4),
                        direction_label("line", source, 5),
                    )
                )
            )
        )
    for line_source in C0:
        components.append(
            tuple(
                sorted(
                    (
                        direction_label("ambient_column", 4, 6),
                        direction_label("ambient_column", 4, 7),
                        direction_label("line", line_source, 5),
                    )
                )
            )
        )
        components.append(
            tuple(
                sorted(
                    (
                        direction_label("ambient_column", 5, 6),
                        direction_label("ambient_column", 5, 7),
                        direction_label("line", line_source, 4),
                    )
                )
            )
        )
    for source in U:
        components.append((direction_label("row", source, Z),))
    components = sorted(set(components), key=lambda component: (len(component), component))
    require(Counter(len(component) for component in components) == Counter({4: 4, 3: 8, 1: 7}), components)
    return components


def build_payload() -> dict[str, object]:
    audit = build_tangent_audit()
    graph, psi, b_part = direction_maps(audit)
    labels = sorted(audit.directions)
    shadow_ids = {value: index for index, value in enumerate(sorted(audit.shadow))}
    all_lower = {
        (row, column)
        for row in combinations(range(N), K - 1)
        for column in combinations(range(N), K - 1)
    }
    outside_lower = sorted(all_lower - audit.shadow)
    outside_ids = {value: index for index, value in enumerate(outside_lower)}

    obstruction_columns: list[dict[tuple[object, ...], int]] = []
    coordinate_equations: dict[tuple[object, ...], dict[QuadraticTerm, int]] = defaultdict(dict)
    zero_pairs = []
    nonzero_pairs = []

    for label in labels:
        self_vector = quotient_obstruction_vector(
            audit, label, label, psi, b_part, shadow_ids, outside_ids
        )
        require(not self_vector, ("nonzero self obstruction", label))

    for left, right in combinations(labels, 2):
        vector = quotient_obstruction_vector(
            audit, left, right, psi, b_part, shadow_ids, outside_ids
        )
        if vector:
            nonzero_pairs.append((left, right))
            obstruction_columns.append(vector)
            for coordinate, coefficient in vector.items():
                coordinate_equations[coordinate][(left, right)] = coefficient
        else:
            zero_pairs.append((left, right))

    require(len(zero_pairs) == 42, len(zero_pairs))
    require(len(nonzero_pairs) == 309, len(nonzero_pairs))

    actual_equations = {
        normalize_equation(terms) for terms in coordinate_equations.values() if terms
    }
    expected_equations = expected_quadratic_equations()
    require(actual_equations == expected_equations, (len(actual_equations), len(expected_equations)))
    obstruction_rank = modular_rank(obstruction_columns)
    require(obstruction_rank == 256, obstruction_rank)

    components = maximal_components()
    component_union_edges = {
        tuple(sorted((left, right)))
        for component in components
        for left, right in combinations(component, 2)
    }
    require(component_union_edges == set(zero_pairs), (component_union_edges, zero_pairs))

    direction_rows = []
    for label in labels:
        direction = audit.directions[label]
        direction_rows.append(
            {
                "label": label,
                "kind": direction.kind,
                "source": direction.source,
                "target": direction.target,
                "graph_variable_count": len(direction.variables),
                "psi_nonzero_weight_count": len(psi[label]),
                "B_part_nonzero_column_count": len(b_part[label]),
            }
        )

    core = {
        "status": [
            "N8_FLAG_EQUALITY_REDUCED_QUADRATIC_TANGENT_CONE",
            "EXACT_COMBINATORIAL_LINEARIZATION",
            "EXACT_MIXED_SECOND_ORDER_OBSTRUCTION",
            "NONCOORDINATE_EQUALITY_INTERFACE",
        ],
        "reference_flag": {
            "ambient_dimension": comb(N, K) ** 2,
            "family_dimension": len(audit.family),
            "shadow_dimension": len(audit.shadow),
            "quotient_dimension": len(audit.outside),
            "raw_grassmann_tangent_variable_count": len(audit.family) * len(audit.outside),
            "row_hyperplane_U": list(U),
            "column_six_set_V": list(V),
            "low_column_C0": list(C0),
        },
        "linear_tangent_audit": {
            "allowed_graph_variables_after_zero_column_filter": len(audit.allowed_variables),
            "variables_in_zero_component": audit.zero_component_size,
            "variables_in_nonzero_components": sum(
                len(direction.variables) for direction in audit.directions.values()
            ),
            "tangent_dimension": len(audit.directions),
            "component_size_histogram": {
                str(size): count
                for size, count in sorted(
                    Counter(len(direction.variables) for direction in audit.directions.values()).items()
                )
            },
            "direction_kind_histogram": dict(
                sorted(Counter(direction.kind for direction in audit.directions.values()).items())
            ),
            "directions": direction_rows,
        },
        "quadratic_obstruction": {
            "unordered_direction_pair_count": comb(len(labels), 2),
            "zero_mixed_obstruction_pair_count": len(zero_pairs),
            "nonzero_mixed_obstruction_pair_count": len(nonzero_pairs),
            "distinct_equation_count": len(actual_equations),
            "monomial_equation_count": sum(len(equation) == 1 for equation in actual_equations),
            "binomial_equation_count": sum(len(equation) == 2 for equation in actual_equations),
            "characteristic_zero_equation_rank": obstruction_rank,
            "rank_certificate_prime": PRIME,
            "equation_shapes": {
                "row_annihilation_monomials": 161,
                "ambient_same_external_monomials": 30,
                "line_same_target_monomials": 12,
                "ambient_2x2_permanents": 15,
                "line_2x2_permanents": 6,
                "ambient_line_internal_permanents": 24,
                "ambient_line_outer_permanents": 8,
            },
        },
        "reduced_tangent_cone": {
            "maximal_linear_component_count": len(components),
            "component_dimension_histogram": {
                str(size): count for size, count in sorted(Counter(map(len, components)).items())
            },
            "components": [list(component) for component in components],
            "set_theoretic_classification": (
                "The quadratic zero set is the union of four 4-planes, eight 3-planes, "
                "and seven row-transvection lines. Each plane is integrated by an "
                "explicit elementary-replacement equality family, so this union is "
                "the support of the reduced quadratic tangent cone."
            ),
            "local_equality_locus_dimension": 4,
        },
        "global_equality_locus": {
            "projective_and_torus_stable": True,
            "torus_fixed_point_count": 6_720,
            "all_fixed_points_in_coordinate_flag_orbit": True,
            "dimension": 4,
            "dimension_reason": (
                "Every irreducible component contains a torus-fixed coordinate flag point; "
                "the local tangent-cone support there has maximum dimension four. The "
                "explicit four-dimensional elementary-replacement families attain the cap."
            ),
            "global_irreducible_component_classification": "open",
        },
        "logical_boundary": {
            "coordinate_equality_locus": "complete in PR #35",
            "quadratic_tangent_cone_support_at_each_flag_point": "complete",
            "formal_or_analytic_arc_leading_direction": "one of 19 component types",
            "full_noncoordinate_equality_locus": "open",
            "higher_order_branch_switching": "open",
            "fourteen_chow_term_realizability": "open",
            "new_perm8_lower_bound": False,
            "border_rank_claim": False,
            "literature_novelty": "not established",
        },
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N8_PRODUCT_SHADOW_TANGENT_CONE_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
