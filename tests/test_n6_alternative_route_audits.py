from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECOND_SCRIPT = ROOT / "scripts" / "n6_second_koszul_rank_audit.py"
GLYNN_SCRIPT = ROOT / "scripts" / "glynn_family_rigidity_audit.py"
SECOND_FROZEN = ROOT / "data" / "n6_second_koszul_rank_audit.json"
GLYNN_FROZEN = ROOT / "data" / "glynn_family_rigidity_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SECOND = load_module("n6_second_koszul_rank_audit", SECOND_SCRIPT)
GLYNN = load_module("glynn_family_rigidity_audit", GLYNN_SCRIPT)


class N6AlternativeRouteAuditTests(unittest.TestCase):
    def test_first_koszul_reference_values(self) -> None:
        self.assertEqual(
            [SECOND.first_koszul_permanent_rank(m) for m in (2, 3, 4)],
            [7700, 14175, 8064],
        )
        self.assertEqual(
            [SECOND.first_koszul_chow_rank(m) for m in (2, 3, 4)],
            [520, 705, 534],
        )
        self.assertEqual(
            [
                SECOND.ceil_div(
                    SECOND.first_koszul_permanent_rank(m),
                    SECOND.first_koszul_chow_rank(m),
                )
                for m in (2, 3, 4)
            ],
            [15, 21, 16],
        )

    def test_frozen_second_koszul_summary(self) -> None:
        frozen = json.loads(SECOND_FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen["prime"], 1_000_003)
        self.assertEqual(
            [row["certified_second_koszul_rank_ratio_lower_bound"] for row in frozen["degrees"]],
            [15, 21, 16],
        )
        self.assertEqual(
            [row["first_koszul_integer_rank_ratio_lower_bound"] for row in frozen["degrees"]],
            [15, 21, 16],
        )
        self.assertEqual(
            [row["rank_exact_in_characteristic_zero"] for row in frozen["degrees"]],
            [False, True, True],
        )

    def test_scalar_second_shadow_is_vacuous_for_q_at_least_six(self) -> None:
        for fixed_terms in (6, 7, 8):
            first_derivative_cap = min(36, 6 * fixed_terms)
            self.assertEqual(first_derivative_cap, 36)
            maximum_x = int(first_derivative_cap**0.5)
            self.assertEqual(maximum_x, 6)
            self.assertEqual(SECOND.comb(6, 3) ** 2, 400)

    def test_glynn_family_rigidity_and_frozen_summary(self) -> None:
        payload = GLYNN.build_payload()
        n6 = next(row for row in payload["degrees"] if row["n"] == 6)
        self.assertEqual(n6["family_size"], 32)
        self.assertEqual(n6["nonzero_expansion_coefficient_count"], 32)
        self.assertFalse(n6["proper_subfamily_can_span_permanent"])

        frozen = json.loads(GLYNN_FROZEN.read_text(encoding="utf-8"))
        compact = {
            "status": payload["status"],
            "n6_conclusion": payload["n6_conclusion"],
            "claim_boundary": payload["claim_boundary"],
            "degrees": [
                {
                    "n": row["n"],
                    "family_size": row["family_size"],
                    "nonzero_expansion_coefficient_count": row[
                        "nonzero_expansion_coefficient_count"
                    ],
                    "positive_coefficient_count": row[
                        "positive_coefficient_count"
                    ],
                    "negative_coefficient_count": row[
                        "negative_coefficient_count"
                    ],
                    "proper_subfamily_can_span_permanent": row[
                        "proper_subfamily_can_span_permanent"
                    ],
                }
                for row in payload["degrees"]
            ],
        }
        self.assertEqual(compact, frozen)


if __name__ == "__main__":
    unittest.main()
