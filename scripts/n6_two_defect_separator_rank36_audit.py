#!/usr/bin/env python3
"""Exact characteristic-zero audit for the fixed-base two-defect separator.

For ``g(r)=n_4(r)n_5(r)``, N6-022 proved ``31 <= rho_2(g) <= 36``.
This audit closes the interval.

A coordinate retraction identifies row values 1, 2, and 3 with row value 0.
It fixes ``g`` and maps every normalized sign vector to one of the four labels
``0, 8, 16, 24``.  Hence the full fixed-base dictionary has the same atomic
rank as this restricted dictionary.

On one column pair, the nine nonconstant restricted atoms are enumerated over
``Q``.  All 243 exact support-affine spaces are reconstructed.  Every support
of size at least four compresses, without increasing total support, to a
size-two or size-three pair representation plus ordinary lower-order atoms,
except for two size-four points and two size-five affine families.

The resulting global problem starts with thirty forced pair atoms.  An exact
finite search covers every way to spend at most five additional atoms among
seven cost-one point bundles, two cost-two point bundles, two cost-three
affine bundles, and the ordinary constant/unary dictionary.  No support of
size at most 35 is possible.  The existing 36-atom identity supplies equality.

All elimination uses ``Fraction``.  No floating point, random search, or
finite-field equality carries theorem responsibility.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path

N = 6
PAIRS = tuple(combinations(range(N), 2))
LABELS = (8, 16, 24)
BASE_SUPPORT = (1, 3)
TARGET_PURE = (Fraction(0), Fraction(1), Fraction(1), Fraction(0))

Vector = tuple[Fraction, ...]
IntVector = tuple[int, ...]


def sign_value(label: int, row: int) -> int:
    if row == 0:
        return 1
    return -1 if (label >> (row - 1)) & 1 else 1


def local_pattern(label: int) -> tuple[int, int, int]:
    return (sign_value(label, 0), sign_value(label, 4), sign_value(label, 5))


def local_pure(left: int, right: int) -> Vector:
    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    left_difference = (
        left_pattern[1] - left_pattern[0],
        left_pattern[2] - left_pattern[0],
    )
    right_difference = (
        right_pattern[1] - right_pattern[0],
        right_pattern[2] - right_pattern[0],
    )
    return tuple(
        Fraction(left_difference[row] * right_difference[column])
        for row in range(2)
        for column in range(2)
    )


def local_lower(left: int, right: int) -> Vector:
    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    constant = Fraction(left_pattern[0] * right_pattern[0])
    return (
        constant,
        Fraction(left_pattern[1] * right_pattern[0]) - constant,
        Fraction(left_pattern[2] * right_pattern[0]) - constant,
        Fraction(left_pattern[0] * right_pattern[1]) - constant,
        Fraction(left_pattern[0] * right_pattern[2]) - constant,
    )


ATOMS = tuple((left, right) for left in LABELS for right in LABELS)
PURE_COLUMNS = tuple(local_pure(*atom) for atom in ATOMS)
LOWER_COLUMNS = tuple(local_lower(*atom) for atom in ATOMS)
LOCAL_ORDINARY_COLUMNS: tuple[Vector, ...] = (
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(-2), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(-2), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(-2), Fraction(-2), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(-2), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(-2)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(-2), Fraction(-2)),
)


def affine_solution(
    columns: tuple[Vector, ...],
    target: Vector,
) -> tuple[Vector, tuple[Vector, ...]] | None:
    row_count = len(target)
    column_count = len(columns)
    data = [
        [
            Fraction(columns[column][row])
            for column in range(column_count)
        ]
        + [Fraction(target[row])]
        for row in range(row_count)
    ]

    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if data[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        scale = data[pivot_row][column]
        data[pivot_row] = [value / scale for value in data[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            coefficient = data[row][column]
            if coefficient:
                data[row] = [
                    data[row][entry]
                    - coefficient * data[pivot_row][entry]
                    for entry in range(column_count + 1)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    for row in range(pivot_row, row_count):
        if (
            all(data[row][column] == 0 for column in range(column_count))
            and data[row][column_count] != 0
        ):
            return None

    free_columns = [
        column
        for column in range(column_count)
        if column not in pivot_columns
    ]
    base = [Fraction(0) for _ in range(column_count)]
    for row, column in enumerate(pivot_columns):
        base[column] = data[row][column_count]

    directions: list[Vector] = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = Fraction(1)
        for row, column in enumerate(pivot_columns):
            vector[column] = -data[row][free_column]
        directions.append(tuple(vector))
    return tuple(base), tuple(directions)


def linear_combination(
    columns: tuple[Vector, ...],
    coefficients: Vector,
) -> Vector:
    if not columns:
        return ()
    return tuple(
        sum(
            (
                coefficients[column] * columns[column][coordinate]
                for column in range(len(columns))
            ),
            Fraction(0),
        )
        for coordinate in range(len(columns[0]))
    )


def matrix_rank(columns: tuple[Vector, ...]) -> int:
    if not columns:
        return 0
    zero = tuple(Fraction(0) for _ in range(len(columns[0])))
    solution = affine_solution(columns, zero)
    if solution is None:
        raise AssertionError("homogeneous system cannot be inconsistent")
    return len(columns) - len(solution[1])


def independent_basis(vectors: tuple[Vector, ...]) -> tuple[Vector, ...]:
    basis: list[Vector] = []
    rank = 0
    for vector in vectors:
        candidate = tuple(basis + [vector])
        new_rank = matrix_rank(candidate)
        if new_rank > rank:
            basis.append(vector)
            rank = new_rank
    return tuple(basis)


def affine_image(
    source_columns: tuple[Vector, ...],
    base: Vector,
    directions: tuple[Vector, ...],
) -> tuple[Vector, tuple[Vector, ...]]:
    image_base = linear_combination(source_columns, base)
    images = tuple(
        linear_combination(source_columns, direction)
        for direction in directions
    )
    return image_base, independent_basis(
        tuple(vector for vector in images if any(vector))
    )


def span_contains(columns: tuple[Vector, ...], vector: Vector) -> bool:
    return affine_solution(columns, vector) is not None


def affine_contained(
    source_base: Vector,
    source_directions: tuple[Vector, ...],
    target_base: Vector,
    target_directions: tuple[Vector, ...],
) -> bool:
    delta = tuple(
        source_base[index] - target_base[index]
        for index in range(len(source_base))
    )
    return span_contains(target_directions, delta) and all(
        span_contains(target_directions, direction)
        for direction in source_directions
    )


def exact_support_possible(
    base: Vector,
    directions: tuple[Vector, ...],
) -> bool:
    for coordinate in range(len(base)):
        if base[coordinate] == 0 and all(
            direction[coordinate] == 0 for direction in directions
        ):
            return False
    return True


def lower_support_minimum(vector: Vector) -> int:
    for size in range(len(LOCAL_ORDINARY_COLUMNS) + 1):
        for indices in combinations(range(len(LOCAL_ORDINARY_COLUMNS)), size):
            columns = tuple(
                LOCAL_ORDINARY_COLUMNS[index] for index in indices
            )
            if span_contains(columns, vector):
                return size
    raise AssertionError(vector)


def local_normal_form_certificate() -> dict[str, object]:
    spaces: list[dict[str, object]] = []
    histogram: Counter[tuple[int, int]] = Counter()
    for size in range(1, len(ATOMS) + 1):
        for indices in combinations(range(len(ATOMS)), size):
            pure_columns = tuple(PURE_COLUMNS[index] for index in indices)
            solution = affine_solution(pure_columns, TARGET_PURE)
            if solution is None:
                continue
            base, directions = solution
            if not exact_support_possible(base, directions):
                continue
            lower_columns = tuple(LOWER_COLUMNS[index] for index in indices)
            lower_base, lower_directions = affine_image(
                lower_columns,
                base,
                directions,
            )
            histogram[(size, len(lower_directions))] += 1
            spaces.append(
                {
                    "size": size,
                    "indices": indices,
                    "base": base,
                    "directions": directions,
                    "lower_base": lower_base,
                    "lower_directions": lower_directions,
                }
            )

    expected_histogram = {
        (2, 0): 1,
        (3, 0): 11,
        (4, 0): 20,
        (4, 1): 10,
        (5, 1): 77,
        (5, 2): 2,
        (6, 2): 76,
        (7, 3): 36,
        (8, 4): 9,
        (9, 5): 1,
    }
    if dict(histogram) != expected_histogram:
        raise AssertionError((histogram, expected_histogram))

    low_spaces = [space for space in spaces if space["size"] in (2, 3)]
    ordinary_subsets: dict[int, list[tuple[Vector, ...]]] = {}
    for size in range(len(LOCAL_ORDINARY_COLUMNS) + 1):
        ordinary_subsets[size] = [
            tuple(
                LOCAL_ORDINARY_COLUMNS[index] for index in indices
            )
            for indices in combinations(range(len(LOCAL_ORDINARY_COLUMNS)), size)
        ]

    exceptions: list[dict[str, object]] = []
    compressed = 0
    for source in spaces:
        if source["size"] <= 3:
            continue
        found = False
        for candidate in low_spaces:
            allowance = source["size"] - candidate["size"]
            if allowance < 0:
                continue
            for lower_size in range(allowance + 1):
                for lower_directions in ordinary_subsets[lower_size]:
                    if affine_contained(
                        source["lower_base"],
                        source["lower_directions"],
                        candidate["lower_base"],
                        lower_directions,
                    ):
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            compressed += 1
        else:
            exceptions.append(source)

    expected_exception_indices = {
        (0, 5, 7, 8),
        (2, 4, 6, 8),
        (0, 2, 4, 6, 8),
        (0, 4, 5, 7, 8),
    }
    if {space["indices"] for space in exceptions} != expected_exception_indices:
        raise AssertionError([space["indices"] for space in exceptions])
    if compressed != 227:
        raise AssertionError(compressed)

    baseline = next(
        space for space in low_spaces if space["indices"] == BASE_SUPPORT
    )
    size_three_spaces = [space for space in low_spaces if space["size"] == 3]
    beneficial: list[IntVector] = []
    trivial = 0
    for space in size_three_spaces:
        difference = tuple(
            space["lower_base"][index] - baseline["lower_base"][index]
            for index in range(5)
        )
        minimum = lower_support_minimum(difference)
        scaled = tuple(int(4 * value) for value in difference)
        if minimum == 1:
            trivial += 1
        else:
            beneficial.append(scaled)
    if trivial != 4:
        raise AssertionError(trivial)
    expected_beneficial = {
        (-2, 2, 0, 2, 0),
        (-3, 2, 2, 2, 2),
        (0, -2, 0, 2, 0),
        (0, 0, 2, 0, -2),
        (0, 2, 0, -2, 0),
        (0, 0, -2, 0, 2),
        (-2, 0, 2, 0, 2),
    }
    if set(beneficial) != expected_beneficial:
        raise AssertionError(beneficial)

    point_cost_two: list[IntVector] = []
    affine_cost_three: list[dict[str, IntVector]] = []
    for space in exceptions:
        difference_base = tuple(
            space["lower_base"][index] - baseline["lower_base"][index]
            for index in range(5)
        )
        scaled_base = tuple(int(4 * value) for value in difference_base)
        if space["size"] == 4:
            point_cost_two.append(scaled_base)
        else:
            if len(space["lower_directions"]) != 1:
                raise AssertionError(space)
            scaled_direction = tuple(
                int(4 * value) for value in space["lower_directions"][0]
            )
            affine_cost_three.append(
                {"base": scaled_base, "direction": scaled_direction}
            )

    expected_cost_two = {
        (-4, 4, 2, 4, 2),
        (-4, 2, 4, 2, 4),
    }
    if set(point_cost_two) != expected_cost_two:
        raise AssertionError(point_cost_two)
    expected_affine = {
        ((-2, 2, 0, 2, 0), (-4, 0, 8, 0, 8)),
        ((-2, 0, 2, 0, 2), (-4, 8, 0, 8, 0)),
    }
    if {
        (row["base"], row["direction"])
        for row in affine_cost_three
    } != expected_affine:
        raise AssertionError(affine_cost_three)

    return {
        "exact_local_support_space_count": len(spaces),
        "support_space_histogram": {
            f"size_{size}_affine_dimension_{dimension}": count
            for (size, dimension), count in sorted(histogram.items())
        },
        "compressed_support_spaces_size_at_least_four": compressed,
        "exception_supports": [list(space["indices"]) for space in exceptions],
        "trivial_size_three_types_absorbed_as_one_ordinary_atom": trivial,
        "cost_one_point_bundle_types": [
            list(vector) for vector in sorted(beneficial)
        ],
        "cost_two_point_bundle_types": [
            list(vector) for vector in sorted(point_cost_two)
        ],
        "cost_three_affine_bundle_types": [
            {
                "base": list(row["base"]),
                "direction": list(row["direction"]),
            }
            for row in sorted(
                affine_cost_three,
                key=lambda row: (row["base"], row["direction"]),
            )
        ],
    }


def embed(edge: tuple[int, int], local: IntVector) -> IntVector:
    left, right = edge
    out = [0] * 13
    out[0] = local[0]
    out[1 + 2 * left] = local[1]
    out[2 + 2 * left] = local[2]
    out[1 + 2 * right] = local[3]
    out[2 + 2 * right] = local[4]
    return tuple(out)


def add_vectors(*vectors: IntVector) -> IntVector:
    if not vectors:
        return (0,) * 13
    return tuple(sum(values) for values in zip(*vectors))


def subtract(left: IntVector, right: IntVector) -> IntVector:
    return tuple(a - b for a, b in zip(left, right))


def ordinary_minimum(vector: IntVector) -> int:
    constant = Fraction(vector[0], 4)
    possible_constants = {Fraction(0)}
    support = 0
    for vertex in range(N):
        x_value = Fraction(vector[1 + 2 * vertex], 4)
        y_value = Fraction(vector[2 + 2 * vertex], 4)
        if x_value == 0 and y_value == 0:
            local_support = 0
            local_constants = {Fraction(0)}
        elif y_value == 0:
            local_support = 1
            local_constants = {-x_value / 2}
        elif x_value == 0:
            local_support = 1
            local_constants = {-y_value / 2}
        elif x_value == y_value:
            local_support = 1
            local_constants = {-x_value / 2}
        else:
            local_support = 2
            local_constants = {
                -x_value / 2,
                -y_value / 2,
                -(x_value + y_value) / 2,
            }
        support += local_support
        possible_constants = {
            existing + local
            for existing in possible_constants
            for local in local_constants
        }
    return support if constant in possible_constants else support + 1


def ordinary_at_most_one(vector: IntVector) -> bool:
    nonzero: list[tuple[int, int]] = []
    for vertex in range(N):
        x_value = vector[1 + 2 * vertex]
        y_value = vector[2 + 2 * vertex]
        if x_value or y_value:
            nonzero.append((x_value, y_value))
            if len(nonzero) > 1:
                return False
    if not nonzero:
        return True
    x_value, y_value = nonzero[0]
    if y_value == 0:
        return 2 * vector[0] == -x_value
    if x_value == 0:
        return 2 * vector[0] == -y_value
    if x_value == y_value:
        return 2 * vector[0] == -x_value
    return False


def affine_in_ordinary_span(
    base: IntVector,
    direction: IntVector,
    ordinary_indices: tuple[int, ...],
    ordinary_columns: tuple[IntVector, ...],
) -> bool:
    columns = (
        tuple(Fraction(value) for value in direction),
    ) + tuple(
        tuple(Fraction(value) for value in ordinary_columns[index])
        for index in ordinary_indices
    )
    target = tuple(Fraction(-value) for value in base)
    return affine_solution(columns, target) is not None


def affine_hits_zero(base: IntVector, direction: IntVector) -> bool:
    parameter: Fraction | None = None
    for value, slope in zip(base, direction):
        if slope == 0:
            if value != 0:
                return False
            continue
        candidate = Fraction(-value, slope)
        if parameter is None:
            parameter = candidate
        elif candidate != parameter:
            return False
    return True


def global_search_certificate(
    normal_forms: dict[str, object],
) -> dict[str, object]:
    cost_one_local = tuple(
        tuple(row) for row in normal_forms["cost_one_point_bundle_types"]
    )
    cost_two_local = tuple(
        tuple(row) for row in normal_forms["cost_two_point_bundle_types"]
    )
    affine_local = tuple(
        (tuple(row["base"]), tuple(row["direction"]))
        for row in normal_forms["cost_three_affine_bundle_types"]
    )

    cost_one: list[tuple[int, IntVector]] = []
    cost_two: list[tuple[int, IntVector]] = []
    affine: list[tuple[int, IntVector, IntVector]] = []
    for edge_index, edge in enumerate(PAIRS):
        cost_one.extend(
            (edge_index, embed(edge, local)) for local in cost_one_local
        )
        cost_two.extend(
            (edge_index, embed(edge, local)) for local in cost_two_local
        )
        affine.extend(
            (
                edge_index,
                embed(edge, base),
                embed(edge, direction),
            )
            for base, direction in affine_local
        )

    if (len(cost_one), len(cost_two), len(affine)) != (105, 30, 30):
        raise AssertionError((len(cost_one), len(cost_two), len(affine)))

    ordinary_columns: list[IntVector] = []
    constant = [0] * 13
    constant[0] = 1
    ordinary_columns.append(tuple(constant))
    for vertex in range(N):
        for label in LABELS:
            vector = [0] * 13
            vector[0] = 1
            if label & 8:
                vector[1 + 2 * vertex] = -2
            if label & 16:
                vector[2 + 2 * vertex] = -2
            ordinary_columns.append(tuple(vector))
    ordinary_columns_tuple = tuple(ordinary_columns)
    if len(ordinary_columns_tuple) != 19:
        raise AssertionError(len(ordinary_columns_tuple))

    target = (-30,) + (10,) * 12
    if ordinary_minimum(target) != 6:
        raise AssertionError(ordinary_minimum(target))

    minima: dict[str, int] = {"no_bundle": ordinary_minimum(target)}
    counts: dict[str, int] = {}

    for size in (1, 2, 3):
        minimum = 99
        count = 0
        for indices in combinations(range(len(cost_one)), size):
            edges = {cost_one[index][0] for index in indices}
            if len(edges) != size:
                continue
            total = add_vectors(
                *(cost_one[index][1] for index in indices)
            )
            residual = subtract(target, total)
            minimum = min(
                minimum,
                size + ordinary_minimum(residual),
            )
            count += 1
        expected_count = comb(15, size) * 7**size
        if count != expected_count:
            raise AssertionError((size, count, expected_count))
        minima[f"cost_one_bundle_count_{size}"] = minimum
        counts[f"cost_one_bundle_count_{size}"] = count

    count_four = 0
    violation_four = False
    for indices in combinations(range(len(cost_one)), 4):
        edges = {cost_one[index][0] for index in indices}
        if len(edges) != 4:
            continue
        total = add_vectors(*(cost_one[index][1] for index in indices))
        residual = subtract(target, total)
        if ordinary_at_most_one(residual):
            violation_four = True
            break
        count_four += 1
    expected_four = comb(15, 4) * 7**4
    if violation_four or count_four != expected_four:
        raise AssertionError((violation_four, count_four, expected_four))
    counts["cost_one_bundle_count_4"] = count_four

    two_sums: dict[IntVector, list[int]] = defaultdict(list)
    count_two = 0
    for left, right in combinations(range(len(cost_one)), 2):
        edge_left = cost_one[left][0]
        edge_right = cost_one[right][0]
        if edge_left == edge_right:
            continue
        vector = add_vectors(cost_one[left][1], cost_one[right][1])
        mask = (1 << edge_left) | (1 << edge_right)
        two_sums[vector].append(mask)
        count_two += 1
    if count_two != comb(15, 2) * 7**2:
        raise AssertionError(count_two)

    count_three = 0
    five_violation = False
    three_sums: dict[IntVector, list[int]] = defaultdict(list)
    for indices in combinations(range(len(cost_one)), 3):
        edges = [cost_one[index][0] for index in indices]
        if len(set(edges)) != 3:
            continue
        vector = add_vectors(*(cost_one[index][1] for index in indices))
        mask = sum(1 << edge for edge in edges)
        three_sums[vector].append(mask)
        complement = subtract(target, vector)
        for two_mask in two_sums.get(complement, ()):
            if not (two_mask & mask):
                five_violation = True
                break
        if five_violation:
            break
        count_three += 1
    expected_three = comb(15, 3) * 7**3
    if five_violation or count_three != expected_three:
        raise AssertionError((five_violation, count_three, expected_three))
    counts["cost_one_bundle_count_5_covered_by_meet_in_middle"] = (
        comb(15, 5) * 7**5
    )
    counts["cost_one_two_sum_count"] = count_two
    counts["cost_one_three_sum_count"] = count_three

    minimum_one_cost_two = 99
    count_one_cost_two_plus_one = 0
    for edge_two, vector_two in cost_two:
        minimum_one_cost_two = min(
            minimum_one_cost_two,
            2 + ordinary_minimum(subtract(target, vector_two)),
        )
        for edge_one, vector_one in cost_one:
            if edge_one == edge_two:
                continue
            minimum_one_cost_two = min(
                minimum_one_cost_two,
                3
                + ordinary_minimum(
                    subtract(target, add_vectors(vector_two, vector_one))
                ),
            )
            count_one_cost_two_plus_one += 1
    if count_one_cost_two_plus_one != 30 * 14 * 7:
        raise AssertionError(count_one_cost_two_plus_one)
    minima[
        "one_cost_two_bundle_with_at_most_one_cost_one_bundle"
    ] = minimum_one_cost_two
    counts["one_cost_two_plus_one_cost_one"] = count_one_cost_two_plus_one

    count_cost_two_plus_two_one = 0
    violation = False
    for edge_two, vector_two in cost_two:
        valid = [
            index
            for index, (edge, _) in enumerate(cost_one)
            if edge != edge_two
        ]
        for left, right in combinations(valid, 2):
            if cost_one[left][0] == cost_one[right][0]:
                continue
            residual = subtract(
                target,
                add_vectors(
                    vector_two,
                    cost_one[left][1],
                    cost_one[right][1],
                ),
            )
            if ordinary_at_most_one(residual):
                violation = True
                break
            count_cost_two_plus_two_one += 1
        if violation:
            break
    expected = 30 * comb(14, 2) * 7**2
    if violation or count_cost_two_plus_two_one != expected:
        raise AssertionError(
            (violation, count_cost_two_plus_two_one, expected)
        )
    counts["one_cost_two_plus_two_cost_one"] = (
        count_cost_two_plus_two_one
    )

    violation = False
    for edge_two, vector_two in cost_two:
        complement = subtract(target, vector_two)
        for mask in three_sums.get(complement, ()):
            if not (mask & (1 << edge_two)):
                violation = True
                break
        if violation:
            break
    if violation:
        raise AssertionError(
            "one cost-two plus three cost-one bundles reaches the target"
        )
    counts["one_cost_two_plus_three_cost_one_covered_by_hash"] = (
        30 * comb(14, 3) * 7**3
    )

    count_two_cost_two = 0
    count_two_cost_two_plus_one = 0
    violation_two = False
    violation_two_plus_one = False
    for left, right in combinations(range(len(cost_two)), 2):
        edge_left = cost_two[left][0]
        edge_right = cost_two[right][0]
        if edge_left == edge_right:
            continue
        total = add_vectors(cost_two[left][1], cost_two[right][1])
        residual = subtract(target, total)
        if ordinary_at_most_one(residual):
            violation_two = True
            break
        count_two_cost_two += 1
        for edge_one, vector_one in cost_one:
            if edge_one in (edge_left, edge_right):
                continue
            if add_vectors(total, vector_one) == target:
                violation_two_plus_one = True
                break
            count_two_cost_two_plus_one += 1
        if violation_two_plus_one:
            break
    expected_two = comb(15, 2) * 2**2
    expected_two_plus_one = expected_two * 13 * 7
    if (
        violation_two
        or violation_two_plus_one
        or count_two_cost_two != expected_two
        or count_two_cost_two_plus_one != expected_two_plus_one
    ):
        raise AssertionError(
            (
                violation_two,
                violation_two_plus_one,
                count_two_cost_two,
                expected_two,
                count_two_cost_two_plus_one,
                expected_two_plus_one,
            )
        )
    counts["two_cost_two_bundles"] = count_two_cost_two
    counts["two_cost_two_plus_one_cost_one"] = count_two_cost_two_plus_one

    affine_no_other_tests = 0
    affine_plus_one_tests = 0
    affine_plus_two_tests = 0
    affine_plus_cost_two_tests = 0
    affine_violation = False
    ordinary_supports_up_to_two = [
        indices
        for size in range(3)
        for indices in combinations(range(len(ordinary_columns_tuple)), size)
    ]
    ordinary_supports_up_to_one = [
        indices
        for size in range(2)
        for indices in combinations(range(len(ordinary_columns_tuple)), size)
    ]
    for affine_edge, affine_base, affine_direction in affine:
        residual_base = subtract(target, affine_base)
        for indices in ordinary_supports_up_to_two:
            affine_no_other_tests += 1
            if affine_in_ordinary_span(
                residual_base,
                tuple(-value for value in affine_direction),
                indices,
                ordinary_columns_tuple,
            ):
                affine_violation = True
                break
        if affine_violation:
            break

        for edge_one, vector_one in cost_one:
            if edge_one == affine_edge:
                continue
            residual = subtract(
                target,
                add_vectors(affine_base, vector_one),
            )
            for indices in ordinary_supports_up_to_one:
                affine_plus_one_tests += 1
                if affine_in_ordinary_span(
                    residual,
                    tuple(-value for value in affine_direction),
                    indices,
                    ordinary_columns_tuple,
                ):
                    affine_violation = True
                    break
            if affine_violation:
                break
        if affine_violation:
            break

        valid = [
            index
            for index, (edge, _) in enumerate(cost_one)
            if edge != affine_edge
        ]
        for left, right in combinations(valid, 2):
            if cost_one[left][0] == cost_one[right][0]:
                continue
            residual = subtract(
                target,
                add_vectors(
                    affine_base,
                    cost_one[left][1],
                    cost_one[right][1],
                ),
            )
            affine_plus_two_tests += 1
            if affine_hits_zero(
                residual,
                tuple(-value for value in affine_direction),
            ):
                affine_violation = True
                break
        if affine_violation:
            break

        for edge_two, vector_two in cost_two:
            if edge_two == affine_edge:
                continue
            residual = subtract(
                target,
                add_vectors(affine_base, vector_two),
            )
            affine_plus_cost_two_tests += 1
            if affine_hits_zero(
                residual,
                tuple(-value for value in affine_direction),
            ):
                affine_violation = True
                break
        if affine_violation:
            break

    expected_affine_no_other = 30 * (1 + 19 + comb(19, 2))
    expected_affine_plus_one = 30 * 14 * 7 * (1 + 19)
    expected_affine_plus_two = 30 * comb(14, 2) * 7**2
    expected_affine_plus_cost_two = 30 * 14 * 2
    if (
        affine_violation
        or affine_no_other_tests != expected_affine_no_other
        or affine_plus_one_tests != expected_affine_plus_one
        or affine_plus_two_tests != expected_affine_plus_two
        or affine_plus_cost_two_tests != expected_affine_plus_cost_two
    ):
        raise AssertionError(
            (
                affine_violation,
                affine_no_other_tests,
                expected_affine_no_other,
                affine_plus_one_tests,
                expected_affine_plus_one,
                affine_plus_two_tests,
                expected_affine_plus_two,
                affine_plus_cost_two_tests,
                expected_affine_plus_cost_two,
            )
        )
    counts["affine_no_other_exact_span_tests"] = affine_no_other_tests
    counts["affine_plus_one_cost_one_exact_span_tests"] = (
        affine_plus_one_tests
    )
    counts["affine_plus_two_cost_one_exact_zero_tests"] = (
        affine_plus_two_tests
    )
    counts["affine_plus_one_cost_two_exact_zero_tests"] = (
        affine_plus_cost_two_tests
    )

    if min(minima.values()) != 6:
        raise AssertionError(minima)

    return {
        "baseline_pair_atom_count": 30,
        "ordinary_correction_minimum_without_bundles": 6,
        "minimum_total_extra_cost_in_directly_enumerated_small_cases": min(
            minima.values()
        ),
        "small_case_minima": minima,
        "coverage_counts": counts,
        "support_at_most_35_counterexample_found": False,
        "lower_bound": 36,
    }


def projection_certificate() -> dict[str, object]:
    checks = 0
    for label in range(32):
        projected = label & 24
        for row in range(6):
            retracted_row = row if row in (0, 4, 5) else 0
            if sign_value(label, retracted_row) != sign_value(projected, row):
                raise AssertionError((label, row))
            checks += 1
    for assignment in product(range(6), repeat=6):
        retracted = tuple(
            value if value in (0, 4, 5) else 0 for value in assignment
        )
        left = assignment.count(4) * assignment.count(5)
        right = retracted.count(4) * retracted.count(5)
        if left != right:
            raise AssertionError(assignment)
    return {
        "sign_vector_checks": checks,
        "separator_assignment_checks": 6**6,
        "label_projection": "v -> v & 24",
        "row_retraction": "1,2,3 -> 0; 0,4,5 fixed",
        "support_nonincrease": True,
    }


def upper_bound_certificate() -> dict[str, object]:
    atoms: list[tuple[Fraction, tuple[int, ...], tuple[int, ...]]] = []
    for left, right in PAIRS:
        atoms.append((Fraction(1, 4), (left, right), (8, 16)))
        atoms.append((Fraction(1, 4), (left, right), (16, 8)))
    for position in range(6):
        atoms.append((Fraction(-5, 4), (position,), (24,)))
    if len(atoms) != 36:
        raise AssertionError(len(atoms))

    checks = 0
    for assignment in product(range(6), repeat=6):
        observed = Fraction(0)
        for coefficient, positions, labels in atoms:
            value = coefficient
            for position, label in zip(positions, labels, strict=True):
                value *= sign_value(label, assignment[position])
            observed += value
        expected = Fraction(assignment.count(4) * assignment.count(5))
        if observed != expected:
            raise AssertionError((assignment, observed, expected))
        checks += 1
    return {"atom_count": len(atoms), "exact_assignment_checks": checks}


def build_payload() -> dict[str, object]:
    projection = projection_certificate()
    normal_forms = local_normal_form_certificate()
    search = global_search_certificate(normal_forms)
    upper = upper_bound_certificate()
    if search["lower_bound"] != upper["atom_count"]:
        raise AssertionError((search, upper))
    return {
        "status": "N6_FIXED_BASE_TWO_DEFECT_SEPARATOR_ATOMIC_RANK_EXACT_36",
        "field": "characteristic zero",
        "separator": "g(r)=n_4(r)*n_5(r)",
        "projection_certificate": projection,
        "local_normal_form_certificate": normal_forms,
        "global_support_search_certificate": search,
        "upper_bound_certificate": upper,
        "exact_atomic_rank": 36,
        "sixteen_base_assignment_actual_term_cost": 16 * 36,
        "claim_boundary": (
            "The exact rank 36 is for one fixed-base separator and, by the "
            "row retraction, for the full fixed-base two-defect sign "
            "dictionary. It does not determine the minimum support of "
            "perm_6 in the global two-defect family or unrestricted Chow "
            "rank."
        ),
    }


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
    print("N6_TWO_DEFECT_SEPARATOR_RANK36_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
