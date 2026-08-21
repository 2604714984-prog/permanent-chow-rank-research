import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_monomial_classification.py"
    spec = importlib.util.spec_from_file_location("n7_monomial_classification", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MonomialClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT / "data" / "n7_mixed_glynn_monomial_classification.json"
            ).read_text(encoding="utf-8")
        )

    def test_all_swap_relations_have_extensions(self):
        self.assertEqual(self.row["row_pair_count"], 15)
        self.assertEqual(self.row["column_pair_count"], 21)
        self.assertEqual(self.row["swap_relation_count"], 315)
        self.assertEqual(self.row["direct_swap_relation_count"], 300)
        self.assertEqual(self.row["derived_swap_relation_count"], 15)
        self.assertEqual(len(self.row["swap_extension_witnesses"]), 300)
        self.assertEqual(len(self.row["derived_swap_relations"]), 15)

    def test_imported_exact_certificates(self):
        imported = self.row["imported_certificates"]
        self.assertEqual(
            imported["two_underlying_permutations"]["invalid_tail_rank_histogram"],
            {"42": 3595},
        )
        self.assertTrue(
            all(
                case["answer"] == "unsat"
                for case in imported["three_or_more_underlying_permutations"][
                    "cases"
                ]
            )
        )

    def test_local_and_global_classification(self):
        self.assertEqual(
            self.row["local_classification"],
            {
                "six_equal_monomial_transforms": 1,
                "every_other_six_block_assignment": 0,
            },
        )
        self.assertEqual(
            self.row["global_classification"],
            {
                "seven_equal_monomial_transforms": 7,
                "one_exceptional_block": 1,
                "every_other_seven_block_assignment": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
