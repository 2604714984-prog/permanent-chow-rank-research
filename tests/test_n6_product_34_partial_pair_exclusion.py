from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_34_partial_pair_exclusion.py"
FROZEN = ROOT / "data" / "n6_product_34_partial_pair_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_product_34_partial", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Product34PartialPairExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_four_fixed_pair_orbits_are_complete(self) -> None:
        fixed = self.payload["coordinate_fixed_pair_classification"]
        self.assertEqual(fixed["cross_dimension_at_most_five_count"], 90)
        self.assertEqual(fixed["dimension_distribution"], {"3": 18, "5": 72})
        self.assertTrue(fixed["orbit_union_is_complete_and_disjoint"])
        self.assertEqual(
            sorted(orbit["orbit_size"] for orbit in fixed["orbits"].values()),
            [6, 12, 36, 36],
        )

    def test_rank_five_normal_directions_are_killed_linearly(self) -> None:
        for certificate in self.payload["rank_five_linear_normal_certificates"].values():
            self.assertEqual(certificate["exact_QQ_rank"], 64)
            self.assertEqual(certificate["exact_QQ_nullity"], 8)
            self.assertEqual(certificate["normal_graph_variables"], 48)
            self.assertEqual(certificate["exact_normal_linear_rank"], 48)
            self.assertTrue(
                certificate["all_tangent_directions_stay_in_common_two_row_ambient"]
            )

    def test_rank_three_cubic_normal_cones_are_empty(self) -> None:
        certificates = self.payload["rank_three_cubic_normal_cone_certificates"]
        self.assertEqual(certificates["K23_diagonal"]["weight_group_count"], 12)
        self.assertEqual(certificates["K32_diagonal"]["weight_group_count"], 15)
        for certificate in certificates.values():
            self.assertTrue(
                certificate["relative_projectivized_normal_cone_has_no_fixed_point"]
            )
            self.assertTrue(all(
                group["all_normal_cubic_monomials_in_exact_initial_ideal"]
                for group in certificate["groups"]
            ))

    def test_partial_product_corollary_closes_thirteen_and_fourteen(self) -> None:
        corollary = self.payload["partial_pair_corollary"]
        self.assertEqual(corollary["excluded_dimensions"], [13, 14, 15])
        self.assertTrue(corollary["transpose"])
        application = self.payload["application"]
        self.assertEqual(application["newly_closed_biflag_kappa2_values"], [1, 2])
        self.assertIn(
            "standard hook and biflag at kappa2=0",
            application["remaining_a2_72_branches"],
        )

    def test_boundary_remains_explicit(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("standard-hook", boundary)
        self.assertIn("kappa2=0", boundary)
        self.assertIn("lower 29", boundary)
        self.assertIn("ChowRank", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
