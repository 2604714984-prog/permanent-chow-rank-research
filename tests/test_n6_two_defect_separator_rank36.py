from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_defect_separator_rank36_audit.py"
FROZEN = ROOT / "data" / "n6_two_defect_separator_rank36_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_two_defect_separator_rank36_audit", SCRIPT)


class N6TwoDefectSeparatorRank36Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_projection_and_exact_rank(self) -> None:
        projection = self.payload["projection_certificate"]
        self.assertEqual(projection["label_projection"], "v -> v & 24")
        self.assertEqual(projection["sign_vector_checks"], 192)
        self.assertEqual(projection["separator_assignment_checks"], 46_656)
        self.assertTrue(projection["support_nonincrease"])
        self.assertEqual(self.payload["exact_atomic_rank"], 36)
        self.assertEqual(
            self.payload["sixteen_base_assignment_actual_term_cost"],
            576,
        )

    def test_local_normal_forms(self) -> None:
        local = self.payload["local_normal_form_certificate"]
        self.assertEqual(local["exact_local_support_space_count"], 243)
        self.assertEqual(
            local["compressed_support_spaces_size_at_least_four"],
            227,
        )
        self.assertEqual(
            local["exception_supports"],
            [
                [0, 5, 7, 8],
                [2, 4, 6, 8],
                [0, 2, 4, 6, 8],
                [0, 4, 5, 7, 8],
            ],
        )
        self.assertEqual(
            local["trivial_size_three_types_absorbed_as_one_ordinary_atom"],
            4,
        )
        self.assertEqual(len(local["cost_one_point_bundle_types"]), 7)
        self.assertEqual(len(local["cost_two_point_bundle_types"]), 2)
        self.assertEqual(len(local["cost_three_affine_bundle_types"]), 2)

    def test_global_support_exhaustion(self) -> None:
        search = self.payload["global_support_search_certificate"]
        self.assertEqual(search["baseline_pair_atom_count"], 30)
        self.assertEqual(
            search["ordinary_correction_minimum_without_bundles"],
            6,
        )
        self.assertFalse(search["support_at_most_35_counterexample_found"])
        self.assertEqual(search["lower_bound"], 36)
        counts = search["coverage_counts"]
        self.assertEqual(counts["cost_one_bundle_count_4"], 3_277_365)
        self.assertEqual(
            counts["cost_one_bundle_count_5_covered_by_meet_in_middle"],
            50_471_421,
        )
        self.assertEqual(
            counts["one_cost_two_plus_three_cost_one_covered_by_hash"],
            3_745_560,
        )
        self.assertEqual(
            counts["affine_plus_two_cost_one_exact_zero_tests"],
            133_770,
        )

    def test_upper_bound_and_frozen_payload(self) -> None:
        upper = self.payload["upper_bound_certificate"]
        self.assertEqual(upper["atom_count"], 36)
        self.assertEqual(upper["exact_assignment_checks"], 46_656)
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
