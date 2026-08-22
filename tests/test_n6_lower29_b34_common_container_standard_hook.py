from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_common_container_standard_hook.py"
DATA = ROOT / "data" / "n6_lower29_b34_common_container_standard_hook.json"

SPEC = importlib.util.spec_from_file_location("n6103", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestN6103(unittest.TestCase):
    def test_small_product_shadows(self) -> None:
        self.assertEqual(
            [MODULE.quadratic_product_shadow_minimum(size) for size in range(12, 16)],
            [11, 12, 12, 12],
        )

    def test_relation_graph_complements(self) -> None:
        rows = MODULE.relation_graph_rows()
        self.assertEqual(
            [row["admissible_intersection_graph_count"] for row in rows],
            [1, 16, 141, 966],
        )
        self.assertTrue(all(row["every_complement_connected"] for row in rows))

    def test_separated_bounds(self) -> None:
        self.assertEqual(
            [MODULE.separated_block_bound(kappa)[0] for kappa in range(4)],
            [40, 36, 36, 33],
        )

    def test_scalar_interface(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(
            [(row["kappa2"], row["t2"]) for row in payload["a2_72_rows"]],
            [(0, 18), (1, 17), (2, 16), (3, 15)],
        )
        self.assertEqual(payload["excluded_branch"]["kappa2"], 3)
        self.assertEqual(payload["global_zero_terms"]["minimum_external_epsilon_zero_terms"], 13)
        self.assertEqual(payload["global_zero_terms"]["all_nineteen_alpha"], 3)
        self.assertGreater(
            payload["global_zero_terms"]["prolongation_lower_bound"],
            payload["global_zero_terms"]["alpha_at_most_two_prolongation_cap"],
        )
        self.assertTrue(
            payload["global_zero_terms"]["all_nineteen_row_and_column_blocks_forced_singular"]
        )

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text(encoding="utf-8")), MODULE.build_payload())


if __name__ == "__main__":
    unittest.main()
