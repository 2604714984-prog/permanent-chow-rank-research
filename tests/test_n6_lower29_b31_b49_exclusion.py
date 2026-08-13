from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b31_b49_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b31_b49_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_lower29_b31_b49", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B31B49ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_b31_two_level_hereditary_chain(self) -> None:
        row = self.payload["b31_hereditary_endpoint"]
        stage1 = row["stage1_initial_bounds"]
        self.assertEqual(
            (
                stage1["global_residual_permanent_intersection_floor"],
                stage1["initial_x_A_upper"],
                stage1["initial_sixteen_term_literal_floor"],
                stage1["initial_six_term_literal_floor"],
            ),
            (369, 52, 317, 117),
        )
        stage2 = row["stage2_exclude_x_51_52"]
        self.assertEqual(
            [(case["x"], case["required_prolongation_lower"], case["common_W12_cap"]) for case in stage2["cases"]],
            [(51, 466, 436), (52, 465, 436)],
        )
        self.assertEqual(stage2["x_A_upper_after_stage"], 50)

        stage3 = row["stage3_exclude_some_f_50"]
        self.assertEqual(
            (
                stage3["sixteen_term_literal_floor"],
                stage3["N6_031_nonfull_sixteen_term_cap"],
                stage3["six_term_literal_floor"],
                stage3["profile"]["required_prolongation_lower"],
            ),
            (319, 318, 119, 469),
        )
        self.assertEqual(stage3["profile"]["forced_quadratic_state"]["t2"], 15)

        stage4 = row["stage4_all_f_49_and_literal_directness"]
        self.assertEqual(
            (
                stage4["f_A_dimension"],
                stage4["global_residual_permanent_intersection_dimension"],
                stage4["every_sixteen_term_literal_dimension"],
                stage4["every_six_term_literal_dimension"],
            ),
            (49, 369, 320, 120),
        )
        self.assertTrue(stage4["every_sixteen_term_family_literal_direct"])

        stage5 = row["stage5_exclude_x_50_then_force_x_49"]
        self.assertEqual(
            (
                stage5["x_50_required_prolongation"],
                stage5["forced_x_A"],
                stage5["x_49_required_prolongation"],
            ),
            (470, 49, 471),
        )
        self.assertEqual(stage5["x_49_profile"]["forced_quadratic_state"]["a2"], 75)

    def test_b49_thirteen_states_split_twelve_plus_one(self) -> None:
        row = self.payload["b49_fixed_six_endpoint"]
        self.assertEqual(row["scalar_state_count"], 13)
        self.assertEqual(row["cap_excluded_state_count"], 12)
        survivor = row["unique_pre_geometry_state"]
        self.assertEqual((survivor["epsilon"], survivor["alpha"], survivor["kappa2"]), ([0] * 6, [3] * 6, 0))
        self.assertEqual((survivor["d2"], survivor["a2"], survivor["t2"], survivor["h"]), (90, 75, 15, 120))
        self.assertEqual(survivor["alpha_at_most_two_subcase_cap"], 458)
        self.assertGreater(survivor["alpha_at_most_two_subcase_strict_gap"], 0)

    def test_n6073_and_shared_route(self) -> None:
        interface = self.payload["n6073_interface"]
        self.assertTrue(interface["every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"])
        self.assertEqual(interface["second_shadow_dimension"], 23)
        self.assertTrue(interface["second_shadow_is_a_projective_flag_hook"])
        route = " ".join(self.payload["shared_geometric_route"])
        for name in ("N6-073", "N6-069", "N6-061", "N6-059", "N6-072"):
            self.assertIn(name, route)

    def test_frontier_and_boundary(self) -> None:
        self.assertEqual(self.payload["excluded_here"], [31, 49])
        self.assertEqual(self.payload["frontier_after"], list(range(32, 49)))
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude b=32 or b=48", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
