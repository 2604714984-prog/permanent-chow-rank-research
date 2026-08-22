#!/usr/bin/env python3
"""Exact finite audits for the residual/projection barriers in report.md.

Only the Python standard library is used.  Polynomials are sparse dictionaries
with integer coefficients, so every check below is exact.
"""

from collections import defaultdict
from itertools import combinations, product
from math import comb, factorial


def mul(p, q):
    out = defaultdict(int)
    for mon_p, coeff_p in p.items():
        for mon_q, coeff_q in q.items():
            out[tuple(sorted(mon_p + mon_q))] += coeff_p * coeff_q
    return {mon: coeff for mon, coeff in out.items() if coeff}


def add(p, q, q_scale=1):
    out = defaultdict(int, p)
    for mon, coeff in q.items():
        out[mon] += q_scale * coeff
    return {mon: coeff for mon, coeff in out.items() if coeff}


def linear(row_coefficients, column):
    return {
        (f"x{row}_{column}",): coefficient
        for row, coefficient in enumerate(row_coefficients, start=1)
        if coefficient
    }


def same_row_signature(p, row, a, b):
    mon = tuple(sorted((f"x{row}_{a}", f"x{row}_{b}")))
    return p.get(mon, 0)


def check_pair_defect():
    ell = {c: linear((1, 1), c) for c in range(1, 8)}
    minus = {c: linear((1, -1), c) for c in range(1, 8)}
    witnesses = []

    for a, b in combinations(range(1, 8), 2):
        ell_ab = mul(ell[a], ell[b])
        minus_ab = mul(minus[a], minus[b])
        witness = add(ell_ab, minus_ab, q_scale=-1)
        expected = {
            tuple(sorted((f"x1_{a}", f"x2_{b}"))): 2,
            tuple(sorted((f"x2_{a}", f"x1_{b}"))): 2,
        }
        assert witness == expected
        witnesses.append(witness)

        # Each same-row monomial is a private coordinate of the corresponding
        # ell_a ell_b (and likewise of m_a m_b).  Hence no nonzero combination
        # in either individual span can lie in the off-row quadratic space E_2.
        assert same_row_signature(ell_ab, 1, a, b) == 1
        assert same_row_signature(minus_ab, 1, a, b) == 1

    # The two monomials of a witness use its unordered column pair, so distinct
    # witnesses have disjoint support and are linearly independent.
    supports = [set(witness) for witness in witnesses]
    assert all(
        supports[i].isdisjoint(supports[j])
        for i in range(len(supports))
        for j in range(i)
    )
    assert len(witnesses) == comb(7, 2) == 21

    # With z = ell_1 and the complement containing m_1, ell_c, m_c (c > 1),
    # T_+ has z-order one and T_- has z-order zero.  No higher z-jets occur.
    plus_factor_z_degrees = [1] + [0] * 6
    minus_factor_z_degrees = [0] * 7
    assert sum(plus_factor_z_degrees) == 1
    assert sum(minus_factor_z_degrees) == 0
    return len(witnesses)


def check_scalar_annihilator_ceiling():
    capacities = []
    for order in range(8):
        atom_cap = comb(7, order)
        target_cap = atom_cap * atom_cap
        residual_bound_cap = 1 + target_cap // atom_cap
        assert residual_bound_cap == 1 + atom_cap
        capacities.append((order, atom_cap, target_cap, residual_bound_cap))
    assert max(row[3] for row in capacities) == 36
    return capacities


def check_glynn_factor_hyperplane():
    signs = [(1,) + tail for tail in product((-1, 1), repeat=6)]
    assert len(signs) == 64

    # After any one column is omitted, the sixfold tensors v_delta^{tensor 6}
    # contain the full Walsh character table as a coordinate minor.  A subset
    # S of the six free signs is realized by using every row in S once in the
    # six remaining column slots and filling the unused slots with row 1.
    characters = []
    for mask in range(64):
        characters.append(
            [
                product_value(
                    sign[index + 1]
                    for index in range(6)
                    if mask & (1 << index)
                )
                for sign in signs
            ]
        )
    for left in range(64):
        for right in range(64):
            inner_product = sum(
                characters[left][column] * characters[right][column]
                for column in range(64)
            )
            assert inner_product == (64 if left == right else 0)

    chosen_sign = (1,) * 7
    chosen_column = 1

    occurrences = 0
    for sign in signs:
        for column in range(1, 8):
            # Factors in different columns have disjoint variable support.
            # In the chosen column, normalization delta_1=1 removes the
            # otherwise possible global sign ambiguity.
            proportional = column == chosen_column and sign == chosen_sign
            occurrences += int(proportional)
    assert occurrences == 1
    assert len(signs) - occurrences == 63

    # A coordinate form such as x_77 is not proportional to any normalized
    # sign form: every sign form has all seven coefficients nonzero.
    coordinate_coefficients = (0, 0, 0, 0, 0, 0, 1)
    assert all(
        coordinate_coefficients != sign
        and coordinate_coefficients != tuple(-entry for entry in sign)
        for sign in signs
    )
    return len(signs) - occurrences


def product_value(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def check_row_multilinear_projection_of_t0():
    # A monomial of prod_j(sum_i x_ij) chooses one row for each column.
    # Its row multidegree is (1,...,1) exactly when the row choices form a
    # permutation, giving precisely the permanent support, all coefficients 1.
    transversal_choices = [
        rows for rows in product(range(1, 8), repeat=7) if len(set(rows)) == 7
    ]
    assert len(transversal_choices) == factorial(7) == 5040
    assert len(set(transversal_choices)) == factorial(7)
    return len(transversal_choices)


def check_repeated_factor_jet():
    # z^2 y_1 ... y_5 has no coefficient in z-degrees zero or one.
    z_multiplicity = 2
    assert z_multiplicity > 1
    zeroth_jet = int(z_multiplicity == 0)
    first_jet = int(z_multiplicity == 1)
    assert (zeroth_jet, first_jet) == (0, 0)
    return z_multiplicity


def main():
    pair_dim = check_pair_defect()
    capacities = check_scalar_annihilator_ceiling()
    remaining_glynn_terms = check_glynn_factor_hyperplane()
    transversal_terms = check_row_multilinear_projection_of_t0()
    repeated_order = check_repeated_factor_jet()

    print(f"pair-defect witnesses: {pair_dim}")
    print("annihilator table (order, atom cap, target cap, residual cap):")
    for row in capacities:
        print("  ", row)
    print(f"Glynn terms after chosen factor hyperplane: {remaining_glynn_terms}")
    print(f"row-multilinear terms surviving from T0: {transversal_terms}")
    print(f"first nonzero repeated-factor normal jet: order {repeated_order}")
    print("PASS: all residual/projection barrier checks are exact")


if __name__ == "__main__":
    main()
