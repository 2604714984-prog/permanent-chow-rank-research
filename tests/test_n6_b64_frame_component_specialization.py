from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b64_frame_component_specialization.py"
FROZEN = ROOT / "data" / "n6_b64_frame_component_specialization.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b64_specialization", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6B64FrameComponentSpecializationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_complete_hall_classification(self) -> None:
        component = self.payload["component_classification"]
        self.assertEqual(component["ordered_component_assignments"], 15_625)
        self.assertEqual(component["admissible_ordered_assignments"], 14_810)
        self.assertEqual(component["inadmissible_ordered_assignments"], 815)
        self.assertEqual(component["unordered_component_count_vectors"], 210)
        self.assertEqual(component["admissible_component_count_vectors"], 153)
        self.assertEqual(component["inadmissible_component_count_vectors"], 57)

    def test_every_inadmissible_type_has_strict_hall_witness(self) -> None:
        table = self.payload["component_classification"][
            "component_count_vector_table"
        ]
        for row in table:
            witness = row["hall_deficiency_witness"]
            if row["admissible"]:
                self.assertIsNone(witness)
                self.assertGreater(row["perfect_matching_count"], 0)
            else:
                self.assertIsNotNone(witness)
                self.assertEqual(row["perfect_matching_count"], 0)
                self.assertLess(witness["neighbor_size"], witness["subset_size"])

    def test_matching_histogram(self) -> None:
        histogram = self.payload["component_classification"][
            "perfect_matching_histogram"
        ]
        self.assertEqual(
            histogram,
            {
                "0": 815,
                "12": 1320,
                "18": 720,
                "24": 1890,
                "32": 4590,
                "36": 1460,
                "44": 540,
                "48": 2700,
                "56": 1080,
                "72": 420,
                "80": 90,
            },
        )
        self.assertEqual(sum(histogram.values()), 15_625)

    def test_noncoordinate_exact_tangent_certificate(self) -> None:
        tangent = self.payload["noncoordinate_tangent_certificate"]
        self.assertEqual(
            tangent["dual_frame_pairing_matrix"],
            [[int(row == column) for column in range(6)] for row in range(6)],
        )
        self.assertEqual(tangent["quotient_rank_mod_prime"], 12)
        self.assertEqual(tangent["quotient_rref_support_size"], 14)
        self.assertEqual(len(tangent["quotient_square_axes_in_support"]), 2)
        self.assertEqual(tangent["fixed_W_tangent_matrix_shape"], [1243, 216])
        self.assertEqual(tangent["fixed_W_tangent_rank_mod_prime"], 210)
        self.assertEqual(tangent["fixed_W_tangent_kernel_dimension"], 6)
        self.assertEqual(tangent["explicit_scaling_kernel_dimension"], 6)
        self.assertEqual(tangent["selected_minor_size"], 210)
        self.assertEqual(tangent["selected_minor_determinant_mod_prime"], 16)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("not a global radicial theorem", boundary)
        self.assertIn("does not exclude b=64", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=27", boundary)


if __name__ == "__main__":
    unittest.main()
