#!/usr/bin/env python3
"""Audit the apolar multiplication-tensor framework for Chow decompositions.

The mathematical statements are proved in
`docs/general_apolar_multiplication_tensor_framework.md`.

The finite audit checks:

* the Boolean top-pairing model for dependent and independent Chow terms;
* the diagonal-Segre multiplication table for the permanent apolar algebra;
* exact dimension identities and baseline tensor-rank arithmetic; and
* the strict comparison with the already known central-binomial profile.

All theorem-facing finite arithmetic is exact over the rationals or integers.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Iterable


EXPECTED_CORE_SHA256 = "c08cb4506bea294754c630e8b711747279b68b75fae64b82d8fdae6f66477f41"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def compositions(total: int, length: int) -> tuple[tuple[int, ...], ...]:
    if length == 1:
        return ((total,),)
    result = []
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            result.append((first, *tail))
    return tuple(result)


def matrix_rank(matrix: Iterable[Iterable[int | Fraction]]) -> int:
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][column]
        rows[rank] = [entry / value for entry in rows[rank]]
        for index in range(row_count):
            if index == rank or not rows[index][column]:
                continue
            factor = rows[index][column]
            rows[index] = [
                rows[index][entry] - factor * rows[rank][entry]
                for entry in range(column_count)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def independent_column_indices(matrix: list[list[int | Fraction]]) -> tuple[int, ...]:
    if not matrix or not matrix[0]:
        return ()
    selected: list[int] = []
    current: list[list[int | Fraction]] = [[] for _ in matrix]
    current_rank = 0
    for column in range(len(matrix[0])):
        candidate = [
            [*current[row], matrix[row][column]]
            for row in range(len(matrix))
        ]
        candidate_rank = matrix_rank(candidate)
        if candidate_rank > current_rank:
            selected.append(column)
            current = candidate
            current_rank = candidate_rank
    return tuple(selected)


def multiply_polynomial(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(
                left_exp[index] + right_exp[index]
                for index in range(len(left_exp))
            )
            result[exponent] = (
                result.get(exponent, 0)
                + left_coefficient * right_coefficient
            )
    return {key: value for key, value in result.items() if value}


def product_of_factors(
    factors: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], int]:
    variable_count = len(factors[0])
    polynomial = {(0,) * variable_count: 1}
    for factor in factors:
        linear = {
            tuple(1 if index == variable else 0 for index in range(variable_count)): coefficient
            for variable, coefficient in enumerate(factor)
            if coefficient
        }
        polynomial = multiply_polynomial(polynomial, linear)
    return polynomial


def catalecticant_rank(
    polynomial: dict[tuple[int, ...], int],
    variable_count: int,
    degree: int,
    total_degree: int,
) -> int:
    source = compositions(degree, variable_count)
    target = compositions(total_degree - degree, variable_count)
    matrix = []
    for target_exp in target:
        row = []
        for source_exp in source:
            full_exp = tuple(
                source_exp[index] + target_exp[index]
                for index in range(variable_count)
            )
            coefficient = polynomial.get(full_exp, 0)
            derivative_factor = 1
            for full, remaining in zip(full_exp, target_exp, strict=True):
                derivative_factor *= factorial(full) // factorial(remaining)
            row.append(coefficient * derivative_factor)
        matrix.append(row)
    return matrix_rank(matrix)


def squarefree_multiply(
    state: dict[int, int],
    linear_coefficients: tuple[int, ...],
) -> dict[int, int]:
    output: dict[int, int] = {}
    for mask, coefficient in state.items():
        for index, scalar in enumerate(linear_coefficients):
            bit = 1 << index
            if scalar and not mask & bit:
                output[mask | bit] = (
                    output.get(mask | bit, 0)
                    + coefficient * scalar
                )
    return output


def psi_vector(
    differential_monomial: tuple[int, ...],
    factors: tuple[tuple[int, ...], ...],
    subset_index: dict[int, int],
) -> list[int]:
    state = {0: 1}
    for variable, exponent in enumerate(differential_monomial):
        coefficients = tuple(factor[variable] for factor in factors)
        for _ in range(exponent):
            state = squarefree_multiply(state, coefficients)
    vector = [0] * len(subset_index)
    for mask, coefficient in state.items():
        if mask in subset_index:
            vector[subset_index[mask]] = coefficient
    return vector


def boolean_pairing_rank(
    factors: tuple[tuple[int, ...], ...],
    degree: int,
) -> tuple[int, int, int]:
    n = len(factors)
    variable_count = len(factors[0])
    complement_degree = n - degree
    degree_masks = [
        mask
        for mask in range(1 << n)
        if mask.bit_count() == degree
    ]
    complement_masks = [
        mask
        for mask in range(1 << n)
        if mask.bit_count() == complement_degree
    ]
    degree_index = {mask: index for index, mask in enumerate(degree_masks)}
    complement_index = {
        mask: index for index, mask in enumerate(complement_masks)
    }

    degree_monomials = compositions(degree, variable_count)
    complement_monomials = compositions(complement_degree, variable_count)

    degree_matrix = [
        psi_vector(monomial, factors, degree_index)
        for monomial in degree_monomials
    ]
    complement_matrix = [
        psi_vector(monomial, factors, complement_index)
        for monomial in complement_monomials
    ]

    degree_columns = [
        [degree_matrix[column][row] for column in range(len(degree_matrix))]
        for row in range(len(degree_masks))
    ]
    complement_columns = [
        [
            complement_matrix[column][row]
            for column in range(len(complement_matrix))
        ]
        for row in range(len(complement_masks))
    ]
    degree_basis_indices = independent_column_indices(degree_columns)
    complement_basis_indices = independent_column_indices(complement_columns)

    degree_basis = [
        [degree_columns[row][column] for row in range(len(degree_masks))]
        for column in degree_basis_indices
    ]
    complement_basis = [
        [
            complement_columns[row][column]
            for row in range(len(complement_masks))
        ]
        for column in complement_basis_indices
    ]

    full_mask = (1 << n) - 1
    pairing = []
    for left in degree_basis:
        row = []
        for right in complement_basis:
            value = 0
            for left_index, left_mask in enumerate(degree_masks):
                complement_mask = full_mask ^ left_mask
                right_index = complement_index[complement_mask]
                value += left[left_index] * right[right_index]
            row.append(value)
        pairing.append(row)

    return (
        matrix_rank(pairing),
        len(degree_basis),
        len(complement_basis),
    )


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def permanent_basis(n: int) -> tuple[tuple[int, int], ...]:
    basis = []
    for degree in range(n + 1):
        row_masks = [
            mask for mask in range(1 << n) if mask.bit_count() == degree
        ]
        for row_mask in row_masks:
            for column_mask in row_masks:
                basis.append((row_mask, column_mask))
    return tuple(basis)


def permanent_product(
    left: tuple[int, int],
    right: tuple[int, int],
) -> tuple[int, int] | None:
    if left[0] & right[0] or left[1] & right[1]:
        return None
    return left[0] | right[0], left[1] | right[1]


def build_payload() -> dict[str, object]:
    factor_examples = {
        "power_4": ((1,), (1,), (1,), (1,)),
        "dependent_cubic": ((1, 0), (0, 1), (1, 1)),
        "dependent_quartic": (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 1),
        ),
        "independent_quartic": (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        ),
    }

    pairing_checks = 0
    factor_rows = []
    for name, factors in factor_examples.items():
        n = len(factors)
        variable_count = len(factors[0])
        polynomial = product_of_factors(factors)
        hilbert = []
        ambient_subalgebra_dimensions = []
        for degree in range(n + 1):
            direct_rank = catalecticant_rank(
                polynomial,
                variable_count,
                degree,
                n,
            )
            pairing_rank, left_dimension, right_dimension = boolean_pairing_rank(
                factors,
                degree,
            )
            require(direct_rank == pairing_rank, (
                name,
                degree,
                direct_rank,
                pairing_rank,
            ))
            require(pairing_rank <= left_dimension, (
                name,
                degree,
                pairing_rank,
                left_dimension,
            ))
            require(pairing_rank <= right_dimension, (
                name,
                degree,
                pairing_rank,
                right_dimension,
            ))
            hilbert.append(pairing_rank)
            ambient_subalgebra_dimensions.append(left_dimension)
            pairing_checks += 1
        require(hilbert == list(reversed(hilbert)), (name, hilbert))
        require(sum(hilbert) <= 2**n, (name, hilbert))
        factor_rows.append(
            {
                "name": name,
                "n": n,
                "variable_count": variable_count,
                "hilbert": hilbert,
                "boolean_subalgebra_dimensions": ambient_subalgebra_dimensions,
                "factor_sha256": canonical_sha256(factors),
            }
        )

    multiplication_checks = 0
    associativity_checks = 0
    permanent_rows = []
    for n in range(1, 7):
        basis = permanent_basis(n)
        expected_dimension = comb(2 * n, n)
        require(len(basis) == expected_dimension, (n, len(basis)))
        vandermonde = sum(comb(n, degree) ** 2 for degree in range(n + 1))
        require(vandermonde == expected_dimension, (n, vandermonde))

        sample = basis if len(basis) <= 252 else basis[:126]
        for left in sample:
            for right in sample:
                product = permanent_product(left, right)
                if product is not None:
                    require(
                        product[0].bit_count() == product[1].bit_count(),
                        (n, left, right, product),
                    )
                multiplication_checks += 1

        triple_sample = sample[: min(30, len(sample))]
        for first in triple_sample:
            for second in triple_sample:
                for third in triple_sample:
                    left_product = permanent_product(first, second)
                    right_product = permanent_product(second, third)
                    left_associated = (
                        None
                        if left_product is None
                        else permanent_product(left_product, third)
                    )
                    right_associated = (
                        None
                        if right_product is None
                        else permanent_product(first, right_product)
                    )
                    require(left_associated == right_associated, (
                        n,
                        first,
                        second,
                        third,
                    ))
                    associativity_checks += 1

        permanent_rows.append(
            {
                "n": n,
                "dimension": expected_dimension,
                "hilbert": [comb(n, degree) ** 2 for degree in range(n + 1)],
                "basis_sha256": canonical_sha256(basis),
            }
        )

    arithmetic_checks = 0
    bound_rows = []
    for n in range(1, 41):
        dimension = comb(2 * n, n)
        boolean_border_rank = 2**n
        border_bound = ceil_div(dimension, boolean_border_rank)
        central = comb(n, n // 2)
        require(border_bound <= central, (n, border_bound, central))

        boolean_ordinary_upper = (n + 2) * 2 ** (n - 1)
        ordinary_bound = ceil_div(
            2 * dimension - 1,
            boolean_ordinary_upper,
        )
        require(ordinary_bound <= border_bound, (
            n,
            ordinary_bound,
            border_bound,
        ))
        self_contained_ordinary = ceil_div(
            2 * dimension - 1,
            3**n,
        )
        require(self_contained_ordinary <= ordinary_bound, (
            n,
            self_contained_ordinary,
            ordinary_bound,
        ))

        bound_rows.append(
            {
                "n": n,
                "apolar_dimension": dimension,
                "central_binomial": central,
                "boolean_border_rank": boolean_border_rank,
                "border_chow_bound": border_bound,
                "boolean_ordinary_upper_W": boolean_ordinary_upper,
                "ordinary_chow_bound_W": ordinary_bound,
                "boolean_ordinary_upper_tensor_product": 3**n,
                "ordinary_chow_bound_tensor_product": self_contained_ordinary,
            }
        )
        arithmetic_checks += 3

    require(pairing_checks == 19, pairing_checks)
    require(multiplication_checks == 84_720, multiplication_checks)
    require(associativity_checks == 89_224, associativity_checks)
    require(arithmetic_checks == 120, arithmetic_checks)

    core: dict[str, object] = {
        "status": [
            "GENERAL_CHOW_TERM_BOOLEAN_ALGEBRA_SUBQUOTIENT",
            "GENERAL_APOLAR_MULTIPLICATION_TENSOR_INEQUALITY",
            "PERMANENT_DIAGONAL_SEGRE_APOLAR_ALGEBRA",
            "BORDER_MULTIPLICATION_BASELINE",
            "ORDINARY_MULTIPLICATION_BASELINE",
            "EXACT_RATIONAL_AND_INTEGER_REPLAYED",
        ],
        "theorem": {
            "term_envelope": (
                "For T=product_i ell_i, A_T is isomorphic to "
                "C/Ann_C(lambda), where C is the subalgebra of "
                "B_n=k[z_i]/(z_i^2) generated by "
                "sum_i alpha(ell_i)z_i."
            ),
            "decomposition_subquotient": (
                "For f=sum_i T_i, A_f is an algebra quotient of a "
                "subalgebra of direct_product_i A_(T_i)."
            ),
            "tensor_inequality": (
                "For tensor rank R and border rank borderR, "
                "R(mu_(A_f))<=sum_i R(mu_(A_Ti)) and similarly for "
                "borderR; every term is bounded by the Boolean algebra."
            ),
            "permanent_algebra": (
                "A_(perm_n) is the diagonal Segre product B_n#B_n, "
                "with basis (R,C), |R|=|C|, and disjoint-union "
                "multiplication."
            ),
            "border_bound": (
                "ChowRank(perm_n)>=ceil(binom(2n,n)/2^n)."
            ),
            "ordinary_bound": (
                "Using Alder-Strassen and the W-state product-rank "
                "upper bound, ChowRank(perm_n)>=ceil((2*binom(2n,n)-1)"
                "/((n+2)*2^(n-1)))."
            ),
            "route_ceiling": (
                "Because A_(perm_n) is a subalgebra of B_n tensor B_n, "
                "the ordinary multiplication-tensor ratio is at most "
                "R(mu_Bn), and the border ratio is at most 2^n."
            ),
        },
        "finite_replay": {
            "factor_rows": factor_rows,
            "boolean_top_pairing_checks": pairing_checks,
            "permanent_rows": permanent_rows,
            "multiplication_table_checks": multiplication_checks,
            "associativity_checks": associativity_checks,
            "bound_arithmetic_checks": arithmetic_checks,
            "bound_rows_sha256": canonical_sha256(bound_rows),
        },
        "external_dependencies": {
            "alder_strassen": (
                "R(A)>=2*dim(A)-t(A) for finite-dimensional "
                "associative algebras."
            ),
            "W_product_upper": (
                "R(W_3 tensor ... tensor W_3)<=(n+2)*2^(n-1)."
            ),
        },
        "claim_boundary": (
            "This opens a legal nonlinear algebra-structure route and gives "
            "baseline ordinary and border lower bounds. Neither baseline "
            "improves the current repository bounds. The theorem does not "
            "determine the tensor or border rank of the permanent apolar "
            "multiplication tensor, prove smoothability or nonsmoothability "
            "of A_(perm_n), improve border Chow rank beyond existing scalar "
            "bounds, determine an exact Chow rank for n>=6, or prove Glynn "
            "optimality. The W-state ordinary bound is a cited external "
            "input; the 3^n fallback and border bound are self-contained."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_APOLAR_MULTIPLICATION_TENSOR_FRAMEWORK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
