import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_glynn64_mixed_catalectic_tangent.py"
SPEC = importlib.util.spec_from_file_location("n7_glynn64_mixed_catalectic_tangent", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GlynnTangentTest(unittest.TestCase):
    def test_frozen_tangent_ranks(self):
        row = MODULE.run()
        self.assertEqual(row["full_jacobian_rank"], 225)
        self.assertEqual(row["tangent_dimension"], 223)
        self.assertEqual(row["coefficient_projection_dimension"], 64)
        full = row["full_waring_system"]
        self.assertTrue(full["identity_residual_is_zero"])
        self.assertEqual(full["point_jacobian_rank"], 379)
        self.assertEqual(full["coefficient_jacobian_rank"], 64)
        self.assertEqual(full["full_jacobian_rank"], 442)
        self.assertEqual(full["tangent_dimension"], 6)
        self.assertEqual(full["coefficient_projection_dimension"], 1)


if __name__ == "__main__":
    unittest.main()
