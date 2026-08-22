"""Compose the existing K3,2 fixed-direction certificates.

This script is deliberately a small logical certificate.  It does not claim
that a component of the rank-six incidence through the K3,2 point always
degenerates to one of the finite representatives.  It records exactly what
would follow if that missing finite-point realization interface were proved.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_actual_normal_cone_composition.json"


def require(condition: bool, detail: object = "requirement failed") -> None:
    if not condition:
        raise AssertionError(detail)


def load(name: str) -> dict[str, object]:
    path = ROOT / "data" / name
    return json.loads(path.read_text(encoding="utf-8"))


def build_payload() -> dict[str, object]:
    first = load("n6_k32_full_first_schur_weight_blocks.json")
    single = load("n6_k32_single_cross_determinant_weight.json")
    same = load("n6_k32_same_row_finite_germ.json")
    signs = load("n6_k32_average_sign_germs.json")

    require(first["status"] == "EXACT_QQ_FULL_FIRST_SCHUR_WEIGHT_BLOCKS")
    require(first["fixed_direction_count"] == 44)
    require(first["row_changing_block_count"] == 24)
    require(first["same_row_block_count"] == 4)

    require(single["status"] == "PURE_TORUS_WEIGHT_COMPLETED_K32_SINGLE_CROSS_EXCLUSION")
    require(single["symmetry_orbit"]["unit_directions_covered"] == 24)
    require(single["theorem"].endswith("noncomplementary."))

    require(same["status"] == "EXACT_SAME_ROW_FINITE_GERM_EXCLUSION")
    same_branches = same["exact_certificate"]["branches"]
    require(same_branches["plus"]["sum_rank"] == 9)
    require(same_branches["minus"]["sum_rank"] == 9)
    require(same_branches["product"]["sum_rank"] == 12)
    require("actual" in same["consequence"])

    require(signs["status"] == "EXACT_QQ_AVERAGE_SIGN_GERM_EXCLUSION")
    sign_profiles = signs["profiles"]
    require(len(sign_profiles) == 4)
    require(all(profile["base_cross_rank"] == 6 for profile in sign_profiles))
    require(signs["consequence"].startswith("The three nontrivial sign-average lines"))

    direction_partition = {
        "row_changing": 24,
        "same_row_relative": 4,
        "same_row_average_sign": 4 * 4,
        "total": 24 + 4 + 4 * 4,
    }
    require(direction_partition["total"] == first["fixed_direction_count"])

    return {
        "certificate": "N6-131",
        "status": "CONDITIONAL_K32_ACTUAL_NORMAL_CONE_COMPOSITION",
        "field": "characteristic zero",
        "hypothesis": {
            "base": "the coordinate K3,2 rank-three collision",
            "incidence": "the actual Chow-pair rank-at-most-six incidence is torus-stable",
            "finite_point_realization": (
                "every irreducible complementary component through the base has an "
                "extremal torus degeneration to one of the finite representatives "
                "listed below, with the local branch map preserved"
            ),
        },
        "fixed_direction_partition": direction_partition,
        "local_inputs": {
            "row_changing": {
                "directions": 24,
                "certificate": "N6-123",
                "conclusion": "completed complement determinant vanishes",
            },
            "same_row_relative": {
                "directions": 4,
                "certificate": "N6-125",
                "relaxed_product_branch": "excluded for actual Chow differences by N6-119",
            },
            "same_row_average_sign": {
                "directions": 16,
                "certificate": "N6-127",
                "conclusion": "all local branches are noncomplementary",
            },
        },
        "conditional_conclusion": (
            "Under finite_point_realization, no actual complementary component of "
            "the K3,2 rank-at-most-six incidence passes through the coordinate "
            "collision: its torus-fixed extremal direction is in the 24+4+16 list, "
            "and the corresponding local certificate excludes complementarity."
        ),
        "logic": [
            "N6-126 classifies the torus-fixed first-Schur directions.",
            "N6-123, N6-125, and N6-127 exclude actual complementarity at every listed finite orbit.",
            "A torus-stable component with the stated finite degeneration would therefore contradict its generic complementarity.",
        ],
        "boundary": [
            "finite_point_realization is an explicit unproved hypothesis",
            "mixed torus-weight sums and arbitrary nonlinear lifts are not classified by this certificate",
            "the K2,3 transpose endpoint is not included",
            "this does not prove ordinary lower 29, exact ChowRank(perm_6), or border rank",
        ],
        "source_certificates": ["N6-123", "N6-125", "N6-126", "N6-127", "N6-119"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen JSON differs from exact replay")
    print("certificate=N6-131")
    print("fixed_directions=44")
    print("conditional_local_exclusions=44")
    print("status=PASS_CONDITIONAL")


if __name__ == "__main__":
    main()
