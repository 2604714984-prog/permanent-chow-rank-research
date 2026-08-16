from __future__ import annotations

import hashlib
import json
import unittest
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "general_recursive_shadow_route_ceiling.json"
LEDGER = ROOT / "docs" / "RESEARCH_RESULTS_LEDGER.md"


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class GeneralRecursiveShadowRouteCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_core_hash(self) -> None:
        core = dict(self.payload)
        expected = core.pop("core_sha256")
        self.assertEqual(
            expected,
            "b4a55c1f6fe331b9c43159a0d7fad991645039c5feba1f25e6e979f1e07de86c",
        )
        self.assertEqual(canonical_sha256(core), expected)

    def test_n7_complete_output_degree_ceiling(self) -> None:
        rows = self.payload["n7"]["all_valid_output_degrees"]
        self.assertEqual(
            {degree: row["ceiling"] for degree, row in rows.items()},
            {"2": 44, "3": 45, "4": 43},
        )
        self.assertEqual(
            self.payload["n7"]["global_recursive_two_level_ceiling"],
            45,
        )
        representative = self.payload["n7"]["representative_optimum"]
        self.assertEqual(
            representative,
            {
                "block_cap": 64,
                "block_terms": 4,
                "fixed_terms": 19,
                "outer_cap": 341,
                "output_degree": 3,
                "projected_capacity": 589,
                "residual_terms": 26,
                "total": 45,
            },
        )

    def test_n8_recursive_cap_profile(self) -> None:
        beta = self.payload["n8"]["central_beta"]
        self.assertEqual(beta[:6], [0, 0, 16, 64, 106, 160])
        for terms in range(5, 59):
            self.assertEqual(beta[terms], 56 * terms - 120)
        self.assertTrue(all(value == 3136 for value in beta[59:]))

    def test_n8_central_route_ceiling(self) -> None:
        rows = self.payload["n8"]["central_route_rows"]
        self.assertEqual(len(rows), 77)
        self.assertEqual(max(row[-1] for row in rows), 79)
        self.assertEqual(
            [row[0] for row in rows if row[-1] == 79],
            [16, 17, 18, 19, 20, 21, 29],
        )
        self.assertEqual(
            self.payload["n8"]["central_recursive_two_level_ceiling"],
            79,
        )
        self.assertEqual(
            self.payload["n8"]["complementary_output_degree_5_ceiling"],
            78,
        )

    def test_exact_lower_80_target(self) -> None:
        target = self.payload["n8"]["next_lower_bound_target"]
        self.assertEqual(target["fixed_terms"], 20)
        self.assertEqual(target["block_terms"], 5)
        self.assertEqual(target["current_general_block_cap"], 160)
        self.assertEqual(target["required_chow_realizable_block_cap"], 146)
        self.assertEqual(target["required_cap_improvement"], 14)

        # q=20, residual=60, outer b<=772.
        koszul_target = 310_464
        one_term_cap = 4_424
        outer_cap = target["required_outer_intersection_cap"]
        self.assertGreater(
            koszul_target - 64 * outer_cap,
            59 * one_term_cap,
        )
        self.assertEqual(
            ceil((koszul_target - 64 * outer_cap) / one_term_cap),
            60,
        )
        self.assertEqual(
            target["outside_capacity"]
            + target["required_chow_realizable_block_cap"],
            target["maximum_projected_capacity"],
        )
        self.assertEqual(target["first_excluded_outer_size"], 773)
        self.assertEqual(target["first_excluded_outer_shadow"], 987)

    def test_ledger_update_policy(self) -> None:
        text = LEDGER.read_text(encoding="utf-8")
        self.assertIn("Every future theorem", text)
        self.assertIn("#42", text)
        self.assertIn("five-term", text)
        self.assertIn("146", text)


if __name__ == "__main__":
    unittest.main()
