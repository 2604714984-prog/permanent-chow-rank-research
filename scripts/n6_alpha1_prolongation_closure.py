#!/usr/bin/env python3
"""Exact N6-048 state pruning after the pure alpha-one cap."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_DATA = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"
CAP_DATA = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"
PERMANENT_CUBIC_DIMENSION = 400


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def state_id(b_value: int, zero_based_index: int) -> str:
    return f"b{b_value}_state_{zero_based_index:03d}"


def build_payload() -> dict[str, object]:
    states = json.loads(STATE_DATA.read_text(encoding="utf-8"))
    cap_payload = json.loads(CAP_DATA.read_text(encoding="utf-8"))
    caps = cap_payload["fixed_point_cap_audit"][
        "characteristic_zero_prolongation_upper_caps"
    ]
    require((int(caps["13"]), int(caps["14"])) == (440, 448), caps)

    rows = []
    expected = {61: (73, 72, 1), 62: (11, 11, 0), 63: (11, 11, 0)}
    for layer in states["layers"]:
        b_value = int(layer["middle_intersection_b"])
        excluded = []
        remaining = []
        for index, state in enumerate(layer["states"]):
            identifier = state_id(b_value, index)
            pairs = state["epsilon_alpha_pairs"]
            has_extremal = [0, 0] in pairs
            alpha_one_near = (
                int(state["fixed_quadratic_quotient_t2"]) in (13, 14)
                and [0, 1] in pairs
            )
            if has_extremal or alpha_one_near:
                required = (
                    PERMANENT_CUBIC_DIMENSION
                    + int(state["fixed_middle_rank_h"])
                    - b_value
                )
                applicable_cap = (
                    int(caps[str(state["fixed_quadratic_quotient_t2"])])
                    if has_extremal
                    else int(caps[str(state["fixed_quadratic_quotient_t2"])])
                )
                require(required > applicable_cap, (identifier, required, applicable_cap))
                excluded.append(
                    {
                        "state_id": identifier,
                        "reason": (
                            "N6-047 extremal-term cap"
                            if has_extremal
                            else "N6-048 universal alpha-one cap at t2=13 or 14"
                        ),
                        "required_prolongation_dimension": required,
                        "applicable_upper_cap": applicable_cap,
                    }
                )
            else:
                remaining.append(
                    {
                        "state_id": identifier,
                        "epsilon_alpha_pairs": pairs,
                        "t2": int(state["fixed_quadratic_quotient_t2"]),
                    }
                )

        observed = (len(layer["states"]), len(excluded), len(remaining))
        require(observed == expected[b_value], (b_value, observed))
        rows.append(
            {
                "b": b_value,
                "canonical_state_count": observed[0],
                "excluded_state_count": observed[1],
                "excluded_states": excluded,
                "remaining_state_count": observed[2],
                "remaining_states": remaining,
            }
        )

    require(
        [row["state_id"] for row in rows[0]["remaining_states"]]
        == ["b61_state_072"],
        rows[0]["remaining_states"],
    )
    require(not rows[1]["remaining_states"] and not rows[2]["remaining_states"], rows)

    return {
        "status": "N6_048_ALPHA1_PROLONGATION_CLOSURE",
        "arithmetic": "exact integer pruning using frozen N6-041 states and N6-047 caps",
        "pure_alpha1_prolongation_caps": {"13": 440, "14": 448},
        "layers": rows,
        "strict_conclusion": (
            "The complete b=62 and b=63 layers are impossible. One canonical "
            "all-alpha-two t2=14 state remains at b=61."
        ),
        "claim_boundary": (
            "The result is conditional on the fixed-six reduction of a "
            "hypothetical twenty-six-term decomposition. It does not exclude "
            "the single b=61 state, prove ChowRank(perm_6)>=27, or make a "
            "border-rank claim."
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
    for row in payload["layers"]:
        print(
            f"b={row['b']} excluded={row['excluded_state_count']} "
            f"remaining={row['remaining_state_count']}"
        )
    print("N6_ALPHA1_PROLONGATION_CLOSURE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
