#!/usr/bin/env python3
"""Exact coordinate and local frontier for near-extremal permanent six-planes."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTREMAL = ROOT / "scripts" / "n6_extremal_six_plane_audit.py"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_extremal():
    spec = importlib.util.spec_from_file_location("n6_extremal_local", EXTREMAL)
    require(spec is not None and spec.loader is not None, EXTREMAL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rectangle_count(edges: frozenset[tuple[int, int]]) -> int:
    return sum(
        frozenset(((r, c), (r, d), (s, c), (s, d))) <= edges
        for r, s in combinations(range(6), 2)
        for c, d in combinations(range(6), 2)
    )


def oriented_graph_key(edges: frozenset[tuple[int, int]]) -> tuple[object, ...]:
    rows = sorted({row for row, _ in edges})
    columns = sorted({column for _, column in edges})
    normalized = {(rows.index(row), columns.index(column)) for row, column in edges}
    best = None
    for row_order in permutations(range(len(rows))):
        patterns = tuple(
            sorted(
                tuple((row_order[index], column) in normalized for index in range(len(rows)))
                for column in range(len(columns))
            )
        )
        candidate = (len(rows), len(columns), patterns)
        if best is None or candidate < best:
            best = candidate
    require(best is not None, edges)
    return best


def unoriented_graph_key(edges: frozenset[tuple[int, int]]) -> tuple[object, ...]:
    transpose = frozenset((column, row) for row, column in edges)
    return min(oriented_graph_key(edges), oriented_graph_key(transpose))


def coordinate_classification() -> dict[str, object]:
    oriented_classes: dict[tuple[object, ...], tuple[int, frozenset[tuple[int, int]]]] = {}
    unoriented_classes: dict[tuple[object, ...], tuple[int, frozenset[tuple[int, int]]]] = {}
    # Every graph with a rectangle can be relabelled to contain this base
    # K_2,2. Adding the remaining two edges gives all relevant isomorphism
    # types without scanning all C(36,6) labelled supports.
    base_rectangle = frozenset(((0, 0), (0, 1), (1, 0), (1, 1)))
    all_edges = frozenset((row, column) for row in range(6) for column in range(6))
    for extra in combinations(sorted(all_edges - base_rectangle), 2):
        edges = base_rectangle | frozenset(extra)
        count = rectangle_count(edges)
        oriented_classes.setdefault(oriented_graph_key(edges), (count, edges))
        unoriented_classes.setdefault(unoriented_graph_key(edges), (count, edges))

    oriented_histogram: dict[int, int] = {}
    for count, _ in oriented_classes.values():
        oriented_histogram[count] = oriented_histogram.get(count, 0) + 1
    unoriented_histogram: dict[int, int] = {}
    representatives: dict[int, list[list[list[int]]]] = {}
    for count, edges in unoriented_classes.values():
        unoriented_histogram[count] = unoriented_histogram.get(count, 0) + 1
        representatives.setdefault(count, []).append([list(edge) for edge in sorted(edges)])

    require(oriented_histogram == {1: 12, 3: 2}, oriented_histogram)
    require(unoriented_histogram == {1: 7, 3: 1}, unoriented_histogram)
    five_max = 1
    return {
        "oriented_positive_rectangle_isomorphism_histogram": {str(k): v for k, v in sorted(oriented_histogram.items())},
        "unoriented_positive_rectangle_isomorphism_histogram": {str(k): v for k, v in sorted(unoriented_histogram.items())},
        "unoriented_one_rectangle_representatives": sorted(representatives[1]),
        "five_edge_maximum_rectangle_count": five_max,
    }


def rational_rank(matrix: list[list[int]]) -> int:
    data = [[Fraction(value) for value in row] for row in matrix]
    rows = len(data)
    columns = len(data[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if data[row][column]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        scale = data[rank][column]
        data[rank] = [value / scale for value in data[rank]]
        for row in range(rows):
            if row == rank or not data[row][column]:
                continue
            factor = data[row][column]
            data[row] = [left - factor * right for left, right in zip(data[row], data[rank])]
        rank += 1
    return rank


def residual_rank(matrix: list[list[int]]) -> int:
    nonzero_rows = [row for row in matrix if any(row)]
    return rational_rank(nonzero_rows) if nonzero_rows else 0


def column_collision_family(extremal) -> list[dict[str, object]]:
    rows = []
    for sources in ((0, 1), (0, 2), (1, 2), (0, 1, 2)):
        ranks = []
        for parameter in (1, 2):
            vectors = []
            for row in (0, 1):
                for column in (0, 1, 2):
                    vector = {extremal.variable(row, column): 1}
                    if column in sources:
                        vector[extremal.variable(row, 3)] = parameter
                    vectors.append(vector)
            matrix = extremal.zero_matrix(
                len(extremal.QUOTIENT_MONOMIALS), len(extremal.L0_PAIRS)
            )
            output_column = 0
            for first_index, first in enumerate(vectors):
                for second in vectors[first_index:]:
                    for first_variable, first_coefficient in first.items():
                        for second_variable, second_coefficient in second.items():
                            extremal.add_quotient_monomial(
                                matrix,
                                output_column,
                                first_variable,
                                second_variable,
                                first_coefficient * second_coefficient,
                            )
                    output_column += 1
            ranks.append(rational_rank(matrix))
        require(ranks == [19, 19], (sources, ranks))
        rows.append({
            "shifted_base_columns": list(sources),
            "outside_column": 3,
            "exact_mu_ranks_at_parameters_1_and_2": ranks,
            "exact_intersection_dimensions_at_parameters_1_and_2": [2, 2],
        })
    return rows


def local_leading_diagnostic(extremal) -> dict[str, object]:
    directions, labels = extremal.expected_tangent_directions()
    rows = []
    samples = {
        "row_bad_pair": (0, 4),
        "column_bad_pair": (8, 11),
        "column_bad_triple": (8, 11, 14),
    }
    for name, indices in samples.items():
        direction = extremal.combine_directions(*(directions[index] for index in indices))
        first, second = extremal.direction_matrices(direction)
        residual_one, residual_two = extremal.schur_series(first, second)
        require(extremal.matrix_is_zero(residual_one), (name, "nonzero first residual"))
        rank = residual_rank(residual_two)
        exact_ranks = []
        for parameter in (1, 2):
            actual = extremal.matrix_add(
                extremal.BASE_MATRIX,
                [[parameter * first[r][c] + parameter * parameter * second[r][c]
                  for c in range(len(extremal.L0_PAIRS))]
                 for r in range(len(extremal.BASE_MATRIX))],
            )
            exact_ranks.append(rational_rank(actual))
        rows.append({
            "name": name,
            "direction_labels": [list(labels[index]) for index in indices],
            "linear_normal_schur_rank": 0,
            "normal_schur_quadratic_rank": rank,
            "belongs_to_rank_le_19_ordinary_tangent_cone": True,
            "zero_second_correction_straight_arc_passes_first_nonzero_schur_rank_condition": rank <= 1,
            "exact_mu_ranks_at_parameters_1_and_2": exact_ranks,
            "exact_intersection_dimensions_at_parameters_1_and_2": [21 - value for value in exact_ranks],
        })
    require([row["normal_schur_quadratic_rank"] for row in rows] == [3, 1, 1], rows)
    require([row["exact_mu_ranks_at_parameters_1_and_2"] for row in rows]
            == [[21, 21], [19, 19], [19, 19]], rows)
    return {
        "base_mu_rank": 18,
        "rank_le_19_zariski_tangent_dimension": 180,
        "reason": (
            "At a rank-18 base point, the 20-minors defining rank at most 19 have "
            "no linear terms. The ordinary tangent cone is defined by the "
            "2-by-2 minors of the linear normal Schur map. The three displayed "
            "directions have zero linear Schur map. Their reported quadratic "
            "ranks concern only straight chart arcs with zero second-order "
            "correction."
        ),
        "exact_direction_rows": rows,
        "integrable_column_family": (
            "For a fixed outside column t and a subset S of at least two base "
            "columns, replace every x_(i,c), i=0,1 and c in S, by "
            "x_(i,c)+lambda*x_(i,t). For lambda nonzero the resulting six-plane "
            "has mu rank 19, hence exactly two permanent quadrics. The replay "
            "checks lambda=1,2 and |S|=2,3 exactly over QQ."
        ),
        "integrable_column_family_exact_rows": column_collision_family(extremal),
    }


def build_payload() -> dict[str, object]:
    extremal = load_extremal()
    return {
        "status": "N6_NEAR_EXTREMAL_SIX_PLANE_FRONTIER",
        "arithmetic": "exact integers and rational elimination",
        "coordinate_fixed_supports": coordinate_classification(),
        "proved_geometric_consequence": (
            "For dim L at most five, dim(E2 intersect Sym2 L) is at most one. "
            "The closed projective torus-stable locus with intersection at least "
            "two would have a coordinate fixed point, while a five-edge graph has "
            "at most one rectangle. Hence an epsilon-zero span-five Chow term has "
            "alpha at least two, and alpha one forces factor-span dimension six."
        ),
        "actual_chow_examples": {
            "epsilon_zero_alpha_one": (
                "Use the six independent grid factors u_i tensor w_c of the "
                "integrable column family. Its two permanent quadrics are "
                "squarefree in this frame, hence lie in D2(T). Therefore "
                "dim(E2 intersect D2(T))=2 and (epsilon,alpha)=(0,1)."
            ),
            "epsilon_zero_alpha_two": (
                "Use the six coordinate edge factors of any one-rectangle "
                "support. Its unique permanent quadric is squarefree in the "
                "coordinate frame, giving (epsilon,alpha)=(0,2)."
            ),
        },
        "k23_rank_le_19_local_diagnostic": local_leading_diagnostic(extremal),
        "strict_boundary": (
            "The coordinate classification and dim-L-at-most-five theorem are "
            "characteristic-zero proofs. The K_2,3 rows are exact local or explicit "
            "one-parameter diagnostics, not a component classification. For "
            "span-six Chow terms the quadratic derivative space is the "
            "15-dimensional squarefree frame subspace of Sym2(L), so alpha is "
            "not determined by E2 intersect Sym2(L) alone."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print("N6_NEAR_EXTREMAL_SIX_PLANE_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
