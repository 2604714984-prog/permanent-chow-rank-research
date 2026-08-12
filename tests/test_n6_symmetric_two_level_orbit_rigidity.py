from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_symmetric_two_level_orbit_rigidity.py"


def load_module():
    spec = spec_from_file_location("n6_symmetric_two_level_orbit_rigidity", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class SymmetricTwoLevelOrbitRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_missing_types_are_separated_exactly(self) -> None:
        rows = self.payload["missing_type_certificates"]
        self.assertEqual([row["missing_k"] for row in rows], [1, 2, 3])
        for row in rows:
            self.assertEqual(row["target_value"], 1)
            self.assertTrue(
                all(value == "0" for value in row["annihilated_polynomials"].values())
            )

    def test_orbit_cost_forces_unique_length_31_shape(self) -> None:
        costs = self.payload["reduced_orbit_costs"]
        self.assertEqual((costs["k1_t_not_1"], costs["k2_t_not_1"]), (6, 15))
        self.assertEqual((costs["k3_generic"], costs["k3_t_minus_1"]), (20, 10))
        self.assertIn("total 31", self.payload["unique_sub_32_shape"])

    def test_three_branch_determinants(self) -> None:
        result = self.payload["length_31_exclusion"]
        self.assertEqual(
            result["generic_minor_determinant"],
            "4*(a - 1)**2*(a + 1)*(b - 1)**4*(b + 1)**2",
        )
        self.assertEqual(
            result["a_equals_minus_one_minor_determinant"],
            "128*(b - 1)**2*(b + 1)**3",
        )
        self.assertEqual(
            result["b_equals_minus_one_minor_determinant"],
            "8*(a - 1)**2*(a + 1)",
        )
        self.assertEqual(result["branch_conclusion_under_a_not_1_b_not_1"], "a=b=-1")

    def test_final_functional_is_a_contradiction(self) -> None:
        result = self.payload["length_31_exclusion"]
        self.assertEqual(result["final_orbit_values"], {"1": "0", "2": "0", "3": "0"})
        self.assertEqual(result["final_target_value"], 1)

    def test_projective_boundary_is_excluded(self) -> None:
        result = self.payload["projective_boundary_exclusion"]
        self.assertEqual(
            result["a_infinity_force_determinant"],
            "-8*(b - 1)**2*(b + 1)**3",
        )
        self.assertEqual(result["a_infinity_contradiction_value_at_b_minus_1"], -8)
        self.assertEqual(result["b_infinity_force_determinant"], "-60*(a + 1)**2")
        self.assertEqual(result["b_infinity_contradiction_value_at_a_minus_1"], -64)
        self.assertEqual(result["both_infinity_determinant"], 24)

    def test_redundant_groebner_basis_is_one_over_qq(self) -> None:
        replay = self.payload["redundant_groebner_replay"]
        self.assertEqual(replay["coefficient_field"], "QQ")
        self.assertEqual(len(replay["input_equations"]), 11)
        self.assertEqual(replay["reduced_basis"], ["1"])

    def test_glynn_endpoint_has_exactly_32_terms(self) -> None:
        endpoint = self.payload["glynn_endpoint"]
        self.assertTrue(endpoint["coefficient_vector_verified"])
        self.assertEqual(endpoint["distinct_chow_terms"], 32)
        self.assertEqual(self.payload["restricted_family_minimum"], 32)

    def test_claim_boundary_is_restricted(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude arbitrary non-sign", boundary)
        self.assertIn("26 <= ChowRank(perm_6) <= 32", boundary)

    def test_checked_in_json_is_exact_replay(self) -> None:
        stored = json.loads(
            (ROOT / "data" / "n6_symmetric_two_level_orbit_rigidity.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
