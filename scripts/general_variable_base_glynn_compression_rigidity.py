#!/usr/bin/env python3
"""Exact replay for variable-base one-term Glynn compression rigidity."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

EXPECTED_CORE = "6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def signs(order: int) -> tuple[tuple[int, ...], ...]:
    return tuple((1,) + tail for tail in product((1, -1), repeat=order - 1))


def character(value: tuple[int, ...]) -> int:
    result = 1
    for entry in value:
        result *= entry
    return result


def abstract_left_coordinates(order: int) -> tuple[tuple[int, ...], ...]:
    values = signs(order)
    characters = tuple(character(value) for value in values)
    dimension = len(values) - 1
    result = []
    for index in range(len(values)):
        if index == 0:
            result.append(tuple(-characters[j] for j in range(1, len(values))))
        else:
            row = [0] * dimension
            row[index - 1] = 1
            result.append(tuple(row))
    require(
        all(
            sum(characters[index] * result[index][column] for index in range(len(values))) == 0
            for column in range(dimension)
        ),
        order,
    )
    return tuple(result)


def tail_tensor(value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left * right for left in value for right in value)


def add_outer(
    target: list[int],
    left: tuple[int, ...],
    right: tuple[int, ...],
    scalar: int,
) -> None:
    width = len(right)
    for row, left_value in enumerate(left):
        if not left_value:
            continue
        offset = row * width
        for column, right_value in enumerate(right):
            target[offset + column] += scalar * left_value * right_value


def direct_reconstruction(order: int) -> dict[str, int]:
    values = signs(order)
    left = abstract_left_coordinates(order)
    tails = tuple(tail_tensor(value) for value in values)
    characters = tuple(character(value) for value in values)
    dimension = len(values) - 1
    width = order * order
    target = [0] * (dimension * width)
    for index in range(len(values)):
        add_outer(target, left[index], tails[index], characters[index])

    checked = 0
    for omitted in range(len(values)):
        compressed = [0] * len(target)
        for index in range(len(values)):
            if index == omitted:
                continue
            difference = tuple(
                tails[index][position] - tails[omitted][position]
                for position in range(width)
            )
            add_outer(compressed, left[index], difference, characters[index])
        require(compressed == target, (order, omitted))
        checked += 1
    return {
        "omitted_bases_checked": checked,
        "target_coordinate_count": len(target),
    }


def order_row(order: int) -> dict[str, object]:
    sign_count = 1 << (order - 1)
    full_character_mask = sign_count - 1
    reachable_masks = tuple(mask for mask in range(sign_count) if mask != full_character_mask)
    require(len(reachable_masks) == sign_count - 1, order)
    values = signs(order)
    tails = {tail_tensor(value) for value in values}
    require(len(tails) == sign_count, order)
    return {
        "order": order,
        "sign_count": sign_count,
        "left_tensor_rank": sign_count - 1,
        "unique_left_relation_dimension": 1,
        "missing_walsh_character_mask": full_character_mask,
        "reachable_parity_masks": len(reachable_masks),
        "directed_dictionary_atoms": sign_count * (sign_count - 1),
        "minimum_dictionary_atoms": sign_count - 1,
        "equality_families": sign_count,
        "tail_rank_one_points": len(tails),
        "secant_minor_constant": 4,
    }


def build_core() -> dict[str, object]:
    rows = [order_row(order) for order in range(3, 11)]
    reconstructions = {
        str(order): direct_reconstruction(order)
        for order in range(3, 7)
    }
    quartic = next(row for row in rows if row["order"] == 4)
    require(quartic["directed_dictionary_atoms"] == 56, quartic)
    require(quartic["minimum_dictionary_atoms"] == 7, quartic)
    require(quartic["equality_families"] == 8, quartic)
    return {
        "schema": "general_variable_base_glynn_compression_rigidity/v1",
        "classification": "EXACT_RESTRICTED_DICTIONARY_RIGIDITY",
        "field": "characteristic_zero",
        "family": {
            "atom": "U_v tensor (B_v-B_u), v!=u",
            "U_v": "v tensor power (m-2)",
            "B_v": "v tensor v",
            "bases_may_vary_by_atom": True,
            "column_split_is_fixed": True,
        },
        "rows": rows,
        "direct_reconstructions": reconstructions,
        "quartic": {
            "directed_atoms": quartic["directed_dictionary_atoms"],
            "minimum_atoms": quartic["minimum_dictionary_atoms"],
            "equality_families": quartic["equality_families"],
            "consequence": "SIX_ATOMS_IMPOSSIBLE_IN_VARIABLE_BASE_FIXED_SPLIT_FAMILY",
        },
        "proof_interface": {
            "grouped_source_equation": "Y_v=chi(v)*(B_v+Z)",
            "absent_source_forces": "Z=-B_v",
            "maximum_absent_sources": 1,
            "equality_classification": "exactly one omitted source and a common omitted base",
            "no_three_tail_points_collinear": "two-sign secant has nonzero 2x2 minor 4*alpha*beta",
        },
        "claim_boundary": {
            "variable_base_fixed_split_threshold": "2^(m-1)-1",
            "quartic_threshold": 7,
            "global_six_block_literal_sum": "OPEN",
            "mixed_column_splits": "NOT_EXCLUDED",
            "remote_non_sign_frames": "NOT_EXCLUDED",
            "mu_6_4": "OPEN_IN_[6,7]",
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
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.print_core_only:
        print(digest)
    else:
        print("GENERAL_VARIABLE_BASE_GLYNN_COMPRESSION_RIGIDITY_PASS")
        print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
