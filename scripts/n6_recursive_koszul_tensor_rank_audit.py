#!/usr/bin/env python3
"""Independent exact replay of the order-six permanent recursive flattening.

The script reconstructs the 162000-by-162000 integer matrix for
``(perm_6)^{wedge(1,2,3,4)}`` directly from the definition.  It does not read
the upstream Matlab orbit matrix or any precomputed rank data.

Logical direction:

* matrix entries are integers;
* a modular rank is a characteristic-zero rank lower bound;
* a rank-one tensor has flattening rank 2500;
* determinantal rank loci are closed, so the quotient also lower-bounds border
  tensor rank.

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import struct
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterator

N = 6
MATRIX_DIMENSION = 162_000
PERMUTATION_COUNT = math.factorial(N)
NONZEROS_PER_PERMUTATION = 2_500
EXPECTED_GENERATED_ENTRIES = PERMUTATION_COUNT * NONZEROS_PER_PERMUTATION
RANK_ONE_NORMALIZATION = 2_500
PRIMES = (1_000_003, 1_000_033)
EXPECTED_EDGE_SHA256 = (
    "b06ddee0d9573b2b20e82fb75aa738a5d505190412c15a78959ea63f0aa500f1"
)
EXPECTED_COMPONENT_HISTOGRAM = {
    (1, 1): 720,
    (3, 2): 480,
    (8, 5): 540,
    (9, 4): 20,
    (21, 12): 360,
    (49, 24): 240,
    (55, 29): 180,
    (110, 46): 12,
    (125, 58): 120,
    (276, 118): 180,
    (590, 225): 60,
    (1236, 434): 20,
}
EXPECTED_COMPONENT_COUNT = 2_932
EXPECTED_TOTAL_RANK = 70_692

Edge = tuple[int, int, int]


class UnionFind:
    """Small iterative union-find for the bipartite support graph."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, value: int) -> int:
        parent = self.parent
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        if self.size[left] < self.size[right]:
            left, right = right, left
        self.parent[right] = left
        self.size[left] += self.size[right]


def exterior_data() -> tuple[dict[int, list[tuple[int, ...]]], dict[tuple[int, int], list[tuple[int, int, int]]]]:
    subsets = {
        degree: list(itertools.combinations(range(N), degree))
        for degree in range(1, N)
    }
    indices = {
        degree: {subset: index for index, subset in enumerate(subsets[degree])}
        for degree in subsets
    }
    wedge: dict[tuple[int, int], list[tuple[int, int, int]]] = {}
    for degree in range(1, N - 1):
        for basis_value in range(N):
            transitions: list[tuple[int, int, int]] = []
            for source_index, source in enumerate(subsets[degree]):
                if basis_value in source:
                    continue
                target = tuple(sorted((basis_value,) + source))
                sign = -1 if sum(value < basis_value for value in source) % 2 else 1
                transitions.append(
                    (source_index, indices[degree + 1][target], sign)
                )
            expected = math.comb(N - 1, degree)
            if len(transitions) != expected:
                raise AssertionError((degree, basis_value, len(transitions), expected))
            wedge[(degree, basis_value)] = transitions
    return subsets, wedge


_SUBSETS, _WEDGE = exterior_data()


def matrix_edges() -> Iterator[Edge]:
    """Yield the canonical integer entries as ``(row, column, sign)``."""

    for sigma in itertools.permutations(range(N)):
        s1, s2, s3, s4, s5, s6 = sigma
        for first in _WEDGE[(1, s1)]:
            i1, j1, z1 = first
            for second in _WEDGE[(2, s2)]:
                i2, j2, z2 = second
                for third in _WEDGE[(3, s3)]:
                    i3, j3, z3 = third
                    for fourth in _WEDGE[(4, s4)]:
                        i4, j4, z4 = fourth
                        column = ((((i1 * 15 + i2) * 20 + i3) * 15 + i4) * 6 + s5)
                        row = ((((j1 * 20 + j2) * 15 + j3) * 6 + j4) * 6 + s6)
                        yield row, column, z1 * z2 * z3 * z4


