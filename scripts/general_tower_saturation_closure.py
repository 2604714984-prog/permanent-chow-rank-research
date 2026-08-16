#!/usr/bin/env python3
"""Direct saturation lower bounds from the permanent derivative tower.

If ``perm_n`` is a sum of ``q`` Chow terms, then its complete degree-``d``
derivative space is contained in the literal sum of the ``q`` one-term
derivative spaces.  Therefore every valid tower capacity ``B_(n,d)(q)`` must
already equal the full permanent dimension ``binom(n,d)^2``.

This gives a general lower bound from the first saturation index of every tower
row.  Combined with the Koszul bootstrap of the parent branch, the exact n=7
closure is

    direct tower threshold = 48,
    enhanced scalar closure = 48.

All arithmetic is deterministic and exact.
"""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path
from typing import Any

from general_derivative_tower_capacity import (
    derivative_tower_capacities,
    require,
)
from general_tower_bootstrap_fixed_point import (
    bootstrap_step,
    global_first_koszul_bound,
)


def saturation_threshold(row: list[int], ambient: int) -> int:
    """First q for which a nondecreasing capacity row reaches ambient."""

    require(row and row[0] == 0, row[:3])
    require(
        all(left <= right <= ambient for left, right in zip(row, row[1:])),
        (ambient, row),
    )
    for terms, value in enumerate(row):
        if value == ambient:
            return terms
    raise RuntimeError(("row does not saturate", ambient, row[-1]))


def tower_lower_bound(n: int, rows: dict[int, list[int]]) -> tuple[int, dict[int, int]]:
    """Return max_d min{q:B_(n,d)(q)=dim D_d(perm_n)}."""

    thresholds = {
        degree: saturation_threshold(row, comb(n, degree) ** 2)
        for degree, row in rows.items()
    }
    return max(thresholds.values()), thresholds


def enhanced_step(
    n: int,
    rows: dict[int, list[int]],
    lower_bound: int,
) -> tuple[int, int, int]:
    """Combine the direct tower threshold with the Koszul bootstrap step."""

    direct_bound, _ = tower_lower_bound(n, rows)
    koszul_bound, _, _ = bootstrap_step(n, rows, lower_bound)
    return max(lower_bound, direct_bound, koszul_bound), direct_bound, koszul_bound


def enhanced_sequence(
    n: int,
    rows: dict[int, list[int]],
    initial_bound: int,
) -> list[int]:
    sequence = [initial_bound]
    while True:
        next_bound, _, _ = enhanced_step(n, rows, sequence[-1])
        sequence.append(next_bound)
        if next_bound == sequence[-2]:
            return sequence


def build_payload() -> dict[str, Any]:
    n = 7
    maximum_terms = 48
    rows = derivative_tower_capacities(n, n - 2, maximum_terms)

    direct_bound, thresholds = tower_lower_bound(n, rows)
    require(direct_bound == 48, (direct_bound, thresholds))
    require(rows[5][46:49] == [405, 426, 441], rows[5][44:49])
    require(comb(7, 5) ** 2 == 441, comb(7, 5) ** 2)
    require(thresholds[5] == 48, thresholds)
    require(all(value <= 48 for value in thresholds.values()), thresholds)

    base = global_first_koszul_bound(n)
    require(base == 36, base)
    sequence = enhanced_sequence(n, rows, base)
    require(sequence == [36, 48, 48], sequence)

    enhanced_36 = enhanced_step(n, rows, 36)
    enhanced_48 = enhanced_step(n, rows, 48)
    require(enhanced_36 == (48, 48, 46), enhanced_36)
    require(enhanced_48 == (48, 48, 48), enhanced_48)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_TOWER_SATURATION_THEOREM",
            "EXACT_INTEGER_REPLAYED",
            "PERM7_LOWER_48",
            "N7_SCALAR_TOWER_CLOSURE_48",
        ],
        "theorem": {
            "full_coverage": (
                "If perm_n=sum_(i=1)^q T_i, then D_d(perm_n) is contained "
                "in sum_i D_d(T_i), so B_(n,d)(q)=binom(n,d)^2 for every d."
            ),
            "tower_bound": (
                "ChowRank(perm_n) is at least max_d min{q:B_(n,d)(q) "
                "equals binom(n,d)^2}."
            ),
            "enhanced_closure": (
                "Combine the direct tower threshold with the general Koszul "
                "promotion operator Phi_n."
            ),
            "boundary": (
                "A saturation fixed point closes only the current scalar "
                "derivative-tower plus first-Koszul inference system."
            ),
        },
        "n7": {
            "base_first_koszul_bound": base,
            "degree_five_ambient_dimension": 441,
            "degree_five_capacities": {
                "B_7_5_46": rows[5][46],
                "B_7_5_47": rows[5][47],
                "B_7_5_48": rows[5][48],
            },
            "degree_five_saturation_threshold": thresholds[5],
            "all_degree_thresholds_at_most_48": True,
            "direct_tower_lower_bound": direct_bound,
            "koszul_only_step_at_36": enhanced_36[2],
            "koszul_only_step_at_48": enhanced_48[2],
            "enhanced_sequence": sequence,
            "ordinary_lower_bound": 48,
        },
        "claim_boundary": (
            "The theorem is uniform in n. The finite n=7 certificate proves "
            "the stacked ordinary bound perm_7>=48 and corrects the stopping "
            "point of the named scalar tower inference from 47 to 48 by "
            "including the direct full-coverage consequence of the tower. "
            "It does not prove the exact rank of perm_7, a border-rank result, "
            "an asymptotic ceiling for every invariant, or general Glynn "
            "optimality."
        ),
    }
    return core


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
    print("GENERAL_TOWER_SATURATION_CLOSURE_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
