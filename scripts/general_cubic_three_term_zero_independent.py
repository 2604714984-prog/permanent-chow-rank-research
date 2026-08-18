#!/usr/bin/env python3
"""Independent replay for the cubic three-term zero theorem.

This file imports none of the primary audit.  It independently enumerates the
integer private-polar state and exhausts all disjoint-support two-plane tensor
configurations over F_2.  The finite-field enumeration is a regression for the
pure characteristic-zero tensor-plane lemma, not a transfer of a finite-field
nonexistence statement.
"""

from __future__ import annotations

from itertools import product


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_bits(vectors: list[int]) -> int:
    pivots: dict[int, int] = {}
    result = 0
    for value in vectors:
        current = value
        while current:
            pivot = current.bit_length() - 1
            if pivot in pivots:
                current ^= pivots[pivot]
            else:
                pivots[pivot] = current
                result += 1
                break
    return result


def rref_rows_f2(rows: tuple[int, int]) -> tuple[int, int]:
    values = list(rows)
    for pivot in range(3, -1, -1):
        candidates = [index for index, value in enumerate(values) if (value >> pivot) & 1]
        if not candidates:
            continue
        selected = candidates[0]
        values[0], values[selected] = values[selected], values[0]
        for index in range(1, len(values)):
            if (values[index] >> pivot) & 1:
                values[index] ^= values[0]
        if len(values) == 2 and values[1]:
            break
    values = sorted(values, reverse=True)
    require(rank_bits(values) == 2, values)
    return values[0], values[1]


def disjoint_support_planes() -> list[tuple[int, int]]:
    planes: set[tuple[int, int]] = set()
    for left in range(1, 16):
        for right in range(1, 16):
            if left & right:
                continue
            if rank_bits([left, right]) != 2:
                continue
            planes.add(rref_rows_f2((left, right)))
    result = sorted(planes)
    require(len(result) == 25, len(result))
    return result


def tensor_plane(left: tuple[int, int], right: tuple[int, int]) -> list[int]:
    vectors: list[int] = []
    for row in left:
        for column in right:
            value = 0
            for i in range(4):
                if not ((row >> i) & 1):
                    continue
                for j in range(4):
                    if (column >> j) & 1:
                        value ^= 1 << (4 * i + j)
            vectors.append(value)
    require(rank_bits(vectors) == 4, (left, right, vectors))
    return vectors


def independent_private_state() -> tuple[int, int, tuple[int, int, int], tuple[int, int, int]]:
    survivors = []
    for r1, r2, r3 in product(range(1, 5), repeat=3):
        total = r1 + r2 + r3
        for defect in range(4):
            ambient = total - defect
            if ambient < 9:
                continue
            for t1, t2, t3 in product(range(4), repeat=3):
                ranks = (r1, r2, r3)
                overlaps = (t1, t2, t3)
                if any(overlaps[i] > min(ranks[i], defect) for i in range(3)):
                    continue
                private = tuple(ranks[i] - overlaps[i] for i in range(3))
                if any(value not in (0, 1) for value in private):
                    continue
                if sum(private) < ambient - 2 * defect:
                    continue
                survivors.append((ambient, defect, ranks, overlaps, private))
    require(
        survivors == [(9, 3, (4, 4, 4), (3, 3, 3), (1, 1, 1))],
        survivors,
    )
    ambient, defect, ranks, overlaps, _ = survivors[0]
    return ambient, defect, ranks, overlaps


def main() -> None:
    ambient, defect, ranks, overlaps = independent_private_state()

    support_planes = disjoint_support_planes()
    tensor_spaces: list[list[int]] = []
    for row_plane in support_planes:
        for column_plane in support_planes:
            tensor_spaces.append(tensor_plane(row_plane, column_plane))
    require(len(tensor_spaces) == 625, len(tensor_spaces))

    adjacency = [set() for _ in tensor_spaces]
    disjoint_pairs = 0
    for first in range(len(tensor_spaces)):
        for second in range(first + 1, len(tensor_spaces)):
            if rank_bits(tensor_spaces[first] + tensor_spaces[second]) == 8:
                adjacency[first].add(second)
                adjacency[second].add(first)
                disjoint_pairs += 1

    totals: set[int] = set()
    triple_count = 0
    for first in range(len(tensor_spaces)):
        later = {index for index in adjacency[first] if index > first}
        for second in sorted(later):
            common = later.intersection(adjacency[second])
            for third in common:
                if third <= second:
                    continue
                total_dimension = rank_bits(
                    tensor_spaces[first]
                    + tensor_spaces[second]
                    + tensor_spaces[third]
                )
                totals.add(total_dimension)
                triple_count += 1

    require(totals == {8, 10, 12}, totals)
    require(9 not in totals, totals)
    require(disjoint_pairs == 132_300, disjoint_pairs)
    require(triple_count == 12_510_100, triple_count)

    print(f"private_ambient_dimension={ambient}")
    print(f"private_relation_defect={defect}")
    print(f"private_component_ranks={ranks}")
    print(f"private_overlap_dimensions={overlaps}")
    print(f"support_two_planes={len(support_planes)}")
    print(f"tensor_product_planes={len(tensor_spaces)}")
    print(f"pairwise_disjoint_pairs={disjoint_pairs}")
    print(f"pairwise_disjoint_triples={triple_count}")
    print(f"observed_total_dimensions={sorted(totals)}")
    print("GENERAL_CUBIC_THREE_TERM_ZERO_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
