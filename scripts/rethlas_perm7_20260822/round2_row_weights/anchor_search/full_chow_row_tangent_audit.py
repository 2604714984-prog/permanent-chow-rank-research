#!/usr/bin/env python3
"""Exact row-weight tangent audit in the full Chow ambient space.

Unlike ``glynn_tangent_audit.py``, this permits every linear-factor variation
in all n^2 variables.  It therefore audits the actual Chow tangent spaces,
not merely the column-separated Segre subfamily.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

from glynn_tangent_audit import glynn_signs, rank_mod_prime, rank_over_q


def multiply_factors(n, factors):
    """Expand a product; a factor is either ('column', j, eps) or ('unit', v)."""
    terms = {(): 1}
    for factor in factors:
        next_terms = {}
        if factor[0] == "column":
            _, column, eps = factor
            choices = [(row * n + column, eps[row]) for row in range(n)]
        else:
            _, variable = factor
            choices = [(variable, 1)]
        for monomial, coefficient in terms.items():
            for variable, value in choices:
                new_monomial = tuple(sorted(monomial + (variable,)))
                next_terms[new_monomial] = (
                    next_terms.get(new_monomial, 0) + coefficient * value
                )
        terms = {monomial: value for monomial, value in next_terms.items() if value}
    return terms


def tangent_columns(n):
    columns = []
    for eps in glynn_signs(n):
        base = [("column", j, eps) for j in range(n)]
        columns.append(multiply_factors(n, base))
        for omitted_factor in range(n):
            # L_(omitted_factor) has coefficient one on x_(0,omitted_factor),
            # so all other coordinate variables give a complement to its span.
            pivot_variable = omitted_factor
            for variable in range(n * n):
                if variable == pivot_variable:
                    continue
                factors = list(base)
                factors[omitted_factor] = ("unit", variable)
                columns.append(multiply_factors(n, factors))
    return columns


def is_row_multilinear(n, monomial):
    counts = [0] * n
    for variable in monomial:
        counts[variable // n] += 1
    return all(count == 1 for count in counts)


def audit(n):
    columns = tangent_columns(n)
    all_rows = sorted(set().union(*(column.keys() for column in columns)))
    target_rows = [row for row in all_rows if is_row_multilinear(n, row)]
    off_rows = [row for row in all_rows if not is_row_multilinear(n, row)]

    rank_full = rank_over_q(columns, all_rows)
    rank_off = rank_over_q(columns, off_rows)
    rank_target = rank_over_q(columns, target_rows)
    modular_replays = {}
    for prime in (1000003, 1000033):
        replay = {
            "full": rank_mod_prime(columns, all_rows, prime),
            "off": rank_mod_prime(columns, off_rows, prime),
            "target": rank_mod_prime(columns, target_rows, prime),
        }
        assert replay == {
            "full": rank_full,
            "off": rank_off,
            "target": rank_target,
        }
        modular_replays[str(prime)] = replay
    domain = len(columns)
    compatible_target_motion = rank_full - rank_off
    expected = n**n if n == 2 else n**3 - 2 * n + 2
    one_term = n * (n * n - 1) + 1

    assert domain == 2 ** (n - 1) * one_term
    assert rank_target == expected
    assert compatible_target_motion == expected
    if n >= 3:
        assert domain - rank_full == n - 1
        assert domain - rank_off == one_term

    return {
        "n": n,
        "terms": 2 ** (n - 1),
        "full_symmetric_ambient_dimension": math.comb(n * n + n - 1, n),
        "tangent_support_rows": len(all_rows),
        "row_multilinear_ambient_dimension": n**n,
        "one_term_full_chow_tangent_dimension": one_term,
        "direct_sum_tangent_dimension": domain,
        "rank_full_jacobian": rank_full,
        "rank_row_offweight_jacobian": rank_off,
        "rank_row_target_restriction": rank_target,
        "kernel_full_jacobian_dimension": domain - rank_full,
        "kernel_row_offweight_jacobian_dimension": domain - rank_off,
        "compatible_row_target_motion_dimension": compatible_target_motion,
        "expected_row_block_orbit_tangent_dimension": expected,
        "independent_modular_replays": modular_replays,
        "checks": {
            "compatible_motion_equals_full_minus_off_rank": True,
            "compatible_motion_is_exactly_row_block_GL_tangent": True,
            "all_ranks_over_Q": True,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=4)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if not 2 <= args.max_n <= 4:
        raise SystemExit("exact full-Chow audit supports 2 <= max-n <= 4")
    payload = [audit(n) for n in range(2, args.max_n + 1)]
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("FULL_CHOW_ROW_TANGENT_AUDIT_PASS")


if __name__ == "__main__":
    main()
