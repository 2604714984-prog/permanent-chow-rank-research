#!/usr/bin/env python3
"""Exact t=15 prolongation cap for an actual alpha-two term (N6-052)."""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path

try:
    from n6_resource_policy import (
        GIB,
        parse_worker_argument,
        resolve_worker_count,
    )
except ModuleNotFoundError:
    from scripts.n6_resource_policy import (
        GIB,
        parse_worker_argument,
        resolve_worker_count,
    )


ROOT = Path(__file__).resolve().parents[1]
ALPHA2_SCRIPT = ROOT / "scripts" / "n6_alpha2_prolongation_exclusion.py"
T15_SCRIPT = ROOT / "scripts" / "n6_global_t15_prolongation_cap.py"
T15_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
PRIME = 1_000_003
AXIS_COUNT = 441
LOCAL_QF_DIMENSION = 14
PERMANENT_CUBIC_DIMENSION = 400
EXPECTED_REPRESENTATIVE_COUNTS = (
    10_292,
    9_892,
    38_760,
    19_608,
    19_608,
    19_608,
    10_292,
    9_892,
    19_608,
    5_276,
    5_276,
    5_276,
)
_SHAPE_CONTEXT = None


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def support_orbit_representatives(alpha2, quotient, support):
    """All fourteen-axis local quotients modulo the support automorphism group."""

    support_set = frozenset(support)
    automorphisms = [
        (rows, columns)
        for rows, columns in alpha2.STABILIZER
        if frozenset((rows[row], columns[column]) for row, column in support_set)
        == support_set
    ]
    edges = tuple(row * 6 + column for row, column in support)
    local_axes: list[int] = []
    axis_pairs: dict[int, tuple[int, int]] = {}
    for left, right in combinations_with_replacement(edges, 2):
        axis = quotient.AXIS_INDEX[quotient.quotient_axis(left, right)[0]]
        if axis not in local_axes:
            local_axes.append(axis)
            axis_pairs[axis] = (left, right)
    require(len(local_axes) == 20, (support, local_axes))

    axis_position = {axis: index for index, axis in enumerate(local_axes)}
    actions = set()
    for rows, columns in automorphisms:
        permutation = []
        for axis in local_axes:
            left, right = axis_pairs[axis]
            left_row, left_column = divmod(left, 6)
            right_row, right_column = divmod(right, 6)
            new_left = rows[left_row] * 6 + columns[left_column]
            new_right = rows[right_row] * 6 + columns[right_column]
            image = quotient.AXIS_INDEX[
                quotient.quotient_axis(new_left, new_right)[0]
            ]
            permutation.append(axis_position[image])
        actions.add(tuple(permutation))

    seen: set[tuple[int, ...]] = set()
    representatives: list[tuple[int, ...]] = []
    orbit_histogram: Counter[int] = Counter()
    for raw in combinations(range(20), LOCAL_QF_DIMENSION):
        if raw in seen:
            continue
        orbit = {
            tuple(sorted(action[index] for index in raw)) for action in actions
        }
        seen.update(orbit)
        representatives.append(
            tuple(local_axes[index] for index in min(orbit))
        )
        orbit_histogram[len(orbit)] += 1
    require(len(seen) == comb(20, LOCAL_QF_DIMENSION), (support, len(seen)))
    return (
        tuple(local_axes),
        tuple(representatives),
        len(actions),
        dict(sorted(orbit_histogram.items())),
    )


def fixed_base(name_suffix: str):
    alpha2 = load_module(ALPHA2_SCRIPT, f"n6052_alpha2_{name_suffix}")
    t15 = load_module(T15_SCRIPT, f"n6052_t15_{name_suffix}")
    base = t15.load_base_module()
    quotient = base.load_quotient_module()
    blocks, occurrences = base.cubic_weight_blocks(quotient)
    supports, orbit_sizes = alpha2.one_rectangle_support_orbits()
    return alpha2, quotient, blocks, occurrences, supports, orbit_sizes


def fixed_input(name_suffix: str):
    alpha2, quotient, blocks, occurrences, supports, orbit_sizes = fixed_base(
        name_suffix
    )
    rows = []
    global_index = 0
    for support_index, support in enumerate(supports):
        local_axes, representatives, action_count, orbit_histogram = (
            support_orbit_representatives(alpha2, quotient, support)
        )
        rows.append(
            {
                "support_index": support_index,
                "support": tuple(support),
                "marked_support_count": orbit_sizes[support],
                "local_axes": local_axes,
                "representatives": representatives,
                "automorphism_action_count": action_count,
                "quotient_orbit_size_histogram": orbit_histogram,
                "global_index_start": global_index,
            }
        )
        global_index += len(representatives)
    require(global_index == 173_388, global_index)
    return quotient, blocks, occurrences, rows


