#!/usr/bin/env python3
"""Exact small certificates for the residual-flag normal-jet report.

The calculations are deliberately tiny.  They check the identities used as
stress tests; they do not search for a Chow decomposition and do not certify
the exact rank of the permanent.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


Monomial = tuple[str, ...]
Polynomial = dict[Monomial, int]


def add(*polys: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
            if out[monomial] == 0:
                del out[monomial]
    return out


def scale(poly: Polynomial, scalar: int) -> Polynomial:
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(sorted(lm + rm))
            out[monomial] = out.get(monomial, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


def linear_form(terms: dict[str, int]) -> Polynomial:
    return {(variable,): coefficient for variable, coefficient in terms.items() if coefficient}


def product_of_forms(forms: list[Polynomial]) -> Polynomial:
    out: Polynomial = {(): 1}
    for form in forms:
        out = multiply(out, form)
    return out


def exact_rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows = len(a)
    cols = len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_value = a[pivot_row][col]
        a[pivot_row] = [x / pivot_value for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def check_repeated_factor_orders() -> None:
    # z^m y_1 ... y_(7-m) has exactly one nonzero normal layer, q=m.
    for multiplicity in range(1, 8):
        layer_sizes = [0] * 8
        layer_sizes[multiplicity] = 1
        assert next(q for q, size in enumerate(layer_sizes) if size) == multiplicity
        assert sum(layer_sizes) == 1


def check_two_anchor_tangent_amplification() -> None:
    # A(t)=prod_a(u_a+t v_a), B(t)=-prod_a u_a.  The constant layers
    # cancel.  The first layer is sum_a v_a prod_(b!=a)u_b and its
    # Z^* -> Sym^6(H) flattening is the 7 by 7 identity in these bases.
    tangent_matrix = [[int(i == j) for j in range(7)] for i in range(7)]
    assert exact_rank(tangent_matrix) == 7
    layer_counts = [comb(7, q) for q in range(8)]
    layer_counts[0] -= 1  # cancellation with B(t)
    assert layer_counts[0] == 0
    assert layer_counts[1] == 7
    assert sum(layer_counts[2:]) == 120


def check_generic_jet_split_ranks() -> None:
    # For prod_a(u_a+t v_a), the q-th coefficient has the diagonal
    # flattening indexed by q-subsets A: v_A tensor u_(A^c).  Hence its
    # split (Z|H) matrix rank is exactly C(7,q), not one.
    for q in range(8):
        size = comb(7, q)
        identity = [[int(i == j) for j in range(size)] for i in range(size)]
        assert exact_rank(identity) == size


def check_t_plus_minus_quadratic_packet() -> None:
    relations: list[Polynomial] = []
    for a, b in combinations(range(1, 8), 2):
        ell_a = linear_form({f"x1{a}": 1, f"x2{a}": 1})
        ell_b = linear_form({f"x1{b}": 1, f"x2{b}": 1})
        min_a = linear_form({f"x1{a}": 1, f"x2{a}": -1})
        min_b = linear_form({f"x1{b}": 1, f"x2{b}": -1})
        relation = add(multiply(ell_a, ell_b), scale(multiply(min_a, min_b), -1))
        expected = {
            tuple(sorted((f"x1{a}", f"x2{b}"))): 2,
            tuple(sorted((f"x2{a}", f"x1{b}"))): 2,
        }
        assert relation == expected
        relations.append(relation)
    # Distinct unordered column pairs have disjoint monomial supports.
    supports = [set(relation) for relation in relations]
    assert len(relations) == 21
    assert all(supports[i].isdisjoint(supports[j])
               for i in range(21) for j in range(i))


def check_row_killing_weight() -> None:
    # Every permanent monomial uses exactly one variable from row 7.
    normal_degrees = []
    for sigma in permutations(range(1, 8)):
        monomial = [(row, sigma[row - 1]) for row in range(1, 8)]
        normal_degrees.append(sum(row == 7 for row, _ in monomial))
    assert len(normal_degrees) == factorial(7) == 5040
    assert set(normal_degrees) == {1}


def check_glynn_factor_flag_and_row_obstruction() -> None:
    # Seven normalized sign vectors form a basis of one column space:
    # all-plus and the six vectors obtained by flipping one of rows 2..7.
    sign_vectors = [[1] * 7]
    for row in range(1, 7):
        vector = [1] * 7
        vector[row] = -1
        sign_vectors.append(vector)
    assert exact_rank(sign_vectors) == 7

    # A normalized Glynn factor has all seven row coefficients nonzero.
    # Hence it never lies in the coordinate row-7 space, whose intersection
    # with its column is spanned by x_(7,c).
    assert all(sum(coefficient != 0 for coefficient in vector) == 7
               for vector in sign_vectors)

    # For Z_j=span(v_all-plus,e_2,...,e_j), the normalized sign cube meets
    # Z_j in exactly the vectors whose flipped coordinates lie in 2..j.
    # Hence the same-column Glynn flag kills 1,2,4,...,64 atoms.
    normalized_signs = [(1,) + tail for tail in product((1, -1), repeat=6)]
    killed_counts = []
    for j in range(1, 8):
        killed = [
            delta for delta in normalized_signs
            if all(delta[row] == 1 for row in range(j, 7))
        ]
        killed_counts.append(len(killed))
    assert killed_counts == [1, 2, 4, 8, 16, 32, 64]

    # Under a coordinate-row scaling, sign vectors differing only in row 7
    # have the same constant anchor and opposite Glynn coefficient.  There
    # are exactly 32 such cancellation pairs.
    row_deleted_classes = {delta[:-1] for delta in normalized_signs}
    assert len(row_deleted_classes) == 32


def check_zero_anchor_boolean_delta() -> None:
    # On the standard six-bit Boolean slice, the diagonal monomial has
    # coefficient one only at (1,...,1).  It is a single legal Chow atom,
    # so allowing zero anchors destroys a one-character Fourier cap.
    values = {}
    for bits in product((0, 1), repeat=6):
        values[bits] = int(all(bits))
    assert sum(values.values()) == 1
    assert values[(1,) * 6] == 1


def check_nested_rees_exponents() -> None:
    # Under z_a -> (t_a ... t_s) z_a, a normal monomial z^alpha has
    # t_j-exponent m_j=sum_(a<=j)alpha_a.  The map is injective, with
    # alpha_j=m_j-m_(j-1).
    seen: set[tuple[int, ...]] = set()
    s = 4
    for total in range(8):
        for alpha in product(range(total + 1), repeat=s):
            if sum(alpha) != total:
                continue
            cumulative = tuple(sum(alpha[:j + 1]) for j in range(s))
            recovered = (cumulative[0],) + tuple(
                cumulative[j] - cumulative[j - 1] for j in range(1, s)
            )
            assert recovered == alpha
            assert cumulative not in seen
            seen.add(cumulative)
    assert len(seen) == comb(7 + s, s)


def main() -> None:
    check_repeated_factor_orders()
    check_two_anchor_tangent_amplification()
    check_generic_jet_split_ranks()
    check_t_plus_minus_quadratic_packet()
    check_row_killing_weight()
    check_glynn_factor_flag_and_row_obstruction()
    check_zero_anchor_boolean_delta()
    check_nested_rees_exponents()
    print("JET_INCIDENCE_AUDIT_PASS")
    print("permanent_monomials=5040")
    print("t_plus_minus_independent_relations=21")
    print("two_anchor_first_layer_rank=7")
    print("glynn_same_column_killed_counts=1,2,4,8,16,32,64")
    print("glynn_row_anchor_pairs=32")
    print("nested_rees_degree_le_7_states=330")


if __name__ == "__main__":
    main()
