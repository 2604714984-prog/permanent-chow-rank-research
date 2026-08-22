#!/usr/bin/env python3
"""Exact subpacket ranks for the canonical two-transposition Packet-B joins."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
JOIN_PATH = HERE / "n7_b2_two_transposition_join_obstruction.py"
SPEC = importlib.util.spec_from_file_location(
    "n7_b2_two_transposition_join_obstruction", JOIN_PATH
)
join = importlib.util.module_from_spec(SPEC)
if SPEC.loader is None:
    raise RuntimeError("failed to load the two-transposition join module")
SPEC.loader.exec_module(join)


JOIN_TYPES = {
    "shared_row_01_02": ((0, 1), (0, 2)),
    "disjoint_01_23": ((0, 1), (2, 3)),
}


def canonical_terms(
    pairs: tuple[tuple[int, int], tuple[int, int]],
) -> list[list[tuple[sp.Rational, ...]]]:
    terms = join.pair_slice_terms(pairs[0], (7, 8), sp.Rational(1, 2))
    terms += join.pair_slice_terms(pairs[1], (9, 10), sp.Rational(1, 2))
    if len(terms) != 4:
        raise ArithmeticError("the canonical join must contain four terms")
    return terms


def subset_row(
    local_maps: list[tuple[sp.Matrix, sp.Matrix]],
    subset: tuple[int, ...],
) -> dict[str, object]:
    if not subset:
        raise ValueError("the subset must be nonempty")
    global_b = sp.Matrix.hstack(*(local_maps[index][0] for index in subset))
    global_c = sp.Matrix.vstack(*(local_maps[index][1] for index in subset))
    flint_b = join.flint_matrix(global_b)
    flint_c = join.flint_matrix(global_c)
    rank_b = flint_b.rank()
    rank_c = flint_c.rank()
    rank_bc = (flint_b * flint_c).rank()
    middle_dimension = global_b.cols
    defect = middle_dimension - rank_b - rank_c + rank_bc
    if defect < 0:
        raise ArithmeticError("negative subpacket obstruction dimension")
    if len(subset) == 1:
        orbit = "singleton"
    elif len(subset) == 2 and subset in ((0, 1), (2, 3)):
        orbit = "within_slice_pair"
    elif len(subset) == 2:
        orbit = "cross_slice_pair"
    elif len(subset) == 3:
        orbit = "triple"
    else:
        orbit = "full_join"
    return {
        "labels": list(subset),
        "subset_size": len(subset),
        "orbit": orbit,
        "middle_dimension": middle_dimension,
        "rank_B": rank_b,
        "rank_C": rank_c,
        "rank_BC": rank_bc,
        "kernel_image_defect": defect,
        "sylvester_equality_holds": defect == 0,
    }


def orbit_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    summary: dict[str, object] = {}
    for orbit in (
        "singleton",
        "within_slice_pair",
        "cross_slice_pair",
        "triple",
        "full_join",
    ):
        orbit_rows = [row for row in rows if row["orbit"] == orbit]
        rank_tuples = sorted(
            {
                (
                    row["middle_dimension"],
                    row["rank_B"],
                    row["rank_C"],
                    row["rank_BC"],
                    row["kernel_image_defect"],
                )
                for row in orbit_rows
            }
        )
        summary[orbit] = {
            "row_count": len(orbit_rows),
            "rank_tuples": [list(values) for values in rank_tuples],
        }
    return summary


def join_profile(
    name: str,
    pairs: tuple[tuple[int, int], tuple[int, int]],
) -> dict[str, object]:
    local_maps = [join.formal_maps(term) for term in canonical_terms(pairs)]
    rows = [
        subset_row(local_maps, subset)
        for size in range(1, 5)
        for subset in itertools.combinations(range(4), size)
    ]
    proper = [row for row in rows if row["subset_size"] < 4]
    full = next(row for row in rows if row["subset_size"] == 4)
    positive_sizes = [
        row["subset_size"] for row in rows if row["kernel_image_defect"] > 0
    ]
    if not positive_sizes:
        raise ArithmeticError("the canonical join unexpectedly has no obstruction")
    return {
        "join_type": name,
        "transpositions": [list(pair) for pair in pairs],
        "proper_subpacket_count": len(proper),
        "all_proper_subpackets_zero_defect": all(
            row["kernel_image_defect"] == 0 for row in proper
        ),
        "minimal_positive_subset_size": min(positive_sizes),
        "full_join_defect": full["kernel_image_defect"],
        "orbit_summary": orbit_summary(rows),
    }


def validate_expected(profiles: dict[str, dict[str, object]]) -> None:
    expected = {
        "shared_row_01_02": {
            "singleton": [[35, 35, 35, 35, 0]],
            "within_slice_pair": [[70, 65, 60, 55, 0]],
            "cross_slice_pair": [[70, 69, 66, 65, 0]],
            "triple": [[105, 95, 85, 75, 0]],
            "full_join": [[140, 111, 94, 75, 10]],
        },
        "disjoint_01_23": {
            "singleton": [[35, 35, 35, 35, 0]],
            "within_slice_pair": [[70, 65, 60, 55, 0]],
            "cross_slice_pair": [[70, 70, 69, 69, 0]],
            "triple": [[105, 98, 88, 81, 0]],
            "full_join": [[140, 114, 95, 81, 12]],
        },
    }
    for name, orbit_expected in expected.items():
        profile = profiles[name]
        summary = profile["orbit_summary"]
        if not profile["all_proper_subpackets_zero_defect"]:
            raise ArithmeticError(("proper subpacket acquired a defect", name))
        if profile["minimal_positive_subset_size"] != 4:
            raise ArithmeticError(("unexpected minimal positive subset size", name))
        for orbit, rank_tuples in orbit_expected.items():
            if summary[orbit]["rank_tuples"] != rank_tuples:
                raise ArithmeticError(
                    ("unexpected exact subpacket ranks", name, orbit, summary[orbit])
                )


def build_payload() -> dict[str, object]:
    profiles = {
        name: join_profile(name, pairs) for name, pairs in JOIN_TYPES.items()
    }
    validate_expected(profiles)
    return {
        "schema_version": 1,
        "status": "CANONICAL_JOINS_HAVE_MINIMAL_FOUR_WAY_OBSTRUCTION",
        "profiles": profiles,
        "candidate_cardinality_checked_before_materialization": {
            "join_types": len(JOIN_TYPES),
            "nonempty_subsets_per_join": 15,
            "exact_subset_rows": 30,
            "middle_columns_per_term": 35,
        },
        "decision": "ALL_PROPER_SUBPACKETS_HAVE_ZERO_DEFECT_BUT_BOTH_FULL_JOINS_HAVE_POSITIVE_DEFECT",
        "claim_boundary": [
            "Every rank is computed exactly over Q after assembling the selected term blocks in one common unprojected eleven-variable space.",
            "All singleton, pair, and triple subpackets of both canonical joins satisfy Sylvester equality.",
            "The first positive obstruction occurs only when all four terms are present: defect ten for the shared-row join and twelve for the disjoint join.",
            "Pairwise and triple synchronization are therefore insufficient to imply four-term synchronization.",
            "This does not classify noncanonical four-term cross-slice couplings or close full Packet B.",
            "No lower-50 or border-rank claim is made.",
        ],
        "next_exact_gate": "Construct a four-way compatibility invariant or classify the zero-defect noncanonical four-term locus; pairwise and triple tests alone cannot close the frontier.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 B2 minimal four-way obstruction JSON mismatch")
        print("PASS n7 B2 minimal four-way obstruction")
        return
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
