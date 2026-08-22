import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_two_permutation_tail_rank.py"
    spec = importlib.util.spec_from_file_location("n7_two_permutation_tail", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TwoPermutationTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_two_permutation_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_complete_two_permutation_exhaustion(self):
        self.assertEqual(self.row["candidate_count"], 719 * 5)
        self.assertEqual(self.row["candidate_count"], self.module.CANDIDATE_COUNT)
        self.assertEqual(
            self.row["invalid_tail_rank_histogram"],
            {"42": self.module.CANDIDATE_COUNT},
        )

    def test_tail_characters_and_identity_control(self):
        self.assertEqual(self.row["tail_count"], 42)
        self.assertEqual(self.row["distinct_tail_character_count"], 42)
        self.assertEqual(self.row["full_walsh_feature_rank"], 42)
        self.assertEqual(self.row["identity_packet_invalid_tail_rank"], 41)
        self.assertEqual(self.row["identity_kernel_dimension"], 1)
        self.assertEqual(len(self.row["identity_kernel_target_profile"]), 7)
        self.assertEqual(self.row["identity_kernel_target_support"], [0, 1])
        self.assertTrue(
            all(self.row["identity_kernel_target_profile"][column] for column in (0, 1))
        )

    def test_every_cycle_type_has_full_rank(self):
        self.assertEqual(len(self.row["cycle_type_rank_histogram"]), 10)
        self.assertTrue(
            all(
                set(histogram) == {"42"}
                for histogram in self.row["cycle_type_rank_histogram"].values()
            )
        )


if __name__ == "__main__":
    unittest.main()
