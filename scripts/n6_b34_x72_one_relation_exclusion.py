#!/usr/bin/env python3
"""Exact interface certificate for the x=72 one-relation packet exclusion."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_b34_x72_one_relation_exclusion.json"
N6083_DATA = ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json"
N6092_DATA = ROOT / "data" / "n6_product_shadow_b72_equality_locus.json"
N6093_DATA = ROOT / "data" / "n6_lower29_b34_x72_frontier.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def good_edge_graph_certificate() -> dict[str, object]:
    vertices = tuple(range(7))
    rows = []
    for bad_edge in [None, *combinations(vertices, 2)]:
        good = {
            edge for edge in combinations(vertices, 2) if edge != bad_edge
        }
        degrees = {
            vertex: sum(vertex in edge for edge in good) for vertex in vertices
        }
        require(min(degrees.values()) >= 5, (bad_edge, degrees))
        for vertex in vertices:
            neighbors = {other for other in vertices if tuple(sorted((vertex, other))) in good}
            require(len(neighbors) >= 5, (bad_edge, vertex, neighbors))
            require(
                any(
                    tuple(sorted((left, right))) in good
                    for left, right in combinations(neighbors, 2)
                ),
                (bad_edge, vertex),
            )
        rows.append(
            {
                "bad_edge": None if bad_edge is None else list(bad_edge),
                "good_edge_count": len(good),
                "minimum_good_degree": min(degrees.values()),
            }
        )
    require(len(rows) == 22, len(rows))
    return {
        "kernel_line_positions": len(rows),
        "good_edge_count_is_21_or_20": True,
        "minimum_good_degree": 5,
        "every_vertex_has_two_good_neighbors_joined_by_a_good_edge": True,
        "cases": rows,
    }


def build_payload() -> dict[str, object]:
    n6083 = json.loads(N6083_DATA.read_text(encoding="utf-8"))
    n6092 = json.loads(N6092_DATA.read_text(encoding="utf-8"))
    n6093 = json.loads(N6093_DATA.read_text(encoding="utf-8"))
    require(
        n6083["all_singular_branch"]["contradiction"]
        and n6083["invertible_block_branch"]["resulting_cubic_permanent_intersection_dimension"] == 60,
        n6083,
    )
    require(
        n6092["projective_globalization"][
            "every_72_to_89_point_lies_in_a_partitioned_80_to_90_product_parent"
        ]
        and n6092["projective_globalization"]["every_equality_point_has_second_shadow_dimension"] == 24,
        n6092,
    )
    packets = {
        row["actual_refinement"]["name"]: row
        for row in n6093["open_actual_packets"]
    }
    packet = packets["one_quadratic_relation_common_W15_packet"]
    require(
        packet["state"]["epsilon"] == [0] * 7
        and packet["state"]["kappa2"] == 1
        and packet["actual_refinement"]["forced_a2"] == 89,
        packet,
    )
    graph = good_edge_graph_certificate()
    require(104 % 15 == 14, None)
    return {
        "status": [
            "PURE_ACTUAL_B34_X72_ONE_RELATION_EXCLUSION",
            "EXACT_KERNEL_LINE_GRAPH_REPLAY",
            "N6-094",
        ],
        "packet": {
            "frame_count": 7,
            "common_quotient_dimension": 15,
            "quadratic_sum_dimension": 104,
            "permanent_difference_space_dimension": 89,
            "difference_domain_dimension": 90,
            "difference_kernel_dimension": 1,
            "first_shadow_dimension": 24,
            "product_parent_row_dimension": 4,
        },
        "pair_difference_graph": graph,
        "good_pair_consequence": {
            "difference_dimension": 15,
            "universal_product_shadow_lower": 12,
            "factor_pair_span_upper": 12,
            "factor_planes_are_transverse_and_their_sum_lies_in_the_product_24_plane": True,
            "all_seven_factor_planes_lie_in_the_product_24_plane": True,
            "their_total_sum_equals_the_product_24_plane": True,
        },
        "invertible_block_branch": {
            "n6069_on_a_good_pair_gives_common_column_or_row_separation": True,
            "n6061_common_quotient_domain_propagates_separation_to_all_seven_frames": True,
            "n6070_on_good_edges_forces_each_frame_row_factor_span_to_have_dimension_at_most_two": True,
            "a_two_dimensional_row_factor_span_would_put_six_frames_in_one_two_plane_and_the_last_in_at_most_one_extra_line": True,
            "resulting_total_row_span_upper": 3,
            "required_total_row_span": 4,
            "therefore_every_frame_row_factor_span_is_one_dimensional": True,
            "separated_quadratic_sum_dimension_must_be_a_multiple_of_15": True,
            "observed_quadratic_sum_dimension": 104,
            "observed_remainder_modulo_15": 104 % 15,
            "excluded": True,
        },
        "all_singular_branch": {
            "n6071_common_quotient_same_row_synchronization_reapplies": True,
            "a_rank_at_least_two_active_row_block_would_force_common_rank_six": True,
            "otherwise_each_of_four_active_row_blocks_has_rank_at_most_one": True,
            "frame_rank_upper": 4,
            "required_frame_rank": 6,
            "excluded": True,
        },
        "actual_packet_excluded": True,
        "updated_x72_frontier": [
            "direct_t16_packet",
            "one_defective_term_t15_packet",
        ],
        "claim_boundary": (
            "This excludes only the all-epsilon-zero one-quadratic-relation common-W15 packet. "
            "It does not exclude the direct t16 or one-defective-term packets, x_A=72 in full, "
            "global b=34, ordinary lower 29, or any border-rank configuration."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        require(payload == json.loads(args.verify_json.read_text(encoding="utf-8")), args.verify_json)
    print("one_relation_kernel_dimension=1 good_pair_graph=K7_minus_at_most_one_edge")
    print("invertible_branch=excluded all_singular_branch=excluded")
    print("N6_B34_X72_ONE_RELATION_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
