#!/usr/bin/env python3
"""Finite audit for the vector-valued quadratic Macaulay lemma.

The characteristic-zero proof is in
``docs/vector_valued_macaulay_prolongation.md``. This script checks only its
finite combinatorial interfaces:

* explicit separation of all colored quadratic weights for 36 variables and
  six colors;
* the six-part Macaulay partition inequality through total dimension 16; and
* an exhaustive divided-power counterexample search over ``F_2`` for all
  2,825 subspaces when ``dim V=2`` and ``dim W=2``.

The small-field search is diagnostic and is not part of the proof.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path


def macaulay_successor_degree_two(value: int) -> int:
    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def explicit_weight_certificate(
    variables: int = 36,
    colors: int = 6,
) -> dict[str, object]:
    beta = [3**index for index in range(variables)]
    color_stride = 1 + 2 * 3 ** (variables - 1)
    gamma = [color * color_stride for color in range(colors)]
    weights: dict[int, tuple[int, int, int]] = {}
    for color in range(colors):
        for left in range(variables):
            for right in range(left, variables):
                weight = gamma[color] + beta[left] + beta[right]
                if weight in weights:
                    raise AssertionError(
                        (weights[weight], (color, left, right))
                    )
                weights[weight] = (color, left, right)
    expected = colors * comb(variables + 1, 2)
    if len(weights) != expected:
        raise AssertionError((len(weights), expected))
    return {
        "variables": variables,
        "colors": colors,
        "color_stride": color_stride,
        "colored_quadratic_weight_count": len(weights),
        "all_weights_distinct": True,
    }


def partitions_nondecreasing(
    total: int,
    parts: int,
    minimum: int = 0,
):
    if parts == 1:
        if total >= minimum:
            yield (total,)
        return
    for value in range(minimum, total + 1):
        for tail in partitions_nondecreasing(
            total - value,
            parts - 1,
            value,
        ):
            yield (value,) + tail


def partition_certificate(
    maximum_total: int = 16,
    colors: int = 6,
) -> dict[str, object]:
    rows: dict[str, object] = {}
    for total in range(maximum_total + 1):
        target = macaulay_successor_degree_two(total)
        maximum = -1
        maximizers: list[list[int]] = []
        count = 0
        for partition in partitions_nondecreasing(total, colors):
            count += 1
            value = sum(
                macaulay_successor_degree_two(part)
                for part in partition
            )
            if value > maximum:
                maximum = value
                maximizers = [list(partition)]
            elif value == maximum:
                maximizers.append(list(partition))
        if maximum != target:
            raise AssertionError((total, maximum, target, maximizers))
        rows[str(total)] = {
            "partition_count": count,
            "maximum_partition_sum": maximum,
            "scalar_macaulay_successor": target,
            "maximizers": maximizers,
        }
    return rows


def exponent_tuples(
    total: int,
    variables: int,
) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], remaining: int) -> None:
        if len(prefix) == variables - 1:
            out.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            rec(prefix + (value,), remaining - value)

    rec((), total)
    return out


def rref_bits(
    rows: list[int],
    columns: int,
) -> tuple[list[int], list[int]]:
    data = [row for row in rows if row]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(columns):
        pivot = next(
            (
                index
                for index in range(pivot_row, len(data))
                if (data[index] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        for index in range(len(data)):
            if index != pivot_row and ((data[index] >> column) & 1):
                data[index] ^= data[pivot_row]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(data):
            break
    return data[:pivot_row], pivots


def annihilator_basis(rows: list[int], columns: int) -> list[int]:
    reduced, pivots = rref_bits(rows[:], columns)
    free = [column for column in range(columns) if column not in pivots]
    basis: list[int] = []
    for free_column in free:
        vector = 1 << free_column
        for row, pivot in enumerate(pivots):
            if (reduced[row] >> free_column) & 1:
                vector |= 1 << pivot
        basis.append(vector)
    return basis


def rref_subspaces(columns: int, dimension: int):
    if dimension == 0:
        yield []
        return
    for pivots in combinations(range(columns), dimension):
        free = [column for column in range(columns) if column not in pivots]
        slots = [
            (row, column)
            for row, pivot in enumerate(pivots)
            for column in free
            if column > pivot
        ]
        for mask in range(1 << len(slots)):
            rows = [1 << pivot for pivot in pivots]
            for slot, (row, column) in enumerate(slots):
                if (mask >> slot) & 1:
                    rows[row] |= 1 << column
            yield rows


def small_divided_power_model(
) -> tuple[int, int, list[list[int | None]]]:
    variables = 2
    colors = 2
    degree_two = exponent_tuples(2, variables)
    degree_three = exponent_tuples(3, variables)
    degree_two_index = {
        exponent: index for index, exponent in enumerate(degree_two)
    }
    quadratic_dimension = colors * len(degree_two)
    cubic_dimension = colors * len(degree_three)
    contractions: list[list[int | None]] = []
    for variable in range(variables):
        columns: list[int | None] = []
        for color in range(colors):
            for exponent in degree_three:
                if exponent[variable] == 0:
                    columns.append(None)
                    continue
                image = list(exponent)
                image[variable] -= 1
                columns.append(
                    color * len(degree_two)
                    + degree_two_index[tuple(image)]
                )
        contractions.append(columns)
    return quadratic_dimension, cubic_dimension, contractions


def prolongation_dimension_f2(
    subspace: list[int],
    quadratic_dimension: int,
    cubic_dimension: int,
    contractions: list[list[int | None]],
) -> int:
    annihilator = annihilator_basis(subspace, quadratic_dimension)
    constraints: list[int] = []
    for contraction in contractions:
        for functional in annihilator:
            row = 0
            for column, quadratic_index in enumerate(contraction):
                if (
                    quadratic_index is not None
                    and ((functional >> quadratic_index) & 1)
                ):
                    row |= 1 << column
            if row:
                constraints.append(row)
    rank = len(rref_bits(constraints, cubic_dimension)[1])
    return cubic_dimension - rank


def exhaustive_small_field_certificate() -> dict[str, object]:
    (
        quadratic_dimension,
        cubic_dimension,
        contractions,
    ) = small_divided_power_model()
    maxima: dict[str, int] = {}
    counts: dict[str, int] = {}
    total_count = 0
    for dimension in range(quadratic_dimension + 1):
        maximum = -1
        count = 0
        for subspace in rref_subspaces(quadratic_dimension, dimension):
            count += 1
            total_count += 1
            observed = prolongation_dimension_f2(
                subspace,
                quadratic_dimension,
                cubic_dimension,
                contractions,
            )
            if observed > macaulay_successor_degree_two(dimension):
                raise AssertionError(
                    (
                        dimension,
                        observed,
                        macaulay_successor_degree_two(dimension),
                    )
                )
            maximum = max(maximum, observed)
        counts[str(dimension)] = count
        maxima[str(dimension)] = maximum
    if total_count != 2_825:
        raise AssertionError(total_count)
    return {
        "field": "F_2 divided-power contraction",
        "variables": 2,
        "colors": 2,
        "quadratic_ambient_dimension": quadratic_dimension,
        "cubic_ambient_dimension": cubic_dimension,
        "subspace_count": total_count,
        "subspace_count_by_dimension": counts,
        "maximum_prolongation_by_dimension": maxima,
        "counterexample_found": False,
        "logical_role": "diagnostic only",
    }


def build_payload() -> dict[str, object]:
    return {
        "status": "VECTOR_VALUED_MACAULAY_FINITE_INTERFACES_REPLAYED",
        "explicit_weight_certificate": explicit_weight_certificate(),
        "six_color_partition_certificate": partition_certificate(),
        "small_field_exhaustive_diagnostic": (
            exhaustive_small_field_certificate()
        ),
        "claim_boundary": (
            "The script does not prove upper semicontinuity or scalar "
            "Macaulay growth and does not transfer finite-field equality "
            "to characteristic zero. Those steps are the mathematical proof "
            "in the companion note."
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
    print("VECTOR_VALUED_MACAULAY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
