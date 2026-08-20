"""Synchronize the current b=34 scalar frontier from frozen certificates.

This script does not recompute a rank.  It prevents the intermediate N6-102
ten-state table from being reported as current after the N6-107, N6-108, and
N6-109 geometric exclusions.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_state_aggregation.json"


def load(name: str) -> dict[str, object]:
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def build_payload() -> dict[str, object]:
    scalar = load("n6_lower29_b34_critical_six_scalar_frontier.json")
    biflag = load("n6_biflag_four_by_three_global_exclusion.json")
    partial_product = load("n6_product_34_partial_pair_exclusion.json")
    standard_hook = load("n6_standard_hook_partial_pair_exclusion.json")
    states = scalar["critical_six_scalar_states"]
    require(len(states) == 10, len(states))
    require("CERTIFIED_A72_KAPPA3_BIFLAG_BRANCH_EXCLUSION" in biflag["status"], biflag["status"])
    require(partial_product["certificate"] == "N6-108", partial_product["certificate"])
    require(standard_hook["certificate"] == "N6-109", standard_hook["certificate"])

    excluded_key = (72, 3, 15)
    excluded = [
        row for row in states
        if (row["a2"], row["kappa2"], row["t2"]) == excluded_key
    ]
    require(len(excluded) == 1, excluded)
    closed_keys = {(72, 1, 17), (72, 2, 16), excluded_key}
    open_states = [
        row for row in states
        if (row["a2"], row["kappa2"], row["t2"]) not in closed_keys
    ]
    require(len(open_states) == 7, len(open_states))

    closed_states = [
        {
            "a2": a2,
            "kappa2": kappa2,
            "t2": t2,
            "theorem": theorem,
            "geometry": geometry,
        }
        for (a2, kappa2, t2), theorem, geometry in (
            ((72, 1, 17), "N6-108 and N6-109", "standard and biflag product branches"),
            ((72, 2, 16), "N6-108 and N6-109", "standard and biflag product branches"),
            ((72, 3, 15), "N6-103 and N6-107", "standard and biflag hook branches"),
        )
    ]

    return {
        "status": "N6_133_B34_FRONTIER_SYNCHRONIZED",
        "source_certificates": [
            "n6_lower29_b34_critical_six_scalar_frontier.json",
            "n6_biflag_four_by_three_global_exclusion.json",
            "n6_product_34_partial_pair_exclusion.json",
            "n6_standard_hook_partial_pair_exclusion.json",
        ],
        "initial_scalar_state_count": len(states),
        "closed_states": closed_states,
        "current_open_state_count": len(open_states),
        "current_open_states": [
            {"a2": row["a2"], "kappa2": row["kappa2"], "t2": row["t2"]}
            for row in open_states
        ],
        "strict_conclusion": "N6-108 and N6-109 remove both product geometries at (a2,kappa2,t2)=(72,1,17) and (72,2,16), while N6-103 and N6-107 remove both hook geometries at (72,3,15); seven scalar states remain open.",
        "boundary": [
            "This is a state synchronization, not a new lower-29 proof.",
            "At a2=72 only the kappa2=0 standard and biflag geometries remain open.",
            "All a2=73,74,75 states remain open.",
            "It does not determine ChowRank(perm_6) or prove the 2^(n-1) conjecture.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen payload mismatch")
        print(json.dumps(payload, sort_keys=True))
        return
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
