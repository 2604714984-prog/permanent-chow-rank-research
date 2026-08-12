#!/usr/bin/env python3
"""Exact modular t=15 prolongation cap above an extremal frame (N6-051)."""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
from itertools import combinations
from math import comb
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_global_quotient_prolongation_caps.py"
STATE_DATA = ROOT / "data" / "n6_b60_scalar_frontier.json"
PRIME = 1_000_003
AXIS_COUNT = 441
LOCAL_W_DIMENSION = 12
EXTRA_AXIS_COUNT = 3
PERMANENT_CUBIC_DIMENSION = 400


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_base_module():
    spec = importlib.util.spec_from_file_location("n6_t15_base", BASE_SCRIPT)
    require(spec is not None and spec.loader is not None, BASE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixed_combinatorics(base_module):
    quotient = base_module.load_quotient_module()
    blocks, occurrences = base_module.cubic_weight_blocks(quotient)
    local_axes, representatives, orbit_histogram = (
        base_module.local_axes_and_orbits(quotient)
    )
    occurrence_maps = [dict(rows) for rows in occurrences]

    edges: list[tuple[int, int, tuple[int, ...]]] = []
    for first in range(AXIS_COUNT):
        first_blocks = set(occurrence_maps[first])
        for second in range(first + 1, AXIS_COUNT):
            shared = tuple(
                sorted(first_blocks & set(occurrence_maps[second]))
            )
            if shared:
                edges.append((first, second, shared))

    triple_blocks: dict[tuple[int, int, int], list[int]] = {}
    for block_index, block in enumerate(blocks):
        for triple in combinations(block.axes, 3):
            triple_blocks.setdefault(triple, []).append(block_index)
    triples = sorted(triple_blocks)

    vertex_rows: list[list[tuple[int, int, int]]] = [
        [] for _ in range(AXIS_COUNT)
    ]
    for index, triple in enumerate(triples):
        for vertex in triple:
            others = [value for value in triple if value != vertex]
            vertex_rows[vertex].append((others[0], others[1], index))
    by_vertex = []
    for rows in vertex_rows:
        by_vertex.append(
            tuple(
                np.asarray([row[position] for row in rows], dtype=np.int32)
                for position in range(3)
            )
        )

    require(len(blocks) == 3_136, len(blocks))
    require(len(local_axes) == 18, len(local_axes))
    require(len(representatives) == 1_683, len(representatives))
    require(len(edges) == 19_980, len(edges))
    require(len(triples) == 57_240, len(triples))
    return (
        quotient,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        orbit_histogram,
        edges,
        triples,
        triple_blocks,
        by_vertex,
    )


def evaluate_representative(
    w_axes: tuple[int, ...],
    blocks,
    occurrences,
    occurrence_maps,
    edges,
    triples,
    triple_blocks,
    by_vertex,
) -> tuple[int, tuple[int, int, int], int, int]:
    """Maximize exactly over all three distinct axes outside ``w_axes``."""

    w_set = set(w_axes)
    masks: dict[int, int] = {}
    base_dimension = PERMANENT_CUBIC_DIMENSION
    for axis in w_axes:
        for block_index, bit in occurrences[axis]:
            masks[block_index] = masks.get(block_index, 0) | bit
    for block_index, mask in masks.items():
        block = blocks[block_index]
        base_dimension += block.nullity(mask) - block.base_nullity

    gains = np.full(AXIS_COUNT, -100, dtype=np.int16)
    for axis in range(AXIS_COUNT):
        if axis in w_set:
            continue
        gains[axis] = sum(
            blocks[block_index].nullity(masks.get(block_index, 0) | bit)
            - blocks[block_index].nullity(masks.get(block_index, 0))
            for block_index, bit in occurrences[axis]
        )

    pair_corrections = np.zeros((AXIS_COUNT, AXIS_COUNT), dtype=np.int16)
    for first, second, shared_blocks in edges:
        if first in w_set or second in w_set:
            continue
        correction = 0
        for block_index in shared_blocks:
            block = blocks[block_index]
            old = masks.get(block_index, 0)
            first_bit = occurrence_maps[first][block_index]
            second_bit = occurrence_maps[second][block_index]
            correction += (
                block.nullity(old | first_bit | second_bit)
                - block.nullity(old | first_bit)
                - block.nullity(old | second_bit)
                + block.nullity(old)
            )
        pair_corrections[first, second] = correction
        pair_corrections[second, first] = correction

    triple_corrections = np.zeros(len(triples), dtype=np.int16)
    for index, (first, second, third) in enumerate(triples):
        correction = 0
        for block_index in triple_blocks[(first, second, third)]:
            block = blocks[block_index]
            old = masks.get(block_index, 0)
            first_bit = occurrence_maps[first][block_index]
            second_bit = occurrence_maps[second][block_index]
            third_bit = occurrence_maps[third][block_index]
            correction += (
                block.nullity(old | first_bit | second_bit | third_bit)
                - block.nullity(old | first_bit | second_bit)
                - block.nullity(old | first_bit | third_bit)
                - block.nullity(old | second_bit | third_bit)
                + block.nullity(old | first_bit)
                + block.nullity(old | second_bit)
                + block.nullity(old | third_bit)
                - block.nullity(old)
            )
        triple_corrections[index] = correction

    pair_score = gains[:, None] + gains[None, :] + pair_corrections
    np.fill_diagonal(pair_score, -1_000)
    best_increment = -1
    best_triple = None
    for third in range(AXIS_COUNT):
        candidate = (
            gains[third]
            + pair_corrections[:, third, None]
            + pair_corrections[None, :, third]
        )
        left, right, indices = by_vertex[third]
        values = triple_corrections[indices]
        candidate[left, right] += values
        candidate[right, left] += values
        candidate[third, :] = -1_000
        candidate[:, third] = -1_000
        total = pair_score + candidate
        flat_index = int(total.argmax())
        increment = int(total.ravel()[flat_index])
        if increment > best_increment:
            first, second = divmod(flat_index, AXIS_COUNT)
            best_increment = increment
            best_triple = (first, second, third)

    require(best_triple is not None, w_axes)
    require(not (set(best_triple) & w_set), (w_axes, best_triple))
    require(len(set(best_triple)) == EXTRA_AXIS_COUNT, best_triple)
    return base_dimension + best_increment, best_triple, base_dimension, best_increment


def worker(task: tuple[int, int]) -> dict[str, object]:
    slot, worker_count = task
    base_module = load_base_module()
    (
        quotient,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        _,
        edges,
        triples,
        triple_blocks,
        by_vertex,
    ) = fixed_combinatorics(base_module)

    best_value = -1
    best_row = None
    checked = 0
    for representative_index in range(slot, len(representatives), worker_count):
        w_axes = representatives[representative_index]
        value, extra_axes, base_dimension, increment = evaluate_representative(
            w_axes,
            blocks,
            occurrences,
            occurrence_maps,
            edges,
            triples,
            triple_blocks,
            by_vertex,
        )
        row = {
            "representative_index": representative_index,
            "W_axis_indices": list(w_axes),
            "extra_axis_indices": list(extra_axes),
            "base_prolongation_dimension": base_dimension,
            "three_axis_increment": increment,
        }
        if best_row is None or (value, -representative_index) > (
            best_value,
            -int(best_row["representative_index"]),
        ):
            best_value = value
            best_row = row
        checked += 1
    require(best_row is not None, task)
    return {
        "slot": slot,
        "checked_representatives": checked,
        "maximum": best_value,
        "maximizer": best_row,
    }


def compute_cap(worker_count: int) -> dict[str, object]:
    require(1 <= worker_count <= 64, worker_count)
    if worker_count == 1:
        rows = [worker((0, 1))]
    else:
        context = mp.get_context("spawn")
        with context.Pool(worker_count) as pool:
            rows = pool.map(worker, [(slot, worker_count) for slot in range(worker_count)])
    require(sum(int(row["checked_representatives"]) for row in rows) == 1_683, rows)
    best = min(
        (row for row in rows if int(row["maximum"]) == max(int(x["maximum"]) for x in rows)),
        key=lambda row: int(row["maximizer"]["representative_index"]),
    )
    require(int(best["maximum"]) == 458, best)

    base_module = load_base_module()
    quotient = base_module.load_quotient_module()
    sample = best["maximizer"]
    return {
        "worker_count": worker_count,
        "checked_orbit_representative_count": 1_683,
        "maximum_modular_nullity": int(best["maximum"]),
        "sample_maximizer": {
            "representative_index": int(sample["representative_index"]),
            "W_axes": [
                list(quotient.QUOTIENT_AXES[index])
                for index in sample["W_axis_indices"]
            ],
            "extra_axes": [
                list(quotient.QUOTIENT_AXES[index])
                for index in sample["extra_axis_indices"]
            ],
            "base_prolongation_dimension": int(
                sample["base_prolongation_dimension"]
            ),
            "three_axis_increment": int(sample["three_axis_increment"]),
        },
    }


def state_pruning(cap: int) -> dict[str, object]:
    payload = json.loads(STATE_DATA.read_text(encoding="utf-8"))
    frontier = [
        state
        for state in payload["states"]
        if not state["excluded_by_existing_cap"]
    ]
    require(len(frontier) == 84, len(frontier))

    extremal = []
    alpha_one = []
    remaining = []
    for state in frontier:
        required = (
            PERMANENT_CUBIC_DIMENSION
            + int(state["fixed_middle_rank_h_lower"])
            - int(payload["layer_parameters"]["middle_intersection_b"])
        )
        require(required == 460 and required > cap, (state, required, cap))
        if int(state["extremal_term_count"]):
            extremal.append(state["state_id"])
        elif int(state["alpha_one_term_count"]):
            alpha_one.append(state["state_id"])
        else:
            remaining.append(state)

    require((len(extremal), len(alpha_one), len(remaining)) == (56, 21, 7), (
        len(extremal), len(alpha_one), len(remaining)
    ))
    require(
        all(
            all(pair[1] in (2, 3) for pair in state["epsilon_alpha_pairs"])
            for state in remaining
        ),
        remaining,
    )
    return {
        "input_t15_frontier_count": len(frontier),
        "excluded_by_extremal_t15_cap_count": len(extremal),
        "excluded_by_extremal_t15_cap_ids": extremal,
        "excluded_by_alpha1_t15_closure_count": len(alpha_one),
        "excluded_by_alpha1_t15_closure_ids": alpha_one,
        "remaining_count": len(remaining),
        "remaining_state_ids": [state["state_id"] for state in remaining],
        "remaining_epsilon_alpha_pairs": [
            state["epsilon_alpha_pairs"] for state in remaining
        ],
    }


def build_payload(computation: dict[str, object]) -> dict[str, object]:
    cap = int(computation["maximum_modular_nullity"])
    pruning = state_pruning(cap)
    return {
        "status": "N6_051_GLOBAL_T15_PROLONGATION_CAP",
        "arithmetic": (
            "exact ranks modulo 1000003; modular nullities are rigorous "
            "characteristic-zero upper bounds"
        ),
        "prime": PRIME,
        "fixed_cubic_weight_block_count": 3_136,
        "local_quotient_axis_count": 18,
        "fixed_W_count": 18_564,
        "fixed_W_orbit_representative_count": 1_683,
        "ambient_quotient_axis_count": AXIS_COUNT,
        "extra_axis_count": EXTRA_AXIS_COUNT,
        "extra_axis_triples_per_W": comb(AXIS_COUNT - LOCAL_W_DIMENSION, 3),
        "represented_fixed_configurations": (
            18_564 * comb(AXIS_COUNT - LOCAL_W_DIMENSION, 3)
        ),
        "interacting_axis_pair_count": 19_980,
        "common_block_axis_triple_count": 57_240,
        "characteristic_zero_prolongation_upper_cap_t15": cap,
        "sample_maximizer": computation["sample_maximizer"],
        "state_pruning": pruning,
        "strict_conclusion": (
            "The universal t=15 prolongation cap is 458 above an extremal "
            "term and on the alpha-one closure. It excludes 56 extremal and "
            "21 additional alpha-one states from the N6-050 frontier; seven "
            "alpha-two/alpha-three states remain."
        ),
        "claim_boundary": (
            "The cap does not cover the one-rectangle alpha-two t=15 branch "
            "or an all-alpha-three state. It does not yet exclude b=60, prove "
            "ChowRank(perm_6)>=27, or make a border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workers",
        type=int,
        default=min(10, os.cpu_count() or 1),
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    computation = compute_cap(args.workers)
    payload = build_payload(computation)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print(f"workers={args.workers}")
    print(f"t15_cap={payload['characteristic_zero_prolongation_upper_cap_t15']}")
    print(f"remaining_states={payload['state_pruning']['remaining_count']}")
    print("N6_GLOBAL_T15_PROLONGATION_CAP_PASS")
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
