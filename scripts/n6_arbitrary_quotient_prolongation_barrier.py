#!/usr/bin/env python3
"""Exact G-041 counterexample to an arbitrary t2=13 prolongation cap."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAP_SCRIPT = ROOT / "scripts" / "n6_global_quotient_prolongation_caps.py"


def load_caps():
    spec = importlib.util.spec_from_file_location("n6_caps_barrier", CAP_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(CAP_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_payload() -> dict[str, object]:
    caps = load_caps()
    quotient = caps.load_quotient_module()
    blocks, occurrences = caps.cubic_weight_blocks(quotient)

    # Five variables in row zero.  Take all ten pair axes and three squares.
    variables = (0, 2, 3, 4, 5)
    selected: set[int] = set()
    for first_index, first in enumerate(variables):
        for second in variables[first_index + 1 :]:
            axis = quotient.quotient_axis(first, second)[0]
            selected.add(quotient.AXIS_INDEX[axis])
    for variable in (2, 3, 4):
        axis = quotient.quotient_axis(variable, variable)[0]
        selected.add(quotient.AXIS_INDEX[axis])
    if len(selected) != 13:
        raise AssertionError(selected)

    masks: dict[int, int] = {}
    for axis in selected:
        for block_index, bit in occurrences[axis]:
            masks[block_index] = masks.get(block_index, 0) | bit

    modular_dimension = 400
    rational_dimension = 400
    changed_blocks: list[dict[str, object]] = []
    for block_index, mask in masks.items():
        block = blocks[block_index]
        retained = [
            row
            for row, axis in zip(block.rows, block.row_axes)
            if not mask >> block.axis_position[axis] & 1
        ]
        modular_nullity = block.nullity(mask)

        # The relevant blocks are tiny.  Independent rational elimination is
        # used to certify the characteristic-zero equality, not inferred from
        # the finite-field rank.
        from fractions import Fraction

        work = [[Fraction(value) for value in row] for row in retained if any(row)]
        rank = 0
        for column in range(block.column_count):
            pivot = next(
                (row for row in range(rank, len(work)) if work[row][column]), None
            )
            if pivot is None:
                continue
            work[rank], work[pivot] = work[pivot], work[rank]
            scale = work[rank][column]
            work[rank] = [value / scale for value in work[rank]]
            for row in range(rank + 1, len(work)):
                scale = work[row][column]
                if scale:
                    work[row] = [
                        left - scale * right
                        for left, right in zip(work[row], work[rank])
                    ]
            rank += 1
            if rank == len(work):
                break
        rational_nullity = block.column_count - rank
        if rational_nullity != modular_nullity:
            raise AssertionError((block_index, rational_nullity, modular_nullity))
        modular_dimension += modular_nullity - block.base_nullity
        rational_dimension += rational_nullity - block.base_nullity
        if rational_nullity > block.base_nullity:
            changed_blocks.append(
                {
                    "block_index": block_index,
                    "base_nullity": block.base_nullity,
                    "extended_nullity": rational_nullity,
                }
            )

    if modular_dimension != 475 or rational_dimension != 475:
        raise AssertionError((modular_dimension, rational_dimension))
    if len(changed_blocks) != 75:
        raise AssertionError(len(changed_blocks))
    if any(row["extended_nullity"] - row["base_nullity"] != 1 for row in changed_blocks):
        raise AssertionError(changed_blocks)

    return {
        "status": "G_041_ARBITRARY_QUOTIENT_PROLONGATION_BARRIER",
        "field": "characteristic zero",
        "prime_for_regression": caps.PRIME,
        "row_zero_variables": ["x00", "x02", "x03", "x04", "x05"],
        "selected_quotient_axes": [
            list(quotient.QUOTIENT_AXES[axis]) for axis in sorted(selected)
        ],
        "selected_axis_count": len(selected),
        "base_permanent_cubic_dimension": 400,
        "changed_cubic_weight_block_count": len(changed_blocks),
        "increment_per_changed_block": 1,
        "exact_QQ_prolongation_dimension": rational_dimension,
        "modular_regression_prolongation_dimension": modular_dimension,
        "dimension_required_at_b63_h120": 457,
        "strict_excess_over_457": rational_dimension - 457,
        "conclusion": (
            "No dimension-only theorem can bound the first prolongation of "
            "every A containing E2 with dim(A/E2)=13 by less than 457."
        ),
        "claim_boundary": (
            "This coordinate thirteen-plane is not asserted to arise from six "
            "actual alpha-one Chow terms. It does not contradict N6-047, whose "
            "ambient A contains an actual extremal term, and it does not prove "
            "that any surviving all-alpha-one state is realizable."
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
    print("N6_ARBITRARY_QUOTIENT_PROLONGATION_BARRIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
