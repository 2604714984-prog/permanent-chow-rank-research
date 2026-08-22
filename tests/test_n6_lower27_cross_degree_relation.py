from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower27_cross_degree_relation_audit.py"

SPEC = importlib.util.spec_from_file_location("n6_lower27_cross_degree", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the cross-degree relation audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6Lower27CrossDegreeRelationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_residual_relation_and_macaulay_endpoints(self) -> None:
        residual = self.payload["twenty_term_residual"]
        self.assertEqual(residual["ordinary_middle_relation_plus_radical_upper"], 16)
        self.assertEqual(residual["ordinary_quartic_relation_upper"], 25)
        endpoints = self.payload["macaulay_endpoint_checks"]
        self.assertEqual(endpoints["73_degree_2_successor"], 314)
        self.assertEqual(endpoints["74_degree_2_successor"], 322)

    def test_shadow_forces_203_quadratic_directions(self) -> None:
        residual = self.payload["twenty_term_residual"]
        self.assertEqual(residual["colored_quadratic_relation_lower_from_shadow"], 203)
        self.assertGreater(
            residual["colored_quadratic_relation_lower_from_shadow"],
            residual["colored_quadratic_relation_lower_from_macaulay_only"],
        )

    def test_fixed_six_dual_table(self) -> None:
        rows = self.payload["fixed_six_dual_quartic_intersection_table"]
        self.assertEqual([row["middle_intersection_b"] for row in rows], list(range(45, 65)))
        self.assertEqual(rows[0]["quartic_intersection_upper"], 15)
        self.assertEqual(rows[-1]["quartic_intersection_upper"], 22)
        self.assertTrue(
            all(
                row["dual_quadratic_shadow_lower"]
                + row["quartic_intersection_upper"]
                == 225
                for row in rows
            )
        )

    def test_scalar_state_is_explicitly_diagnostic(self) -> None:
        state = self.payload["scalar_nonclosure_witness"]
        self.assertEqual(state["classification"], "AGGREGATE_INTEGER_DIAGNOSTIC_ONLY")
        self.assertIn("not a family of Chow terms", state["warning"])
        fixed = state["fixed_six"]
        self.assertLessEqual(fixed["middle_rank_h"], 2 * fixed["middle_intersection_b"])
        self.assertLessEqual(45, fixed["middle_intersection_b"])
        self.assertLessEqual(fixed["middle_intersection_b"], 64)
        self.assertGreaterEqual(
            fixed["quadratic_rank"] - fixed["quadratic_intersection_a2"], 1
        )
        self.assertLessEqual(fixed["quartic_intersection_c4"], 22)
        self.assertGreaterEqual(
            state["twenty_term_residual"]["coupled_quadratic_intersection_with_E2"],
            203,
        )

    def test_claim_boundary(self) -> None:
        self.assertIn("Nothing here excludes", self.payload["claim_boundary"])
        self.assertIn("ChowRank(perm_6)>=27", self.payload["claim_boundary"])

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (
                ROOT
                / "data"
                / "n6_lower27_cross_degree_relation_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
