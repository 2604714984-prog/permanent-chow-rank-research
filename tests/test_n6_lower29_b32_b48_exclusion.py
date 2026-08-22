from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b32_b48_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b32_b48_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6077_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B32B48ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_b32_three_level_hereditary_chain(self) -> None:
        row = self.payload["b32_hereditary_endpoint"]
        first = row["stage1_initial_bounds"]
        self.assertEqual(
            (first["initial_x_A_upper"], first["initial_sixteen_term_literal_floor"], first["initial_six_term_literal_floor"]),
            (52, 316, 116),
        )
        second = row["stage2_exclude_some_f_50"]
        self.assertEqual((second["sixteen_term_literal_floor"], second["six_term_literal_floor"], second["required_prolongation_lower"]), (318, 118, 468))
        third = row["stage3_exclude_some_f_49"]
        self.assertEqual((third["sixteen_term_literal_floor"], third["nonfull_sixteen_term_cap"]), (319, 318))
        self.assertEqual([(case["x"], case["required_prolongation_lower"]) for case in third["cases"]], [(50, 469), (49, 470)])
        fourth = row["stage4_all_f_48_and_literal_directness"]
        self.assertEqual((fourth["f_A_dimension"], fourth["global_residual_permanent_intersection_dimension"], fourth["every_sixteen_term_literal_dimension"], fourth["every_six_term_literal_dimension"]), (48, 368, 320, 120))
        final = row["stage5_exclude_x_50_49_48"]
        self.assertEqual([(case["x"], case["required_prolongation"]) for case in final["cases"]], [(50, 470), (49, 471), (48, 472)])
        self.assertTrue(final["last_case_uses_N6-076"])

    def test_b48_thirteen_states_split(self) -> None:
        row = self.payload["b48_fixed_six_endpoint"]
        self.assertEqual((row["scalar_state_count"], row["cap_excluded_state_count"]), (13, 12))
        survivor = row["unique_pre_geometry_state"]
        self.assertEqual((survivor["epsilon"], survivor["alpha"], survivor["kappa2"]), ([0] * 6, [3] * 6, 0))
        self.assertEqual((survivor["d2"], survivor["a2"], survivor["t2"], survivor["h"]), (90, 75, 15, 120))
        self.assertEqual(survivor["required_prolongation_lower"], 472)

    def test_extension_interfaces_and_route(self) -> None:
        self.assertTrue(self.payload["n6076_interface"]["every_48_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"])
        self.assertTrue(self.payload["n6073_interface"]["every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"])
        route = " ".join(self.payload["shared_geometric_route"])
        for name in ("N6-076", "N6-064", "N6-069", "N6-072"):
            self.assertIn(name, route)

    def test_frontier_and_boundary(self) -> None:
        self.assertEqual(self.payload["excluded_here"], [32, 48])
        self.assertEqual(self.payload["frontier_after"], list(range(33, 48)))
        boundary = self.payload["claim_boundary"]
        self.assertIn("b=33 and b=47 remains open", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
