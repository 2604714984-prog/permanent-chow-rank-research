#!/usr/bin/env python3
"""Exact capacity inventory for candidate perm_7 lower-bound routes.

This script performs integer arithmetic only.  It records route ceilings and
does not claim a new Chow-rank lower bound.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_multidegree_capacity_inventory.json"


def encode(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}" if value.denominator != 1 else str(value.numerator)


def first_koszul_row(n: int, m: int) -> dict[str, object]:
    derivative_rank = comb(n, m)
    next_rank = comb(n, m + 1)
    permanent_rank = n * n * derivative_rank**2 - next_rank**2
    one_term_cap = n * n * derivative_rank - next_rank
    ratio = Fraction(permanent_rank, one_term_cap)
    return {
        "output_degree": m,
        "permanent_rank": permanent_rank,
        "one_term_cap": one_term_cap,
        "ratio": encode(ratio),
        "integer_lower_bound": ceil(ratio),
    }


def sparse_rank_mod(columns: list[dict[int, int]], prime: int = 1_000_003) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for raw in columns:
        column = {row: value % prime for row, value in raw.items() if value % prime}
        while column:
            pivot = min(column)
            old = pivots.get(pivot)
            if old is None:
                inverse = pow(column[pivot], prime - 2, prime)
                pivots[pivot] = {
                    row: value * inverse % prime for row, value in column.items()
                }
                break
            factor = column[pivot]
            for row, value in old.items():
                updated = (column.get(row, 0) - factor * value) % prime
                if updated:
                    column[row] = updated
                else:
                    column.pop(row, None)
    return len(pivots)


def internal_koszul_rank(n: int, m: int, p: int) -> int:
    """Modular rank on the active variables of one squarefree Chow term."""
    degree_basis = tuple(combinations(range(n), m))
    wedge_basis = tuple(combinations(range(n), p))
    target_degree = {
        value: index for index, value in enumerate(combinations(range(n), m - 1))
    }
    target_wedge = {
        value: index for index, value in enumerate(combinations(range(n), p + 1))
    }
    wedge_count = len(target_wedge)
    columns: list[dict[int, int]] = []
    for degree in degree_basis:
        for wedge in wedge_basis:
            entries: dict[int, int] = {}
            for variable in degree:
                if variable in wedge:
                    continue
                output_degree = tuple(item for item in degree if item != variable)
                output_wedge = tuple(sorted((*wedge, variable)))
                insertion = output_wedge.index(variable)
                row = target_degree[output_degree] * wedge_count + target_wedge[output_wedge]
                entries[row] = -1 if insertion % 2 else 1
            columns.append(entries)
    return sparse_rank_mod(columns)


def higher_wedge_capacity(n: int) -> dict[str, object]:
    inactive = n * n - n
    internal = {
        m: [internal_koszul_rank(n, m, p) for p in range(n + 1)]
        for m in range(1, n + 1)
    }
    best: tuple[Fraction, dict[str, object]] | None = None
    checked = 0
    for m in range(1, n + 1):
        for p in range(n * n):
            checked += 1
            permanent_upper = min(
                comb(n, m) ** 2 * comb(n * n, p),
                comb(n, m - 1) ** 2 * comb(n * n, p + 1),
            )
            one_term_lower = sum(
                comb(inactive, p - q) * rank
                for q, rank in enumerate(internal[m])
                if 0 <= p - q <= inactive
            )
            if not one_term_lower:
                continue
            ratio = Fraction(permanent_upper, one_term_lower)
            witness = {
                "output_degree": m,
                "wedge_degree": p,
                "permanent_rank_dimension_upper_bound": permanent_upper,
                "independent_term_modular_rank_lower_bound": one_term_lower,
                "ratio_upper_bound": encode(ratio),
                "integer_lower_bound_ceiling": ceil(ratio),
            }
            if best is None or ratio > best[0]:
                best = (ratio, witness)
    assert best is not None
    return {
        "checked_output_degrees": [1, n],
        "checked_wedge_degrees": [0, n * n - 1],
        "checked_pair_count": checked,
        "active_internal_modular_rank_table": [internal[m] for m in range(1, n + 1)],
        "inactive_variable_count": inactive,
        "one_term_convolution": "sum_q C(42,p-q)*internal_rank[m,q]",
        "maximum": best[1],
    }


def build_payload() -> dict[str, object]:
    n = 7
    derivative_tower = [comb(n, m) ** 2 for m in range(n + 1)]
    chow_term_tower = [comb(n, m) for m in range(n + 1)]
    raw_ratios = [Fraction(a, b) for a, b in zip(derivative_tower, chow_term_tower)]
    koszul_rows = [first_koszul_row(n, m) for m in range(2, n)]

    apolar_ratio = Fraction(comb(2 * n, n), 2**n)
    best_raw_ratio = max(raw_ratios)
    best_koszul_integer = max(int(row["integer_lower_bound"]) for row in koszul_rows)
    higher_wedge = higher_wedge_capacity(n)

    multishadow = json.loads((ROOT / "data" / "multishadow_bounds.json").read_text(encoding="utf-8"))
    n7_multishadow = next(row for row in multishadow["certificates"] if row["n"] == n)
    assert n7_multishadow["lower_bound"] == 41

    rectangular = json.loads(
        (ROOT / "data" / "n7_rectangular_half_defect_reduction.json").read_text(encoding="utf-8")
    )
    assert rectangular["full_quotient_symbol_capacity"] == 70
    assert rectangular["full_quotient_required_by_linear_slope"] == "145"

    assert derivative_tower == [1, 49, 441, 1225, 1225, 441, 49, 1]
    assert chow_term_tower == [1, 7, 21, 35, 35, 21, 7, 1]
    assert encode(apolar_ratio) == "429/16"
    assert ceil(apolar_ratio) == 27
    assert best_raw_ratio == 35
    assert best_koszul_integer == 36
    assert higher_wedge["checked_pair_count"] == 343
    assert higher_wedge["active_internal_modular_rank_table"] == [
        [7, 21, 35, 35, 21, 7, 1, 0],
        [21, 112, 210, 224, 140, 48, 7, 0],
        [35, 210, 511, 595, 393, 140, 21, 0],
        [35, 224, 595, 832, 595, 224, 35, 0],
        [21, 140, 393, 595, 511, 210, 35, 0],
        [7, 48, 140, 224, 210, 112, 21, 0],
        [1, 7, 21, 35, 35, 21, 7, 0],
    ]
    assert higher_wedge["maximum"] == {
        "output_degree": 4,
        "wedge_degree": 24,
        "permanent_rank_dimension_upper_bound": 77_426_496_443_123_100,
        "independent_term_modular_rank_lower_bound": 1_284_156_702_075_780,
        "ratio_upper_bound": "24262105/402399",
        "integer_lower_bound_ceiling": 61,
    }

    return {
        "status": "N7_ROUTE_CAPACITY_INVENTORY",
        "field": "characteristic zero",
        "n": n,
        "glynn_upper_bound": 64,
        "derivative_tower": derivative_tower,
        "independent_chow_term_tower": chow_term_tower,
        "raw_derivative_component_ratio_ceiling": encode(best_raw_ratio),
        "full_apolar_length": {
            "permanent": comb(2 * n, n),
            "one_term": 2**n,
            "ratio": encode(apolar_ratio),
            "integer_lower_bound": ceil(apolar_ratio),
        },
        "first_koszul": {
            "rows": koszul_rows,
            "best_integer_lower_bound": best_koszul_integer,
        },
        "all_standard_higher_wedge_koszul_capacity": higher_wedge,
        "imported_best_current_ordinary_lower_bound": {
            "value": n7_multishadow["lower_bound"],
            "source": "multishadow_bounds.json",
            "method": "multidimensional-shadow",
        },
        "single_middle_layer_barrier": {
            "required_full_quotient_rank": int(rectangular["full_quotient_required_by_linear_slope"]),
            "available_full_quotient_capacity": rectangular["full_quotient_symbol_capacity"],
            "gap": int(rectangular["full_quotient_required_by_linear_slope"])
            - rectangular["full_quotient_symbol_capacity"],
        },
        "direct_sum_ceiling": {
            "statement": (
                "A nonnegative direct sum of rank inequalities has ratio at most "
                "the maximum component ratio."
            ),
            "raw_derivative_components": 35,
            "first_koszul_components": 36,
            "all_standard_higher_wedge_components": 61,
            "reaches_64": False,
        },
        "route_decision": {
            "discard": [
                "raw derivative-layer direct sums",
                "full apolar-length dimension count",
                "nonnegative direct sums of first-Koszul inequalities",
                "nonnegative direct sums of standard higher-wedge Koszul inequalities",
                "the single-middle-layer rectangular half-defect route",
            ],
            "retain": (
                "a genuinely coupled multi-degree derivative module whose one-term cap "
                "is smaller than the sum of its separate degreewise caps"
            ),
        },
        "claim_boundary": [
            "This file proves route-capacity ceilings, not ChowRank(perm_7)=64.",
            "The value 41 is imported from the existing exact multishadow certificate.",
            "No statement about border Chow rank is added here.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise SystemExit("frozen payload mismatch")
        print("PASS: n7 multi-degree capacity inventory matches")
        return 0
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
