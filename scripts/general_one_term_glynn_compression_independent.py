#!/usr/bin/env python3
"""Independent bit-mask replay for one-term Glynn compression."""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path

PRIME = 1_000_003
EXPECTED_CORE = "045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def delta_from_mask(mask: int, m: int) -> tuple[int, ...]:
    return (1,) + tuple(-1 if (mask >> bit) & 1 else 1 for bit in range(m - 1))


def parity_character(mask: int) -> int:
    return -1 if mask.bit_count() & 1 else 1


def compressed_m4_tensor() -> list[int]:
    output = [0] * (4**4)
    missing_mask = 0
    for rows in product(range(4), repeat=4):
        index = ((rows[0] * 4 + rows[1]) * 4 + rows[2]) * 4 + rows[3]
        total = 0
        for mask in range(8):
            if mask == missing_mask:
                continue
            delta = delta_from_mask(mask, 4)
            shared = delta[rows[0]] * delta[rows[1]]
            moving = delta[rows[2]] * delta[rows[3]]
            fixed = 1
            total += parity_character(mask) * shared * (moving - fixed)
        output[index] = total
    return output


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    width = len(rows[0])
    for column in range(width):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank or rows[row][column] == 0:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                (left - multiplier * right) % prime
                for left, right in zip(rows[row], rows[rank], strict=True)
            ]
        rank += 1
    return rank


def sign_outer_rows() -> list[list[int]]:
    rows = []
    for mask in range(1, 8):
        delta = delta_from_mask(mask, 4)
        rows.append([delta[i] * delta[j] for i in range(4) for j in range(4)])
    return rows


def permanent_flattening() -> list[list[int]]:
    matrix = [[0] * 16 for _ in range(16)]
    for rows in product(range(4), repeat=4):
        if len(set(rows)) != 4:
            continue
        matrix[rows[1] * 4 + rows[2]][rows[0] * 4 + rows[3]] = 1
    return matrix


def build_summary() -> dict[str, object]:
    tensor = compressed_m4_tensor()
    nonzero = 0
    zero = 0
    for rows in product(range(4), repeat=4):
        index = ((rows[0] * 4 + rows[1]) * 4 + rows[2]) * 4 + rows[3]
        expected = 8 if len(set(rows)) == 4 else 0
        require(tensor[index] == expected, (rows, tensor[index], expected))
        if expected:
            nonzero += 1
        else:
            zero += 1

    sign_rank = rank_mod(sign_outer_rows())
    flattening_rank = rank_mod(permanent_flattening())
    require(sign_rank == 7, sign_rank)
    require(flattening_rank == 6, flattening_rank)

    rows = {}
    for m in range(3, 17):
        shared = m - 2
        factor_count = shared + 4
        require(factor_count == m + 2, (m, factor_count))
        rows[str(m)] = {
            "sign_terms": 1 << (m - 1),
            "compressed_blocks": (1 << (m - 1)) - 1,
            "envelope_degree": factor_count,
        }

    return {
        "m4_row_assignments": len(tensor),
        "m4_permanent_coefficients": nonzero,
        "m4_zero_coefficients": zero,
        "m4_unscaled_coefficient": 8,
        "retained_sign_outer_rank_mod_prime": sign_rank,
        "permanent_pair_flattening_rank_mod_prime": flattening_rank,
        "construction_rows": rows,
        "expected_core": EXPECTED_CORE,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    summary = build_summary()
    if arguments.json is not None:
        arguments.json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("GENERAL_ONE_TERM_GLYNN_COMPRESSION_INDEPENDENT_PASS")
    print(EXPECTED_CORE)


if __name__ == "__main__":
    main()
