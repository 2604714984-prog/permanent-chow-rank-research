from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_fixed_six_offcentral_c42_ceiling.py"
DATA = ROOT / "data" / "n6_fixed_six_offcentral_c42_ceiling.json"


def load_script():
    spec = importlib.util.spec_from_file_location("offcentral_c42", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FixedSixOffcentralC42CeilingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_script()
        cls.payload = cls.module.build_payload()
        cls.frozen = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)
        self.assertEqual(
            self.payload["inherited_high_layers_verified_against"],
            "data/n6_lower27_hereditary_residual_audit.json",
        )

    def test_every_direct_c42_upper_is_below_twenty_term_cap(self) -> None:
        rows = self.payload["rows"]
        self.assertEqual([row["middle_intersection_b"] for row in rows], list(range(45, 65)))
        self.assertTrue(
            all(
                row["residual_C42_rank_upper_from_common_sum_space"] < 300
                for row in rows
            )
        )
        self.assertEqual(
            max(row["residual_C42_rank_upper_from_common_sum_space"] for row in rows),
            251,
        )

    def test_b64_endpoint_is_closed(self) -> None:
        endpoint = self.payload["b64_endpoint"]
        self.assertEqual(endpoint["middle_rank_h"], 120)
        self.assertEqual(endpoint["fixed_quadratic_rank_d2"], 90)
        self.assertEqual(endpoint["fixed_quadratic_intersection_a2"], 78)
        self.assertEqual(endpoint["fixed_quadratic_quotient_t2"], 12)
        self.assertEqual(endpoint["residual_C42_rank_window"], [215, 237])

    def test_high_layer_t2_intervals(self) -> None:
        by_b = {row["middle_intersection_b"]: row for row in self.payload["rows"]}
        self.assertEqual(
            {
                b: (
                    by_b[b]["fixed_quadratic_quotient_t2_lower"],
                    by_b[b]["fixed_quadratic_quotient_t2_upper"],
                )
                for b in range(58, 65)
            },
            {
                58: (2, 16),
                59: (4, 15),
                60: (4, 15),
                61: (8, 14),
                62: (10, 13),
                63: (10, 13),
                64: (12, 12),
            },
        )

    def test_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("N6_FIXED_SIX_OFFCENTRAL_C42_CEILING_PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
