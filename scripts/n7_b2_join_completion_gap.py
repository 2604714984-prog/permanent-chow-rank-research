#!/usr/bin/env python3
"""Exact quotient-gap basis and generic fifth-term test for B2 joins."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

from flint import fmpq_mat
import sympy as sp


HERE = Path(__file__).resolve().parent
JOIN_PATH = HERE / "n7_b2_two_transposition_join_obstruction.py"
SPEC = importlib.util.spec_from_file_location(
    "n7_b2_two_transposition_join_obstruction", JOIN_PATH
)
join = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(join)


def pivot_columns(matrix: fmpq_mat) -> list[int]:
    reduced, rank = matrix.rref()
    pivots = []
    for row in range(rank):
        pivot = next(
            column for column in range(matrix.ncols()) if reduced[row, column]
        )
        pivots.append(pivot)
    return pivots


def kernel_columns(matrix: fmpq_mat) -> fmpq_mat:
    reduced, rank = matrix.rref()
    pivots = pivot_columns(matrix)
    free = [column for column in range(matrix.ncols()) if column not in pivots]
    entries = [[0 for _ in free] for _ in range(matrix.ncols())]
    for basis_column, free_column in enumerate(free):
        entries[free_column][basis_column] = 1
        for row, pivot in enumerate(pivots):
            entries[pivot][basis_column] = -reduced[row, free_column]
    answer = fmpq_mat(entries)
    if (matrix * answer).rank() != 0 or answer.ncols() != matrix.ncols() - rank:
        raise AssertionError("exact kernel reconstruction failed")
    return answer


def concatenate_columns(left: fmpq_mat, right: fmpq_mat) -> fmpq_mat:
    if left.nrows() != right.nrows():
        raise ValueError("column concatenation needs equal row counts")
    return fmpq_mat(
        [
            [left[row, column] for column in range(left.ncols())]
            + [right[row, column] for column in range(right.ncols())]
            for row in range(left.nrows())
        ]
    )


def base_complex(
    pairs: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[sp.Matrix, sp.Matrix, fmpq_mat, fmpq_mat]:
    factors = join.pair_slice_terms(pairs[0], (7, 8), sp.Rational(1, 2))
    factors += join.pair_slice_terms(pairs[1], (9, 10), sp.Rational(1, 2))
    local = [join.formal_maps(term) for term in factors]
    sympy_b = sp.Matrix.hstack(*(row[0] for row in local))
    sympy_c = sp.Matrix.vstack(*(row[1] for row in local))
    return sympy_b, sympy_c, join.flint_matrix(sympy_b), join.flint_matrix(sympy_c)


def quotient_gap(
    name: str, pairs: tuple[tuple[int, int], tuple[int, int]]
) -> dict[str, object]:
    _, _, matrix_b, matrix_c = base_complex(pairs)
    kernel = kernel_columns(matrix_b)
    combined = concatenate_columns(matrix_c, kernel)
    extension_indices = [
        column - matrix_c.ncols()
        for column in pivot_columns(combined)
        if column >= matrix_c.ncols()
    ]
    representatives = fmpq_mat(
        [
            [kernel[row, column] for column in extension_indices]
            for row in range(kernel.nrows())
        ]
    )
    defect = len(extension_indices)
    if concatenate_columns(matrix_c, representatives).rank() != matrix_c.rank() + defect:
        raise AssertionError("gap representatives failed to extend image(C)")
    sparse = []
    for output_column, kernel_column in enumerate(extension_indices):
        entries = [
            [row, str(representatives[row, output_column])]
            for row in range(representatives.nrows())
            if representatives[row, output_column]
        ]
        sparse.append(
            {
                "kernel_basis_column": kernel_column,
                "support_by_35_column_term_block": [
                    sum(1 for row, _ in entries if 35 * block <= row < 35 * (block + 1))
                    for block in range(4)
                ],
                "entries": entries,
            }
        )
    return {
        "join_type": name,
        "kernel_B_dimension": kernel.ncols(),
        "rank_C": matrix_c.rank(),
        "kernel_B_intersection_image_C_dimension": kernel.ncols() - defect,
        "quotient_gap_dimension": defect,
        "selected_kernel_basis_columns": extension_indices,
        "sparse_gap_representatives": sparse,
    }


def graph_term(kind: str) -> list[tuple[sp.Integer, ...]]:
    basis = [
        tuple(sp.Integer(row == column) for column in range(11))
        for row in range(11)
    ]
    factors = []
    for column in range(7):
        vector = list(basis[column])
        if kind == "diagonal":
            vector[7 + column % 4] = 1
        elif kind == "dense_vandermonde":
            for row in range(4):
                vector[7 + row] = (column + 1) ** row
        elif kind == "zero_graph":
            pass
        else:
            raise ValueError(("unknown graph-term control", kind))
        factors.append(tuple(vector))
    return factors


def fifth_term_control(
    name: str,
    pairs: tuple[tuple[int, int], tuple[int, int]],
    kind: str,
) -> dict[str, object]:
    sympy_b, sympy_c, old_b, old_c = base_complex(pairs)
    extra_b, extra_c = join.formal_maps(graph_term(kind))
    new_b = join.flint_matrix(sp.Matrix.hstack(sympy_b, extra_b))
    new_c = join.flint_matrix(sp.Matrix.vstack(sympy_c, extra_c))
    old_ranks = (old_b.rank(), old_c.rank(), (old_b * old_c).rank())
    new_ranks = (new_b.rank(), new_c.rank(), (new_b * new_c).rank())
    increments = tuple(new - old for new, old in zip(new_ranks, old_ranks))
    old_defect = old_b.ncols() - old_ranks[0] - old_ranks[1] + old_ranks[2]
    new_defect = new_b.ncols() - new_ranks[0] - new_ranks[1] + new_ranks[2]
    return {
        "join_type": name,
        "fifth_term_kind": kind,
        "fifth_term_factor_rank": sp.Matrix(graph_term(kind)).rank(),
        "old_ranks_B_C_BC": list(old_ranks),
        "rank_increments_B_C_BC": list(increments),
        "new_ranks_B_C_BC": list(new_ranks),
        "old_defect": old_defect,
        "new_defect": new_defect,
        "defect_eliminated": new_defect == 0,
        "polynomial_identity_preserved_by_direct_append": False,
    }


def build_payload() -> dict[str, object]:
    gaps = [quotient_gap(name, pairs) for name, pairs in join.JOIN_TYPES.items()]
    controls = [
        fifth_term_control(name, pairs, kind)
        for name, pairs in join.JOIN_TYPES.items()
        for kind in ("zero_graph", "diagonal", "dense_vandermonde")
    ]
    dense = {
        row["join_type"]: row
        for row in controls
        if row["fifth_term_kind"] == "dense_vandermonde"
    }
    if any(row["rank_increments_B_C_BC"] != [35, 35, 35] for row in dense.values()):
        raise AssertionError("dense graph control missed the generic maximum increments")
    if {row["join_type"]: row["quotient_gap_dimension"] for row in gaps} != {
        "shared_row_01_02": 10,
        "disjoint_01_23": 12,
    }:
        raise AssertionError("unexpected explicit quotient-gap dimensions")
    return {
        "schema_version": 1,
        "status": "JOIN_GAP_EXPLICIT_GENERIC_FIFTH_TERM_CANNOT_REPAIR",
        "quotient_gaps": gaps,
        "fifth_term_controls": controls,
        "generic_increment_theorem": {
            "formula": "defect_new=defect_old+35-delta_B-delta_C+delta_BC",
            "maximum_increment_bounds": [35, 35, 35],
            "exact_dense_point_increments": [35, 35, 35],
            "conclusion": "The simultaneous maximum-rank locus is a nonempty Zariski-open set. On it defect_new=defect_old, so a general rank-seven graph term cannot repair either join gap.",
            "necessary_special_condition_for_repair": "delta_B+delta_C-delta_BC must equal 35+defect_old; in particular, if delta_B=35 then delta_C-delta_BC must equal defect_old.",
        },
        "identity_append_obstruction": "The four joined terms already equal the three-monomial target. Directly appending one nonzero rank-seven Chow product changes the polynomial, so an identity-preserving fifth-term completion is impossible without jointly deforming the first four terms.",
        "candidate_cardinality_checked_before_materialization": {
            "join_types": 2,
            "gap_dimensions": [10, 12],
            "fifth_term_structural_controls_per_join": 3,
            "maximum_middle_dimension": 175,
            "B_shape_with_fifth_term": [1001, 175],
            "C_shape_with_fifth_term": [175, 286],
            "full_degree_seven_monomials_skipped": 202927725,
        },
        "conservative_peak_memory_mib": 128,
        "decision": "GENERIC_ONE_TERM_OPERATOR_REPAIR_IMPOSSIBLE_DIRECT_IDENTITY_APPEND_IMPOSSIBLE",
        "claim_boundary": [
            "The quotient-gap representatives are exact rational kernel vectors selected modulo the exact image of C.",
            "Every displayed gap representative crosses all four original 35-column term blocks.",
            "The dense exact point proves the generic full-rank increment statement; the diagonal and zero-graph rows are structured degenerations, not a random scan.",
            "Special rank-drop graph terms not represented by these controls may satisfy the necessary increment equation and remain open under joint deformation.",
            "No exact five-term polynomial survivor, full Packet-B decision, lower-50, or border-rank claim is made.",
        ],
        "next_exact_gate": "Impose the special equation delta_C-delta_BC=10 or 12 on a jointly deformed fifth-term chart, beginning with rank-one graph updates aligned to the explicit sparse gap representatives.",
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
            raise SystemExit("n7 B2 join-completion gap JSON mismatch")
        print("PASS n7 B2 join-completion gap")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
