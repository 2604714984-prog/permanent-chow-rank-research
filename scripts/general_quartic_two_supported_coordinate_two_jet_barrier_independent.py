#!/usr/bin/env python3
"""Independent modular replay of the two-supported coordinate two-jet barrier.

This implementation imports neither the primary verifier nor its symbolic
kernel certificate.  It reconstructs the first-order equation matrices and
quadratic matching tables over the strict prime 1,000,003.  Every symbolic
normal-form chart is evaluated at two deterministic generic parameter points.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations

PRIME = 1_000_003
ORDER = 4
PARAMETERS_PER_COMPONENT = 111
SUBSETS = tuple(combinations(range(6), 4))

CYCLE_EXPECTED = (
    ((0, 1, 3, 2, 4, 5), 330, 336, 562),
    ((0, 1, 3, 2, 8, 6), 344, 322, 487),
    ((0, 1, 3, 2, 8, 14), 344, 322, 487),
    ((0, 1, 3, 2, 12, 6), 344, 322, 493),
    ((0, 1, 3, 2, 23, 21), 343, 323, 488),
    ((0, 1, 3, 5, 4, 2), 330, 336, 562),
    ((0, 1, 3, 5, 11, 6), 344, 322, 493),
    ((0, 1, 3, 5, 16, 14), 343, 323, 488),
    ((0, 1, 3, 5, 19, 21), 344, 322, 487),
    ((0, 1, 3, 9, 8, 6), 348, 318, 462),
    ((0, 1, 3, 9, 11, 6), 348, 318, 462),
    ((0, 1, 3, 13, 12, 6), 348, 318, 462),
    ((0, 1, 3, 22, 8, 6), 348, 318, 448),
)

CHART_EXPECTED = {
    "tight_handcuff_full_character_rank": (
        ((0, 3, 4, 1, 2), 286, 380, ()),
        ((0, 3, 7, 9, 1), 290, 376, (15,)),
        ((0, 3, 7, 13, 1), 290, 376, (15,)),
        ((0, 3, 8, 9, 2), 290, 376, (23,)),
    ),
    "tight_handcuff_deficient_character_rank": (
        ((0, 3, 11, 9, 5), 288, 378, (4, 16, 19)),
    ),
    "loose_handcuff_full_character_rank": (
        ((0, 3, 4, 1, 2), 285, 381, ()),
        ((0, 3, 4, 1, 5), 285, 381, ()),
        ((0, 3, 7, 1, 2), 289, 377, (4,)),
        ((0, 3, 7, 1, 5), 289, 377, (4,)),
        ((0, 3, 7, 9, 2), 293, 373, ()),
        ((0, 3, 7, 9, 5), 293, 373, ()),
        ((0, 3, 7, 13, 2), 293, 373, ()),
        ((0, 3, 8, 2, 1), 289, 377, (4,)),
        ((0, 3, 8, 2, 5), 289, 377, (4,)),
        ((0, 3, 8, 9, 1), 293, 373, ()),
        ((0, 3, 8, 9, 5), 293, 373, ()),
        ((0, 3, 8, 22, 5), 293, 373, ()),
        ((0, 3, 11, 5, 1), 289, 377, (4,)),
        ((0, 3, 11, 5, 2), 289, 377, (4,)),
        ((0, 3, 11, 9, 1), 293, 373, ()),
        ((0, 3, 11, 9, 2), 293, 373, ()),
        ((0, 7, 16, 10, 1), 293, 373, ()),
    ),
    "loose_handcuff_deficient_character_rank": (
        ((0, 3, 11, 9, 5), 288, 378, ()),
    ),
    "theta_full_character_rank": (
        ((0, 3, 4, 1, 2), 287, 379, ()),
    ),
    "six_cycle_deficient_character_rank": (
        ((0, 1, 3, 2, 4, 5), 330, 336, ()),
        ((0, 1, 3, 2, 23, 21), 343, 323, ()),
        ((0, 1, 3, 5, 4, 2), 330, 336, ()),
        ((0, 1, 3, 5, 16, 14), 343, 323, ()),
    ),
}

CHART_SAMPLES = {
    "tight_handcuff_full_character_rank": ((1, 1), (2, 3)),
    "tight_handcuff_deficient_character_rank": ((1, 1, 2), (2, 3, 5)),
    "loose_handcuff_full_character_rank": ((2, 1), (3, 2)),
    "loose_handcuff_deficient_character_rank": ((2, 1, 2), (3, 2, 5)),
    "theta_full_character_rank": ((1, 2), (2, 4)),
    "six_cycle_deficient_character_rank": ((2,), (3,)),
}


def fail(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def add_mod(table: dict, key: object, value: int) -> None:
    value %= PRIME
    if not value:
        return
    updated = (table.get(key, 0) + value) % PRIME
    if updated:
        table[key] = updated
    elif key in table:
        del table[key]


def matching(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(4 * row + permutation[row] for row in range(4)))


def adjacent(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return sum(a == b for a, b in zip(left, right, strict=True)) == 2


def component_columns(
    left: tuple[int, ...],
    right: tuple[int, ...],
    left_coefficient: int,
    right_coefficient: int,
) -> tuple[
    tuple[dict[tuple[int, ...], int], ...],
    tuple[int, ...],
    tuple[int, ...],
]:
    left_edges = set(matching(left))
    right_edges = set(matching(right))
    frame = tuple(sorted(left_edges | right_edges))
    fail(len(frame) == 6, frame)
    left_labels = tuple(sorted(frame.index(edge) for edge in left_edges))
    right_labels = tuple(sorted(frame.index(edge) for edge in right_edges))
    base = [0] * 15
    base[SUBSETS.index(left_labels)] = left_coefficient % PRIME
    base[SUBSETS.index(right_labels)] = right_coefficient % PRIME

    columns: list[dict[tuple[int, ...], int]] = []
    for subset in SUBSETS:
        columns.append({tuple(sorted(frame[label] for label in subset)): 1})
    for label in range(6):
        for variable in range(16):
            output: dict[tuple[int, ...], int] = {}
            for subset_index, subset in enumerate(SUBSETS):
                coefficient = base[subset_index]
                if coefficient and label in subset:
                    monomial = tuple(
                        sorted(
                            [frame[item] for item in subset if item != label]
                            + [variable]
                        )
                    )
                    add_mod(output, monomial, coefficient)
            columns.append(output)
    fail(len(columns) == PARAMETERS_PER_COMPONENT, len(columns))
    return tuple(columns), frame, tuple(base)


def sparse_nullspace(
    columns: tuple[dict[tuple[int, ...], int], ...]
) -> tuple[int, tuple[dict[int, int], ...]]:
    equations: dict[tuple[int, ...], dict[int, int]] = defaultdict(dict)
    for parameter, column in enumerate(columns):
        for monomial, coefficient in column.items():
            add_mod(equations[monomial], parameter, coefficient)
    rows = [row for _, row in sorted(equations.items()) if row]
    pivot_rows: dict[int, dict[int, int]] = {}
    active_row = 0
    for parameter in range(len(columns)):
        pivot = next(
            (
                index
                for index in range(active_row, len(rows))
                if rows[index].get(parameter, 0)
            ),
            None,
        )
        if pivot is None:
            continue
        rows[active_row], rows[pivot] = rows[pivot], rows[active_row]
        row = rows[active_row]
        reciprocal = pow(row[parameter], PRIME - 2, PRIME)
        row = {
            column: coefficient * reciprocal % PRIME
            for column, coefficient in row.items()
            if coefficient % PRIME
        }
        rows[active_row] = row
        for index, other in enumerate(rows):
            if index == active_row:
                continue
            factor = other.get(parameter, 0)
            if not factor:
                continue
            for column, coefficient in row.items():
                add_mod(other, column, -factor * coefficient)
        pivot_rows[parameter] = row
        active_row += 1
        if active_row == len(rows):
            break

    pivot_columns = set(pivot_rows)
    free_columns = [
        parameter for parameter in range(len(columns)) if parameter not in pivot_columns
    ]
    kernel = []
    for free in free_columns:
        relation = {free: 1}
        for pivot, row in pivot_rows.items():
            coefficient = row.get(free, 0)
            if coefficient:
                relation[pivot] = (-coefficient) % PRIME
        kernel.append(relation)
    for relation in kernel:
        for row in rows:
            value = sum(
                coefficient * relation.get(parameter, 0)
                for parameter, coefficient in row.items()
            ) % PRIME
            fail(value == 0, value)
    return len(pivot_rows), tuple(kernel)


Packet = tuple[
    tuple[dict[tuple[int, ...], int], ...],
    tuple[int, ...],
    tuple[int, ...],
]


def quadratic_table(
    packets: tuple[Packet, ...],
) -> dict[tuple[int, int], dict[tuple[int, ...], int]]:
    matching_set = {matching(value) for value in permutations(range(4))}
    table: dict[tuple[int, int], dict[tuple[int, ...], int]] = defaultdict(dict)
    for component, (_, frame, base) in enumerate(packets):
        offset = component * PARAMETERS_PER_COMPONENT
        for subset_index, subset in enumerate(SUBSETS):
            base_edges = [frame[label] for label in subset]
            source_parameter = offset + subset_index
            for label in subset:
                for variable in range(16):
                    monomial = tuple(
                        sorted(
                            [edge for edge in base_edges if edge != frame[label]]
                            + [variable]
                        )
                    )
                    if monomial in matching_set:
                        factor_parameter = offset + 15 + 16 * label + variable
                        key = tuple(sorted((source_parameter, factor_parameter)))
                        add_mod(table[key], monomial, 1)
        for subset_index, subset in enumerate(SUBSETS):
            coefficient = base[subset_index]
            if not coefficient:
                continue
            for first_position in range(4):
                first_label = subset[first_position]
                for second_position in range(first_position + 1, 4):
                    second_label = subset[second_position]
                    remainder = [
                        frame[label]
                        for label in subset
                        if label not in (first_label, second_label)
                    ]
                    for first_variable in range(16):
                        for second_variable in range(16):
                            monomial = tuple(
                                sorted(remainder + [first_variable, second_variable])
                            )
                            if monomial in matching_set:
                                first_parameter = (
                                    offset + 15 + 16 * first_label + first_variable
                                )
                                second_parameter = (
                                    offset + 15 + 16 * second_label + second_variable
                                )
                                key = tuple(
                                    sorted((first_parameter, second_parameter))
                                )
                                add_mod(table[key], monomial, coefficient)
    return dict(table)


def bilinear(
    left: dict[int, int],
    right: dict[int, int],
    table: dict[tuple[int, int], dict[tuple[int, ...], int]],
) -> dict[tuple[int, ...], int]:
    output: dict[tuple[int, ...], int] = {}
    for left_parameter, left_coefficient in left.items():
        for right_parameter, right_coefficient in right.items():
            values = table.get(tuple(sorted((left_parameter, right_parameter))))
            if not values:
                continue
            factor = left_coefficient * right_coefficient
            if left_parameter == right_parameter:
                factor *= 2
            for monomial, coefficient in values.items():
                add_mod(output, monomial, factor * coefficient)
    return output


def leading_columns(packets: tuple[Packet, ...]) -> tuple[dict[tuple[int, ...], int], ...]:
    result = []
    for _, frame, base in packets:
        column: dict[tuple[int, ...], int] = {}
        for subset_index, subset in enumerate(SUBSETS):
            coefficient = base[subset_index]
            if coefficient:
                monomial = tuple(sorted(frame[label] for label in subset))
                add_mod(column, monomial, coefficient)
        result.append(column)
    return tuple(result)


def chart_edges(name: str, parameters: tuple[int, ...]) -> tuple[tuple[int, int, int, int], ...]:
    if name == "tight_handcuff_full_character_rank":
        x, y = parameters
        return (
            (0, 4, 1, 1),
            (0, 4, -1, x),
            (1, 3, 1, -1),
            (1, 4, -1, y),
            (2, 3, 1, 1),
            (2, 4, -1, -1 - x - y),
        )
    if name == "tight_handcuff_deficient_character_rank":
        x, y, z = parameters
        return (
            (0, 4, 1, 1),
            (0, 4, -1, x),
            (1, 3, z, -1),
            (1, 4, -z, y),
            (2, 3, 1, 1),
            (2, 4, -1, -1 - x - y),
        )
    if name == "loose_handcuff_full_character_rank":
        x, y = parameters
        return (
            (0, 4, 1, 1),
            (0, 4, -1, y),
            (1, 3, 1, -1),
            (1, 4, -1, -1 - y),
            (2, 3, 1, x),
            (2, 3, -1, 1 - x),
        )
    if name == "loose_handcuff_deficient_character_rank":
        x, y, z = parameters
        return (
            (0, 4, 1, 1),
            (0, 4, -1, y),
            (1, 3, z, -1),
            (1, 4, -z, -1 - y),
            (2, 3, 1, x),
            (2, 3, -1, 1 - x),
        )
    if name == "theta_full_character_rank":
        a, b = parameters
        return (
            (0, 3, -1, 1),
            (1, 3, -1, a),
            (2, 3, -1, -1 - a),
            (0, 4, 1, 1),
            (1, 4, 1, b),
            (2, 4, 1, -1 - b),
        )
    raise RuntimeError(name)


def chart_packets(
    name: str,
    representative: tuple[int, ...],
    parameters: tuple[int, ...],
) -> tuple[Packet, ...]:
    group = tuple(permutations(range(4)))
    values = tuple(group[index] for index in representative)
    if name == "six_cycle_deficient_character_rank":
        (z,) = parameters
        scales = (z, 1, 1, 1, 1, 1)
        return tuple(
            component_columns(
                values[index],
                values[(index + 1) % 6],
                scales[index],
                -scales[(index + 1) % 6],
            )
            for index in range(6)
        )
    return tuple(
        component_columns(values[left], values[right], left_coefficient, right_coefficient)
        for left, right, left_coefficient, right_coefficient in chart_edges(
            name, parameters
        )
    )


def audit_packets(
    packets: tuple[Packet, ...],
    representative: tuple[int, ...],
    expected_rank: int,
    expected_nullity: int,
    expected_outside_indices: tuple[int, ...],
) -> None:
    leading_rank, leading_kernel = sparse_nullspace(leading_columns(packets))
    fail(leading_rank == 5, (representative, leading_rank))
    fail(len(leading_kernel) == 1, (representative, len(leading_kernel)))
    fail(
        all(leading_kernel[0].get(index, 0) for index in range(6)),
        (representative, leading_kernel),
    )

    columns = tuple(column for packet in packets for column in packet[0])
    rank, kernel = sparse_nullspace(columns)
    fail(rank == expected_rank, (representative, rank, expected_rank))
    fail(len(kernel) == expected_nullity, (representative, len(kernel)))
    group = tuple(permutations(range(4)))
    base_support = {matching(group[index]) for index in representative}
    expected_outside = {matching(group[index]) for index in expected_outside_indices}
    table = quadratic_table(packets)
    actual_outside = set()
    for left_index, left in enumerate(kernel):
        for right in kernel[left_index:]:
            output = bilinear(left, right, table)
            actual_outside.update(set(output) - base_support)
    fail(
        actual_outside == expected_outside,
        (representative, actual_outside, expected_outside),
    )
    fail(len(base_support | actual_outside) <= 8, representative)


def replay_unit_cycles() -> None:
    group = tuple(permutations(range(4)))
    for representative, expected_rank, expected_nullity, expected_pairs in CYCLE_EXPECTED:
        cycle = tuple(group[index] for index in representative)
        fail(
            all(
                adjacent(cycle[index], cycle[(index + 1) % 6])
                for index in range(6)
            ),
            representative,
        )
        packets = tuple(
            component_columns(cycle[index], cycle[(index + 1) % 6], 1, -1)
            for index in range(6)
        )
        columns = tuple(column for packet in packets for column in packet[0])
        rank, kernel = sparse_nullspace(columns)
        fail(rank == expected_rank, (representative, rank, expected_rank))
        fail(len(kernel) == expected_nullity, (representative, len(kernel)))
        cycle_support = {matching(value) for value in cycle}
        table = quadratic_table(packets)
        nonzero_pairs = 0
        for left_index, left in enumerate(kernel):
            for right in kernel[left_index:]:
                output = bilinear(left, right, table)
                if output:
                    nonzero_pairs += 1
                    fail(set(output) <= cycle_support, (representative, set(output)))
        fail(nonzero_pairs == expected_pairs, (representative, nonzero_pairs))


def replay_symbolic_charts_at_generic_points() -> None:
    for name, rows in CHART_EXPECTED.items():
        samples = CHART_SAMPLES[name]
        for representative, rank, nullity, outside in rows:
            for parameters in samples:
                packets = chart_packets(name, representative, parameters)
                audit_packets(packets, representative, rank, nullity, outside)


def main() -> None:
    fail(len(CYCLE_EXPECTED) == 13, len(CYCLE_EXPECTED))
    fail(sum(len(rows) for rows in CHART_EXPECTED.values()) == 28, CHART_EXPECTED)
    replay_unit_cycles()
    replay_symbolic_charts_at_generic_points()
    print("GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
