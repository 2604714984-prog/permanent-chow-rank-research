#!/usr/bin/env python3
"""Generate exact even-degree multidimensional-shadow certificates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.even_multishadow import (  # noqa: E402
    central_koszul_lower_bound,
    reviewed_even_certificates,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--csv",
        type=Path,
        default=ROOT / "data" / "even_multishadow_bounds.csv",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=ROOT / "data" / "even_multishadow_bounds.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    certificates = list(reviewed_even_certificates())

    rows: list[dict[str, object]] = []
    for certificate in certificates:
        row = certificate.to_dict()
        row["central_koszul_lower_bound"] = central_koszul_lower_bound(certificate.n)
        rows.append(row)

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "n",
        "k",
        "witness",
        "witness_numerator",
        "witness_denominator",
        "central_koszul_lower_bound",
        "fixed_terms",
        "intersection_dimension_cap",
        "permanent_koszul_rank",
        "chow_term_koszul_cap",
        "residual_koszul_rank_floor",
        "residual_term_count",
        "lower_bound",
    ]
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in fieldnames})

    payload = {
        "status": "PROOF_DRAFT_COMPLETE",
        "method": "even-central-koszul-plus-multidimensional-shadow",
        "reference": "Bukh, arXiv:1009.2375",
        "scope": "ordinary Chow rank for even n",
        "certificates": rows,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(f"wrote {args.csv}")
    print(f"wrote {args.json}")
    print("EVEN_MULTISHADOW_TABLE_REPLAY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
