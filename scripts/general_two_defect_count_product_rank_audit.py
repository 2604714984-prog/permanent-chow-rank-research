#!/usr/bin/env python3
"""Exact finite interfaces for the general count-product atomic-rank theorem.

The mathematical proof is in ``docs/general_two_defect_count_product_rank.md``.
This audit reconstructs the nine local pure atoms, classifies every support of
size at most four over ``Fraction``, verifies sharp star examples, and replays
the atomic and Fourier identities on every assignment for ``n=4,5,6``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

D = {
    "A": (Fraction(-2), Fraction(0)),
    "B": (Fraction(0), Fraction(-2)),
    "C": (Fraction(-2), Fraction(-2)),
}
LABELS = tuple(D)
TARGET = (Fraction(0), Fraction(1), Fraction(1), Fraction(0))


def atoms() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for left in LABELS:
        for right in LABELS:
            dl, dr = D[left], D[right]
            rows.append(
                {
                    "labels": (left, right),
                    "pure": tuple(dl[i] * dr[j] for i in range(2) for j in range(2)),
                    "left_unary": dl,
                    "right_unary": dr,
                }
            )
    return rows


def solve(columns: list[tuple[Fraction, ...]], target: tuple[Fraction, ...]):
    m, n = len(target), len(columns)
    a = [
        [Fraction(columns[j][i]) for j in range(n)] + [Fraction(target[i])]
        for i in range(m)
    ]
    row = 0
    pivots: list[int] = []
    for col in range(n):
        pivot = next((i for i in range(row, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [value / scale for value in a[row]]
        for i in range(m):
            if i != row and a[i][col]:
                q = a[i][col]
                a[i] = [a[i][j] - q * a[row][j] for j in range(n + 1)]
        pivots.append(col)
        row += 1
        if row == m:
            break
    if any(all(a[i][j] == 0 for j in range(n)) and a[i][n] for i in range(m)):
        return None
    free = [j for j in range(n) if j not in pivots]
    particular = [Fraction(0)] * n
    for i, col in enumerate(pivots):
        particular[col] = a[i][n]
    kernel = []
    for f in free:
        vector = [Fraction(0)] * n
        vector[f] = 1
        for i, col in enumerate(pivots):
            vector[col] = -a[i][f]
        kernel.append(tuple(vector))
    return tuple(particular), tuple(kernel)


def endpoint_unary(
    table: list[dict[str, object]],
    support: tuple[int, ...],
    coefficients: tuple[Fraction, ...],
    endpoint: str,
) -> tuple[Fraction, Fraction]:
    key = f"{endpoint}_unary"
    return tuple(
        sum(
            coefficients[i] * table[index][key][coordinate]
            for i, index in enumerate(support)
        )
        for coordinate in range(2)
    )  # type: ignore[return-value]


def local_catalog() -> dict[str, object]:
    table = atoms()
    compatible: Counter[int] = Counter()
    genuine: Counter[int] = Counter()
    left_hist: Counter[tuple[Fraction, Fraction]] = Counter()
    right_hist: Counter[tuple[Fraction, Fraction]] = Counter()
    unique_two = None

    for size in (1, 2, 3):
        for support in combinations(range(9), size):
            result = solve([table[index]["pure"] for index in support], TARGET)
            if result is None:
                continue
            coefficients, kernel = result
            if kernel:
                raise AssertionError((size, support, kernel))
            compatible[size] += 1
            if all(coefficients):
                genuine[size] += 1
            if size == 2 and all(coefficients):
                unique_two = {
                    "support": [list(table[index]["labels"]) for index in support],
                    "coefficients": [str(value) for value in coefficients],
                    "left_unary": [
                        str(value)
                        for value in endpoint_unary(table, support, coefficients, "left")
                    ],
                    "right_unary": [
                        str(value)
                        for value in endpoint_unary(table, support, coefficients, "right")
                    ],
                }
            if size == 3:
                left_hist[endpoint_unary(table, support, coefficients, "left")] += 1
                right_hist[endpoint_unary(table, support, coefficients, "right")] += 1

    expected_hist = Counter(
        {
            (Fraction(-1, 2), Fraction(-1, 2)): 9,
            (Fraction(0), Fraction(-1, 2)): 3,
            (Fraction(-1, 2), Fraction(0)): 3,
            (Fraction(0), Fraction(0)): 1,
            (Fraction(-1), Fraction(-1, 2)): 1,
            (Fraction(-1, 2), Fraction(-1)): 1,
        }
    )
    if compatible != Counter({3: 18, 2: 1}):
        raise AssertionError(compatible)
    if genuine != Counter({3: 11, 2: 1}):
        raise AssertionError(genuine)
    if left_hist != expected_hist or right_hist != expected_hist:
        raise AssertionError((left_hist, right_hist))
    if unique_two != {
        "support": [["A", "B"], ["B", "A"]],
        "coefficients": ["1/4", "1/4"],
        "left_unary": ["-1/2", "-1/2"],
        "right_unary": ["-1/2", "-1/2"],
    }:
        raise AssertionError(unique_two)

    return {
        "compatible_supports": {str(size): compatible[size] for size in (1, 2, 3)},
        "genuine_supports": {str(size): genuine[size] for size in (1, 2, 3)},
        "unique_two_atom_expression": unique_two,
        "three_atom_endpoint_histogram": {
            f"{x},{y}": count for (x, y), count in sorted(expected_hist.items())
        },
        "both_endpoint_coordinates_nonpositive": True,
    }


def equal_unary_catalog() -> dict[str, object]:
    table = atoms()
    histograms: dict[str, Counter[Fraction]] = {}
    by_size: dict[str, dict[str, int]] = {}
    for endpoint in ("left", "right"):
        t_column = (Fraction(0),) * 4 + (Fraction(-1), Fraction(-1))
        target = TARGET + (Fraction(0), Fraction(0))
        histogram: Counter[Fraction] = Counter()
        sizes: Counter[int] = Counter()
        for size in range(1, 5):
            for support in combinations(range(9), size):
                columns = [
                    table[index]["pure"] + table[index][f"{endpoint}_unary"]
                    for index in support
                ] + [t_column]
                result = solve(columns, target)
                if result is None:
                    continue
                solution, kernel = result
                if any(vector[-1] for vector in kernel):
                    raise AssertionError((endpoint, support, solution, kernel))
                histogram[solution[-1]] += 1
                sizes[size] += 1
        expected = Counter({Fraction(-1, 2): 42, Fraction(0): 10})
        if histogram != expected:
            raise AssertionError((endpoint, histogram))
        histograms[endpoint] = histogram
        by_size[endpoint] = {str(size): sizes[size] for size in range(1, 5)}
    return {
        "compatible_supports_by_endpoint_and_size": by_size,
        "equal_unary_value_histogram": {
            endpoint: {str(value): count for value, count in sorted(hist.items())}
            for endpoint, hist in histograms.items()
        },
        "positive_equal_unary_with_at_most_four_atoms": False,
    }


def star_examples() -> list[dict[str, object]]:
    table = atoms()
    index = {tuple(atom["labels"]): i for i, atom in enumerate(table)}
    support_labels = (("A", "B"), ("B", "A"), ("C", "A"), ("C", "B"), ("C", "C"))
    support = tuple(index[label] for label in support_labels)
    rows = []
    for degree in range(3, 10):
        coefficients = (
            Fraction(1, 4),
            Fraction(1, 4),
            Fraction(-degree, 4),
            Fraction(-degree, 4),
            Fraction(degree, 4),
        )
        pure = tuple(
            sum(coefficients[i] * table[atom]["pure"][coordinate] for i, atom in enumerate(support))
            for coordinate in range(4)
        )
        unary = endpoint_unary(table, support, coefficients, "left")
        expected = (Fraction(degree - 1, 2),) * 2
        if pure != TARGET or unary != expected:
            raise AssertionError((degree, pure, unary))
        rows.append(
            {
                "degree": degree,
                "support": [list(label) for label in support_labels],
                "coefficients": [str(value) for value in coefficients],
                "endpoint_unary": [str(value) for value in unary],
            }
        )
    return rows


def sign_value(label: int, row: int) -> int:
    return 1 if row == 0 or not ((label >> (row - 1)) & 1) else -1


def character(left: int, right: int) -> int:
    return -1 if (left & right).bit_count() & 1 else 1


def parity(assignment: tuple[int, ...]) -> int:
    value = 0
    for row in assignment:
        if row:
            value ^= 1 << (row - 1)
    return value


def count_product(assignment: tuple[int, ...], a: int, b: int) -> int:
    return assignment.count(a) * assignment.count(b)


def construction(assignment: tuple[int, ...], a: int, b: int) -> Fraction:
    n = len(assignment)
    label_a, label_b = 1 << (a - 1), 1 << (b - 1)
    label_ab = label_a | label_b
    value = Fraction(0)
    for j, k in combinations(range(n), 2):
        value += Fraction(1, 4) * sign_value(label_a, assignment[j]) * sign_value(label_b, assignment[k])
        value += Fraction(1, 4) * sign_value(label_b, assignment[j]) * sign_value(label_a, assignment[k])
    for j in range(n):
        value -= Fraction(n - 1, 4) * sign_value(label_ab, assignment[j])
    return value


def replay(n: int) -> dict[str, object]:
    a, b = n - 2, n - 1
    target_parity = (1 << (n - 1)) - 1
    support_character = (1 << (a - 1)) | (1 << (b - 1))
    zero_parity = target_parity ^ support_character
    group_size = 1 << (n - 1)
    nonzero_bases = [
        base
        for base in range(group_size)
        if character(target_parity, base) != character(zero_parity, base)
    ]
    target_fiber = zero_fiber = checks = 0
    for assignment in product(range(n), repeat=n):
        g = count_product(assignment, a, b)
        p = parity(assignment)
        if p == target_parity:
            target_fiber += 1
            if g != 1:
                raise AssertionError((n, assignment, "target", g))
        if p == zero_parity:
            zero_fiber += 1
            if g != 0:
                raise AssertionError((n, assignment, "zero", g))
        if construction(assignment, a, b) != g:
            raise AssertionError((n, assignment, "construction"))
        aggregate = sum(
            Fraction(
                character(p, base)
                * (character(target_parity, base) - character(zero_parity, base)),
                group_size,
            )
            * g
            for base in range(group_size)
        )
        expected = Fraction(int(tuple(sorted(assignment)) == tuple(range(n))))
        if aggregate != expected:
            raise AssertionError((n, assignment, aggregate, expected))
        checks += 1
    return {
        "n": n,
        "fixed_base_rank": n * n,
        "nonzero_bases": len(nonzero_bases),
        "base_labelled_cost": len(nonzero_bases) * n * n,
        "exact_post_collection_cost": len(nonzero_bases) * n * n if n >= 5 else None,
        "target_fiber_size": target_fiber,
        "zero_fiber_size": zero_fiber,
        "assignment_checks": checks,
    }


def build_payload() -> dict[str, object]:
    local = local_catalog()
    equal = equal_unary_catalog()
    examples = star_examples()
    replays = [replay(n) for n in (4, 5, 6)]
    return {
        "status": "GENERAL_TWO_DEFECT_COUNT_PRODUCT_RANK_EXACT",
        "field": "characteristic zero",
        "theorem": {
            "range": "n>=4",
            "fixed_base_atomic_rank": "rho_2(n_a*n_b)=n^2",
            "nonzero_base_count": "2^(n-2)",
            "base_labelled_cost": "2^(n-2)*n^2",
            "exact_post_collection_cost": "2^(n-2)*n^2 for n>=5",
        },
        "local_support_certificate": local,
        "equal_unary_certificate": equal,
        "sharp_star_examples": examples,
        "global_double_counting": {
            "incident_excess_per_zero_unary_vertex": 3,
            "edge_excess_endpoint_multiplicity_cap": 2,
            "inequality": "R>=n*(n-1)+E+n-Z>=n^2 because 3Z<=2E",
        },
        "exact_replays": replays,
        "n6_corollary": {
            "exact_fixed_base_rank": 36,
            "exact_sixteen_base_assignment_cost": 576,
            "independent_exhaustive_certificate": "N6-023",
        },
        "claim_boundary": (
            "The theorem concerns count-product separators and their fixed "
            "aggregate assignment. It does not determine another aggregate "
            "assignment, the global two-defect minimum, row-homogeneous "
            "tensor rank, or unrestricted Chow rank."
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
    print("GENERAL_TWO_DEFECT_COUNT_PRODUCT_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
