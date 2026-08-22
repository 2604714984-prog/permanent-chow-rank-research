"""Exact full-graph first-Schur torus blocks at the K3,2 collision."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_product_32_rank_six_frame_barrier import beta, rank_mod, require
except ModuleNotFoundError:  # Direct script execution.
    from n6_product_32_rank_six_frame_barrier import beta, rank_mod, require


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_full_first_schur_weight_blocks.json"
SUPPORT = (0, 1, 4, 5, 8, 9)
COMPLEMENT = (2, 3, 6, 7, 10, 11)


def unit(index: int) -> list[int]:
    return [int(i == index) for i in range(12)]


def pivot_rows_and_columns(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    _, columns = matrix.rref()
    columns = list(columns)
    rows = list(matrix[:, columns].T.rref()[1])
    return rows, columns


def full_first_schur_columns() -> tuple[list[tuple[str, int, int]], list[sp.Matrix]]:
    left = [unit(index) for index in SUPPORT]
    right = [unit(index) for index in SUPPORT]
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
    columns: list[sp.Matrix] = []
    for side in ("L", "M"):
        for basis_index, source in enumerate(SUPPORT):
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
                schur = derivative.extract(lower_rows, right_columns) - (
                    c1 * inverse0 * b0
                    + c0 * inverse1 * b0
                    + c0 * inverse0 * b1
                )
                labels.append((side, target, source))
                columns.append(schur)
    return labels, columns


def block_key(label: tuple[str, int, int]) -> tuple[int, ...]:
    _side, target, source = label
    target_row, target_column = divmod(target, 4)
    source_row, source_column = divmod(source, 4)
    target_column -= 2
    if target_row == source_row:
        return (0, target_column, source_column)
    return (1, target_row, source_row, target_column, source_column)


def grouped_columns(
    labels: list[tuple[str, int, int]],
) -> dict[tuple[int, ...], list[int]]:
    groups: dict[tuple[int, ...], list[int]] = {}
    for index, label in enumerate(labels):
        groups.setdefault(block_key(label), []).append(index)
    return groups


def coefficient_matrix(
    columns: list[sp.Matrix], indices: list[int], symbols: tuple[sp.Symbol, ...]
) -> sp.Matrix:
    result = sp.zeros(33, 15)
    for symbol, index in zip(symbols, indices, strict=True):
        result += symbol * columns[index]
    return result


def nonzero_support(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    rows = [
        i for i in range(matrix.rows)
        if any(matrix[i, j] != 0 for j in range(matrix.cols))
    ]
    columns = [
        j for j in range(matrix.cols)
        if any(matrix[i, j] != 0 for i in rows)
    ]
    return rows, columns


def normalize_vector(vector: sp.Matrix) -> list[int]:
    values = [sp.Rational(value) for value in vector]
    first = next(value for value in values if value != 0)
    values = [sp.factor(value / first) for value in values]
    require(all(value.q == 1 for value in values), values)
    return [int(value) for value in values]


def change_block_certificate(
    columns: list[sp.Matrix], indices: list[int]
) -> dict[str, object]:
    a, b = sp.symbols("a b")
    matrix = coefficient_matrix(columns, indices, (a, b))
    rows, output_columns = nonzero_support(matrix)
    minors: set[sp.Expr] = set()
    for row_set in combinations(rows, 4):
        determinant = sp.factor(matrix.extract(row_set, output_columns).det())
        if determinant != 0:
            minors.add(sp.expand(determinant))
    require(matrix.subs({a: 1, b: 1}).rank() == 4, matrix)
    require(matrix.subs({a: 1, b: -1}).rank() == 3, matrix)
    require(all(sp.rem(item, a + b, domain=sp.QQ) == 0 for item in minors), minors)
    common_factor = sp.factor(sp.gcd_list(list(minors)))
    factor_ratio = sp.factor(common_factor / (a + b))
    require(factor_ratio.is_number and factor_ratio != 0, common_factor)
    quotients = [sp.cancel(item / (a + b)) for item in minors]
    univariate = [sp.Poly(item.subs(b, 1), a) for item in quotients]
    quotient_gcd = univariate[0]
    for polynomial in univariate[1:]:
        quotient_gcd = sp.gcd(quotient_gcd, polynomial)
    require(quotient_gcd.degree() == 0, quotient_gcd)
    b_zero_candidates = sorted(
        (item for item in minors if item.subs(b, 0) != 0),
        key=lambda item: str(sp.factor(item)),
    )
    b_zero_witness = b_zero_candidates[0] if b_zero_candidates else None
    require(b_zero_witness is not None, minors)
    return {
        "variable_count": 2,
        "support_shape": [len(rows), len(output_columns)],
        "generic_rank": 4,
        "rank_on_anti_diagonal": 3,
        "nonzero_4x4_minor_count": len(minors),
        "rank_at_most_three_locus": "a+b=0",
        "all_minors_divisible_by": "a+b",
        "quotient_gcd_at_b1": "1",
        "b_zero_witness": str(sp.factor(b_zero_witness)),
    }


def same_block_certificate(
    columns: list[sp.Matrix], indices: list[int]
) -> dict[str, object]:
    symbols = sp.symbols("l0:3") + sp.symbols("m0:3")
    matrix = coefficient_matrix(columns, indices, symbols)
    rows, output_columns = nonzero_support(matrix)
    require(len(output_columns) == 6, output_columns)
    column_forms: list[list[str]] = []
    for column in output_columns:
        forms = sorted({
            str(sp.factor(matrix[row, column]))
            for row in rows
            if matrix[row, column] != 0
        })
        column_forms.append(forms)
    # Every nonzero row belongs to only one output column.  Hence the matrix
    # rank is the number of active output columns, so rank <= 3 means that at
    # least three columns vanish identically.
    lines: list[list[int]] = []
    zero_column_triples: list[list[int]] = []
    for triple in combinations(range(6), 3):
        equations: list[list[sp.Expr]] = []
        for column in triple:
            for form in [
                sp.sympify(text, locals=dict(zip(symbols, symbols)))
                for text in column_forms[column]
            ]:
                equations.append([sp.expand(form).coeff(symbol) for symbol in symbols])
        coefficient = sp.Matrix(equations)
        nullspace = coefficient.nullspace()
        if not nullspace:
            continue
        require(len(nullspace) == 1, (triple, nullspace))
        line = normalize_vector(nullspace[0])
        zero_column_triples.append(list(triple))
        if line not in lines:
            lines.append(line)
    lines.sort()
    require(len(lines) == 5, lines)
    expected = [
        [1, 1, 1, 1, 1, 1],
        [1, -1, -1, 1, -1, -1],
        [1, -1, 1, 1, -1, 1],
        [1, 1, -1, 1, 1, -1],
        [1, 1, 1, -1, -1, -1],
    ]
    require(lines == sorted(expected), lines)
    return {
        "variable_count": 6,
        "support_shape": [len(rows), len(output_columns)],
        "row_support_is_column_disjoint": True,
        "rank_at_most_three_line_count": len(lines),
        "rank_at_most_three_lines": lines,
        "zero_column_triples": zero_column_triples,
        "column_forms": column_forms,
        "locus_argument": (
            "Each nonzero matrix row has support in one output column. "
            "Thus rank is the number of active columns; enumerating the "
            "20 triples of zero columns leaves exactly these five lines."
        ),
    }


def build_payload() -> dict[str, object]:
    labels, columns = full_first_schur_columns()
    groups = grouped_columns(labels)
    change_profiles: list[dict[str, object]] = []
    same_profiles: list[dict[str, object]] = []
    for key, indices in sorted(groups.items()):
        if key[0] == 1:
            require(len(indices) == 2, (key, indices))
            profile = change_block_certificate(columns, indices)
            profile["weight_key"] = list(key)
            profile["labels"] = [list(labels[index]) for index in indices]
            change_profiles.append(profile)
        else:
            require(len(indices) == 6, (key, indices))
            profile = same_block_certificate(columns, indices)
            profile["weight_key"] = list(key)
            profile["labels"] = [list(labels[index]) for index in indices]
            same_profiles.append(profile)
    require(len(change_profiles) == 24, len(change_profiles))
    require(len(same_profiles) == 4, len(same_profiles))
    require(
        all(item["rank_at_most_three_locus"] == "a+b=0" for item in change_profiles),
        change_profiles,
    )
    require(
        all(item["rank_at_most_three_line_count"] == 5 for item in same_profiles),
        same_profiles,
    )
    return {
        "certificate": "N6-126",
        "status": "EXACT_QQ_FULL_FIRST_SCHUR_WEIGHT_BLOCKS",
        "field": "characteristic zero",
        "hypothesis": "full 72-variable Grassmann graph chart at L=M=A3 tensor P2",
        "base_cross_rank": 3,
        "first_schur_shape": [33, 15],
        "coefficient_matrix_shape": [495, 72],
        "coefficient_matrix_rank": 72,
        "weight_block_count": len(groups),
        "row_changing_block_count": len(change_profiles),
        "same_row_block_count": len(same_profiles),
        "row_changing_profiles": change_profiles,
        "same_row_profiles": same_profiles,
        "fixed_direction_count": 24 + 4 * 5,
        "consequence": (
            "In the full graph chart, each row-changing character has only "
            "the anti-diagonal rank-three line. Each same-row character has "
            "four explicit sign lines. This is a fixed-weight classification; "
            "sums of different characters and nonlinear lifts remain open."
        ),
        "boundary": [
            "does not classify mixed torus-weight sums",
            "does not classify the full first tangent cone",
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
    print("certificate=N6-126")
    print("weight_blocks=28")
    print("fixed_rank_three_lines=44")
    print("status=PASS")


if __name__ == "__main__":
    main()
