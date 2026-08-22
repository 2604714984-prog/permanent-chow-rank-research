import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_overlapping_22", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Overlapping22NilpotentShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_complete_family(self):
        self.assertEqual(self.row["support_count"], 15)
        self.assertEqual(self.row["candidate_count"], 75)
        self.assertEqual(self.row["candidate_count"], self.module.CANDIDATE_COUNT)
        self.assertEqual(len(self.row["rows"]), 75)
        self.assertEqual(
            self.row["status_counts"],
            {"DENSE_TORUS_COVERED_BY_EXACT_MINORS": 75},
        )

    def test_exact_minor_gcd_has_only_scale_axis(self):
        minor_count_histogram = {}
        for row in self.row["rows"]:
            minor_count_histogram[row["minor_count"]] = (
                minor_count_histogram.get(row["minor_count"], 0) + 1
            )
            self.assertIn(row["minor_count"], (1, 2))
            self.assertEqual(len(row["gcd_exponents"]), 2)
            self.assertEqual(row["gcd_exponents"][0], 0)
            self.assertGreater(row["gcd_exponents"][1], 0)
            for minor in row["minors"]:
                self.assertGreater(minor["determinant_term_count"], 0)
        self.assertEqual(minor_count_histogram, {1: 19, 2: 56})

    def test_support_coverage(self):
        self.assertEqual(
            {
                (tuple(row["support"]), row["identity_count"])
                for row in self.row["rows"]
            },
            {
                (support, identity_count)
                for support in self.module.SUPPORTS
                for identity_count in range(1, 6)
            },
        )


if __name__ == "__main__":
    unittest.main()
