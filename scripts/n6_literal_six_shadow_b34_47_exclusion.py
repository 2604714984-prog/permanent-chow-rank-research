#!/usr/bin/env python3
"""Exact integer replay for the N6-060 literal-six shadow exclusion."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHADOW_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"
DEFAULT_JSON = ROOT / "data" / "n6_literal_six_shadow_b34_47_exclusion.json"

PERMANENT_MIDDLE_DIMENSION = 400
RESIDUAL_COMPLEMENT_TERM_COUNT = 15
SINGLE_TERM_MIDDLE_CAP = 20
SIX_TERM_QUADRATIC_PROJECTION_CAP = 78
SHADOW_TEST_DIMENSION = 53


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_shadow_module():
    spec = importlib.util.spec_from_file_location("n6_product_shadow_n6060", SHADOW_SCRIPT)
    require(spec is not None and spec.loader is not None, SHADOW_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_payload() -> dict[str, object]:
    shadow_module = load_shadow_module()
    shadow, minimizer_count, witness, state_count = (
        shadow_module.minimum_ferrers_shadow(SHADOW_TEST_DIMENSION)
    )
    require(shadow == 81, shadow)

    complement_literal_cap = (
        RESIDUAL_COMPLEMENT_TERM_COUNT * SINGLE_TERM_MIDDLE_CAP
    )
    rows = []
    for b in range(34, 48):
        residual_permanent_intersection_lower = PERMANENT_MIDDLE_DIMENSION - b
        literal_six_intersection_lower = (
            residual_permanent_intersection_lower - complement_literal_cap
        )
        excluded = (
            literal_six_intersection_lower >= SHADOW_TEST_DIMENSION
            and shadow > SIX_TERM_QUADRATIC_PROJECTION_CAP
        )
        require(excluded, (b, literal_six_intersection_lower))
        rows.append(
            {
                "b": b,
                "dim_E3_intersect_G3_lower": residual_permanent_intersection_lower,
                "dim_E3_intersect_literal_six_lower": literal_six_intersection_lower,
                "chosen_subspace_dimension": SHADOW_TEST_DIMENSION,
                "exact_product_shadow_lower": shadow,
                "six_term_quadratic_projection_cap": SIX_TERM_QUADRATIC_PROJECTION_CAP,
                "excluded": excluded,
            }
        )

    require(rows[0]["dim_E3_intersect_literal_six_lower"] == 66, rows[0])
    require(rows[-1]["dim_E3_intersect_literal_six_lower"] == 53, rows[-1])

    return {
        "status": [
            "PURE_LINEAR_ALGEBRA_REDUCTION",
            "EXACT_INTEGER_DP_REPLAY",
            "B34_TO_B47_EXCLUDED",
            "LOWER_28_FRONTIER_REDUCED_TO_B50",
            "N6-060",
        ],
        "hypothesis": "the N6-058 fixed-six reduction under a hypothetical 27-term ordinary Chow decomposition of perm_6",
        "permanent_middle_dimension": PERMANENT_MIDDLE_DIMENSION,
        "residual_term_count": 21,
        "literal_six_term_count": 6,
        "literal_complement_term_count": RESIDUAL_COMPLEMENT_TERM_COUNT,
        "single_term_middle_rank_cap": SINGLE_TERM_MIDDLE_CAP,
        "literal_complement_dimension_cap": complement_literal_cap,
        "universal_lower_bound": "dim(E3 intersect L_A) >= 100-b",
        "exact_product_shadow_at_53": {
            "minimum": shadow,
            "minimizer_count": minimizer_count,
            "first_ferrers_witness": list(witness),
            "memoized_dp_state_count": state_count,
        },
        "six_term_quadratic_projection_cap": SIX_TERM_QUADRATIC_PROJECTION_CAP,
        "strict_shadow_excess": shadow - SIX_TERM_QUADRATIC_PROJECTION_CAP,
        "excluded_b_values": list(range(34, 48)),
        "rows": rows,
        "lower_28_frontier_before_N6_060": list(range(34, 47)) + [50],
        "lower_28_frontier_after_N6_060": [50],
        "conclusion": (
            "The literal-six shadow argument excludes every N6-058 residual "
            "layer b=34,...,46; it also gives a new proof at b=47, which had "
            "already been excluded by a prolongation cap."
        ),
        "claim_boundary": (
            "This certificate does not exclude the all-alpha-three b=50 "
            "endpoint, prove ChowRank(perm_6)>=28, determine the exact ordinary "
            "rank, or make a border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_LITERAL_SIX_SHADOW_B34_47_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
