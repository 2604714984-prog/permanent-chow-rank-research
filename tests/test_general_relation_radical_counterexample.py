from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_relation_radical_counterexample.py"
FROZEN = ROOT / "data" / "general_relation_radical_counterexample.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_relation_radical_counterexample", SCRIPT)


class GeneralRelationRadicalCounterexampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_central_pairing_data(self) -> None:
        self.assertEqual(self.payload["central_relation_dimension"], 47)
        self.assertEqual(self.payload["central_pairing"]["rank_over_Q"], 24)
        self.assertEqual(
            self.payload["central_pairing"]["minor_determinant"], 256
        )
        self.assertEqual(
            self.payload["central_pairing_radical_dimension"], 23
        )
        self.assertGreater(
            self.payload["central_pairing_radical_dimension"],
            self.payload["naive_four_times_q_minus_one_cap"],
        )

    def test_direct_central_rank_matches_pairing_identity(self) -> None:
        self.assertEqual(self.payload["central_catalectic"]["rank_over_Q"], 50)
        self.assertEqual(
            self.payload["central_catalectic"]["minor_determinant"], -256
        )
        self.assertEqual(self.payload["central_rank_from_pairing_identity"], 50)

    def test_raw_derivative_shadow_is_not_the_radical(self) -> None:
        self.assertEqual(self.payload["degree_four_relation_dimension"], 15)
        self.assertEqual(self.payload["raw_derivative_shadow_dimension"], 47)
        self.assertTrue(
            self.payload["raw_derivative_shadow_equals_central_relation_space"]
        )
        self.assertEqual(
            self.payload["shadow_to_central_relation_pairing_rank"], 24
        )

    def test_scope_boundary(self) -> None:
        self.assertEqual(self.payload["residual_quartic_C22_rank_over_Q"], 18)
        self.assertEqual(
            self.payload["residual_quartic_flattening_lower_bound"], 3
        )
        self.assertIn("not proved minimum", self.payload["strict_scope"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
