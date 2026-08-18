#!/usr/bin/env python3
"""Exact arithmetic audit for multiblock polar descent.

The proof is in ``docs/general_multiblock_polar_descent.md``.

If z terms are known to have zero permanent-relative intersection in output
degree d-1, then

    z + floor((d^2-1)/n)

terms have zero intersection in output degree d.  Iterating from degree one
gives the universal count

    Z_(n,m) = sum_(d=2)^m floor((d^2-1)/n).

The code checks the exact integer interface, finite descent traces and selected
comparison rows.  The linear-algebra proof is in the companion document.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "data" / "general_multiblock_polar_descent.json"
EXPECTED_CORE_SHA256 = "bee52542fdaf272923cd937d97397a64670ee68e23c6b656f070b14abbcb2794"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def lifting_increment(n: int, degree: int) -> int:
    require(n >= degree >= 2, (n, degree))
    return (degree * degree - 1) // n


def lifted_zero_counts(n: int, maximum_degree: int | None = None) -> tuple[int, ...]:
    require(n >= 2, n)
    if maximum_degree is None:
        maximum_degree = n
    require(1 <= maximum_degree <= n, (n, maximum_degree))
    values = [0] * (maximum_degree + 1)
    for degree in range(2, maximum_degree + 1):
        values[degree] = values[degree - 1] + lifting_increment(n, degree)
    return tuple(values)


def descent_trace(n: int, degree: int, term_count: int) -> tuple[dict[str, int | str], ...]:
    """Replay the inductive proof for one term count.

    At degree d, ``a=floor((d^2-1)/n)`` labels may be discarded while leaving
    a nonzero polar supported on the remaining labels.  If the current term
    count is at most a, the strict factor-span theorem closes immediately.
    """

    require(n >= degree >= 1, (n, degree))
    require(term_count >= 0, term_count)
    trace: list[dict[str, int | str]] = []
    current = term_count
    for output_degree in range(degree, 1, -1):
        increment = lifting_increment(n, output_degree)
        if current <= increment:
            trace.append(
                {
                    "output_degree": output_degree,
                    "term_count_before": current,
                    "discarded_labels": current,
                    "term_count_after": 0,
                    "route": "STRICT_FACTOR_SPAN",
                }
            )
            current = 0
            break
        next_count = current - increment
        trace.append(
            {
                "output_degree": output_degree,
                "term_count_before": current,
                "discarded_labels": increment,
                "term_count_after": next_count,
                "route": "MULTIBLOCK_POLAR_DESCENT",
            }
        )
        current = next_count
    require(current == 0, (n, degree, term_count, trace))
    return tuple(trace)


def top_rank_lower_bound(n: int) -> int:
    """The direct rank consequence at output degree n."""

    return lifted_zero_counts(n)[n] + 1


def selected_degree_rows() -> list[dict[str, int]]:
    choices = [
        (8, 5),
        (9, 6),
        (10, 8),
        (12, 8),
        (16, 12),
        (20, 10),
        (32, 16),
        (64, 32),
        (100, 50),
    ]
    rows = []
    for n, degree in choices:
        counts = lifted_zero_counts(n, degree)
        rows.append(
            {
                "n": n,
                "degree": degree,
                "last_increment": lifting_increment(n, degree),
                "guaranteed_zero_terms": counts[degree],
                "direct_strict_terms": (degree * degree - 1) // n,
            }
        )
    return rows


def build_payload(maximum_n: int = 256) -> dict[str, Any]:
    require(maximum_n >= 8, maximum_n)

    one_step_checks = 0
    recurrence_checks = 0
    exhaustive_trace_checks = 0
    ceiling_identity_checks = 0

    top_rows: dict[str, dict[str, int]] = {}
    for n in range(2, maximum_n + 1):
        values = lifted_zero_counts(n)
        require(values[0] == values[1] == 0, (n, values[:2]))
        for degree in range(2, n + 1):
            increment = lifting_increment(n, degree)
            require(
                increment == ((degree * degree + n - 1) // n) - 1,
                (n, degree, increment),
            )
            ceiling_identity_checks += 1
            require(increment * n < degree * degree, (n, degree, increment))
            one_step_checks += 1
            require(
                values[degree] == values[degree - 1] + increment,
                (n, degree, values[degree]),
            )
            recurrence_checks += 1

        rank_lower = values[n] + 1
        central = comb(n, n // 2)
        glynn = 2 ** (n - 1)
        if n >= 4:
            require(rank_lower <= central, (n, rank_lower, central))
        require(rank_lower <= glynn, (n, rank_lower, glynn))
        if n in {3, 4, 5, 8, 9, 10, 16, 32, 64, 100, 128, 256}:
            top_rows[str(n)] = {
                "zero_terms": values[n],
                "rank_lower_bound": rank_lower,
                "central_binomial_lower_bound": central,
                "glynn_upper_bound": glynn,
            }

    for n in range(2, min(maximum_n, 40) + 1):
        values = lifted_zero_counts(n)
        for degree in range(2, n + 1):
            for terms in range(values[degree] + 1):
                descent_trace(n, degree, terms)
                exhaustive_trace_checks += 1

    selected = selected_degree_rows()
    require(
        {(row["n"], row["degree"]): row["guaranteed_zero_terms"] for row in selected}
        == {
            (8, 5): 5,
            (9, 6): 6,
            (10, 8): 16,
            (12, 8): 14,
            (16, 12): 35,
            (20, 10): 15,
            (32, 16): 40,
            (64, 32): 164,
            (100, 50): 404,
        },
        selected,
    )

    core: dict[str, Any] = {
        "status": [
            "GENERAL_MULTIBLOCK_POLAR_DESCENT",
            "RECURSIVE_CHOW_ZERO_BLOCK_LIFTING",
            "QUADRATIC_SIZE_ZERO_BLOCKS_AT_LINEAR_OUTPUT_DEGREE",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "one_step": (
                "If z_(n,d-1) terms have zero permanent-relative intersection "
                "in output degree d-1, then z_(n,d-1)+floor((d^2-1)/n) "
                "terms have zero intersection in output degree d."
            ),
            "closed_form": (
                "Z_(n,m)=sum_(d=2)^m floor((d^2-1)/n) is a guaranteed "
                "zero-block size for D_m(perm_n)."
            ),
            "rank_consequence": (
                "ChowRank(perm_n)>=1+sum_(d=2)^n floor((d^2-1)/n)."
            ),
            "asymptotic": (
                "For m=floor(alpha*n), Z_(n,m)=(alpha^3/3)n^2+O(n)."
            ),
        },
        "proof_interface": {
            "discarded_labels": "a_(n,d)=floor((d^2-1)/n)",
            "discarded_span": "a_(n,d)*n<d^2",
            "remaining_polar_terms": "q-a_(n,d)",
            "coupled_literal_firewall": (
                "The polar is taken from one selected literal representation "
                "of an actual intersection element; no coupled image is "
                "identified with the literal sum."
            ),
        },
        "finite_replay": {
            "maximum_n": maximum_n,
            "one_step_checks": one_step_checks,
            "recurrence_checks": recurrence_checks,
            "ceiling_identity_checks": ceiling_identity_checks,
            "exhaustive_trace_checks": exhaustive_trace_checks,
            "selected_degree_rows": selected,
            "top_rows": top_rows,
        },
        "claim_boundary": (
            "This is an ordinary characteristic-zero Chow-realizability "
            "zero-block theorem. Its direct top-degree rank consequence is "
            "polynomial and, apart from the exact n=3 endpoint, no stronger "
            "than the existing central-binomial bound; "
            "no optimized finite-n lower bound, exact rank beyond the accepted "
            "small orders, border-rank result, asymptotic Glynn proof or "
            "literature-novelty claim is made. The main use is as a hard zero "
            "seed for future derivative-tower and block-projection arguments."
        ),
    }
    payload = {**core, "core_sha256": canonical_hash(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload["core_sha256"])
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-n", type=int, default=256)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload(args.maximum_n)
    if FROZEN.exists() and args.maximum_n == 256:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_MULTIBLOCK_POLAR_DESCENT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
