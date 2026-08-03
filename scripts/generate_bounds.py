#!/usr/bin/env python3
"""Generate deterministic JSON and CSV bound tables."""

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

from permanent_chow_rank.bounds import (  # noqa: E402
    best_koszul_bound,
    best_shadow_removal_bound,
    central_catalecticant_bound,
    glynn_upper_bound,
)


def build_records(max_n: int) -> list[dict[str, int | str | None]]:
    if max_n < 3:
        raise ValueError("max_n must be at least 3")

    records: list[dict[str, int | str | None]] = []
    for n in range(3, max_n + 1):
        base = best_koszul_bound(n)
        enhanced = best_shadow_removal_bound(n)
        records.append(
            {
                "n": n,
                "central_catalecticant": central_catalecticant_bound(n),
                "generalized_koszul": base.lower_bound,
                "shadow_removal": enhanced.lower_bound,
                "glynn_upper": glynn_upper_bound(n),
                "certificate_m": enhanced.m,
                "certificate_derivative_order": enhanced.derivative_order,
                "certificate_removed_terms": enhanced.removed_terms,
                "method": enhanced.method,
            }
        )
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=50)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data")
    args = parser.parse_args()

    records = build_records(args.max_n)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    json_path = args.output_dir / f"general_bounds_n3_n{args.max_n}.json"
    csv_path = args.output_dir / f"general_bounds_n3_n{args.max_n}.csv"

    json_path.write_text(
        json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
