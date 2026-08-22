#!/usr/bin/env python3
"""Exact arithmetic audit for the row-normal-layer report.

The script checks only finite binomial arithmetic and the combinatorial
dimensions of the two displayed circuit examples.  The symbolic support and
prolongation arguments remain in report.md.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


def exponent_vectors(number_of_variables: int, degree: int, prefix: tuple[int, ...] = ()):
    """Yield all exponent vectors of a fixed total degree."""
    if number_of_variables == 1:
        yield prefix + (degree,)
        return
    for exponent in range(degree + 1):
        yield from exponent_vectors(
            number_of_variables - 1, degree - exponent, prefix + (exponent,)
        )


class WeightedUnionFind:
    """Exact multiplicative relations between scalar coefficients."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.weight = [Fraction(1)] * size
        self.forced_zero = [False] * size

    def find(self, item: int) -> tuple[int, Fraction]:
        parent = self.parent[item]
        if parent != item:
            root, parent_weight = self.find(parent)
            self.weight[item] *= parent_weight
            self.parent[item] = root
        return self.parent[item], self.weight[item]

    def mark_zero(self, item: int) -> None:
        root, _ = self.find(item)
        self.forced_zero[root] = True

    def equate(self, left: int, left_scale: int, right: int, right_scale: int) -> None:
        """Impose left_scale * left = right_scale * right."""
        left_root, left_weight = self.find(left)
        right_root, right_weight = self.find(right)
        if left_root == right_root:
            if left_scale * left_weight != right_scale * right_weight:
                self.forced_zero[left_root] = True
            return

        ratio = Fraction(right_scale * right_weight, left_scale * left_weight)
        if self.rank[left_root] > self.rank[right_root]:
            self.parent[right_root] = left_root
            self.weight[right_root] = 1 / ratio
            self.forced_zero[left_root] |= self.forced_zero[right_root]
        else:
            self.parent[left_root] = right_root
            self.weight[left_root] = ratio
            self.forced_zero[right_root] |= self.forced_zero[left_root]
            if self.rank[left_root] == self.rank[right_root]:
                self.rank[right_root] += 1


def universal_polar_prolongation_dimension(n: int, m: int) -> tuple[int, int]:
    """Exact coefficient-graph audit of (D_m G_n)^(1).

    G_n = sum_a e_a product_(b != a) y_b.  The ambient candidate has
    U-valued y-degree m+1.  For every derivative direction y_j we impose
    that the derivative lies in the span of
    g_R = sum_(a in R) e_a y_(R without a), |R|=m+1.
    """
    monomials = list(exponent_vectors(n, m + 1))
    variables = {
        (u_index, exponents): index
        for index, (u_index, exponents) in enumerate(
            (pair for pair in ((a, alpha) for a in range(n) for alpha in monomials))
        )
    }
    relations = WeightedUnionFind(len(variables))
    derivative_monomials = list(exponent_vectors(n, m))

    for derivative_index in range(n):
        # Coordinates outside the squarefree linked support of D_m G_n vanish.
        for u_index in range(n):
            for beta in derivative_monomials:
                valid = all(exponent in (0, 1) for exponent in beta) and beta[u_index] == 0
                alpha = list(beta)
                alpha[derivative_index] += 1
                variable = variables[u_index, tuple(alpha)]
                if not valid:
                    relations.mark_zero(variable)

        # Within each R-block all linked coefficients are equal.
        for subset in combinations(range(n), m + 1):
            entries = []
            for u_index in subset:
                beta = tuple(
                    int(index in subset and index != u_index) for index in range(n)
                )
                alpha = list(beta)
                alpha[derivative_index] += 1
                entries.append(
                    (
                        variables[u_index, tuple(alpha)],
                        beta[derivative_index] + 1,
                    )
                )
            first_variable, first_scale = entries[0]
            for variable, scale in entries[1:]:
                relations.equate(first_variable, first_scale, variable, scale)

    roots = set()
    for variable in range(len(variables)):
        root, _ = relations.find(variable)
        roots.add(root)
    dimension = sum(not relations.forced_zero[root] for root in roots)
    return dimension, len(variables)


