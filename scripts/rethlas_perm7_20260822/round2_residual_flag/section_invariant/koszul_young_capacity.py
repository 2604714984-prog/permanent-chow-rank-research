#!/usr/bin/env python3
"""Exact capacity gate for all standard Koszul--Young maps on the section.

This uses only binomial arithmetic.  The internal one-term ranks are obtained
by decomposing the Boolean Koszul map into simplex boundary blocks.
"""

from fractions import Fraction
from math import ceil, comb


DEGREE = 7
AMBIENT = 48
INACTIVE = AMBIENT - DEGREE
SECTION_HILBERT = (1, 48, 441, 1225, 1225, 441, 48, 1)
# From F^perp=(quadrics)+(one minimal sextic), the first prolongations of
# D_m(F), m=1,...,6, have these dimensions.  At m=5 the new sextic makes
# the prolongation one dimension larger than D_6(F).
SECTION_FIRST_PROLONGATIONS = (1176, 1225, 1225, 441, 49, 1)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def internal_rank(output_degree, wedge_degree):
    """Rank inside the seven-dimensional factor span of one generic atom."""
    total = 0
    for intersection_size in range(min(output_degree - 1, wedge_degree) + 1):
        remainder_size = output_degree + wedge_degree - 2 * intersection_size
        if intersection_size + remainder_size > DEGREE:
            continue
        multiplicity = choose(DEGREE, intersection_size) * choose(
            DEGREE - intersection_size, remainder_size
        )
        simplex_rank = choose(
            remainder_size - 1,
            output_degree - intersection_size - 1,
        )
        total += multiplicity * simplex_rank
    return total


def atom_cap(output_degree, wedge_degree):
    """Exact maximum over all seven-factor Chow atoms in 48 variables."""
    return sum(
        choose(INACTIVE, inactive_wedge)
        * internal_rank(output_degree, wedge_degree - inactive_wedge)
        for inactive_wedge in range(
            max(0, wedge_degree - DEGREE),
            min(INACTIVE, wedge_degree) + 1,
        )
    )


def target_dimension_ceiling(output_degree, wedge_degree):
    source = SECTION_HILBERT[output_degree] * choose(AMBIENT, wedge_degree)
    target = SECTION_HILBERT[output_degree - 1] * choose(
        AMBIENT, wedge_degree + 1
    )
    return min(source, target)


def section_capacity_table():
    rows = []
    for output_degree in range(1, DEGREE + 1):
        for wedge_degree in range(AMBIENT):
            cap = atom_cap(output_degree, wedge_degree)
            ceiling = target_dimension_ceiling(output_degree, wedge_degree)
            rows.append(
                (
                    Fraction(ceiling, cap),
                    output_degree,
                    wedge_degree,
                    ceiling,
                    cap,
                )
            )
    return sorted(rows, reverse=True)


def n4_toy():
    # For perm_4|x_44=0: dim W=15, h_2=36 and h_3=15.  The first
    # Koszul map at (m,p)=(2,1) has kernel the first prolongation.  The
    # coordinate apolar presentation has one new cubic generator, so the
    # prolongation has dimension h_3+1=16.
    ambient = 15
    target_rank = ambient * 36 - 16

    # The internal ranks for a four-factor term are r_(2,1)=20 and
    # r_(2,0)=6; the other 11 variables are inactive.
    atom = 20 + 11 * 6
    return target_rank, atom, Fraction(target_rank, atom)


def main():
    table = section_capacity_table()
    ratio, output_degree, wedge_degree, ceiling, cap = table[0]
    tied = [
        (m, p)
        for value, m, p, _, _ in table
        if value == ratio
    ]

    print("internal_rank_table")
    for m in range(1, DEGREE + 1):
        print(m, [internal_rank(m, p) for p in range(DEGREE + 1)])

    print(
        "section_max",
        f"ratio={ratio.numerator}/{ratio.denominator}",
        f"decimal={float(ratio):.12f}",
        f"ceiling_integer={ceil(ratio)}",
        f"pairs={tied}",
        f"target_dimension_ceiling={ceiling}",
        f"one_atom_cap={cap}",
    )
    assert ratio == Fraction(7_922_320, 134_133)
    assert tied == [(4, 24), (4, 23)]
    assert ratio < 60

    first_koszul_rows = []
    for m, prolongation in enumerate(SECTION_FIRST_PROLONGATIONS, start=1):
        target_rank = AMBIENT * SECTION_HILBERT[m] - prolongation
        cap_p1 = atom_cap(m, 1)
        first_koszul_rows.append(
            (m, prolongation, target_rank, cap_p1, ceil(Fraction(target_rank, cap_p1)))
        )
    print("coordinate_first_prolongation_rows")
    for row in first_koszul_rows:
        print(
            f"m={row[0]}",
            f"prolongation={row[1]}",
            f"target_rank={row[2]}",
            f"one_atom_cap={row[3]}",
            f"ceiling_integer={row[4]}",
        )
    assert first_koszul_rows == [
        (1, 1176, 1128, 308, 4),
        (2, 1225, 19943, 973, 21),
        (3, 1225, 57575, 1645, 35),
        (4, 441, 58359, 1659, 36),
        (5, 49, 21119, 1001, 22),
        (6, 1, 2303, 335, 7),
    ]

    target, atom, toy_ratio = n4_toy()
    print(
        "n4_coordinate_toy",
        f"target_rank={target}",
        f"one_atom_cap={atom}",
        f"ratio={toy_ratio.numerator}/{toy_ratio.denominator}",
        f"ceiling_integer={ceil(toy_ratio)}",
    )
    assert (target, atom, ceil(toy_ratio)) == (524, 86, 7)
    print("SECTION_KOSZUL_YOUNG_CAPACITY_PASS")


if __name__ == "__main__":
    main()
