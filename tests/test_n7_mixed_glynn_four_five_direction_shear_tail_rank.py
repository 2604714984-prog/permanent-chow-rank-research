import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_four_five_direction_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_four_five_direction_shear", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FourFiveDirectionShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payloads = {
            4: json.loads(
                (
                    ROOT / "data" / "n7_mixed_glynn_four_direction_shear_tail_rank.json"
                ).read_text(encoding="utf-8")
            ),
            5: json.loads(
                (
                    ROOT / "data" / "n7_mixed_glynn_five_direction_shear_tail_rank.json"
                ).read_text(encoding="utf-8")
            ),
        }

    def test_complete_families(self):
        expected_counts = {4: 300, 5: 60}
        for arms, payload in self.payloads.items():
            self.assertEqual(payload["candidate_count"], expected_counts[arms])
            self.assertEqual(len(payload["rows"]), expected_counts[arms])
            self.assertEqual(
                payload["status_counts"],
                {"NONZERO_MULTIVARIATE_MONOMIAL_MINOR": expected_counts[arms]},
            )

    def test_every_exact_minor_is_one_monomial(self):
        for arms, payload in self.payloads.items():
            for row in payload["rows"]:
                self.assertEqual(row["rank_at_all_one"], 42)
                self.assertEqual(row["determinant_term_count"], 1)
                self.assertNotEqual(int(row["determinant_coefficient"]), 0)
                self.assertEqual(len(row["parameter_exponents"]), arms)
                self.assertGreater(sum(row["parameter_exponents"]), 0)

    def test_support_coverage(self):
        for arms, payload in self.payloads.items():
            self.assertEqual(
                {
                    (
                        row["shape"],
                        row["fixed"],
                        tuple(row["directions"]),
                        row["identity_count"],
                    )
                    for row in payload["rows"]
                },
                {
                    (*support, identity_count)
                    for support in self.module.supports(arms)
                    for identity_count in range(1, 6)
                },
            )


if __name__ == "__main__":
    unittest.main()
