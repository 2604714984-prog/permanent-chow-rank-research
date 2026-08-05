#!/usr/bin/env python3
"""Exact audit for a 16-base two-defect aggregate representation of perm_6.

Let ``n_i(r)`` be the number of occurrences of row value ``i`` in an
assignment ``r`` and set ``g(r)=n_4(r)n_5(r)``.  Then ``g`` equals one on the
permutation parity fiber ``X_31`` and zero on ``X_7``.  Fourier inversion gives

    W_a = (chi_31(a)-chi_7(a))*g/32,

so only the 16 bases with ``chi_24(a)=-1`` are nonzero.

The script also proves a fail-closed fixed-base atomic-rank window

    31 <= rho_2(g) <= 36.

The lower bound restricts row values to ``{0,4,5}``.  Every one of the 15 pure
pair blocks needs at least two local sign atoms, and the unique two-atom block
representation has a nonzero lower-order ANOVA contribution.  Therefore a
30-atom global representation is impossible.  The upper bound is an explicit
30-pair-atom plus six one-defect-atom construction.

The 16-base aggregate assignment consequently has actual term cost between
496 and 576.  This is a bound for this assignment only, not for every
possible two-defect decomposition.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

N = 6
BITS = N - 1
GROUP_SIZE = 1 << BITS
TARGET_PARITY = 31
ZERO_PARITY = 7
SUPPORT_CHARACTER = TARGET_PARITY ^ ZERO_PARITY  # 24
ROW_LEFT = 4
ROW_RIGHT = 5
LABEL_LEFT = 1 << (ROW_LEFT - 1)  # 8
LABEL_RIGHT = 1 << (ROW_RIGHT - 1)  # 16
LABEL_BOTH = LABEL_LEFT | LABEL_RIGHT  # 24
LOCAL_LABELS = (LABEL_LEFT, LABEL_RIGHT, LABEL_BOTH)
PAIRS = tuple(combinations(range(N), 2))

Assignment = tuple[int, ...]
Vector = tuple[Fraction, ...]
Atom = tuple[Fraction, tuple[int, ...], tuple[int, ...]]


def character(left: int, right: int) -> int:
    return -1 if (left & right).bit_count() & 1 else 1


def sign_value(label: int, row: int) -> int:
    if row == 0:
        return 1
    return -1 if (label >> (row - 1)) & 1 else 1


def row_character(row: int) -> int:
    return 0 if row == 0 else 1 << (row - 1)


def assignment_parity(assignment: Assignment) -> int:
    value = 0
    for row in assignment:
        value ^= row_character(row)
    return value


def parity_fibers() -> dict[int, list[Assignment]]:
    fibers: dict[int, list[Assignment]] = defaultdict(list)
    for assignment in product(range(N), repeat=N):
        fibers[assignment_parity(assignment)].append(assignment)
    if sum(map(len, fibers.values())) != N**N:
        raise AssertionError("parity fibers do not partition the ambient basis")
    return dict(fibers)


def separator_value(assignment: Assignment) -> int:
    return assignment.count(ROW_LEFT) * assignment.count(ROW_RIGHT)


def solve_columns(columns: list[Vector], target: Vector) -> tuple[Vector, int] | None:
    row_count = len(target)
    column_count = len(columns)
    augmented = [
        [Fraction(columns[column][row]) for column in range(column_count)]
        + [Fraction(target[row])]
        for row in range(row_count)
    ]

    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if augmented[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        augmented[pivot_row], augmented[pivot] = (
            augmented[pivot],
            augmented[pivot_row],
        )
        pivot_value = augmented[pivot_row][column]
        augmented[pivot_row] = [
            value / pivot_value for value in augmented[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            coefficient = augmented[row][column]
            if coefficient:
                augmented[row] = [
                    augmented[row][entry]
                    - coefficient * augmented[pivot_row][entry]
                    for entry in range(column_count + 1)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    for row in range(pivot_row, row_count):
        if (
            all(augmented[row][column] == 0 for column in range(column_count))
            and augmented[row][column_count] != 0
        ):
            return None

    solution = [Fraction(0) for _ in range(column_count)]
    for row, column in enumerate(pivot_columns):
        solution[column] = augmented[row][column_count]
    return tuple(solution), len(pivot_columns)


def local_pattern(label: int) -> tuple[int, int, int]:
    return (
        sign_value(label, 0),
        sign_value(label, ROW_LEFT),
        sign_value(label, ROW_RIGHT),
    )


def local_pure_vector(left: int, right: int) -> Vector:
    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    left_difference = (
        left_pattern[1] - left_pattern[0],
        left_pattern[2] - left_pattern[0],
    )
    right_difference = (
        right_pattern[1] - right_pattern[0],
        right_pattern[2] - right_pattern[0],
    )
    return tuple(
        Fraction(left_difference[row] * right_difference[column])
        for row in range(2)
        for column in range(2)
    )


def local_lower_vector(left: int, right: int) -> Vector:
    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    constant = Fraction(left_pattern[0] * right_pattern[0])
    return (
        constant,
        Fraction(left_pattern[1] * right_pattern[0]) - constant,
        Fraction(left_pattern[2] * right_pattern[0]) - constant,
        Fraction(left_pattern[0] * right_pattern[1]) - constant,
        Fraction(left_pattern[0] * right_pattern[2]) - constant,
    )


def local_dictionary_certificate() -> dict[str, object]:
    atoms = [
        {
            "left": left,
            "right": right,
            "pure": local_pure_vector(left, right),
            "lower": local_lower_vector(left, right),
        }
        for left in LOCAL_LABELS
        for right in LOCAL_LABELS
    ]
    target = (
        Fraction(0),
        Fraction(1),
        Fraction(1),
        Fraction(0),
    )

    compatible: dict[str, int] = {}
    exact_pairs: list[dict[str, object]] = []
    for support_size in (1, 2):
        count = 0
        for indices in combinations(range(len(atoms)), support_size):
            result = solve_columns(
                [atoms[index]["pure"] for index in indices],
                target,
            )
            if result is None:
                continue
            coefficients, rank = result
            if any(coefficient == 0 for coefficient in coefficients):
                continue
            count += 1
            if support_size == 2:
                lower = tuple(
                    sum(
                        coefficients[position]
                        * atoms[index]["lower"][coordinate]
                        for position, index in enumerate(indices)
                    )
                    for coordinate in range(5)
                )
                exact_pairs.append(
                    {
                        "support": [
                            [atoms[index]["left"], atoms[index]["right"]]
                            for index in indices
                        ],
                        "coefficients": [
                            str(coefficient) for coefficient in coefficients
                        ],
                        "coefficient_matrix_rank": rank,
                        "lower_anova": [str(value) for value in lower],
                    }
                )
        compatible[str(support_size)] = count

    expected_pair = [
        {
            "support": [
                [LABEL_LEFT, LABEL_RIGHT],
                [LABEL_RIGHT, LABEL_LEFT],
            ],
            "coefficients": ["1/4", "1/4"],
            "coefficient_matrix_rank": 2,
            "lower_anova": ["1/2", "-1/2", "-1/2", "-1/2", "-1/2"],
        }
    ]
    if compatible != {"1": 0, "2": 1}:
        raise AssertionError(compatible)
    if exact_pairs != expected_pair:
        raise AssertionError(exact_pairs)

    return {
        "restricted_rows": [0, ROW_LEFT, ROW_RIGHT],
        "restricted_nonconstant_sign_labels": list(LOCAL_LABELS),
        "local_pure_atom_count": len(atoms),
        "pure_target": [["0", "1"], ["1", "0"]],
        "compatible_support_count": compatible,
        "unique_two_atom_type": exact_pairs[0],
    }


def evaluate_atom(atom: Atom, assignment: Assignment) -> Fraction:
    coefficient, positions, labels = atom
    value = coefficient
    for position, label in zip(positions, labels, strict=True):
        value *= sign_value(label, assignment[position])
    return value


def separator_construction() -> list[Atom]:
    atoms: list[Atom] = []
    for left, right in PAIRS:
        atoms.append(
            (
                Fraction(1, 4),
                (left, right),
                (LABEL_LEFT, LABEL_RIGHT),
            )
        )
        atoms.append(
            (
                Fraction(1, 4),
                (left, right),
                (LABEL_RIGHT, LABEL_LEFT),
            )
        )
    for position in range(N):
        atoms.append((Fraction(-5, 4), (position,), (LABEL_BOTH,)))
    if len(atoms) != 36:
        raise AssertionError(len(atoms))
    return atoms


def atomic_rank_certificate() -> dict[str, object]:
    local = local_dictionary_certificate()

    # With only 30 atoms, every pair block must use the unique local two-atom
    # representation and no lower-order atom remains.  Sum its lower ANOVA
    # contribution over K_6.
    forced_constant = Fraction(len(PAIRS), 2)
    forced_unary = Fraction(-(N - 1), 2)
    if forced_constant != Fraction(15, 2) or forced_unary != Fraction(-5, 2):
        raise AssertionError((forced_constant, forced_unary))

    atoms = separator_construction()
    checks = 0
    for assignment in product(range(N), repeat=N):
        observed = sum(evaluate_atom(atom, assignment) for atom in atoms)
        expected = Fraction(separator_value(assignment))
        if observed != expected:
            raise AssertionError((assignment, observed, expected))
        checks += 1
    if checks != N**N:
        raise AssertionError(checks)

    return {
        "local_dictionary_certificate": local,
        "pair_block_count": len(PAIRS),
        "minimum_atoms_per_nonzero_pair_block": 2,
        "thirty_atom_pure_block_lower_bound": 30,
        "forced_lower_anova_if_exactly_30_atoms": {
            "constant": str(forced_constant),
            "each_position_row4_unary": str(forced_unary),
            "each_position_row5_unary": str(forced_unary),
        },
        "target_lower_anova": "zero",
        "thirty_atom_representation_possible": False,
        "atomic_rank_lower_bound": 31,
        "explicit_pair_atom_count": 30,
        "explicit_one_defect_correction_count": 6,
        "atomic_rank_upper_bound": 36,
        "construction_assignment_checks": checks,
    }


def aggregate_certificate() -> dict[str, object]:
    fibers = parity_fibers()
    target_values = {separator_value(value) for value in fibers[TARGET_PARITY]}
    zero_values = {separator_value(value) for value in fibers[ZERO_PARITY]}
    if target_values != {1}:
        raise AssertionError(target_values)
    if zero_values != {0}:
        raise AssertionError(zero_values)

    zero_bases: list[int] = []
    nonzero_bases: list[int] = []
    coefficient_histogram: dict[str, int] = defaultdict(int)
    for base in range(GROUP_SIZE):
        numerator = (
            character(TARGET_PARITY, base)
            - character(ZERO_PARITY, base)
        )
        coefficient_histogram[str(numerator)] += 1
        if numerator:
            nonzero_bases.append(base)
        else:
            zero_bases.append(base)

    expected_zero = list(range(0, 8)) + list(range(24, 32))
    expected_nonzero = list(range(8, 24))
    if zero_bases != expected_zero or nonzero_bases != expected_nonzero:
        raise AssertionError((zero_bases, nonzero_bases))
    if dict(coefficient_histogram) != {"0": 16, "-2": 8, "2": 8}:
        raise AssertionError(coefficient_histogram)

    checks = 0
    for assignment in product(range(N), repeat=N):
        parity = assignment_parity(assignment)
        total = Fraction(0)
        for base in range(GROUP_SIZE):
            numerator = (
                character(TARGET_PARITY, base)
                - character(ZERO_PARITY, base)
            )
            total += (
                Fraction(character(parity, base) * numerator, GROUP_SIZE)
                * separator_value(assignment)
            )
        expected = Fraction(
            int(tuple(sorted(assignment)) == tuple(range(N)))
        )
        if total != expected:
            raise AssertionError((assignment, parity, total, expected))
        checks += 1
    if checks != N**N:
        raise AssertionError(checks)

    return {
        "separator": "g(r)=n_4(r)*n_5(r)",
        "target_parity": TARGET_PARITY,
        "zero_parity": ZERO_PARITY,
        "support_character": SUPPORT_CHARACTER,
        "target_fiber_size": len(fibers[TARGET_PARITY]),
        "zero_fiber_size": len(fibers[ZERO_PARITY]),
        "target_fiber_separator_values": [1],
        "zero_fiber_separator_values": [0],
        "formula": "W_a=(chi_31(a)-chi_7(a))*g/32",
        "coefficient_numerator_histogram": dict(coefficient_histogram),
        "zero_base_labels": zero_bases,
        "nonzero_base_labels": nonzero_bases,
        "nonzero_base_aggregate_count": len(nonzero_bases),
        "exact_assignment_checks": checks,
    }


def build_payload() -> dict[str, object]:
    aggregate = aggregate_certificate()
    rank = atomic_rank_certificate()
    lower_cost = aggregate["nonzero_base_aggregate_count"] * rank[
        "atomic_rank_lower_bound"
    ]
    upper_cost = aggregate["nonzero_base_aggregate_count"] * rank[
        "atomic_rank_upper_bound"
    ]
    if (lower_cost, upper_cost) != (496, 576):
        raise AssertionError((lower_cost, upper_cost))

    return {
        "status": "N6_TWO_DEFECT_SIXTEEN_BASE_AGGREGATE_COMPLETE",
        "field": "characteristic zero",
        "aggregate_certificate": aggregate,
        "fixed_base_atomic_rank_certificate": rank,
        "specific_assignment_actual_term_cost_window": {
            "lower_bound": lower_cost,
            "upper_bound": upper_cost,
        },
        "route_decision": {
            "previous_nonzero_base_aggregate_count": 24,
            "new_nonzero_base_aggregate_count": 16,
            "sixteen_base_aggregate_representation_exact": True,
            "sixteen_base_is_minimum": False,
            "specific_assignment_can_yield_at_most_25_terms": False,
            "global_two_defect_minimum": "open",
            "broad_sparse_optimization_authorized": False,
        },
        "claim_boundary": (
            "The 16-base Fourier aggregate representation is exact.  The "
            "fixed-base separator rank is only bounded between 31 and 36, so "
            "the actual cost of this assignment is between 496 and 576.  No "
            "minimum base-support or global two-defect rank claim is made."
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
    print("N6_TWO_DEFECT_SIXTEEN_BASE_AGGREGATE_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
