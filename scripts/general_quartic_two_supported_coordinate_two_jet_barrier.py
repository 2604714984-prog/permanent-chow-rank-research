#!/usr/bin/env python3
"""Deterministic replay for the two-supported coordinate two-jet barrier.

The proof is recorded in
``docs/general_quartic_two_supported_coordinate_two_jet_barrier.md``.

This lightweight entry point performs three checks:

* rerun the independent exact modular reconstruction of every named support
  orbit and two deterministic points in every continuous gain chart;
* verify the integrity and schema of the frozen characteristic-zero symbolic
  kernel certificate; and
* verify the frozen theorem payload and its canonical SHA-256 digest.

The symbolic certificate is proof evidence, not a substitute for the written
characteristic-zero argument.  This script makes no unrestricted six-block or
border-rank claim.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import lzma
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_THEOREM_HASH = (
    "0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9"
)
EXPECTED_PAYLOAD_XZ_HASH = (
    "3517e2335ff0031df23ec3a890eb5307b340f6ddac0c994ab8ecc97b22b9b5e1"
)
EXPECTED_CERTIFICATE_XZ_HASH = (
    "723d556d1e5bd2a905f00cd69a294f1dafdff0ae2566df44666515ba25d6f9aa"
)
EXPECTED_CERTIFICATE_RAW_HASH = (
    "49cfa37dba3b74ac41e9b3f055ffad1b85c147fd47af58ee19c3a6ada1734c62"
)
PAYLOAD = ROOT / "data" / "general_quartic_two_supported_coordinate_two_jet_barrier.json.xz"
CERTIFICATE = (
    ROOT
    / "data"
    / "general_quartic_two_supported_coordinate_two_jet_symbolic_kernel_v2"
)
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_quartic_two_supported_coordinate_two_jet_barrier_independent.py"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_xz_json(path: Path, expected_xz_hash: str) -> dict[str, Any]:
    compressed = path.read_bytes()
    require(digest(compressed) == expected_xz_hash, (path, digest(compressed)))
    value = json.loads(lzma.decompress(compressed).decode("utf-8"))
    require(isinstance(value, dict), path)
    return value


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def load_independent_module():
    spec = importlib.util.spec_from_file_location("quartic_two_jet_independent", INDEPENDENT)
    require(spec is not None and spec.loader is not None, INDEPENDENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def replay_independent() -> None:
    module = load_independent_module()
    require(len(module.CYCLE_EXPECTED) == 13, len(module.CYCLE_EXPECTED))
    require(sum(len(rows) for rows in module.CHART_EXPECTED.values()) == 28, module.CHART_EXPECTED)
    module.replay_unit_cycles()
    module.replay_symbolic_charts_at_generic_points()


def verify_certificate(path: Path) -> dict[str, Any]:
    manifest_path = path / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    require(
        manifest.get("schema")
        == "general_quartic_two_supported_coordinate_two_jet_symbolic_kernel_shards/v1",
        manifest.get("schema"),
    )
    chunks = []
    for row in manifest.get("parts", []):
        part = path / str(row["path"])
        data = part.read_bytes()
        require(len(data) == int(row["bytes"]), (part, len(data)))
        require(digest(data) == str(row["sha256"]), (part, digest(data)))
        chunks.append(data)
    compressed = b"".join(chunks)
    require(len(compressed) == int(manifest["combined_bytes"]), len(compressed))
    require(digest(compressed) == EXPECTED_CERTIFICATE_XZ_HASH, digest(compressed))
    require(digest(compressed) == str(manifest["combined_sha256"]), digest(compressed))
    raw = lzma.decompress(compressed)
    require(digest(raw) == EXPECTED_CERTIFICATE_RAW_HASH, digest(raw))
    certificate = json.loads(raw.decode("utf-8"))
    require(
        certificate.get("schema")
        == "general_quartic_two_supported_coordinate_two_jet_symbolic_kernel/v2",
        certificate.get("schema"),
    )
    charts = certificate.get("charts")
    require(isinstance(charts, list) and len(charts) == 6, type(charts))
    chart_names = {str(chart.get("name")) for chart in charts}
    require(
        chart_names
        == {
            "tight_handcuff_full_character_rank",
            "tight_handcuff_deficient_character_rank",
            "loose_handcuff_full_character_rank",
            "loose_handcuff_deficient_character_rank",
            "theta_full_character_rank",
            "six_cycle_deficient_character_rank",
        },
        chart_names,
    )
    return certificate


def verify_payload(path: Path) -> dict[str, Any]:
    payload = read_xz_json(path, EXPECTED_PAYLOAD_XZ_HASH)
    core = payload.get("theorem_core")
    require(isinstance(core, dict), type(core))
    theorem_hash = hashlib.sha256(canonical_json(core).encode("utf-8")).hexdigest()
    require(theorem_hash == EXPECTED_THEOREM_HASH, theorem_hash)
    require(payload.get("theorem_core_sha256") == theorem_hash, payload.get("theorem_core_sha256"))
    require(core.get("global_maximum_two_jet_matching_support") == 8, core)
    require(core.get("perm4_matching_support") == 24, core)
    boundary = core.get("claim_boundary", {})
    require(boundary.get("six_block_exclusion") is False, boundary)
    require(boundary.get("mu_6_4_exact_value") == "OPEN_IN_[6,8]", boundary)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", type=Path, default=PAYLOAD)
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()

    replay_independent()
    verify_certificate(arguments.certificate)
    payload = verify_payload(arguments.payload)
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_PASS")
    print(EXPECTED_THEOREM_HASH)


if __name__ == "__main__":
    main()
