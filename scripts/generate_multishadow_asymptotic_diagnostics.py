#!/usr/bin/env python3
"""Generate exact parity-sensitive multishadow diagnostics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.multishadow_asymptotics import (  # noqa: E402
    even_limiting_constant,
    even_optimal_defect,
    odd_limiting_constant,
    odd_optimal_defect,
    reviewed_asymptotic_diagnostics,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        type=Path,
        default=ROOT / "data" / "multishadow_asymptotic_diagnostics.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = {
        "status": "EXACT_FINITE_DIAGNOSTICS_REPLAYED",
        "claim_boundary": (
            "Finite lower bounds use exact Fraction arithmetic. Decimal constants "
            "are display-only diagnostics for the proved asymptotic formulas."
        ),
        "analytic_limits": {
            "even_optimal_defect": f"{even_optimal_defect():.15f}",
            "odd_optimal_defect": f"{odd_optimal_defect():.15f}",
            "even_scaled_gain_limit": f"{even_limiting_constant():.15f}",
            "odd_scaled_gain_limit": f"{odd_limiting_constant():.15f}",
        },
        "diagnostics": [
            diagnostic.to_dict()
            for diagnostic in reviewed_asymptotic_diagnostics()
        ],
    }

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("MULTISHADOW_ASYMPTOTIC_DIAGNOSTICS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
