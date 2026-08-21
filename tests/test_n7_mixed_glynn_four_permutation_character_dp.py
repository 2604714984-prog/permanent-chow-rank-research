import importlib.util
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_four_permutation_character_dp.py"
    spec = importlib.util.spec_from_file_location("n7_four_permutation", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FourPermutationCharacterDPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()

    def test_cover_size_and_cycle_types(self):
        self.assertEqual(len(self.module.REPRESENTATIVES), 10)
        self.assertEqual(len(self.module.COMPOSITIONS), math.comb(5, 3))
        self.assertEqual(
            self.module.CANDIDATE_COUNT, 10 * math.comb(718, 2) * math.comb(5, 3)
        )

    def test_decoder_has_four_distinct_types_and_six_blocks(self):
        for index in (0, self.module.CANDIDATE_COUNT - 1):
            types, counts = self.module.decode_candidate(index)
            self.assertEqual(len(set(types)), 4)
            self.assertEqual(sum(counts), 6)
            self.assertTrue(all(count > 0 for count in counts))

    def test_reduced_index_skips_identity_and_marked_type(self):
        for marked in range(1, 720):
            values = {
                self.module._actual_nonidentity_index(index, marked)
                for index in range(718)
            }
            self.assertEqual(values, set(range(1, 720)) - {marked})

    def test_complete_four_type_cover(self):
        row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_four_permutation_character_dp.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            row["status"],
            "EXHAUSTIVE_FOUR_PERMUTATION_CHARACTER_COLLISION_DP",
        )
        self.assertEqual(row["candidate_interval"], [0, self.module.CANDIDATE_COUNT])
        self.assertEqual(
            row["protected_character_count_histogram"],
            {"0": self.module.CANDIDATE_COUNT},
        )
        self.assertEqual(row["maximum_protected_character_count"], 0)


if __name__ == "__main__":
    unittest.main()
