from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_defect_sixteen_base_aggregate_audit.py"
FROZEN = ROOT / "data" / "n6_two_defect_sixteen_base_aggregate_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_two_defect_sixteen_base_aggregate_audit", SCRIPT)


class N6TwoDefectSixteenBaseAggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_aggregate_formula(self) -> None:
        aggregate = self.payload["aggregate_certificate"]
        self.assertEqual(aggregate["separator"], "g(r)=n_4(r)*n_5(r)")
        self.assertEqual(aggregate["target_parity"], 31)
        self.assertEqual(aggregate["zero_parity"], 7)
        self.assertEqual(aggregate["support_character"], 24)
        self.assertEqual(aggregate["target_fiber_separator_values"], [1])
        self.assertEqual(aggregate["zero_fiber_separator_values"], [0])
        self.assertEqual(aggregate["nonzero_base_aggregate_count"], 16)
        self.assertEqual(aggregate["nonzero_base_labels"], list(range(8, 24)))
        self.assertEqual(
            aggregate["zero_base_labels"],
            list(range(0, 8)) + list(range(24, 32)),
        )
        self.assertEqual(aggregate["exact_assignment_checks"], 46_656)

    def test_local_two_atom_classification(self) -> None:
        local = self.payload["fixed_base_atomic_rank_certificate"][
            "local_dictionary_certificate"
        ]
        self.assertEqual(local["restricted_rows"], [0, 4, 5])
        self.assertEqual(local["restricted_nonconstant_sign_labels"], [8, 16, 24])
        self.assertEqual(local["local_pure_atom_count"], 9)
        self.assertEqual(local["compatible_support_count"], {"1": 0, "2": 1})
        unique = local["unique_two_atom_type"]
        self.assertEqual(unique["support"], [[8, 16], [16, 8]])
        self.assertEqual(unique["coefficients"], ["1/4", "1/4"])
        self.assertEqual(
            unique["lower_anova"],
            ["1/2", "-1/2", "-1/2", "-1/2", "-1/2"],
        )

    def test_fixed_base_atomic_rank_window(self) -> None:
        rank = self.payload["fixed_base_atomic_rank_certificate"]
        self.assertEqual(rank["pair_block_count"], 15)
        self.assertEqual(rank["minimum_atoms_per_nonzero_pair_block"], 2)
        self.assertEqual(rank["thirty_atom_pure_block_lower_bound"], 30)
        self.assertFalse(rank["thirty_atom_representation_possible"])
        self.assertEqual(rank["atomic_rank_lower_bound"], 31)
        self.assertEqual(rank["explicit_pair_atom_count"], 30)
        self.assertEqual(rank["explicit_one_defect_correction_count"], 6)
        self.assertEqual(rank["atomic_rank_upper_bound"], 36)
        self.assertEqual(rank["construction_assignment_checks"], 46_656)

    def test_cost_window_and_fail_closed_boundary(self) -> None:
        cost = self.payload["specific_assignment_actual_term_cost_window"]
        self.assertEqual(cost, {"lower_bound": 496, "upper_bound": 576})
        decision = self.payload["route_decision"]
        self.assertEqual(decision["previous_nonzero_base_aggregate_count"], 24)
        self.assertEqual(decision["new_nonzero_base_aggregate_count"], 16)
        self.assertTrue(decision["sixteen_base_aggregate_representation_exact"])
        self.assertFalse(decision["sixteen_base_is_minimum"])
        self.assertFalse(decision["specific_assignment_can_yield_at_most_25_terms"])
        self.assertEqual(decision["global_two_defect_minimum"], "open")
        self.assertFalse(decision["broad_sparse_optimization_authorized"])

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
