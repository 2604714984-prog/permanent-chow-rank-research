#!/usr/bin/env python3
"""Exact rational six-permutation aggregate-collision audit."""

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


def build_payload() -> dict[str, object]:
    base_blocks = PAIR.permanent_blocks()
    base_rank = sum(
        PAIR.exact_sparse_rank(columns) for columns in base_blocks.values()
    )
    if base_rank != 14_175:
        raise AssertionError(base_rank)

    permutations = []
    term_blocks = []
    for top_permutation in itertools.permutations(range(3)):
        permutation = tuple(top_permutation) + (3, 4, 5)
        permutations.append(permutation)
        edges = [row * 6 + permutation[row] for row in range(6)]
        term_blocks.append(PAIR.term_blocks(edges))

    collision_blocks: dict[PAIR.Weight, list[PAIR.SparseColumn]] = defaultdict(list)
    rows = (0, 1, 2)
    columns = (0, 1, 2)
    cubic_permanent = PAIR.BASE.permanent_cubic(rows, columns)
    for tensor_variable in range(PAIR.VARIABLES):
        weight = PAIR.permanent_weight(rows, columns, tensor_variable)
        collision_blocks[weight].append(
            PAIR.integer_delta_column(cubic_permanent, tensor_variable)
        )

    all_weights = set(base_blocks) | set(collision_blocks)
    for blocks in term_blocks:
        all_weights.update(blocks)

    ordinary_span_rank = 0
    combined_rank = 0
    collision_rank = 0
    span_plus_collision_rank = 0
    base_plus_collision_rank = 0
    for weight in all_weights:
        term_columns = []
        for blocks in term_blocks:
            term_columns.extend(blocks.get(weight, []))
        base_columns = base_blocks.get(weight, [])
        collision_columns = collision_blocks.get(weight, [])
        if term_columns:
            ordinary_span_rank += PAIR.exact_sparse_rank(term_columns)
        if base_columns or term_columns:
            combined_rank += PAIR.exact_sparse_rank(base_columns + term_columns)
        if collision_columns:
            collision_rank += PAIR.exact_sparse_rank(collision_columns)
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
    if collision_rank != 36:
        raise AssertionError(collision_rank)
    if span_plus_collision_rank != ordinary_span_rank:
        raise AssertionError((span_plus_collision_rank, ordinary_span_rank))
    if base_plus_collision_rank != base_rank:
        raise AssertionError((base_plus_collision_rank, base_rank))
    if aggregate_collision != collision_rank:
        raise AssertionError((aggregate_collision, collision_rank))

    return {
        "method": "exact-rational-row-column-torus-block-elimination",
        "field": "Q",
        "six_permutations": [list(permutation) for permutation in permutations],
        "common_complement_edges": [[3, 3], [4, 4], [5, 5]],
        "permanent_koszul_rank_over_Q": base_rank,
        "six_individual_rank_sum": 6 * 705,
        "ordinary_six_output_span_rank_over_Q": ordinary_span_rank,
        "quotient_six_output_span_rank_over_Q": quotient_span_rank,
        "internal_output_relation_dimension_eta": internal_relations,
        "aggregate_collision_dimension_j": aggregate_collision,
        "explicit_cubic_permanent_collision_rank_over_Q": collision_rank,
        "collision_subspace_contained_in_six_output_span": True,
        "collision_subspace_contained_in_permanent_output": True,
        "six_term_sum_has_chow_rank_upper_bound_four": True,
        "factorization": (
            "x_33*x_44*x_55*perm_3(rows 0,1,2; columns 0,1,2)"
        ),
        "conclusion": (
            "Six permutation monomials can have a 36-dimensional aggregate "
            "collision with im K_3(perm_6). This presentation is nonminimum, "
            "because its sum has a four-term Chow expression inherited from "
            "perm_3."
        ),
        "scope": (
            "This is a counterexample to unconditional six-term aggregate "
            "transversality, not a counterexample for minimum six-term "
            "decompositions."
        ),
    }


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
