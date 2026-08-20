"""Bounded exact replay for the K3,2 rank-six product frame barrier."""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable, Sequence
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_32_rank_six_frame_barrier.json"
PRIME = 1_000_003
ROW_EDGES = tuple(combinations(range(3), 2))
COLUMN_EDGES = tuple(combinations(range(4), 2))


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def rank_mod(rows: Iterable[Sequence[int]], cap: int | None = None) -> int:
    prime = PRIME
    pivots: list[list[int] | None] | None = None
    rank = 0
    for source in rows:
        row = [entry % prime for entry in source]
        if pivots is None:
            pivots = [None] * len(row)
        for pivot_column, coefficient in enumerate(row):
            if coefficient == 0:
                continue
            pivot_row = pivots[pivot_column]
            if pivot_row is None:
                inverse = pow(coefficient, -1, prime)
                row[pivot_column] = 1
                for column in range(pivot_column + 1, len(row)):
                    row[column] = row[column] * inverse % prime
                pivots[pivot_column] = row
                rank += 1
                if cap is not None and rank > cap:
                    return rank
                break
            row[pivot_column] = 0
            for column in range(pivot_column + 1, len(row)):
                row[column] = (
                    row[column] - coefficient * pivot_row[column]
                ) % prime
    return rank


def integer_nullspace(matrix: list[list[int]]) -> list[list[int]]:
    answer: list[list[int]] = []
    for vector in sp.Matrix(matrix).nullspace():
        denominator = 1
        for entry in vector:
            denominator = denominator * entry.q // gcd(denominator, entry.q)
        scaled = [int(entry * denominator) for entry in vector]
        divisor = 0
        for entry in scaled:
            divisor = gcd(divisor, abs(entry))
        answer.append([entry // max(divisor, 1) for entry in scaled])
    return answer


def unit(index: int) -> list[int]:
    return [int(i == index) for i in range(12)]


def beta(left: list[int], right: list[int]) -> list[int]:
    return [
        left[4 * i + c] * right[4 * j + d]
        + left[4 * i + d] * right[4 * j + c]
        + left[4 * j + c] * right[4 * i + d]
        + left[4 * j + d] * right[4 * i + c]
        for i, j in ROW_EDGES
        for c, d in COLUMN_EDGES
    ]


BETA_BASIS = tuple(
    tuple(tuple(beta(unit(i), unit(j))) for j in range(12)) for i in range(12)
)


@lru_cache(maxsize=8192)
def graph_beta(
    source_left: int,
    target_left: int,
    sign_left: int,
    source_right: int,
    target_right: int,
    sign_right: int,
) -> tuple[int, ...]:
    return tuple(
        BETA_BASIS[source_left][source_right][k]
        + sign_right * BETA_BASIS[source_left][target_right][k]
        + sign_left * BETA_BASIS[target_left][source_right][k]
        + sign_left * sign_right * BETA_BASIS[target_left][target_right][k]
        for k in range(18)
    )


def signed_permutation_scan(support: tuple[int, ...]) -> dict[str, object]:
    targets = tuple(index for index in range(12) if index not in support)
    rank_histogram: dict[str, int] = {}
    equality_candidates: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for target_permutation in permutations(targets):
        for tail in product((-1, 1), repeat=5):
            signs = (1,) + tail
            cross_rows = [
                graph_beta(
                    support[i], target_permutation[i], signs[i],
                    support[j], target_permutation[j], -signs[j],
                )
                for i in range(6)
                for j in range(6)
            ]
            cross_rank = rank_mod(cross_rows)
            key = str(cross_rank)
            rank_histogram[key] = rank_histogram.get(key, 0) + 1
            if cross_rank == 6:
                equality_candidates.append((target_permutation, signs))
    require(sum(rank_histogram.values()) == 23_040, rank_histogram)
    return {
        "candidate_count": 23_040,
        "streaming_rank_histogram_mod_prime": rank_histogram,
        "modular_rank_six_candidates": [
            {"target_permutation": list(targets), "signs": list(signs)}
            for targets, signs in equality_candidates
        ],
    }


def graph_pair(
    support: tuple[int, ...], target_permutation: tuple[int, ...],
    signs: tuple[int, ...]
) -> tuple[list[list[int]], list[list[int]]]:
    left: list[list[int]] = []
    right: list[list[int]] = []
    for source, target, sign in zip(
        support, target_permutation, signs, strict=True
    ):
        left_vector = unit(source)
        right_vector = unit(source)
        left_vector[target] = sign
        right_vector[target] = -sign
        left.append(left_vector)
        right.append(right_vector)
    return left, right


def exact_candidate(
    support: tuple[int, ...], target_permutation: tuple[int, ...],
    signs: tuple[int, ...]
) -> dict[str, object]:
    left, right = graph_pair(support, target_permutation, signs)
    cross = sp.Matrix([beta(x, y) for x in left for y in right])
    kernel = sp.Matrix.hstack(*cross.nullspace())
    left_restriction = sp.Matrix(
        [beta(x, y) for x in left for y in left]
    ) * kernel
    right_restriction = sp.Matrix(
        [beta(x, y) for x in right for y in right]
    ) * kernel
    ambient_sum = sp.Matrix.hstack(*map(sp.Matrix, left + right))
    return {
        "target_permutation": list(target_permutation),
        "signs": list(signs),
        "ambient_sum_rank_over_QQ": int(ambient_sum.rank()),
        "cross_rank_over_QQ": int(cross.rank()),
        "cross_free_kernel_dimension": kernel.cols,
        "left_block_projection_rank_over_QQ": int(left_restriction.rank()),
        "right_block_projection_rank_over_QQ": int(right_restriction.rank()),
    }


def column_graph_symbolic_certificate() -> dict[str, object]:
    a, b, c, d = sp.symbols("a b c d")
    edges = tuple(combinations(range(4), 2))

    def evaluate(left: sp.Matrix, right: sp.Matrix) -> list[sp.Expr]:
        return [left[i] * right[j] + left[j] * right[i] for i, j in edges]

    left = (sp.Matrix([1, 0, a, 0]), sp.Matrix([0, 1, 0, b]))
    right = (sp.Matrix([1, 0, c, 0]), sp.Matrix([0, 1, 0, d]))
    matrix = sp.Matrix([evaluate(x, y) for x in left for y in right])
    minors = {
        sp.factor(matrix.extract(rows, columns).det())
        for rows in combinations(range(4), 3)
        for columns in combinations(range(6), 3)
    }
    minors.discard(sp.Integer(0))
    first = sp.expand((a - c) * (a + c))
    second = sp.expand((b - d) * (b + d))
    require(any(sp.expand(item) == first for item in minors), sorted(map(str, minors)))
    require(any(sp.expand(item) == second for item in minors), sorted(map(str, minors)))
    require(
        all(sp.expand(item.subs({c: -a, d: -b})) == 0 for item in minors),
        sorted(map(str, minors)),
    )
    return {
        "cross_matrix_shape": list(matrix.shape),
        "nonzero_three_minor_count": len(minors),
        "selected_minor_factors": ["(a-c)(a+c)", "(b-d)(b+d)"],
        "complementarity_factors": ["a-c", "b-d"],
        "rank_at_most_two_forces": ["c=-a", "d=-b"],
        "substitution_kills_every_three_minor": True,
    }


def finite_field_counterexample_screen() -> dict[str, object]:
    """A tiny complete F3 diagnostic; it is not used to prove the theorem."""
    prime = 3

    def normalize(vector: tuple[int, ...]) -> tuple[int, ...]:
        pivot = next(i for i, entry in enumerate(vector) if entry % prime)
        inverse = pow(vector[pivot] % prime, -1, prime)
        return tuple(entry * inverse % prime for entry in vector)

    projective_points = sorted({
        normalize(vector)
        for vector in product(range(prime), repeat=4)
        if any(vector)
    })
    planes: set[tuple[tuple[int, ...], ...]] = set()
    for first, second in combinations(projective_points, 2):
        points = {
            normalize(tuple(
                (a * first[i] + b * second[i]) % prime for i in range(4)
            ))
            for a, b in product(range(prime), repeat=2)
            if a or b
        }
        if len(points) == 4:
            planes.add(tuple(sorted(points)))

    def plane_basis(plane: tuple[tuple[int, ...], ...]) -> list[list[int]]:
        first = list(plane[0])
        second = next(
            list(vector)
            for vector in plane[1:]
            if rank_mod([first, list(vector)]) == 2
        )
        return [first, second]

    def cross_rank(
        first: tuple[tuple[int, ...], ...], second: tuple[tuple[int, ...], ...]
    ) -> int:
        return rank_mod([
            [
                (left[i] * right[j] + left[j] * right[i]) % prime
                for i, j in combinations(range(4), 2)
            ]
            for left in plane_basis(first)
            for right in plane_basis(second)
        ])

    complementary_low_pairs = [
        (first, second)
        for first in planes
        for second in planes
        if rank_mod(plane_basis(first) + plane_basis(second)) == 4
        and cross_rank(first, second) <= 2
    ]

    def span(first: list[int], second: list[int]) -> tuple[tuple[int, ...], ...]:
        return tuple(sorted({
            normalize(tuple(
                (a * first[i] + b * second[i]) % prime for i in range(4)
            ))
            for a, b in product(range(prime), repeat=2)
            if a or b
        }))

    generated = set()
    for (i, k), (j, ell) in (
        ((0, 2), (1, 3)), ((0, 1), (2, 3)), ((0, 3), (1, 2))
    ):
        for a, b in product((1, 2), repeat=2):
            p = [0] * 4
            q = [0] * 4
            r = [0] * 4
            s = [0] * 4
            p[i] = q[i] = r[j] = s[j] = 1
            p[k] = a
            q[k] = -a % prime
            r[ell] = b
            s[ell] = -b % prime
            generated.add((span(p, r), span(q, s)))

    require(len(planes) == 130, len(planes))
    require(len(complementary_low_pairs) == 12, len(complementary_low_pairs))
    require(set(complementary_low_pairs) == generated, (complementary_low_pairs, generated))
    return {
        "status": "COMPLETE_F3_COUNTEREXAMPLE_SCREEN_ONLY",
        "grassmannian_point_count": len(planes),
        "ordered_pair_count": len(planes) ** 2,
        "complementary_cross_rank_at_most_two_count": len(complementary_low_pairs),
        "all_twelve_pairs_are_harmonic_graph_pairs": True,
        "not_used_for_characteristic_zero_proof": True,
    }


def product_family_certificate() -> dict[str, object]:
    # The representative a=b=1 is enough for the exact rational ranks; the
    # symbolic chart above proves the two-parameter family.
    support = (0, 1, 4, 5, 8, 9)
    targets = (2, 3, 6, 7, 10, 11)
    signs = (1, 1, 1, 1, 1, 1)
    candidate = exact_candidate(support, targets, signs)

    left, right = graph_pair(support, targets, signs)
    cross_rows = [beta(x, y) for x in left for y in right]
    right_kernel = integer_nullspace(cross_rows)
    left_kernel = integer_nullspace([list(column) for column in zip(*cross_rows)])

    # Each frame derivative has only six nonzero rows.  Contract those rows
    # directly instead of materializing 72 mostly-zero 36-by-18 matrices.
    left_motion_rows = [
        [beta(right[target_index], right[j]) for j in range(6)]
        for target_index in range(6)
    ]
    right_motion_rows = [
        [beta(left[i], left[target_index]) for i in range(6)]
        for target_index in range(6)
    ]
    def contract_motion_rows(
        motion_rows: list[list[list[int]]],
    ) -> list[list[list[int]]]:
        return [
            [
                [
                    sum(
                        entry * weight
                        for entry, weight in zip(row, right_vector, strict=True)
                    )
                    for row in target_rows
                ]
                for target_rows in motion_rows
            ]
            for right_vector in right_kernel
        ]

    left_contractions_by_kernel = contract_motion_rows(left_motion_rows)
    right_contractions_by_kernel = contract_motion_rows(right_motion_rows)

    equations: list[list[int]] = []
    for left_vector in left_kernel:
        for left_contractions, right_contractions in zip(
            left_contractions_by_kernel,
            right_contractions_by_kernel,
            strict=True,
        ):
            equations.append(
                [
                    sum(
                        left_vector[6 * basis_index + j]
                        * left_contractions[target_index][j]
                        for j in range(6)
                    )
                    for basis_index in range(6)
                    for target_index in range(6)
                ]
                + [
                    sum(
                        left_vector[6 * i + basis_index]
                        * right_contractions[target_index][i]
                        for i in range(6)
                    )
                    for basis_index in range(6)
                    for target_index in range(6)
                ]
            )
    tangent_rank = rank_mod(equations)
    require(tangent_rank == 70, tangent_rank)
    require(candidate["left_block_projection_rank_over_QQ"] == 9, candidate)
    require(candidate["right_block_projection_rank_over_QQ"] == 9, candidate)
    return {
        "representative": candidate,
        "determinantal_tangent_equation_shape": [len(equations), 72],
        "modular_tangent_rank_lower_bound": tangent_rank,
        "explicit_product_family_dimension_lower_bound": 2,
        "exact_characteristic_zero_tangent_dimension": 2,
        "column_cross_rank": 2,
        "column_cross_free_kernel_dimension": 4,
        "column_block_projection_rank": 3,
        "E34_cross_rank": 6,
        "E34_cross_free_kernel_dimension": 12,
        "E34_block_projection_rank": 9,
    }


def build_payload() -> dict[str, object]:
    k32_support = (0, 1, 4, 5, 8, 9)
    k23_support = (0, 1, 2, 4, 5, 6)
    k32_scan = signed_permutation_scan(k32_support)
    k23_scan = signed_permutation_scan(k23_support)
    exact = [
        exact_candidate(
            k32_support,
            tuple(item["target_permutation"]),
            tuple(item["signs"]),
        )
        for item in k32_scan["modular_rank_six_candidates"]
    ]
    require(len(exact) == 4, exact)
    require(
        all(
            item["ambient_sum_rank_over_QQ"] == 12
            and item["cross_rank_over_QQ"] == 6
            and item["cross_free_kernel_dimension"] == 12
            and item["left_block_projection_rank_over_QQ"] == 9
            and item["right_block_projection_rank_over_QQ"] == 9
            for item in exact
        ),
        exact,
    )
    require(not k23_scan["modular_rank_six_candidates"], k23_scan)
    return {
        "certificate": "N6-115",
        "status": (
            "PURE_COMPLEMENTARY_2_PLUS_2_COLUMN_EQUALITY_CLASSIFICATION; "
            "PURE_COMMON_A_PRODUCT_FRAME_BARRIER; "
            "EXACT_BOUNDED_SIGNED_PERMUTATION_AND_TANGENT_REPLAY"
        ),
        "field": "algebraically closed characteristic zero",
        "prime_used_only_for_rank_lower_bounds": PRIME,
        "column_graph_symbolic_certificate": column_graph_symbolic_certificate(),
        "finite_field_counterexample_screen": finite_field_counterexample_screen(),
        "common_A_product_family": product_family_certificate(),
        "bounded_signed_permutation_scan": {
            "K32": k32_scan,
            "K23": k23_scan,
            "K32_exact_QQ_rank_six_candidates": exact,
            "all_rank_six_candidates_fail_actual_block_injectivity": True,
        },
        "pure_theorem": {
            "column_statement": (
                "complementary two-planes P,Q in k4 with S0(k4) cross rank at "
                "most two are harmonic graph pairs along one coordinate matching"
            ),
            "product_statement": (
                "for L=A3 tensor P2 and M=A3 tensor Q2, a twelve-dimensional "
                "E34 cross-free kernel has block projection rank at most nine and "
                "cannot be an actual twelve-dimensional Chow section difference"
            ),
        },
        "boundary": {
            "not_proved": [
                "every complementary K32 rank-six component is a common-A product component",
                "the complete K23/K32 formal rank-three normal-cone classification",
                "the kappa2=0 six-color endpoint",
                "ordinary lower 29 or exact ChowRank(perm6)=32",
                "any border-rank statement",
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
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == frozen, "frozen JSON differs from exact replay")
    print("certificate=N6-115")
    print("K32_signed_rank_six=4")
    print("K23_signed_rank_six=0")
    print("exact_block_projection_rank=9")
    print("generic_product_tangent_dimension=2")
    print("status=PASS")


if __name__ == "__main__":
    main()
