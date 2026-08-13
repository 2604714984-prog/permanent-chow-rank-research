#!/usr/bin/env python3
"""Exact t=16 prolongation cap for an actual alpha-two term (N6-096)."""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALPHA2_T15_SCRIPT = ROOT / "scripts" / "n6_alpha2_t15_prolongation_cap.py"
T16_SCRIPT = ROOT / "scripts" / "n6_global_t16_prolongation_cap.py"
T16_DATA = ROOT / "data" / "n6_global_t16_prolongation_cap.json"
PRIME = 1_000_003
AXIS_COUNT = 441
PERMANENT_CUBIC_DIMENSION = 400


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixed_input(suffix: str):
    alpha2 = load_module(
        ALPHA2_T15_SCRIPT, f"n6096_alpha2_t15_{suffix}"
    )
    t16 = load_module(T16_SCRIPT, f"n6096_t16_{suffix}")
    quotient, blocks, occurrences, support_rows = alpha2.fixed_input(suffix)
    occurrence_maps = [dict(rows) for rows in occurrences]
    edges: list[tuple[int, int, tuple[int, ...]]] = []
    occurrence_blocks = [set(row) for row in occurrence_maps]
    for first in range(AXIS_COUNT):
        for second in range(first + 1, AXIS_COUNT):
            shared = tuple(sorted(occurrence_blocks[first] & occurrence_blocks[second]))
            if shared:
                edges.append((first, second, shared))
    require(len(edges) == 19_980, len(edges))
    return (
        alpha2,
        t16,
        quotient,
        blocks,
        occurrences,
        occurrence_maps,
        edges,
        support_rows,
    )


def pair_correction_bound_certificate(blocks) -> dict[str, object]:
    histogram: dict[int, int] = {}
    maximum = -1
    checked = 0
    for block in blocks:
        axis_count = len(block.axes)
        for mask in range(1 << axis_count):
            for first, second in combinations(range(axis_count), 2):
                first_bit = 1 << first
                second_bit = 1 << second
                correction = (
                    block.nullity(mask | first_bit | second_bit)
                    - block.nullity(mask | first_bit)
                    - block.nullity(mask | second_bit)
                    + block.nullity(mask)
                )
                histogram[correction] = histogram.get(correction, 0) + 1
                maximum = max(maximum, correction)
                checked += 1
    require(maximum == 1, (maximum, histogram))
    return {
        "checked_block_mask_axis_pairs": checked,
        "correction_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "maximum_pair_correction_per_shared_block": maximum,
    }


def maximize_two_extras(
    qf_axes,
    t16,
    blocks,
    occurrences,
    occurrence_maps,
    edges,
) -> dict[str, object]:
    masks, base_dimension, gains = t16.base_masks_and_gains(
        qf_axes, blocks, occurrences
    )
    qf_set = set(qf_axes)
    available = [axis for axis in range(AXIS_COUNT) if axis not in qf_set]
    ordered = sorted(available, key=lambda axis: (-int(gains[axis]), axis))
    best_gain = int(gains[ordered[0]] + gains[ordered[1]])
    best_pair = (ordered[0], ordered[1])
    evaluated = 0

    for first, second, shared_blocks in edges:
        if first in qf_set or second in qf_set:
            continue
        gain_sum = int(gains[first] + gains[second])
        if gain_sum + len(shared_blocks) <= best_gain:
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
        evaluated += 1
        value = gain_sum + correction
        if value > best_gain or (
            value == best_gain and (first, second) < best_pair
        ):
            best_gain = value
            best_pair = (first, second)

    dimension = base_dimension + best_gain
    require(
        t16.direct_dimension(qf_axes, best_pair, blocks, occurrences)
        == dimension,
        (qf_axes, best_pair, dimension),
    )
    return {
        "dimension": dimension,
        "base_dimension": base_dimension,
        "two_axis_increment": best_gain,
        "extra_axis_indices": list(best_pair),
        "evaluated_interacting_pairs": evaluated,
    }


def worker(task: tuple[int, int]) -> dict[str, object]:
    slot, worker_count = task
    (
        _,
        t16,
        _,
        blocks,
        occurrences,
        occurrence_maps,
        edges,
        support_rows,
    ) = fixed_input(str(slot))
    maxima = [-1] * len(support_rows)
    samples: list[dict[str, object] | None] = [None] * len(support_rows)
    checked = 0
    global_index = 0
    evaluated_pairs = 0

    for support_row in support_rows:
        support_index = int(support_row["support_index"])
        for qf_axes in support_row["representatives"]:
            if global_index % worker_count == slot:
                result = maximize_two_extras(
                    qf_axes,
                    t16,
                    blocks,
                    occurrences,
                    occurrence_maps,
                    edges,
                )
                result["support_index"] = support_index
                result["global_representative_index"] = global_index
                result["qF_axis_indices"] = list(qf_axes)
                evaluated_pairs += int(result["evaluated_interacting_pairs"])
                if samples[support_index] is None or (
                    int(result["dimension"]), -global_index
                ) > (
                    maxima[support_index],
                    -int(samples[support_index]["global_representative_index"]),
                ):
                    maxima[support_index] = int(result["dimension"])
                    samples[support_index] = result
                checked += 1
            global_index += 1
    require(global_index == 173_388, global_index)
    return {
        "slot": slot,
        "checked_representatives": checked,
        "evaluated_interacting_pairs": evaluated_pairs,
        "support_maxima": maxima,
        "support_samples": samples,
    }


