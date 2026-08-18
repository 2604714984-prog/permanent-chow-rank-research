#!/usr/bin/env python3
"""Compile and audit the recursively zero-seeded derivative tower.

The C++17 engine rebuilds the exact Ferrers inverse shadows, the original
prefix min-plus tower, and the tower after inserting the hard zero rows
certified by the current factor-span/private-polar stack and PR #80.

The exact result through n=10 is diagnostic: capacities change in a few low-q
cells, but every saturation threshold remains unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CPP_SOURCE = ROOT / "scripts" / "general_recursive_zero_seeded_tower.cpp"
FROZEN = ROOT / "data" / "general_recursive_zero_seeded_tower.json"
EXPECTED_CORE_SHA256 = "db770e0622813e208dbedaef03c83dd70e43c1cfff42e3d71729183515da1312"


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


def expected_thresholds() -> dict[str, list[int]]:
    return {
        "3": [3, 4],
        "4": [4, 7, 8],
        "5": [5, 11, 14, 15],
        "6": [6, 16, 24, 26, 27],
        "7": [7, 22, 39, 46, 48, 49],
        "8": [8, 29, 59, 80, 87, 89, 90],
        "9": [9, 37, 87, 136, 155, 161, 163, 164],
        "10": [10, 46, 123, 219, 280, 299, 305, 307, 307],
    }


def expected_zero_counts() -> dict[str, list[int]]:
    return {
        "3": [0, 1, 3],
        "4": [0, 0, 2, 5],
        "5": [0, 0, 2, 5, 9],
        "6": [0, 0, 1, 3, 7, 12],
        "7": [0, 0, 1, 3, 6, 11, 17],
        "8": [0, 0, 1, 2, 5, 9, 15, 22],
        "9": [0, 0, 0, 2, 4, 7, 12, 19, 27],
        "10": [0, 0, 0, 2, 4, 7, 11, 17, 25, 34],
    }


def expected_changes() -> dict[str, tuple[int, int]]:
    return {
        "3": (0, 0),
        "4": (0, 0),
        "5": (2, 1),
        "6": (0, 0),
        "7": (1, 1),
        "8": (1, 1),
        "9": (2, 1),
        "10": (4, 2),
    }


def find_compiler() -> str:
    requested = os.environ.get("CXX")
    candidates = [requested] if requested else []
    candidates.extend(["g++", "c++", "clang++"])
    for candidate in candidates:
        if candidate and shutil.which(candidate):
            return candidate
    raise RuntimeError("No C++17 compiler found; exact replay fails closed")


def compile_and_run() -> dict[str, Any]:
    compiler = find_compiler()
    require(CPP_SOURCE.is_file(), CPP_SOURCE)
    with tempfile.TemporaryDirectory(prefix="recursive_zero_tower_") as directory:
        executable = Path(directory) / "recursive_zero_seeded_tower"
        base_command = [
            compiler,
            "-std=c++17",
            "-O2",
            "-Wall",
            "-Wextra",
            "-pedantic",
            str(CPP_SOURCE),
            "-o",
            str(executable),
        ]
        parallel = subprocess.run(
            base_command + ["-fopenmp"],
            capture_output=True,
            text=True,
            timeout=180,
        )
        if parallel.returncode != 0:
            subprocess.run(
                base_command,
                check=True,
                capture_output=True,
                text=True,
                timeout=180,
            )
        completed = subprocess.run(
            [str(executable)],
            check=True,
            capture_output=True,
            text=True,
            timeout=600,
        )

    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    require(len(lines) == 2, lines)
    require(lines[-1] == "RECURSIVE_ZERO_SEEDED_TOWER_AUDIT_PASS", lines)
    payload = json.loads(lines[0])
    rows = payload["rows"]
    require(set(rows) == set(expected_thresholds()), rows)

    for n_text, expected in expected_thresholds().items():
        row = rows[n_text]
        require(row["thresholds"] == expected, (n_text, row))
        require(
            row["zero_counts"] == expected_zero_counts()[n_text],
            (n_text, row),
        )
        changed, maximum = expected_changes()[n_text]
        require(row["changed_capacity_cells"] == changed, (n_text, row))
        require(row["maximum_capacity_reduction"] == maximum, (n_text, row))
    return payload


def build_payload() -> dict[str, Any]:
    replay = compile_and_run()

    core: dict[str, Any] = {
        "status": [
            "RECURSIVE_ZERO_SEEDED_TOWER_EXACT_DIAGNOSTIC",
            "HARD_ZERO_ROWS_INSERTED",
            "THRESHOLDS_UNCHANGED_N3_TO_N10",
            "EXACT_INTEGER_CPP_REPLAYED",
        ],
        "theorem_interface": {
            "direct_seed": (
                "Use the strongest current direct zero count at each output "
                "degree from the strict, endpoint, first-excess and PR #79 bands."
            ),
            "recursive_closure": (
                "Zhat_(n,d)=max(direct_seed_(n,d),"
                "Zhat_(n,d-1)+floor((d^2-1)/n))."
            ),
            "tower_insertion": (
                "Set the direct permanent-relative capacity to zero for "
                "q<=Zhat_(n,d), then rebuild the exact inverse-shadow and "
                "prefix min-plus recurrence at every degree."
            ),
        },
        "exact_result": {
            "n_min": 3,
            "n_max": 10,
            "rows": replay["rows"],
            "thresholds_unchanged": True,
            "maximum_changed_capacity_cells": max(
                row["changed_capacity_cells"]
                for row in replay["rows"].values()
            ),
            "maximum_capacity_reduction": max(
                row["maximum_capacity_reduction"]
                for row in replay["rows"].values()
            ),
        },
        "claim_boundary": (
            "This is an exact finite diagnostic for the named scalar tower "
            "through n=10. It proves that the current recursive hard-zero "
            "seeds do not change the published saturation thresholds on that "
            "range. It is not a theorem that polynomial zero seeds are "
            "asymptotically irrelevant, does not rule out improvements for "
            "n>=11, and introduces no new Chow-rank or border-rank bound."
        ),
    }
    payload = {**core, "core_sha256": canonical_hash(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_RECURSIVE_ZERO_SEEDED_TOWER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
