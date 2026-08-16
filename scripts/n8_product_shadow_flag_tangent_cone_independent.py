#!/usr/bin/env python3
"""Independent modular replay for the n=8 flag tangent-cone interface.

This script does not import the primary tangent enumerator.  It constructs the
27 semantic elementary graph directions directly and compares their exact
integer derivative matrices modulo 1,000,003.  Modular ranks are cross-checks
only; the characteristic-zero tangent and obstruction statements are proved
by the primary combinatorial factorization and the companion note.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

N = 8
K = 4
Z = 7
U = tuple(range(7))
V = tuple(range(6))
C0 = (0, 1, 2, 3)
EXTERNAL = (6, 7)
INTERNAL = (4, 5)
PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def replace(subset: tuple[int, ...], old: int, new: int) -> tuple[int, ...]:
    return tuple(sorted((set(subset) - {old}) | {new}))


def label(kind: str, source: int, target: int) -> str:
    return f"{ {'ambient':'A','row':'R','line':'L'}[kind] }{source}to{target}"


def reference_family() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    layer = list(combinations(range(N), K))
    high_rows = [row for row in layer if Z not in row]
    low_rows = [row for row in layer if Z in row]
    high_columns = [column for column in layer if set(column) <= set(V)]
    family = {(row, column) for row in high_rows for column in high_columns}
    family |= {(row, C0) for row in low_rows}
    result = sorted(family)
    require(len(result) == 560, len(result))
    return result


def semantic_directions(
    family: list[tuple[tuple[int, ...], tuple[int, ...]]]
) -> dict[str, dict[int, tuple[tuple[int, ...], tuple[int, ...]]]]:
    family_set = set(family)
    directions: dict[str, dict[int, tuple[tuple[int, ...], tuple[int, ...]]]] = {}

    for source in V:
        for target in EXTERNAL:
            current = {}
            for index, (row, column) in enumerate(family):
                if source in column and target not in column:
                    outside = (row, replace(column, source, target))
                    if outside not in family_set:
                        current[index] = outside
            directions[label("ambient", source, target)] = current

    for source in U:
        current = {}
        for index, (row, column) in enumerate(family):
            if source in row and Z not in row:
                outside = (replace(row, source, Z), column)
                if outside not in family_set:
                    current[index] = outside
        directions[label("row", source, Z)] = current

    for source in C0:
        for target in INTERNAL:
            current = {}
            for index, (row, column) in enumerate(family):
                if Z in row and column == C0:
                    current[index] = (row, replace(C0, source, target))
            directions[label("line", source, target)] = current

    require(len(directions) == 27, len(directions))
    require(
        Counter(len(value) for value in directions.values())
        == Counter({385: 8, 350: 4, 280: 7, 35: 8}),
        {key: len(value) for key, value in directions.items()},
    )
    return directions


def sparse_rank(columns: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for raw in columns:
        column = {key: value % PRIME for key, value in raw.items() if value % PRIME}
        while column:
            pivot = min(column)
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(column[pivot], PRIME - 2, PRIME)
                pivots[pivot] = {
                    key: value * inverse % PRIME for key, value in column.items()
                }
                break
            coefficient = column[pivot]
            for key, value in existing.items():
                updated = (column.get(key, 0) - coefficient * value) % PRIME
                if updated:
                    column[key] = updated
                else:
                    column.pop(key, None)
    return len(pivots)


def derivative_rank(
    family: list[tuple[tuple[int, ...], tuple[int, ...]]],
    directions: dict[str, dict[int, tuple[tuple[int, ...], tuple[int, ...]]]],
    coefficients: dict[str, int],
) -> int:
    lower = list(combinations(range(N), K - 1))
    lower_id = {
        (row, column): row_index * len(lower) + column_index
        for row_index, row in enumerate(lower)
        for column_index, column in enumerate(lower)
    }
    by_family: dict[int, list[tuple[tuple[int, ...], tuple[int, ...], int]]] = defaultdict(list)
    for direction_label, coefficient in coefficients.items():
        for family_index, (row, column) in directions[direction_label].items():
            by_family[family_index].append((row, column, coefficient))

    columns = []
    for family_index, (row, column) in enumerate(family):
        additions = by_family.get(family_index, ())
        for i in range(N):
            for j in range(N):
                vector: dict[int, int] = {}
                if i in row and j in column:
                    lower_pair = (
                        tuple(value for value in row if value != i),
                        tuple(value for value in column if value != j),
                    )
                    vector[lower_id[lower_pair]] = 1
                for new_row, new_column, coefficient in additions:
                    if i in new_row and j in new_column:
                        lower_pair = (
                            tuple(value for value in new_row if value != i),
                            tuple(value for value in new_column if value != j),
                        )
                        index = lower_id[lower_pair]
                        vector[index] = vector.get(index, 0) + coefficient
                if vector:
                    columns.append(vector)
    return sparse_rank(columns)


def maximal_components() -> list[tuple[str, ...]]:
    components = []
    for source in C0:
        components.append(
            tuple(
                sorted(
                    (
                        label("ambient", source, 6),
                        label("ambient", source, 7),
                        label("line", source, 4),
                        label("line", source, 5),
                    )
                )
            )
        )
    for line_source in C0:
        components.append(
            tuple(
                sorted(
                    (
                        label("ambient", 4, 6),
                        label("ambient", 4, 7),
                        label("line", line_source, 5),
                    )
                )
            )
        )
        components.append(
            tuple(
                sorted(
                    (
                        label("ambient", 5, 6),
                        label("ambient", 5, 7),
                        label("line", line_source, 4),
                    )
                )
            )
        )
    for source in U:
        components.append((label("row", source, Z),))
    return sorted(set(components), key=lambda value: (len(value), value))


def main() -> int:
    family = reference_family()
    directions = semantic_directions(family)
    components = maximal_components()
    expected_edges = {
        tuple(sorted((left, right)))
        for component in components
        for left, right in combinations(component, 2)
    }
    require(len(expected_edges) == 42, len(expected_edges))

    for direction_label in sorted(directions):
        rank = derivative_rank(family, directions, {direction_label: 2})
        require(rank == 784, (direction_label, rank))

    observed_edges = set()
    pair_rank_histogram = Counter()
    for left, right in combinations(sorted(directions), 2):
        rank = derivative_rank(family, directions, {left: 2, right: 3})
        pair_rank_histogram[rank] += 1
        if rank == 784:
            observed_edges.add((left, right))
    require(observed_edges == expected_edges, (observed_edges, expected_edges))

    coefficients = (2, 3, 5, 7)
    for component in components:
        assignment = {
            direction_label: coefficients[index]
            for index, direction_label in enumerate(component)
        }
        rank = derivative_rank(family, directions, assignment)
        require(rank == 784, (component, rank))

    print("independent_tangent_direction_count=27")
    print("independent_compatible_pair_count=42")
    print("independent_maximal_component_count=19")
    print(f"independent_pair_rank_histogram={dict(sorted(pair_rank_histogram.items()))}")
    print("N8_PRODUCT_SHADOW_TANGENT_CONE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
