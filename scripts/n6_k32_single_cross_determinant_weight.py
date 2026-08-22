"""Torus-weight completion of the K3,2 single-cross local exclusion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.n6_product_32_rank_six_frame_barrier import require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_single_cross_determinant_weight.json"
SOURCE_JSON = ROOT / "data" / "n6_product_32_single_cross_tangent_reduction.json"


def cell_character(index: int) -> list[int]:
    row, column = divmod(index, 4)
    return [int(i == row) for i in range(3)] + [
        int(i == column) for i in range(4)
    ]


def quotient_character(weight: list[int]) -> list[int]:
    """Impose the base constraint wt(12)-wt(00)=0 and remove r_1."""
    r0, r1, r2, c0, c1, c2, c3 = weight
    return [r0 + r1, r2, c0 + r1, c1, c2 - r1, c3]


def variable_weights(labels: list[list[dict[str, object]]]) -> list[list[int]]:
    weights: list[list[int]] = []
    for variable in labels:
        first = variable[0]
        target = int(first["target"])
        source = int(first["source"])
        target_weight = cell_character(target)
        source_weight = cell_character(source)
        weights.append(
            quotient_character(
                [a - b for a, b in zip(target_weight, source_weight)]
            )
        )
    return weights


def determinant_weight() -> list[int]:
    support = (0, 1, 4, 5, 8, 9)
    weight = [0] * 7
    for index in range(12):
        weight = [
            a + b for a, b in zip(weight, cell_character(index))
        ]
    for index in support:
        weight = [
            a - 2 * b for a, b in zip(weight, cell_character(index))
        ]
    return quotient_character(weight)


def exact_certificate() -> dict[str, object]:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    local = source["local_system"]
    labels = local["tangent_variable_labels"]
    facets = [tuple(item) for item in local["maximal_facets"]]
    weights = variable_weights(labels)
    target = determinant_weight()
    require(
        target == [0, 0, -3, -3, 3, 3],
        target,
    )
    require(
        facets
        == [
            (0, 1, 3, 6, 7),
            (0, 2, 3, 4),
            (0, 2, 3, 6, 7),
            (0, 3, 5, 6, 7),
        ],
        facets,
    )
    positive_c3 = [
        index for index, weight in enumerate(weights) if weight[5] > 0
    ]
    require(positive_c3 == [1], positive_c3)
    facet_obstructions: list[dict[str, object]] = []
    for facet in facets:
        if 1 not in facet:
            facet_obstructions.append(
                {
                    "facet": list(facet),
                    "reason": "no variable has positive c3 weight",
                    "required_c3": 3,
                }
            )
            continue
        residual = [
            target[i] - 3 * weights[1][i] for i in range(6)
        ]
        other = [index for index in facet if index != 1]
        other_c0 = [weights[index][2] for index in other]
        require(residual[2] == -3, residual)
        require(min(other_c0) >= 0, (facet, other_c0))
        facet_obstructions.append(
            {
                "facet": list(facet),
                "forced_variable": "x1^3",
                "residual_weight": residual,
                "remaining_c0_weights": other_c0,
                "reason": "required residual c0 is negative but all remaining c0 weights are nonnegative",
            }
        )
    return {
        "source_certificate": "N6-116",
        "weight_basis": ["r0+r1", "r2", "c0+r1", "c1", "c2-r1", "c3"],
        "base_constraint": "wt(12)-wt(00)=0",
        "tangent_variable_weights": weights,
        "determinant_weight": target,
        "positive_c3_variables": positive_c3,
        "facets": [list(item) for item in facets],
        "facet_obstructions": facet_obstructions,
        "no_surviving_determinant_weight_monomial": True,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-123",
        "status": "PURE_TORUS_WEIGHT_COMPLETED_K32_SINGLE_CROSS_EXCLUSION",
        "field": "characteristic zero",
        "hypothesis": (
            "completed rank-at-most-six germ at the N6-116 single-cross "
            "K3,2 point, with N6-116 quadratic initial ideal"
        ),
        "exact_certificate": exact_certificate(),
        "theorem": (
            "The complement determinant vanishes in the completed local "
            "incidence ring; every branch through this point is "
            "noncomplementary."
        ),
        "symmetry_orbit": {
            "unit_directions_covered": 24,
            "condition": "target row differs from source row",
            "nonzero_coefficient_torus_orbit": True,
        },
        "proof_interface": [
            "N6-116 supplies J subset in_m(I) and the four facet primes.",
            "The determinant is a semi-invariant for the base-preserving "
            "row-column subtorus.",
            "No monomial in the four facet quotients has its determinant weight.",
            "Completeness of the m-adic ring then forces the determinant to "
            "vanish identically.",
        ],
        "boundary": [
            "does not classify the other K3,2 collision points",
            "does not classify nonlinear lifts at the remaining K32 facets "
            "outside this exact representative orbit",
            "does not classify arbitrary invertible 6 by 6 graph operators",
            "does not prove ordinary lower 29 or exact Chow rank 32",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
    if args.verify_json:
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            "frozen JSON differs from exact replay",
        )
    print("certificate=N6-123")
    print("determinant_weight=(0,0,-3,-3,3,3)")
    print("facet_count=4")
    print("status=PASS")


if __name__ == "__main__":
    main()