def compute_cap(worker_count: int) -> dict[str, object]:
    require(1 <= worker_count <= 64, worker_count)
    if worker_count == 1:
        worker_rows = [worker((0, 1))]
    else:
        context = mp.get_context("spawn")
        with context.Pool(worker_count) as pool:
            worker_rows = pool.map(
                worker,
                [(slot, worker_count) for slot in range(worker_count)],
            )
    require(
        sum(int(row["checked_representatives"]) for row in worker_rows)
        == 173_388,
        worker_rows,
    )

    (
        _,
        _,
        quotient,
        blocks,
        _,
        _,
        _,
        support_rows,
    ) = fixed_input("parent")
    bound = pair_correction_bound_certificate(blocks)
    result_rows = []
    for support_index, support_row in enumerate(support_rows):
        candidates = []
        for row in worker_rows:
            sample = row["support_samples"][support_index]
            if sample is not None:
                candidates.append(sample)
        maximum = max(int(sample["dimension"]) for sample in candidates)
        sample = min(
            (row for row in candidates if int(row["dimension"]) == maximum),
            key=lambda row: int(row["global_representative_index"]),
        )
        result_rows.append(
            {
                "support_index": support_index,
                "support": [list(edge) for edge in support_row["support"]],
                "marked_support_count": int(
                    support_row["marked_support_count"]
                ),
                "qF_orbit_representative_count": len(
                    support_row["representatives"]
                ),
                "prolongation_upper_cap": maximum,
                "sample_maximizer": {
                    "global_representative_index": int(
                        sample["global_representative_index"]
                    ),
                    "qF_axes": [
                        list(quotient.QUOTIENT_AXES[index])
                        for index in sample["qF_axis_indices"]
                    ],
                    "extra_axes": [
                        list(quotient.QUOTIENT_AXES[index])
                        for index in sample["extra_axis_indices"]
                    ],
                    "base_prolongation_dimension": int(
                        sample["base_dimension"]
                    ),
                    "two_axis_increment": int(sample["two_axis_increment"]),
                },
            }
        )
    return {
        "worker_count": worker_count,
        "checked_representatives": 173_388,
        "evaluated_interacting_pairs_after_pruning": sum(
            int(row["evaluated_interacting_pairs"]) for row in worker_rows
        ),
        "pair_correction_bound_certificate": bound,
        "support_rows": result_rows,
        "one_rectangle_cap": max(
            int(row["prolongation_upper_cap"]) for row in result_rows
        ),
    }


def build_payload(computation: dict[str, object]) -> dict[str, object]:
    t16 = json.loads(T16_DATA.read_text(encoding="utf-8"))
    three_rectangle_cap = int(
        t16["characteristic_zero_prolongation_upper_cap_t16"]
    )
    one_rectangle_cap = int(computation["one_rectangle_cap"])
    universal_cap = max(three_rectangle_cap, one_rectangle_cap)
    return {
        "status": "N6_096_ALPHA2_T16_PROLONGATION_CAP",
        "arithmetic": (
            "exact ranks modulo 1000003; modular nullities are rigorous "
            "characteristic-zero upper bounds"
        ),
        "prime": PRIME,
        "one_rectangle_support_orbit_count": 12,
        "one_rectangle_qF_orbit_representative_count": 173_388,
        "checked_one_rectangle_qF_representatives": computation[
            "checked_representatives"
        ],
        "evaluated_interacting_pairs_after_pruning": computation[
            "evaluated_interacting_pairs_after_pruning"
        ],
        "pair_correction_bound_certificate": computation[
            "pair_correction_bound_certificate"
        ],
        "one_rectangle_support_rows": computation["support_rows"],
        "one_rectangle_prolongation_upper_cap_t16": one_rectangle_cap,
        "three_rectangle_prolongation_upper_cap_t16_from_N6_095": (
            three_rectangle_cap
        ),
        "universal_alpha2_t16_prolongation_upper_cap": universal_cap,
        "direct_packet_required_prolongation_lower": 468,
        "direct_packet_gap_when_alpha_at_most_two": 468 - universal_cap,
        "strict_conclusion": (
            "Every direct b=34, x=72 configuration containing a term with "
            f"alpha at most two has prolongation dimension at most {universal_cap}, "
            "strictly below the required 468. Any direct-packet survivor must "
            "therefore have alpha three for all seven terms."
        ),
        "claim_boundary": (
            "The all-alpha-three direct packet and the one-defective-term "
            "packet remain open. This does not exclude x=72 or b=34, prove "
            "ordinary lower29, or imply a border-rank bound."
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
        "alpha2_t16_cap="
        f"{payload['universal_alpha2_t16_prolongation_upper_cap']}"
    )
    print("N6_ALPHA2_T16_PROLONGATION_CAP_PASS")
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
