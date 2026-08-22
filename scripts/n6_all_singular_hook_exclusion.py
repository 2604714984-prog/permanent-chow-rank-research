#!/usr/bin/env python3
"""Small exact regressions for the pure N6-072 hook exclusion."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


N = 6
EDGES = list(combinations(range(N), 2))


def exact_rank(matrix) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next(
            (row for row in range(answer, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        value = work[answer][column]
        work[answer] = [entry / value for entry in work[answer]]
        for row in range(answer + 1, len(work)):
            scale = work[row][column]
            if scale:
                work[row] = [
                    entry - scale * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[answer], strict=True)
                ]
        answer += 1
    return answer


def s0_action_rank(vector):
    columns = []
    for left, right in EDGES:
        column = [0] * N
        column[left] = vector[right]
        column[right] = vector[left]
        columns.append(column)
    return exact_rank(list(map(list, zip(*columns, strict=True))))


def wedge_map(vector):
    columns = []
    for basis in range(N):
        column = []
        for left, right in EDGES:
            column.append(
                vector[left] * int(basis == right)
                - vector[right] * int(basis == left)
            )
        columns.append(column)
    return list(map(list, zip(*columns, strict=True)))


def horizontal_join(matrices):
    return [
        [entry for matrix in matrices for entry in matrix[row]]
        for row in range(len(matrices[0]))
    ]


def build_payload() -> dict[str, object]:
    support_rows = []
    for support in range(1, N + 1):
        vector = [1] * support + [0] * (N - support)
        action_rank = s0_action_rank(vector)
        if action_rank < 5:
            raise AssertionError((support, action_rank))
        support_rows.append(
            {"support_size": support, "exact_rank_of_S0_times_y": action_rank}
        )

    coordinate_vectors = [
        [int(index == coordinate) for index in range(N)]
        for coordinate in range(3)
    ]
    wedge_matrices = [wedge_map(vector) for vector in coordinate_vectors]
    pair_intersection = (
        exact_rank(wedge_matrices[0])
        + exact_rank(wedge_matrices[1])
        - exact_rank(horizontal_join(wedge_matrices[:2]))
    )
    edge_01 = [[int(edge == (0, 1))] for edge in EDGES]
    triple_intersection = (
        pair_intersection
        if exact_rank(horizontal_join([wedge_matrices[2], edge_01]))
        == exact_rank(wedge_matrices[2])
        else 0
    )
    if (pair_intersection, triple_intersection) != (1, 0):
        raise AssertionError((pair_intersection, triple_intersection))

    hook_cases = []
    for full_rows in range(3, 7):
        label_classes = full_rows
        survives_q_le_four = label_classes <= 4
        conclusion = (
            "excluded_by_q_le_4"
            if not survives_q_le_four
            else "requires_m4_column_argument"
            if full_rows == 4
            else "requires_m3_parallel_argument"
        )
        hook_cases.append(
            {
                "full_row_count_m": full_rows,
                "label_class_count_q": label_classes,
                "q_at_most_4": survives_q_le_four,
                "proof_branch": conclusion,
            }
        )

    return {
        "status": [
            "PURE_ALL_SINGULAR_FLAG_HOOK_EXCLUSION",
            "EXACT_QQ_ELEMENTARY_REGRESSION",
            "N6-072",
        ],
        "s0_action_rank_profile": support_rows,
        "wedge_space_intersections": {
            "pair_intersection_dimension": pair_intersection,
            "triple_intersection_dimension": triple_intersection,
        },
        "finite_hook_case_routing": hook_cases,
        "strict_conclusion": (
            "Under the previously proved unique b=50 common-W15 endpoint, "
            "the flag-hook second shadow and the N6-069 all-singular block "
            "condition are incompatible. Hence ordinary "
            "ChowRank(perm_6)>=28. Together with the 32-term Glynn "
            "decomposition, 28<=ChowRank(perm_6)<=32."
        ),
        "claim_boundary": (
            "The exclusion uses the ordinary-rank b=50 reduction, the N6-064 "
            "flag-hook theorem, and the N6-069 all-singular reduction. It does "
            "not prove exact rank 32, does not give a border-rank lower bound, "
            "and does not prove the general conjecture ChowRank(perm_n)=2^(n-1)."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(rendered, end="")


if __name__ == "__main__":
    main()
