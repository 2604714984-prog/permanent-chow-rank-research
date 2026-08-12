#!/usr/bin/env python3
"""Pure same-row/column alpha-three coupling exclusion (N6-053)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALPHA3_SCRIPT = ROOT / "scripts" / "n6_alpha3_individual_prolongation_barrier.py"
QUOTIENT_SCRIPT = ROOT / "scripts" / "n6_b64_frame_component_specialization.py"
N6052_DATA = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"
PRIME = 1_000_003
N = 6
VARIABLES = 36


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sparse_rank_mod(columns: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    rank = 0
    for column in columns:
        vector = {
            index: value % PRIME
            for index, value in column.items()
            if value % PRIME
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, PRIME - 2, PRIME)
                pivots[pivot] = {
                    index: value * inverse % PRIME
                    for index, value in vector.items()
                }
                rank += 1
                break
            for index, value in pivots[pivot].items():
                updated = (
                    vector.get(index, 0) - coefficient * value
                ) % PRIME
                if updated:
                    vector[index] = updated
                else:
                    vector.pop(index, None)
    return rank


def quotient_differential_rank(quotient, support) -> int:
    """Rank of the frame-to-quotient Grassmann differential at a support."""

    edges = tuple(row * N + column for row, column in support)
    quotient_axes = []
    generators = []
    for first, second in combinations(range(N), 2):
        axis, _ = quotient.quotient_axis(edges[first], edges[second])
        quotient_axes.append(quotient.AXIS_INDEX[axis])
        generators.append((first, second))
    require(len(set(quotient_axes)) == 15, (support, quotient_axes))
    quotient_set = set(quotient_axes)

    row_index: dict[tuple[int, int], int] = {}
    columns: list[dict[int, int]] = []
    for factor_index in range(N):
        for variable in range(VARIABLES):
            if variable == edges[factor_index]:
                continue
            column: dict[int, int] = {}
            for generator_index, (first, second) in enumerate(generators):
                if factor_index == first:
                    other = edges[second]
                elif factor_index == second:
                    other = edges[first]
                else:
                    continue
                axis, sign = quotient.quotient_axis(variable, other)
                axis_index = quotient.AXIS_INDEX[axis]
                if axis_index in quotient_set:
                    continue
                row = row_index.setdefault(
                    (generator_index, axis_index),
                    len(row_index),
                )
                column[row] = (column.get(row, 0) + sign) % PRIME
            columns.append(column)
    require(len(columns) == 210, len(columns))
    return sparse_rank_mod(columns)


def exact_rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            coefficient = work[row][column]
            work[row] = [
                value - coefficient * pivot_value
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def sign_example() -> dict[str, object]:
    rows = (
        (1, -1, -1, -1),
        (1, -1, -1, 1),
        (1, -1, 1, -1),
        (1, -1, 1, 1),
        (1, 1, -1, -1),
        (1, 1, -1, 1),
    )
    sign_rank = exact_rank([list(row) for row in rows])
    square_rows = [
        [
            row[first] * row[second]
            for first in range(4)
            for second in range(first, 4)
        ]
        for row in rows
    ]
    cube_rows = [
        [
            row[first] * row[second] * row[third]
            for first in range(4)
            for second in range(first, 4)
            for third in range(second, 4)
        ]
        for row in rows
    ]
    square_rank = exact_rank(square_rows)
    cube_rank = exact_rank(cube_rows)
    require((sign_rank, square_rank, cube_rank) == (4, 6, 6), (
        sign_rank, square_rank, cube_rank
    ))
    return {
        "normalized_sign_rows": [list(row) for row in rows],
        "exact_QQ_sign_matrix_rank": sign_rank,
        "exact_QQ_rank_one_square_span_rank": square_rank,
        "exact_QQ_rank_one_cube_span_rank": cube_rank,
        "per_column_triple_intersection_dimension": 6 - sign_rank,
        "total_twenty_column_triple_intersection_dimension": (
            20 * (6 - sign_rank)
        ),
    }


def build_payload() -> dict[str, object]:
    alpha3 = load_module(ALPHA3_SCRIPT, "n6053_alpha3")
    quotient = load_module(QUOTIENT_SCRIPT, "n6053_quotient")
    rectangle_free_orbits = alpha3.coordinate_support_orbits()[0]
    ranks = []
    exceptional = []
    for orbit_index, row_masks in enumerate(rectangle_free_orbits):
        support = alpha3.support_from_masks(row_masks)
        rank = quotient_differential_rank(quotient, support)
        ranks.append(rank)
        if rank < 210:
            exceptional.append(
                {
                    "orbit_index": orbit_index,
                    "row_masks": list(row_masks),
                    "support": [list(edge) for edge in support],
                    "modular_differential_rank": rank,
                    "explicit_kernel_dimension": 210 - rank,
                }
            )
    rank_histogram = Counter(ranks)
    require(rank_histogram == {205: 2, 210: 74}, rank_histogram)
    require(
        [row["row_masks"] for row in exceptional]
        == [[0, 0, 0, 0, 0, 63], [1, 1, 1, 1, 1, 1]],
        exceptional,
    )

    n6052 = json.loads(N6052_DATA.read_text(encoding="utf-8"))
    require(
        n6052["state_pruning"]["remaining_state_ids"]
        == ["b60_state_366"]
        and n6052["state_pruning"]["remaining_profile"] == [[0, 3]] * 6,
        n6052["state_pruning"],
    )
    example = sign_example()
    require(
        example["total_twenty_column_triple_intersection_dimension"] == 40,
        example,
    )

    return {
        "status": "N6_053_ALPHA3_ROW_COLUMN_COUPLING_EXCLUSION",
        "arithmetic": (
            "pure sign-fiber proof; exact QQ example and exact modular "
            "coordinate-quotient differential diagnostic"
        ),
        "surviving_state_id": "b60_state_366",
        "surviving_state_profile": [[0, 3]] * 6,
        "pure_coupling_theorem": {
            "common_quotient_classification": (
                "q(F_u)=q(F_v) iff the coordinate-square vectors "
                "(u_r^2) and (v_r^2) are projectively proportional; after "
                "scaling, v is a coordinatewise sign transform of u"
            ),
            "literal_directness_consequence": (
                "the six rank-one squares u_i^2 are independent, hence their "
                "normalized sign rows are six distinct classes modulo global sign"
            ),
            "hypercube_affine_bound": (
                "a normalized sign matrix of rank r has at most 2^(r-1) "
                "distinct rows, so six distinct rows force r>=4"
            ),
            "intersection_formula": (
                "for each column triple, dim(E3_block intersection H3_block) "
                "=6-rank(normalized sign matrix)"
            ),
            "total_intersection_upper_bound": 40,
            "required_intersection_b": 60,
            "strict_gap": 20,
        },
        "exact_QQ_sign_example": example,
        "coordinate_quotient_differential_diagnostic": {
            "rectangle_free_support_orbit_count": len(rectangle_free_orbits),
            "domain_dimension": 210,
            "rank_histogram": {
                str(key): rank_histogram[key] for key in sorted(rank_histogram)
            },
            "exceptional_orbits": exceptional,
            "exceptional_rank_upper_reason": (
                "same-row and same-column families have an explicit "
                "five-dimensional first-order kernel; together with modular "
                "rank 205 this proves exact rank 205 in characteristic zero"
            ),
        },
        "strict_conclusion": (
            "The all-alpha-three b=60 state cannot lie in the common-quotient "
            "same-row family or its transposed same-column family: literal "
            "directness forces b<=40, contradicting b=60."
        ),
        "claim_boundary": (
            "This excludes the two row/column-separated common-quotient "
            "families, not every all-alpha-three configuration or every "
            "degeneration through their coordinate endpoints. It does not yet "
            "exclude b=60, prove ChowRank(perm_6)>=27, or make a border-rank claim."
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
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print(
        "quotient_differential_rank_histogram="
        f"{payload['coordinate_quotient_differential_diagnostic']['rank_histogram']}"
    )
    print(
        "same_row_column_coupled_b_upper="
        f"{payload['pure_coupling_theorem']['total_intersection_upper_bound']}"
    )
    print("N6_ALPHA3_ROW_COLUMN_COUPLING_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
