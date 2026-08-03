#!/usr/bin/env python3
"""Independent exact audit of the computational claims in the perm4 Chow-rank proof.

This script is self-contained and does not import any author/project code. It rebuilds
all relevant bases and Koszul matrices directly from the definitions in the PDF.
It uses only exact integer/rational arithmetic and finite-field rank-profile selection;
no floating point and no random sampling are used.

Tested with Python 3.11+ and SymPy 1.14.
"""

from __future__ import annotations

import itertools
import sys

import sympy
from heapq import heappop, heappush
from typing import Dict, Iterable, List, Sequence, Tuple

from sympy.polys.domains import GF, ZZ
from sympy.polys.matrices import DomainMatrix

N = 16
TARGET_DIM = N * (N * (N - 1) // 2)  # dim(V tensor wedge^2 V) = 1920
PRIME = 1_000_003

SparseColumn = Dict[int, int]

SYM_PAIRS: List[Tuple[int, int]] = [
    (a, b) for a in range(N) for b in range(a, N)
]
SYM_INDEX = {pair: idx for idx, pair in enumerate(SYM_PAIRS)}
WEDGE_PAIRS: List[Tuple[int, int]] = [
    (a, b) for a in range(N) for b in range(a + 1, N)
]
WEDGE_INDEX = {pair: idx for idx, pair in enumerate(WEDGE_PAIRS)}


def variable_index(row: int, col: int) -> int:
    return 4 * row + col


def _add_wedge(
    column: SparseColumn,
    first_tensor_factor: int,
    left: int,
    right: int,
    coefficient: int,
) -> None:
    if left == right:
        return
    if left < right:
        wedge_position = WEDGE_INDEX[(left, right)]
        sign = 1
    else:
        wedge_position = WEDGE_INDEX[(right, left)]
        sign = -1
    row = first_tensor_factor * len(WEDGE_PAIRS) + wedge_position
    column[row] = column.get(row, 0) + sign * coefficient
    if column[row] == 0:
        del column[row]


def delta_monomial(a: int, b: int, w: int) -> SparseColumn:
    """Column of delta((x_a x_b) tensor x_w) in the stated lexicographic basis."""
    result: SparseColumn = {}
    _add_wedge(result, b, a, w, 1)
    _add_wedge(result, a, b, w, 1)
    return result


def columns_to_domain_matrix(
    columns: Sequence[SparseColumn], row_count: int, domain
) -> DomainMatrix:
    rows: Dict[int, Dict[int, int]] = {}
    for column_index, column in enumerate(columns):
        for row_index, value in column.items():
            rows.setdefault(row_index, {})[column_index] = value
    return DomainMatrix(rows, (row_count, len(columns)), domain)


def select_submatrix(
    columns: Sequence[SparseColumn],
    selected_columns: Sequence[int],
    selected_rows: Sequence[int],
) -> DomainMatrix:
    rows: Dict[int, Dict[int, int]] = {}
    for new_row, old_row in enumerate(selected_rows):
        row: Dict[int, int] = {}
        for new_col, old_col in enumerate(selected_columns):
            value = columns[old_col].get(old_row, 0)
            if value:
                row[new_col] = value
        if row:
            rows[new_row] = row
    return DomainMatrix(rows, (len(selected_rows), len(selected_columns)), ZZ)


def independent_columns_and_rows(
    columns: Sequence[SparseColumn], row_count: int, prime: int = PRIME
) -> Tuple[List[int], List[int]]:
    matrix = columns_to_domain_matrix(columns, row_count, GF(prime))
    _, column_pivots = matrix.rref()
    selected_columns = list(column_pivots)

    independent_columns: List[SparseColumn] = [columns[j] for j in selected_columns]
    independent_matrix = columns_to_domain_matrix(
        independent_columns, row_count, GF(prime)
    )
    _, row_pivots = independent_matrix.transpose().rref()
    return selected_columns, list(row_pivots)


def build_perm4_E_basis() -> List[List[Tuple[int, int, int]]]:
    basis: List[List[Tuple[int, int, int]]] = []
    for i, j in itertools.combinations(range(4), 2):
        for a, b in itertools.combinations(range(4), 2):
            basis.append(
                [
                    (variable_index(i, a), variable_index(j, b), 1),
                    (variable_index(i, b), variable_index(j, a), 1),
                ]
            )
    assert len(basis) == 36
    return basis


def delta_columns_from_quadratic_basis(
    basis: Sequence[Sequence[Tuple[int, int, int]]]
) -> List[SparseColumn]:
    columns: List[SparseColumn] = []
    for quadratic in basis:
        for w in range(N):
            column: SparseColumn = {}
            for a, b, coefficient in quadratic:
                for row, value in delta_monomial(a, b, w).items():
                    column[row] = column.get(row, 0) + coefficient * value
                    if column[row] == 0:
                        del column[row]
            columns.append(column)
    return columns


def matrix_from_rows_and_columns(
    base_columns: Sequence[SparseColumn],
    base_selection: Sequence[int],
    added_columns: Sequence[SparseColumn],
    selected_rows: Sequence[int],
) -> DomainMatrix:
    rows: Dict[int, Dict[int, int]] = {}
    base_width = len(base_selection)
    for new_row, old_row in enumerate(selected_rows):
        row: Dict[int, int] = {}
        for new_col, old_col in enumerate(base_selection):
            value = base_columns[old_col].get(old_row, 0)
            if value:
                row[new_col] = value
        for added_index, column in enumerate(added_columns):
            value = column.get(old_row, 0)
            if value:
                row[base_width + added_index] = value
        if row:
            rows[new_row] = row
    return DomainMatrix(
        rows,
        (len(selected_rows), base_width + len(added_columns)),
        ZZ,
    )


def force_base_rows_then_select_extras(
    combined: DomainMatrix, base_rows: Sequence[int]
) -> List[int]:
    base_set = set(base_rows)
    row_order = list(base_rows) + [
        row for row in range(combined.shape[0]) if row not in base_set
    ]
    original_to_ordered = {original: ordered for ordered, original in enumerate(row_order)}

    transpose_rows: Dict[int, Dict[int, int]] = {}
    sparse_rep = combined.to_sparse().rep
    for original_row, row_entries in sparse_rep.items():
        ordered_column = original_to_ordered[original_row]
        for original_col, value in row_entries.items():
            transpose_rows.setdefault(original_col, {})[ordered_column] = int(value)

    transposed = DomainMatrix(
        transpose_rows,
        (combined.shape[1], combined.shape[0]),
        combined.domain,
    )
    _, row_pivots_in_order = transposed.rref()
    pivots = list(row_pivots_in_order)
    assert pivots[: len(base_rows)] == list(range(len(base_rows)))
    return [row_order[position] for position in pivots[len(base_rows) :]]


def build_block_from_rows(
    base_columns: Sequence[SparseColumn],
    base_selection: Sequence[int],
    selected_rows: Sequence[int],
) -> DomainMatrix:
    return select_submatrix(base_columns, base_selection, selected_rows)


def q_matrix(
    representatives: Sequence[Tuple[int, int]],
    selected_rows: Sequence[int],
    v_basis_index: int,
) -> DomainMatrix:
    rows: Dict[int, Dict[int, int]] = {}
    for new_row, old_row in enumerate(selected_rows):
        row: Dict[int, int] = {}
        for col, (a, b) in enumerate(representatives):
            value = delta_monomial(a, b, v_basis_index).get(old_row, 0)
            if value:
                row[col] = value
        if row:
            rows[new_row] = row
    return DomainMatrix(rows, (len(selected_rows), len(representatives)), ZZ)


def exact_nonzero_pattern(matrix: DomainMatrix) -> Iterable[Tuple[int, int, int]]:
    for row, entries in matrix.to_sparse().rep.items():
        for col, value in entries.items():
            value_int = int(value)
            if value_int:
                yield row, col, value_int


def main() -> None:
    # 1. rank delta(E tensor V) = 560, with an exact unimodular minor.
    E_basis = build_perm4_E_basis()
    perm_columns = delta_columns_from_quadratic_basis(E_basis)
    perm_matrix_mod = columns_to_domain_matrix(
        perm_columns, TARGET_DIM, GF(PRIME)
    )
    perm_rank = perm_matrix_mod.rank()
    assert perm_rank == 560
    perm_selected_columns, perm_selected_rows = independent_columns_and_rows(
        perm_columns, TARGET_DIM
    )
    perm_minor = select_submatrix(
        perm_columns, perm_selected_columns, perm_selected_rows
    )
    perm_minor_det = int(perm_minor.det())
    assert abs(perm_minor_det) == 1

    # 2. rank for x0*x1*x2*x3 equals 92, again with an exact unimodular minor.
    chow_basis = [[(a, b, 1)] for a, b in itertools.combinations(range(4), 2)]
    chow_columns = delta_columns_from_quadratic_basis(chow_basis)
    chow_matrix_mod = columns_to_domain_matrix(
        chow_columns, TARGET_DIM, GF(PRIME)
    )
    chow_rank = chow_matrix_mod.rank()
    assert chow_rank == 92
    chow_selected_columns, chow_selected_rows = independent_columns_and_rows(
        chow_columns, TARGET_DIM
    )
    chow_minor = select_submatrix(
        chow_columns, chow_selected_columns, chow_selected_rows
    )
    chow_minor_det = int(chow_minor.det())
    assert abs(chow_minor_det) == 1

    # 3. Build a deterministic monomial complement to E in Sym^2 V.
    E_coefficient_rows: Dict[int, Dict[int, int]] = {}
    for E_col, quadratic in enumerate(E_basis):
        for a, b, coefficient in quadratic:
            monomial_row = SYM_INDEX[tuple(sorted((a, b)))]
            E_coefficient_rows.setdefault(monomial_row, {})[E_col] = coefficient
    E_coefficient_matrix = DomainMatrix(
        E_coefficient_rows, (len(SYM_PAIRS), len(E_basis)), GF(PRIME)
    )
    _, E_pivot_monomials = E_coefficient_matrix.transpose().rref()
    E_pivot_set = set(E_pivot_monomials)
    quotient_representatives = [
        pair for index, pair in enumerate(SYM_PAIRS) if index not in E_pivot_set
    ]
    assert len(quotient_representatives) == 100
    assert (0, 0) in quotient_representatives
    chart_representatives = [
        pair for pair in quotient_representatives if pair != (0, 0)
    ]
    assert len(chart_representatives) == 99

    # 4. At v=e_00, select the 99 additional rows and reconstruct the exact chart.
    chart_e0_columns = [
        delta_monomial(a, b, 0) for a, b in chart_representatives
    ]
    combined_rows: Dict[int, Dict[int, int]] = {}
    for new_col, old_col in enumerate(perm_selected_columns):
        for row, value in perm_columns[old_col].items():
            combined_rows.setdefault(row, {})[new_col] = value
    for chart_col, column in enumerate(chart_e0_columns):
        for row, value in column.items():
            combined_rows.setdefault(row, {})[560 + chart_col] = value
    combined_mod = DomainMatrix(combined_rows, (TARGET_DIM, 659), GF(PRIME))
    assert combined_mod.rank() == 659

    extra_rows = force_base_rows_then_select_extras(
        combined_mod, perm_selected_rows
    )
    assert len(extra_rows) == 99

    A0 = build_block_from_rows(
        perm_columns, perm_selected_columns, perm_selected_rows
    )
    A1 = build_block_from_rows(
        perm_columns, perm_selected_columns, extra_rows
    )
    det_A0 = int(A0.det())
    assert abs(det_A0) == 1
    A0_inverse, A0_denominator = A0.inv_den()
    assert int(A0_denominator) == 1
    projection = A1.matmul(A0_inverse)

    S_matrices: List[DomainMatrix] = []
    for k in range(N):
        Q0 = q_matrix(chart_representatives, perm_selected_rows, k)
        Q1 = q_matrix(chart_representatives, extra_rows, k)
        S_matrices.append(Q1.sub(projection.matmul(Q0)))

    S0 = S_matrices[0]
    det_S0 = int(S0.det())
    assert det_S0 == -32768

    S0_adjugate, S0_denominator = S0.inv_den()
    denominator = int(S0_denominator)
    assert denominator != 0

    union_edges: set[Tuple[int, int]] = set()
    diagonal_entries: List[Tuple[int, int, int]] = []
    for k in range(1, N):
        numerator = S0_adjugate.matmul(S_matrices[k])
        for row, col, value in exact_nonzero_pattern(numerator):
            union_edges.add((row, col))
            if row == col:
                diagonal_entries.append((k, row, value))

    assert not diagonal_entries
    assert len(union_edges) == 156

    adjacency = [set() for _ in range(99)]
    indegree = [0] * 99
    for source, target in union_edges:
        if target not in adjacency[source]:
            adjacency[source].add(target)
            indegree[target] += 1

    queue: List[int] = []
    for vertex, degree in enumerate(indegree):
        if degree == 0:
            heappush(queue, vertex)

    topological_order: List[int] = []
    while queue:
        source = heappop(queue)
        topological_order.append(source)
        for target in sorted(adjacency[source]):
            indegree[target] -= 1
            if indegree[target] == 0:
                heappush(queue, target)

    assert len(topological_order) == 99
    order_position = {vertex: position for position, vertex in enumerate(topological_order)}
    assert all(
        order_position[source] < order_position[target]
        for source, target in union_edges
    )

    print(f"python_version={sys.version.split()[0]}")
    print(f"sympy_version={sympy.__version__}")
    print(f"perm4_delta_rank_mod_{PRIME}={perm_rank}")
    print(f"perm4_exact_560_minor_det={perm_minor_det}")
    print(f"chow_delta_rank_mod_{PRIME}={chow_rank}")
    print(f"chow_exact_92_minor_det={chow_minor_det}")
    print(f"chart_combined_rank_at_e00_mod_{PRIME}=659")
    print(f"chart_det_A0={det_A0}")
    print(f"chart_det_S0={det_S0}")
    print(f"chart_normalized_common_denominator={denominator}")
    print(f"chart_normalized_union_nonzero_positions={len(union_edges)}")
    print("chart_normalized_diagonal_zero=True")
    print("chart_normalized_union_DAG=True")
    print("determinant_identity=det(M(v))=det(A0)*(-32768)*v00^99")
    print("INDEPENDENT_PERM4_CHOW_RANK_CERTIFICATE_AUDIT_PASS")


if __name__ == "__main__":
    main()
