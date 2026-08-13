import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k34_special_d_fano_exclusion.py"
SPEC = importlib.util.spec_from_file_location("n6_k34_special_d_fano_exclusion", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class SpecialDFanoExclusionTest(unittest.TestCase):
    def test_frozen_certificate(self):
        expected = json.loads(
            (ROOT / "data" / "n6_k34_special_d_fano_exclusion.json").read_text(encoding="utf-8")
        )
        self.assertEqual(MODULE.certificate(), expected)

    def test_unique_fixed_support_and_zero_tangent(self):
        result = MODULE.certificate()
        self.assertEqual(result["fixed_support_scan"]["compatible_six_supports"], [list(MODULE.L0)])
        self.assertEqual(result["tangent_certificate"]["certified_tangent_dimension"], 0)


if __name__ == "__main__":
    unittest.main()
