#!/usr/bin/env python3
"""Exact replay for the N6-039 symmetric two-level orbit theorem.

The proof itself uses coefficient functionals and three small determinants.
The final five-variable Groebner basis is replayed only as an independent
exact check.  No floating point or finite-field arithmetic is used.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import sympy as sp


PARTITIONS = (
    (6,),
    (5, 1),
    (4, 2),
    (4, 1, 1),
    (3, 3),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
)
TARGET = sp.Matrix([0] * 10 + [1])


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def orbit_coefficient(k: int, parameter: sp.Expr, partition: tuple[int, ...]) -> sp.Expr:
    """Coefficient on a row-multiplicity class for the orbit O_k(parameter)."""

    multiplicities = partition + (0,) * (6 - len(partition))
    return sp.expand(
        sum(
            parameter ** sum(multiplicities[index] for index in subset)
            for subset in combinations(range(6), k)
        )
    )


def orbit_vector(k: int, parameter: sp.Expr) -> sp.Matrix:
    return sp.Matrix(
        [orbit_coefficient(k, parameter, partition) for partition in PARTITIONS]
    )


def infinity_orbit_vector(k: int) -> sp.Matrix:
    """The projective parameter t=infinity, i.e. the t^6 coefficient."""

    t = sp.symbols("t")
    return sp.Matrix(
        [
            sp.Poly(orbit_coefficient(k, t, partition), t).coeff_monomial(t**6)
            for partition in PARTITIONS
        ]
    )


def verify_missing_type_certificates() -> list[dict[str, object]]:
    """Verify functionals separating the target when one orbit type is absent."""

    certificates = (
        {
            "missing_k": 1,
            "allowed_k": (0, 2, 3),
            "weights": {
                (6,): -1,
                (5, 1): 5,
                (4, 1, 1): -10,
                (3, 1, 1, 1): 10,
                (2, 1, 1, 1, 1): -5,
                (1, 1, 1, 1, 1, 1): 1,
            },
        },
        {
            "missing_k": 2,
            "allowed_k": (0, 1, 3),
            "weights": {
                (3, 2, 1): -1,
                (3, 1, 1, 1): 1,
                (2, 2, 2): 1,
                (2, 1, 1, 1, 1): -2,
                (1, 1, 1, 1, 1, 1): 1,
            },
        },
        {
            "missing_k": 3,
            "allowed_k": (0, 1, 2),
            "weights": {
                (2, 2, 2): -1,
                (2, 2, 1, 1): 3,
                (2, 1, 1, 1, 1): -3,
                (1, 1, 1, 1, 1, 1): 1,
            },
        },
    )
    t = sp.symbols("t")
    output: list[dict[str, object]] = []
    for certificate in certificates:
        weights = certificate["weights"]
        functional = sp.Matrix([weights.get(partition, 0) for partition in PARTITIONS])
        target_value = (functional.T * TARGET)[0]
        require(target_value == 1, (certificate, target_value))
        annihilated: dict[str, str] = {}
        for k in certificate["allowed_k"]:
            value = sp.factor((functional.T * orbit_vector(k, t))[0])
            require(value == 0, (certificate, k, value))
            annihilated[str(k)] = str(value)
        output.append(
            {
                "missing_k": certificate["missing_k"],
                "allowed_k": list(certificate["allowed_k"]),
                "weights": {
                    str(partition): weight for partition, weight in weights.items()
                },
                "target_value": int(target_value),
                "annihilated_polynomials": annihilated,
            }
        )
    return output


def determinant_certificate(
    rows: tuple[tuple[int, ...], ...],
    first_parameter: sp.Expr,
    second_parameter: sp.Expr,
) -> sp.Expr:
    indices = [PARTITIONS.index(partition) for partition in rows]
    matrix = sp.Matrix(
        [
            [
                orbit_coefficient(1, first_parameter, PARTITIONS[index]),
                orbit_coefficient(2, second_parameter, PARTITIONS[index]),
                orbit_coefficient(3, -1, PARTITIONS[index]),
                TARGET[index],
            ]
            for index in indices
        ]
    )
    return sp.factor(matrix.det())


def verify_length_31_exclusion() -> dict[str, object]:
    """Exclude c1 O_1(a)+c2 O_2(b)+c3 O_3(-1)=perm_6 exactly."""

    a, b = sp.symbols("a b")
    rows0 = ((3, 3), (3, 2, 1), (2, 2, 1, 1), (1, 1, 1, 1, 1, 1))
    rows_a = ((4, 1, 1), (2, 2, 2), (2, 2, 1, 1), (1, 1, 1, 1, 1, 1))
    rows_b = ((5, 1), (3, 1, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1))

    determinant0 = determinant_certificate(rows0, a, b)
    determinant_a = determinant_certificate(rows_a, -1, b)
    determinant_b = determinant_certificate(rows_b, a, -1)
    expected0 = 4 * (a - 1) ** 2 * (a + 1) * (b - 1) ** 4 * (b + 1) ** 2
    expected_a = 128 * (b - 1) ** 2 * (b + 1) ** 3
    expected_b = 8 * (a - 1) ** 2 * (a + 1)
    require(sp.expand(determinant0 - expected0) == 0, determinant0)
    require(sp.expand(determinant_a - expected_a) == 0, determinant_a)
    require(sp.expand(determinant_b - expected_b) == 0, determinant_b)

    final_weights = {
        (6,): 1,
        (5, 1): 15,
        (3, 1, 1, 1): 15,
        (1, 1, 1, 1, 1, 1): 1,
    }
    functional = sp.Matrix(
        [final_weights.get(partition, 0) for partition in PARTITIONS]
    )
    final_values = {
        str(k): sp.factor((functional.T * orbit_vector(k, -1))[0])
        for k in (1, 2, 3)
    }
    require(all(value == 0 for value in final_values.values()), final_values)
    final_target_value = (functional.T * TARGET)[0]
    require(final_target_value == 1, final_target_value)

    return {
        "generic_minor_rows": [str(row) for row in rows0],
        "generic_minor_determinant": str(determinant0),
        "a_equals_minus_one_minor_rows": [str(row) for row in rows_a],
        "a_equals_minus_one_minor_determinant": str(determinant_a),
        "b_equals_minus_one_minor_rows": [str(row) for row in rows_b],
        "b_equals_minus_one_minor_determinant": str(determinant_b),
        "branch_conclusion_under_a_not_1_b_not_1": "a=b=-1",
        "final_functional_weights": {
            str(partition): weight for partition, weight in final_weights.items()
        },
        "final_orbit_values": {key: str(value) for key, value in final_values.items()},
        "final_target_value": int(final_target_value),
    }


def selected_determinant(columns: tuple[sp.Matrix, ...], rows: tuple[tuple[int, ...], ...]) -> sp.Expr:
    indices = [PARTITIONS.index(partition) for partition in rows]
    matrix = sp.Matrix([[column[index] for column in columns] for index in indices])
    return sp.factor(matrix.det())


def verify_projective_boundary() -> dict[str, object]:
    """Exclude a=infinity and b=infinity from the unique length-31 shape."""

    a, b = sp.symbols("a b")
    v3 = orbit_vector(3, -1)
    columns_a_infinity = (infinity_orbit_vector(1), orbit_vector(2, b), v3, TARGET)
    a_force_rows = ((6,), (4, 1, 1), (2, 2, 1, 1), (1, 1, 1, 1, 1, 1))
    a_contradiction_rows = ((6,), (4, 1, 1), (3, 1, 1, 1), (1, 1, 1, 1, 1, 1))
    a_force = selected_determinant(columns_a_infinity, a_force_rows)
    a_contradiction = selected_determinant(columns_a_infinity, a_contradiction_rows)
    require(sp.expand(a_force + 8 * (b - 1) ** 2 * (b + 1) ** 3) == 0, a_force)
    require(
        sp.expand(a_contradiction - 8 * (b**3 + 2) * (b**2 + 3 * b + 1)) == 0,
        a_contradiction,
    )
    require(a_contradiction.subs(b, -1) == -8, a_contradiction.subs(b, -1))

    columns_b_infinity = (orbit_vector(1, a), infinity_orbit_vector(2), v3, TARGET)
    b_force_rows = ((6,), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1))
    b_contradiction_rows = ((5, 1), (2, 2, 2), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1))
    b_force = selected_determinant(columns_b_infinity, b_force_rows)
    b_contradiction = selected_determinant(columns_b_infinity, b_contradiction_rows)
    require(sp.expand(b_force + 60 * (a + 1) ** 2) == 0, b_force)
    require(sp.expand(b_contradiction - 8 * (a**2 + 10 * a + 1)) == 0, b_contradiction)
    require(b_contradiction.subs(a, -1) == -64, b_contradiction.subs(a, -1))

    columns_both_infinity = (
        infinity_orbit_vector(1),
        infinity_orbit_vector(2),
        v3,
        TARGET,
    )
    both_infinity_rows = ((6,), (5, 1), (4, 2), (1, 1, 1, 1, 1, 1))
    both_infinity = selected_determinant(
        columns_both_infinity, both_infinity_rows
    )
    require(both_infinity == 24, both_infinity)

    return {
        "a_infinity_force_rows": [str(row) for row in a_force_rows],
        "a_infinity_force_determinant": str(a_force),
        "a_infinity_forces_under_b_not_1": "b=-1",
        "a_infinity_contradiction_rows": [str(row) for row in a_contradiction_rows],
        "a_infinity_contradiction_determinant": str(a_contradiction),
        "a_infinity_contradiction_value_at_b_minus_1": int(a_contradiction.subs(b, -1)),
        "b_infinity_force_rows": [str(row) for row in b_force_rows],
        "b_infinity_force_determinant": str(b_force),
        "b_infinity_forces": "a=-1",
        "b_infinity_contradiction_rows": [str(row) for row in b_contradiction_rows],
        "b_infinity_contradiction_determinant": str(b_contradiction),
        "b_infinity_contradiction_value_at_a_minus_1": int(b_contradiction.subs(a, -1)),
        "both_infinity_rows": [str(row) for row in both_infinity_rows],
        "both_infinity_determinant": int(both_infinity),
    }


def verify_groebner_replay() -> dict[str, object]:
    """Redundant exact QQ replay of the full length-31 coefficient system."""

    a, b, c1, c2, c3 = sp.symbols("a b c1 c2 c3")
    equations = [
        sp.expand(
            c1 * orbit_coefficient(1, a, partition)
            + c2 * orbit_coefficient(2, b, partition)
            + c3 * orbit_coefficient(3, -1, partition)
            - TARGET[index]
        )
        for index, partition in enumerate(PARTITIONS)
    ]
    basis = sp.groebner(
        equations,
        c1,
        c2,
        c3,
        a,
        b,
        order="grevlex",
        domain=sp.QQ,
    )
    basis_strings = [str(polynomial.as_expr()) for polynomial in basis.polys]
    require(basis_strings == ["1"], basis_strings)
    require(basis.domain == sp.QQ, basis.domain)
    return {
        "coefficient_field": str(basis.domain),
        "variables_in_order": ["c1", "c2", "c3", "a", "b"],
        "monomial_order": "grevlex",
        "partition_order": [str(partition) for partition in PARTITIONS],
        "input_equations": [str(equation) for equation in equations],
        "reduced_basis": basis_strings,
        "logical_role": "redundant exact replay; the determinant proof is primary",
    }


def verify_glynn_endpoint() -> dict[str, object]:
    reconstructed = (
        sp.Rational(1, 32) * orbit_vector(0, -1)
        - sp.Rational(1, 32) * orbit_vector(1, -1)
        + sp.Rational(1, 32) * orbit_vector(2, -1)
        - sp.Rational(1, 64) * orbit_vector(3, -1)
    )
    require(reconstructed == TARGET, list(reconstructed))
    return {
        "identity": "perm_6=(O_0(-1)-O_1(-1)+O_2(-1))/32-O_3(-1)/64",
        "distinct_chow_terms": 1 + 6 + 15 + 10,
        "orbit_costs": {"k0": 1, "k1": 6, "k2": 15, "k3_at_minus_one": 10},
        "coefficient_vector_verified": True,
    }


def build_payload() -> dict[str, object]:
    missing = verify_missing_type_certificates()
    exclusion = verify_length_31_exclusion()
    projective_boundary = verify_projective_boundary()
    groebner = verify_groebner_replay()
    glynn = verify_glynn_endpoint()
    return {
        "status": "N6_039_SYMMETRIC_TWO_LEVEL_ORBIT_RANK_32",
        "arithmetic": "exact integer and rational polynomial arithmetic over QQ",
        "partition_classes": [str(partition) for partition in PARTITIONS],
        "orbit_definition": (
            "O_k(t)=sum_{|S|=k} product_j(t sum_{i in S} x_ij + "
            "sum_{i not in S} x_ij), for k=0,1,2,3"
        ),
        "missing_type_certificates": missing,
        "reduced_orbit_costs": {
            "k0": 1,
            "k1_t_not_1": 6,
            "k2_t_not_1": 15,
            "k3_generic": 20,
            "k3_t_minus_1": 10,
            "k3_t_1": 1,
        },
        "unique_sub_32_shape": (
            "one k=1 orbit, one k=2 orbit, and the ten-term k=3,t=-1 "
            "orbit; total 31 and no k=0 orbit"
        ),
        "length_31_exclusion": exclusion,
        "projective_boundary_exclusion": projective_boundary,
        "redundant_groebner_replay": groebner,
        "glynn_endpoint": glynn,
        "restricted_family_minimum": 32,
        "claim_boundary": (
            "This theorem concerns S6-row-symmetrized two-level subset-orbit "
            "decompositions. It does not exclude arbitrary non-sign, arbitrary "
            "column-dependent, or unrestricted Chow decompositions and does not "
            "change 26 <= ChowRank(perm_6) <= 32."
        ),
    }


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
    print("N6_039_SYMMETRIC_TWO_LEVEL_ORBIT_RIGIDITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
