#!/usr/bin/env python3
"""Exact monomial-degeneration endpoint floors for factor ranks one to five."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def partitions(total: int, length: int, maximum: int | None = None):
    maximum = total if maximum is None else maximum
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(min(maximum, total - length + 1), 0, -1):
        for tail in partitions(total - first, length - 1, first):
            yield (first, *tail)


def monomial_middle_dimension(caps: tuple[int, ...]) -> int:
    return sum(
        1
        for exponent in itertools.product(*(range(cap + 1) for cap in caps))
        if sum(exponent) == 3
    )


def build() -> dict:
    rows = []
    for factor_rank in range(1, 6):
        profiles = sorted(
            (monomial_middle_dimension(caps), caps)
            for caps in partitions(7, factor_rank)
        )
        minimum_middle, witness = profiles[0]
        rows.append(
            {
                "factor_rank": factor_rank,
                "minimum_middle_dimension": minimum_middle,
                "minimum_partition": list(witness),
                "full_increment_surplus_floor": minimum_middle + 35 - 10 * factor_rank,
                "zero_increment_surplus_for_minimum_partition": 35 - minimum_middle,
                "positive_partitions": [
                    {"partition": list(caps), "middle_dimension": middle}
                    for middle, caps in profiles
                ],
            }
        )
    assert [row["minimum_middle_dimension"] for row in rows] == [1, 2, 4, 8, 15]
    assert [row["full_increment_surplus_floor"] for row in rows] == [26, 17, 9, 3, 0]
    return {
        "schema_version": 1,
        "claim": (
            "A product of seven linear forms with essential factor rank r<=5 "
            "degenerates to a positive r-variable monomial. The table gives the "
            "minimum middle dimension and resulting full-increment surplus floor."
        ),
        "claim_boundary": (
            "Equality forms outside the monomial special fibre and intermediate "
            "quotient increments are not classified here."
        ),
        "rows": rows,
        "pair_span_floor": 5,
        "triple_span_floor": 12,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    print(rendered, end="")
    print("N7_LOWER51_LOW_RANK_ENDPOINT_ATOMS_PASS")


if __name__ == "__main__":
    main()
