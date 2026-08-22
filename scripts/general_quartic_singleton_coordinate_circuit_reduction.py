#!/usr/bin/env python3
"""Verify the corrected positive-singleton coordinate two-jet packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "general_quartic_singleton_coordinate_circuit_reduction.json"
EXPECTED_HASH = "cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def scalar(value: object, parameter: Fraction) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    if value == "a":
        return parameter
    if value == "-1-a":
        return -1 - parameter
    raise RuntimeError(value)


def rank(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                left - factor * right
                for left, right in zip(rows[row], rows[pivot_row], strict=True)
            ]
        pivot_row += 1
    return pivot_row


def verify_normal_forms(core: dict[str, object]) -> None:
    forms = core["circuit_normal_forms"]["normal_forms"]
    for name, columns in forms.items():
        for parameter in (Fraction(1), Fraction(2), Fraction(-2)):
            matrix = [[Fraction(0) for _ in columns] for _ in range(5)]
            for column_index, column in enumerate(columns):
                for support, coefficient in zip(
                    column["support"], column["coefficients"], strict=True
                ):
                    matrix[int(support)][column_index] = scalar(coefficient, parameter)
            require(
                all(sum(matrix[row]) == 0 for row in range(5)),
                (name, parameter, "sum"),
            )
            require(rank(matrix) == 5, (name, parameter, "rank"))
            for omitted in range(6):
                minor = [row[:omitted] + row[omitted + 1 :] for row in matrix]
                require(rank(minor) == 5, (name, parameter, omitted))


def payload() -> dict[str, object]:
    value = json.loads(DATA.read_text(encoding="utf-8"))
    core = value["theorem_core"]
    encoded = json.dumps(
        core, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    theorem_hash = hashlib.sha256(encoded).hexdigest()
    require(theorem_hash == EXPECTED_HASH, theorem_hash)
    require(value["theorem_core_sha256"] == theorem_hash, value)
    verify_normal_forms(core)
    support = core["positive_singleton_support_classification"]
    require(
        support["embedding_counts_fixed_identity"]
        == {
            "double_edge_tail": 696,
            "endpoint_marked_p5": 696,
            "square_lollipop": 216,
        },
        support,
    )
    envelope = core["second_order_envelope"]
    require(envelope["global_maximum_support"] == 23, envelope)
    require(envelope["perm4_matching_support"] == 24, envelope)
    require(core["strict_boundary"]["six_block_zero"] is False, core)
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    value = payload()
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_PASS")
    print(EXPECTED_HASH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
