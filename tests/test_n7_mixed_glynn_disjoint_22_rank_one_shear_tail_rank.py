import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_disjoint_22_shear", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Disjoint22RankOneShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_complete_family(self):
        self.assertEqual(self.row["support_count"], 90)
        self.assertEqual(self.row["candidate_count"], 450)
        self.assertEqual(self.row["candidate_count"], self.module.CANDIDATE_COUNT)
        self.assertEqual(len(self.row["rows"]), 450)
        self.assertEqual(
            self.row["status_counts"],
            {"NONZERO_TRIVARIATE_MONOMIAL_MINOR": 450},
        )

    def test_every_exact_minor_is_one_monomial(self):
        for row in self.row["rows"]:
            self.assertEqual(row["rank_at_all_one"], 42)
            self.assertEqual(row["determinant_term_count"], 1)
            self.assertNotEqual(int(row["determinant_coefficient"]), 0)
            self.assertEqual(len(row["parameter_exponents"]), 3)
            self.assertGreater(sum(row["parameter_exponents"]), 0)

    def test_support_coverage(self):
        self.assertEqual(
            {
                (
                    tuple(row["left_support"]),
                    tuple(row["right_support"]),
                    row["identity_count"],
                )
                for row in self.row["rows"]
            },
            {
                (*support, identity_count)
                for support in self.module.SUPPORTS
                for identity_count in range(1, 6)
            },
        )


if __name__ == "__main__":
    unittest.main()
