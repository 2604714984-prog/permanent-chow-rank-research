from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_six_permutation_collision_audit.py"
FROZEN = ROOT / "data" / "n6_six_permutation_collision_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_six_permutation_collision_audit", SCRIPT)


class N6SixPermutationCollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_output_and_quotient_dimensions(self) -> None:
        self.assertEqual(
            self.payload["ordinary_six_output_span_rank_over_Q"], 3087
        )
        self.assertEqual(
            self.payload["quotient_six_output_span_rank_over_Q"], 3051
        )
        self.assertEqual(
            self.payload["internal_output_relation_dimension_eta"], 1143
        )
        self.assertEqual(self.payload["aggregate_collision_dimension_j"], 36)

    def test_explicit_collision_is_the_full_intersection(self) -> None:
        self.assertEqual(
            self.payload[
                "explicit_cubic_permanent_collision_rank_over_Q"
            ],
            36,
        )
        self.assertTrue(
            self.payload["collision_subspace_contained_in_six_output_span"]
        )
        self.assertTrue(
            self.payload["collision_subspace_contained_in_permanent_output"]
        )

    def test_nonminimum_boundary(self) -> None:
        self.assertTrue(
            self.payload["six_term_sum_has_chow_rank_upper_bound_four"]
        )
        self.assertIn("nonminimum", self.payload["conclusion"])
        self.assertIn("minimum", self.payload["scope"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
