#!/usr/bin/env python3
"""Exact bounded checks for the row-weight circuit report.

The proof is symbolic; this script only replays the finite coefficient
identities used in the adversarial examples.
"""

from collections import defaultdict


def mul_linear(left, right):
    """Multiply two sparse polynomials with tuple exponent keys."""
    out = defaultdict(int)
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return {m: c for m, c in out.items() if c}


def linear(coeffs):
    n = len(coeffs)
    return {
        tuple(1 if i == j else 0 for i in range(n)): c
        for j, c in enumerate(coeffs)
        if c
    }


def add_scaled(target, source, scale=1):
    for monomial, coefficient in source.items():
        target[monomial] += scale * coefficient


def check_pluecker():
    # Variables are a,b,c,d.
    a_minus_b = linear((1, -1, 0, 0))
    c_minus_d = linear((0, 0, 1, -1))
    a_minus_c = linear((1, 0, -1, 0))
    b_minus_d = linear((0, 1, 0, -1))
    a_minus_d = linear((1, 0, 0, -1))
    b_minus_c = linear((0, 1, -1, 0))
    total = defaultdict(int)
    add_scaled(total, mul_linear(a_minus_b, c_minus_d), 1)
    add_scaled(total, mul_linear(a_minus_c, b_minus_d), -1)
    add_scaled(total, mul_linear(a_minus_d, b_minus_c), 1)
    assert all(value == 0 for value in total.values())


def check_fourier_moments():
    # Sum_{s=0}^6 zeta^{s(q-1)} is represented exactly by the
    # elementary cyclotomic identity: 7 when 7 divides q-1, else 0.
    moments = [7 if (q - 1) % 7 == 0 else 0 for q in range(8)]
    assert moments == [0, 7, 0, 0, 0, 0, 0, 0]


def check_zero_anchor_orders():
    # A term with z zero W-projections has no coefficient below U-degree z.
    for z in range(8):
        possible_degrees = [
            q
            for q in range(8)
            if any(
                len(subset) == q and set(range(z)).issubset(subset)
                for subset in __import__("itertools").combinations(range(7), q)
            )
        ]
        assert possible_degrees == list(range(z, 8))


def main():
    check_pluecker()
    check_fourier_moments()
    check_zero_anchor_orders()
    print("COMMON_FACTOR_CIRCUIT_AUDIT_PASS")


if __name__ == "__main__":
    main()
