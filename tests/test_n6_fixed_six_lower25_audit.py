from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_fixed_six_lower25_audit.py"

spec = importlib.util.spec_from_file_location("lower25", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class Lower25AuditTests(unittest.TestCase):
    def test_macaulay_and_module_caps(self) -> None:
        scalar = [
            module.macaulay_successor_degree_two(value)
            for value in range(17)
        ]
        self.assertEqual(
            scalar,
            [
                0,
                1,
                2,
                4,
                5,
                7,
                10,
                11,
                13,
                16,
                20,
                21,
                23,
                26,
                30,
                35,
                36,
            ],
        )
        self.assertEqual(
            scalar,
            [module.module_partition_cap(value) for value in range(17)],
        )

    def test_shadow_certificates(self) -> None:
        payload = module.validate_shadow_certificates()
        self.assertEqual(payload["projection_cap"], 78)
        self.assertTrue(payload["b65_forces_shadow_at_least_79"])
        self.assertEqual(
            payload["per_b_certificates"]["42"][
                "integer_shadow_lower_bound"
            ],
            62,
        )
        self.assertEqual(
            payload["per_b_certificates"]["64"][
                "integer_shadow_lower_bound"
            ],
            78,
        )

    def test_all_relation_layers_are_strict(self) -> None:
        for b in range(42, 65):
            layer = module.layer_payload(b)
            self.assertGreater(layer["strict_margin"], 0)
            self.assertGreater(
                layer["minimum_coupled_central_rank_lower_bound"],
                layer["residual_central_rank_upper_bound"],
            )

    def test_full_payload(self) -> None:
        payload = module.build_payload()
        self.assertEqual(
            payload["status"],
            "EXACT_N6_FIXED_SIX_24_TERM_EXCLUSION_REPLAYED",
        )
        self.assertEqual(
            payload["certified_interval_if_algebraic_lemmas_are_accepted"],
            [25, 32],
        )
        self.assertTrue(
            payload["reconstructed_term_profiles"][
                "quadratic_dimension_twelve_impossible"
            ]
        )
        self.assertEqual(
            [row["strict_margin"] for row in payload["automatic_low_layers"]],
            [45, 9],
        )
        self.assertEqual(len(payload["component_relation_layers"]), 23)


if __name__ == "__main__":
    unittest.main()
