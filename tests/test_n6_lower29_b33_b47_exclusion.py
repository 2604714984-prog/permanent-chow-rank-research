from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b33_b47_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b33_b47_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6079_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B33B47ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_b33_successive_shortening_levels(self) -> None:
        row = self.payload["b33_hereditary_endpoint"]
        self.assertEqual((row["initial_bounds"]["sixteen_term_literal_floor"], row["initial_bounds"]["six_term_literal_floor"]), (315, 115))
        stages = row["successive_excluded_f_levels"]
        self.assertEqual([(stage["assumed_f_A"], stage["sixteen_term_literal_floor"], stage["six_term_literal_floor"]) for stage in stages], [(50, 317, 117), (49, 318, 118), (48, 319, 119)])
        direct = row["forced_directness"]
        self.assertEqual((direct["f_A_dimension"], direct["global_residual_permanent_intersection_dimension"], direct["every_sixteen_term_literal_dimension"], direct["every_six_term_literal_dimension"]), (47, 367, 320, 120))
        self.assertEqual([(case["x"], case["required_prolongation"]) for case in row["final_x_cases"]], [(50, 470), (49, 471), (48, 472), (47, 473)])
        self.assertTrue(row["last_case_uses_N6-078"])

    def test_b47_scalar_split(self) -> None:
        row = self.payload["b47_fixed_six_endpoint"]
        self.assertEqual((row["scalar_state_count"], row["cap_excluded_state_count"]), (13, 12))
        survivor = row["unique_pre_geometry_state"]
        self.assertEqual((survivor["epsilon"], survivor["alpha"], survivor["kappa2"]), ([0] * 6, [3] * 6, 0))
        self.assertEqual((survivor["d2"], survivor["a2"], survivor["t2"], survivor["h"], survivor["required_prolongation_lower"]), (90, 75, 15, 120, 473))

    def test_n6078_interface_and_boundary(self) -> None:
        self.assertTrue(self.payload["extension_interfaces"]["N6-078"]["every_47_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"])
        self.assertEqual(self.payload["excluded_here"], [33, 47])
        self.assertEqual(self.payload["frontier_after"], list(range(34, 47)))
        boundary = self.payload["claim_boundary"]
        self.assertIn("defect-six layer is not classified", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
