import importlib.util
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_protected_character_smt.py"
    spec = importlib.util.spec_from_file_location("n7_protected_smt", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProtectedCharacterSMTTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.row = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_protected_character_explicit_smt.json"
            ).read_text(encoding="utf-8")
        )

    def test_complete_explicit_unsat_certificate(self):
        self.assertEqual(
            self.row["status"],
            "EXACT_UNSAT_PROTECTED_CHARACTER_AT_LEAST_THREE_TYPES",
        )
        self.assertEqual(self.row["collision_scope"], "all_explicit")
        self.assertEqual(
            [(case["case"], case["answer"]) for case in self.row["cases"]],
            [("nonzero_columns", "unsat"), ("zero_column", "unsat")],
        )

    def test_invalid_assignment_count(self):
        expected = 7**6 - math.perm(7, 6)
        self.assertEqual(expected, 112_609)
        self.assertTrue(
            all(
                case["invalid_assignment_count"] == expected
                for case in self.row["cases"]
            )
        )

    def test_two_valid_matching_normal_forms_are_distinct(self):
        nonzero = self.module.build_formula("nonzero_columns", "valid_pair_changes")
        with_zero = self.module.build_formula("zero_column", "valid_pair_changes")
        self.assertIn("(define-fun target", nonzero)
        self.assertIn("(define-fun target", with_zero)
        self.assertNotEqual(nonzero, with_zero)


if __name__ == "__main__":
    unittest.main()
