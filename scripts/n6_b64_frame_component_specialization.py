#!/usr/bin/env python3
"""Exact component and noncoordinate tangent audit for the b=64 W12 map.

The finite part has two independent pieces.

* Hall's theorem classifies which ordered choices of the five irreducible
  components of the extremal frame base locus can contain a projective frame.
* A small exact modular calculation checks the fixed-W tangent space at one
  explicitly noncoordinate frame.  A nonzero minor modulo a prime is used
  only as a characteristic-zero lower-rank certificate.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path


N = 6
PRIME = 1_000_003
VARIABLE_COUNT = N * N
FACTOR_COUNT = 6
PARAMETER_COUNT = FACTOR_COUNT * VARIABLE_COUNT

COMPONENTS = ("P_A", "P_B", "Q_01", "Q_02", "Q_12")
ALLOWED_AXES = {
    "P_A": frozenset((0, 1, 2)),
    "P_B": frozenset((3, 4, 5)),
    "Q_01": frozenset((0, 1, 3, 4)),
    "Q_02": frozenset((0, 2, 3, 5)),
    "Q_12": frozenset((1, 2, 4, 5)),
}


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def perfect_matching_count(assignment: tuple[str, ...]) -> int:
    """Count perfect matchings by the exact 2^6 subset dynamic program."""

    counts = [0] * (1 << FACTOR_COUNT)
    counts[0] = 1
    for component in assignment:
        following = [0] * (1 << FACTOR_COUNT)
        for used, value in enumerate(counts):
            if not value:
                continue
            for axis in ALLOWED_AXES[component]:
                bit = 1 << axis
                if not used & bit:
                    following[used | bit] += value
        counts = following
    return counts[-1]


def hall_witness(assignment: tuple[str, ...]) -> dict[str, object] | None:
    """Return a strict Hall-deficient subset, if one exists."""

    for size in range(1, FACTOR_COUNT + 1):
        for indices in combinations(range(FACTOR_COUNT), size):
            neighbors: set[int] = set()
            for index in indices:
                neighbors.update(ALLOWED_AXES[assignment[index]])
            if len(neighbors) < size:
                return {
                    "positions": list(indices),
                    "component_multiset": sorted(assignment[index] for index in indices),
                    "neighbor_axes": sorted(neighbors),
                    "subset_size": size,
                    "neighbor_size": len(neighbors),
                }
    return None


def count_vectors(total: int, length: int, prefix: tuple[int, ...] = ()):
    if length == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from count_vectors(total - value, length - 1, prefix + (value,))


def canonical_assignment(counts: tuple[int, ...]) -> tuple[str, ...]:
    return tuple(
        component
        for component, count in zip(COMPONENTS, counts)
        for _ in range(count)
    )


def component_audit() -> dict[str, object]:
    histogram: Counter[int] = Counter()
    admissible_ordered = 0
    inadmissible_ordered = 0
    for assignment in product(COMPONENTS, repeat=FACTOR_COUNT):
        matchings = perfect_matching_count(assignment)
        histogram[matchings] += 1
        if matchings:
            admissible_ordered += 1
        else:
            inadmissible_ordered += 1

    vector_rows: list[dict[str, object]] = []
    for counts in count_vectors(FACTOR_COUNT, len(COMPONENTS)):
        assignment = canonical_assignment(counts)
        matchings = perfect_matching_count(assignment)
        witness = hall_witness(assignment)
        require((matchings == 0) == (witness is not None), (assignment, witness))
        vector_rows.append(
            {
                "component_counts": {
                    component: count for component, count in zip(COMPONENTS, counts)
                },
                "perfect_matching_count": matchings,
                "admissible": bool(matchings),
                "hall_deficiency_witness": witness,
            }
        )

    admissible_vectors = sum(row["admissible"] for row in vector_rows)
    require(admissible_ordered == 14_810, admissible_ordered)
    require(inadmissible_ordered == 815, inadmissible_ordered)
    require(admissible_vectors == 153, admissible_vectors)
    require(len(vector_rows) - admissible_vectors == 57, len(vector_rows))
    require(
        histogram
        == {
            0: 815,
            12: 1320,
            18: 720,
            24: 1890,
            32: 4590,
            36: 1460,
            44: 540,
            48: 2700,
            56: 1080,
            72: 420,
            80: 90,
        },
        histogram,
    )
    return {
        "ordered_component_assignments": len(COMPONENTS) ** FACTOR_COUNT,
        "admissible_ordered_assignments": admissible_ordered,
        "inadmissible_ordered_assignments": inadmissible_ordered,
        "perfect_matching_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "unordered_component_count_vectors": len(vector_rows),
        "admissible_component_count_vectors": admissible_vectors,
        "inadmissible_component_count_vectors": len(vector_rows) - admissible_vectors,
        "component_count_vector_table": vector_rows,
    }


def cell(index: int) -> tuple[int, int]:
    return divmod(index, N)


def quotient_axis(left: int, right: int) -> tuple[tuple[object, ...], int]:
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


QUOTIENT_AXES = tuple(
    sorted(
        {
            quotient_axis(left, right)[0]
            for left in range(VARIABLE_COUNT)
            for right in range(left, VARIABLE_COUNT)
        },
        key=repr,
    )
)
AXIS_INDEX = {axis: index for index, axis in enumerate(QUOTIENT_AXES)}


def quotient_product(
    left: dict[int, int], right: dict[int, int], prime: int
) -> dict[int, int]:
    answer: dict[int, int] = {}
    for left_index, left_value in left.items():
        for right_index, right_value in right.items():
            axis, sign = quotient_axis(left_index, right_index)
            index = AXIS_INDEX[axis]
            answer[index] = (
                answer.get(index, 0) + sign * left_value * right_value
            ) % prime
            if answer[index] == 0:
                del answer[index]
    return answer


def dense(vector: dict[int, int], width: int) -> list[int]:
    row = [0] * width
    for index, value in vector.items():
        row[index] = value
    return row


def rref_mod(
    matrix: list[list[int]], prime: int
) -> tuple[list[list[int]], list[int]]:
    work = [[value % prime for value in row] for row in matrix]
    pivot_columns: list[int] = []
    rank = 0
    width = len(work[0]) if work else 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            multiplier = work[row][column]
            work[row] = [
                (value - multiplier * pivot_value) % prime
                for value, pivot_value in zip(work[row], work[rank])
            ]
        pivot_columns.append(column)
        rank += 1
        if rank == len(work):
            break
    return work[:rank], pivot_columns


def reduce_mod_rowspace(
    vector: dict[int, int], rref: list[list[int]], pivots: list[int], prime: int
) -> dict[int, int]:
    answer = dict(vector)
    for row, pivot in zip(rref, pivots):
        multiplier = answer.get(pivot, 0)
        if not multiplier:
            continue
        for index, value in enumerate(row):
            if value:
                answer[index] = (answer.get(index, 0) - multiplier * value) % prime
                if answer[index] == 0:
                    answer.pop(index, None)
    return answer


def modular_rank_with_minor(
    matrix: list[list[int]], prime: int
) -> tuple[int, list[int], list[int]]:
    work = [[value % prime for value in row] for row in matrix]
    original_rows = list(range(len(work)))
    pivot_rows: list[int] = []
    pivot_columns: list[int] = []
    rank = 0
    width = len(work[0]) if work else 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        original_rows[rank], original_rows[pivot] = (
            original_rows[pivot],
            original_rows[rank],
        )
        inverse = pow(work[rank][column], prime - 2, prime)
        for index in range(column, width):
            work[rank][index] = work[rank][index] * inverse % prime
        for row in range(rank + 1, len(work)):
            multiplier = work[row][column]
            if not multiplier:
                continue
            for index in range(column, width):
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
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant % prime
        value = work[column][column]
        determinant = determinant * value % prime
        inverse = pow(value, prime - 2, prime)
        for row in range(column + 1, size):
            multiplier = work[row][column] * inverse % prime
            if not multiplier:
                continue
            for index in range(column, size):
                work[row][index] = (
                    work[row][index] - multiplier * work[column][index]
                ) % prime
    return determinant


def noncoordinate_factors() -> tuple[list[dict[int, int]], list[list[int]]]:
    """Return an integral frame dual to three P_A and three P_B points."""

    edges = (0, 1, 2, 6, 7, 8)
    local_factors = (
        (1, 0, -1),
        (0, 1, -1),
        (0, 0, 1),
        (1, 0, -1),
        (0, 1, 1),
        (0, 0, 1),
    )
    factors: list[dict[int, int]] = []
    for factor_index, coefficients in enumerate(local_factors):
        offset = 0 if factor_index < 3 else 3
        factors.append(
            {
                edges[offset + index]: value
                for index, value in enumerate(coefficients)
                if value
            }
        )
    dual_points = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, -1, 1],
    ]
    return factors, dual_points


def noncoordinate_tangent_audit() -> dict[str, object]:
    require(len(QUOTIENT_AXES) == 441, len(QUOTIENT_AXES))
    factors, dual_points = noncoordinate_factors()
    local_edges = (0, 1, 2, 6, 7, 8)
    local_factor_matrix = [
        [factor.get(edge, 0) for factor in factors] for edge in local_edges
    ]
    duality_matrix = [
        [
            sum(point[index] * local_factor_matrix[index][column] for index in range(6))
            for column in range(6)
        ]
        for point in dual_points
    ]
    require(
        duality_matrix
        == [[int(row == column) for column in range(6)] for row in range(6)],
        duality_matrix,
    )
    for point in dual_points:
        a = point[:3]
        b = point[3:]
        require(
            all(a[i] * b[j] + a[j] * b[i] == 0 for i, j in combinations(range(3), 2)),
            point,
        )
    pair_labels = list(combinations(range(FACTOR_COUNT), 2))
    w_rows = [
        dense(quotient_product(factors[i], factors[j], PRIME), len(QUOTIENT_AXES))
        for i, j in pair_labels
    ]
    w_rref, w_pivots = rref_mod(w_rows, PRIME)
    require(len(w_pivots) == 12, w_pivots)
    w_support = sorted(
        {
            index
            for row in w_rref
            for index, value in enumerate(row)
            if value
        }
    )
    square_axes = [
        QUOTIENT_AXES[index]
        for index in w_support
        if QUOTIENT_AXES[index][0] == "square"
    ]
    require(len(w_support) == 14, w_support)
    require(len(square_axes) == 2, square_axes)

    free_axes = [index for index in range(len(QUOTIENT_AXES)) if index not in w_pivots]
    free_set = set(free_axes)
    sparse_rows: dict[tuple[int, int, int], dict[int, int]] = {}
    for first, second in pair_labels:
        for moving, fixed in ((first, factors[second]), (second, factors[first])):
            for variable in range(VARIABLE_COUNT):
                residual = reduce_mod_rowspace(
                    quotient_product({variable: 1}, fixed, PRIME),
                    w_rref,
                    w_pivots,
                    PRIME,
                )
                column = moving * VARIABLE_COUNT + variable
                for axis_index, value in residual.items():
                    if axis_index not in free_set:
                        require(value == 0, (axis_index, value))
                        continue
                    key = (first, second, axis_index)
                    sparse_rows.setdefault(key, {})[column] = value

    row_keys = sorted(sparse_rows, key=repr)
    matrix = [dense(sparse_rows[key], PARAMETER_COUNT) for key in row_keys]
    rank, pivot_rows, pivot_columns = modular_rank_with_minor(matrix, PRIME)
    require(rank == 210, rank)
    selected = [
        [matrix[row][column] for column in pivot_columns] for row in pivot_rows
    ]
    determinant = determinant_mod(selected, PRIME)
    require(determinant != 0, determinant)

    scaling_vectors: list[list[int]] = []
    for factor_index, factor in enumerate(factors):
        vector = [0] * PARAMETER_COUNT
        for variable, value in factor.items():
            vector[factor_index * VARIABLE_COUNT + variable] = value % PRIME
        scaling_vectors.append(vector)
    for vector in scaling_vectors:
        for row in matrix:
            require(sum(a * b for a, b in zip(row, vector)) % PRIME == 0, vector)

    return {
        "prime": PRIME,
        "dual_base_locus_points": dual_points,
        "dual_frame_pairing_matrix": duality_matrix,
        "ambient_factors": [
            [[cell(index)[0], cell(index)[1], value] for index, value in factor.items()]
            for factor in factors
        ],
        "quotient_rank_mod_prime": len(w_pivots),
        "quotient_rref_pivot_columns": w_pivots,
        "quotient_rref_support_size": len(w_support),
        "quotient_square_axes_in_support": [list(axis) for axis in square_axes],
        "noncoordinate_reason": (
            "The RREF uses fourteen quotient axes and includes two square axes; "
            "a coordinate K_(2,3) or K_(3,2) quotient is a twelve-axis subspace "
            "with no square axis."
        ),
        "fixed_W_tangent_matrix_shape": [len(matrix), PARAMETER_COUNT],
        "fixed_W_tangent_rank_mod_prime": rank,
        "fixed_W_tangent_kernel_dimension": PARAMETER_COUNT - rank,
        "explicit_scaling_kernel_dimension": len(scaling_vectors),
        "selected_minor_size": rank,
        "selected_minor_rows": pivot_rows,
        "selected_minor_columns": pivot_columns,
        "selected_minor_determinant_mod_prime": determinant,
    }


def build_payload() -> dict[str, object]:
    return {
        "status": "EXACT_B64_FRAME_COMPONENT_SPECIALIZATION",
        "arithmetic": "exact integer combinatorics and strict modular nonzero minor",
        "component_classification": component_audit(),
        "noncoordinate_tangent_certificate": noncoordinate_tangent_audit(),
        "pure_conclusions": [
            "For a fixed extremal six-plane L, equality of quotient W12 determines the actual fifteen-dimensional Chow quadratic space and its unordered projective factor frame.",
            "An ordered choice of the five base-locus components contains a projective frame if and only if its six allowed-axis sets have a perfect matching.",
            "Every admissible frame-component branch contains an honest coordinate frame; consequently the quotient map is generically quasi-finite on every such geometric branch by the coordinate fixed-W tangent certificate.",
        ],
        "claim_boundary": (
            "The Hall classification concerns individual extremal frame branches.  "
            "It does not preserve a common W or directness for six frames under a "
            "simultaneous degeneration.  The noncoordinate tangent calculation is "
            "one exact point certificate, not a global radicial theorem or a fiber-size "
            "bound.  This result does not exclude b=64 and does not prove "
            "ChowRank(perm_6)>=27."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_B64_FRAME_COMPONENT_SPECIALIZATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
