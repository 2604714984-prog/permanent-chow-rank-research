#!/usr/bin/env python3
"""Exact six-variable audit of the colored mapping-cone scalar barrier."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def load_g037():
    path = ROOT / "scripts" / "n6_labelled_cycle_fitting_barrier.py"
    spec = importlib.util.spec_from_file_location("n6_g037", path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_g034():
    path = ROOT / "scripts" / "n6_hereditary_central_koszul_barrier.py"
    spec = importlib.util.spec_from_file_location("n6_g034", path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pair_relation_homology(
    g037, profile: dict[str, object], second_matrix: list[list[int]]
) -> dict[str, object]:
    derivative = profile["verified_derivative_dimensions"]
    term_middle = [int(row["D3_dimension"]) for row in derivative]
    middle_products = []
    for matrix in (g037.IDENTITY, second_matrix):
        factors = g037.factor_columns(matrix)
        middle_products.extend(
            g037.product_of_linears([factors[index] for index in subset])
            for subset in g037.combinations(range(6), 3)
        )
    literal_middle_rank = g037.rank_fraction(middle_products)
    ordinary_middle_relation = sum(term_middle) - literal_middle_rank
    return {
        "name": profile["name"],
        "individual_middle_ranks": term_middle,
        "literal_middle_sum_rank": literal_middle_rank,
        "ordinary_middle_relation_dimension": ordinary_middle_relation,
        "aggregate_boundary_rank": profile["boundary_sum_rank"],
        "labelled_cycle_rank": profile["cycle_sum_rank"],
        "labelled_presentation_rank": profile["joint_labelled_presentation_rank"],
        "labelled_presentation_kernel": profile["joint_kernel_dimension"],
    }


def build_payload() -> dict[str, object]:
    g037 = load_g037()
    g034 = load_g034()
    full = g037.pair_profile(g037.UPPER_ONES, "two_full_span_terms")
    rank_five = g037.pair_profile(
        g037.CYCLIC_NEIGHBOUR,
        "full_span_plus_uniform_five_span_term",
    )
    rows = [
        pair_relation_homology(g037, full, g037.UPPER_ONES),
        pair_relation_homology(g037, rank_five, g037.CYCLIC_NEIGHBOUR),
    ]
    require(rows[0]["ordinary_middle_relation_dimension"] == 4, rows[0])
    require(rows[0]["labelled_presentation_kernel"] == 7, rows[0])
    require(rows[1]["ordinary_middle_relation_dimension"] == 2, rows[1])
    require(rows[1]["labelled_presentation_kernel"] == 12, rows[1])

    triple_factors = [list(family) for family in g034.FACTOR_FAMILIES]
    triple_boundaries = [
        column
        for factors in triple_factors
        for column in g037.boundary_columns(factors)
    ]
    triple_cycles = [
        column
        for factors in triple_factors
        for column in g037.labelled_cycles(factors)
    ]
    triple_middle_products = [
        g037.product_of_linears([factors[index] for index in subset])
        for factors in triple_factors
        for subset in g037.combinations(range(6), 3)
    ]
    triple_boundary_rank = g037.rank_fraction(triple_boundaries)
    triple_cycle_rank = g037.rank_fraction(triple_cycles)
    triple_joint_rank = g037.rank_fraction([*triple_boundaries, *triple_cycles])
    triple_middle_rank = g037.rank_fraction(triple_middle_products)
    require(
        (triple_middle_rank, triple_boundary_rank, triple_cycle_rank, triple_joint_rank)
        == (56, 570, 60, 630),
        (triple_middle_rank, triple_boundary_rank, triple_cycle_rank, triple_joint_rank),
    )
    triple = {
        "name": "g034_completed_three_term_block",
        "individual_middle_ranks": [20, 20, 20],
        "literal_middle_sum_rank": triple_middle_rank,
        "ordinary_middle_relation_dimension": 4,
        "aggregate_boundary_rank": triple_boundary_rank,
        "labelled_cycle_rank": triple_cycle_rank,
        "boundary_plus_labelled_rank": triple_joint_rank,
        "labelled_presentation_rank": triple_joint_rank - triple_boundary_rank,
        "labelled_presentation_kernel": 60
        - (triple_joint_rank - triple_boundary_rank),
        "evidence": (
            "The middle rank 56 is replayed by the G-034 Bareiss certificate; "
            "the 570/60/630 ranks are reconstructed here over Q in its "
            "six-variable completed block."
        ),
    }
    require(
        triple["ordinary_middle_relation_dimension"]
        == rows[0]["ordinary_middle_relation_dimension"],
        (triple, rows[0]),
    )

    return {
        "status": "G039_COLORED_MAPPING_CONE_SCALAR_ROUTE_BLOCKED",
        "field": "characteristic zero",
        "ordinary_relation_complex": (
            "Ordinary output relations allow unrelated preimages in the term "
            "images. The synchronized subspace is the image of one common "
            "operator and is strictly more structured."
        ),
        "mapping_cone_identity": (
            "For P=H+Q, put K_m(f)=ker C_(6-m,m)(f) and "
            "J_m^diag=C(P)(K_m(Q))=C(H)(K_m(Q)). Then "
            "0 -> K_m(P) intersect K_m(H) -> K_m(Q) -> J_m^diag -> 0 "
            "is exact. The last map sends x to C(P)x=C(H)x. This is the "
            "same-operator mapping-cone interface; it gives no additive "
            "inclusion among K_m(P), K_m(H), and K_m(Q)."
        ),
        "synchronized_colored_middle_lower": 336,
        "exact_relation_homology_rows": [triple, *rows],
        "counterexample": (
            "The G-034 triple and the two-full-span G-037 pair both have "
            "ordinary middle relation dimension four, but their labelled "
            "presentation kernels are zero and seven. The rank-five pair has "
            "ordinary relation dimension two and labelled kernel twelve."
        ),
        "permanent_data_not_used_by_counterexample": {
            "dim_H_3_6_perm6": 40,
            "dim_E3_intersect_G3_lower": 336,
            "dim_E2_intersect_G2_lower": 203,
            "fixed_six_middle_intersection_range": [45, 64],
        },
        "claim_boundary": (
            "The exact examples show that ordinary middle relation dimension "
            "does not determine the labelled quotient kernel, does not make it "
            "monotone increasing, and does not upper-bound it directly. They do "
            "not exclude every inequality using additional term or permanent "
            "data. This is not a permanent decomposition, does not rule out a "
            "weight-refined permanent-specific cone, and proves neither "
            "ChowRank(perm_6)>=27 nor any border-rank statement."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    if arguments.json:
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("G039_COLORED_MAPPING_CONE_BARRIER_PASS")


if __name__ == "__main__":
    main()
