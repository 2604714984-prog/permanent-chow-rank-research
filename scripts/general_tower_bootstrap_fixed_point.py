#!/usr/bin/env python3
"""Bootstrap permanent Chow-rank bounds from derivative-tower capacities.

The derivative-tower theorem bounds, for every n, d and q,

    dim(D_d(perm_n) intersect sum_i D_d(T_i)) <= B_(n,d)(q).

The complementary-intersection Koszul residual inequality converts a valid
rank lower bound L into a possibly larger valid lower bound Phi_n(L).  This
module defines the operator, iterates it, and performs the exact n=7 closure:

    36 -> 46 -> 47 -> 47.

The fixed point 47 is a ceiling only for this named scalar-tower/Koszul
bootstrap.  It is not an upper bound on the actual Chow rank or on other
methods.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

from general_derivative_tower_capacity import (
    derivative_tower_capacities,
    require,
)
from general_exact_product_shadow import first_koszul_data


EXPECTED_CORE_SHA256 = (
    "2f11127a199b52e147090557d2a767c950ad97d4dc478e9f05833fa6580f6872"
)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def positive_ceiling(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return 0 if numerator <= 0 else -(-numerator // denominator)


def global_first_koszul_bound(n: int) -> int:
    require(n >= 4, n)
    return max(
        first_koszul_data(n, output_degree)[2]
        for output_degree in range(2, n - 1)
    )


def bootstrap_scan(
    n: int,
    capacities: dict[int, list[int]],
    lower_bound: int,
) -> list[list[int]]:
    """Enumerate every legal Koszul residual certificate at input L.

    A row is

        [L, m, r, q, cap, target, one_term, numerator, residual, total].

    Here m is the Koszul output degree and r=n-m is the complementary
    derivative degree controlled by the tower.
    """

    require(lower_bound >= 1, lower_bound)
    rows: list[list[int]] = []
    for output_degree in range(2, n - 1):
        complementary_degree = n - output_degree
        require(complementary_degree in capacities, complementary_degree)
        require(
            len(capacities[complementary_degree]) > lower_bound,
            (complementary_degree, lower_bound),
        )
        target, one_term, _ = first_koszul_data(n, output_degree)
        for fixed_terms in range(1, lower_bound + 1):
            intersection_cap = capacities[complementary_degree][fixed_terms]
            numerator = target - n * n * intersection_cap
            residual_terms = positive_ceiling(numerator, one_term)
            rows.append(
                [
                    lower_bound,
                    output_degree,
                    complementary_degree,
                    fixed_terms,
                    intersection_cap,
                    target,
                    one_term,
                    numerator,
                    residual_terms,
                    fixed_terms + residual_terms,
                ]
            )
    return rows


def bootstrap_step(
    n: int,
    capacities: dict[int, list[int]],
    lower_bound: int,
) -> tuple[int, list[list[int]], list[list[int]]]:
    scan = bootstrap_scan(n, capacities, lower_bound)
    output_bound = max([lower_bound, *(row[-1] for row in scan)])
    maximizers = [row for row in scan if row[-1] == output_bound]
    return output_bound, maximizers, scan


def bootstrap_sequence(
    n: int,
    capacities: dict[int, list[int]],
    initial_bound: int,
) -> list[int]:
    sequence = [initial_bound]
    while True:
        next_bound, _, _ = bootstrap_step(n, capacities, sequence[-1])
        sequence.append(next_bound)
        if next_bound == sequence[-2]:
            return sequence


def build_payload() -> dict[str, Any]:
    n = 7
    maximum_terms = 47
    capacities = derivative_tower_capacities(n, n - 2, maximum_terms)

    base_bound = global_first_koszul_bound(n)
    require(base_bound == 36, base_bound)
    sequence = bootstrap_sequence(n, capacities, base_bound)
    require(sequence == [36, 46, 47, 47], sequence)

    bound_36, witnesses_36, scan_36 = bootstrap_step(n, capacities, 36)
    bound_46, witnesses_46, scan_46 = bootstrap_step(n, capacities, 46)
    bound_47, witnesses_47, scan_47 = bootstrap_step(n, capacities, 47)
    require((bound_36, bound_46, bound_47) == (46, 47, 47), (
        bound_36,
        bound_46,
        bound_47,
    ))

    require(capacities[4][20] == 341, capacities[4][20])
    require(capacities[5][36] == 233, capacities[5][36])
    require(capacities[5][39] == 267, capacities[5][39])
    require(capacities[5][46] == 405, capacities[5][46])
    require(capacities[5][47] == 426, capacities[5][47])

    first_witness = [3, 4, 20, 341, 58_800, 1_680, 42_091, 26, 46]
    second_witness = [2, 5, 46, 405, 20_384, 994, 539, 1, 47]
    require(
        [
            witnesses_36[1],
            witnesses_46[-1],
        ]
        == [
            [36, *first_witness],
            [46, *second_witness],
        ],
        (witnesses_36, witnesses_46),
    )

    core: dict[str, Any] = {
        "status": [
            "GENERAL_TOWER_BOOTSTRAP_PROOF_DRAFT",
            "EXACT_INTEGER_REPLAYED",
            "PERM7_LOWER_47",
            "N7_SCALAR_TOWER_FIXED_POINT_47",
        ],
        "theorem": {
            "promotion": (
                "If ChowRank(perm_n)>=L, then ChowRank(perm_n)>=Phi_n(L)."
            ),
            "operator": (
                "Phi_n(L)=max(L, max_(2<=m<=n-2,1<=q<=L) "
                "q+ceil_pos((A_(n,m)-n^2*B_(n,n-m)(q))/K_(n,m)))."
            ),
            "iteration": (
                "Every iterate from a valid lower bound is valid and the "
                "integer sequence stabilizes below the actual Chow rank."
            ),
            "fixed_point_boundary": (
                "A fixed point closes this derivative-tower/Koszul bootstrap "
                "only; it is not an upper bound on Chow rank or on other "
                "methods."
            ),
        },
        "n7": {
            "base_first_koszul_bound": base_bound,
            "bootstrap_sequence": sequence,
            "capacity_row_sha256": {
                str(degree): canonical_sha256(capacities[degree])
                for degree in sorted(capacities)
            },
            "key_capacities": {
                "B_7_4_20": capacities[4][20],
                "B_7_5_36": capacities[5][36],
                "B_7_5_39": capacities[5][39],
                "B_7_5_46": capacities[5][46],
                "B_7_5_47": capacities[5][47],
            },
            "first_promotion": {
                "input_bound": 36,
                "output_bound": bound_36,
                "canonical_witness": first_witness,
                "maximizer_count": len(witnesses_36),
                "scan_sha256": canonical_sha256(scan_36),
            },
            "second_promotion": {
                "input_bound": 46,
                "output_bound": bound_46,
                "canonical_witness": second_witness,
                "maximizer_count": len(witnesses_46),
                "scan_sha256": canonical_sha256(scan_46),
            },
            "fixed_point": {
                "input_bound": 47,
                "output_bound": bound_47,
                "maximizer_count": len(witnesses_47),
                "scan_sha256": canonical_sha256(scan_47),
            },
        },
        "claim_boundary": (
            "The theorem is uniform in n and composes the already proved "
            "derivative-tower capacity with the complementary-intersection "
            "Koszul residual inequality. The finite certificate proves the "
            "stacked ordinary bound perm_7>=47 and shows that the same scalar "
            "tower/Koszul bootstrap stabilizes at 47 for n=7. It does not "
            "prove the exact rank of perm_7, a border-rank result, an "
            "asymptotic ceiling for every scalar invariant, or general Glynn "
            "optimality."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


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
    print("GENERAL_TOWER_BOOTSTRAP_FIXED_POINT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
