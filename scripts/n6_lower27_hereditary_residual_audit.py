#!/usr/bin/env python3
"""Exact finite audit for the N6-032 hereditary-residual reduction.

The proof is mathematical.  This replay checks the small single-term profile
interface, the two Bukh-shadow endpoints used to eliminate maximum ranks 17
and 18, and the thirteen fixed-six central layers used to force the residual
middle rank at least 384.  Arithmetic is exact over the integers/rationals.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
LOWER26_SCRIPT = ROOT / "scripts" / "n6_lower26_average_subset_audit.py"
RANK_GAP_SCRIPT = ROOT / "scripts" / "n6_single_term_middle_rank_gap.py"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LOWER26 = load_module("n6_lower26_average", LOWER26_SCRIPT)
RANK_GAP = load_module("n6_single_term_rank_gap", RANK_GAP_SCRIPT)


def build_payload() -> dict[str, object]:
    rank_gap = RANK_GAP.build_payload()
    if rank_gap["excluded_middle_rank"] != 19:
        raise AssertionError(rank_gap)

    span_five = rank_gap["factor_span_five_support_profiles"]
    if span_five != {"1": 14, "2": 14, "3": 18, "4": 20, "5": 20}:
        raise AssertionError(span_five)

    low_maximum_rank_branches = [
        {
            "maximum_individual_middle_rank": 17,
            "selected_six_middle_rank_lower": 92,
            "central_intersection_lower": 46,
            "individual_quadratic_rank_cap": 11,
            "fixed_six_quadratic_projection_cap": 58,
            "shadow_lower": int(
                LOWER26.exact_shadow_certificate(46)[
                    "integer_shadow_lower_bound"
                ]
            ),
        },
        {
            "maximum_individual_middle_rank": 18,
            "selected_six_middle_rank_lower": 88,
            "global_extra_span_upper": 34,
            "central_intersection_lower": 54,
            "individual_quadratic_rank_cap": 13,
            "fixed_six_quadratic_projection_cap": 68,
            "shadow_lower": int(
                LOWER26.exact_shadow_certificate(54)[
                    "integer_shadow_lower_bound"
                ]
            ),
        },
    ]
    for branch in low_maximum_rank_branches:
        if branch["shadow_lower"] <= branch["fixed_six_quadratic_projection_cap"]:
            raise AssertionError(branch)

    high_layers: list[dict[str, int]] = []
    for intersection in range(52, 65):
        layer = LOWER26.central_layer(intersection)
        central_lower = int(layer["central_rank_lower_bound"])
        required = 2 * intersection - 16
        if central_lower < required:
            raise AssertionError((intersection, central_lower, required))
        high_layers.append(
            {
                "b": intersection,
                "shadow_lower": int(layer["shadow_lower_bound"]),
                "central_rank_lower": central_lower,
                "required_for_residual_384": required,
                "margin": central_lower - required,
            }
        )

    cutoff = LOWER26.exact_shadow_certificate(65)
    if cutoff["integer_shadow_lower_bound"] != 79:
        raise AssertionError(cutoff)

    hereditary = [
        {
            "subset_size": size,
            "middle_rank_lower": 20 * size - 16,
            "shorter_expression_cap": 20 * (size - 1),
            "strict_margin": 4,
        }
        for size in range(1, 21)
    ]

    return {
        "status": "EXACT_N6_LOWER27_HEREDITARY_RESIDUAL_REDUCTION",
        "arithmetic": "exact integers and Fraction over Q",
        "hypothetical_total_terms": 26,
        "maximum_individual_middle_rank_forced": 20,
        "rank_19_excluded_by": "N6-031",
        "low_maximum_rank_branches": low_maximum_rank_branches,
        "conditional_six_subset_middle_lower": "ceil(96-tau/5)",
        "selected_six_intersection_cut": {
            "low_branch": "b<=51 uses h>=120-2b/3>=2b-16",
            "high_branch": "b>=52 uses the exact fixed-six layer table",
            "first_shadow_excluded_b": 65,
            "shadow_at_65": int(cutoff["integer_shadow_lower_bound"]),
            "quadratic_projection_cap": 78,
        },
        "fixed_six_high_layer_table": high_layers,
        "twenty_term_residual_middle_rank_lower": 384,
        "twenty_term_residual_exact_chow_rank": 20,
        "hereditary_subset_middle_rank_bounds": hereditary,
        "hereditary_consequence": (
            "Every nonempty subset of the displayed twenty residual terms is "
            "a minimum Chow decomposition certified by its own middle "
            "catalecticant; every such central relation-pairing radical has "
            "dimension at most 9."
        ),
        "minimum_number_of_full_middle_rank_residual_terms": 12,
        "claim_boundary": (
            "This is a necessary consequence of a hypothetical 26-term "
            "decomposition. It does not exclude that decomposition and does "
            "not prove ChowRank(perm_6)>=27."
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
    print("N6_LOWER27_HEREDITARY_RESIDUAL_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
