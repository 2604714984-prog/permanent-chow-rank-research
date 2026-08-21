import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_overlapping_23_torus_ideal_audit.py"
    spec = importlib.util.spec_from_file_location("n7_overlap23_torus_audit", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Overlapping23TorusIdealAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_23_torus_ideal_audit.json"
            ).read_text(encoding="utf-8")
        )

    def test_frozen_payload_replays_exactly(self):
        self.assertEqual(self.module.build_payload(), self.payload)

    def test_inventory_and_status(self):
        self.assertEqual(self.payload["candidate_count"], 600)
        self.assertEqual(self.payload["single_minor_row_count"], 270)
        self.assertEqual(self.payload["multi_minor_row_count"], 330)
        self.assertEqual(
            {row["status"] for row in self.payload["rows"]},
            {self.module.ROW_STATUS},
        )

    def test_representative_two_minor_bezout_reduction(self):
        row = next(
            row
            for row in self.payload["rows"]
            if row["shape"] == "extra_left"
            and row["core_support"] == [0, 2]
            and row["extra_coordinate"] == 1
            and row["identity_count"] == 1
        )
        residuals = [
            sp.Poly(item["residual_in_z_equals_r_times_t"], self.module.z)
            for item in row["reductions"]
        ]
        self.assertEqual(sp.gcd(residuals[0], residuals[1]).monic().as_expr(), 1)


if __name__ == "__main__":
    unittest.main()
