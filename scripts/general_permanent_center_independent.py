#!/usr/bin/env python3
"""Independent sparse-matrix replay of permanent Hessian centers.

This file imports none of the primary combinatorial audit.  For m=3 and m=4
it constructs the complete integer center equations and proves rank N^2-1
modulo a prime.  The scalar identity gives the matching characteristic-zero
kernel lower bound.
"""

from __future__ import annotations

from collections import defaultdict


PRIME = 1_000_003
Cell = tuple[int, int]
Label = tuple[tuple[int, int], tuple[int, int]]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def cell_list(m: int) -> list[Cell]:
    return [(i, j) for i in range(m) for j in range(m)]


def label(left: Cell, right: Cell) -> Label | None:
    if left[0] == right[0] or left[1] == right[1]:
        return None
    return (
        tuple(sorted((left[0], right[0]))),
        tuple(sorted((left[1], right[1]))),
    )


def center_rows(m: int) -> tuple[list[dict[int, int]], int]:
    cells = cell_list(m)
    variable_count = len(cells) ** 2
    rows: list[dict[int, int]] = []

    for x_index, x in enumerate(cells):
        for y_index in range(x_index + 1, len(cells)):
            y = cells[y_index]
            by_label: dict[Label, dict[int, int]] = defaultdict(dict)
            for z_index, z in enumerate(cells):
                left = label(x, z)
                if left is not None:
                    variable = z_index * len(cells) + y_index
                    by_label[left][variable] = by_label[left].get(variable, 0) + 1
                right = label(y, z)
                if right is not None:
                    variable = z_index * len(cells) + x_index
                    by_label[right][variable] = by_label[right].get(variable, 0) - 1
            for row in by_label.values():
                cleaned = {column: value for column, value in row.items() if value}
                if cleaned:
                    rows.append(cleaned)

    scalar = [0] * variable_count
    for cell_index in range(len(cells)):
        scalar[cell_index * len(cells) + cell_index] = 1
    for row in rows:
        require(
            sum(value * scalar[column] for column, value in row.items()) == 0,
            (m, row),
        )
    return rows, variable_count


def sparse_rank_mod(rows: list[dict[int, int]], prime: int) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for raw in rows:
        vector = {
            column: value % prime
            for column, value in raw.items()
            if value % prime
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(coefficient, prime - 2, prime)
                vector = {
                    column: value * inverse % prime
                    for column, value in vector.items()
                }
                pivots[pivot] = vector
                break
            for column, value in existing.items():
                updated = (vector.get(column, 0) - coefficient * value) % prime
                if updated:
                    vector[column] = updated
                else:
                    vector.pop(column, None)
    return len(pivots)


def main() -> int:
    for m in (3, 4):
        rows, variables = center_rows(m)
        rank = sparse_rank_mod(rows, PRIME)
        require(rank == variables - 1, (m, rank, variables))
        print(
            f"m={m} variables={variables} equations={len(rows)} "
            f"modular_rank={rank} center_dimension=1"
        )
    print("GENERAL_PERMANENT_CENTER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
