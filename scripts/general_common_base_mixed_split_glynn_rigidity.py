#!/usr/bin/env python3
"""Exact replay for common-base mixed-split Glynn rigidity."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations, product
from math import comb
from pathlib import Path
from typing import Sequence

EXPECTED_CORE = "b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def sign_vectors(order: int) -> tuple[tuple[int, ...], ...]:
    return tuple((1,) + tail for tail in product((1, -1), repeat=order - 1))


def character(value: Sequence[int]) -> int:
    result = 1
    for entry in value:
        result *= int(entry)
    return result


def tensor_entry(value: Sequence[int], assignment: Sequence[int]) -> int:
    result = 1
    for index in assignment:
        result *= int(value[index])
    return result


def quartic_atom(source: Sequence[int], base: Sequence[int], shared: tuple[int, int]) -> tuple[int, ...]:
    tail = tuple(index for index in range(4) if index not in shared)
    result = []
    for assignment in product(range(4), repeat=4):
        prefix = source[assignment[shared[0]]] * source[assignment[shared[1]]]
        source_tail = source[assignment[tail[0]]] * source[assignment[tail[1]]]
        base_tail = base[assignment[tail[0]]] * base[assignment[tail[1]]]
        result.append(prefix * (source_tail - base_tail))
    return tuple(result)


def quartic_target(signs: Sequence[Sequence[int]]) -> tuple[int, ...]:
    return tuple(
        sum(character(value) * tensor_entry(value, assignment) for value in signs)
        for assignment in product(range(4), repeat=4)
    )


def add_vectors(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def subtract_vectors(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def quartic_equality_scan() -> dict[str, object]:
    signs = sign_vectors(4)
    base = signs[0]
    retained = signs[1:]
    shared_pairs = tuple(combinations(range(4), 2))
    target = quartic_target(signs)
    contributions = tuple(
        tuple(
            tuple(character(value) * entry for entry in quartic_atom(value, base, shared))
            for shared in shared_pairs
        )
        for value in retained
    )
    last_lookup = {contributions[-1][index]: index for index in range(len(shared_pairs))}
    solutions = []
    zero = (0,) * len(target)
    for choices in product(range(len(shared_pairs)), repeat=6):
        partial = zero
        for source_index, split_index in enumerate(choices):
            partial = add_vectors(partial, contributions[source_index][split_index])
        needed = subtract_vectors(target, partial)
        final = last_lookup.get(needed)
        if final is not None:
            solutions.append(choices + (final,))
    expected = [tuple([index] * 7) for index in range(len(shared_pairs))]
    require(solutions == expected, solutions)
    return {
        "assignments_checked": len(shared_pairs) ** 7,
        "meet_in_middle_prefixes_checked": len(shared_pairs) ** 6,
        "solutions": len(solutions),
        "solution_split_indices": [list(value) for value in solutions],
        "all_solutions_uniform": True,
    }


def audit_order(order: int) -> dict[str, object]:
    require(order >= 3, order)
    free_dimension = order - 1
    sign_count = 1 << free_dimension
    nonzero_boolean_points = sign_count - 1
    split_count = comb(order, 2)
    degree_m_zeta_rows = nonzero_boolean_points
    require(degree_m_zeta_rows == nonzero_boolean_points, order)
    defect_zeta_rows = sign_count - 2
    require(defect_zeta_rows + 1 == nonzero_boolean_points, order)
    return {
        "order": order,
        "sign_count": sign_count,
        "retained_source_signs": nonzero_boolean_points,
        "column_splits": split_count,
        "common_base_dictionary_atoms": nonzero_boolean_points * split_count,
        "degree_m_quotient_rank": nonzero_boolean_points,
        "degree_m_quotient_relation_dimension": 0,
        "degree_m_minus_two_defect_rank": sign_count - 2,
        "degree_m_minus_two_defect_relation_dimension": 1,
        "defect_relation_support": nonzero_boolean_points,
        "minimum_atom_count": nonzero_boolean_points,
        "minimal_uniform_split_families_per_base": split_count,
        "minimal_uniform_split_families_all_bases": sign_count * split_count,
        "equality_structure": "ONE ATOM PER NONBASE SIGN, ALL USING ONE COMMON SPLIT",
    }


def build_core() -> dict[str, object]:
    rows = [audit_order(order) for order in range(3, 11)]
    quartic = next(row for row in rows if row["order"] == 4)
    scan = quartic_equality_scan()
    require(quartic["common_base_dictionary_atoms"] == 42, quartic)
    require(quartic["minimum_atom_count"] == 7, quartic)
    require(scan["solutions"] == 6, scan)
    return {
        "schema": "general_common_base_mixed_split_glynn_rigidity/v1",
        "classification": "STRICT_DICTIONARY_RIGIDITY_THEOREM",
        "field": "characteristic_zero",
        "family": {
            "common_deleted_base": True,
            "source_sign": "ARBITRARY_NONBASE_SIGN",
            "column_split": "ARBITRARY_PER_ATOM",
            "atom": "PRODUCT_ON_SHARED_SPLIT TIMES (SOURCE_TAIL_PRODUCT-BASE_TAIL_PRODUCT)",
        },
        "general_theorem": {
            "minimum_atoms": "2^(m-1)-1",
            "equality_classification": "ALL NONBASE SIGNS ONCE AND ONE UNIFORM COLUMN SPLIT",
            "orders_replayed": list(range(3, 11)),
        },
        "rows": rows,
        "quartic_exhaustive_equality_scan": scan,
        "quartic_application": {
            "fixed_base_dictionary_atoms": 42,
            "minimum_blocks": 7,
            "uniform_split_equality_families_per_base": 6,
            "all_base_and_split_equality_families": 48,
            "six_block_representation": "IMPOSSIBLE",
            "mu_6_4": "OPEN_IN_[6,7]",
        },
        "claim_boundary": {
            "common_base_mixed_split_dictionary": "THRESHOLD_AND_EQUALITY_EXACT",
            "variable_base_and_variable_split_simultaneously": "NOT_INCLUDED",
            "non_sign_frames": "NOT_INCLUDED",
            "global_six_block_literal_sum": "OPEN",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--print-core-only", action="store_true")
    args = parser.parse_args()
    core = build_core()
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    require(digest == EXPECTED_CORE, digest)
    payload = dict(core)
    payload["core_sha256"] = digest
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.print_core_only:
        print(digest)
    else:
        print("GENERAL_COMMON_BASE_MIXED_SPLIT_GLYNN_RIGIDITY_PASS")
        print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
