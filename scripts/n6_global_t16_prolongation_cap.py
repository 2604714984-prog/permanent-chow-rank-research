#!/usr/bin/env python3
"""Exact modular t=16 prolongation cap above an extremal frame (N6-095)."""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
T15_SCRIPT = ROOT / "scripts" / "n6_global_t15_prolongation_cap.py"
PRIME = 1_000_003
AXIS_COUNT = 441
LOCAL_W_DIMENSION = 12
EXTRA_AXIS_COUNT = 4
PERMANENT_CUBIC_DIMENSION = 400


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_t15_module():
    spec = importlib.util.spec_from_file_location("n6_t16_t15", T15_SCRIPT)
    require(spec is not None and spec.loader is not None, T15_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixed_data():
    t15 = load_t15_module()
    base = t15.load_base_module()
    (
        quotient,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        orbit_histogram,
        _,
        _,
        _,
        _,
    ) = t15.fixed_combinatorics(base)
    return (
        quotient,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        orbit_histogram,
    )


def base_masks_and_gains(w_axes, blocks, occurrences):
    w_set = set(w_axes)
    masks: dict[int, int] = {}
    for axis in w_axes:
        for block_index, bit in occurrences[axis]:
            masks[block_index] = masks.get(block_index, 0) | bit

    base_dimension = PERMANENT_CUBIC_DIMENSION + sum(
        blocks[index].nullity(mask) - blocks[index].base_nullity
        for index, mask in masks.items()
    )
    gains = np.full(AXIS_COUNT, -1_000, dtype=np.int16)
    for axis in range(AXIS_COUNT):
        if axis in w_set:
            continue
        gains[axis] = sum(
            blocks[index].nullity(masks.get(index, 0) | bit)
            - blocks[index].nullity(masks.get(index, 0))
            for index, bit in occurrences[axis]
        )
    return masks, base_dimension, gains


def mobius_corrections(
    order: int,
    w_axes,
    masks,
    blocks,
    occurrence_maps,
) -> dict[tuple[int, ...], int]:
    """Return every nonzero order-``order`` block-nullity correction."""

    w_set = set(w_axes)
    common_blocks: dict[tuple[int, ...], list[int]] = {}
    for block_index, block in enumerate(blocks):
        available = [axis for axis in block.axes if axis not in w_set]
        for axes in combinations(available, order):
            common_blocks.setdefault(axes, []).append(block_index)

    corrections: dict[tuple[int, ...], int] = {}
    for axes, block_indices in common_blocks.items():
        value = 0
        for block_index in block_indices:
            block = blocks[block_index]
            old_mask = masks.get(block_index, 0)
            for size in range(order + 1):
                sign = -1 if (order - size) % 2 else 1
                for subset in combinations(axes, size):
                    mask = old_mask
                    for axis in subset:
                        mask |= occurrence_maps[axis][block_index]
                    value += sign * block.nullity(mask)
        if value:
            corrections[axes] = value
    return corrections


def direct_dimension(
    w_axes,
    extra_axes,
    blocks,
    occurrences,
) -> int:
    masks, base_dimension, _ = base_masks_and_gains(
        w_axes, blocks, occurrences
    )
    updated = dict(masks)
    touched: set[int] = set()
    for axis in extra_axes:
        for block_index, bit in occurrences[axis]:
            updated[block_index] = updated.get(block_index, 0) | bit
            touched.add(block_index)
    return base_dimension + sum(
        blocks[index].nullity(updated[index])
        - blocks[index].nullity(masks.get(index, 0))
        for index in touched
    )


def maximize_four_axes(
    w_axes,
    blocks,
    occurrences,
    occurrence_maps,
) -> dict[str, object]:
    """Maximize exactly over four distinct quotient axes outside ``w_axes``."""

    masks, base_dimension, gains = base_masks_and_gains(
        w_axes, blocks, occurrences
    )
    c2 = mobius_corrections(
        2, w_axes, masks, blocks, occurrence_maps
    )
    c3 = mobius_corrections(
        3, w_axes, masks, blocks, occurrence_maps
    )
    c4 = mobius_corrections(
        4, w_axes, masks, blocks, occurrence_maps
    )

    pair_adjacency: list[dict[int, int]] = [
        {} for _ in range(AXIS_COUNT)
    ]
    for (first, second), value in c2.items():
        pair_adjacency[first][second] = value
        pair_adjacency[second][first] = value

    triple_by_pair: dict[tuple[int, int], dict[int, int]] = defaultdict(dict)
    triples_by_vertex: list[list[tuple[tuple[int, int], int]]] = [
        [] for _ in range(AXIS_COUNT)
    ]
    for axes, value in c3.items():
        for first, second in combinations(axes, 2):
            third = next(axis for axis in axes if axis not in (first, second))
            triple_by_pair[(first, second)][third] = value
        for vertex in axes:
            remainder = tuple(axis for axis in axes if axis != vertex)
            triples_by_vertex[vertex].append((remainder, value))

    quads_by_pair: dict[
        tuple[int, int], list[tuple[tuple[int, int], int]]
    ] = defaultdict(list)
    quads_by_triple: dict[tuple[int, int, int], dict[int, int]] = (
        defaultdict(dict)
    )
    for axes, value in c4.items():
        for first, second in combinations(axes, 2):
            remainder = tuple(axis for axis in axes if axis not in (first, second))
            quads_by_pair[(first, second)].append((remainder, value))
        for triple in combinations(axes, 3):
            fourth = next(axis for axis in axes if axis not in triple)
            quads_by_triple[triple][fourth] = value

    pair_keys = list(c2)
    pair_first = np.asarray([pair[0] for pair in pair_keys], dtype=np.int32)
    pair_second = np.asarray([pair[1] for pair in pair_keys], dtype=np.int32)
    pair_values = np.asarray([c2[pair] for pair in pair_keys], dtype=np.int16)

    available = [axis for axis in range(AXIS_COUNT) if axis not in set(w_axes)]
    baseline_axes = tuple(
        sorted(available, key=lambda axis: (-int(gains[axis]), axis))[:4]
    )
    best_increment = sum(int(gains[axis]) for axis in baseline_axes)
    best_axes = baseline_axes
    best_source = "singleton"

    def consider(value: int, axes, source: str) -> None:
        nonlocal best_increment, best_axes, best_source
        canonical = tuple(sorted(int(axis) for axis in axes))
        if value > best_increment or (
            value == best_increment and canonical < best_axes
        ):
            best_increment = value
            best_axes = canonical
            best_source = source

    # Every four-set having a nonzero pair correction is covered here.
    for first, second in pair_keys:
        weights = gains.astype(np.int32).copy()
        weights[first] = weights[second] = -100_000
        for axis, value in pair_adjacency[first].items():
            weights[axis] += value
        for axis, value in pair_adjacency[second].items():
            weights[axis] += value
        for axis, value in triple_by_pair[(first, second)].items():
            weights[axis] += value

        extra_pair_bonus: dict[tuple[int, int], int] = defaultdict(int)
        for pair, value in triples_by_vertex[first]:
            if second not in pair:
                extra_pair_bonus[pair] += value
        for pair, value in triples_by_vertex[second]:
            if first not in pair:
                extra_pair_bonus[pair] += value
        for pair, value in quads_by_pair[(first, second)]:
            extra_pair_bonus[pair] += value

        top = np.argpartition(weights, -2)[-2:]
        completion_value = int(weights[top[0]] + weights[top[1]])
        completion_pair = (int(top[0]), int(top[1]))

        values = (
            weights[pair_first]
            + weights[pair_second]
            + pair_values
            + np.asarray(
                [extra_pair_bonus.get(pair, 0) for pair in pair_keys],
                dtype=np.int16,
            )
        )
        forbidden = (
            (pair_first == first)
            | (pair_first == second)
            | (pair_second == first)
            | (pair_second == second)
        )
        values[forbidden] = -100_000
        index = int(values.argmax())
        if int(values[index]) > completion_value:
            completion_value = int(values[index])
            completion_pair = pair_keys[index]

        for pair, bonus in extra_pair_bonus.items():
            if pair in c2 or first in pair or second in pair:
                continue
            value = int(weights[pair[0]] + weights[pair[1]] + bonus)
            if value > completion_value:
                completion_value = value
                completion_pair = pair

        value = (
            int(gains[first])
            + int(gains[second])
            + c2[(first, second)]
            + completion_value
        )
        consider(value, (first, second) + completion_pair, "pair")

    # If no pair correction is present, a nonzero triple correction is next.
    for triple, triple_value in c3.items():
        if any(pair in c2 for pair in combinations(triple, 2)):
            continue
        weights = gains.astype(np.int32).copy()
        weights[list(triple)] = -100_000
        for vertex in triple:
            for axis, value in pair_adjacency[vertex].items():
                weights[axis] += value
        for pair in combinations(triple, 2):
            for axis, value in triple_by_pair[pair].items():
                weights[axis] += value
        for axis, value in quads_by_triple[triple].items():
            weights[axis] += value
        fourth = int(weights.argmax())
        value = sum(int(gains[axis]) for axis in triple) + triple_value
        consider(value + int(weights[fourth]), triple + (fourth,), "triple")

    # A remaining set can only be detected by its nonzero fourth correction.
    for axes, fourth_value in c4.items():
        value = sum(int(gains[axis]) for axis in axes)
        value += sum(c2.get(pair, 0) for pair in combinations(axes, 2))
        value += sum(c3.get(triple, 0) for triple in combinations(axes, 3))
        consider(value + fourth_value, axes, "quadruple")

    dimension = base_dimension + best_increment
    require(
        direct_dimension(w_axes, best_axes, blocks, occurrences) == dimension,
        (w_axes, best_axes, dimension),
    )
    return {
        "dimension": dimension,
        "base_dimension": base_dimension,
        "increment": best_increment,
        "extra_axis_indices": list(best_axes),
        "maximizer_source": best_source,
        "nonzero_correction_counts": {
            "2": len(c2),
            "3": len(c3),
            "4": len(c4),
        },
    }


def worker(task: tuple[int, int]) -> dict[str, object]:
    slot, worker_count = task
    (
        _,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        _,
    ) = fixed_data()
    best: dict[str, object] | None = None
    checked = 0
    for index in range(slot, len(representatives), worker_count):
        row = maximize_four_axes(
            representatives[index], blocks, occurrences, occurrence_maps
        )
        row["representative_index"] = index
        row["W_axis_indices"] = list(representatives[index])
        if best is None or (
            int(row["dimension"]), -index
        ) > (int(best["dimension"]), -int(best["representative_index"])):
            best = row
        checked += 1
    require(best is not None, task)
    return {
        "slot": slot,
        "checked_representatives": checked,
        "maximum": int(best["dimension"]),
        "maximizer": best,
    }


def compute_cap(worker_count: int) -> dict[str, object]:
    require(1 <= worker_count <= 64, worker_count)
    if worker_count == 1:
        rows = [worker((0, 1))]
    else:
        context = mp.get_context("spawn")
        with context.Pool(worker_count) as pool:
            rows = pool.map(
                worker,
                [(slot, worker_count) for slot in range(worker_count)],
            )
    require(
        sum(int(row["checked_representatives"]) for row in rows) == 1_683,
        rows,
    )
    maximum = max(int(row["maximum"]) for row in rows)
    best = min(
        (row for row in rows if int(row["maximum"]) == maximum),
        key=lambda row: int(row["maximizer"]["representative_index"]),
    )
    _, _, _, _, representatives, histogram = fixed_data()
    sample = best["maximizer"]
    quotient = fixed_data()[0]
    return {
        "worker_count": worker_count,
        "checked_orbit_representative_count": len(representatives),
        "fixed_W_orbit_size_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "maximum_modular_nullity": maximum,
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
            "base_prolongation_dimension": int(sample["base_dimension"]),
            "four_axis_increment": int(sample["increment"]),
            "maximizer_source": sample["maximizer_source"],
            "nonzero_correction_counts": sample[
                "nonzero_correction_counts"
            ],
        },
    }


