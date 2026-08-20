from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_coordinate_graph_orbit_search.py"
DATA = ROOT / "data" / "n7_coordinate_graph_orbit_search.json"
SPEC = importlib.util.spec_from_file_location("n7_coordinate_graph_orbit_search", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class CoordinateGraphOrbitSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(cls_payload := self.payload, json.loads(DATA.read_text(encoding="utf-8")))
        self.assertTrue(cls_payload["inconsistent_over_Q"])

    def test_orbit_counts(self) -> None:
        self.assertEqual(self.payload["full_function_count"], 6**7)
        self.assertEqual(self.payload["proper_partial_map_count"], 7**7 - 6**7)
        self.assertEqual(self.payload["full_function_orbit_count"], 100)
        self.assertEqual(self.payload["proper_partial_map_orbit_count"], 243)

    def test_exact_rank_jump(self) -> None:
        self.assertEqual(self.payload["coefficient_matrix_shape"], [243, 100])
        self.assertEqual(self.payload["rational_coefficient_rank"], 82)
        self.assertEqual(self.payload["rational_augmented_rank"], 83)

    def test_degree_two_already_excludes_relaxed_family(self) -> None:
        row = self.payload["degreewise_relaxed_moment_ranks"][2]
        self.assertEqual(row, {
            "A_degree": 2,
            "orbit_equation_count": 4,
            "coefficient_rank": 3,
            "augmented_rank": 4,
        })
        certificate = self.payload["degree_two_combinatorial_certificate"]
        self.assertEqual(certificate["left_kernel_coefficients"], [-5, -2, 1, 1])
        self.assertEqual(certificate["target_evaluation"], -5)
        self.assertEqual(
            [entry["name"] for entry in certificate["row_orbits"]],
            ["two_cycle", "length_two_path", "common_target_collision", "disjoint_edges"],
        )


if __name__ == "__main__":
    unittest.main()
