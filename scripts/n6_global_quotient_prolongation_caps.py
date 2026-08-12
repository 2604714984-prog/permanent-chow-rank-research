#!/usr/bin/env python3
"""Exact torus-fixed prolongation caps for N6-047.

For a coordinate K_(2,3) extremal plane this script enumerates, modulo its
S_2 x S_3 stabilizer, every twelve-axis quotient W=q(F) of a torus-fixed
fifteen-plane F containing the rectangle net.  It then allows zero, one, or
two arbitrary ambient quotient axes, corresponding to t=12,13,14.

The cubic equations split into 3136 row/column weight blocks.  Ranks are
computed exactly modulo the prime 1,000,003.  Modular rank is a lower bound
for characteristic-zero rank, so the resulting nullities are rigorous
characteristic-zero upper bounds.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUOTIENT_SCRIPT = ROOT / "scripts" / "n6_b64_frame_component_specialization.py"
STATE_DATA = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"
PRIME = 1_000_003
N = 6
VARIABLES = 36
LOCAL_EDGES = (0, 1, 2, 6, 7, 8)


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_quotient_module():
    spec = importlib.util.spec_from_file_location("n6_q_axes", QUOTIENT_SCRIPT)
    require(spec is not None and spec.loader is not None, QUOTIENT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rank_mod(matrix: list[list[int]], width: int) -> int:
    work = [[value % PRIME for value in row] for row in matrix if any(row)]
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], PRIME - 2, PRIME)
        for index in range(column, width):
            work[rank][index] = work[rank][index] * inverse % PRIME
        for row in range(rank + 1, len(work)):
            multiplier = work[row][column]
            if not multiplier:
                continue
            for index in range(column, width):
                work[row][index] = (
                    work[row][index] - multiplier * work[rank][index]
                ) % PRIME
        rank += 1
        if rank == len(work):
            break
    return rank


class CubicBlock:
    def __init__(
        self,
        column_count: int,
        rows: list[list[int]],
        row_axes: list[int],
    ) -> None:
        self.column_count = column_count
        self.rows = rows
        self.row_axes = row_axes
        self.axes = sorted(set(row_axes))
        self.axis_position = {axis: index for index, axis in enumerate(self.axes)}
        self.base_nullity = column_count - rank_mod(rows, column_count)
        self.cache = {0: self.base_nullity}

    def nullity(self, selected_mask: int) -> int:
        if selected_mask not in self.cache:
            retained = [
                row
                for row, axis in zip(self.rows, self.row_axes)
                if not selected_mask >> self.axis_position[axis] & 1
            ]
            self.cache[selected_mask] = self.column_count - rank_mod(
                retained, self.column_count
            )
        return self.cache[selected_mask]


def cubic_weight_blocks(quotient):
    monomial_groups: dict[
        tuple[tuple[int, ...], tuple[int, ...]],
        list[tuple[int, int, int]],
    ] = defaultdict(list)
    for monomial in combinations_with_replacement(range(VARIABLES), 3):
        cells = [divmod(variable, N) for variable in monomial]
        key = (
            tuple(sorted(row for row, _ in cells)),
            tuple(sorted(column for _, column in cells)),
        )
        monomial_groups[key].append(monomial)

    blocks: list[CubicBlock] = []
    axis_occurrences: list[list[tuple[int, int]]] = [
        [] for _ in quotient.QUOTIENT_AXES
    ]
    for monomials in monomial_groups.values():
        rows: list[list[int]] = []
        row_axes: list[int] = []
        for direction in range(VARIABLES):
            row = [0] * len(monomials)
            axis_index = None
            for column, monomial in enumerate(monomials):
                multiplicity = monomial.count(direction)
                if not multiplicity:
                    continue
                remaining = list(monomial)
                remaining.remove(direction)
                axis, sign = quotient.quotient_axis(*remaining)
                current_axis = quotient.AXIS_INDEX[axis]
                if axis_index is None:
                    axis_index = current_axis
                require(axis_index == current_axis, (monomial, direction))
                row[column] = multiplicity * sign
            if axis_index is not None:
                rows.append(row)
                row_axes.append(axis_index)
        block_index = len(blocks)
        block = CubicBlock(len(monomials), rows, row_axes)
        blocks.append(block)
        for axis in block.axes:
            bit = 1 << block.axis_position[axis]
            axis_occurrences[axis].append((block_index, bit))

    require(len(blocks) == 3_136, len(blocks))
    require(sum(block.base_nullity for block in blocks) == 400, "E3 baseline")
    require(
        all(len(occurrences) == 36 for occurrences in axis_occurrences),
        "each quadratic quotient axis has 36 cubic extensions",
    )
    return blocks, axis_occurrences


def local_axes_and_orbits(quotient):
    local_axes: list[int] = []
    representatives: dict[int, tuple[int, int]] = {}
    for left, right in combinations_with_replacement(LOCAL_EDGES, 2):
        axis = quotient.AXIS_INDEX[quotient.quotient_axis(left, right)[0]]
        if axis not in local_axes:
            local_axes.append(axis)
            representatives[axis] = (left, right)
    require(len(local_axes) == 18, local_axes)

    actions: list[dict[int, int]] = []
    for row_permutation in ((0, 1), (1, 0)):
        for column_permutation in permutations((0, 1, 2)):
            variable_image = list(range(VARIABLES))
            for row in (0, 1):
                for column in (0, 1, 2):
                    variable_image[row * N + column] = (
                        row_permutation[row] * N + column_permutation[column]
                    )
            actions.append(
                {
                    axis: quotient.AXIS_INDEX[
                        quotient.quotient_axis(
                            variable_image[pair[0]], variable_image[pair[1]]
                        )[0]
                    ]
                    for axis, pair in representatives.items()
                }
            )

    seen: set[tuple[int, ...]] = set()
    orbit_representatives: list[tuple[int, ...]] = []
    orbit_size_histogram: Counter[int] = Counter()
    for raw in combinations(local_axes, 12):
        candidate = tuple(sorted(raw))
        if candidate in seen:
            continue
        orbit = {
            tuple(sorted(action[axis] for axis in candidate)) for action in actions
        }
        seen.update(orbit)
        orbit_representatives.append(min(orbit))
        orbit_size_histogram[len(orbit)] += 1

    require(len(seen) == 18_564, len(seen))
    require(len(orbit_representatives) == 1_683, len(orbit_representatives))
    require(
        orbit_size_histogram == {1: 3, 2: 6, 3: 17, 6: 231, 12: 1426},
        orbit_size_histogram,
    )
    return local_axes, orbit_representatives, orbit_size_histogram


def cap_audit() -> dict[str, object]:
    quotient = load_quotient_module()
    require(len(quotient.QUOTIENT_AXES) == 441, len(quotient.QUOTIENT_AXES))
    blocks, occurrences = cubic_weight_blocks(quotient)
    local_axes, orbit_representatives, orbit_histogram = local_axes_and_orbits(
        quotient
    )
    occurrence_maps = [dict(rows) for rows in occurrences]

    interacting_pairs: list[tuple[int, int, tuple[int, ...]]] = []
    disjoint_pairs: list[tuple[int, int]] = []
    shared_block_histogram: Counter[int] = Counter()
    for first, second in combinations(range(441), 2):
        shared = tuple(
            sorted(set(occurrence_maps[first]) & set(occurrence_maps[second]))
        )
        shared_block_histogram[len(shared)] += 1
        if shared:
            interacting_pairs.append((first, second, shared))
        else:
            disjoint_pairs.append((first, second))
    require(
        shared_block_histogram == {0: 77_040, 1: 16_200, 6: 3_780},
        shared_block_histogram,
    )

    maxima = {12: 0, 13: 0, 14: 0}
    maximizers: dict[int, list[dict[str, object]]] = {12: [], 13: [], 14: []}

    def record(t_value: int, value: int, row: dict[str, object]) -> None:
        if value > maxima[t_value]:
            maxima[t_value] = value
            maximizers[t_value] = [row]
        elif value == maxima[t_value]:
            maximizers[t_value].append(row)

    for w_axes in orbit_representatives:
        w_set = set(w_axes)
        masks: dict[int, int] = {}
        base_dimension = 400
        for axis in w_axes:
            for block_index, bit in occurrences[axis]:
                masks[block_index] = masks.get(block_index, 0) | bit
        for block_index, mask in masks.items():
            block = blocks[block_index]
            base_dimension += block.nullity(mask) - block.base_nullity

        record(
            12,
            base_dimension,
            {"W_axes": list(w_axes), "extra_axes": []},
        )

        gains = [-1] * 441
        for axis in range(441):
            if axis in w_set:
                continue
            gain = 0
            for block_index, bit in occurrences[axis]:
                block = blocks[block_index]
                old_mask = masks.get(block_index, 0)
                gain += block.nullity(old_mask | bit) - block.nullity(old_mask)
            gains[axis] = gain
            record(
                13,
                base_dimension + gain,
                {"W_axes": list(w_axes), "extra_axes": [axis]},
            )

        # If two axes occur in disjoint cubic-weight blocks, their gains add.
        # Sorting permits an exact branch-and-bound search for the best such
        # pair: once the sum of the current gain and the next gain cannot beat
        # the incumbent, no later pair can do so.
        ordered = sorted(
            ((gain, axis) for axis, gain in enumerate(gains) if gain >= 0),
            reverse=True,
        )
        best_disjoint = -1
        best_disjoint_pair = None
        for first_index, (first_gain, first) in enumerate(ordered):
            if (
                first_index + 1 >= len(ordered)
                or first_gain + ordered[first_index + 1][0] <= best_disjoint
            ):
                break
            for second_gain, second in ordered[first_index + 1 :]:
                if first_gain + second_gain <= best_disjoint:
                    break
                if not (
                    set(occurrence_maps[first]) & set(occurrence_maps[second])
                ):
                    best_disjoint = first_gain + second_gain
                    best_disjoint_pair = (first, second)
        require(best_disjoint_pair is not None, w_axes)
        record(
            14,
            base_dimension + best_disjoint,
            {
                "W_axes": list(w_axes),
                "extra_axes": list(best_disjoint_pair),
            },
        )

        # Every remaining pair shares one or six cubic-weight blocks.  The
        # displayed correction is the exact failure of gain additivity.
        for first, second, shared_blocks in interacting_pairs:
            if first in w_set or second in w_set:
                continue
            correction = 0
            for block_index in shared_blocks:
                block = blocks[block_index]
                old_mask = masks.get(block_index, 0)
                first_bit = occurrence_maps[first][block_index]
                second_bit = occurrence_maps[second][block_index]
                correction += (
                    block.nullity(old_mask | first_bit | second_bit)
                    - block.nullity(old_mask | first_bit)
                    - block.nullity(old_mask | second_bit)
                    + block.nullity(old_mask)
                )
            record(
                14,
                base_dimension + gains[first] + gains[second] + correction,
                {"W_axes": list(w_axes), "extra_axes": [first, second]},
            )

    require(maxima == {12: 436, 13: 440, 14: 448}, maxima)
    return {
        "prime": PRIME,
        "quadratic_quotient_dimension": 441,
        "local_quotient_axis_count": len(local_axes),
        "fixed_W_count": 18_564,
        "fixed_W_orbit_representative_count": len(orbit_representatives),
        "fixed_W_orbit_size_histogram": {
            str(key): orbit_histogram[key] for key in sorted(orbit_histogram)
        },
        "ambient_axis_pair_shared_cubic_block_histogram": {
            str(key): shared_block_histogram[key]
            for key in sorted(shared_block_histogram)
        },
        "characteristic_zero_prolongation_upper_caps": {
            str(key): maxima[key] for key in sorted(maxima)
        },
        "maximizer_representation_counts": {
            str(key): len(maximizers[key]) for key in sorted(maximizers)
        },
        "sample_maximizers": {
            str(key): {
                "W_axes": [
                    list(quotient.QUOTIENT_AXES[axis])
                    for axis in maximizers[key][0]["W_axes"]
                ],
                "extra_axes": [
                    list(quotient.QUOTIENT_AXES[axis])
                    for axis in maximizers[key][0]["extra_axes"]
                ],
            }
            for key in sorted(maximizers)
        },
    }


def state_exclusions(caps: dict[str, int]) -> list[dict[str, object]]:
    payload = json.loads(STATE_DATA.read_text(encoding="utf-8"))
    rows = []
    expected = {61: (73, 61, 12), 62: (11, 10, 1), 63: (11, 10, 1)}
    for layer in payload["layers"]:
        b_value = layer["middle_intersection_b"]
        excluded_ids: list[str] = []
        remaining: list[dict[str, object]] = []
        for index, state in enumerate(layer["states"]):
            state_id = f"b{b_value}_state_{index:03d}"
            t_value = state["fixed_quadratic_quotient_t2"]
            required = (
                400 + state["fixed_middle_rank_h"] - b_value
            )
            if state["extremal_rectangle_term_count"]:
                require(t_value in (12, 13, 14), (state_id, t_value))
                require(required > caps[str(t_value)], (state_id, required))
                excluded_ids.append(state_id)
            else:
                remaining.append(
                    {
                        "state_id": state_id,
                        "epsilon_alpha_pairs": state["epsilon_alpha_pairs"],
                        "t2": t_value,
                        "h": state["fixed_middle_rank_h"],
                    }
                )
        observed = (len(layer["states"]), len(excluded_ids), len(remaining))
        require(observed == expected[b_value], (b_value, observed))
        rows.append(
            {
                "b": b_value,
                "canonical_state_count": len(layer["states"]),
                "excluded_state_count": len(excluded_ids),
                "excluded_state_ids": excluded_ids,
                "remaining_state_count": len(remaining),
                "remaining_states": remaining,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    cap_data = cap_audit()
    caps = cap_data["characteristic_zero_prolongation_upper_caps"]
    return {
        "status": "N6_047_GLOBAL_QUOTIENT_PROLONGATION_CAPS",
        "arithmetic": (
            "complete torus-fixed enumeration and exact modular ranks; modular "
            "nullities are characteristic-zero upper bounds"
        ),
        "fixed_point_cap_audit": cap_data,
        "state_exclusions": state_exclusions(caps),
        "strict_conclusion": (
            "Every b=61,62,63 canonical state containing at least one extremal "
            "rectangle term is impossible. The remaining counts are 12,1,1."
        ),
        "claim_boundary": (
            "The theorem does not exclude the fourteen states with no extremal "
            "rectangle term and does not yet prove ChowRank(perm_6)>=27."
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
    print("N6_GLOBAL_QUOTIENT_PROLONGATION_CAPS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
