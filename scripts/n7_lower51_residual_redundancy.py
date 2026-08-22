#!/usr/bin/env python3
"""Exact arithmetic gate for the redundant-image residual theorem.

The mathematical content is proved in the companion note.  This replay
checks every integer residual cap allowed by v7 and deliberately keeps the
cap-35 boundary separate from the strict exclusion range.
"""

from __future__ import annotations

import json


LOCAL_QUARTIC_DIMENSION = 35


def consequence(residual_cap: int) -> str:
    if not 0 <= residual_cap <= LOCAL_QUARTIC_DIMENSION:
        raise ValueError("v7 residual cap must lie in 0,...,35")
    if residual_cap < LOCAL_QUARTIC_DIMENSION:
        return "EXCLUDED_BY_REDUNDANT_IMAGE_PROPAGATION"
    return "FORCED_K3_0_K4_35"


def main() -> None:
    rows = [
        {"residual_cap": cap, "consequence": consequence(cap)}
        for cap in range(LOCAL_QUARTIC_DIMENSION + 1)
    ]
    assert all(
        row["consequence"] == "EXCLUDED_BY_REDUNDANT_IMAGE_PROPAGATION"
        for row in rows[:-1]
    )
    assert rows[-1] == {
        "residual_cap": 35,
        "consequence": "FORCED_K3_0_K4_35",
    }
    print(
        json.dumps(
            {
                "local_quartic_dimension": LOCAL_QUARTIC_DIMENSION,
                "strict_exclusion_caps": [0, 34],
                "boundary_cap": 35,
                "rows": rows,
            },
            sort_keys=True,
        )
    )
    print("N7_LOWER51_RESIDUAL_REDUNDANCY_PASS")


if __name__ == "__main__":
    main()
