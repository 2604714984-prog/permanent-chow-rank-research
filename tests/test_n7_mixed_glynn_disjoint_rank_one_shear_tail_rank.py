import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SIZE_PAIRS = ((2, 3), (3, 2), (2, 4), (4, 2), (3, 3))


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_disjoint_rank_one_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_disjoint_rank_one_shear", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DisjointRankOneShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payloads = {
            pair: json.loads(
                (
                    ROOT
                    / "data"
                    / f"n7_mixed_glynn_disjoint_{pair[0]}{pair[1]}_rank_one_shear_tail_rank.json"
                ).read_text(encoding="utf-8")
            )
            for pair in SIZE_PAIRS
        }

    def test_complete_families(self):
        expected_counts = {(2, 3): 300, (3, 2): 300, (2, 4): 75, (4, 2): 75, (3, 3): 100}
        for pair, payload in self.payloads.items():
            self.assertEqual(payload["candidate_count"], expected_counts[pair])
            self.assertEqual(len(payload["rows"]), expected_counts[pair])
            self.assertEqual(
                payload["status_counts"],
                {"NONZERO_MULTIVARIATE_MONOMIAL_MINOR": expected_counts[pair]},
            )

    def test_every_exact_minor_is_one_monomial(self):
        for pair, payload in self.payloads.items():
            parameter_count = sum(pair) - 1
            for row in payload["rows"]:
                self.assertEqual(row["rank_at_all_one"], 42)
                self.assertEqual(row["determinant_term_count"], 1)
                self.assertNotEqual(int(row["determinant_coefficient"]), 0)
                self.assertEqual(len(row["parameter_exponents"]), parameter_count)
                self.assertGreater(sum(row["parameter_exponents"]), 0)

    def test_support_coverage(self):
        for pair, payload in self.payloads.items():
            self.assertEqual(
                {
                    (
                        tuple(row["left_support"]),
                        tuple(row["right_support"]),
                        row["identity_count"],
                    )
                    for row in payload["rows"]
                },
                {
                    (*support, identity_count)
                    for support in self.module.supports(*pair)
                    for identity_count in range(1, 6)
                },
            )


if __name__ == "__main__":
    unittest.main()
