import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SIZE_PAIRS = (
    (2, 4),
    (3, 3),
    (4, 2),
    (2, 5),
    (3, 4),
    (4, 3),
    (5, 2),
)


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_overlap_two_rank_one_shear_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_overlap_two", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapTwoRankOneShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payloads = {
            pair: json.loads(
                (
                    ROOT
                    / "data"
                    / f"n7_mixed_glynn_overlap_two_{pair[0]}{pair[1]}_nilpotent_shear_tail_rank.json"
                ).read_text(encoding="utf-8")
            )
            for pair in SIZE_PAIRS
        }

    def test_complete_families(self):
        expected_counts = {
            (2, 4): 450,
            (3, 3): 900,
            (4, 2): 450,
            (2, 5): 300,
            (3, 4): 900,
            (4, 3): 900,
            (5, 2): 300,
        }
        for pair, payload in self.payloads.items():
            self.assertEqual(payload["candidate_count"], expected_counts[pair])
            self.assertEqual(len(payload["rows"]), expected_counts[pair])
            self.assertEqual(
                payload["status_counts"],
                {"DENSE_TORUS_COVERED_BY_EXACT_MINORS": expected_counts[pair]},
            )

    def test_exact_minor_gcd_cover(self):
        expected_histograms = {
            (2, 4): {1: 207, 2: 243},
            (3, 3): {1: 567, 2: 333},
            (4, 2): {1: 294, 2: 156},
            (2, 5): {1: 229, 2: 71},
            (3, 4): {1: 900},
            (4, 3): {1: 900},
            (5, 2): {1: 300},
        }
        for pair, payload in self.payloads.items():
            histogram = {}
            for row in payload["rows"]:
                histogram[row["minor_count"]] = histogram.get(row["minor_count"], 0) + 1
                self.assertEqual(row["gcd_term_count"], 1)
                self.assertEqual(len(row["gcd_exponents"]), sum(pair) - 2)
                self.assertGreater(sum(row["gcd_exponents"]), 0)
            self.assertEqual(histogram, expected_histograms[pair])

    def test_support_coverage(self):
        for pair, payload in self.payloads.items():
            self.assertEqual(
                {
                    (
                        tuple(row["core_support"]),
                        tuple(row["left_extra_support"]),
                        tuple(row["right_extra_support"]),
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
