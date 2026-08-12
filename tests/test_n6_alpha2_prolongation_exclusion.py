from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha2_prolongation_exclusion.py"
FROZEN = ROOT / "data" / "n6_alpha2_prolongation_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_alpha2", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Alpha2ProlongationExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_complete_support_orbits(self) -> None:
        self.assertEqual(self.payload["one_rectangle_support_orbit_count"], 12)
        self.assertEqual(self.payload["one_rectangle_marked_orbit_input_count"], 488)
        self.assertEqual(self.payload["one_rectangle_marked_support_count"], 109_800)
        self.assertEqual(
            sum(row["marked_support_count"] for row in self.payload["one_rectangle_support_rows"]),
            488,
        )

    def test_complete_fixed_A_enumeration(self) -> None:
        for row in self.payload["one_rectangle_support_rows"]:
            self.assertEqual(row["local_quotient_axis_count"], 20)
            self.assertEqual(row["fixed_A_count"], 38_760)
            self.assertEqual(
                sum(row["upper_bound_histogram"].values()), 38_760
            )

    def test_strict_cap_and_state_contradiction(self) -> None:
        self.assertEqual(
            self.payload["one_rectangle_universal_prolongation_cap"], 453
        )
        self.assertEqual(
            self.payload["three_rectangle_extremal_t14_cap_from_N6_047"], 448
        )
        self.assertEqual(
            self.payload["three_rectangle_limit_intersection_dimensions_covered"],
            [1, 2, 3],
        )
        state = self.payload["all_alpha2_state_certificate"]
        self.assertEqual(state["state_identifier"], "b61_state_072")
        self.assertEqual(state["epsilon_alpha_pairs"], [[0, 2]] * 6)
        self.assertEqual(state["required_prolongation_dimension"], 459)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("only the all-alpha-two scalar state", boundary)
        self.assertIn("does not by itself exclude the other b=61 states", boundary)
        self.assertIn("does not", boundary)


if __name__ == "__main__":
    unittest.main()
