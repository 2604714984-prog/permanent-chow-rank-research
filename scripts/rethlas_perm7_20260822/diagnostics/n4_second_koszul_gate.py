#!/usr/bin/env python3
"""Exact modular audit of all one-step Koszul-Chow gates for perm_4.

The matrix is split by the row/column torus weight for the permanent and by
the full variable torus weight for one independent four-factor Chow term.
Modular rank is a characteristic-zero lower bound.  The preceding Koszul
image gives a characteristic-zero upper bound because consecutive Koszul
maps compose to zero.  Apolar/Koszul transpose duality supplies the same
rank at the complementary derivative and wedge degrees.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial

N = 4
VARIABLES = N * N
PRIME = 1_000_003
def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def sparse_rank(columns):
    pivots = {}
    rank = 0
    for raw in columns:
        vector = {i: c % PRIME for i, c in raw.items() if c % PRIME}
        while vector:
            pivot = min(vector)
            coeff = vector[pivot]
            old = pivots.get(pivot)
            if old is None:
                inv = pow(coeff, PRIME - 2, PRIME)
                pivots[pivot] = {i: c * inv % PRIME for i, c in vector.items()}
                rank += 1
                break
            for i, c in old.items():
                value = (vector.get(i, 0) - coeff * c) % PRIME
                if value:
                    vector[i] = value
                else:
                    vector.pop(i, None)
    return rank


def canonical(weight):
    return tuple(sorted(weight[:N])) + tuple(sorted(weight[N:]))


def orbit_size(weight):
    answer = 1
    for half in (weight[:N], weight[N:]):
        value = factorial(N)
        for multiplicity in Counter(half).values():
            value //= factorial(multiplicity)
        answer *= value
    return answer


def rc_weight(rows, columns, wedge):
    answer = [0] * (2 * N)
    for r in rows:
        answer[r] += 1
    for c in columns:
        answer[N + c] += 1
    for variable in wedge:
        r, c = divmod(variable, N)
        answer[r] += 1
        answer[N + c] += 1
    return tuple(answer)


def permanent_rank(output_degree: int, wedge_degree: int):
    wedge_in = tuple(combinations(range(VARIABLES), wedge_degree))
    wedge_out = tuple(combinations(range(VARIABLES), wedge_degree + 1))
    wedge_out_index = {w: i for i, w in enumerate(wedge_out)}
    subsets = tuple(combinations(range(N), output_degree))
    basis = tuple((r, c) for r in subsets for c in subsets)
    output_monomials = set()
    for rows in combinations(range(N), output_degree - 1):
        for columns in combinations(range(N), output_degree - 1):
            for permuted in permutations(columns):
                output_monomials.add(
                    tuple(sorted(r * N + c for r, c in zip(rows, permuted, strict=True)))
                )
    output_monomials = tuple(sorted(output_monomials))
    monomial_index = {m: i for i, m in enumerate(output_monomials)}
    blocks = defaultdict(list)
    for rows, columns in basis:
        for wedge in wedge_in:
            weight = rc_weight(rows, columns, wedge)
            if weight == canonical(weight):
                blocks[weight].append((rows, columns, wedge))

    def column(descriptor):
        rows, columns, wedge = descriptor
        wedge_set = set(wedge)
        values = {}
        for row in rows:
            for column_value in columns:
                variable = row * N + column_value
                if variable in wedge_set:
                    continue
                rr = tuple(x for x in rows if x != row)
                cc = tuple(x for x in columns if x != column_value)
                for permuted in permutations(cc):
                    monomial = tuple(sorted(r * N + c for r, c in zip(rr, permuted, strict=True)))
                    output_wedge = tuple(sorted((variable,) + wedge))
                    row_id = monomial_index[monomial] * len(wedge_out) + wedge_out_index[output_wedge]
                    values[row_id] = (values.get(row_id, 0) + insertion_sign(variable, wedge)) % PRIME
        return {i: c for i, c in values.items() if c}

    total = 0
    represented = 0
    for weight, descriptors in blocks.items():
        mult = orbit_size(weight)
        represented += mult * len(descriptors)
        total += mult * sparse_rank(column(d) for d in descriptors)
    assert represented == len(basis) * len(wedge_in)
    return total, len(basis) * len(wedge_in)


def chow_rank(output_degree: int, wedge_degree: int):
    wedge_in = tuple(combinations(range(VARIABLES), wedge_degree))
    wedge_out = tuple(combinations(range(VARIABLES), wedge_degree + 1))
    wedge_out_index = {w: i for i, w in enumerate(wedge_out)}
    active = tuple(range(N))
    basis = tuple(combinations(active, output_degree))
    output = tuple(combinations(active, output_degree - 1))
    output_index = {m: i for i, m in enumerate(output)}
    blocks = defaultdict(list)
    for monomial in basis:
        for wedge in wedge_in:
            weight = [0] * VARIABLES
            for variable in monomial + wedge:
                weight[variable] += 1
            blocks[tuple(weight)].append((monomial, wedge))

    def column(descriptor):
        monomial, wedge = descriptor
        values = {}
        for variable in monomial:
            if variable in wedge:
                continue
            output_monomial = tuple(x for x in monomial if x != variable)
            output_wedge = tuple(sorted((variable,) + wedge))
            row_id = output_index[output_monomial] * len(wedge_out) + wedge_out_index[output_wedge]
            values[row_id] = (values.get(row_id, 0) + insertion_sign(variable, wedge)) % PRIME
        return {i: c for i, c in values.items() if c}

    total = sum(sparse_rank(column(d) for d in descriptors) for descriptors in blocks.values())
    return total, len(basis) * len(wedge_in)


def first_permanent(m: int) -> int:
    return VARIABLES * comb(N, m) ** 2 - comb(N, m + 1) ** 2


def first_chow(m: int) -> int:
    return VARIABLES * comb(N, m) - comb(N, m + 1)


def main():
    print("n4 Koszul-Chow wedge gate")
    prior_perm = {}
    prior_chow = {}
    table = {}
    for p in range(1, VARIABLES):
        print(f"p={p}")
        next_perm = {}
        next_chow = {}
        for m in (1, 2, 3, 4):
            perm_mod, perm_domain = permanent_rank(m, p)
            chow_mod, chow_domain = chow_rank(m, p)
            if p == 1:
                # The p=0 derivative map is injective.  Its image lies in
                # the p=1 kernel, so these are rigorous complex upper bounds;
                # they need not equal the modular lower ranks (notably m=1).
                perm_upper = first_permanent(m)
                chow_upper = first_chow(m)
            else:
                perm_upper = perm_domain - prior_perm.get(m + 1, 0)
                chow_upper = chow_domain - prior_chow.get(m + 1, 0)
            certified_bound = (perm_mod + chow_upper - 1) // chow_upper if chow_upper else 0
            route_ceiling = (perm_upper + chow_mod - 1) // chow_mod if chow_mod else 0
            if m < 4:
                print(
                    f"  m={m} perm=[{perm_mod},{perm_upper}] "
                    f"chow=[{chow_mod},{chow_upper}] "
                    f"certified_bound={certified_bound} route_ceiling={route_ceiling}"
                )
            next_perm[m] = perm_mod
            next_chow[m] = chow_mod
            table[p, m] = {
                "perm_mod": perm_mod,
                "perm_upper": perm_upper,
                "chow_mod": chow_mod,
                "chow_upper": chow_upper,
            }
        prior_perm = next_perm
        prior_chow = next_chow

    for m in (1, 2, 3, 4):
        print(f"duality-sharpened m={m} route ceilings")
        dual_m = N - m + 1
        for p in range(1, VARIABLES):
            if p == VARIABLES - 1:
                # Dual wedge degree zero: the derivative map is injective,
                # so its rank is the complementary derivative-space dimension.
                target_upper = min(table[p, m]["perm_upper"], comb(N, dual_m) ** 2)
                term_lower = max(table[p, m]["chow_mod"], comb(N, dual_m))
            else:
                dual_p = VARIABLES - p - 1
                target_upper = min(
                    table[p, m]["perm_upper"], table[dual_p, dual_m]["perm_upper"]
                )
                term_lower = max(
                    table[p, m]["chow_mod"], table[dual_p, dual_m]["chow_mod"]
                )
            route_ceiling = (target_upper + term_lower - 1) // term_lower
            print(
                f"  p={p} target_upper={target_upper} "
                f"term_lower={term_lower} route_ceiling={route_ceiling}"
            )


if __name__ == "__main__":
    main()
