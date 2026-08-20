"""Exact two-line pencil classification for the K3,2 first-Schur rays.

The 44 input matrices are the 24 row-changing anti-diagonal rays and the
20 same-row sign rays from N6-126.  For every pair A,B we study

    P(t) = t A + B.

Each 4 by 4 minor has degree at most three: its leading and constant
coefficients vanish because rank(A), rank(B) are both at most three.  Thus
five exact sample values certify an identically rank-three pencil.  Otherwise
we collect a few certified nonzero minors and take their exact QQ gcd; a
constant gcd after removing t excludes every nonzero finite ratio.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_k32_full_first_schur_weight_blocks import (
        full_first_schur_columns,
        grouped_columns,
        same_block_certificate,
    )
except ModuleNotFoundError:  # Direct script execution.
    from n6_k32_full_first_schur_weight_blocks import (
        full_first_schur_columns,
        grouped_columns,
        same_block_certificate,
    )


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_two_line_pencil_classification.json"
SAMPLE_VALUES = (1, 2, 3, 5, 7)
PRIME = 1_000_003


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def determinant4(matrix: list[list[int]]) -> int:
    answer = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        answer += (-1 if inversions % 2 else 1) * term
    return answer


def rank_four_pivots(
    rows: list[list[int]],
) -> tuple[list[int], list[int]] | None:
    """Return four independent source rows and pivot columns modulo PRIME."""

    basis: list[list[int]] = []
    pivot_columns: list[int] = []
    source_rows: list[int] = []
    for source, original in enumerate(rows):
        row = [value % PRIME for value in original]
        for pivot, pivot_row in zip(pivot_columns, basis, strict=True):
            coefficient = row[pivot]
            if coefficient:
                row = [
                    (value - coefficient * previous) % PRIME
                    for value, previous in zip(row, pivot_row, strict=True)
                ]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        inverse = pow(row[pivot], -1, PRIME)
        row = [(value * inverse) % PRIME for value in row]
        pivot_columns.append(pivot)
        basis.append(row)
        source_rows.append(source)
        if len(pivot_columns) == 4:
            selected_rows = source_rows[:4]
            selected_columns = pivot_columns[:4]
            witness = [
                [rows[row][column] for column in selected_columns]
                for row in selected_rows
            ]
            require(determinant4(witness) % PRIME != 0, (selected_rows, selected_columns))
            return selected_rows, selected_columns
    return None


def candidate_data() -> tuple[list[str], list[list[list[int]]]]:
    labels, columns = full_first_schur_columns()
    groups = grouped_columns(labels)
    names: list[str] = []
    matrices: list[list[list[int]]] = []
    for key, indices in sorted(groups.items()):
        if key[0] == 1:
            vectors = [(1, -1)]
        else:
            vectors = [
                tuple(vector)
                for vector in same_block_certificate(columns, indices)[
                    "rank_at_most_three_lines"
                ]
            ]
        for vector in vectors:
            matrix = sum(
                (vector[position] * columns[index] for position, index in enumerate(indices)),
                sp.zeros(33, 15),
            )
            require(matrix.rank() == 3, (key, vector, matrix.rank()))
            names.append(f"{'change' if key[0] else 'same'}:{key}:{vector}")
            matrices.append([[int(value) for value in row] for row in matrix.tolist()])
    require(len(names) == 44, len(names))
    return names, matrices


def pencil_rows(left: list[list[int]], right: list[list[int]], value: int) -> list[list[int]]:
    return [
        [value * left[row][column] + right[row][column] for column in range(15)]
        for row in range(33)
    ]


def exact_rank(rows: list[list[int]]) -> int:
    return int(sp.Matrix(rows).rank())


def minor_polynomial(
    left: list[list[int]], right: list[list[int]], rows: list[int], columns: list[int]
) -> sp.Poly:
    variable = sp.symbols("t")
    values = []
    for value in range(4):
        matrix = [
            [value * left[row][column] + right[row][column] for column in columns]
            for row in rows
        ]
        values.append(determinant4(matrix))
    polynomial = sp.Poly(
        sp.interpolate([(value, values[value]) for value in range(4)], variable),
        variable,
        domain=sp.QQ,
    )
    require(polynomial.degree() <= 3 or polynomial.is_zero, polynomial)
    return polynomial


def remove_zero_root(polynomial: sp.Poly) -> sp.Poly:
    variable = polynomial.gens[0]
    result = polynomial
    while not result.is_zero and result.eval(0) == 0:
        result = sp.quo(result, sp.Poly(variable, variable, domain=sp.QQ))
    return result.monic() if not result.is_zero else result


def projectively_equal(left: list[list[int]], right: list[list[int]]) -> bool:
    left_flat = [value for row in left for value in row]
    right_flat = [value for row in right for value in row]
    pivot = next((index for index, value in enumerate(right_flat) if value), None)
    if pivot is None:
        return all(value == 0 for value in left_flat)
    if left_flat[pivot] == 0:
        return False
    left_scale = left_flat[pivot]
    right_scale = right_flat[pivot]
    return all(
        left_value * right_scale == right_value * left_scale
        for left_value, right_value in zip(left_flat, right_flat, strict=True)
    )


def exact_four_pivots(rows: list[list[int]]) -> tuple[list[int], list[int]]:
    matrix = sp.Matrix(rows)
    rows_out = list(matrix.T.rref()[1])[:4]
    columns_out = list(matrix.rref()[1])[:4]
    require(len(rows_out) == 4 and len(columns_out) == 4, "exact rank below four")
    witness = [
        [rows[row][column] for column in columns_out]
        for row in rows_out
    ]
    require(determinant4(witness) != 0, (rows_out, columns_out))
    return rows_out, columns_out


def build_payload() -> dict[str, object]:
    names, matrices = candidate_data()
    identical_pairs: list[list[int]] = []
    no_nonzero_root_pairs: list[list[int]] = []
    exceptional_pairs: list[dict[str, object]] = []
    pair_count = 0
    variable = sp.symbols("t")

    for left_index, right_index in combinations(range(len(matrices)), 2):
        pair_count += 1
        selected_polynomials: list[sp.Poly] = []
        all_sample_ranks_le_three = True
        sample_rows: list[list[list[int]]] = []
        for sample in SAMPLE_VALUES:
            rows = pencil_rows(matrices[left_index], matrices[right_index], sample)
            sample_rows.append(rows)
            witness = rank_four_pivots(rows)
            if witness is None:
                continue
            all_sample_ranks_le_three = False
            selected_polynomials.append(
                minor_polynomial(
                    matrices[left_index],
                    matrices[right_index],
                    witness[0],
                    witness[1],
                )
            )

        if all_sample_ranks_le_three:
            require(
                all(exact_rank(rows) <= 3 for rows in sample_rows),
                (left_index, right_index),
            )
            identical_pairs.append([left_index, right_index])
            continue

        gcd = None
        for polynomial in selected_polynomials:
            if polynomial.is_zero:
                continue
            gcd = polynomial if gcd is None else sp.gcd(gcd, polynomial)
            if gcd.degree() == 0:
                break
        require(gcd is not None, (left_index, right_index))
        pair_exceptionals: list[dict[str, object]] = []
        while True:
            stripped = remove_zero_root(gcd)
            if stripped.degree() == 0:
                no_nonzero_root_pairs.append([left_index, right_index])
                break
            factors = sp.factor_list(stripped.as_expr())[1]
            require(factors and all(factor.as_poly().degree() == 1 for factor, _ in factors),
                    (left_index, right_index, stripped))
            changed = False
            for factor, _multiplicity in factors:
                linear = factor.as_poly()
                root = sp.factor(-linear.nth(0) / linear.nth(1))
                require(root.is_Rational and root != 0, (left_index, right_index, root))
                numerator, denominator = int(root.p), int(root.q)
                scaled = [
                    [
                        numerator * matrices[left_index][row][column]
                        + denominator * matrices[right_index][row][column]
                        for column in range(15)
                    ]
                    for row in range(33)
                ]
                if exact_rank(scaled) > 3:
                    witness = exact_four_pivots(scaled)
                    extra = minor_polynomial(
                        matrices[left_index],
                        matrices[right_index],
                        witness[0],
                        witness[1],
                    )
                    gcd = sp.gcd(gcd, extra)
                    changed = True
                    break
                target = next(
                    index for index, matrix in enumerate(matrices)
                    if projectively_equal(scaled, matrix)
                )
                pair_exceptionals.append(
                    {
                        "pair": [left_index, right_index],
                        "ratio": [numerator, denominator],
                        "resulting_line": target,
                    }
                )
            if changed:
                pair_exceptionals.clear()
                continue
            exceptional_pairs.extend(pair_exceptionals)
            break

    require(pair_count == 946, pair_count)
    require(len(identical_pairs) == 102, len(identical_pairs))
    require(len(no_nonzero_root_pairs) == 844, len(no_nonzero_root_pairs))
    require(len(exceptional_pairs) == 0, len(exceptional_pairs))
    return {
        "certificate": "N6-128",
        "status": "EXACT_QQ_TWO_LINE_PENCIL_CLASSIFICATION",
        "field": "characteristic zero",
        "candidate_count": len(names),
        "candidate_names": names,
        "pair_count": pair_count,
        "sample_values": list(SAMPLE_VALUES),
        "minor_degree_bound": 3,
        "identically_rank_three_pair_count": len(identical_pairs),
        "no_nonzero_finite_root_pair_count": len(no_nonzero_root_pairs),
        "exceptional_ratio_pair_count": len(exceptional_pairs),
        "exceptional_ratio": -1,
        "exceptional_pairs": exceptional_pairs,
        "consequence": (
            "Every two-line pencil is either identically rank at most three or "
            "has no nonzero finite rank-three point."
        ),
        "boundary": [
            "classifies only pairs of the 44 fixed first-Schur lines",
            "does not classify sums of three or more torus weights",
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
    print("certificate=N6-128")
    print("candidate_count=44")
    print("pair_count=946")
    print("identical=102")
    print("no_nonzero_root=844")
    print("exceptional_ratio_count=0")
    print("status=PASS")


if __name__ == "__main__":
    main()
