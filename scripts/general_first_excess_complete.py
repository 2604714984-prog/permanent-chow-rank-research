#!/usr/bin/env python3
"""Exact replay for the complete first-excess zero theorem.

The proof is in docs/general_first_excess_complete.md.  The only new finite
interface is the exact quadratic product-shadow transition

    F_(5,2)(1)=4,
    F_(5,2)(2)=6,

which closes the cubic triple (n,m,q)=(5,3,2).  The parent first-excess audit
supplies the complete divisor scan and the reduction to the two cubic branches.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from general_exact_product_shadow import ExactProductShadow
from general_first_excess_circuit_reduction import build_payload as build_parent


FROZEN = ROOT / "data" / "general_first_excess_complete.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def zeta_plus(n: int, m: int) -> int:
    require(n >= m >= 3, (n, m))
    return (m * m + 1) // n


def build_payload() -> dict[str, Any]:
    parent = build_parent()
    parent_rows = parent["scan"]["rows"]
    cubic_rows = [row for row in parent_rows if row["m"] == 3]
    require(
        cubic_rows
        == [
            {
                "n": 5,
                "m": 3,
                "q": 2,
                "first_excess": 10,
                "derivative_gap": False,
            }
        ],
        cubic_rows,
    )

    shadow = ExactProductShadow(5, 2)
    minimum_one = shadow.minimum(1)
    minimum_two = shadow.minimum(2)
    last_good, first_bad = shadow.transition(5)

    require(minimum_one.shadow_size == 4, minimum_one)
    require(minimum_two.shadow_size == 6, minimum_two)
    require(last_good.family_size == 1, last_good)
    require(last_good.shadow_size == 4, last_good)
    require(first_bad.family_size == 2, first_bad)
    require(first_bad.shadow_size == 6, first_bad)

    direct_polar_dimension = 5
    circuit_polar_dimension = 4
    inverse_capacity = last_good.family_size
    require(direct_polar_dimension > inverse_capacity, direct_polar_dimension)
    require(circuit_polar_dimension > inverse_capacity, circuit_polar_dimension)

    core = {
        "status": [
            "COMPLETE_GENERAL_FIRST_POSITIVE_EXCESS_ZERO_THEOREM",
            "CUBIC_EXCEPTION_CLOSED_BY_EXACT_PRODUCT_SHADOW",
            "EXACT_INTEGER_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "closed_range": (
                "For m>=3, q>=2 and q*n<=m^2+1, every q-term Chow block "
                "has zero intersection with D_m(perm_n)."
            ),
            "zero_block": (
                "zeta_plus(n,m)=floor((m^2+1)/n), for m>=3 when the "
                "displayed quotient is at least two."
            ),
            "next_open_excess": "q*n=m^2+2.",
        },
        "cubic_interface": {
            "n": 5,
            "m": 3,
            "q": 2,
            "quadratic_shadow_budget": 5,
            "minimum_shadow_size_1": minimum_one.shadow_size,
            "minimum_shadow_size_2": minimum_two.shadow_size,
            "inverse_shadow_capacity": inverse_capacity,
            "direct_polar_dimension": direct_polar_dimension,
            "circuit_private_polar_dimension": circuit_polar_dimension,
        },
        "parent_boundary": {
            "parent_core_sha256": parent["core_sha256"],
            "parent_cubic_exception": parent["theorem"]["cubic_exception"],
        },
        "selected_zero_block_examples": [
            {"n": 5, "m": 3, "zeta_plus": zeta_plus(5, 3)},
            {"n": 13, "m": 5, "zeta_plus": zeta_plus(13, 5)},
            {"n": 10, "m": 7, "zeta_plus": zeta_plus(10, 7)},
            {"n": 13, "m": 8, "zeta_plus": zeta_plus(13, 8)},
        ],
        "claim_boundary": (
            "This is an ordinary characteristic-zero zero-intersection "
            "theorem for the first positive factor-span excess. It does not "
            "prove a new exact Chow rank, optimize all finite-n numerical "
            "bounds, improve border rank or establish literature novelty."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        for key in (
            "status",
            "theorem",
            "cubic_interface",
            "parent_boundary",
            "selected_zero_block_examples",
            "claim_boundary",
        ):
            require(frozen[key] == payload[key], ("frozen mismatch", key))

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_FIRST_EXCESS_COMPLETE_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
