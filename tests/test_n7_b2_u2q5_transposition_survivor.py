import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_u2q5_transposition_survivor.py"
DATA = ROOT / "data" / "n7_b2_u2q5_transposition_survivor.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_u2q5_transposition_survivor", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class U2Q5TranspositionSurvivorTests(unittest.TestCase):
    def test_exact_polynomial_identity(self) -> None:
        factors = MODULE.transposition_survivor_factors()
        self.assertEqual(MODULE.product_column(factors[0]) + MODULE.product_column(factors[1]), MODULE.target_column())
        self.assertEqual(MODULE.u_degree_histogram(MODULE.target_column()), {0: 1, 1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0})

    def test_minimal_complex_satisfies_sylvester_equality(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(payload["minimal_complex"], {
            "middle_dimension": 70,
            "rank_B": 65,
            "rank_C": 60,
            "rank_BC": 55,
            "kernel_image_defect": 0,
            "sylvester_equality_holds": True,
        })

    def test_u2_bilinear_isotropic_pair(self) -> None:
        self.assertEqual(MODULE.bilinear_residual_form((1, 0), (1, 0)), 0)
        self.assertEqual(MODULE.bilinear_residual_form((-1, 1), (-1, 1)), 0)
        self.assertEqual(MODULE.bilinear_residual_form((1, 0), (-1, 1)), 1)

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