def build_payload(computation: dict[str, object]) -> dict[str, object]:
    cap = int(computation["maximum_modular_nullity"])
    return {
        "status": "N6_095_GLOBAL_T16_PROLONGATION_CAP",
        "arithmetic": (
            "exact ranks modulo 1000003; modular nullities are rigorous "
            "characteristic-zero upper bounds"
        ),
        "prime": PRIME,
        "fixed_cubic_weight_block_count": 3_136,
        "local_quotient_axis_count": 18,
        "fixed_W_count": 18_564,
        "fixed_W_orbit_representative_count": 1_683,
        "fixed_W_orbit_size_histogram": computation[
            "fixed_W_orbit_size_histogram"
        ],
        "ambient_quotient_axis_count": AXIS_COUNT,
        "extra_axis_count": EXTRA_AXIS_COUNT,
        "extra_axis_quadruples_per_W": comb(
            AXIS_COUNT - LOCAL_W_DIMENSION, EXTRA_AXIS_COUNT
        ),
        "represented_fixed_configurations": (
            18_564
            * comb(AXIS_COUNT - LOCAL_W_DIMENSION, EXTRA_AXIS_COUNT)
        ),
        "characteristic_zero_prolongation_upper_cap_t16": cap,
        "sample_maximizer": computation["sample_maximizer"],
        "strict_conclusion": (
            "The projective fixed-point reduction and exhaustive four-axis "
            f"optimization give the characteristic-zero upper cap {cap} "
            "for a sixteen-dimensional global quadratic quotient containing "
            "an extremal actual term or a term on the actual alpha-one "
            "closure."
        ),
        "claim_boundary": (
            "This cap covers the extremal and alpha-one closures. The "
            "one-rectangle alpha-two boundary requires a separate exhaustive "
            "calculation. It makes no border-rank or lower29 claim by itself."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workers", type=int, default=min(10, os.cpu_count() or 1)
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
    print(
        "t16_cap="
        f"{payload['characteristic_zero_prolongation_upper_cap_t16']}"
    )
    print("N6_GLOBAL_T16_PROLONGATION_CAP_PASS")
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
