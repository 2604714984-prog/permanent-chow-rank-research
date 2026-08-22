import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_column_uniform_mixed_catalectic.py"
SPEC = importlib.util.spec_from_file_location("n7_column_uniform_mixed_catalectic", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MixedCatalecticTest(unittest.TestCase):
    def test_glynn_positive_control(self):
        self.assertEqual(
            MODULE.glynn_control(),
            {
                "point_count": 64,
                "coefficient_rank": 64,
                "augmented_rank": 64,
                "target_increment": 0,
            },
        )

    def test_fixed_line_packet_is_excluded(self):
        row = MODULE.trial(20460815, 2)
        self.assertEqual(row["coefficient_rank"], 49)
        self.assertEqual(row["augmented_rank"], 50)
        self.assertEqual(row["target_increment"], 1)


if __name__ == "__main__":
    unittest.main()
