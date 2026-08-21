#!/usr/bin/env python3
"""Exact exponent-collision certificates for packet-B moment curves."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_mixed_curve_endpoint_search as curve  # noqa: E402


def exact_compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    if parts == 1:
        return ((total,),)
    answer = []
    for first in range(total + 1):
        for suffix in exact_compositions(total - first, parts - 1):
            answer.append((first, *suffix))
    return tuple(answer)


DEGREE_SIX_COMPOSITIONS = exact_compositions(6, 7)
SQUAREFREE_TARGETS = tuple(
    tuple(0 if coordinate == excluded else 1 for coordinate in range(7))
    for excluded in range(7)
)
SQUAREFREE_TARGET_SET = frozenset(SQUAREFREE_TARGETS)
MISSING_ROW_MULTIDEGREES = tuple(
    tuple(0 if row == missing else 1 for row in range(7))
    for missing in range(7)
)
PURE_ROW_MULTIDEGREES = tuple(
    tuple(6 if row == supported else 0 for row in range(7))
    for supported in range(7)
)


def weighted_exponent(alpha: tuple[int, ...], weights: tuple[int, ...]) -> int:
    affine_weights = (0, *weights)
    return sum(power * weight for power, weight in zip(alpha, affine_weights))


def collision_witnesses(weights: tuple[int, ...]) -> list[dict[str, object]]:
    by_exponent: dict[int, list[tuple[int, ...]]] = {}
    for alpha in DEGREE_SIX_COMPOSITIONS:
        if alpha in SQUAREFREE_TARGET_SET:
            continue
        by_exponent.setdefault(weighted_exponent(alpha, weights), []).append(alpha)

    witnesses = []
    for excluded, target in enumerate(SQUAREFREE_TARGETS):
        exponent = weighted_exponent(target, weights)
        alternatives = by_exponent.get(exponent, [])
        witnesses.append(
            {
                "excluded_coordinate": excluded,
                "weighted_exponent": exponent,
                "target_composition": list(target),
                "nonsquarefree_collision": list(alternatives[0])
                if alternatives
                else None,
            }
        )
    return witnesses


def build_payload(max_weight: int = 24) -> dict[str, object]:
    scanned, candidates = curve.scan_weight_profiles(max_weight)
    rows = []
    for weights in candidates:
        h3 = curve.exact_curve_rank(weights, 3)
        h4 = curve.exact_curve_rank(weights, 4)
        if h3 + h4 != curve.GRAPH_MIDDLE_PROFILE_SUM:
            continue
        witnesses = collision_witnesses(weights)
        certified = sum(
            witness["nonsquarefree_collision"] is not None
            for witness in witnesses
        )
        rows.append(
            {
                "weights": list(weights),
                "point_code_profile": [h3, h4],
                "certified_independent_degree_six_targets_per_missing_row": certified,
                "packet_degree_six_target_increment": 7 * certified,
                "witnesses": witnesses,
            }
        )
    histogram: dict[str, int] = {}
    for row in rows:
        key = str(row["certified_independent_degree_six_targets_per_missing_row"])
        histogram[key] = histogram.get(key, 0) + 1
    return {
        "schema_version": 1,
        "status": "EXACT_CHARACTERISTIC_ZERO_CURVE_TARGET_EXCLUSION",
        "max_weight": max_weight,
        "weight_candidate_count": scanned,
        "middle_equality_candidate_count": len(rows),
        "degree_six_composition_count": len(DEGREE_SIX_COMPOSITIONS),
        "certified_target_count_histogram_per_missing_row": histogram,
        "rows": rows,
        "certificate": (
            "In the labelled tensor product of the six retained row spaces, "
            "every graph ordered-word coefficient depends only on its weighted "
            "exponent.  Subtracting a nonsquarefree collision-word coefficient "
            "from the corresponding squarefree target-word coefficient "
            "annihilates every graph row and evaluates as a Kronecker delta on "
            "the seven permanent targets."
        ),
        "claim_boundary": [
            "The certificate is over the integers and hence in characteristic zero; it does not rely on a random evaluation projection.",
            "The seven rank-six packet terms have incompatible row multidegrees and cannot repair these missing-one-row target components.",
            "The scan exhausts only strictly increasing monomial-curve weights in the displayed box.",
            "No arbitrary common-point-set classification, ordinary lower-50 theorem, or border-rank statement follows.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-weight", type=int, default=24)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args.max_weight)
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 packet-B curve target JSON mismatch")
        print("PASS n7 packet-B curve target certificate")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
