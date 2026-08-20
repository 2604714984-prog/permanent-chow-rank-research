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


if __name__ == "__main__":
    unittest.main()
