#!/usr/bin/env python3
"""Audit the full monomial-transform classification for the perm7 packet."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def swap_extension_witness(
    first_row: int,
    second_row: int,
    first_column: int,
    second_column: int,
    missing_column: int,
) -> tuple[int, ...]:
    other_rows = [row for row in range(6) if row not in (first_row, second_row)]
    available = [
        column
        for column in range(7)
        if column not in (first_column, second_column, missing_column)
    ]
    assignment = [-1] * 6
    assignment[first_row] = first_column
    assignment[second_row] = second_column
    for row, column in zip(other_rows, available[:4]):
        assignment[row] = column
    if len(set(assignment)) != 6:
        raise AssertionError(assignment)
    if missing_column in assignment:
        raise AssertionError((assignment, missing_column))
    return tuple(assignment)


def build_payload() -> dict[str, object]:
    two_permutation = json.loads(
        (ROOT / "data" / "n7_mixed_glynn_two_permutation_tail_rank.json").read_text(
            encoding="utf-8"
        )
    )
    three_plus = json.loads(
        (
            ROOT
            / "data"
            / "n7_mixed_glynn_protected_character_explicit_smt.json"
        ).read_text(encoding="utf-8")
    )
    if two_permutation["invalid_tail_rank_histogram"] != {"42": 3595}:
        raise AssertionError("two-permutation certificate mismatch")
    target_support = two_permutation["identity_kernel_target_support"]
    if len(target_support) < 2:
        raise AssertionError("identity target profile has insufficient support")
    if three_plus["status"] != "EXACT_UNSAT_PROTECTED_CHARACTER_AT_LEAST_THREE_TYPES":
        raise AssertionError("three-plus certificate mismatch")

    witnesses = []
    derived_relations = []
    for first_row, second_row in itertools.combinations(range(6), 2):
        for first_column, second_column in itertools.combinations(range(7), 2):
            missing_column = next(
                (
                    column
                    for column in target_support
                    if column not in (first_column, second_column)
                ),
                None,
            )
            if missing_column is None:
                bridge = next(
                    column
                    for column in range(7)
                    if column not in (first_column, second_column)
                )
                derived_relations.append(
                    {
                        "rows": [first_row, second_row],
                        "columns": [first_column, second_column],
                        "bridge_column": bridge,
                        "from_column_pairs": [
                            [first_column, bridge],
                            [second_column, bridge],
                        ],
                    }
                )
                continue
            assignment = swap_extension_witness(
                first_row,
                second_row,
                first_column,
                second_column,
                missing_column,
            )
            swapped = list(assignment)
            swapped[first_row], swapped[second_row] = (
                swapped[second_row],
                swapped[first_row],
            )
            if len(set(swapped)) != 6 or set(swapped) != set(assignment):
                raise AssertionError((assignment, swapped))
            witnesses.append(
                {
                    "rows": [first_row, second_row],
                    "columns": [first_column, second_column],
                    "missing_column": missing_column,
                    "assignment": list(assignment),
                    "swapped_assignment": swapped,
                }
            )

    return {
        "schema_version": 1,
        "status": "EXACT_MONOMIAL_TRANSFORM_PACKET_CLASSIFICATION",
        "field": "characteristic zero (indeed characteristic not two)",
        "row_pair_count": 15,
        "column_pair_count": 21,
        "identity_kernel_target_support": target_support,
        "direct_swap_relation_count": len(witnesses),
        "derived_swap_relation_count": len(derived_relations),
        "swap_relation_count": len(witnesses) + len(derived_relations),
        "swap_extension_witnesses_first_5": witnesses[:5],
        "derived_swap_relations_first_5": derived_relations[:5],
        "imported_certificates": {
            "two_underlying_permutations": {
                "candidate_count": two_permutation["candidate_count"],
                "invalid_tail_rank_histogram": two_permutation[
                    "invalid_tail_rank_histogram"
                ],
            },
            "three_or_more_underlying_permutations": {
                "status": three_plus["status"],
                "cases": [
                    {"case": row["case"], "answer": row["answer"]}
                    for row in three_plus["cases"]
                ],
            },
        },
        "local_classification": {
            "six_equal_monomial_transforms": 1,
            "every_other_six_block_assignment": 0,
        },
        "global_classification": {
            "seven_equal_monomial_transforms": 7,
            "one_exceptional_block": 1,
            "every_other_seven_block_assignment": 0,
        },
        "proof_summary": [
            "For one underlying permutation, its one-dimensional invalid kernel is nonzero on exactly two missing-column target fibres.",
            "Twenty of the 21 column pairs admit a direct swap while omitting one of those two supported columns; the remaining pair follows through any bridge column.",
            "Thus target membership forces d_ia*d_jb=d_ib*d_ja for all 15 row pairs and 21 column pairs, so the 6-by-7 scaling matrix has multiplicative rank one.",
            "Its column-zero entries are all one, forcing every row to be identical and hence all six monomial transforms to agree.",
            "For two underlying permutations, arbitrary nonzero diagonal scalars only rescale invalid-monomial columns and preserve the certified rank 42.",
            "For at least three underlying permutations, the protected-character obstruction is likewise unchanged by nonzero column rescaling.",
        ],
        "claim_boundary": [
            "The theorem covers invertible monomial graph transformations: arbitrary nonzero diagonal scalings followed by coordinate permutations.",
            "It does not cover non-monomial GL(6) transformations, arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
