#!/usr/bin/env python3
"""Exact N6-046 pruning of the N6-041 near-extremal scalar states.

The replay applies the N6-044 universal extremal-frame prolongation cap to
the frozen N6-041 state table.  It performs only exact integer comparisons;
it neither tests geometric realizability nor discards an entire ``b`` layer.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6041_DATA = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"
N6044_DATA = ROOT / "data" / "n6_b64_prolongation_exclusion.json"
PERMANENT_CUBIC_DIMENSION = 400


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def state_identifier(intersection: int, ordinal: int) -> str:
    return f"N6-041-B{intersection}-S{ordinal:03d}"


def build_payload() -> dict[str, object]:
    source = json.loads(N6041_DATA.read_text(encoding="utf-8"))
    cap_source = json.loads(N6044_DATA.read_text(encoding="utf-8"))
    cap = int(cap_source["maximum_prolongation_dimension_upper_bound"])
    require(cap == 436, ("N6-044 cap drift", cap))

    layers: list[dict[str, object]] = []
    for layer in source["layers"]:
        intersection = int(layer["middle_intersection_b"])
        excluded: list[dict[str, object]] = []
        retained: list[str] = []

        for ordinal, state in enumerate(layer["states"], start=1):
            identifier = state_identifier(intersection, ordinal)
            pairs = state["epsilon_alpha_pairs"]
            has_extremal_term = any(pair == [0, 0] for pair in pairs)
            common_quotient = (
                int(state["fixed_quadratic_quotient_t2"]) == 12
                and has_extremal_term
            )
            if not common_quotient:
                retained.append(identifier)
                continue

            middle_rank = int(state["fixed_middle_rank_h"])
            required = PERMANENT_CUBIC_DIMENSION + middle_rank - intersection
            require(required > cap, (identifier, required, cap))
            excluded.append(
                {
                    "state_identifier": identifier,
                    "epsilon_alpha_pairs": pairs,
                    "quadratic_relation_dimension_kappa2": int(
                        state["quadratic_relation_dimension_kappa2"]
                    ),
                    "fixed_quadratic_rank_d2": int(
                        state["fixed_quadratic_rank_d2"]
                    ),
                    "fixed_quadratic_intersection_a2": int(
                        state["fixed_quadratic_intersection_a2"]
                    ),
                    "fixed_quadratic_quotient_t2": 12,
                    "fixed_middle_rank_h": middle_rank,
                    "extremal_rectangle_term_count": int(
                        state["extremal_rectangle_term_count"]
                    ),
                    "required_common_prolongation_dimension": required,
                    "universal_extremal_prolongation_cap": cap,
                    "strict_contradiction_gap": required - cap,
                }
            )

        total = int(layer["canonical_scalar_state_count"])
        require(total == len(excluded) + len(retained), intersection)
        layers.append(
            {
                "middle_intersection_b": intersection,
                "source_scalar_state_count": total,
                "excluded_scalar_state_count": len(excluded),
                "remaining_scalar_state_count": len(retained),
                "excluded_state_identifiers": [
                    row["state_identifier"] for row in excluded
                ],
                "remaining_state_identifiers": retained,
                "excluded_states": excluded,
            }
        )

    by_b = {int(row["middle_intersection_b"]): row for row in layers}
    require(
        {
            b: (
                int(by_b[b]["excluded_scalar_state_count"]),
                int(by_b[b]["remaining_scalar_state_count"]),
            )
            for b in (61, 62, 63)
        }
        == {61: (13, 60), 62: (4, 7), 63: (4, 7)},
        by_b,
    )

    return {
        "status": "EXACT_N6_NEAR_EXTREMAL_PROLONGATION_PRUNING",
        "arithmetic": "exact integer filtering of frozen scalar states",
        "source_state_table": "N6-041",
        "universal_extremal_prolongation_cap_source": "N6-044",
        "universal_extremal_prolongation_cap": cap,
        "layers": layers,
        "strict_conclusion": {
            "excluded_scalar_states_by_b": {"61": 13, "62": 4, "63": 4},
            "remaining_scalar_states_by_b": {"61": 60, "62": 7, "63": 7},
        },
        "claim_boundary": (
            "The replay excludes only the listed canonical scalar states.  "
            "It does not exclude any complete b=61,62,63 layer, assert that "
            "a retained state is geometrically realizable, exclude a "
            "hypothetical 26-term decomposition, prove "
            "ChowRank(perm_6)>=27, or make a border-rank claim."
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
    for layer in payload["layers"]:
        print(
            f"b={layer['middle_intersection_b']} "
            f"excluded={layer['excluded_scalar_state_count']} "
            f"remaining={layer['remaining_scalar_state_count']}"
        )
    print("N6_NEAR_EXTREMAL_PROLONGATION_PRUNING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
