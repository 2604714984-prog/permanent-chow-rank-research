#!/usr/bin/env python3
"""Exact low-layer arithmetic completing the ordinary lower bound 27.

N6-056 excludes fixed-six intersection dimensions 53 through 64.  This
replay exhausts every conservative quadratic-defect profile in the remaining
layers 45 through 52 and proves that its coupled middle-rank lower bound is
strictly larger than the twenty-term residual upper bound ``2*b``.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHADOW_DATA = ROOT / "data" / "n6_product_shadow_b53_64_exclusion.json"
FIXED_TERMS = 6
QUADRATIC_CAP = 15
PROJECTION_CAP = 78


def macaulay_successor_degree_two(value: int) -> int:
    """The exact degree-two Macaulay successor ``value^{<2>}``."""

    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    if not 0 <= remainder < largest:
        raise AssertionError((value, largest, remainder))
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def individual_middle_lower(epsilon: int) -> int | None:
    """Conservative exact single-term profile indexed by ``15-dim F``."""

    quadratic_dimension = QUADRATIC_CAP - epsilon
    if quadratic_dimension == 15:
        return 20
    if quadratic_dimension == 14:
        return 20
    if quadratic_dimension == 13:
        return 18
    if quadratic_dimension == 12:
        return None
    if quadratic_dimension == 11:
        return 14
    if 0 <= quadratic_dimension <= 10:
        return 0
    raise ValueError(epsilon)


def enumerate_layer(b: int, shadow: int) -> dict[str, object]:
    defect_budget = PROJECTION_CAP - shadow
    profiles = []
    impossible = []
    for epsilon in combinations_with_replacement(range(QUADRATIC_CAP + 1), 6):
        omitted_defect = sum(epsilon) - min(epsilon)
        if omitted_defect > defect_budget:
            continue
        individual = [individual_middle_lower(value) for value in epsilon]
        if any(value is None for value in individual):
            impossible.append(list(epsilon))
            continue
        relation_cap = defect_budget - omitted_defect
        cubic_relation_cap = macaulay_successor_degree_two(relation_cap)
        middle_lower = sum(int(value) for value in individual) - 2 * cubic_relation_cap
        profiles.append(
            {
                "epsilon": list(epsilon),
                "individual_middle_rank_lowers": [int(value) for value in individual],
                "quadratic_relation_cap": relation_cap,
                "cubic_relation_cap": cubic_relation_cap,
                "coupled_middle_rank_lower": middle_lower,
            }
        )
    minimum = min(row["coupled_middle_rank_lower"] for row in profiles)
    minimizers = [
        row for row in profiles if row["coupled_middle_rank_lower"] == minimum
    ]
    residual_upper = 2 * b
    if minimum <= residual_upper:
        raise AssertionError((b, minimum, residual_upper, minimizers))
    return {
        "b": b,
        "exact_product_shadow_minimum": shadow,
        "defect_budget": defect_budget,
        "enumerated_symmetric_epsilon_type_count": len(profiles) + len(impossible),
        "feasible_symmetric_epsilon_type_count": len(profiles),
        "impossible_quadratic_rank_twelve_type_count": len(impossible),
        "minimum_coupled_middle_rank_lower": minimum,
        "twenty_term_residual_middle_rank_upper": residual_upper,
        "strict_margin": minimum - residual_upper,
        "minimizers": minimizers,
        "profiles": profiles,
    }


def build_payload() -> dict[str, object]:
    shadow_payload = json.loads(SHADOW_DATA.read_text(encoding="utf-8"))
    if shadow_payload["excluded_middle_dimensions"] != list(range(53, 65)):
        raise AssertionError(shadow_payload["excluded_middle_dimensions"])
    shadow_by_b = {
        row["middle_intersection_dimension_b"]: row["exact_product_shadow_minimum"]
        for row in shadow_payload["rows"]
    }
    layers = [enumerate_layer(b, shadow_by_b[b]) for b in range(45, 53)]
    observed = {
        row["b"]: (
            row["exact_product_shadow_minimum"],
            row["defect_budget"],
            row["feasible_symmetric_epsilon_type_count"],
            row["impossible_quadratic_rank_twelve_type_count"],
            row["minimum_coupled_middle_rank_lower"],
            row["twenty_term_residual_middle_rank_upper"],
            row["strict_margin"],
        )
        for row in layers
    }
    expected = {
        45: (72, 6, 24, 7, 98, 90, 8),
        46: (72, 6, 24, 7, 98, 92, 6),
        47: (75, 3, 6, 1, 112, 94, 18),
        48: (75, 3, 6, 1, 112, 96, 16),
        49: (75, 3, 6, 1, 112, 98, 14),
        50: (75, 3, 6, 1, 112, 100, 12),
        51: (78, 0, 1, 0, 120, 102, 18),
        52: (78, 0, 1, 0, 120, 104, 16),
    }
    if observed != expected:
        raise AssertionError((observed, expected))
    return {
        "status": "EXACT_N6_ORDINARY_CHOW_RANK_LOWER_27_COMPLETION",
        "arithmetic": "pure inequalities plus exhaustive exact integer profile enumeration",
        "dependencies": {
            "fixed_six_surviving_range": [45, 64],
            "N6_056_excluded_range": list(range(53, 65)),
            "projection_cap": PROJECTION_CAP,
            "single_term_quadratic_middle_profiles": {
                "15": 20,
                "14": 20,
                "13": 18,
                "12": "impossible",
                "11": 14,
                "0_to_10": 0,
            },
        },
        "low_layers": layers,
        "strict_conclusion": (
            "Every fixed-six layer b=45,...,52 contradicts h<=2b, while "
            "N6-056 excludes b=53,...,64. Therefore a 26-term Chow "
            "decomposition of perm_6 does not exist. Together with the "
            "existing lower bound 26, ChowRank(perm_6)>=27."
        ),
        "ordinary_rank_interval": [27, 32],
        "claim_boundary": (
            "This is an ordinary Chow-rank lower bound conditional only on "
            "the cited proved fixed-six interfaces. It does not prove border "
            "Chow rank at least 27 and does not determine the exact ordinary "
            "rank inside 27,...,32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(
        "low_layer_margins="
        + str({row["b"]: row["strict_margin"] for row in payload["low_layers"]})
    )
    print("ordinary_rank_interval=27..32")
    print("N6_LOWER27_COMPLETION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
