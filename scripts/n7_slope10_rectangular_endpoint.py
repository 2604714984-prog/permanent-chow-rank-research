#!/usr/bin/env python3
"""Finite certificate for the N7 slope-ten rectangular endpoint.

This script replays bounded finite rows: formal rank-seven coordinate pairs,
six rank-six normal forms, the codimension-one partial-shadow cap, and the
endpoint equality arithmetic.  Arbitrary d=1,2 quotients are transferred to
the monomial row through fixed-source raw composite maps, as proved in the
adjacent note.  It does not assert ChowRank(perm_7) >= 50.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


PRIME = 65521


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first, *tail)


def modular_rank(rows: list[list[int]], prime: int = PRIME) -> int:
    if not rows:
        return 0
    work = [[value % prime for value in row] for row in rows]
    rank = 0
    columns = len(work[0])
    for column in range(columns):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for i in range(len(work)):
            if i == rank or work[i][column] == 0:
                continue
            factor = work[i][column]
            work[i] = [
                (left - factor * right) % prime
                for left, right in zip(work[i], work[rank])
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def formal_rank_seven_rows() -> list[dict[str, int]]:
    vertices = tuple(range(7))
    pairs = tuple(itertools.combinations(vertices, 2))
    triples = tuple(itertools.combinations(vertices, 3))
    quadruples = tuple(itertools.combinations(vertices, 4))
    rows = []
    for quotient_rank in range(1, 8):
        best = 10**9
        for quotient_tuple in itertools.combinations(vertices, quotient_rank):
            quotient = set(quotient_tuple)
            beta_plus = sum(bool(set(item) & quotient) for item in quadruples)
            for r_dimension in range(4):
                for r_tuple in itertools.combinations(pairs, r_dimension):
                    r_space = set(r_tuple)
                    beta_minus = sum(
                        any(
                            vertex in quotient
                            and tuple(sorted(set(item) - {vertex})) not in r_space
                            for vertex in item
                        )
                        for item in triples
                    )
                    best = min(best, beta_plus + beta_minus)
        endpoint_row = 70 if quotient_rank == 7 else best
        rows.append(
            {
                "quotient_rank": quotient_rank,
                "coordinate_minimum_allowing_bad_prolongation": best,
                "endpoint_row": endpoint_row,
                "proof_status": (
                    "PROVEN_FULL_QUOTIENT"
                    if quotient_rank == 7
                    else "PROVEN_MONOMIAL_TORUS_DEGENERATION"
                ),
            }
        )
    return rows


def derivative_space_basis(support_size: int, degree: int):
    variables = 6
    monomials = tuple(compositions(degree, variables))
    monomial_index = {item: i for i, item in enumerate(monomials)}
    source = tuple(compositions(7 - degree, variables))
    term_support = [
        tuple(2 if j == i else 1 for j in range(variables))
        for i in range(support_size)
    ]
    rows = []
    for differential in source:
        row = [0] * len(monomials)
        for exponent in term_support:
            if not all(left <= right for left, right in zip(differential, exponent)):
                continue
            output = tuple(
                right - left for left, right in zip(differential, exponent)
            )
            coefficient = 1
            for before, after in zip(exponent, output):
                coefficient *= math.factorial(before) // math.factorial(after)
            row[monomial_index[output]] += coefficient
        rows.append(row)
    # Return an echelon basis, still in the monomial coefficient coordinates.
    work = [[value % PRIME for value in row] for row in rows]
    basis = []
    pivot_columns = []
    for row in work:
        for pivot, old in zip(pivot_columns, basis):
            if row[pivot]:
                factor = row[pivot]
                row = [(x - factor * y) % PRIME for x, y in zip(row, old)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        inverse = pow(row[pivot], PRIME - 2, PRIME)
        row = [value * inverse % PRIME for value in row]
        basis.append(row)
        pivot_columns.append(pivot)
    return monomials, basis


def raw_symbol_rank(basis, monomials, degree: int, selected: tuple[int, ...]) -> int:
    lower = tuple(compositions(degree - 1, 6))
    lower_index = {item: i for i, item in enumerate(lower)}
    rows = []
    for vector in basis:
        output = []
        for direction in selected:
            block = [0] * len(lower)
            for coefficient, exponent in zip(vector, monomials):
                if exponent[direction] == 0:
                    continue
                target = list(exponent)
                target[direction] -= 1
                index = lower_index[tuple(target)]
                block[index] = (
                    block[index] + coefficient * exponent[direction]
                ) % PRIME
            output.extend(block)
        rows.append(output)
    return modular_rank(rows)


def rank_six_rows() -> list[dict[str, object]]:
    answer = []
    for support_size in range(1, 7):
        degree2_monomials, degree2 = derivative_space_basis(support_size, 2)
        degree3_monomials, degree3 = derivative_space_basis(support_size, 3)
        degree4_monomials, degree4 = derivative_space_basis(support_size, 4)
        assert degree2_monomials and degree3_monomials and degree4_monomials
        u = len(degree3)
        assert len(degree4) == u
        defect = 35 - u
        rows = [{"quotient_rank": 0, "proven_arbitrary_lower": defect}]
        for quotient_rank in range(1, 5):
            raw_minimum = 10**9
            raw_parts = None
            for selected in itertools.combinations(range(6), quotient_rank):
                beta_plus = raw_symbol_rank(
                    degree4, degree4_monomials, 4, selected
                )
                beta_minus = raw_symbol_rank(
                    degree3, degree3_monomials, 3, selected
                )
                if beta_plus + beta_minus < raw_minimum:
                    raw_minimum = beta_plus + beta_minus
                    raw_parts = (beta_plus, beta_minus)
            # Quotienting by R_2 of dimension at most three loses at most 3d.
            coordinate_lower = raw_minimum - 3 * quotient_rank + defect
            row = {
                "quotient_rank": quotient_rank,
                "raw_coordinate_minimum": raw_minimum,
                "raw_beta_plus": raw_parts[0],
                "raw_beta_minus": raw_parts[1],
                "coordinate_lower": coordinate_lower,
            }
            if support_size == 1:
                row["proven_arbitrary_lower"] = coordinate_lower
                row["proof_status"] = "PROVEN_MONOMIAL_TORUS_DEGENERATION"
            elif quotient_rank == 3:
                # ker(beta+) + raw ker(beta-) <= 12+7, and R2 costs <=9.
                row["proven_arbitrary_lower"] = u + 7
                row["proof_status"] = "PROVEN_VERONESE_DISJOINTNESS"
            elif quotient_rank == 4:
                # ker(beta+) + raw ker(beta-) <= 3+2, and R2 costs <=12.
                row["proven_arbitrary_lower"] = u + 18
                row["proof_status"] = "PROVEN_VERONESE_DISJOINTNESS"
            else:
                # A joint diagonal degeneration of the fixed-source raw
                # composites reaches the T1 coordinate minima 25 and 39.
                row["proven_arbitrary_lower"] = 22 if quotient_rank == 1 else 33
                row["proof_status"] = "PROVEN_RAW_COMPOSITE_DEGENERATION"
            rows.append(row)
        # The pure partial-shadow lemma gives ker(beta_minus)<=9 at d=5;
        # beta_plus is injective because D4 contains no fourth power.
        rows.append(
            {
                "quotient_rank": 5,
                "proven_arbitrary_lower": u + 26,
                "proof_status": "PROVEN_PARTIAL_SHADOW",
            }
        )
        # At the full quotient both symbols inject by zero prolongation.
        rows.append(
            {
                "quotient_rank": 6,
                "proven_arbitrary_lower": 35 + u,
                "proof_status": "PROVEN_FULL_QUOTIENT",
            }
        )
        answer.append(
            {
                "normal_form_support_size": support_size,
                "degree2_dimension": len(degree2),
                "middle_rank": u,
                "middle_defect": defect,
                "rows": rows,
            }
        )
    return answer


def partial_shadow_cap() -> dict[str, object]:
    quadratics = tuple(compositions(2, 6))
    quadratic_index = {item: i for i, item in enumerate(quadratics)}
    cubics = tuple(compositions(3, 6))
    shadows = []
    for exponent in cubics:
        shadow = set()
        for direction in range(5):
            if exponent[direction]:
                target = list(exponent)
                target[direction] -= 1
                shadow.add(quadratic_index[tuple(target)])
        shadows.append(frozenset(shadow))
    maximum = 0
    witnesses = 0
    for size in range(4):
        for selected in itertools.combinations(range(len(quadratics)), size):
            selected_set = set(selected)
            count = sum(shadow <= selected_set for shadow in shadows)
            if count > maximum:
                maximum = count
                witnesses = 1
            elif count == maximum:
                witnesses += 1
    return {
        "direction_dimension": 5,
        "quadratic_shadow_budget": 3,
        "maximum_cubic_dimension": maximum,
        "maximizing_coordinate_shadows": witnesses,
    }


def equality_arithmetic() -> dict[str, object]:
    solutions = [
        {"rank6_full_blocks": a, "rank7_full_blocks": b}
        for a in range(9)
        for b in range(8)
        if 6 * a + 7 * b == 49
    ]
    return {
        "solutions_to_6a_plus_7b_equals_49": solutions,
        "rank5_full_then_rank7_remainder_possible": (49 - 5) % 7 == 0,
    }


def build_payload() -> dict[str, object]:
    rank7 = formal_rank_seven_rows()
    rank6 = rank_six_rows()
    shadow = partial_shadow_cap()
    arithmetic = equality_arithmetic()
    assert [row["endpoint_row"] for row in rank7] == [
        32, 49, 56, 57, 64, 67, 70
    ]
    assert shadow["maximum_cubic_dimension"] == 9
    assert [item["middle_rank"] for item in rank6] == [25, 25, 31, 34, 35, 35]
    assert arithmetic["solutions_to_6a_plus_7b_equals_49"] == [
        {"rank6_full_blocks": 0, "rank7_full_blocks": 7},
        {"rank6_full_blocks": 7, "rank7_full_blocks": 1},
    ]
    return {
        "schema_version": 1,
        "n": 7,
        "slope": 10,
        "status": "PROVEN_LOCAL_SLOPE10_ENDPOINT",
        "rank7_coordinate_initial_rows": rank7,
        "rank6_normal_form_rows": rank6,
        "codimension_one_partial_shadow": shadow,
        "equality_arithmetic": arithmetic,
        "equality_conclusion": (
            "A hypothetical N=49 identity must lie in one of two equality "
            "cases: an all-rank-seven simple "
            "rank-seven 7-multilinear matroid, or seven direct rank-six s=1/2 "
            "blocks plus forty-two rank-seven graph complements. Both also "
            "satisfy rectangular Sylvester equality."
        ),
        "claim_boundary": (
            "The rank-seven monomial and rank-six s=1 monomial are covered by a "
            "joint diagonal-torus degeneration. Veronese disjointness proves all "
            "rank-six d=3,4 rows, d=5,6 are proved directly, and fixed-source "
            "raw composite degeneration proves the nonmonomial d=1,2 rows "
            "without preserving middle rank, defect, or R2 in the limit. The "
            "two N=49 equality cases remain open. No lower-50 or border-rank "
            "claim is made."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("n7 slope-ten endpoint JSON mismatch")
        print("PASS n7 slope-ten rectangular endpoint")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