def evaluate_support_shape(
    support_index: int,
    support,
    marked_support_count: int,
    alpha2,
    quotient,
    blocks,
    occurrences,
) -> dict[str, object]:
    local_axes, representatives, action_count, orbit_histogram = (
        support_orbit_representatives(alpha2, quotient, support)
    )
    maximum = -1
    sample = None
    checked = 0
    for local_index, qf_axes in enumerate(representatives):
        qf_set = set(qf_axes)
        masks: dict[int, int] = {}
        base_dimension = PERMANENT_CUBIC_DIMENSION
        for axis in qf_axes:
            for block_index, bit in occurrences[axis]:
                masks[block_index] = masks.get(block_index, 0) | bit
        for block_index, mask in masks.items():
            block = blocks[block_index]
            base_dimension += block.nullity(mask) - block.base_nullity

        best_gain = -1
        best_axis = None
        for axis in range(AXIS_COUNT):
            if axis in qf_set:
                continue
            gain = sum(
                blocks[block_index].nullity(masks.get(block_index, 0) | bit)
                - blocks[block_index].nullity(masks.get(block_index, 0))
                for block_index, bit in occurrences[axis]
            )
            if gain > best_gain:
                best_gain = gain
                best_axis = axis
        require(best_axis is not None, qf_axes)
        value = base_dimension + best_gain
        candidate = {
            "support_index": support_index,
            "support": [list(edge) for edge in support],
            "qF_axes": [
                list(quotient.QUOTIENT_AXES[axis]) for axis in qf_axes
            ],
            "extra_axis": list(quotient.QUOTIENT_AXES[best_axis]),
            "base_prolongation_dimension": base_dimension,
            "extra_axis_increment": best_gain,
            "local_representative_index": local_index,
        }
        if sample is None or (value, -local_index) > (
            maximum,
            -int(sample["local_representative_index"]),
        ):
            maximum = value
            sample = candidate
        checked += 1
    require(sample is not None, support_index)
    return {
        "support_index": support_index,
        "support": tuple(support),
        "marked_support_count": marked_support_count,
        "local_axes": local_axes,
        "automorphism_action_count": action_count,
        "quotient_orbit_size_histogram": orbit_histogram,
        "checked_representatives": checked,
        "maximum": maximum,
        "sample": sample,
    }


def initialize_shape_worker() -> None:
    global _SHAPE_CONTEXT
    _SHAPE_CONTEXT = fixed_base(f"worker_{mp.current_process().pid}")


def shape_worker(support_index: int) -> dict[str, object]:
    require(_SHAPE_CONTEXT is not None, "shape worker context")
    alpha2, quotient, blocks, occurrences, supports, orbit_sizes = _SHAPE_CONTEXT
    support = supports[support_index]
    return evaluate_support_shape(
        support_index,
        support,
        orbit_sizes[support],
        alpha2,
        quotient,
        blocks,
        occurrences,
    )


