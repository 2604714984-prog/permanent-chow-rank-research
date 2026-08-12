#!/usr/bin/env python3
"""Exact G-046 barrier for the abstract colored-shadow route at b=50.

The construction is over QQ.  Integer Vandermonde matrices give the subset
kernel dimensions.  Full colored-shadow ranks are certified modulo a prime;
because the matrices are integral, modular rank is a lower bound for rational
rank, while containment in K_I gives the matching rational upper bound.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


COLORS = 6
COLOR_DIMENSION = 20
U_DIMENSION = 5
W_DIMENSION = 15
Z_DIMENSION = 70
PRIME = 1_000_003
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_colored_differential_barrier.json"


def modular_rank(matrix: list[list[int]], prime: int = PRIME) -> int:
    """Return the row rank over F_prime."""

    if not matrix:
        return 0
    work = [[entry % prime for entry in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % prime
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def modular_kernel_basis(
    matrix: list[list[int]], prime: int = PRIME
) -> list[list[int]]:
    """Return a reduced-echelon kernel basis over F_prime."""

    if not matrix:
        return []
    work = [[entry % prime for entry in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivot_columns: list[int] = []
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % prime
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        pivot_columns.append(column)
        rank += 1
        if rank == rows:
            break

    pivot_set = set(pivot_columns)
    basis: list[list[int]] = []
    for free_column in range(columns):
        if free_column in pivot_set:
            continue
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = (-work[row][free_column]) % prime
        basis.append(vector)
    return basis


def vandermonde() -> list[list[int]]:
    """The 70 by 120 integer Vandermonde matrix beta."""

    return [
        [pow(column + 1, row, PRIME) for column in range(COLORS * COLOR_DIMENSION)]
        for row in range(Z_DIMENSION)
    ]


def subset_certificate(
    colors: tuple[int, ...], matrix: list[list[int]]
) -> dict[str, object]:
    q = len(colors)
    global_columns = [
        color * COLOR_DIMENSION + local
        for color in colors
        for local in range(COLOR_DIMENSION)
    ]
    beta = [[row[column] for column in global_columns] for row in matrix]
    beta_modular_rank = modular_rank(beta)
    kernel = modular_kernel_basis(beta)

    shadow_rows: list[list[int]] = []
    for vector in kernel:
        for u_coordinate in range(U_DIMENSION):
            output = [0] * (q * W_DIMENSION)
            for subset_color, color in enumerate(colors):
                for w_coordinate in range(W_DIMENSION):
                    z_coordinate = u_coordinate * W_DIMENSION + w_coordinate
                    if z_coordinate >= Z_DIMENSION:
                        continue
                    output[subset_color * W_DIMENSION + w_coordinate] = sum(
                        vector[subset_color * COLOR_DIMENSION + local]
                        * matrix[z_coordinate][color * COLOR_DIMENSION + local]
                        for local in range(COLOR_DIMENSION)
                    ) % PRIME
            shadow_rows.append(output)

    shadow_modular_rank = modular_rank(shadow_rows)
    expected_beta_rank = min(Z_DIMENSION, q * COLOR_DIMENSION)
    expected_kernel_dimension = max(0, q * COLOR_DIMENSION - Z_DIMENSION)
    k_dimension = W_DIMENSION * (q - 1)
    if beta_modular_rank != expected_beta_rank:
        raise AssertionError((colors, beta_modular_rank, expected_beta_rank))
    if len(kernel) != expected_kernel_dimension:
        raise AssertionError((colors, len(kernel), expected_kernel_dimension))
    if shadow_modular_rank > k_dimension:
        raise AssertionError((colors, shadow_modular_rank, k_dimension))

    return {
        "colors": list(colors),
        "color_count": q,
        "beta_rank_over_Q": expected_beta_rank,
        "S_I_dimension_over_Q": expected_kernel_dimension,
        "K_I_dimension_over_Q": k_dimension,
        "colored_shadow_rank_mod_prime": shadow_modular_rank,
        "colored_shadow_rank_over_Q": shadow_modular_rank,
        "shadow_is_all_of_K_I": shadow_modular_rank == k_dimension,
    }


def audit() -> dict[str, object]:
    matrix = vandermonde()
    certificates = [
        subset_certificate(colors, matrix)
        for q in range(1, COLORS + 1)
        for colors in combinations(range(COLORS), q)
    ]
    grouped: dict[str, dict[str, object]] = {}
    endpoint_caps = {1: 0, 2: 2, 3: 10, 4: 20, 5: 40, 6: 50}
    for q in range(1, COLORS + 1):
        rows = [row for row in certificates if row["color_count"] == q]
        s_dimensions = sorted({int(row["S_I_dimension_over_Q"]) for row in rows})
        shadow_ranks = sorted(
            {int(row["colored_shadow_rank_over_Q"]) for row in rows}
        )
        if len(s_dimensions) != 1 or len(shadow_ranks) != 1:
            raise AssertionError((q, s_dimensions, shadow_ranks))
        if s_dimensions[0] > endpoint_caps[q]:
            raise AssertionError((q, s_dimensions[0], endpoint_caps[q]))
        grouped[str(q)] = {
            "number_of_subsets": len(rows),
            "S_I_dimension_over_Q": s_dimensions[0],
            "b50_product_shadow_cap": endpoint_caps[q],
            "colored_shadow_rank_over_Q": shadow_ranks[0],
            "K_I_dimension_over_Q": W_DIMENSION * (q - 1),
            "every_subset_shadow_equals_K_I": all(
                bool(row["shadow_is_all_of_K_I"]) for row in rows
            ),
        }

    expected = {
        "1": (0, 0),
        "2": (0, 0),
        "3": (0, 0),
        "4": (10, 45),
        "5": (30, 60),
        "6": (50, 75),
    }
    actual = {
        q: (
            row["S_I_dimension_over_Q"],
            row["colored_shadow_rank_over_Q"],
        )
        for q, row in grouped.items()
    }
    if actual != expected:
        raise AssertionError(actual)

    return {
        "status": "EXACT_ABSTRACT_COLORED_DIFFERENTIAL_BARRIER_G046",
        "base_field": "Q",
        "construction": {
            "colors": COLORS,
            "color_dimension": COLOR_DIMENSION,
            "U_dimension": U_DIMENSION,
            "W_dimension": W_DIMENSION,
            "Z_dimension": Z_DIMENSION,
            "beta_columns": "v_t=(1,t,...,t^69), t=1,...,120, grouped into six consecutive colors",
            "Z_embedding": "the first 70 coordinate axes of U tensor W in five row-major blocks of length 15",
            "S_I": "kernel of the sum of beta_i over colors in I",
            "K_I": "kernel of the sum map from the I-indexed copies of W to W",
            "colored_differentials": "the five U-coordinate contractions of beta_i, taken colorwise",
        },
        "exact_rank_certificate": {
            "prime": PRIME,
            "prime_exceeds_all_vandermonde_nodes": True,
            "rational_beta_rank_reason": "every required square Vandermonde minor on distinct integer nodes is nonzero over Q",
            "rational_shadow_rank_reason": "the displayed Vandermonde pivot minor is nonzero modulo the prime, so the reduced-echelon kernel basis lifts over Z localized at that prime; the computed colored-shadow matrix is its reduction, hence rational rank is at least modular rank, while containment in K_I gives the matching upper bound",
        },
        "all_63_nonempty_color_subsets_checked": True,
        "by_color_count": grouped,
        "strict_conclusion": "The common K_I incidence, all b=50 subset dimension caps, and even surjective colored shadows for every four-, five-, and six-color subset are jointly consistent over Q. Those data alone cannot exclude the b=50 endpoint.",
        "claim_boundary": "This is an abstract colored linear-differential model, not a family of sextic Chow terms, not a permanent derivative configuration, and not a b=50 or 27-term decomposition. It omits the squarefree cubic coproduct, factor-frame integrability, and common-section cocycle constraints of actual Chow terms. It proves only that a route using the recorded common kernels, subset caps, and colored-shadow ranks cannot close the endpoint without such additional structure.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = audit()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
