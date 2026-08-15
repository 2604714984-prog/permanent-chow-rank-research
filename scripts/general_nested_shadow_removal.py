#!/usr/bin/env python3
"""Combine existing zero-intersection removal with nonzero-intersection shadows.

The repository already proves the permanent-side derivative-shadow rigidity
and the corresponding zero-intersection criterion in
``docs/general_n_koszul_bounds.md``. This audit reuses that theorem inside
the later multidimensional-shadow and exact product-shadow arguments.

All arithmetic is exact integer arithmetic. The companion mathematical proof
is ``docs/general_nested_shadow_removal.md``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MULTISHADOW = ROOT / "data" / "multishadow_bounds.json"
EXACT_SHADOW = ROOT / "data" / "general_exact_product_shadow.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def zero_intersection_block(n: int, degree: int) -> dict[str, int]:
    """Largest block certified disjoint from D_degree(perm_n).

    This is exactly the finite optimization in Corollary 5.3 of
    ``docs/general_n_koszul_bounds.md``. ``derivative_order`` is the number of
    differentiations and ``zero_intersection_output_degree`` is the remaining
    output degree. Ties are reported at the smaller output degree.
    """

    require(n >= 2, n)
    require(2 <= degree <= n, (n, degree))
    candidates = []
    for order in range(1, degree):
        permanent_minimum = comb(degree, order) ** 2
        one_term_cap = min(comb(n, order), comb(n, degree - order))
        safe = (permanent_minimum - 1) // one_term_cap
        candidates.append(
            {
                "safe_terms": safe,
                "derivative_order": order,
                "zero_intersection_output_degree": degree - order,
                "permanent_minimum": permanent_minimum,
                "one_term_cap": one_term_cap,
            }
        )
    best = max(
        candidates,
        key=lambda row: (
            row["safe_terms"],
            -row["one_term_cap"],
            row["derivative_order"],
        ),
    )
    require(
        best["safe_terms"] * best["one_term_cap"]
        < best["permanent_minimum"],
        best,
    )
    return best


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def residual_count_from_general(raw: dict[str, object]) -> int:
    n = int(raw["n"])
    numerator = (
        int(raw["permanent_koszul_rank"])
        - n * n * int(raw["complementary_intersection_cap"])
    )
    require(numerator > 0, (n, numerator))
    return ceil_div(numerator, int(raw["chow_term_koszul_cap"]))


def general_rows() -> list[dict[str, object]]:
    payload = load_json(MULTISHADOW)
    certificates = payload.get("certificates")
    require(isinstance(certificates, list), "missing multishadow certificates")
    rows: list[dict[str, object]] = []
    for raw in certificates:
        require(isinstance(raw, dict), raw)
        n = int(raw["n"])
        if not 7 <= n <= 16:
            continue
        complementary_degree = int(raw["complementary_degree"])
        shadow_degree = complementary_degree - 1
        block = zero_intersection_block(n, shadow_degree)
        saving = block["safe_terms"]
        require(saving >= 1, (n, block))

        former_fixed = int(raw["fixed_terms"])
        enlarged_fixed = former_fixed + saving
        global_bound = int(raw["global_koszul_bound"])
        require(enlarged_fixed <= global_bound, (n, enlarged_fixed, global_bound))

        former_capacity = former_fixed * comb(n, shadow_degree)
        projected_capacity = (enlarged_fixed - saving) * comb(n, shadow_degree)
        require(former_capacity == projected_capacity, (n, former_capacity))

        residual = residual_count_from_general(raw)
        require(residual == int(raw["residual_term_count"]), (n, residual, raw))
        former_bound = int(raw["lower_bound"])
        require(former_fixed + residual == former_bound, (n, raw))
        refined = enlarged_fixed + residual
        require(refined == former_bound + saving, (n, refined, former_bound, saving))

        rows.append(
            {
                "n": n,
                "koszul_output_degree": int(raw["output_degree"]),
                "complementary_degree": complementary_degree,
                "shadow_degree": shadow_degree,
                **block,
                "former_fixed_terms": former_fixed,
                "enlarged_fixed_terms": enlarged_fixed,
                "unchanged_shadow_capacity": former_capacity,
                "unchanged_intersection_cap": int(
                    raw["complementary_intersection_cap"]
                ),
                "residual_terms": residual,
                "former_lower_bound": former_bound,
                "nested_shadow_lower_bound": refined,
                "global_first_koszul_bound": global_bound,
            }
        )

    require([row["n"] for row in rows] == list(range(7, 17)), rows)
    expected = {
        7: 42,
        8: 77,
        9: 142,
        10: 268,
        11: 508,
        12: 970,
        13: 1855,
        14: 3570,
        15: 6883,
        16: 13315,
    }
    require(
        {int(row["n"]): int(row["nested_shadow_lower_bound"]) for row in rows}
        == expected,
        rows,
    )
    return rows


def exact_rows() -> list[dict[str, object]]:
    payload = load_json(EXACT_SHADOW)
    rows: list[dict[str, object]] = []
    expected = {7: 43, 8: 78}
    for n, key in ((7, "n7_application"), (8, "n8_application")):
        raw = payload.get(key)
        require(isinstance(raw, dict), key)
        shadow_degree = int(raw["complement_degree"]) - 1
        block = zero_intersection_block(n, shadow_degree)
        saving = block["safe_terms"]
        require(saving == 1, (n, block))

        former_fixed = int(raw["fixed_term_count"])
        enlarged_fixed = former_fixed + saving
        capacity = int(raw["derivative_shadow_threshold"])
        require(
            capacity == (enlarged_fixed - saving) * comb(n, shadow_degree),
            (n, capacity),
        )
        require(
            int(raw["shadow_at_cap"]) <= capacity
            < int(raw["shadow_at_first_excluded_size"]),
            raw,
        )

        cap = int(raw["exact_intersection_cap"])
        numerator = int(raw["first_koszul_target_rank"]) - n * n * cap
        residual = ceil_div(numerator, int(raw["one_term_koszul_cap"]))
        require(residual == int(raw["residual_term_count"]), (n, residual, raw))
        refined = enlarged_fixed + residual
        require(refined == expected[n], (n, refined))
        require(enlarged_fixed <= int(raw["global_first_koszul_bound"]), raw)

        rows.append(
            {
                "n": n,
                "koszul_output_degree": int(raw["output_degree"]),
                "shadow_degree": shadow_degree,
                **block,
                "former_fixed_terms": former_fixed,
                "enlarged_fixed_terms": enlarged_fixed,
                "unchanged_shadow_capacity": capacity,
                "exact_intersection_cap": cap,
                "shadow_at_cap": int(raw["shadow_at_cap"]),
                "first_excluded_size": int(raw["first_excluded_size"]),
                "shadow_at_first_excluded_size": int(
                    raw["shadow_at_first_excluded_size"]
                ),
                "residual_terms": residual,
                "former_exact_shadow_bound": int(
                    raw["exact_multishadow_lower_bound"]
                ),
                "nested_exact_shadow_bound": refined,
            }
        )
    return rows


def asymptotic_rows() -> list[dict[str, int]]:
    rows = []
    for n in (16, 20, 24, 32, 40, 50, 64):
        complementary_degree = n // 2 if n % 2 == 0 else (n + 1) // 2
        shadow_degree = complementary_degree - 1
        rows.append(
            {
                "n": n,
                "shadow_degree": shadow_degree,
                **zero_intersection_block(n, shadow_degree),
            }
        )
    expected = {16: 3, 20: 6, 24: 13, 32: 51, 40: 205, 50: 1199, 64: 14757}
    require({row["n"]: row["safe_terms"] for row in rows} == expected, rows)
    return rows


def build_payload() -> dict[str, object]:
    core = {
        "status": [
            "NESTED_ZERO_INTERSECTION_INSIDE_MULTISHADOW",
            "EXISTING_SHADOW_REMOVAL_THEOREM_REUSED",
            "PERM7_LOWER_43",
            "PERM8_LOWER_78",
            "PERM15_GENERAL_BOUND_6883",
        ],
        "logical_dependencies": {
            "zero_intersection": (
                "Lemma 5.1, Lemma 5.2 and Corollary 5.3 of "
                "docs/general_n_koszul_bounds.md"
            ),
            "nonzero_intersection": "docs/general_multidimensional_shadow_bound.md",
            "exact_shadow": "docs/general_exact_product_shadow.md",
            "new_step": (
                "A section of the literal summation map is projected away "
                "from a zero-intersection block, retaining the old shadow "
                "capacity for more fixed terms."
            ),
        },
        "general_certificate_refinements": general_rows(),
        "exact_product_shadow_refinements": exact_rows(),
        "asymptotic_diagnostics": asymptotic_rows(),
        "asymptotic_statement": (
            "The reusable zero-intersection block has size "
            "Theta(((1+sqrt(2))/2)^n/sqrt(n)) along the central sequence, "
            "as already proved in docs/shadow_removal_asymptotics.md."
        ),
        "claim_boundary": (
            "The derivative-shadow rigidity and zero-intersection theorem "
            "are pre-existing repository results. The new contribution is "
            "their omitted-block integration with nonzero-intersection and "
            "exact product-shadow certificates. No exact-rank, border-rank, "
            "perm6, or novelty claim is made."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_NESTED_SHADOW_REMOVAL_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
