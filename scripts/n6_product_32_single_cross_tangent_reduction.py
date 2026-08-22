"""Exact local tangent-cone reduction at the K3,2 single-cross point."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, rank_mod, require
except ModuleNotFoundError:  # Direct ``python scripts/...py`` execution.
    from n6_product_32_rank_six_frame_barrier import beta, rank_mod, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_32_single_cross_tangent_reduction.json"
SUPPORT = (0, 1, 4, 5, 8, 9)
COMPLEMENT = (2, 3, 6, 7, 10, 11)


def unit(index: int) -> list[int]:
    return [int(i == index) for i in range(12)]


def base_pair() -> tuple[list[list[int]], list[list[int]]]:
    left = [unit(index) for index in SUPPORT]
    right = [unit(index) for index in SUPPORT]
    source = SUPPORT.index(0)
    left[source][6] = 1
    right[source][6] = -1
    return left, right


def pivot_rows_and_columns(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    _, columns = matrix.rref()
    columns = list(columns)
    rows = list(matrix[:, columns].T.rref()[1])
    return rows, columns


def build_local_system() -> dict[str, object]:
    left, right = base_pair()
    base = sp.Matrix([beta(x, y) for x in left for y in right])
    pivot_rows, pivot_columns = pivot_rows_and_columns(base)
    lower_rows = [i for i in range(36) if i not in pivot_rows]
    right_columns = [i for i in range(18) if i not in pivot_columns]

    def blocks(matrix: sp.Matrix) -> tuple[sp.Matrix, ...]:
        return (
            matrix.extract(pivot_rows, pivot_columns),
            matrix.extract(pivot_rows, right_columns),
            matrix.extract(lower_rows, pivot_columns),
            matrix.extract(lower_rows, right_columns),
        )

    a0, b0, c0, _ = blocks(base)
    inverse0 = a0.inv()
    labels: list[tuple[str, int, int]] = []
    derivatives: list[sp.Matrix] = []
    for side in ("L", "M"):
        for basis_index, source in enumerate(SUPPORT):
            for target in COMPLEMENT:
                labels.append((side, target, source))
                target_vector = unit(target)
                rows: list[list[int]] = []
                for i in range(6):
                    for j in range(6):
                        if side == "L" and i == basis_index:
                            rows.append(beta(target_vector, right[j]))
                        elif side == "M" and j == basis_index:
                            rows.append(beta(left[i], target_vector))
                        else:
                            rows.append([0] * 18)
                derivatives.append(sp.Matrix(rows))

    def first_schur(derivative: sp.Matrix) -> sp.Matrix:
        a1, b1, c1, d1 = blocks(derivative)
        inverse1 = -inverse0 * a1 * inverse0
        return d1 - (c1 * inverse0 * b0 + c0 * inverse1 * b0 + c0 * inverse0 * b1)

    linear = sp.Matrix.hstack(*[
        sp.Matrix(list(first_schur(derivative))) for derivative in derivatives
    ])
    linear_rank_mod = rank_mod([
        [int(entry) for entry in row] for row in linear.tolist()
    ])
    kernel = linear.nullspace()
    require(linear_rank_mod == 64, linear_rank_mod)
    require(len(kernel) == 8, len(kernel))

    variables = sp.symbols("x0:8")
    coefficients = [
        sum((variables[a] * kernel[a][i] for a in range(8)), sp.Integer(0))
        for i in range(72)
    ]
    first_matrix = sum(
        (coefficients[i] * derivatives[i] for i in range(72)), sp.zeros(36, 18)
    )
    second_matrix = sp.zeros(36, 18)
    for i in range(6):
        for j in range(6):
            delta_left = [0] * 12
            delta_right = [0] * 12
            for a, target in enumerate(COMPLEMENT):
                delta_left[target] = coefficients[i * 6 + a]
                delta_right[target] = coefficients[36 + j * 6 + a]
            second_matrix[i * 6 + j, :] = sp.Matrix(
                1, 18, beta(delta_left, delta_right)
            )

    a1, b1, c1, d1 = blocks(first_matrix)
    a2, b2, c2, d2 = blocks(second_matrix)
    inverse1 = -inverse0 * a1 * inverse0
    inverse2 = inverse0 * a1 * inverse0 * a1 * inverse0 - inverse0 * a2 * inverse0
    second_schur = sp.expand(
        d2
        - (
            c2 * inverse0 * b0
            + c1 * inverse1 * b0
            + c1 * inverse0 * b1
            + c0 * inverse2 * b0
            + c0 * inverse1 * b1
            + c0 * inverse0 * b2
        )
    )

    monomials = [
        variables[i] * variables[j]
        for i, j in combinations_with_replacement(range(8), 2)
    ]
    quadratic = sp.Matrix([
        [sp.Poly(entry, *variables).coeff_monomial(monomial) for monomial in monomials]
        for entry in list(second_schur)
    ])
    _, pivot_linear_columns = linear.rref()
    pivot_linear_columns = list(pivot_linear_columns)
    pivot_linear_rows = list(linear[:, pivot_linear_columns].T.rref()[1])
    other_rows = [i for i in range(linear.rows) if i not in pivot_linear_rows]
    square = linear.extract(pivot_linear_rows, pivot_linear_columns)
    residual = (
        quadratic.extract(other_rows, range(len(monomials)))
        - linear.extract(other_rows, pivot_linear_columns)
        * square.inv()
        * quadratic.extract(pivot_linear_rows, range(len(monomials)))
    )
    reduced, pivots = residual.rref()
    generators = [
        sp.factor(sum(reduced[row, column] * monomials[column] for column in range(36)))
        for row in range(len(pivots))
    ]
    expected_generators = [
        variables[1] * variables[2],
        variables[1] * variables[4],
        variables[1] * variables[5],
        variables[2] * variables[5],
        variables[4] * variables[5],
        variables[4] * variables[6],
        variables[4] * variables[7],
    ]
    require(generators == expected_generators, generators)

    edges = {(1, 2), (1, 4), (1, 5), (2, 5), (4, 5), (4, 6), (4, 7)}
    facets: list[tuple[int, ...]] = []
    for mask in range(1 << 8):
        subset = tuple(i for i in range(8) if mask & (1 << i))
        if any(i in subset and j in subset for i, j in edges):
            continue
        if any(set(subset) < set(facet) for facet in facets):
            continue
        facets = [facet for facet in facets if not set(facet) < set(subset)]
        facets.append(subset)
    facets.sort()
    expected_facets = [
        (0, 1, 3, 6, 7),
        (0, 2, 3, 4),
        (0, 2, 3, 6, 7),
        (0, 3, 5, 6, 7),
    ]
    require(facets == expected_facets, facets)

    kernel_supports = [
        [
            {"side": labels[i][0], "target": labels[i][1], "source": labels[i][2], "coefficient": int(entry)}
            for i, entry in enumerate(vector)
            if entry
        ]
        for vector in kernel
    ]
    facet_target_sets = []
    for facet in facets:
        targets = {6}
        for index in facet:
            targets.update(item["target"] for item in kernel_supports[index])
        facet_target_sets.append(sorted(targets))
    require(all(len(targets) <= 2 for targets in facet_target_sets), facet_target_sets)

    return {
        "base": {
            "cross_rank_over_QQ": int(base.rank()),
            "sum_rank_over_QQ": int(sp.Matrix.hstack(*map(sp.Matrix, left + right)).rank()),
        },
        "linear_system_shape": list(linear.shape),
        "modular_linear_rank_lower_bound": linear_rank_mod,
        "explicit_QQ_kernel_dimension": len(kernel),
        "exact_QQ_linear_rank": 64,
        "tangent_variable_labels": kernel_supports,
        "quadratic_monomial_count": len(monomials),
        "quadratic_cokernel_rank_over_QQ": len(pivots),
        "quadratic_initial_generators": [str(item) for item in generators],
        "squarefree_initial_ideal": True,
        "maximal_facets": [list(facet) for facet in facets],
        "facet_extra_coordinate_sets": facet_target_sets,
        "every_facet_moves_inside_a_common_eight_space": True,
    }


def build_payload() -> dict[str, object]:
    return {
        "certificate": "N6-116",
        "status": "EXACT_SINGLE_CROSS_LINEAR_AND_QUADRATIC_TANGENT_CONE_REDUCTION",
        "field": "characteristic zero",
        "local_system": build_local_system(),
        "claim": (
            "the reduced quadratic tangent-cone support at the K32 single-cross "
            "rank-six point has four coordinate facets, and every facet changes "
            "the pair inside a common eight-dimensional coordinate ambient"
        ),
        "boundary": {
            "not_proved": [
                "the completed local germ is contained in the union of the four eight-space incidences",
                "the three nonlinearly obstructed facets have no higher-order separating branches",
                "all rank-three K23/K32 components are exhausted",
                "the kappa2=0 six-color endpoint or ordinary lower 29",
            ]
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            "frozen JSON differs from exact replay",
        )
    print("certificate=N6-116")
    print("linear_rank=64")
    print("quadratic_rank=7")
    print("facet_count=4")
    print("status=PASS")


if __name__ == "__main__":
    main()
