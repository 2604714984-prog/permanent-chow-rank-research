#!/usr/bin/env python3
"""Exact audit of a minimum six-term aggregate Koszul collision for perm_6."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from collections import defaultdict
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
PAIR_SCRIPT = ROOT / "scripts" / "n6_two_permutation_monomial_quotient_audit.py"


def load_pair_audit() -> ModuleType:
    spec = importlib.util.spec_from_file_location("n6_pair_audit", PAIR_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PAIR_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PAIR = load_pair_audit()
PERMUTATIONS = tuple(itertools.permutations(range(3)))


def block_diagonal_permutation(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return permutation + tuple(value + 3 for value in permutation)


def term_edges(permutation: tuple[int, ...]) -> tuple[int, ...]:
    full = block_diagonal_permutation(permutation)
    return tuple(row * 6 + full[row] for row in range(6))


def normalized_fiber_intersection_count(phi: tuple[int, ...]) -> int:
    if len(phi) != 6 or any(index < 0 or index >= 6 for index in phi):
        raise ValueError(phi)
    selected = [
        permutation + tuple(value + 3 for value in PERMUTATIONS[phi[index]])
        for index, permutation in enumerate(PERMUTATIONS)
    ]
    count = 0
    for rows in itertools.combinations(range(6), 3):
        image_sets = [tuple(sorted(permutation[row] for row in rows))
                      for permutation in selected]
        if len(set(image_sets)) != 1:
            continue
        columns = image_sets[0]
        restrictions = {
            tuple(columns.index(permutation[row]) for row in rows)
            for permutation in selected
        }
        if len(restrictions) == 6:
            count += 1
    return count


def normalized_fiber_classification() -> dict[str, object]:
    histogram: dict[int, int] = {}
    bijective_count = 0
    formula_verified = True
    for phi in itertools.product(range(6), repeat=6):
        intersection = normalized_fiber_intersection_count(phi)
        histogram[intersection] = histogram.get(intersection, 0) + 1
        bijective = len(set(phi)) == 6
        bijective_count += int(bijective)
        formula_verified &= intersection == 1 + int(bijective)
    expected_histogram = {1: 45_936, 2: 720}
    if histogram != expected_histogram or bijective_count != 720 or not formula_verified:
        raise AssertionError((histogram, bijective_count, formula_verified))
    return {
        "normalized_six_permutation_fibers_checked": 6**6,
        "normalized_fiber_intersection_histogram": {
            str(value): count for value, count in sorted(histogram.items())
        },
        "normalized_fiber_maximum_b": 2,
        "two_intersections_exactly_when_complement_map_is_bijective": True,
        "general_six_permutation_monomial_intersection_cap_b": 2,
        "general_cap_proof_type": "pure finite combinatorial proof",
        "enumeration_role": "independent exact diagnostic, not a theorem premise",
    }


def middle_catalectic_certificate() -> dict[str, object]:
    divisor_sets: list[set[tuple[int, ...]]] = []
    complement_pairs: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for permutation in PERMUTATIONS:
        edges = term_edges(permutation)
        support = set(edges)
        divisors = set(itertools.combinations(edges, 3))
        divisor_sets.append(divisors)
        for divisor in sorted(divisors):
            complement = tuple(sorted(support.difference(divisor)))
            complement_pairs.append((divisor, complement))

    all_divisors = set().union(*divisor_sets)
    pairwise_disjoint = all(
        divisor_sets[left].isdisjoint(divisor_sets[right])
        for left in range(len(divisor_sets))
        for right in range(left)
    )
    if not pairwise_disjoint or len(all_divisors) != 120:
        raise AssertionError((pairwise_disjoint, len(all_divisors)))

    coordinates = sorted(all_divisors)
    coordinate_set = set(coordinates)
    if any(left not in coordinate_set or right not in coordinate_set
           for left, right in complement_pairs):
        raise AssertionError("complement coordinate missing")
    row_counts = {coordinate: 0 for coordinate in coordinates}
    column_counts = {coordinate: 0 for coordinate in coordinates}
    for left, right in complement_pairs:
        row_counts[left] += 1
        column_counts[right] += 1
    permutation_matrix = (
        set(row_counts.values()) == {1}
        and set(column_counts.values()) == {1}
    )
    if not permutation_matrix:
        raise AssertionError((row_counts, column_counts))

    contained_subpermanents: list[dict[str, list[int]]] = []
    overlap_histogram: dict[int, int] = {}
    for rows in itertools.combinations(range(6), 3):
        for columns in itertools.combinations(range(6), 3):
            permanent_monomials = set(PAIR.BASE.permanent_cubic(rows, columns))
            overlap = len(permanent_monomials.intersection(all_divisors))
            overlap_histogram[overlap] = overlap_histogram.get(overlap, 0) + 1
            if permanent_monomials.issubset(all_divisors):
                contained_subpermanents.append(
                    {"rows": list(rows), "columns": list(columns)}
                )
    expected_contained = [
        {"rows": [0, 1, 2], "columns": [0, 1, 2]},
        {"rows": [3, 4, 5], "columns": [3, 4, 5]},
    ]
    if contained_subpermanents != expected_contained:
        raise AssertionError(contained_subpermanents)
    if overlap_histogram != {0: 308, 1: 72, 2: 18, 6: 2}:
        raise AssertionError(overlap_histogram)

    return {
        "central_derivative_coordinate_count": len(coordinates),
        "six_term_central_catalectic_rank_over_Q": len(coordinates),
        "central_relation_dimension_rho": 0,
        "rank_certificate": (
            "the displayed 120 by 120 middle-catalectic matrix is a "
            "permutation matrix; every row and column has one unit entry"
        ),
        "certificate_minor_absolute_determinant": 1,
        "individual_chow_term_central_rank_cap": 20,
        "certified_chow_rank_lower_bound": 6,
        "displayed_chow_rank_upper_bound": 6,
        "exact_chow_rank": 6,
        "permanent_central_derivative_intersection_dimension_b": 2,
        "contained_three_by_three_subpermanents": contained_subpermanents,
        "subpermanent_support_overlap_histogram": {
            str(overlap): count for overlap, count in sorted(overlap_histogram.items())
        },
        "hypothetical_25_term_q6_required_minimum_b": 20,
        "compatible_with_q6_central_necessary_condition": False,
    }


def collision_certificate() -> dict[str, object]:
    base_blocks = PAIR.permanent_blocks()
    base_rank = sum(
        PAIR.exact_sparse_rank(columns) for columns in base_blocks.values()
    )
    if base_rank != 14_175:
        raise AssertionError(base_rank)

    full_permutations = [block_diagonal_permutation(p) for p in PERMUTATIONS]
    term_blocks = [PAIR.term_blocks(list(term_edges(p))) for p in PERMUTATIONS]

    collision_blocks: dict[PAIR.Weight, list[PAIR.SparseColumn]] = defaultdict(list)
    collision_labels: dict[PAIR.Weight, list[str]] = defaultdict(list)
    for label, rows, columns in (
        ("top", (0, 1, 2), (0, 1, 2)),
        ("bottom", (3, 4, 5), (3, 4, 5)),
    ):
        cubic_permanent = PAIR.BASE.permanent_cubic(rows, columns)
        for tensor_variable in range(PAIR.VARIABLES):
            weight = PAIR.permanent_weight(rows, columns, tensor_variable)
            collision_blocks[weight].append(
                PAIR.integer_delta_column(cubic_permanent, tensor_variable)
            )
            collision_labels[weight].append(label)

    all_weights = set(base_blocks) | set(collision_blocks)
    for blocks in term_blocks:
        all_weights.update(blocks)

    ordinary_span_rank = 0
    combined_rank = 0
    collision_rank = 0
    top_collision_rank = 0
    bottom_collision_rank = 0
    span_plus_collision_rank = 0
    base_plus_collision_rank = 0
    for weight in all_weights:
        term_columns: list[PAIR.SparseColumn] = []
        for blocks in term_blocks:
            term_columns.extend(blocks.get(weight, []))
        base_columns = base_blocks.get(weight, [])
        collision_columns = collision_blocks.get(weight, [])
        labels = collision_labels.get(weight, [])
        top_columns = [
            column for column, label in zip(collision_columns, labels)
            if label == "top"
        ]
        bottom_columns = [
            column for column, label in zip(collision_columns, labels)
            if label == "bottom"
        ]
        if term_columns:
            ordinary_span_rank += PAIR.exact_sparse_rank(term_columns)
        if base_columns or term_columns:
            combined_rank += PAIR.exact_sparse_rank(base_columns + term_columns)
        if collision_columns:
            collision_rank += PAIR.exact_sparse_rank(collision_columns)
        if top_columns:
            top_collision_rank += PAIR.exact_sparse_rank(top_columns)
        if bottom_columns:
            bottom_collision_rank += PAIR.exact_sparse_rank(bottom_columns)
        if term_columns or collision_columns:
            span_plus_collision_rank += PAIR.exact_sparse_rank(
                term_columns + collision_columns
            )
        if base_columns or collision_columns:
            base_plus_collision_rank += PAIR.exact_sparse_rank(
                base_columns + collision_columns
            )

    quotient_span_rank = combined_rank - base_rank
    internal_relations = 6 * 705 - ordinary_span_rank
    aggregate_collision = ordinary_span_rank - quotient_span_rank
    expected = {
        "ordinary_span_rank": 4_230,
        "quotient_span_rank": 4_158,
        "internal_relations": 0,
        "aggregate_collision": 72,
        "collision_rank": 72,
        "top_collision_rank": 36,
        "bottom_collision_rank": 36,
    }
    actual = {
        "ordinary_span_rank": ordinary_span_rank,
        "quotient_span_rank": quotient_span_rank,
        "internal_relations": internal_relations,
        "aggregate_collision": aggregate_collision,
        "collision_rank": collision_rank,
        "top_collision_rank": top_collision_rank,
        "bottom_collision_rank": bottom_collision_rank,
    }
    if actual != expected:
        raise AssertionError(actual)
    if span_plus_collision_rank != ordinary_span_rank:
        raise AssertionError((span_plus_collision_rank, ordinary_span_rank))
    if base_plus_collision_rank != base_rank:
        raise AssertionError((base_plus_collision_rank, base_rank))

    return {
        "six_permutations": [list(permutation) for permutation in full_permutations],
        "permanent_koszul_rank_over_Q": base_rank,
        "six_individual_koszul_rank_sum": 6 * 705,
        "ordinary_six_output_span_rank_over_Q": ordinary_span_rank,
        "quotient_six_output_span_rank_over_Q": quotient_span_rank,
        "internal_output_relation_dimension_eta": internal_relations,
        "aggregate_collision_dimension_j": aggregate_collision,
        "top_cubic_permanent_collision_rank_over_Q": top_collision_rank,
        "bottom_cubic_permanent_collision_rank_over_Q": bottom_collision_rank,
        "explicit_collision_direct_sum_rank_over_Q": collision_rank,
        "explicit_collision_is_full_intersection": True,
    }


def build_payload() -> dict[str, object]:
    payload = {
        "method": "pure middle-catalectic certificate plus exact rational torus-block elimination",
        "field": "Q",
        "family": (
            "sum over pi in S_3 of the top 3x3 permutation monomial times "
            "the identically indexed bottom 3x3 permutation monomial"
        ),
        **middle_catalectic_certificate(),
        **collision_certificate(),
        **normalized_fiber_classification(),
        "conclusion": (
            "A Chow-rank-six fixed sum can have rho=0, eta=0, and aggregate "
            "collision j=72 with im K_3(perm_6)."
        ),
        "scope": (
            "This disproves claims that minimum length, strict middle-"
            "catalectic minimality, or vanishing central/internal relations "
            "force aggregate quotient-Koszul transversality. It is not a "
            "25-term decomposition of perm_6 and does not change the 25..32 interval."
        ),
        "finite_field_or_random_input": False,
    }
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