def globalize_support_rows(
    rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Restore the historical global index after shape-local evaluation."""

    ordered = sorted(rows, key=lambda row: int(row["support_index"]))
    require(
        [int(row["support_index"]) for row in ordered] == list(range(len(rows))),
        ordered,
    )
    result = []
    global_index = 0
    for raw in ordered:
        row = dict(raw)
        sample = dict(raw["sample"])
        local_index = int(sample.pop("local_representative_index"))
        checked = int(raw["checked_representatives"])
        require(0 <= local_index < checked, (local_index, checked))
        sample["global_representative_index"] = global_index + local_index
        row["sample"] = sample
        row["global_index_start"] = global_index
        result.append(row)
        global_index += checked
    return result


def compute_support_rows(worker_count: int) -> list[dict[str, object]]:
    require(1 <= worker_count <= 12, worker_count)
    if worker_count == 1:
        alpha2, quotient, blocks, occurrences, supports, orbit_sizes = fixed_base(
            "serial_shapes"
        )
        rows = [
            evaluate_support_shape(
                index,
                support,
                orbit_sizes[support],
                alpha2,
                quotient,
                blocks,
                occurrences,
            )
            for index, support in enumerate(supports)
        ]
    else:
        context = mp.get_context("spawn")
        with context.Pool(
            min(worker_count, 12),
            initializer=initialize_shape_worker,
        ) as pool:
            rows = pool.map(shape_worker, range(12))
    rows = globalize_support_rows(rows)
    global_index = sum(int(row["checked_representatives"]) for row in rows)
    require(global_index == 173_388, global_index)
    require(
        tuple(int(row["checked_representatives"]) for row in rows)
        == EXPECTED_REPRESENTATIVE_COUNTS,
        rows,
    )
    return rows


def compute_cap(worker_count: int) -> dict[str, object]:
    support_rows = compute_support_rows(worker_count)

    result_rows = []
    for support_index, support_row in enumerate(support_rows):
        result_rows.append(
            {
                "support_index": support_index,
                "support": [list(edge) for edge in support_row["support"]],
                "marked_support_count": int(support_row["marked_support_count"]),
                "local_quotient_axis_count": 20,
                "raw_local_qF_count": comb(20, LOCAL_QF_DIMENSION),
                "automorphism_action_count": int(
                    support_row["automorphism_action_count"]
                ),
                "qF_orbit_representative_count": int(
                    support_row["checked_representatives"]
                ),
                "qF_orbit_size_histogram": {
                    str(key): value
                    for key, value in support_row[
                        "quotient_orbit_size_histogram"
                    ].items()
                },
                "prolongation_upper_cap": int(support_row["maximum"]),
                "sample_maximizer": support_row["sample"],
            }
        )

    require(
        [row["qF_orbit_representative_count"] for row in result_rows]
        == list(EXPECTED_REPRESENTATIVE_COUNTS),
        result_rows,
    )
    maximum = max(int(row["prolongation_upper_cap"]) for row in result_rows)
    require(maximum == 458, maximum)
    return {
        "support_rows": result_rows,
        "one_rectangle_prolongation_upper_cap_t15": maximum,
    }


def state_pruning() -> dict[str, object]:
    payload = json.loads(T15_DATA.read_text(encoding="utf-8"))
    survivor_ids = payload["state_pruning"]["remaining_state_ids"]
    profiles = payload["state_pruning"]["remaining_epsilon_alpha_pairs"]
    excluded = []
    remaining = []
    for state_id, pairs in zip(survivor_ids, profiles, strict=True):
        if [0, 2] in pairs:
            excluded.append(state_id)
        else:
            remaining.append(state_id)
    require(
        len(excluded) == 6
        and remaining == ["b60_state_366"]
        and profiles[-1] == [[0, 3]] * 6,
        (excluded, remaining, profiles),
    )
    return {
        "input_state_count": len(survivor_ids),
        "excluded_by_alpha2_t15_cap_count": len(excluded),
        "excluded_state_ids": excluded,
        "remaining_state_count": len(remaining),
        "remaining_state_ids": remaining,
        "remaining_profile": [[0, 3]] * 6,
    }


def build_payload(computation: dict[str, object]) -> dict[str, object]:
    n6051 = json.loads(T15_DATA.read_text(encoding="utf-8"))
    three_rectangle_cap = int(
        n6051["characteristic_zero_prolongation_upper_cap_t15"]
    )
    require(three_rectangle_cap == 458, three_rectangle_cap)
    one_rectangle_cap = int(
        computation["one_rectangle_prolongation_upper_cap_t15"]
    )
    require(one_rectangle_cap == 458, one_rectangle_cap)
    return {
        "status": "N6_052_ALPHA2_T15_PROLONGATION_CAP",
        "arithmetic": (
            "exact ranks modulo 1000003; modular nullities are rigorous "
            "characteristic-zero upper bounds"
        ),
        "prime": PRIME,
        "one_rectangle_support_orbit_count": 12,
        "raw_local_qF_count_per_support_orbit": comb(20, 14),
        "raw_support_orbit_qF_configuration_count": 12 * comb(20, 14),
        "qF_orbit_representative_count_across_shapes": 173_388,
        "ambient_extra_axis_choices_per_qF": AXIS_COUNT - LOCAL_QF_DIMENSION,
        "reduced_qF_extra_axis_evaluations": 173_388
        * (AXIS_COUNT - LOCAL_QF_DIMENSION),
        "one_rectangle_support_rows": computation["support_rows"],
        "one_rectangle_prolongation_upper_cap_t15": one_rectangle_cap,
        "three_rectangle_prolongation_upper_cap_t15_from_N6_051": (
            three_rectangle_cap
        ),
        "universal_alpha2_t15_prolongation_upper_cap": max(
            one_rectangle_cap, three_rectangle_cap
        ),
        "state_pruning": state_pruning(),
        "strict_conclusion": (
            "Every actual alpha-two term inside a global t=15 quadratic "
            "space gives prolongation dimension at most 458. The six remaining "
            "N6-051 states containing alpha two are impossible; only the "
            "all-alpha-three state b60_state_366 remains."
        ),
        "claim_boundary": (
            "The theorem does not exclude the all-alpha-three state, exclude "
            "the b=60 layer, prove ChowRank(perm_6)>=27, or make a border-rank "
            "claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workers",
        type=parse_worker_argument,
        default=0,
        metavar="N|auto",
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    workers = resolve_worker_count(
        args.workers,
        max_workers=12,
        estimated_bytes_per_worker=GIB,
    )
    computation = compute_cap(workers)
    payload = build_payload(computation)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print(f"workers={workers}")
    print(f"worker_mode={'auto' if args.workers == 0 else 'explicit'}")
    print(f"alpha2_t15_cap={payload['universal_alpha2_t15_prolongation_upper_cap']}")
    print(f"remaining_states={payload['state_pruning']['remaining_state_count']}")
    print("N6_ALPHA2_T15_PROLONGATION_CAP_PASS")
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
