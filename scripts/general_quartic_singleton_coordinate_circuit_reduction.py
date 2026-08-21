#!/usr/bin/env python3
"""Primary verifier for the positive-singleton coordinate two-jet barrier.

The independent exhaustive replay lives in
``general_quartic_singleton_coordinate_circuit_reduction_independent.py`` and
is executed separately by the focused test suite.  Keeping the primary CLI
lightweight avoids running that exhaustive enumeration twice inside one test
process while preserving both verification paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "general_quartic_singleton_coordinate_circuit_reduction.json"
EXPECTED_HASH = "a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def parse_scalar(value: object, parameter: Fraction) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    text = str(value)
    if text == "a":
        return parameter
    if text == "-1-a":
        return -1 - parameter
    raise RuntimeError(value)


def exact_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    rank = 0
    width = len(rows[0])
    for column in range(width):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                left - factor * right
                for left, right in zip(rows[row], rows[rank], strict=True)
            ]
        rank += 1
    return rank


def verify_normal_forms(core: dict[str, Any]) -> None:
    normal_forms = core["circuit_normal_forms"]["normal_forms"]
    for name, columns in normal_forms.items():
        for parameter in (Fraction(1), Fraction(2)):
            matrix = [[Fraction(0) for _ in columns] for _ in range(5)]
            for column_index, column in enumerate(columns):
                for support, coefficient in zip(
                    column["support"], column["coefficients"], strict=True
                ):
                    matrix[int(support)][column_index] = parse_scalar(coefficient, parameter)
            require(
                all(sum(matrix[row][column] for column in range(6)) == 0 for row in range(5)),
                (name, parameter, "sum"),
            )
            require(exact_rank(matrix) == 5, (name, parameter, "rank"))
            for omitted in range(6):
                minor = [row[:omitted] + row[omitted + 1 :] for row in matrix]
                require(exact_rank(minor) == 5, (name, parameter, omitted))


def payload() -> dict[str, Any]:
    value = json.loads(DATA.read_text(encoding="utf-8"))
    require(isinstance(value, dict), type(value))
    core = value.get("theorem_core")
    require(isinstance(core, dict), type(core))
    theorem_hash = hashlib.sha256(canonical_json(core).encode("utf-8")).hexdigest()
    require(theorem_hash == EXPECTED_HASH, theorem_hash)
    require(value.get("theorem_core_sha256") == theorem_hash, value.get("theorem_core_sha256"))
    verify_normal_forms(core)
    require(core["second_order_envelope"]["global_maximum_support"] == 23, core)
    require(core["second_order_envelope"]["perm4_matching_support"] == 24, core)
    require(core["strict_boundary"]["six_block_zero"] is False, core)
    return value


def main() -> None:
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


if __name__ == "__main__":
    main()
