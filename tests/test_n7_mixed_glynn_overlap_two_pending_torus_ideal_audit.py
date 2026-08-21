import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_overlap_two_pending_torus_ideal_audit.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap_two_torus_audit", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapTwoPendingTorusIdealAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlap_two_pending_torus_ideal_audit.json"
            ).read_text(encoding="utf-8")
        )

    def test_exact_inventory(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_803_PENDING_OVERLAP_TWO_TORUS_IDEALS_AUDITED",
        )
        self.assertEqual(self.payload["candidate_count"], 803)
        self.assertEqual(self.payload["determinant_count"], 1606)
        counts = {}
        for row in self.payload["rows"]:
            family = tuple(row["family"])
            counts[family] = counts.get(family, 0) + 1
        self.assertEqual(counts, self.module.EXPECTED_MULTI_MINOR_COUNTS)

    def test_every_row_has_rank_one_laurent_direction_and_bezout_gcd(self):
        for row in self.payload["rows"]:
            parameter_count = sum(row["family"]) - 2
            self.assertEqual(
                row["laurent_exponent_direction"],
                [1, 1] + [0] * (parameter_count - 2),
            )
            self.assertEqual(row["residual_gcd_over_Q_z"], "1")
            self.assertEqual(row["status"], self.module.ROW_STATUS)

    def test_every_row_has_exact_univariate_gcd_one(self):
        z = sp.Symbol("z")
        for row in self.payload["rows"]:
            residuals = [
                sp.Poly(item["residual_in_z_equals_p0_times_p1"], z)
                for item in row["reductions"]
            ]
            self.assertEqual(sp.gcd(residuals[0], residuals[1]).monic().as_expr(), 1)


if __name__ == "__main__":
    unittest.main()