def sparse_rank_mod(
    rows: list[int],
    row_entries: list[dict[int, int]],
    prime: int,
) -> int:
    """Sparse exact row-echelon rank over ``F_prime``."""

    pivots: dict[int, dict[int, int]] = {}
    for row_index in sorted(rows, key=lambda index: (len(row_entries[index]), index)):
        vector = {
            column: value % prime
            for column, value in row_entries[row_index].items()
            if value % prime
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                if coefficient != 1:
                    inverse = pow(coefficient, prime - 2, prime)
                    vector = {
                        column: value * inverse % prime
                        for column, value in vector.items()
                    }
                pivots[pivot] = vector
                break
            for column, value in existing.items():
                updated = (
                    vector.get(column, 0) - coefficient * value
                ) % prime
                if updated:
                    vector[column] = updated
                else:
                    vector.pop(column, None)
    return len(pivots)


def build_support_graph() -> tuple[
    list[dict[int, int]],
    dict[int, list[int]],
    dict[int, list[int]],
    str,
    int,
]:
    union_find = UnionFind(2 * MATRIX_DIMENSION)
    digest = hashlib.sha256()
    generated = 0

    for row, column, sign in matrix_edges():
        union_find.union(row, MATRIX_DIMENSION + column)
        digest.update(struct.pack("<IIb", row, column, sign))
        generated += 1

    if generated != EXPECTED_GENERATED_ENTRIES:
        raise AssertionError((generated, EXPECTED_GENERATED_ENTRIES))
    edge_hash = digest.hexdigest()
    if edge_hash != EXPECTED_EDGE_SHA256:
        raise AssertionError((edge_hash, EXPECTED_EDGE_SHA256))

    row_entries: list[dict[int, int]] = [
        {} for _ in range(MATRIX_DIMENSION)
    ]
    for row, column, sign in matrix_edges():
        updated = row_entries[row].get(column, 0) + sign
        if updated:
            row_entries[row][column] = updated
        else:
            row_entries[row].pop(column, None)

    nonzero_entries = sum(len(row) for row in row_entries)
    if nonzero_entries != EXPECTED_GENERATED_ENTRIES:
        raise AssertionError((nonzero_entries, EXPECTED_GENERATED_ENTRIES))
    if any(value not in {-1, 1} for row in row_entries for value in row.values()):
        raise AssertionError("the canonical matrix must have only signed-unit entries")

    component_rows: dict[int, list[int]] = defaultdict(list)
    component_columns: dict[int, list[int]] = defaultdict(list)
    for row in range(MATRIX_DIMENSION):
        component_rows[union_find.find(row)].append(row)
    for column in range(MATRIX_DIMENSION):
        component_columns[union_find.find(MATRIX_DIMENSION + column)].append(column)

    if set(component_rows) != set(component_columns):
        raise AssertionError("row and column component sets differ")
    if len(component_rows) != EXPECTED_COMPONENT_COUNT:
        raise AssertionError((len(component_rows), EXPECTED_COMPONENT_COUNT))
    for root in component_rows:
        if len(component_rows[root]) != len(component_columns[root]):
            raise AssertionError((root, len(component_rows[root]), len(component_columns[root])))

    return (
        row_entries,
        dict(component_rows),
        dict(component_columns),
        edge_hash,
        nonzero_entries,
    )


def rank_histogram_for_prime(
    row_entries: list[dict[int, int]],
    component_rows: dict[int, list[int]],
    component_columns: dict[int, list[int]],
    prime: int,
) -> tuple[Counter[tuple[int, int]], int]:
    histogram: Counter[tuple[int, int]] = Counter()
    total_rank = 0
    for root in sorted(component_rows):
        rows = component_rows[root]
        size = len(rows)
        if len(component_columns[root]) != size:
            raise AssertionError(root)
        rank = sparse_rank_mod(rows, row_entries, prime)
        histogram[(size, rank)] += 1
        total_rank += rank
    return histogram, total_rank


def histogram_rows(
    histogram: Counter[tuple[int, int]],
) -> list[dict[str, int]]:
    return [
        {
            "component_order": order,
            "component_rank": rank,
            "component_count": count,
            "rank_contribution": rank * count,
        }
        for (order, rank), count in sorted(histogram.items())
    ]


def build_payload() -> dict[str, object]:
    (
        row_entries,
        component_rows,
        component_columns,
        edge_hash,
        nonzero_entries,
    ) = build_support_graph()

    prime_results: dict[str, object] = {}
    reference_histogram: Counter[tuple[int, int]] | None = None
    for prime in PRIMES:
        histogram, total_rank = rank_histogram_for_prime(
            row_entries,
            component_rows,
            component_columns,
            prime,
        )
        if dict(histogram) != EXPECTED_COMPONENT_HISTOGRAM:
            raise AssertionError((prime, histogram, EXPECTED_COMPONENT_HISTOGRAM))
        if total_rank != EXPECTED_TOTAL_RANK:
            raise AssertionError((prime, total_rank, EXPECTED_TOTAL_RANK))
        if reference_histogram is not None and histogram != reference_histogram:
            raise AssertionError("prime-field component histograms differ")
        reference_histogram = histogram
        prime_results[str(prime)] = {
            "total_rank": total_rank,
            "component_histogram": histogram_rows(histogram),
        }

    lower_bound = math.ceil(EXPECTED_TOTAL_RANK / RANK_ONE_NORMALIZATION)
    if lower_bound != 29:
        raise AssertionError(lower_bound)

    return {
        "status": "N6_RECURSIVE_KOSZUL_TENSOR_RANK_REPLAYED",
        "field_claim": "characteristic zero",
        "source_identity": {
            "paper": "Han--Ju--Kim, arXiv:2503.12032v1, Theorem 5.6",
            "upstream_repository": "jihan099/RKF",
            "upstream_main_commit": "2ebfbf70d7d1474c045bfbc0f7449c7b083667d9",
            "upstream_per6_blob": "395c0a05148e34507d1ba0cbdb347ae84eea1491",
            "upstream_rank_helper_blob": "afe1a349e17d2a1b2f11d223aba3a4bbe0988a16",
            "upstream_data_used_by_this_replay": False,
        },
        "flattening": {
            "exterior_degrees": [1, 2, 3, 4],
            "matrix_rows": MATRIX_DIMENSION,
            "matrix_columns": MATRIX_DIMENSION,
            "generated_integer_entries": EXPECTED_GENERATED_ENTRIES,
            "stored_nonzero_entries": nonzero_entries,
            "entry_values": [-1, 1],
            "canonical_edge_stream_sha256": edge_hash,
            "bipartite_component_count": len(component_rows),
            "rank_one_normalization": RANK_ONE_NORMALIZATION,
        },
        "prime_replays": prime_results,
        "characteristic_zero_rank_lower_bound": EXPECTED_TOTAL_RANK,
        "border_tensor_rank_lower_bound": lower_bound,
        "ordinary_tensor_rank_lower_bound": lower_bound,
        "restricted_family_consequences": {
            "row_homogeneous_rank_lower_bound": lower_bound,
            "full_column_sign_rank_lower_bound": lower_bound,
            "two_defect_sign_rank_lower_bound": lower_bound,
            "one_defect_sign_rank_lower_bound_from_this_audit": lower_bound,
            "one_defect_exact_repository_result": 32,
            "glynn_upper_bound": 32,
            "row_homogeneous_interval": [29, 32],
            "two_defect_sign_interval": [29, 32],
        },
        "route_decision": {
            "row_homogeneous_decomposition_with_at_most_28_terms": "impossible",
            "sign_family_decomposition_with_at_most_25_terms": "impossible",
            "sign_family_can_falsify_unrestricted_lower_26": False,
            "broad_sign_optimization_authorized": False,
        },
        "logical_direction": (
            "The integer matrix has modular rank 70692, so its characteristic-"
            "zero rank is at least 70692. The determinantal rank method then "
            "gives border tensor rank at least ceil(70692/2500)=29."
        ),
        "claim_boundary": (
            "This theorem concerns tensor rank and row-homogeneous or sign "
            "subfamilies. It does not prove unrestricted Chow rank at least "
            "29, border Chow rank at least 29, lower 26 for unrestricted Chow "
            "rank, or exact row-homogeneous rank 32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_RECURSIVE_KOSZUL_TENSOR_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
