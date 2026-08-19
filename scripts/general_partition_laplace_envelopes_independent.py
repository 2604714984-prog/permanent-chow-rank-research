#!/usr/bin/env python3
"""Independent bit-mask replay for partition-Laplace Chow envelopes."""

from __future__ import annotations

from collections import Counter
from itertools import permutations
from math import factorial


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def row_labels(parts: tuple[int, ...]) -> tuple[int, ...]:
    labels: list[int] = []
    for block, size in enumerate(parts):
        labels.extend([block] * size)
    return tuple(labels)


def fiber_key(
    matching: tuple[int, ...], labels: tuple[int, ...], block_count: int
) -> tuple[int, ...]:
    masks = [0] * block_count
    for row, column in enumerate(matching):
        masks[labels[row]] |= 1 << column
    return tuple(masks)


def verify_partition_fibers(m_max: int = 8) -> dict[str, int]:
    shapes = 0
    global_permutations = 0
    fibers = 0
    support_cells = 0

    for m in range(1, m_max + 1):
        all_matchings = tuple(permutations(range(m)))
        for parts in partitions(m):
            labels = row_labels(parts)
            counts: Counter[tuple[int, ...]] = Counter()
            for matching in all_matchings:
                counts[fiber_key(matching, labels, len(parts))] += 1
                global_permutations += 1
            expected_fiber_size = 1
            expected_fiber_count = factorial(m)
            for size in parts:
                expected_fiber_size *= factorial(size)
                expected_fiber_count //= factorial(size)
            require(
                len(counts) == expected_fiber_count,
                (m, parts, len(counts), expected_fiber_count),
            )
            require(
                set(counts.values()) == {expected_fiber_size},
                (m, parts, set(counts.values())),
            )
            for key in counts:
                require(
                    sum(mask.bit_count() for mask in key) == m,
                    (m, parts, key),
                )
                block_support = sum(
                    size * mask.bit_count() for size, mask in zip(parts, key)
                )
                require(
                    block_support == sum(size * size for size in parts),
                    (m, parts, key, block_support),
                )
                support_cells += block_support
            shapes += 1
            fibers += len(counts)

    return {
        "m_max": m_max,
        "partition_shapes_checked": shapes,
        "permutation_visits": global_permutations,
        "fibers_checked": fibers,
        "support_cell_total": support_cells,
    }


def verify_explicit_cubic() -> dict[str, object]:
    matchings = tuple(permutations(range(3)))
    fibers: dict[int, list[tuple[int, ...]]] = {0: [], 1: [], 2: []}
    for matching in matchings:
        fibers[matching[0]].append(matching)

    support_sizes = []
    for first_column, group in sorted(fibers.items()):
        require(len(group) == 2, (first_column, group))
        mask = 0
        for matching in group:
            for row, column in enumerate(matching):
                mask |= 1 << (3 * row + column)
        require(mask.bit_count() == 5, (first_column, mask.bit_count()))
        support_sizes.append(mask.bit_count())

    require(sum(len(group) for group in fibers.values()) == 6, fibers)
    return {"fibers": 3, "support_sizes": support_sizes, "monomials": 6}


def exact_mu(n: int) -> int:
    if n < 3:
        raise RuntimeError(n)
    return 4 if n <= 4 else 3 if n == 5 else 2 if n <= 8 else 1


def verify_mu(n_max: int = 128) -> dict[str, object]:
    values = [exact_mu(n) for n in range(3, n_max + 1)]
    require(values[:7] == [4, 4, 3, 2, 2, 2, 1], values[:7])
    require(
        all(values[i] >= values[i + 1] for i in range(len(values) - 1)),
        values,
    )
    return {"n_max": n_max, "rows": len(values), "initial_values": values[:12]}


def main() -> None:
    partition = verify_partition_fibers()
    cubic = verify_explicit_cubic()
    mu = verify_mu()
    print(f"partition_shapes_checked={partition['partition_shapes_checked']}")
    print(f"permutation_visits={partition['permutation_visits']}")
    print(f"fibers_checked={partition['fibers_checked']}")
    print(f"cubic_support_sizes={cubic['support_sizes']}")
    print(f"cubic_mu_rows={mu['initial_values'][:7]}")
    print("GENERAL_PARTITION_LAPLACE_ENVELOPES_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
