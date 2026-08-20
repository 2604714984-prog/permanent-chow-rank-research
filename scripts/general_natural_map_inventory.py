"""Small exact inventory of already-frozen natural-map certificates.

This is an index, not a new rank engine: it reads immutable JSON certificates,
copies only theorem-bearing fields, and preserves UNKNOWN where a source does
not provide a uniform one-term cap or a characteristic-zero exact rank.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "general_natural_map_inventory.json"


def load(name: str) -> dict[str, object]:
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def build_payload() -> dict[str, object]:
    young = load("n6_all_koszul_young_ceiling.json")
    wedge = load("n6_second_koszul_rank_audit.json")
    homology = load("n6_second_koszul_homology_audit.json")
    t15 = load("n6_global_t15_prolongation_cap.json")
    t16 = load("n6_global_t16_prolongation_cap.json")
    affine = load("general_affine_segre_slice_rank.json")

    require(young["status"] == "N6_ALL_STANDARD_KOSZUL_YOUNG_CEILING_REPLAYED", young["status"])
    require(wedge["status"] == "N6_SECOND_KOSZUL_RANKS_REPLAYED", wedge["status"])
    require(homology["status"] == "N6_SECOND_KOSZUL_HOMOLOGY_CLOSED", homology["status"])
    require(t15["characteristic_zero_prolongation_upper_cap_t15"] == 458, t15)
    require(t16["characteristic_zero_prolongation_upper_cap_t16"] == 462, t16)
    require(affine["n6"]["anchored_continuous_slice_rank"] == 6, affine["n6"])

    wedge_rows = []
    for row in wedge["degrees"]:
        wedge_rows.append(
            {
                "output_degree": row["output_degree"],
                "permanent_rank": row["characteristic_zero_permanent_rank_window"],
                "one_term_rank": row["characteristic_zero_chow_rank_window"],
                "integer_ratio_lower_bound": row["certified_second_koszul_rank_ratio_lower_bound"],
                "rank_exact_in_characteristic_zero": row["rank_exact_in_characteristic_zero"],
                "source_status": "exact_or_modular_window_as_marked",
            }
        )

    return {
        "status": "NGEN_02_NATURAL_MAP_INVENTORY",
        "field": "characteristic zero unless source says modular window",
        "entries": [
            {
                "name": "standard Koszul-Young family",
                "source": "n6_all_koszul_young_ceiling.json",
                "permanent_rank": "UNKNOWN_BY_THIS_CERTIFICATE",
                "one_term_cap": "UNKNOWN_AS_A_UNIFORM_GL(V)_CAP",
                "integer_ratio_ceiling": "strictly below 26",
                "common_factor_result": "not a promoted one-term invariant",
                "profile_determined": False,
                "scope": "all standard p=2,3 candidates covered by the source replay",
                "boundary": young["claim_boundary"],
            },
            {
                "name": "first higher-wedge Koszul p=2",
                "source": "n6_second_koszul_rank_audit.json",
                "rows": wedge_rows,
                "one_term_cap": "source gives exact/window rank, not a separate degenerate uniform cap",
                "common_factor_result": "not an improved integer ratio over first Koszul",
                "profile_determined": False,
                "boundary": wedge["claim_boundary"],
            },
            {
                "name": "second-Koszul homology beta_(2,4)",
                "source": "n6_second_koszul_homology_audit.json",
                "permanent_rank": homology["permanent"]["exact_characteristic_zero_second_koszul_rank"],
                "one_term_rank": homology["single_independent_chow_term"]["exact_characteristic_zero_second_koszul_rank"],
                "integer_ratio_lower_bound": homology["certified_integer_rank_ratio_lower_bound"],
                "one_term_cap": "not promoted to a uniform degenerate cap",
                "common_factor_result": "six-term common-factor family defeats scalar homology upper-bound comparisons",
                "profile_determined": False,
                "boundary": homology["claim_boundary"],
            },
            {
                "name": "global t=15 prolongation cap",
                "source": "n6_global_t15_prolongation_cap.json",
                "permanent_rank": "NOT_APPLICABLE",
                "one_term_cap": t15["characteristic_zero_prolongation_upper_cap_t15"],
                "integer_ratio_lower_bound": "NOT_APPLICABLE",
                "common_factor_result": "cap is only for extremal and alpha-one closure classes",
                "profile_determined": False,
                "boundary": t15["claim_boundary"],
            },
            {
                "name": "global t=16 prolongation cap",
                "source": "n6_global_t16_prolongation_cap.json",
                "permanent_rank": "NOT_APPLICABLE",
                "one_term_cap": t16["characteristic_zero_prolongation_upper_cap_t16"],
                "integer_ratio_lower_bound": "NOT_APPLICABLE",
                "common_factor_result": "one-rectangle alpha-two boundary remains separate",
                "profile_determined": False,
                "boundary": t16["claim_boundary"],
            },
            {
                "name": "continuous anchored affine-Segre slice",
                "source": "general_affine_segre_slice_rank.json",
                "permanent_rank": "NOT_APPLICABLE_TO_FULL_PERMANENT",
                "one_term_cap": "exact slice rank n; for n=6 it is 6",
                "integer_ratio_lower_bound": "NOT_APPLICABLE",
                "common_factor_result": "continuous ratios collapse the Boolean sign slice from 32 to 6",
                "profile_determined": False,
                "boundary": affine["claim_boundary"],
            },
        ],
        "route_decision": {
            "promoted_candidate": None,
            "reason": "Every indexed route either has a strict <26 ceiling, no uniform degenerate one-term cap, or is a restricted slice/cap rather than an unrestricted Chow invariant.",
            "next_required_theorem": "A coordinate-invariant cross-degree invariant with a proved cap for every degenerate Chow term and a subadditivity inequality.",
        },
        "claim_boundary": [
            "This inventory does not determine ChowRank(perm_6).",
            "It does not prove or refute ChowRank(perm_n)=2^(n-1).",
            "UNKNOWN means the cited source did not certify the requested field, not that the value is zero.",
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
