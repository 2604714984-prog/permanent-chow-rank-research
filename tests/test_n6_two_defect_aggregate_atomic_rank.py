from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_defect_aggregate_atomic_rank_audit.py"
FROZEN = ROOT / "data" / "n6_two_defect_aggregate_atomic_rank_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_two_defect_aggregate_atomic_rank_audit", SCRIPT)


class N6TwoDefectAggregateAtomicRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_local_three_atom_classification(self) -> None:
        local = self.payload["local_dictionary_certificate"]
        self.assertEqual(local["restricted_rows"], [0, 2, 3])
        self.assertEqual(local["restricted_nonconstant_sign_labels"], [2, 4, 6])
        self.assertEqual(local["local_atom_count"], 9)
        self.assertEqual(
            local["compatible_support_count"],
            {"1": 0, "2": 0, "3": 2},
        )
        triples = local["exact_three_atom_types"]
        self.assertEqual(
            [triple["lower_anova"] for triple in triples],
            [
                ["3/8", "-1/4", "-1/4", "-1/4", "-1/4"],
                ["-3/8", "1/4", "1/4", "1/4", "1/4"],
            ],
        )

    def test_forty_five_atom_obstruction(self) -> None:
        lower = self.payload["separator_lower_bound_certificate"]
        self.assertEqual(lower["pair_block_count"], 15)
        self.assertEqual(lower["minimum_pair_atoms_per_block"], 3)
        self.assertEqual(lower["minimum_pair_atom_total"], 45)
        self.assertEqual(
            lower["signed_edge_assignments_matching_all_unary_coefficients"],
            70,
        )
        self.assertEqual(lower["forced_signed_edge_sum"], 3)
        self.assertEqual(lower["forced_constant_from_45_pair_atoms"], "9/8")
        self.assertFalse(lower["forty_five_atom_representation_possible"])

    def test_exact_rank_46_constructions(self) -> None:
        construction = self.payload["exact_construction_certificate"]
        self.assertEqual(construction["pair_atom_count"], 45)
        self.assertEqual(construction["total_atom_count"], 46)
        self.assertEqual(construction["separator_atomic_rank"], 46)
        self.assertEqual(construction["one_minus_separator_atomic_rank"], 46)
        self.assertEqual(construction["separator_assignment_checks"], 46_656)
        self.assertEqual(
            construction["one_minus_separator_assignment_checks"],
            46_656,
        )
        self.assertEqual(len(construction["positive_edges"]), 9)
        self.assertEqual(len(construction["negative_edges"]), 6)

    def test_explicit_aggregate_cost_and_boundary(self) -> None:
        aggregate = self.payload["aggregate_formula_certificate"]
        self.assertEqual(aggregate["nonzero_constant_aggregate_count"], 8)
        self.assertEqual(aggregate["nonconstant_aggregate_count"], 16)
        self.assertEqual(
            aggregate["exact_actual_term_cost_for_this_aggregate_assignment"],
            744,
        )
        decision = self.payload["route_decision"]
        self.assertFalse(decision["specific_formula_can_yield_at_most_25_terms"])
        self.assertFalse(
            decision["all_two_defect_decompositions_lower_bounded_by_744"]
        )
        self.assertEqual(decision["two_defect_minimum_term_support"], "open")
        self.assertFalse(decision["broad_sparse_optimization_authorized"])

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
