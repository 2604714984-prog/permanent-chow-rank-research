#!/usr/bin/env python3
"""Exact replay for Packet-B subpacket obstruction monotonicity.

The theorem is linear-algebraic and is proved in the companion document. This
script performs two finite checks only:

1. exhaustive verification over F_2 for every three scalar-block system with
   two-dimensional source and target; and
2. exact propagation of the already-frozen two-transposition join defects.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
JOIN_DATA = ROOT / "data" / "n7_b2_two_transposition_join_obstruction.json"


def rank_mod(matrix: Sequence[Sequence[int]], prime: int) -> int:
    """Return the row rank over F_prime using deterministic elimination."""

    if prime <= 1:
        raise ValueError("prime must exceed one")
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(width):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank or rows[row][column] == 0:
                continue
            scale = rows[row][column]
            rows[row] = [
                (left - scale * right) % prime
                for left, right in zip(rows[row], rows[rank])
            ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def matrix_product_mod(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    prime: int,
) -> list[list[int]]:
    if not left:
        return []
    inner = len(left[0])
    if any(len(row) != inner for row in left):
        raise ValueError("ragged left matrix")
    if len(right) != inner:
        raise ValueError("incompatible matrix shapes")
    output_width = len(right[0]) if right else 0
    if any(len(row) != output_width for row in right):
        raise ValueError("ragged right matrix")
    return [
        [
            sum(left[row][middle] * right[middle][column] for middle in range(inner))
            % prime
            for column in range(output_width)
        ]
        for row in range(len(left))
    ]


def obstruction_dimension(
    b_matrix: Sequence[Sequence[int]],
    c_matrix: Sequence[Sequence[int]],
    prime: int,
) -> int:
    """Compute dim ker(B)/(ker(B) intersect im(C))."""

    middle_dimension = len(c_matrix)
    if b_matrix and len(b_matrix[0]) != middle_dimension:
        raise ValueError("B and C have incompatible middle dimensions")
    rank_b = rank_mod(b_matrix, prime)
    rank_c = rank_mod(c_matrix, prime)
    rank_bc = rank_mod(matrix_product_mod(b_matrix, c_matrix, prime), prime)
    defect = middle_dimension - rank_b - rank_c + rank_bc
    if defect < 0:
        raise ArithmeticError("negative obstruction dimension")
    return defect


def subset_matrices(
    blocks: Sequence[tuple[tuple[int, ...], tuple[int, ...]]],
    indices: Iterable[int],
) -> tuple[list[list[int]], list[list[int]]]:
    """Assemble B horizontally and C vertically for scalar middle blocks."""

    selected = tuple(indices)
    if not selected:
        raise ValueError("the selected subpacket must be nonempty")
    target_dimension = len(blocks[0][1])
    source_dimension = len(blocks[0][0])
    if any(
        len(c_row) != source_dimension or len(b_column) != target_dimension
        for c_row, b_column in blocks
    ):
        raise ValueError("inconsistent block dimensions")
    b_matrix = [
        [blocks[index][1][row] for index in selected]
        for row in range(target_dimension)
    ]
    c_matrix = [list(blocks[index][0]) for index in selected]
    return b_matrix, c_matrix


def exhaustive_scalar_block_replay() -> dict[str, int]:
    """Exhaust all 3-block systems over F_2 and all strict subset pairs."""

    prime = 2
    source_dimension = 2
    target_dimension = 2
    block_count = 3
    vectors = tuple(itertools.product(range(prime), repeat=source_dimension))
    columns = tuple(itertools.product(range(prime), repeat=target_dimension))
    block_types = tuple(itertools.product(vectors, columns))
    nonempty_subsets = tuple(
        subset
        for size in range(1, block_count + 1)
        for subset in itertools.combinations(range(block_count), size)
    )
    strict_pairs = tuple(
        (small, large)
        for small in nonempty_subsets
        for large in nonempty_subsets
        if len(small) < len(large) and set(small).issubset(large)
    )

    systems_checked = 0
    inequalities_checked = 0
    maximum_increase = 0
    for blocks in itertools.product(block_types, repeat=block_count):
        systems_checked += 1
        defects: dict[tuple[int, ...], int] = {}
        for subset in nonempty_subsets:
            b_matrix, c_matrix = subset_matrices(blocks, subset)
            defects[subset] = obstruction_dimension(b_matrix, c_matrix, prime)
        for small, large in strict_pairs:
            inequalities_checked += 1
            increase = defects[large] - defects[small]
            if increase < 0:
                raise ArithmeticError(
                    f"subpacket obstruction decreased for {small} subset {large}: "
                    f"{defects[small]} -> {defects[large]}"
                )
            maximum_increase = max(maximum_increase, increase)

    expected_systems = len(block_types) ** block_count
    expected_inequalities = expected_systems * len(strict_pairs)
    if systems_checked != expected_systems or inequalities_checked != expected_inequalities:
        raise ArithmeticError("exhaustive replay count mismatch")
    return {
        "prime": prime,
        "source_dimension": source_dimension,
        "target_dimension": target_dimension,
        "block_count": block_count,
        "block_types": len(block_types),
        "systems_checked": systems_checked,
        "strict_subset_pairs_per_system": len(strict_pairs),
        "inequalities_checked": inequalities_checked,
        "violations": 0,
        "maximum_observed_increase": maximum_increase,
    }


def canonical_join_corollary(join_data_path: Path = JOIN_DATA) -> dict[str, object]:
    payload = json.loads(join_data_path.read_text(encoding="utf-8"))
    canonical = payload["canonical_half_half_ranks"]
    expected = {
        "shared_row_01_02": 10,
        "disjoint_01_23": 12,
    }
    answer: dict[str, object] = {}
    for name, expected_defect in expected.items():
        row = canonical[name]
        defect = (
            int(row["middle_dimension"])
            - int(row["rank_B"])
            - int(row["rank_C"])
            + int(row["rank_BC"])
        )
        if defect != expected_defect or int(row["kernel_image_defect"]) != expected_defect:
            raise ArithmeticError(("unexpected frozen join defect", name, row))
        answer[name] = {
            "middle_dimension": int(row["middle_dimension"]),
            "rank_B": int(row["rank_B"]),
            "rank_C": int(row["rank_C"]),
            "rank_BC": int(row["rank_BC"]),
            "subpacket_obstruction_dimension": defect,
            "minimum_obstruction_in_every_completion": defect,
            "completion_to_sylvester_equality_possible": False,
        }
    return answer


def build_payload(join_data_path: Path = JOIN_DATA) -> dict[str, object]:
    return {
        "schema_version": 1,
        "status": "SUBPACKET_OBSTRUCTION_MONOTONICITY_PROVED_AND_JOIN_COROLLARIES_REPLAYED",
        "theorem": {
            "obstruction_space": "O_I = ker(B_I) / (ker(B_I) intersect im(C_I))",
            "dimension_formula": "dim O_I = dim K_I - rank(B_I) - rank(C_I) + rank(B_I C_I)",
            "monotonicity": "For I subset J, zero extension induces an injection O_I -> O_J.",
            "increment_inequality": "If the added middle dimension is s, then Delta_B + Delta_C - Delta_BC <= s.",
            "rank_seven_fifth_term_cap": 35,
            "former_shared_repair_target": 45,
            "former_disjoint_repair_target": 47,
            "full_equality_consequence": "If O_J=0, then O_I=0 for every term subpacket I subset J.",
            "field_scope": "arbitrary field",
        },
        "finite_field_replay": exhaustive_scalar_block_replay(),
        "canonical_two_transposition_join_corollary": canonical_join_corollary(join_data_path),
        "superseded_statement": "The frozen v1 join packet said a positive subpacket defect might be repaired by later term blocks. Subpacket obstruction monotonicity proves that statement false.",
        "claim_boundary": [
            "The theorem applies to direct-sum middle spaces with common source and target maps, including the labelled Packet-B maps.",
            "Source enlargement from a local variable space W to the ambient V does not change the image of an old term block because restriction Sym^3(V*) -> Sym^3(W*) is surjective.",
            "The canonical shared-row and disjoint two-transposition joins are globally noncompletable in any larger Packet-B equality packet.",
            "This does not classify noncanonical four-term factorizations or cross-slice graph couplings whose four-term obstruction already vanishes.",
            "No full B2-CLOSED, lower-50, exact perm_7, or border-rank claim is made.",
        ],
        "next_exact_gate": "Classify zero-defect four-term cross-slice couplings. Any positive four-term defect is already globally fatal and must not be sent to additional-term completion tests.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    parser.add_argument("--join-data", type=Path, default=JOIN_DATA)
    args = parser.parse_args()
    payload = build_payload(args.join_data)
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 B2 subpacket obstruction monotonicity JSON mismatch")
        print("PASS n7 B2 subpacket obstruction monotonicity")
        return
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
