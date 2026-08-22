from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_near_extremal_prolongation_pruning.py"
FROZEN = ROOT / "data" / "n6_near_extremal_prolongation_pruning.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_near_pruning", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6NearExtremalProlongationPruningTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_exact_pruning_counts(self) -> None:
        conclusion = self.payload["strict_conclusion"]
        self.assertEqual(
            conclusion["excluded_scalar_states_by_b"],
            {"61": 13, "62": 4, "63": 4},
        )
        self.assertEqual(
            conclusion["remaining_scalar_states_by_b"],
            {"61": 60, "62": 7, "63": 7},
        )

    def test_exact_excluded_state_identifiers(self) -> None:
        layers = {
            str(layer["middle_intersection_b"]): layer for layer in self.payload["layers"]
        }
        suffixes = {
            "61": [3, 5, 6, 12, 13, 15, 16, 18, 19, 20, 29, 30, 31],
            "62": [2, 3, 5, 6],
            "63": [2, 3, 5, 6],
        }
        for b, ordinals in suffixes.items():
            self.assertEqual(
                layers[b]["excluded_state_identifiers"],
                [f"N6-041-B{b}-S{ordinal:03d}" for ordinal in ordinals],
            )

    def test_every_excluded_state_has_strict_contradiction(self) -> None:
        cap = self.payload["universal_extremal_prolongation_cap"]
        for layer in self.payload["layers"]:
            for state in layer["excluded_states"]:
                self.assertEqual(state["fixed_quadratic_quotient_t2"], 12)
                self.assertIn([0, 0], state["epsilon_alpha_pairs"])
                self.assertGreater(
                    state["required_common_prolongation_dimension"], cap
                )
                self.assertEqual(
                    state["strict_contradiction_gap"],
                    state["required_common_prolongation_dimension"] - cap,
                )

    def test_state_identifiers_partition_source_table(self) -> None:
        for layer in self.payload["layers"]:
            excluded = set(layer["excluded_state_identifiers"])
            remaining = set(layer["remaining_state_identifiers"])
            self.assertTrue(excluded.isdisjoint(remaining))
            self.assertEqual(
                len(excluded | remaining), layer["source_scalar_state_count"]
            )

    def test_claim_boundary_is_scalar_only(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("only the listed canonical scalar states", boundary)
        self.assertIn("does not exclude any complete b=61,62,63 layer", boundary)
        self.assertIn("does not", boundary)


if __name__ == "__main__":
    unittest.main()
