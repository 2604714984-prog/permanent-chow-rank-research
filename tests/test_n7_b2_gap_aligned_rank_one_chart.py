import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_gap_aligned_rank_one_chart.py"
DATA = ROOT / "data" / "n7_b2_gap_aligned_rank_one_chart.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_gap_aligned_rank_one_chart", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class GapAlignedRankOneChartTests(unittest.TestCase):
    def test_chart_extrema(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(payload["extrema"]["shared_row_01_02"], {
            "maximum_delta_C_minus_delta_BC": 9,
            "maximum_repair_score": 25,
            "required_repair_score": 45,
            "minimum_new_defect": 20,
        })
        self.assertEqual(payload["extrema"]["disjoint_01_23"], {
            "maximum_delta_C_minus_delta_BC": 12,
            "maximum_repair_score": 31,
            "required_repair_score": 47,
            "minimum_new_defect": 16,
        })

    def test_no_operator_repair(self) -> None:
        self.assertTrue(all(not row["operator_gap_repaired"] for row in MODULE.build_payload()["rows"]))

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
