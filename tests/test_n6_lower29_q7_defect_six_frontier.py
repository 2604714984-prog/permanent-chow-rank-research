from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_q7_defect_six_frontier.py"
FROZEN = ROOT / "data" / "n6_lower29_q7_defect_six_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6080_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29Q7DefectSixFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_actual_term_alpha_floor(self) -> None:
        lemma = self.payload["pure_actual_term_lemma"]
        self.assertIn("epsilon>0", lemma["statement"])
        pruning = self.payload["epsilon_type_pruning"]
        self.assertEqual(
            (
                pruning["raw_symmetric_type_count"],
                pruning["quadratic_dimension_twelve_gap_excluded_count"],
                pruning["positive_epsilon_alpha_floor_excluded_count"],
                pruning["feasible_symmetric_type_count"],
            ),
            (31, 7, 6, 18),
        )
        self.assertIn([1] * 7, pruning["positive_epsilon_alpha_floor_excluded"])

    def test_relation_envelope_split(self) -> None:
        row = self.payload["relation_envelope"]
        self.assertEqual((row["state_count"], row["existing_cap_excluded_count"], row["open_state_count"]), (56, 43, 13))
        self.assertEqual(row["t2_upper_histogram"], {"12": 18, "13": 15, "14": 10, "15": 6, "16": 4, "17": 2, "18": 1})
        self.assertEqual(row["open_t2_upper_histogram"], {"15": 6, "16": 4, "17": 2, "18": 1})
        self.assertEqual(row["open_states_with_cubic_directness_forced_by_kappa_at_most_one"], 10)

    def test_strict_cap_gaps(self) -> None:
        rows = self.payload["relation_envelope"]["states"]
        excluded = [row for row in rows if row["excluded"]]
        self.assertTrue(excluded)
        self.assertTrue(all(row["t2_upper"] <= 14 for row in excluded))
        self.assertTrue(
            all(
                row["required_prolongation_lower_if_b_local_is_66"] > row["existing_cap"]
                for row in excluded
            )
        )

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not force such a packet from global b=34", boundary)
        self.assertIn("does not exclude b=34", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
