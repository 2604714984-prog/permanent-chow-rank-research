import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script_from_name(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location("n7_multiblock_sign", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_script():
    return load_script_from_name("n7_mixed_glynn_multiblock_sign_search.py")


class MixedGlynnMultiblockSignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b2 = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_multiblock_sign_b2.json").read_text()
        )
        cls.b3 = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_multiblock_sign_b3.json").read_text()
        )
        cls.two_type = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_two_type_sign_search.json").read_text()
        )
        cls.three_type = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_three_type_sign_search.json").read_text()
        )
        cls.local = {
            type_count: json.loads(
                (
                    ROOT
                    / "data"
                    / f"n7_mixed_glynn_local_sign_t{type_count}.json"
                ).read_text()
            )
            for type_count in range(1, 7)
        }

    def test_two_block_exhaustion(self):
        self.assertEqual(self.b2["candidate_count"], 64**2)
        self.assertEqual(self.b2["degree_six_rank_histogram"], {"336": 64**2})
        self.assertEqual(
            self.b2["intersection_histogram"], {"0": 63**2, "1": 2 * 63, "7": 1}
        )
        self.assertEqual(self.b2["maximizer_count"], 1)

    def test_three_block_exhaustion(self):
        self.assertEqual(self.b3["candidate_count"], 64**3)
        self.assertEqual(self.b3["degree_six_rank_histogram"], {"336": 64**3})
        self.assertEqual(
            self.b3["intersection_histogram"],
            {"0": 64**3 - 3 * 63 - 1, "1": 3 * 63, "7": 1},
        )
        self.assertEqual(self.b3["maximizer_count"], 1)

    def test_sign_index_is_base_64_and_identity_is_63(self):
        module = load_script()
        signs = module.signs_from_index(63 + 64 * 0, 2)
        self.assertTrue((signs[0] == 1).all())
        self.assertTrue((signs[1] == -1).all())
        with self.assertRaises(ValueError):
            module.signs_from_index(64**2, 2)

    def test_all_two_type_packets(self):
        self.assertEqual(self.two_type["candidate_count"], 12_160)
        self.assertEqual(
            self.two_type["intersection_histogram"],
            {"0": 8_064, "1": 4_032, "7": 64},
        )
        self.assertEqual(self.two_type["maximizer_count"], 64)
        self.assertEqual(
            self.two_type["degree_six_rank_histogram"], {"336": 12_160}
        )

    def test_all_normalized_three_type_packets(self):
        self.assertEqual(self.three_type["candidate_count"], 29_295)
        self.assertEqual(self.three_type["intersection_histogram"], {"0": 29_295})
        self.assertEqual(self.three_type["maximum_target_intersection"], 0)
        self.assertEqual(
            self.three_type["degree_six_rank_histogram"], {"336": 29_295}
        )

    def test_type_representative_counts(self):
        two = load_script_from_name("n7_mixed_glynn_two_type_sign_search.py")
        three = load_script_from_name("n7_mixed_glynn_three_type_sign_search.py")
        self.assertEqual(len(two.candidate_rows()), 12_160)
        self.assertEqual(len(three.candidate_rows()), 29_295)

    def test_complete_local_sign_multiset_exhaustion(self):
        expected_counts = [1, 315, 19_530, 397_110, 2_978_325, 7_028_847]
        for type_count, expected in enumerate(expected_counts, start=1):
            row = self.local[type_count]
            self.assertEqual(row["candidate_count"], expected)
            self.assertEqual(row["local_derivative_rank_histogram"], {"42": expected})
            expected_intersection = {"1": 1} if type_count == 1 else {"0": expected}
            self.assertEqual(
                row["local_target_intersection_histogram"], expected_intersection
            )

    def test_local_candidate_decoder_boundaries(self):
        module = load_script_from_name("n7_mixed_glynn_local_sign_multiset_search.py")
        self.assertEqual(module.unrank_combination(63, 5, 0), (0, 1, 2, 3, 4))
        self.assertEqual(
            module.unrank_combination(63, 5, 7_028_846), (58, 59, 60, 61, 62)
        )


if __name__ == "__main__":
    unittest.main()
