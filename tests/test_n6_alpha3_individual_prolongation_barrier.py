from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_individual_prolongation_barrier.py"
FROZEN = ROOT / "data" / "n6_alpha3_individual_prolongation_barrier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_alpha3_barrier", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Alpha3IndividualProlongationBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # One worker is deliberate: it independently replays the same exact
        # finite calculation without relying on multiprocessing scheduling.
        cls.payload = AUDIT.compute(1)
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload_ignoring_worker_count(self) -> None:
        expected = dict(self.frozen)
        observed = dict(self.payload)
        expected.pop("worker_count")
        observed.pop("worker_count")
        self.assertEqual(observed, expected)

    def test_coordinate_support_classification(self) -> None:
        self.assertEqual(
            self.payload["coordinate_support_count_by_rectangle_count"],
            {"0": 1_837_392, "1": 109_800, "3": 600},
        )
        self.assertEqual(
            self.payload["row_column_support_orbit_count_by_rectangle_count"],
            {"0": 76, "1": 12, "3": 2},
        )

    def test_fixed_cap_histograms(self) -> None:
        diagnostics = self.payload["fixed_local_t15_diagnostics"]
        self.assertEqual(diagnostics["0"]["maximum_component_upper_cap"], 520)
        self.assertEqual(diagnostics["1"]["maximum_component_upper_cap"], 458)
        self.assertEqual(
            sum(diagnostics["0"]["component_upper_cap_histogram"].values()), 76
        )
        self.assertEqual(
            sum(diagnostics["1"]["component_upper_cap_histogram"].values()), 12
        )

    def test_actual_same_row_counterexample(self) -> None:
        example = self.payload["same_row_actual_term"]
        self.assertEqual(example["epsilon_alpha"], [0, 3])
        self.assertEqual(example["quadratic_derivative_dimension"], 15)
        self.assertEqual(example["permanent_quadratic_intersection_dimension"], 0)
        self.assertEqual(example["exact_fraction_prolongation_dimension"], 520)
        self.assertEqual(example["modular_prolongation_nullity_mod_1000003"], 520)

    def test_claim_boundary_is_coupled_safe(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("individual-term", boundary)
        self.assertIn("does not refute or exclude a six-term coupled", boundary)
        self.assertIn("may destroy directness", boundary)


if __name__ == "__main__":
    unittest.main()
