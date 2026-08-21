import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_equality_packet_coupled_obstruction.py"
DATA = ROOT / "data" / "n7_equality_packet_coupled_obstruction.json"
SPEC = importlib.util.spec_from_file_location("n7_equality_packet_coupled", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class EqualityPacketCoupledObstructionTests(unittest.TestCase):
    def test_nontrivial_kernel_controls(self) -> None:
        for prime in MODULE.PRIMES:
            controls = MODULE.small_kernel_controls(prime)
            contained = controls["nontrivial_kernel_contained"]
            missing = controls["one_kernel_direction_missing"]
            self.assertTrue(contained["condition_holds"])
            self.assertEqual(contained["kernel_b_dimension"], 1)
            self.assertEqual(contained["coupling_defect"], 0)
            self.assertFalse(missing["condition_holds"])
            self.assertEqual(missing["coupling_defect"], 1)

    def test_five_plane_control(self) -> None:
        for prime in MODULE.PRIMES:
            output_map, input_map = MODULE.catalectic_maps_for_cubic_products(
                MODULE.five_plane_factors(), prime
            )
            result = MODULE.kernel_image_defect(output_map, input_map, prime)
            self.assertEqual(
                (result["rank_b"], result["rank_c"], result["rank_bc"]),
                (15, 9, 9),
            )
            self.assertTrue(result["condition_holds"])

    def test_middle_and_ambient_basis_invariance(self) -> None:
        for prime in MODULE.PRIMES:
            result = MODULE.basis_invariance_control(prime)
            self.assertEqual(
                result["original"]["coupling_defect"],
                result["transformed"]["coupling_defect"],
            )

    def test_dimension_mismatch_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.kernel_image_defect(np.eye(2), np.eye(3), MODULE.PRIMES[0])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
