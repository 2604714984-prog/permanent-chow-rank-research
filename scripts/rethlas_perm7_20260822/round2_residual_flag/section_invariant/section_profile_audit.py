#!/usr/bin/env python3
"""Bounded diagnostics for the subpermanent no-linear-divisor lemma.

The theorem is proved symbolically in report.md.  This script only stress-tests
small cases and structured/deterministic orientations over prime fields.  It
never treats a finite-field check as a characteristic-zero proof.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement, permutations
from math import comb
import random


def add_to_basis(vec, basis, prime):
    """Insert a sparse vector into a pivot-normalized modular basis."""
    vec = {i: c % prime for i, c in vec.items() if c % prime}
    while vec:
        pivot = max(vec)
        if pivot not in basis:
            inv = pow(vec[pivot], prime - 2, prime)
            vec = {i: (c * inv) % prime for i, c in vec.items() if c % prime}
            basis[pivot] = vec
            return True
        scale = vec[pivot]
        row = basis[pivot]
        for i, c in row.items():
            new = (vec.get(i, 0) - scale * c) % prime
            if new:
                vec[i] = new
            else:
                vec.pop(i, None)
    return False


def monomial_index(variable_count, degree):
    mons = list(combinations_with_replacement(range(variable_count), degree))
    return mons, {mon: i for i, mon in enumerate(mons)}


def subpermanent_columns(n, m, index):
    columns = []
    for rows in combinations(range(n), m):
        for cols in combinations(range(n), m):
            vec = {}
            for perm in permutations(cols):
                mon = tuple(sorted(r * n + c for r, c in zip(rows, perm)))
                vec[index[mon]] = vec.get(index[mon], 0) + 1
            columns.append(vec)
    return columns


def multiplication_columns(ell, variable_count, degree_minus_one, index, prime):
    columns = []
    for hmon in combinations_with_replacement(range(variable_count), degree_minus_one):
        vec = {}
        for variable, coeff in enumerate(ell):
            if coeff % prime:
                mon = tuple(sorted(hmon + (variable,)))
                pos = index[mon]
                vec[pos] = (vec.get(pos, 0) + coeff) % prime
        columns.append(vec)
    return columns


def intersection_dimension(n, m, ell, prime):
    variable_count = n * n
    _, index = monomial_index(variable_count, m)
    e_columns = subpermanent_columns(n, m, index)
    basis = {}
    for vec in e_columns:
        assert add_to_basis(vec, basis, prime)
    e_rank = len(basis)
    before = len(basis)
    multiplication = multiplication_columns(ell, variable_count, m - 1, index, prime)
    for vec in multiplication:
        add_to_basis(vec, basis, prime)
    added_mod_e = len(basis) - before
    multiplication_rank = comb(variable_count + m - 2, m - 1)
    return multiplication_rank - added_mod_e, e_rank, len(index), multiplication_rank


def projective_vectors(variable_count, prime):
    """Yield one normalized representative of every projective point."""
    total = prime ** variable_count
    for encoded in range(1, total):
        digits = []
        value = encoded
        for _ in range(variable_count):
            digits.append(value % prime)
            value //= prime
        first = next((c for c in digits if c), None)
        if first != 1:
            continue
        inv = pow(first, prime - 2, prime)
        yield tuple((c * inv) % prime for c in digits)


def structured_vectors(n, prime):
    variable_count = n * n
    vectors = []

    coordinate = [0] * variable_count
    coordinate[0] = 1
    vectors.append(tuple(coordinate))

    vectors.append(tuple([1] * variable_count))

    row = [0] * variable_count
    for c in range(n):
        row[c] = 1
    vectors.append(tuple(row))

    column = [0] * variable_count
    for r in range(n):
        column[r * n] = 1
    vectors.append(tuple(column))

    diagonal = [0] * variable_count
    for r in range(n):
        diagonal[r * n + r] = 1
    vectors.append(tuple(diagonal))

    cycle = [0] * variable_count
    cycle[0] = cycle[1] = cycle[n] = 1
    cycle[n + 1] = prime - 1
    vectors.append(tuple(cycle))
    return vectors


def deterministic_random_vectors(n, prime, count, seed):
    rng = random.Random(seed)
    variable_count = n * n
    for _ in range(count):
        while True:
            ell = tuple(rng.randrange(prime) for _ in range(variable_count))
            if any(ell):
                yield ell
                break


def check_family(n, m, prime, vectors, label):
    ambient = comb(n * n + m - 1, m)
    e_dimension = comb(n, m) ** 2
    h_dimension = comb(n * n + m - 2, m - 1)
    print(
        f"capacity label={label} n={n} m={m} p={prime} "
        f"ambient={ambient} E={e_dimension} h={h_dimension}"
    )
    checks = 0
    for ell in vectors:
        intersection, e_rank, actual_ambient, actual_h = intersection_dimension(
            n, m, ell, prime
        )
        assert actual_ambient == ambient
        assert e_rank == e_dimension
        assert actual_h == h_dimension
        assert intersection == 0, (n, m, prime, ell, intersection)
        checks += 1
    print(f"pass label={label} checks={checks}")
    return checks


def main():
    checks = 0
    checks += check_family(3, 2, 2, projective_vectors(9, 2), "n3_all_F2")
    checks += check_family(3, 2, 3, projective_vectors(9, 3), "n3_all_F3")
    checks += check_family(4, 2, 1_000_003, structured_vectors(4, 1_000_003), "n4m2_structured")
    checks += check_family(4, 3, 1_000_003, structured_vectors(4, 1_000_003), "n4m3_structured")
    checks += check_family(
        4,
        3,
        1_000_003,
        deterministic_random_vectors(4, 1_000_003, 24, 20260822),
        "n4m3_random",
    )
    checks += check_family(7, 2, 1_000_003, structured_vectors(7, 1_000_003), "n7m2_structured")
    checks += check_family(
        7,
        2,
        1_000_003,
        deterministic_random_vectors(7, 1_000_003, 32, 20260823),
        "n7m2_random",
    )
    print(f"SECTION_PROFILE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
