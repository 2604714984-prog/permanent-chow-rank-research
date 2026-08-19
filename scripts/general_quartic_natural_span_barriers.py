#!/usr/bin/env python3
"""Exact finite replay for two natural degree-six quartic compression barriers.

The mathematical proof is in
``docs/general_quartic_natural_span_compression_barriers.md``. This script
replays only the finite combinatorial interfaces:

* the six (2,2)-Laplace summands partition the 24 permanent monomials;
* every nonempty support pattern in their span has essential dimension at
  least eight;
* the eight Glynn sign tensors form the Walsh parity basis;
* the permanent has a unique Glynn expansion with all eight coefficients
  nonzero.

Only the Python standard library and exact arithmetic are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product, permutations
from pathlib import Path
from typing import Iterable, Sequence


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def exact_rank(matrix: Sequence[Sequence[int | Fraction]]) -> int:
    """Rank over Q by deterministic Gaussian elimination."""

    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    width = len(rows[0])
    require(all(len(row) == width for row in rows), "ragged matrix")
    rank = 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for index in range(len(rows)):
            if index == rank:
                continue
            factor = rows[index][column]
            if factor:
                rows[index] = [
                    left - factor * right
                    for left, right in zip(rows[index], rows[rank], strict=True)
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def permanent_monomials(order: int) -> tuple[tuple[int, ...], ...]:
    return tuple(permutations(range(order)))


def laplace_22_basis() -> dict[tuple[int, int], frozenset[tuple[int, ...]]]:
    """Return the six summand supports for the fixed row split 01|23."""

    columns = frozenset(range(4))
    basis: dict[tuple[int, int], frozenset[tuple[int, ...]]] = {}
    for left in combinations(range(4), 2):
        left_set = frozenset(left)
        right = tuple(sorted(columns - left_set))
        monomials = set()
        for top in permutations(left):
            for bottom in permutations(right):
                monomials.add(top + bottom)
        require(len(monomials) == 4, (left, monomials))
        basis[left] = frozenset(monomials)
    return basis


def laplace_support_profile(
    support: Iterable[tuple[int, int]],
) -> tuple[int, int, int]:
    """Return top union, bottom union, and exact essential dimension.

    For a nonzero coefficient support S, derivatives in each fixed matrix row
    have pairwise disjoint cubic monomial supports. The two top rows each
    contribute |union C| and the two bottom rows each contribute
    |union C^c|.
    """

    selected = tuple(support)
    require(selected, "empty Laplace support")
    all_columns = frozenset(range(4))
    top_union = frozenset().union(*(frozenset(edge) for edge in selected))
    bottom_union = frozenset().union(
        *(all_columns - frozenset(edge) for edge in selected)
    )
    essential_dimension = 2 * len(top_union) + 2 * len(bottom_union)
    return len(top_union), len(bottom_union), essential_dimension


def audit_laplace_span() -> dict[str, object]:
    basis = laplace_22_basis()
    all_permanent = frozenset(permanent_monomials(4))
    union = frozenset().union(*basis.values())
    require(union == all_permanent, (len(union), len(all_permanent)))
    require(sum(len(value) for value in basis.values()) == len(union), "overlap")

    edges = tuple(basis)
    distribution: Counter[int] = Counter()
    detailed: Counter[tuple[int, int, int]] = Counter()
    for mask in range(1, 1 << len(edges)):
        support = tuple(
            edges[index] for index in range(len(edges)) if mask >> index & 1
        )
        profile = laplace_support_profile(support)
        detailed[profile] += 1
        distribution[profile[2]] += 1

    require(sum(distribution.values()) == 63, distribution)
    require(min(distribution) == 8, distribution)
    require(
        distribution == Counter({8: 6, 12: 12, 14: 8, 16: 37}),
        distribution,
    )

    return {
        "basis_size": len(basis),
        "monomials_per_basis_vector": 4,
        "permanent_monomials": len(all_permanent),
        "supports_checked": 63,
        "essential_dimension_distribution": {
            str(key): distribution[key] for key in sorted(distribution)
        },
        "support_profile_distribution": {
            f"top_{top}_bottom_{bottom}_ess_{essential}": count
            for (top, bottom, essential), count in sorted(detailed.items())
        },
        "minimum_nonzero_essential_dimension": min(distribution),
        "degree_six_chow_component_essential_cap": 6,
        "internal_intersection_zero": True,
    }


def sign_vectors() -> tuple[tuple[int, ...], ...]:
    return tuple((1,) + signs for signs in product((-1, 1), repeat=3))


def parity_class(indices: tuple[int, int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(index == value for index in indices) % 2 for value in (1, 2, 3)
    )


def sign_tensor_value(sign: tuple[int, ...], indices: tuple[int, ...]) -> int:
    result = 1
    for index in indices:
        result *= sign[index]
    return result


def glynn_coefficients(signs: Sequence[tuple[int, ...]]) -> tuple[Fraction, ...]:
    return tuple(Fraction(sign[1] * sign[2] * sign[3], 8) for sign in signs)


def audit_glynn_span() -> dict[str, object]:
    signs = sign_vectors()
    classes = tuple(product((0, 1), repeat=3))
    walsh = [
        [
            (
                (-1)
                ** sum(
                    bit * ((1 - sign[index + 1]) // 2)
                    for index, bit in enumerate(label)
                )
            )
            for sign in signs
        ]
        for label in classes
    ]
    representatives: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for indices in product(range(4), repeat=4):
        representatives.setdefault(parity_class(indices), indices)
    require(set(representatives) == set(classes), representatives)
    direct = [
        [sign_tensor_value(sign, representatives[label]) for sign in signs]
        for label in classes
    ]
    require(exact_rank(walsh) == 8, walsh)
    require(exact_rank(direct) == 8, direct)

    coefficients = glynn_coefficients(signs)
    require(all(coefficient for coefficient in coefficients), coefficients)

    for indices in product(range(4), repeat=4):
        reconstructed = sum(
            coefficient * sign_tensor_value(sign, indices)
            for coefficient, sign in zip(coefficients, signs, strict=True)
        )
        target = Fraction(int(len(set(indices)) == 4))
        require(reconstructed == target, (indices, reconstructed, target))

    parity_zero_representatives = {
        tuple(sorted((index, index, index, index))) for index in range(4)
    }
    parity_zero_representatives.update(
        tuple(sorted((left, left, right, right)))
        for left in range(4)
        for right in range(left + 1, 4)
    )
    require(
        all(
            parity_class(indices) == (0, 0, 0)
            for indices in parity_zero_representatives
        ),
        parity_zero_representatives,
    )

    return {
        "basis_size": len(signs),
        "ordered_tensor_coordinates": 4**4,
        "parity_classes": len(classes),
        "walsh_rank": exact_rank(direct),
        "normalized_low_essential_lines": [list(sign) for sign in signs],
        "low_essential_line_count": len(signs),
        "degree_six_chow_component_essential_cap": 6,
        "glynn_coefficients": [str(value) for value in coefficients],
        "all_glynn_coefficients_nonzero": True,
        "internal_minimum_terms": 8,
    }


def theorem_core() -> dict[str, object]:
    return {
        "schema": "general_quartic_natural_span_compression_barriers/v1",
        "field": "characteristic_zero",
        "laplace_22": audit_laplace_span(),
        "glynn_span": audit_glynn_span(),
        "claim_boundary": {
            "mu_6_4_exact_value": "OPEN_IN_[5,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
            "laplace_internal_recombination": "IMPOSSIBLE",
            "glynn_internal_minimum": 8,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def payload() -> dict[str, object]:
    core = theorem_core()
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {
        **core,
        "theorem_core_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    result = payload()
    if arguments.json is not None:
        arguments.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n"
        )
    print("GENERAL_QUARTIC_NATURAL_SPAN_BARRIERS_AUDIT_PASS")
    print(result["theorem_core_sha256"])


if __name__ == "__main__":
    main()