def scalar_table() -> list[dict[str, int]]:
    rows = []
    for m in range(7):
        cap_zero = comb(7, m + 1)
        cap_one = comb(6, m)
        target = cap_zero * cap_one
        rows.append(
            {
                "m": m,
                "target": target,
                "nu0_cap": cap_zero,
                "nu1_cap": cap_one,
            }
        )
    return rows


def koszul_table() -> list[dict[str, int | Fraction]]:
    rows = []
    for m in range(1, 6):
        target_m = comb(6, m) * comb(7, m + 1)
        target_next = comb(6, m + 1) * comb(7, m + 2)
        cap_zero_m = comb(7, m + 1)
        cap_zero_next = comb(7, m + 2)
        cap_one_m = comb(6, m)
        cap_one_next = comb(6, m + 1)

        target = 42 * target_m - target_next
        cap_zero = 42 * cap_zero_m - cap_zero_next
        cap_one = 42 * cap_one_m - cap_one_next
        rows.append(
            {
                "m": m,
                "target": target,
                "nu0_cap": cap_zero,
                "nu1_cap": cap_one,
                "ratio": Fraction(target, max(cap_zero, cap_one)),
            }
        )
    return rows


def main() -> None:
    scalar = scalar_table()
    assert [row["target"] for row in scalar] == [7, 126, 525, 700, 315, 42, 1]
    assert [row["nu0_cap"] for row in scalar] == [7, 21, 35, 35, 21, 7, 1]
    assert [row["nu1_cap"] for row in scalar] == [1, 6, 15, 20, 15, 6, 1]
    assert all(row["nu0_cap"] >= row["nu1_cap"] for row in scalar)
    scalar_ratio = max(Fraction(row["target"], row["nu0_cap"]) for row in scalar)
    assert scalar_ratio == 20

    koszul = koszul_table()
    assert [row["target"] for row in koszul] == [4767, 21350, 29085, 13188, 1763]
    assert [row["nu0_cap"] for row in koszul] == [847, 1435, 1449, 875, 293]
    assert [row["nu1_cap"] for row in koszul] == [237, 610, 825, 624, 251]
    assert all(row["nu0_cap"] >= row["nu1_cap"] for row in koszul)
    koszul_ratio = max(row["ratio"] for row in koszul)
    assert koszul_ratio == Fraction(29085, 1449)
    assert 20 < koszul_ratio < 21

    prolongation_audit = []
    for m in range(1, 6):
        dimension, candidate_count = universal_polar_prolongation_dimension(7, m)
        assert candidate_count <= 6468
        assert dimension == comb(7, m + 2)
        prolongation_audit.append(
            {"m": m, "candidate_count": candidate_count, "dimension": dimension}
        )

    # A proportional pair has one seven-dimensional deletion module.
    proportional_pair_deletion_dimension = comb(7, 6)
    assert proportional_pair_deletion_dimension == 7

    # Q*a + Q*b - Q*(a+b): one deletion of the last factor and two
    # independent directions for each of the six common-factor deletions.
    three_circuit_deletion_dimension = 1 + 2 * 6
    assert three_circuit_deletion_dimension == 13

    print("scalar_table", scalar)
    print("koszul_table", koszul)
    print("scalar_ceiling", scalar_ratio)
    print("koszul_ceiling", koszul_ratio, float(koszul_ratio))
    print("universal_polar_prolongations", prolongation_audit)
    print("pair_deletion_dimension", proportional_pair_deletion_dimension)
    print("three_circuit_deletion_dimension", three_circuit_deletion_dimension)
    print("NORMAL_LAYER_AUDIT_PASS")


if __name__ == "__main__":
    main()
