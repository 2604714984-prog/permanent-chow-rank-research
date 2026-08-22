#!/usr/bin/env python3
"""Exact tangent-rank audit for the 64-term Glynn decomposition of perm_7."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_glynn_tangent_nonredundancy.json"
PRIME = 1_000_003
N = 7
CHARACTERS = 2 ** (N - 1)
ROW_BITS = (0, 1, 2, 4, 8, 16, 32)


def add_sparse_row(pivots: dict[int, dict[int, int]], raw: dict[int, int]) -> None:
    row = {index: value % PRIME for index, value in raw.items() if value % PRIME}
    while row:
        pivot = min(row)
        old = pivots.get(pivot)
        if old is None:
            inverse = pow(row[pivot], PRIME - 2, PRIME)
            pivots[pivot] = {
                index: value * inverse % PRIME for index, value in row.items()
            }
            return
        factor = row[pivot]
        for index, value in old.items():
            updated = (row.get(index, 0) - factor * value) % PRIME
            if updated:
                row[index] = updated
            else:
                row.pop(index, None)


def row_for_mask(mask: int) -> int | None:
    if mask == 0:
        return 0
    if mask & (mask - 1):
        return None
    return mask.bit_length()


def base_block_rank(parity_weight: int) -> dict[str, int]:
    """Rank for the all-columns-once multidegree at a canonical Walsh parity."""
    mask = (1 << parity_weight) - 1
    theoretical_upper = 37 if parity_weight == 6 else 43
    pivots: dict[int, dict[int, int]] = {}
    accepted_rows = 0
    for first_six in product(range(N), repeat=N - 1):
        parity = 0
        for row in first_six:
            parity ^= ROW_BITS[row]
        last = row_for_mask(mask ^ parity)
        if last is None:
            continue
        rows = (*first_six, last)
        accepted_rows += 1
        add_sparse_row(
            pivots,
            {column * N + row: 1 for column, row in enumerate(rows)},
        )
        if len(pivots) == theoretical_upper:
            break
    if len(pivots) != theoretical_upper:
        raise AssertionError((parity_weight, len(pivots), theoretical_upper))
    return {
        "parity_weight": parity_weight,
        "modular_rank_lower_bound": len(pivots),
        "theoretical_rank_upper_bound": theoretical_upper,
        "witness_rows_scanned": accepted_rows,
    }


def off_diagonal_block_ranks() -> list[int]:
    """Ranks for one missing-column/doubled-column multidegree."""
    reachable_rest_parities: set[int] = set()
    for rows in product(range(N), repeat=N - 2):
        parity = 0
        for row in rows:
            parity ^= ROW_BITS[row]
        reachable_rest_parities.add(parity)
    if len(reachable_rest_parities) != 63:
        raise AssertionError(len(reachable_rest_parities))

    ranks = []
    for total_parity in range(CHARACTERS):
        pivots: dict[int, dict[int, int]] = {}
        for left, right in combinations_with_replacement(range(N), 2):
            required = total_parity ^ ROW_BITS[left] ^ ROW_BITS[right]
            if required not in reachable_rest_parities:
                continue
            vector = {left: 1} if left == right else {left: 1, right: 1}
            add_sparse_row(pivots, vector)
        ranks.append(len(pivots))
    return ranks


def build_payload() -> dict[str, object]:
    base_representatives = [base_block_rank(weight) for weight in range(N)]
    base_rank = sum(
        comb(N - 1, row["parity_weight"]) * row["modular_rank_lower_bound"]
        for row in base_representatives
    )
    off_ranks = off_diagonal_block_ranks()
    off_rank = sum(off_ranks)
    off_multidegrees = N * (N - 1)
    tangent_rank = base_rank + off_multidegrees * off_rank

    tangent_dimension_per_term = 1 + N * (N * N - 1)
    effective_source_dimension = CHARACTERS * tangent_dimension_per_term
    extra_kernel = effective_source_dimension - tangent_rank

    assert base_rank == 2_746
    assert {row["modular_rank_lower_bound"] for row in base_representatives[:-1]} == {43}
    assert base_representatives[-1]["modular_rank_lower_bound"] == 37
    assert off_ranks == [7] * CHARACTERS
    assert off_rank == 448
    assert tangent_rank == 21_562
    assert effective_source_dimension == 21_568
    assert extra_kernel == N - 1

    return {
        "status": "N7_GLYNN_LOCAL_RIGIDITY",
        "field": "characteristic zero, certified by a nonzero modular minor",
        "prime": PRIME,
        "glynn_term_count": CHARACTERS,
        "ambient_variable_count": N * N,
        "affine_chow_tangent_dimension_per_term": tangent_dimension_per_term,
        "effective_source_dimension_after_intrinsic_factor_gauge": effective_source_dimension,
        "walsh_blocks": {
            "base_multidegree_representatives_by_parity_weight": base_representatives,
            "base_multidegree_total_rank": base_rank,
            "off_diagonal_multidegree_count": off_multidegrees,
            "one_off_diagonal_multidegree_rank": off_rank,
            "off_diagonal_parity_ranks": off_ranks,
        },
        "sum_map_tangent_rank": tangent_rank,
        "kernel_after_intrinsic_factor_gauge": extra_kernel,
        "identified_kernel": {
            "dimension": N - 1,
            "source": "row-diagonal torus stabilizing perm_7",
        },
        "conclusion": (
            "The ordered decomposition fiber is smooth of dimension six at the Glynn point; "
            "locally it is exactly the row-diagonal stabilizer orbit. After quotienting that "
            "orbit, the point is isolated and reduced."
        ),
        "claim_boundary": [
            "This is local rigidity of the Glynn decomposition modulo its stabilizer.",
            "It does not prove that no unrelated 63-term decomposition exists.",
            "It does not prove ordinary or border Chow rank 64.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise SystemExit("frozen payload mismatch")
        print("PASS: n7 Glynn tangent payload matches")
        return 0
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
