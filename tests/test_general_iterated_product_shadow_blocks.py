from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_iterated_product_shadow_blocks.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_iterated_product_shadow_blocks_independent.py"
)
FROZEN = ROOT / "data" / "general_iterated_product_shadow_blocks.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_iterated_product_shadow_blocks", SCRIPT)


class GeneralIteratedProductShadowBlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_iterated_weight_formula(self) -> None:
        layer = AUDIT.colex_subsets(8, 3)
        weights = AUDIT.iterated_first_container_weights(8, 3, 2, layer)
        self.assertEqual(sum(weights), 8)
        self.assertEqual(weights[:4], (3, 1, 0, 0))

    def test_perm7_transition_and_bound(self) -> None:
        row = self.payload["n7_application"]
        self.assertEqual(
            (
                row["block_intersection_cap"],
                row["block_shadow_at_cap"],
                row["block_shadow_at_first_excluded_size"],
            ),
            (64, 84, 87),
        )
        self.assertEqual(
            (
                row["projected_first_shadow_capacity"],
                row["outer_intersection_cap"],
                row["outer_shadow_at_cap"],
                row["outer_shadow_at_first_excluded_size"],
            ),
            (589, 341, 586, 590),
        )
        self.assertEqual(row["residual_terms"], 26)
        self.assertEqual(row["two_level_lower_bound"], 45)

    def test_perm8_transition_and_bound(self) -> None:
        row = self.payload["n8_application"]
        self.assertEqual(
            (
                row["derivative_order"],
                row["block_intersection_cap"],
                row["block_shadow_at_cap"],
                row["block_shadow_at_first_excluded_size"],
            ),
            (2, 16, 16, 18),
        )
        self.assertEqual(
            (
                row["projected_first_shadow_capacity"],
                row["outer_intersection_cap"],
                row["outer_shadow_at_cap"],
                row["outer_shadow_at_first_excluded_size"],
            ),
            (856, 625, 850, 858),
        )
        self.assertEqual(row["residual_terms"], 62)
        self.assertEqual(row["two_level_lower_bound"], 79)

    def test_frozen_payload_matches(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "383c4eedcd88ab14259be9430f1654f7b0409092a0a237b3717a527dd06f736e",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_ITERATED_PRODUCT_SHADOW_BLOCKS_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=45", completed.stdout)
        self.assertIn("independent_perm8_lower_bound=79", completed.stdout)


if __name__ == "__main__":
    unittest.main()
