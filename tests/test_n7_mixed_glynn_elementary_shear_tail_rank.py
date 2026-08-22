import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_elementary_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_elementary_shear", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ElementaryShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_elementary_shear_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_complete_candidate_family(self):
        self.assertEqual(self.row["candidate_count"], 150)
        self.assertEqual(self.row["candidate_count"], self.module.CANDIDATE_COUNT)
        self.assertEqual(len(self.row["rows"]), 150)
        self.assertEqual(
            self.row["status_counts"], {"NONZERO_MONOMIAL_MINOR": 150}
        )

    def test_every_minor_is_a_nonzero_power_of_parameter(self):
        for row in self.row["rows"]:
            self.assertEqual(row["rank_at_one"], 42)
            self.assertEqual(row["determinant_term_count"], 1)
            self.assertNotEqual(int(row["determinant_coefficient"]), 0)
            self.assertGreater(row["determinant_parameter_exponent"], 0)
            self.assertEqual(
                row["determinant_degree"], row["determinant_parameter_exponent"]
            )

    def test_identity_control_and_coverage(self):
        self.assertEqual(self.row["identity_control_invalid_tail_rank"], 41)
        self.assertEqual(
            {
                (row["target"], row["source"], row["identity_count"])
                for row in self.row["rows"]
            },
            {
                (target, source, identity_count)
                for target, source in self.module.DIRECTIONS
                for identity_count in range(1, 6)
            },
        )


if __name__ == "__main__":
    unittest.main()
