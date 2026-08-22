import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b64_common_quotient_rigidity.py"


class N6B64CommonQuotientRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "audit.json"
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--json", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            cls.stdout = completed.stdout
            cls.payload = json.loads(output.read_text(encoding="utf-8"))

    def test_coordinate_signatures_are_injective(self) -> None:
        self.assertEqual(self.payload["coordinate_extremal_planes"], 600)
        self.assertEqual(
            self.payload["coordinate_orientation_count"],
            {"K_2_3": 300, "K_3_2": 300},
        )
        self.assertEqual(self.payload["distinct_coordinate_W12_signatures"], 600)
        self.assertEqual(
            self.payload["coordinate_signature_collision_histogram"], {"1": 600}
        )
        self.assertEqual(self.payload["cross_orientation_coordinate_collisions"], 0)

    def test_quotient_dimension(self) -> None:
        self.assertEqual(self.payload["quotient_dimension"], 441)

    def test_fixed_quotient_tangent_rank(self) -> None:
        tangent = self.payload["fixed_W_tangent"]
        self.assertEqual(tangent["integer_matrix_shape"], [897, 216])
        self.assertEqual(tangent["prime"], 1_000_003)
        self.assertEqual(tangent["modular_rank"], 210)
        self.assertEqual(tangent["kernel_dimension"], 6)
        self.assertEqual(tangent["selected_minor_size"], 210)
        self.assertNotEqual(tangent["selected_minor_determinant_mod_prime"], 0)
        self.assertEqual(
            len(tangent["selected_minor_columns"]), tangent["selected_minor_size"]
        )
        self.assertEqual(
            len(tangent["selected_minor_row_keys"]), tangent["selected_minor_size"]
        )

    def test_scaling_kernel_is_disjoint_from_pivots(self) -> None:
        tangent = self.payload["fixed_W_tangent"]
        scaling = tangent["explicit_factor_scaling_columns"]
        self.assertEqual(len(scaling), 6)
        self.assertEqual(len(set(scaling)), 6)
        self.assertTrue(set(scaling).isdisjoint(tangent["selected_minor_columns"]))

    def test_claim_boundary_is_fail_closed(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude noncoordinate b=64", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=27", boundary)

    def test_pass_marker(self) -> None:
        self.assertIn("N6_B64_COMMON_QUOTIENT_RIGIDITY_PASS", self.stdout)


if __name__ == "__main__":
    unittest.main()
