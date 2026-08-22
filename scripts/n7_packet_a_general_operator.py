#!/usr/bin/env python3
"""Bounded exact Packet-A factor-plane and 2/5/6 operator controls.

The executable scope is two rank-seven terms in a seven-dimensional ambient
space.  Coefficient matrices and kernel-image defects are computed exactly
over QQ.  The complementary 2/5 relation pairing is computed separately over
one displayed finite field.  This is an interface certificate, not a search
through the 49-term equality locus.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import sympy as sp
from flint import nmod_mat


N = 7
PRIME = 65521
DEGREES = (2, 5, 6)


def exponent_basis(variable_count: int, degree: int) -> tuple[tuple[int, ...], ...]:
    if variable_count < 1 or degree < 0:
        raise ValueError("variable_count must be positive and degree nonnegative")
    if variable_count == 1:
        return ((degree,),)
    rows = []
    for first in range(degree + 1):
        for tail in exponent_basis(variable_count - 1, degree - first):
            rows.append((first, *tail))
    return tuple(rows)


def factor_subsets(degree: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.combinations(range(N), degree))


def validate_factors(factors: tuple[tuple[int, ...], ...]) -> int:
    if len(factors) != N or len({len(row) for row in factors}) != 1:
        raise ValueError("a Packet-A term needs seven equally sized factors")
    ambient = len(factors[0])
    if ambient < 1 or any(not any(value != 0 for value in row) for row in factors):
        raise ValueError("factor rows must be nonzero")
    return ambient


def multiply_subset(
    factors: tuple[tuple[int, ...], ...], subset: tuple[int, ...]
) -> dict[tuple[int, ...], int]:
    ambient = validate_factors(factors)
    polynomial = {(0,) * ambient: 1}
    for factor_index in subset:
        updated: dict[tuple[int, ...], int] = {}
        for exponent, coefficient in polynomial.items():
            for variable, value in enumerate(factors[factor_index]):
                if value == 0:
                    continue
                target = list(exponent)
                target[variable] += 1
                key = tuple(target)
                updated[key] = updated.get(key, 0) + coefficient * value
        polynomial = updated
    return polynomial


def term_catalectic(
    factors: tuple[tuple[int, ...], ...], degree: int
) -> sp.Matrix:
    """Columns are labelled products of the selected factors over ZZ."""

    ambient = validate_factors(factors)
    basis = exponent_basis(ambient, degree)
    columns = []
    for subset in factor_subsets(degree):
        polynomial = multiply_subset(factors, subset)
        columns.append(sp.Matrix([polynomial.get(alpha, 0) for alpha in basis]))
    return sp.Matrix.hstack(*columns)


def aggregate_catalectic(
    terms: tuple[tuple[tuple[int, ...], ...], ...], degree: int
) -> sp.Matrix:
    if not terms:
        raise ValueError("at least one term is required")
    ambient_dimensions = {validate_factors(term) for term in terms}
    if len(ambient_dimensions) != 1:
        raise ValueError("all terms must use one ambient coordinate space")
    return sp.Matrix.hstack(*(term_catalectic(term, degree) for term in terms))


def kernel_dimension(matrix: sp.Matrix) -> int:
    return matrix.cols - matrix.rank()


def qq_kernel_basis(matrix: sp.Matrix) -> sp.Matrix:
    """Return a column basis of the right kernel over QQ."""

    columns = matrix.nullspace()
    basis = sp.Matrix.hstack(*columns) if columns else sp.zeros(matrix.cols, 0)
    if matrix * basis != sp.zeros(matrix.rows, basis.cols):
        raise AssertionError("invalid QQ kernel basis")
    return basis


def complement_transport(term_count: int) -> sp.Matrix:
    """Map degree-five labels to complementary degree-two label order."""

    subsets2 = factor_subsets(2)
    subsets5 = factor_subsets(5)
    index5 = {subset: index for index, subset in enumerate(subsets5)}
    block = len(subsets2)
    transport = sp.zeros(term_count * block, term_count * block)
    full = set(range(N))
    for term in range(term_count):
        for index2, subset2 in enumerate(subsets2):
            complement = tuple(sorted(full.difference(subset2)))
            transport[term * block + index2, term * block + index5[complement]] = 1
    return transport


def coefficient_transport(coefficients: tuple[int, ...], inverse: bool) -> sp.Matrix:
    if not coefficients or any(value == 0 for value in coefficients):
        raise ValueError("external term coefficients must be nonzero")
    diagonal = []
    for coefficient in coefficients:
        value = sp.Rational(1, coefficient) if inverse else sp.Integer(coefficient)
        diagonal.extend([value] * math.comb(N, 2))
    return sp.diag(*diagonal)


def kernel_image_defect_qq(output_map: sp.Matrix, input_map: sp.Matrix) -> dict[str, int | bool]:
    if output_map.cols != input_map.rows:
        raise ValueError("the maps do not share a middle space")
    rank_b = output_map.rank()
    rank_c = input_map.rank()
    rank_bc = (output_map * input_map).rank()
    kernel_b = output_map.cols - rank_b
    intersection = rank_c - rank_bc
    defect = kernel_b - intersection
    if defect < 0:
        raise AssertionError("invalid kernel-image dimensions")
    return {
        "middle_dimension": output_map.cols,
        "rank_b": rank_b,
        "rank_c": rank_c,
        "rank_bc": rank_bc,
        "kernel_b_dimension": kernel_b,
        "kernel_b_intersection_image_c_dimension": intersection,
        "coupling_defect": defect,
        "condition_holds": defect == 0,
    }


def integer_matrix_mod(matrix: sp.Matrix, prime: int) -> list[list[int]]:
    rows = []
    for row in matrix.tolist():
        converted = []
        for value in row:
            rational = sp.Rational(value)
            denominator = int(rational.q) % prime
            if denominator == 0:
                raise ValueError("a rational denominator vanishes modulo the prime")
            converted.append(
                int(rational.p) * pow(denominator, prime - 2, prime) % prime
            )
        rows.append(converted)
    return rows


def modular_nullspace(matrix: sp.Matrix, prime: int) -> sp.Matrix:
    array = integer_matrix_mod(matrix, prime)
    basis, nullity = nmod_mat(array, prime).nullspace()
    if nullity == 0:
        return sp.zeros(matrix.cols, 0)
    return sp.Matrix([row[:nullity] for row in basis.tolist()])


def modular_rank(matrix: sp.Matrix, prime: int) -> int:
    if matrix.rows == 0 or matrix.cols == 0:
        return 0
    return nmod_mat(integer_matrix_mod(matrix, prime), prime).rank()


def relation_pairing_finite_field(
    aggregate2: sp.Matrix,
    aggregate5: sp.Matrix,
    coefficients: tuple[int, ...],
    prime: int = PRIME,
) -> dict[str, int | str]:
    if aggregate2.cols != aggregate5.cols:
        raise ValueError("degree-two and degree-five labelled spaces must align")
    term_count = len(coefficients)
    expected = term_count * math.comb(N, 2)
    if aggregate2.cols != expected:
        raise ValueError("coefficient count does not match the labelled spaces")
    k2 = modular_nullspace(aggregate2, prime)
    k5 = modular_nullspace(aggregate5, prime)
    inverse = coefficient_transport(coefficients, inverse=True)
    complement = complement_transport(term_count)
    pairing = k2.T * inverse * complement * k5
    wrong_pairing = k2.T * coefficient_transport(coefficients, inverse=False) * complement * k5
    return {
        "field": f"F_{prime}",
        "degree_2_kernel_dimension": k2.cols,
        "degree_5_kernel_dimension": k5.cols,
        "inverse_coefficient_pairing_rank": modular_rank(pairing, prime),
        "wrong_coefficient_pairing_rank": modular_rank(wrong_pairing, prime),
        "pairing_formula": "K2^T diag(c)^(-1) P_(2<-5) K5",
    }


def target_quotient_operator_qq(
    aggregate6: sp.Matrix, targets: sp.Matrix
) -> tuple[dict[str, int | bool | list[int]], sp.Matrix, sp.Matrix]:
    if aggregate6.rows != targets.rows:
        raise ValueError("targets and aggregate degree-six columns need one ambient basis")
    annihilator_columns = aggregate6.T.nullspace()
    annihilator = (
        sp.Matrix.hstack(*annihilator_columns).T
        if annihilator_columns
        else sp.zeros(0, aggregate6.rows)
    )
    residual = annihilator * targets
    base_rank = aggregate6.rank()
    target_rank = targets.rank()
    joint_rank = aggregate6.row_join(targets).rank()
    quotient_rank = residual.rank()
    if quotient_rank != joint_rank - base_rank:
        raise AssertionError("annihilator and augmented quotient ranks disagree")
    return (
        {
            "field": "QQ",
            "aggregate_rank": base_rank,
            "aggregate_kernel_dimension": aggregate6.cols - base_rank,
            "target_rank": target_rank,
            "joint_rank": joint_rank,
            "target_quotient_rank": quotient_rank,
            "target_contained": quotient_rank == 0,
            "quotient_operator_shape": [annihilator.rows, annihilator.cols],
            "residual_shape": [residual.rows, residual.cols],
        },
        annihilator,
        residual,
    )


def coordinate_factors() -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(i == j) for j in range(N)) for i in range(N))


def sheared_factors() -> tuple[tuple[int, ...], ...]:
    matrix = sp.eye(N)
    for index in range(N - 1):
        matrix[index, index + 1] = index + 1
    return tuple(tuple(int(value) for value in matrix.row(index)) for index in range(N))


def scaled_coordinate_factors(
    scales: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    if len(scales) != N or any(scale == 0 for scale in scales):
        raise ValueError("seven nonzero factor scales are required")
    factors = coordinate_factors()
    return tuple(
        tuple(scales[index] * value for value in factors[index])
        for index in range(N)
    )


def pure_power_target(variable: int, degree: int) -> sp.Matrix:
    basis = exponent_basis(N, degree)
    exponent = tuple(degree if index == variable else 0 for index in range(N))
    return sp.Matrix([int(alpha == exponent) for alpha in basis])


def preflight() -> dict[str, object]:
    monomial_rows = {degree: math.comb(N + degree - 1, degree) for degree in DEGREES}
    two_term_shapes = {
        str(degree): [monomial_rows[degree], 2 * math.comb(N, degree)]
        for degree in DEGREES
    }
    full_49_shapes = {
        str(degree): [monomial_rows[degree], 49 * math.comb(N, degree)]
        for degree in DEGREES
    }
    largest_entries = max(rows * columns for rows, columns in two_term_shapes.values())
    return {
        "executed_term_count": 2,
        "executed_matrix_shapes": two_term_shapes,
        "largest_executed_dense_entry_count": largest_entries,
        "conservative_executed_peak_memory_mib": 64,
        "deferred_49_term_matrix_shapes": full_49_shapes,
        "full_49_term_materialization_performed": False,
    }


def build_payload() -> dict[str, object]:
    resource = preflight()
    general = sheared_factors()
    general_rows = []
    for degree in DEGREES:
        matrix = term_catalectic(general, degree)
        expected = math.comb(N, degree)
        if matrix.rank() != expected:
            raise AssertionError((degree, matrix.rank(), expected))
        general_rows.append(
            {
                "degree": degree,
                "shape": list(matrix.shape),
                "QQ_exact_rank": matrix.rank(),
                "labelled_column_count": expected,
            }
        )

    terms = (coordinate_factors(), coordinate_factors())
    coefficients = (2, 3)
    aggregate = {degree: aggregate_catalectic(terms, degree) for degree in DEGREES}
    kernels = {degree: qq_kernel_basis(aggregate[degree]) for degree in DEGREES}
    exact_profiles = {
        str(degree): {
            "shape": list(aggregate[degree].shape),
            "QQ_exact_rank": aggregate[degree].rank(),
            "QQ_exact_kernel_dimension": kernel_dimension(aggregate[degree]),
            "QQ_exact_kernel_basis_shape": list(kernels[degree].shape),
        }
        for degree in DEGREES
    }
    complement = complement_transport(len(terms))
    transported_input = (
        coefficient_transport(coefficients, inverse=False)
        * complement
        * aggregate[5].T
    )
    incidence = kernel_image_defect_qq(aggregate[2], transported_input)
    pairing = relation_pairing_finite_field(
        aggregate[2], aggregate[5], coefficients, PRIME
    )

    direction_terms = (
        coordinate_factors(),
        scaled_coordinate_factors((2, 1, 1, 1, 1, 1, 1)),
    )
    direction_coefficients = (2, -1)
    direction2 = aggregate_catalectic(direction_terms, 2)
    direction5 = aggregate_catalectic(direction_terms, 5)
    direction_input = (
        coefficient_transport(direction_coefficients, inverse=False)
        * complement_transport(2)
        * direction5.T
    )
    direction_incidence = kernel_image_defect_qq(direction2, direction_input)
    direction_pairing = relation_pairing_finite_field(
        direction2, direction5, direction_coefficients, PRIME
    )
    if not direction_incidence["condition_holds"]:
        raise AssertionError(direction_incidence)
    if (
        direction_pairing["inverse_coefficient_pairing_rank"] != 0
        or direction_pairing["wrong_coefficient_pairing_rank"] != 21
    ):
        raise AssertionError(direction_pairing)

    included = aggregate[6][:, 0]
    outside = pure_power_target(0, 6)
    targets = sp.Matrix.hstack(included, outside)
    quotient, quotient_operator, residual = target_quotient_operator_qq(
        aggregate[6], targets
    )
    if quotient_operator * aggregate[6] != sp.zeros(quotient_operator.rows, aggregate[6].cols):
        raise AssertionError("target quotient operator does not annihilate A6")
    if quotient["target_quotient_rank"] != 1 or residual.rank() != 1:
        raise AssertionError((quotient, residual.rank()))
    if incidence["condition_holds"]:
        raise AssertionError("the duplicate-term incidence control must fail")

    return {
        "schema_version": 1,
        "status": "PACKET_A_GENERAL_OPERATOR_A01_A02_FOUNDATION",
        "resource_preflight": resource,
        "general_factor_plane_control": {
            "ambient_dimension": N,
            "factor_count": N,
            "factor_matrix_QQ_rank": sp.Matrix(general).rank(),
            "degree_maps": general_rows,
        },
        "inverse_coefficient_direction_control": {
            "description": "the second coordinate term has its first factor scaled by 2; external coefficients are 2 and -1",
            "external_coefficients": list(direction_coefficients),
            "factor_scale_product_of_second_term": 2,
            "QQ_exact_kernel_image_defect": direction_incidence,
            "finite_field_relation_pairing": direction_pairing,
            "conclusion": "inverse coefficient transport gives equality while direct coefficient transport fails",
        },
        "two_term_exact_control": {
            "description": "two identical coordinate factor planes with external coefficients 2 and 3",
            "external_coefficients": list(coefficients),
            "degree_profiles": exact_profiles,
            "inverse_coefficient_transport": {
                "input_map_formula": "diag(c) P_(2<-5) A5^T",
                "restricted_pairing_formula": "K2^T diag(c)^(-1) P_(2<-5) K5",
                "complement_transport_shape": list(complement.shape),
            },
            "QQ_exact_kernel_image_defect": incidence,
            "finite_field_relation_pairing": pairing,
            "QQ_exact_degree_6_target_quotient": quotient,
            "target_control": {
                "column_0": "one included labelled degree-six product",
                "column_1": "the outside pure power x_0^6",
            },
        },
        "rank_fields": {
            "factor_plane_catalectics_kernels_incidence_and_target_quotient": "QQ exact",
            "complementary_relation_pairing": f"F_{PRIME}",
        },
        "claim_boundary": [
            "This closes only the bounded A-01/A-02 operator foundation: general factor input, exact degree-2/5/6 maps, complementary label transport, a QQ kernel-image defect, and a QQ target quotient operator.",
            "The executed control has two terms in a seven-dimensional ambient space; it is not a 49-term Packet-A equality candidate.",
            "The target quotient interface is exact over QQ, but the displayed targets are an included-column/pure-power control, not the 49 permanent sixth derivatives.",
            "The complementary relation pairing is computed over F_65521 and is not promoted to a characteristic-zero zero-rank statement.",
            "A-03 through A-05, the full permanent equations, the 49-term equality incidence scheme, A-CLOSED, ordinary lower 50, and border rank remain unresolved.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("Packet A general operator JSON mismatch")
        print("PASS n7 Packet A general operator")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
