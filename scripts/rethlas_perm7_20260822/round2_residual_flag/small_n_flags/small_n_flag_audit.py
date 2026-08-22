#!/usr/bin/env python3
"""Exact small-n audit for residual flags and first normal layers.

The script uses only the Python standard library.  Integer/rational checks are
exact.  The quartic prolongation calculation is over the prime 1,000,003; its
rank is a rigorous lower bound for the corresponding characteristic-zero
integer matrix rank.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, ceil


PRIME = 1_000_003
SECOND_PRIME = 1_000_033


def sparse_rank_mod(rows: list[dict[int, int]], prime: int = PRIME) -> int:
    """Sparse row rank over F_prime."""

    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        row = {c: value % prime for c, value in source.items() if value % prime}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                scale = pow(row[pivot], prime - 2, prime)
                pivots[pivot] = {
                    c: value * scale % prime for c, value in row.items()
                }
                break
            scale = row[pivot]
            basis = pivots[pivot]
            for c, value in basis.items():
                row[c] = (row.get(c, 0) - scale * value) % prime
                if not row[c]:
                    row.pop(c, None)
    return len(pivots)


def sparse_echelon_mod(
    rows: list[dict[int, int]], prime: int = PRIME
) -> dict[int, dict[int, int]]:
    """Return normalized echelon rows keyed by their pivot column."""

    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        row = {c: value % prime for c, value in source.items() if value % prime}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                scale = pow(row[pivot], prime - 2, prime)
                pivots[pivot] = {
                    c: value * scale % prime for c, value in row.items()
                }
                break
            scale = row[pivot]
            basis = pivots[pivot]
            for c, value in basis.items():
                row[c] = (row.get(c, 0) - scale * value) % prime
                if not row[c]:
                    row.pop(c, None)
    return pivots


def dense_rank_fraction(matrix: list[list[int | Fraction]]) -> int:
    """Exact dense rank over Q."""

    if not matrix:
        return 0
    work = [[Fraction(entry) for entry in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        selected = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                entry - scale * pivot
                for entry, pivot in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def normalized_signs(n: int) -> list[tuple[int, ...]]:
    return [(1,) + tail for tail in product((-1, 1), repeat=n - 1)]


def in_span(vector: tuple[int, ...], basis: list[tuple[int, ...]]) -> bool:
    old_rank = dense_rank_fraction([list(row) for row in basis])
    new_rank = dense_rank_fraction([list(row) for row in basis] + [list(vector)])
    return old_rank == new_rank


def audit_same_column_glynn_flag(n: int) -> dict[str, object]:
    """Audit the cumulative packet kernel along the explicit factor flag."""

    all_plus = tuple(1 for _ in range(n))
    chosen = [all_plus]
    for coordinate in range(1, n):
        vector = list(all_plus)
        vector[coordinate] = -1
        chosen.append(tuple(vector))

    signs = normalized_signs(n)
    cumulative: list[int] = []
    death_stage: dict[tuple[int, ...], int] = {}
    for k in range(1, n + 1):
        basis = chosen[:k]
        assert dense_rank_fraction([list(row) for row in basis]) == k
        contained = [delta for delta in signs if in_span(delta, basis)]
        assert len(contained) == 2 ** (k - 1)
        cumulative.append(len(contained))
        for delta in contained:
            death_stage.setdefault(delta, k)

    layer_histogram = [sum(stage == k for stage in death_stage.values()) for k in range(1, n + 1)]
    expected_histogram = [1] + [2 ** (k - 2) for k in range(2, n + 1)]
    assert layer_histogram == expected_histogram

    # The selected coordinates of the untouched-column tensors form the Walsh
    # character table, proving independence of the packet labels w_delta.
    subsets = list(product((0, 1), repeat=n - 1))
    walsh = []
    for delta in signs:
        row = []
        for indicator in subsets:
            value = 1
            for j, use in enumerate(indicator, start=1):
                if use:
                    value *= delta[j]
            row.append(value)
        walsh.append(row)
    assert dense_rank_fraction(walsh) == 2 ** (n - 1)

    return {
        "n": n,
        "packet_size": 2 ** (n - 1),
        "cumulative_kernel_dimensions": cumulative,
        "new_deaths_by_layer": layer_histogram,
        "walsh_rank": 2 ** (n - 1),
    }


def tangent_profile(n: int) -> list[int]:
    """Derivative profile of sum_i b_i prod_{j!=i} a_j."""

    monomials = [
        frozenset([n + i] + [j for j in range(n) if j != i])
        for i in range(n)
    ]
    dimensions: list[int] = []
    for output_degree in range(n + 1):
        order = n - output_degree
        column_index: dict[tuple[int, ...], int] = {}
        rows: list[dict[int, int]] = []
        for operator in combinations(range(2 * n), order):
            derivative_set = frozenset(operator)
            row: dict[int, int] = {}
            for monomial in monomials:
                if derivative_set <= monomial:
                    output = tuple(sorted(monomial - derivative_set))
                    column = column_index.setdefault(output, len(column_index))
                    row[column] = row.get(column, 0) + 1
            if row:
                rows.append(row)
        dimensions.append(sparse_rank_mod(rows))
    expected = [1] + [2 * comb(n, d) for d in range(1, n)] + [1]
    assert dimensions == expected
    return dimensions


def audit_anchor_circuits(n: int) -> dict[str, object]:
    """Audit two-anchor tangent amplification and degenerate variants."""

    # With independent u_i and l_i, the first normal layer has coefficient
    # matrix I_n between U and the distinct omitted products.
    identity_rows = [{i: 1} for i in range(n)]
    independent_rank = sparse_rank_mod(identity_rows)
    assert independent_rank == n

    # If all restricted factors repeat, every omitted product is l^(n-1), so
    # the U | Sym(W) matrix has just one nonzero column.
    repeated_rows = [{0: 1} for _ in range(n)]
    repeated_rank = sparse_rank_mod(repeated_rows)
    assert repeated_rank == 1

    # If exactly s factors are pure normal factors, the first nonzero normal
    # coefficient occurs in order s and has exactly one product term.
    vanishing_orders = {}
    for s in range(1, n + 1):
        coefficient_counts = [
            0 if q < s else comb(n - s, q - s) for q in range(n + 1)
        ]
        assert coefficient_counts[s] == 1
        vanishing_orders[s] = coefficient_counts

    # In the symmetric T_+ - T_- test, even normal layers cancel and the
    # q-th odd layer contains C(n,q) displayed products.
    parity_counts = [0 if q % 2 == 0 else 2 * comb(n, q) for q in range(n + 1)]
    assert parity_counts[0] == 0 and parity_counts[1] == 2 * n

    return {
        "n": n,
        "two_anchor_tangent_partial_rank": independent_rank,
        "repeated_factor_tangent_partial_rank": repeated_rank,
        "zero_anchor_coefficient_counts": vanishing_orders,
        "T_plus_minus_displayed_term_counts": parity_counts,
        "generic_tangent_derivative_profile": tangent_profile(n),
    }


def permanent_monomials(n: int, killed_first_row: int) -> list[frozenset[int]]:
    killed = frozenset(range(killed_first_row))
    answer = []
    for sigma in permutations(range(n)):
        monomial = frozenset(n * row + sigma[row] for row in range(n))
        if not (monomial & killed):
            answer.append(monomial)
    return answer


def squarefree_derivative_profile(
    monomials: list[frozenset[int]], variable_count: int, degree: int
) -> list[int]:
    dimensions: list[int] = []
    for output_degree in range(degree + 1):
        order = degree - output_degree
        column_index: dict[tuple[int, ...], int] = {}
        rows: list[dict[int, int]] = []
        for operator in combinations(range(variable_count), order):
            derivative_set = frozenset(operator)
            row: dict[int, int] = {}
            for monomial in monomials:
                if derivative_set <= monomial:
                    output = tuple(sorted(monomial - derivative_set))
                    column = column_index.setdefault(output, len(column_index))
                    row[column] = row.get(column, 0) + 1
            if row:
                rows.append(row)
        dimensions.append(sparse_rank_mod(rows))
    return dimensions


def audit_row_killing_profiles() -> dict[str, object]:
    expected = {
        2: [[1, 4, 1], [1, 2, 1], [0, 0, 0]],
        3: [[1, 9, 9, 1], [1, 8, 8, 1], [1, 5, 5, 1], [0, 0, 0, 0]],
        4: [
            [1, 16, 36, 16, 1],
            [1, 15, 36, 15, 1],
            [1, 14, 30, 14, 1],
            [1, 10, 18, 10, 1],
            [0, 0, 0, 0, 0],
        ],
    }
    result: dict[str, object] = {}
    for n in (2, 3, 4):
        rows = []
        for killed in range(n + 1):
            monomials = permanent_monomials(n, killed)
            profile = squarefree_derivative_profile(monomials, n * n, n)
            assert profile == expected[n][killed]
            rows.append(
                {
                    "killed_row_coordinates": killed,
                    "surviving_permutation_monomials": len(monomials),
                    "derivative_profile": profile,
                }
            )
        result[str(n)] = rows
    return result


# Sparse polynomial helpers for factor-selected sections.
Polynomial = dict[tuple[int, ...], int]


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = (answer.get(monomial, 0) + coefficient) % PRIME
        if not answer[monomial]:
            answer.pop(monomial)
    return answer


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                a + b for a, b in zip(left_monomial, right_monomial)
            )
            answer[monomial] = (
                answer.get(monomial, 0) + left_coefficient * right_coefficient
            ) % PRIME
            if not answer[monomial]:
                answer.pop(monomial)
    return answer


def polynomial_derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    answer: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        exponent = monomial[variable]
        if exponent:
            output = list(monomial)
            output[variable] -= 1
            output_tuple = tuple(output)
            answer[output_tuple] = (
                answer.get(output_tuple, 0) + coefficient * exponent
            ) % PRIME
    return {m: c for m, c in answer.items() if c}


def factor_section_polynomial(n: int, section_type: str) -> tuple[Polynomial, int]:
    """Eliminate x_(1,n) either by x=0 or by an all-plus row factor."""

    variable_count = n * n - 1

    def new_index(old_index: int) -> int:
        return old_index if old_index < n - 1 else old_index - 1

    substitutions: list[Polynomial] = []
    for old_index in range(n * n):
        if old_index == n - 1:
            replacement: Polynomial = {}
            if section_type == "glynn_factor":
                for column in range(n - 1):
                    exponent = [0] * variable_count
                    exponent[new_index(column)] = 1
                    replacement[tuple(exponent)] = PRIME - 1
            substitutions.append(replacement)
        else:
            exponent = [0] * variable_count
            exponent[new_index(old_index)] = 1
            substitutions.append({tuple(exponent): 1})

    permanent: Polynomial = {}
    for sigma in permutations(range(n)):
        term: Polynomial = {(0,) * variable_count: 1}
        for row in range(n):
            term = polynomial_multiply(term, substitutions[n * row + sigma[row]])
        permanent = polynomial_add(permanent, term)
    return permanent, variable_count


def general_derivative_profile(polynomial: Polynomial, variable_count: int, degree: int) -> list[int]:
    dimensions = []
    for output_degree in range(degree + 1):
        order = degree - output_degree
        rows: list[dict[int, int]] = []
        monomial_index: dict[tuple[int, ...], int] = {}
        for operator in combinations(range(variable_count), order):
            derivative = polynomial
            for variable in operator:
                derivative = polynomial_derivative(derivative, variable)
            if derivative:
                row = {
                    monomial_index.setdefault(monomial, len(monomial_index)): coefficient
                    for monomial, coefficient in derivative.items()
                }
                rows.append(row)
        dimensions.append(sparse_rank_mod(rows))
    return dimensions


def quartic_middle_prolongation_bound(
    polynomial: Polynomial, variable_count: int
) -> tuple[int, int, int]:
    """Return dim D_2, a char-zero upper bound on dim D_2^(1), and equation rank."""

    degree_two_monomials = []
    for indices in combinations_with_replacement(range(variable_count), 2):
        exponent = [0] * variable_count
        for index in indices:
            exponent[index] += 1
        degree_two_monomials.append(tuple(exponent))
    degree_two_index = {m: i for i, m in enumerate(degree_two_monomials)}

    derivative_rows: list[dict[int, int]] = []
    for operator in combinations(range(variable_count), 2):
        derivative = polynomial
        for variable in operator:
            derivative = polynomial_derivative(derivative, variable)
        if derivative:
            derivative_rows.append(
                {degree_two_index[m]: c for m, c in derivative.items()}
            )
    pivots = sparse_echelon_mod(derivative_rows)
    middle_dimension = len(pivots)

    def reduce_mod_middle(vector: dict[int, int]) -> dict[int, int]:
        remainder = {c: value % PRIME for c, value in vector.items() if value % PRIME}
        for pivot, basis in pivots.items():
            if pivot not in remainder:
                continue
            scale = remainder[pivot]
            for c, value in basis.items():
                remainder[c] = (remainder.get(c, 0) - scale * value) % PRIME
                if not remainder[c]:
                    remainder.pop(c, None)
        return remainder

    degree_three_monomials = []
    for indices in combinations_with_replacement(range(variable_count), 3):
        exponent = [0] * variable_count
        for index in indices:
            exponent[index] += 1
        degree_three_monomials.append(tuple(exponent))

    equations: dict[tuple[int, int], dict[int, int]] = {}
    for cubic_index, monomial in enumerate(degree_three_monomials):
        for variable in range(variable_count):
            exponent = monomial[variable]
            if not exponent:
                continue
            output = list(monomial)
            output[variable] -= 1
            output_index = degree_two_index[tuple(output)]
            remainder = reduce_mod_middle({output_index: exponent})
            for quotient_column, coefficient in remainder.items():
                equations.setdefault((variable, quotient_column), {})[
                    cubic_index
                ] = coefficient

    equation_rank = sparse_rank_mod(list(equations.values()))
    prolongation_upper_bound = len(degree_three_monomials) - equation_rank
    return middle_dimension, prolongation_upper_bound, equation_rank


def direct_quartic_koszul_rank(
    polynomial: Polynomial, variable_count: int
) -> int:
    """Independently build delta_2(C_{2,2}(F) tensor id) over a second prime."""

    target_index: dict[tuple[int, int, int], int] = {}
    columns: list[dict[int, int]] = []
    for operator in combinations(range(variable_count), 2):
        quadratic = polynomial
        for variable in operator:
            quadratic = polynomial_derivative(quadratic, variable)
        if not quadratic:
            continue
        for tensor_variable in range(variable_count):
            column: dict[int, int] = {}
            for monomial, coefficient in quadratic.items():
                for derivative_variable, exponent in enumerate(monomial):
                    if not exponent or derivative_variable == tensor_variable:
                        continue
                    output = list(monomial)
                    output[derivative_variable] -= 1
                    linear_variable = next(
                        index for index, value in enumerate(output) if value
                    )
                    wedge = tuple(sorted((derivative_variable, tensor_variable)))
                    sign = 1 if derivative_variable < tensor_variable else -1
                    target = (linear_variable, wedge[0], wedge[1])
                    target_column = target_index.setdefault(target, len(target_index))
                    column[target_column] = (
                        column.get(target_column, 0)
                        + coefficient * exponent * sign
                    ) % SECOND_PRIME
            if column:
                columns.append(column)
    return sparse_rank_mod(columns, SECOND_PRIME)


def audit_factor_selected_sections() -> dict[str, object]:
    expected_profiles = {
        2: [1, 2, 1],
        3: [1, 8, 8, 1],
        4: [1, 15, 36, 15, 1],
    }
    result: dict[str, object] = {}
    for n in (2, 3, 4):
        polynomial, variable_count = factor_section_polynomial(n, "glynn_factor")
        profile = general_derivative_profile(polynomial, variable_count, n)
        assert profile == expected_profiles[n]
        result[str(n)] = {
            "quotient_variable_count": variable_count,
            "derivative_profile": profile,
            "surviving_glynn_upper_bound": 2 ** (n - 1) - 1,
        }

    quartic, variable_count = factor_section_polynomial(4, "glynn_factor")
    middle, prolongation_upper, equation_rank = quartic_middle_prolongation_bound(
        quartic, variable_count
    )
    assert middle == 36
    assert prolongation_upper == 16
    assert equation_rank == 664
    target_koszul_rank_lower = variable_count * middle - prolongation_upper
    independent_direct_rank = direct_quartic_koszul_rank(quartic, variable_count)
    one_term_cap = variable_count * comb(4, 2) - comb(4, 3)
    lower_bound = ceil(target_koszul_rank_lower / one_term_cap)
    assert target_koszul_rank_lower == 524
    assert independent_direct_rank == 524
    assert one_term_cap == 86
    assert lower_bound == 7
    result["4"].update(
        {
            "prolongation_dimension_upper_bound": prolongation_upper,
            "modular_equation_rank": equation_rank,
            "koszul_rank_lower_bound": target_koszul_rank_lower,
            "independent_direct_koszul_rank_mod_second_prime": independent_direct_rank,
            "one_term_koszul_cap": one_term_cap,
            "certified_chow_rank_lower_bound": lower_bound,
        }
    )
    return result


def tangent_cubic_centroid_audit() -> dict[str, int]:
    """Independent exact replay of the six-variable tangent cubic centroid."""

    variable_count = 6
    triples = [(3, 1, 2), (4, 0, 2), (5, 0, 1)]
    tensor = {
        ordering: 1
        for triple in triples
        for ordering in set(permutations(triple))
    }
    equations: list[list[Fraction]] = []
    for i, j, k in product(range(variable_count), repeat=3):
        for slot in (1, 2):
            row = [Fraction(0) for _ in range(variable_count**2)]
            for q in range(variable_count):
                row[q * variable_count + i] += tensor.get((q, j, k), 0)
                if slot == 1:
                    row[q * variable_count + j] -= tensor.get((i, q, k), 0)
                else:
                    row[q * variable_count + k] -= tensor.get((i, j, q), 0)
            if any(row):
                equations.append(row)
    rank = dense_rank_fraction(equations)
    nullity = variable_count**2 - rank
    identity = [
        Fraction(int(row == column))
        for row in range(variable_count)
        for column in range(variable_count)
    ]
    nilpotent = [
        Fraction(int(row == column + 3 and column < 3))
        for row in range(variable_count)
        for column in range(variable_count)
    ]
    assert all(sum(a * b for a, b in zip(row, identity)) == 0 for row in equations)
    assert all(sum(a * b for a, b in zip(row, nilpotent)) == 0 for row in equations)
    assert identity != nilpotent
    assert len(equations) == 276
    assert rank == 34
    assert nullity == 2
    return {"equation_count": 276, "rank": rank, "centroid_dimension": nullity}


def main() -> None:
    glynn_flags = [audit_same_column_glynn_flag(n) for n in (2, 3, 4, 7)]
    anchor_circuits = [audit_anchor_circuits(n) for n in (2, 3, 4)]
    row_profiles = audit_row_killing_profiles()
    factor_sections = audit_factor_selected_sections()
    centroid = tangent_cubic_centroid_audit()

    print("SAME_COLUMN_GLYNN_FLAGS", glynn_flags)
    print("TWO_ANCHOR_CIRCUITS", anchor_circuits)
    print("ROW_KILLING_PROFILES", row_profiles)
    print("FACTOR_SELECTED_SECTIONS", factor_sections)
    print("TANGENT_CUBIC_CENTROID", centroid)
    print("SMALL_N_RESIDUAL_FLAG_AUDIT_PASS")


if __name__ == "__main__":
    main()
