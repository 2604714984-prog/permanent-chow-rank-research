#!/usr/bin/env python3
"""Exact integer/rational audit for the beta_(2,3) fork obstruction.

This script uses no finite-field inference.  It checks the column-multidegree
counts for the common Glynn span, the F_2 and Glynn barcode data, and the
small linear program governing fractional target-bar selectors.
"""

from fractions import Fraction
from math import comb


def fork_multiplicities(x, y, z, rank_a, rank_b, rank_ab):
    """Multiplicities for Y <- X -> Z in the order p,u,v,s,t,w."""
    p = rank_a + rank_b - rank_ab
    u = rank_ab - rank_b
    v = rank_ab - rank_a
    s = x - rank_ab
    t = y - rank_a
    w = z - rank_b
    values = (p, u, v, s, t, w)
    assert all(value >= 0 for value in values)
    return values


def main():
    rows = 7
    signs = 64

    # Quadrics in the common Glynn annihilator: all quadrics within one
    # column, and a 27-dimensional kernel in every cross-column block.
    same_i2 = comb(rows + 1, 2)
    cross_i2 = rows * rows - 22
    assert (same_i2, cross_i2) == (28, 27)

    # Kernel dimensions of V tensor I_2 -> (I_2)_3, block by block.
    triple_same_domain = rows * same_i2
    triple_same_image = comb(rows + 2, 3)
    triple_same_kernel = triple_same_domain - triple_same_image

    double_domain = rows * same_i2 + rows * cross_i2
    double_image = comb(rows + 1, 2) * rows
    double_kernel = double_domain - double_image

    distinct_domain = 3 * rows * cross_i2
    distinct_quotient = rows + comb(rows, 3)
    distinct_image = rows**3 - distinct_quotient
    distinct_kernel = distinct_domain - distinct_image

    assert (triple_same_kernel, double_kernel, distinct_kernel) == (112, 189, 266)

    triple_same_total = rows * triple_same_kernel
    double_total = rows * (rows - 1) * double_kernel
    distinct_total = comb(rows, 3) * distinct_kernel
    common_beta23 = triple_same_total + double_total + distinct_total
    assert (triple_same_total, double_total, distinct_total) == (784, 7938, 9310)
    assert common_beta23 == 18032

    # A column-separated independent term has only q_j^2 times an inactive
    # linear generator, hence no all-distinct-column beta_(2,3) class.
    one_term_same = rows * (rows - 1)
    one_term_double = rows * (rows - 1) * (rows - 1)
    assert (one_term_same, one_term_double) == (42, 252)
    assert one_term_same + one_term_double == 294
    assert signs * (one_term_same + one_term_double) == 18816

    right_rank_ceiling = triple_same_total + double_total
    right_kernel_floor = distinct_total
    target_beta23 = 18816
    quotient_created = target_beta23 - common_beta23
    survivor_ceiling = right_rank_ceiling + quotient_created
    assert (right_rank_ceiling, right_kernel_floor, quotient_created) == (8722, 9310, 784)
    assert survivor_ceiling == 9506
    assert survivor_ceiling < 18523

    # F_2: a is the identity, the right Tor map has rank 540, and z=588.
    f2 = fork_multiplicities(2016, 2016, 588, 2016, 540, 2016)
    assert f2 == (540, 1476, 0, 0, 0, 48)
    f2_pushout_h0 = f2[0] + f2[4] + f2[5]
    assert f2_pushout_h0 == 588

    # In the Glynn diagram a is injective.  The homotopy-pushout H_0 count
    # p+t+w is y+z-x and is independent of the unknown right-map rank q.
    glynn_pushout_h0 = target_beta23 + 18816 - common_beta23
    assert glynn_pushout_h0 == 19600
    assert glynn_pushout_h0 > 64 * 294

    # Fractional target-bar selector: 0<=c_p,c_u,c_t<=1, c_t=1 is always
    # optimal, and the F_2 cap is 540 c_p + 1476 c_u <= 588.  The maximum
    # over 0<=q<=8722 occurs at q=8722, c_p=1, c_u=4/123.
    feasible_vertices = (
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(49, 123)),
        (Fraction(1), Fraction(4, 123)),
    )
    fractional_candidates = []
    selector_candidates = []
    for q_test in range(right_rank_ceiling + 1):
        u_test = common_beta23 - q_test
        for c_p_test, c_u_test in feasible_vertices:
            assert 540 * c_p_test + 1476 * c_u_test <= 588
            value = q_test * c_p_test + u_test * c_u_test + quotient_created
            fractional_candidates.append((value, q_test, c_p_test, c_u_test))
        for c_p_test in (0, 1):
            for c_u_test in (0, 1):
                for c_t_test in (0, 1):
                    if 540 * c_p_test + 1476 * c_u_test <= 588:
                        value = (
                            q_test * c_p_test
                            + u_test * c_u_test
                            + quotient_created * c_t_test
                        )
                        selector_candidates.append(value)

    fractional_max, q, c_p, c_u = max(fractional_candidates)
    c_t = Fraction(1)
    assert (q, c_p, c_u) == (8722, Fraction(1), Fraction(4, 123))
    assert 540 * c_p + 1476 * c_u == 588
    assert fractional_max == Fraction(1206478, 123)
    assert fractional_max < 18523
    assert max(selector_candidates) == survivor_ceiling

    print("GLYNN_COLUMN_BLOCKS", triple_same_total, double_total, distinct_total)
    print("GLYNN_RIGHT_RANK_CEILING", right_rank_ceiling)
    print("GLYNN_TARGET_SURVIVOR_CEILING", survivor_ceiling)
    print("F2_BARCODES_P_U_V_S_T_W", *f2)
    print("F2_PUSHOUT_H0", f2_pushout_h0)
    print("GLYNN_PUSHOUT_H0", glynn_pushout_h0)
    print("FRACTIONAL_TARGET_SELECTOR_MAX", fractional_max)
    print("FORK_BARCODE_AUDIT_PASS")


if __name__ == "__main__":
    main()
