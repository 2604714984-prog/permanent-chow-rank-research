#!/usr/bin/env python3
"""Exact coordinate and infinitesimal audit for the N6-038 ``b=64`` fiber.

The mathematical proof that an actual Chow quadratic space over a coordinate
extremal quotient is unique is in the companion note.  This replay supplies
two finite checks:

* the 600 coordinate K_(2,3)/K_(3,2) planes have distinct quotient
  signatures; and
* at a coordinate K_(2,3) frame, the fixed-quotient linearization has exact
  characteristic-zero rank 210.  A 210-square minor is nonzero modulo the
  prime 1,000,003, while the six factor-scaling directions give the matching
  upper bound.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


N = 6
PRIME = 1_000_003
VARIABLES = N * N
FACTOR_COUNT = 6
PARAMETER_COUNT = FACTOR_COUNT * VARIABLES


def cell(index: int) -> tuple[int, int]:
    return divmod(index, N)


def quotient_axis(left: int, right: int) -> tuple[tuple[object, ...], int]:
    """Return the quotient basis axis and sign of ``x_left*x_right``.

    The quotient is Sym^2(V)/E_2.  On a rectangle, the two diagonal
    monomials are negatives of one another; all other monomials give their
    own quotient axes.
    """

    row_left, column_left = cell(left)
    row_right, column_right = cell(right)
    if left == right:
        return ("square", left), 1
    if row_left == row_right:
        c0, c1 = sorted((column_left, column_right))
        return ("row", row_left, c0, c1), 1
    if column_left == column_right:
        r0, r1 = sorted((row_left, row_right))
        return ("column", column_left, r0, r1), 1

    r0, r1 = sorted((row_left, row_right))
    c0, c1 = sorted((column_left, column_right))
    parallel = {(r0, c0), (r1, c1)}
    sign = 1 if (row_left, column_left) in parallel else -1
    return ("rectangle", r0, r1, c0, c1), sign


def quotient_axis_count() -> int:
    axes = {
        quotient_axis(left, right)[0]
        for left in range(VARIABLES)
        for right in range(left, VARIABLES)
    }
    return len(axes)


def coordinate_edges(
    first: tuple[int, ...], second: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(row * N + column for row in first for column in second)


def quotient_signature(edges: tuple[int, ...]) -> tuple[tuple[object, ...], ...]:
    axes = {
        quotient_axis(left, right)[0]
        for left, right in combinations(edges, 2)
    }
    if len(axes) != 12:
        raise AssertionError((edges, len(axes)))
    return tuple(sorted(axes, key=repr))


def all_coordinate_signatures() -> tuple[
    dict[tuple[tuple[object, ...], ...], list[dict[str, object]]],
    Counter[str],
]:
    fibers: dict[
        tuple[tuple[object, ...], ...], list[dict[str, object]]
    ] = {}
    orientation_count: Counter[str] = Counter()

    for rows in combinations(range(N), 2):
        for columns in combinations(range(N), 3):
            edges = coordinate_edges(rows, columns)
            signature = quotient_signature(edges)
            fibers.setdefault(signature, []).append(
                {
                    "orientation": "K_2_3",
                    "rows": list(rows),
                    "columns": list(columns),
                }
            )
            orientation_count["K_2_3"] += 1

    for rows in combinations(range(N), 3):
        for columns in combinations(range(N), 2):
            edges = coordinate_edges(rows, columns)
            signature = quotient_signature(edges)
            fibers.setdefault(signature, []).append(
                {
                    "orientation": "K_3_2",
                    "rows": list(rows),
                    "columns": list(columns),
                }
            )
            orientation_count["K_3_2"] += 1

    return fibers, orientation_count


def tangent_matrix() -> tuple[
    list[list[int]], list[tuple[int, int, tuple[object, ...]]], tuple[int, ...]
]:
    """Build the fixed-W linearization at the standard K_(2,3) frame."""

    edges = coordinate_edges((0, 1), (0, 1, 2))
    signature = set(quotient_signature(edges))
    sparse_rows: dict[
        tuple[int, int, tuple[object, ...]], dict[int, int]
    ] = {}

    for first, second in combinations(range(FACTOR_COUNT), 2):
        for moving, fixed_variable in (
            (first, edges[second]),
            (second, edges[first]),
        ):
            for variable in range(VARIABLES):
                axis, sign = quotient_axis(variable, fixed_variable)
                if axis in signature:
                    continue
                key = (first, second, axis)
                column = moving * VARIABLES + variable
                sparse_rows.setdefault(key, {})[column] = sign

    row_keys = sorted(sparse_rows, key=repr)
    matrix: list[list[int]] = []
    for key in row_keys:
        row = [0] * PARAMETER_COUNT
        for column, value in sparse_rows[key].items():
            row[column] = value
        matrix.append(row)
    return matrix, row_keys, edges


def modular_rank_with_minor(
    matrix: list[list[int]], prime: int
) -> tuple[int, list[int], list[int]]:
    work = [[value % prime for value in row] for row in matrix]
    original_rows = list(range(len(work)))
    pivot_rows: list[int] = []
    pivot_columns: list[int] = []
    rank = 0
    column_count = len(work[0]) if work else 0

    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        original_rows[rank], original_rows[pivot] = (
            original_rows[pivot],
            original_rows[rank],
        )
        inverse = pow(work[rank][column], prime - 2, prime)
        for index in range(column, column_count):
            work[rank][index] = work[rank][index] * inverse % prime
        for row in range(rank + 1, len(work)):
            multiplier = work[row][column]
            if not multiplier:
                continue
            for index in range(column, column_count):
                work[row][index] = (
                    work[row][index] - multiplier * work[rank][index]
                ) % prime
        pivot_rows.append(original_rows[rank])
        pivot_columns.append(column)
        rank += 1
        if rank == len(work):
            break
    return rank, pivot_rows, pivot_columns


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant % prime
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, prime - 2, prime)
        for row in range(column + 1, size):
            multiplier = work[row][column] * inverse % prime
            if not multiplier:
                continue
            for index in range(column, size):
                work[row][index] = (
                    work[row][index] - multiplier * work[column][index]
                ) % prime
    return determinant


def audit() -> dict[str, object]:
    if quotient_axis_count() != 441:
        raise AssertionError("incorrect quotient basis dimension")

    fibers, orientation_count = all_coordinate_signatures()
    collision_histogram = Counter(len(fiber) for fiber in fibers.values())
    if orientation_count != {"K_2_3": 300, "K_3_2": 300}:
        raise AssertionError(orientation_count)
    if collision_histogram != {1: 600}:
        raise AssertionError(collision_histogram)

    matrix, row_keys, edges = tangent_matrix()
    if len(matrix) != 897:
        raise AssertionError(len(matrix))
    rank, pivot_rows, pivot_columns = modular_rank_with_minor(matrix, PRIME)
    if rank != 210:
        raise AssertionError(rank)
    selected = [
        [matrix[row][column] for column in pivot_columns]
        for row in pivot_rows
    ]
    minor_determinant = determinant_mod(selected, PRIME)
    if minor_determinant == 0:
        raise AssertionError("selected modular minor vanished")

    scaling_columns = [
        factor * VARIABLES + edges[factor] for factor in range(FACTOR_COUNT)
    ]
    for column in scaling_columns:
        if any(row[column] for row in matrix):
            raise AssertionError(("factor scaling is not in the kernel", column))
    if set(pivot_columns).intersection(scaling_columns):
        raise AssertionError("pivot used a scaling column")

    encoded_row_keys = [
        [row_keys[row][0], row_keys[row][1], list(row_keys[row][2])]
        for row in pivot_rows
    ]
    return {
        "status": "EXACT_N6_B64_COORDINATE_COMMON_QUOTIENT_RIGIDITY",
        "arithmetic": "integer combinatorics plus a strict modular nonzero minor",
        "quotient_dimension": 441,
        "coordinate_extremal_planes": sum(orientation_count.values()),
        "coordinate_orientation_count": dict(sorted(orientation_count.items())),
        "distinct_coordinate_W12_signatures": len(fibers),
        "coordinate_signature_collision_histogram": {
            str(size): count for size, count in sorted(collision_histogram.items())
        },
        "cross_orientation_coordinate_collisions": 0,
        "standard_frame_edges": [list(cell(edge)) for edge in edges],
        "fixed_W_tangent": {
            "integer_matrix_shape": [len(matrix), PARAMETER_COUNT],
            "prime": PRIME,
            "modular_rank": rank,
            "kernel_dimension": PARAMETER_COUNT - rank,
            "explicit_factor_scaling_columns": scaling_columns,
            "selected_minor_size": rank,
            "selected_minor_determinant_mod_prime": minor_determinant,
            "selected_minor_columns": pivot_columns,
            "selected_minor_row_keys": encoded_row_keys,
        },
        "characteristic_zero_bridge": (
            "the nonzero 210-minor modulo 1000003 gives rank at least 210 "
            "over characteristic zero; the six independent factor-scaling "
            "kernel directions give rank at most 216-6=210"
        ),
        "pure_coordinate_fiber_theorem": (
            "If F is an actual 15-dimensional Chow quadratic space and "
            "q(F) equals the W12 of a coordinate K_(2,3) or K_(3,2) plane, "
            "then F is the coordinate squarefree quadratic space itself."
        ),
        "b64_consequence": (
            "The six direct Chow quadratic spaces at b=64 cannot have a "
            "coordinate extremal common quotient W12."
        ),
        "claim_boundary": (
            "This excludes only coordinate common quotients and proves their "
            "reduced local rigidity. It does not exclude noncoordinate b=64 "
            "incidence points and does not prove ChowRank(perm_6)>=27."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    payload = audit()
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    tangent = payload["fixed_W_tangent"]
    print(f"coordinate_extremal_planes={payload['coordinate_extremal_planes']}")
    print(
        "distinct_coordinate_W12_signatures="
        f"{payload['distinct_coordinate_W12_signatures']}"
    )
    print(
        "coordinate_signature_collision_histogram="
        f"{payload['coordinate_signature_collision_histogram']}"
    )
    print(f"fixed_W_tangent_matrix_shape={tangent['integer_matrix_shape']}")
    print(f"fixed_W_tangent_rank_mod_{PRIME}={tangent['modular_rank']}")
    print(
        "selected_210_minor_determinant_mod_prime="
        f"{tangent['selected_minor_determinant_mod_prime']}"
    )
    print("N6_B64_COMMON_QUOTIENT_RIGIDITY_PASS")


if __name__ == "__main__":
    main()
