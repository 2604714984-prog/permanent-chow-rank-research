#!/usr/bin/env python3
"""Independent sparse modular replay for squarefree quotient Koszul homology."""

from __future__ import annotations

import argparse
from itertools import combinations

PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_mod(rows: list[list[int]], prime: int = PRIME) -> int:
    if not rows:
        return 0
    matrix = [[value % prime for value in row] for row in rows]
    height = len(matrix)
    width = len(matrix[0])
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, height) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], prime - 2, prime)
        matrix[rank] = [(value * inverse) % prime for value in matrix[rank]]
        for row in range(height):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[row], matrix[rank], strict=True)
            ]
        rank += 1
        if rank == height:
            break
    return rank


def quotient_matrices(n: int, d: int, kind: str) -> list[list[int]]:
    if kind == "coordinate":
        return [[1 if column == row else 0 for column in range(n)] for row in range(d)]
    if kind == "vandermonde":
        return [
            [pow(column + 1, row, PRIME) for column in range(n)]
            for row in range(d)
        ]
    if kind == "shifted":
        return [
            [pow(column + 2, row + 1, PRIME) + row + 1 for column in range(n)]
            for row in range(d)
        ]
    raise RuntimeError(kind)


def complex_ranks(n: int, k: int, quotient: list[list[int]]) -> tuple[int, int, int]:
    d = len(quotient)
    source = tuple(combinations(range(n), k + 1))
    middle_monomials = tuple(combinations(range(n), k))
    target_monomials = tuple(combinations(range(n), k - 1))
    wedge_pairs = tuple(combinations(range(d), 2))

    middle_index = {
        (a, monomial): index
        for index, (a, monomial) in enumerate(
            (pair for pair in __import__("itertools").product(range(d), middle_monomials))
        )
    }
    target_index = {
        (pair, monomial): index
        for index, (pair, monomial) in enumerate(
            __import__("itertools").product(wedge_pairs, target_monomials)
        )
    }

    d0 = [[0 for _ in source] for _ in middle_index]
    for column, monomial in enumerate(source):
        for removed in monomial:
            remainder = tuple(value for value in monomial if value != removed)
            for a in range(d):
                row = middle_index[(a, remainder)]
                d0[row][column] += quotient[a][removed]

    d1 = [[0 for _ in middle_index] for _ in target_index]
    for a in range(d):
        for monomial in middle_monomials:
            column = middle_index[(a, monomial)]
            for removed in monomial:
                remainder = tuple(value for value in monomial if value != removed)
                for b in range(d):
                    if a == b:
                        continue
                    if a < b:
                        pair = (a, b)
                        sign = 1
                    else:
                        pair = (b, a)
                        sign = -1
                    row = target_index[(pair, remainder)]
                    d1[row][column] += sign * quotient[b][removed]

    rank0 = rank_mod(d0)
    rank1 = rank_mod(d1)
    middle_dimension = d * len(middle_monomials)
    return rank0, rank1, middle_dimension - rank0 - rank1


def replay(max_n: int) -> dict[str, int]:
    checks = 0
    coordinate_equalities = 0
    noncoordinate_checks = 0
    for n in range(2, max_n + 1):
        for d in range(1, n + 1):
            cap_by_k = {
                k: d * __import__("math").comb(n - d, k - 1)
                if 0 <= k - 1 <= n - d
                else 0
                for k in range(1, n + 1)
            }
            for kind in ("coordinate", "vandermonde", "shifted"):
                quotient = quotient_matrices(n, d, kind)
                if rank_mod(quotient) != d:
                    continue
                for k in range(1, n + 1):
                    _, _, homology = complex_ranks(n, k, quotient)
                    require(homology <= cap_by_k[k], (n, d, k, kind, homology))
                    if kind == "coordinate":
                        require(homology == cap_by_k[k], (n, d, k, homology))
                        coordinate_equalities += 1
                    else:
                        noncoordinate_checks += 1
                    checks += 1
    return {
        "max_n": max_n,
        "checks": checks,
        "coordinate_equalities": coordinate_equalities,
        "noncoordinate_checks": noncoordinate_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=6)
    args = parser.parse_args()
    result = replay(args.max_n)
    print(result)
    print("GENERAL_SQUAREFREE_QUOTIENT_KOSZUL_HOMOLOGY_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
