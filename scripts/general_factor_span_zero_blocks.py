#!/usr/bin/env python3
"""Exact integer audit for factor-span zero blocks.

The mathematical input is the permanent derivative-shadow theorem already
proved in ``docs/general_n_koszul_bounds.md``:

    0 != f in D_m(perm_n)  =>  dim partial^(m-1) f >= m^2.

This file replays the finite consequences of combining that lower bound with
the elementary containment ``partial^(m-1) Sym^m(L) subset L``.  It uses only
the Python standard library and exact integers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path


def require(condition: bool, message: object) -> None:
    """Fail closed even under ``python -O``."""

    if not condition:
        raise RuntimeError(message)


def central_output_degree(n: int) -> int:
    require(n >= 2, n)
    return (n + 1) // 2


def permanent_linear_shadow_floor(output_degree: int) -> int:
    """The order-(m-1) shadow floor for nonzero D_m(perm_n) vectors."""

    require(output_degree >= 1, output_degree)
    return output_degree * output_degree


def factor_span_zero(output_degree: int, factor_span_dimension: int) -> bool:
    """Whether the strict factor-span zero-intersection criterion applies."""

    require(output_degree >= 1, output_degree)
    require(factor_span_dimension >= 0, factor_span_dimension)
    return factor_span_dimension < permanent_linear_shadow_floor(output_degree)


def pair_union_dimension(n: int, factor_span_intersection: int) -> int:
    require(n >= 1, n)
    require(0 <= factor_span_intersection <= n, factor_span_intersection)
    return 2 * n - factor_span_intersection


def pair_quotient_exact(
    n: int,
    output_degree: int,
    factor_span_intersection: int,
) -> bool:
    """Exactness of the permanent quotient on the literal pair sum."""

    return factor_span_zero(
        output_degree,
        pair_union_dimension(n, factor_span_intersection),
    )


def independent_frame_literal_cap(
    output_degree: int,
    factor_span_intersection: int,
) -> int:
    """Squarefree literal-overlap cap for independent factor frames."""

    require(output_degree >= 0, output_degree)
    require(factor_span_intersection >= 0, factor_span_intersection)
    return (
        comb(factor_span_intersection, output_degree)
        if factor_span_intersection >= output_degree
        else 0
    )


def projected_capacity(
    n: int,
    output_degree: int,
    total_term_count: int,
    removed_block_size: int,
    removed_block_span_dimension: int,
) -> int:
    """Literal derivative capacity after removing a certified zero block."""

    require(
        0 <= removed_block_size <= total_term_count,
        (total_term_count, removed_block_size),
    )
    require(
        factor_span_zero(output_degree, removed_block_span_dimension),
        ("block is not certified zero", output_degree, removed_block_span_dimension),
    )
    return (total_term_count - removed_block_size) * comb(n, output_degree)


def central_table() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(3, 21):
        m = central_output_degree(n)
        rows.append(
            {
                "n": n,
                "central_output_degree": m,
                "m_squared": m * m,
                "same_span_dimension_cap": n,
                "same_span_cluster_zero": factor_span_zero(m, n),
                "two_full_span_union_cap": 2 * n,
                "every_pair_quotient_exact": factor_span_zero(m, 2 * n),
            }
        )
    return rows


def pair_table(n: int, output_degree: int) -> list[dict[str, object]]:
    return [
        {
            "factor_span_intersection": k,
            "factor_span_union": pair_union_dimension(n, k),
            "quotient_exact": pair_quotient_exact(n, output_degree, k),
            "literal_overlap_cap": independent_frame_literal_cap(output_degree, k),
        }
        for k in range(n + 1)
    ]


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_payload() -> dict[str, object]:
    central = central_table()

    expected_exact_pair_n = [7] + list(range(9, 21))
    observed_exact_pair_n = [
        row["n"] for row in central if row["every_pair_quotient_exact"]
    ]
    require(observed_exact_pair_n == expected_exact_pair_n, observed_exact_pair_n)

    same_span_zero_n = [
        row["n"] for row in central if row["same_span_cluster_zero"]
    ]
    require(same_span_zero_n == [3] + list(range(5, 21)), same_span_zero_n)

    full_pair_tables = {
        "n5_m3": pair_table(5, 3),
        "n6_m3": pair_table(6, 3),
        "n7_m4": pair_table(7, 4),
        "n8_m4": pair_table(8, 4),
        "n9_m5": pair_table(9, 5),
        "n10_m5": pair_table(10, 5),
    }

    require(
        [row["quotient_exact"] for row in full_pair_tables["n8_m4"]]
        == [False] + [True] * 8,
        full_pair_tables["n8_m4"],
    )
    require(
        [row["quotient_exact"] for row in full_pair_tables["n6_m3"]]
        == [False] * 4 + [True] * 3,
        full_pair_tables["n6_m3"],
    )
    require(
        all(row["quotient_exact"] for row in full_pair_tables["n7_m4"]),
        full_pair_tables["n7_m4"],
    )
    require(
        [row["quotient_exact"] for row in full_pair_tables["n5_m3"]]
        == [False, False] + [True] * 4,
        full_pair_tables["n5_m3"],
    )

    pair_summaries = []
    for label, rows in full_pair_tables.items():
        first_exact = next(
            row["factor_span_intersection"]
            for row in rows
            if row["quotient_exact"]
        )
        pair_summaries.append(
            {
                "case": label,
                "first_exact_factor_span_intersection": first_exact,
                "exact_from_intersection_through_n": True,
                "literal_cap_at_first_exact": rows[first_exact][
                    "literal_overlap_cap"
                ],
            }
        )

    projection_examples = [
        {
            "n": 8,
            "output_degree": 4,
            "total_term_count": 20,
            "removed_block_size": 5,
            "removed_block_span_dimension": 8,
            "projected_literal_capacity": projected_capacity(8, 4, 20, 5, 8),
        },
        {
            "n": 9,
            "output_degree": 5,
            "total_term_count": 30,
            "removed_block_size": 12,
            "removed_block_span_dimension": 20,
            "projected_literal_capacity": projected_capacity(9, 5, 30, 12, 20),
        },
    ]
    require(
        projection_examples[0]["projected_literal_capacity"] == 1050,
        projection_examples,
    )
    require(
        projection_examples[1]["projected_literal_capacity"] == 2268,
        projection_examples,
    )

    core = {
        "status": [
            "GENERAL_FACTOR_SPAN_ZERO_BLOCK_PROOF_DRAFT",
            "EXACT_INTEGER_REPLAYED",
            "MATCHED_DIFFERENCE_CLOSED_ON_LOW_SPAN_BLOCKS",
        ],
        "theorem": {
            "zero_block_condition": (
                "If dim(sum_i L_i)<m^2, then D_m(perm_n) intersects "
                "sum_i D_m(T_i) trivially."
            ),
            "projection_consequence": (
                "A certified low-span block can be projected away with zero "
                "permanent-relative defect."
            ),
            "quotient_exactness": (
                "If dim(L_T+L_U)<m^2, quotient intersection equals the image "
                "of the literal intersection and the matched-difference image is zero."
            ),
            "independent_frame_literal_cap": (
                "For independent factor frames, dim(D_m(T) intersect D_m(U)) "
                "<= binom(dim(L_T intersect L_U),m)."
            ),
        },
        "central_table": central,
        "pair_summaries": pair_summaries,
        "projection_examples": projection_examples,
        "claim_boundary": (
            "The strict inequality dim(sum L_i)<m^2 is essential. Equality and "
            "high-span blocks remain open. The result supplies no unconditional "
            "new Chow-rank lower bound."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


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
    print("GENERAL_FACTOR_SPAN_ZERO_BLOCKS_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
