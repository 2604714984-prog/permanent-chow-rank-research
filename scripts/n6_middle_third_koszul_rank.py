#!/usr/bin/env python3
"""Exact middle third-Koszul rank and its forty homology cycles."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_all_koszul_young_ceiling.py"
PRIME = 1_000_003
MODULAR_RANK = 2_715_505


def load_base_module():
    spec = spec_from_file_location("n6_all_koszul_young_ceiling", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE_SCRIPT)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_module()


def representative_columns():
    """The 120 columns in the row-heavy representative weight."""

    heavy_rows = (0, 1, 2)
    for derivative_columns in combinations(range(6), 3):
        complement = tuple(
            column
            for column in range(6)
            if column not in derivative_columns
        )
        for matched_columns in permutations(complement):
            wedge = tuple(
                sorted(
                    6 * row + column
                    for row, column in zip(
                        heavy_rows,
                        matched_columns,
                        strict=True,
                    )
                )
            )
            values = {}
            for row in heavy_rows:
                for column in derivative_columns:
                    variable = 6 * row + column
                    output_rows = tuple(
                        entry for entry in heavy_rows if entry != row
                    )
                    output_columns = tuple(
                        entry
                        for entry in derivative_columns
                        if entry != column
                    )
                    output_wedge = tuple(sorted((variable,) + wedge))
                    key = (output_rows, output_columns, output_wedge)
                    values[key] = values.get(key, 0) + BASE.insertion_sign(
                        variable,
                        wedge,
                    )
            yield values


def exact_representative_audit() -> dict[str, int]:
    columns = list(representative_columns())
    summed = {}
    for column in columns:
        for row, value in column.items():
            summed[row] = summed.get(row, 0) + value
    nonzero_sum_entries = sum(value != 0 for value in summed.values())
    rank = BASE.sparse_rank_fraction(columns)
    return {
        "column_count": len(columns),
        "row_support_count": len(summed),
        "all_ones_cycle_nonzero_entries": nonzero_sum_entries,
        "exact_rational_rank": rank,
        "exact_nullity": len(columns) - rank,
    }


def build_payload(replay_heavy: bool) -> dict[str, object]:
    representative = exact_representative_audit()
    expected_representative = {
        "column_count": 120,
        "row_support_count": 540,
        "all_ones_cycle_nonzero_entries": 0,
        "exact_rational_rank": 119,
        "exact_nullity": 1,
    }
    if representative != expected_representative:
        raise AssertionError(representative)

    domain_dimension = comb(6, 3) ** 2 * comb(36, 3)
    preceding_rank = 140_455
    homology_lower = 2 * comb(6, 3)
    rank_upper = domain_dimension - preceding_rank - homology_lower
    if rank_upper != MODULAR_RANK:
        raise AssertionError(rank_upper)

    heavy = None
    if replay_heavy:
        heavy = BASE.permanent_rank(3, 3)
        expected_heavy = {
            "domain_dimension": 2_856_000,
            "weight_block_count": 119_961,
            "maximum_block_column_count": 2_400,
            "modular_rank": MODULAR_RANK,
            "histogram_entries": 22,
        }
        if heavy != expected_heavy:
            raise AssertionError(heavy)

    internal = BASE.internal_rank_table()
    term_rank = BASE.ambient_term_rank(3, 3, internal)
    if term_rank != 133_545:
        raise AssertionError(term_rank)
    twenty_term_cap = 20 * term_rank
    margin = MODULAR_RANK - twenty_term_cap
    if margin != 44_605:
        raise AssertionError(margin)

    return {
        "status": "N6_MIDDLE_THIRD_KOSZUL_RANK_REPLAYED",
        "prime": PRIME,
        "representative_weight": {
            "row_weight": [2, 2, 2, 0, 0, 0],
            "column_weight": [1, 1, 1, 1, 1, 1],
        },
        "representative_exact_audit": representative,
        "row_heavy_weight_count": comb(6, 3),
        "transpose_weight_count": comb(6, 3),
        "explicit_homology_dimension_lower": homology_lower,
        "domain_dimension": domain_dimension,
        "preceding_image_exact_rank": preceding_rank,
        "characteristic_zero_rank_upper": rank_upper,
        "modular_rank_lower": MODULAR_RANK,
        "characteristic_zero_exact_rank": MODULAR_RANK,
        "single_chow_term_exact_rank": term_rank,
        "twenty_term_rank_cap": twenty_term_cap,
        "margin_above_twenty_term_cap": margin,
        "hypothetical_six_term_two_sided_overlap_defect_lower": margin,
        "heavy_replay_performed": replay_heavy,
        "heavy_replay": heavy,
        "theorem": (
            "The middle third-Koszul map of perm_6 has exact "
            "characteristic-zero rank 2715505 and forty-dimensional "
            "Koszul homology in this strand."
        ),
        "claim_boundary": (
            "The exact permanent rank exceeds twenty one-term caps by 44605. "
            "A hypothetical six-term complement must absorb this as a "
            "two-sided row/column overlap defect. No upper bound excluding "
            "that defect is proved, so this is not a lower-27 theorem."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-heavy", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.replay_heavy)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_MIDDLE_THIRD_KOSZUL_RANK_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
