from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_middle_third_koszul_rank.py"
FROZEN = ROOT / "data" / "n6_middle_third_koszul_rank.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "n6_middle_third_koszul_rank",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6MiddleThirdKoszulRankTests(unittest.TestCase):
    def test_representative_cycle_and_nullity(self) -> None:
        self.assertEqual(
            AUDIT.exact_representative_audit(),
            {
                "column_count": 120,
                "row_support_count": 540,
                "all_ones_cycle_nonzero_entries": 0,
                "exact_rational_rank": 119,
                "exact_nullity": 1,
            },
        )

    def test_exact_rank_chain_and_margin(self) -> None:
        payload = AUDIT.build_payload(False)
        self.assertEqual(payload["explicit_homology_dimension_lower"], 40)
        self.assertEqual(payload["characteristic_zero_exact_rank"], 2_715_505)
        self.assertEqual(payload["single_chow_term_exact_rank"], 133_545)
        self.assertEqual(payload["margin_above_twenty_term_cap"], 44_605)
        self.assertEqual(
            payload["hypothetical_six_term_two_sided_overlap_defect_lower"],
            44_605,
        )
        self.assertFalse(payload["heavy_replay_performed"])

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        actual = json.loads(json.dumps(AUDIT.build_payload(False)))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
