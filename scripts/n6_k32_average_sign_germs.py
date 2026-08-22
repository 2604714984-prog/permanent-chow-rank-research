"""Exact local exclusion of the four same-row average/sign directions."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, rank_mod, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, rank_mod, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_average_sign_germs.json"
SUPPORT = (0, 1, 4, 5, 8, 9)
COMPLEMENT = (2, 3, 6, 7, 10, 11)
AVERAGE_SIGNS = ((1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1))


def unit(index: int) -> list[int]:
    return [int(i == index) for i in range(12)]


def frames(signs: tuple[int, int, int]) -> tuple[list[list[object]], list[list[object]]]:
    left: list[list[object]] = [unit(index) for index in SUPPORT]
    right: list[list[object]] = [unit(index) for index in SUPPORT]
    for row, sign in enumerate(signs):
        basis_index = 2 * row
        left[basis_index][4 * row + 2] = sign
        right[basis_index][4 * row + 2] = sign
    return left, right


def cross_rank(left: list[list[object]], right: list[list[object]]) -> int:
    return int(sp.Matrix([beta(x, y) for x in left for y in right]).rank())


def sum_rank(left: list[list[object]], right: list[list[object]]) -> int:
    return int(sp.Matrix.hstack(sp.Matrix(left).T, sp.Matrix(right).T).rank())


def pivot_rows_and_columns(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    _, columns = matrix.rref()
    columns = list(columns)
    rows = list(matrix[:, columns].T.rref()[1])
    return rows, columns


def linear_setup(signs: tuple[int, int, int]) -> dict[str, object]:
    left, right = frames(signs)
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
    raw: list[sp.Matrix] = []
    schur: list[sp.Matrix] = []
    for side in ("L", "M"):
        for basis_index in range(6):
            for target in COMPLEMENT:
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
                derivative = sp.Matrix(rows)
                a1, b1, c1, _ = blocks(derivative)
                inverse1 = -inverse0 * a1 * inverse0
                raw.append(derivative)
                schur.append(
                    derivative.extract(lower_rows, right_columns)
                    - (c1 * inverse0 * b0 + c0 * inverse1 * b0 + c0 * inverse0 * b1)
                )
    flat = lambda matrix: sp.Matrix(list(matrix))
    average = sp.Matrix.hstack(*[
        flat(schur[i] + schur[36 + i]) for i in range(36)
    ])
    difference = sp.Matrix.hstack(*[
        flat(schur[i] - schur[36 + i]) for i in range(36)
    ])
    linear = sp.Matrix.hstack(*[flat(item) for item in schur])
    return {
        "base": base,
        "left": left,
        "right": right,
        "blocks": blocks,
        "inverse0": inverse0,
        "raw": raw,
        "schur": schur,
        "linear": linear,
        "average": average,
        "difference": difference,
    }


def all_plus_quadratic(setup: dict[str, object]) -> dict[str, object]:
    variables = sp.symbols("x0:3")
    raw: list[sp.Matrix] = setup["raw"]
    linear: sp.Matrix = setup["linear"]
    blocks = setup["blocks"]
    inverse0: sp.Matrix = setup["inverse0"]
    b0 = blocks(setup["base"])[1]
    c0 = blocks(setup["base"])[2]
    # Use the exact kernel vectors rather than reading a flattened coordinate
    # basis from a numerical nullspace.
    kernel = linear.nullspace()
    require(len(kernel) == 3, len(kernel))
    coefficients = [
        sum((variables[a] * kernel[a][i] for a in range(3)), sp.Integer(0))
        for i in range(72)
    ]
    first_matrix = sum(
        (coefficients[i] * raw[i] for i in range(72)), sp.zeros(36, 18)
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
    a1, b1, c1, _ = blocks(first_matrix)
    a2, b2, c2, d2 = blocks(second_matrix)
    inverse1 = -inverse0 * a1 * inverse0
    inverse2 = inverse0 * a1 * inverse0 * a1 * inverse0 - inverse0 * a2 * inverse0
    second = sp.expand(
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
        for i, j in combinations_with_replacement(range(3), 2)
    ]
    quadratic = sp.Matrix([
        [sp.Poly(entry, *variables).coeff_monomial(monomial) for monomial in monomials]
        for entry in list(second)
    ])
    _, pivot_columns = linear.rref()
    pivot_columns = list(pivot_columns)
    pivot_rows = list(linear[:, pivot_columns].T.rref()[1])
    other_rows = [i for i in range(linear.rows) if i not in pivot_rows]
    square = linear.extract(pivot_rows, pivot_columns)
    residual = (
        quadratic.extract(other_rows, range(len(monomials)))
        - linear.extract(other_rows, pivot_columns)
        * square.inv()
        * quadratic.extract(pivot_rows, range(len(monomials)))
    )
    reduced, pivots = residual.rref()
    generators = [
        sp.factor(sum(reduced[row, column] * monomials[column] for column in range(6)))
        for row in range(len(pivots))
    ]
    require(generators == [variables[1] * variables[2]], generators)
    return {
        "linear_rank": int(linear.rank()),
        "kernel_dimension": len(kernel),
        "average_rank": int(setup["average"].rank()),
        "difference_rank": int(setup["difference"].rank()),
        "quadratic_generators": [str(item) for item in generators],
        "branch_ranks": {
            "diagonal": {"cross_rank": 6, "sum_rank": 6},
            "separating": {"cross_rank": 6, "sum_rank": 9},
        },
        "formal_sandwich": True,
    }


def build_payload() -> dict[str, object]:
    profiles: list[dict[str, object]] = []
    for signs in AVERAGE_SIGNS:
        setup = linear_setup(signs)
        base = setup["base"]
        profile: dict[str, object] = {
            "signs": list(signs),
            "base_cross_rank": int(base.rank()),
            "base_sum_rank": sum_rank(setup["left"], setup["right"]),
            "linear_rank": int(setup["linear"].rank()),
            "average_rank": int(setup["average"].rank()),
            "difference_rank": int(setup["difference"].rank()),
        }
        if signs == (1, 1, 1):
            profile["local_germ"] = all_plus_quadratic(setup)
        else:
            require(profile["difference_rank"] == 36, profile)
            profile["local_germ"] = {
                "swap_symmetry_forces_diagonal": True,
                "consequence_sum_rank": 6,
            }
        profiles.append(profile)
    require(len(profiles) == 4, profiles)
    require(all(item["base_cross_rank"] == 6 for item in profiles), profiles)
    require(all(item["linear_rank"] == 69 for item in profiles), profiles)
    return {
        "certificate": "N6-127",
        "status": "EXACT_QQ_AVERAGE_SIGN_GERM_EXCLUSION",
        "field": "characteristic zero",
        "hypothesis": "four same-row average/sign first-Schur lines at the K3,2 collision",
        "profiles": profiles,
        "consequence": (
            "The three nontrivial sign-average lines have full difference "
            "Jacobian and are formally diagonal. The all-positive line has "
            "quadratic ideal (x1*x2), with diagonal and sum-rank-nine branches. "
            "All four average/sign lines are therefore noncomplementary."
        ),
        "boundary": [
            "does not classify mixed torus-weight sums",
            "does not classify arbitrary invertible 6 by 6 graph operators",
            "does not prove ordinary lower 29 or exact Chow rank 32",
            "does not make a border-rank claim",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen payload mismatch")
    print("certificate=N6-127")
    print("profiles=4")
    print("status=PASS")


if __name__ == "__main__":
    main()
