#!/usr/bin/env python3
"""Replay the compact deterministic checks from the 2026-08-22 Rethlas run."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "scripts" / "rethlas_perm7_20260822"

CASES = [
    (("slope10_adversarial_modular.py",), "PASS slope-ten adversarial modular diagnostic"),
    (("p64_ordinary_valuative_residual/residual_barrier_audit.py",), "PASS: all residual/projection barrier checks are exact"),
    (("round2_frobenius_tor/f2_dual_cospan.py",), "F2_DUAL_COSPAN_PASS"),
    (("round2_frobenius_tor/glynn_dual_cospan.py",), "GLYNN_DUAL_COSPAN_PASS"),
    (("round2_residual_flag/jet_incidence/jet_incidence_audit.py",), "JET_INCIDENCE_AUDIT_PASS"),
    (("round2_residual_flag/section_invariant/section_profile_audit.py",), "SECTION_PROFILE_AUDIT_PASS"),
    (("round2_residual_flag/section_invariant/koszul_young_capacity.py",), "SECTION_KOSZUL_YOUNG_CAPACITY_PASS"),
    (("round2_residual_flag/small_n_flags/small_n_flag_audit.py",), "SMALL_N_RESIDUAL_FLAG_AUDIT_PASS"),
    (("round2_row_weights/common_factor_tangent_audit.py",), "COMMON_FACTOR_TANGENT_AUDIT_PASS"),
    (("round2_row_weights/common_factor_circuits/circuit_audit.py",), "COMMON_FACTOR_CIRCUIT_AUDIT_PASS"),
    (("round2_row_weights/normal_layer/normal_layer_audit.py",), "NORMAL_LAYER_AUDIT_PASS"),
    (("round2_row_weights/anchor_search/glynn_tangent_audit.py", "--max-n", "4"), "GLYNN_TANGENT_AUDIT_PASS"),
    (("round2_row_weights/anchor_search/full_chow_row_tangent_audit.py", "--max-n", "4"), "FULL_CHOW_ROW_TANGENT_AUDIT_PASS"),
]


def main() -> int:
    for arguments, marker in CASES:
        command = [sys.executable, str(BASE / arguments[0]), *arguments[1:]]
        completed = subprocess.run(command, text=True, capture_output=True, check=False)
        transcript = completed.stdout + completed.stderr
        if completed.returncode != 0 or marker not in transcript:
            print(f"RETHLAS_PERM7_REPLAY_FAIL {arguments[0]}")
            print(transcript)
            return 1
        print(marker)
    print("RETHLAS_PERM7_20260822_REPLAY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
