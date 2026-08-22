import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_slope10_rectangular_endpoint.py"
DATA = ROOT / "data" / "n7_slope10_rectangular_endpoint.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n7_slope10_endpoint", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SlopeTenRectangularEndpointTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(
            self.payload,
            json.loads(DATA.read_text(encoding="utf-8")),
        )

    def test_rank_seven_coordinate_rows_and_full_endpoint(self):
        rows = self.payload["rank7_coordinate_initial_rows"]
        self.assertEqual(
            [row["endpoint_row"] for row in rows],
            [32, 49, 56, 57, 64, 67, 70],
        )
        self.assertEqual(rows[-1]["coordinate_minimum_allowing_bad_prolongation"], 69)
        self.assertTrue(
            all(
                row["proof_status"] == "PROVEN_MONOMIAL_TORUS_DEGENERATION"
                for row in rows[:-1]
            )
        )
        self.assertEqual(rows[-1]["proof_status"], "PROVEN_FULL_QUOTIENT")

    def test_rank_six_all_rows_are_proven(self):
        proven_positive_equality = []
        for normal_form in self.payload["rank6_normal_form_rows"]:
            support = normal_form["normal_form_support_size"]
            for row in normal_form["rows"]:
                d = row["quotient_rank"]
                lower = row.get(
                    "proven_arbitrary_lower", row.get("coordinate_lower")
                )
                self.assertGreaterEqual(lower, 10 * d)
                if support == 1 and d in (1, 2, 3, 4):
                    self.assertEqual(
                        row["proof_status"], "PROVEN_MONOMIAL_TORUS_DEGENERATION"
                    )
                elif support > 1 and d in (3, 4):
                    self.assertEqual(
                        row["proof_status"], "PROVEN_VERONESE_DISJOINTNESS"
                    )
                elif support > 1 and d in (1, 2):
                    self.assertEqual(
                        row["proof_status"], "PROVEN_RAW_COMPOSITE_DEGENERATION"
                    )
                if d > 0 and "proven_arbitrary_lower" in row and lower == 10 * d:
                    proven_positive_equality.append((support, d))
        self.assertEqual(proven_positive_equality, [(1, 6), (2, 6)])

    def test_local_endpoint_and_equality_boundary(self):
        self.assertEqual(
            self.payload["status"],
            "PROVEN_LOCAL_SLOPE10_ENDPOINT",
        )
        self.assertIn("hypothetical n=49", self.payload["equality_conclusion"].lower())
        self.assertIn("remain open", self.payload["claim_boundary"].lower())

    def test_partial_shadow_and_global_arithmetic(self):
        self.assertEqual(
            self.payload["codimension_one_partial_shadow"][
                "maximum_cubic_dimension"
            ],
            9,
        )
        self.assertEqual(
            self.payload["equality_arithmetic"][
                "solutions_to_6a_plus_7b_equals_49"
            ],
            [
                {"rank6_full_blocks": 0, "rank7_full_blocks": 7},
                {"rank6_full_blocks": 7, "rank7_full_blocks": 1},
            ],
        )


if __name__ == "__main__":
    unittest.main()
