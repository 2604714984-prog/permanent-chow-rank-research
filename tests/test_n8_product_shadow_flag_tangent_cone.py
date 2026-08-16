from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "n8_product_shadow_flag_tangent_cone.py"
INDEPENDENT = ROOT / "scripts" / "n8_product_shadow_flag_tangent_cone_independent.py"
FROZEN = ROOT / "data" / "n8_product_shadow_flag_tangent_cone.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n8_product_shadow_flag_tangent_cone", PRIMARY)


class N8ProductShadowFlagTangentConeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_linear_tangent_counts(self) -> None:
        row = self.payload["linear_tangent_audit"]
        self.assertEqual(row["allowed_graph_variables_after_zero_column_filter"], 8_960)
        self.assertEqual(row["variables_in_zero_component"], 2_240)
        self.assertEqual(row["variables_in_nonzero_components"], 6_720)
        self.assertEqual(row["tangent_dimension"], 27)
        self.assertEqual(
            row["component_size_histogram"],
            {"35": 8, "280": 7, "350": 4, "385": 8},
        )
        self.assertEqual(
            row["direction_kind_histogram"],
            {"ambient_column": 12, "line": 8, "row": 7},
        )

    def test_quadratic_obstruction_counts(self) -> None:
        row = self.payload["quadratic_obstruction"]
        self.assertEqual(row["unordered_direction_pair_count"], 351)
        self.assertEqual(row["zero_mixed_obstruction_pair_count"], 42)
        self.assertEqual(row["nonzero_mixed_obstruction_pair_count"], 309)
        self.assertEqual(row["distinct_equation_count"], 256)
        self.assertEqual(row["monomial_equation_count"], 203)
        self.assertEqual(row["binomial_equation_count"], 53)
        self.assertEqual(row["characteristic_zero_equation_rank"], 256)

    def test_reduced_tangent_cone_and_global_dimension(self) -> None:
        row = self.payload["reduced_tangent_cone"]
        self.assertEqual(row["maximal_linear_component_count"], 19)
        self.assertEqual(row["component_dimension_histogram"], {"1": 7, "3": 8, "4": 4})
        self.assertEqual(row["local_equality_locus_dimension"], 4)
        self.assertEqual(self.payload["global_equality_locus"]["dimension"], 4)
        self.assertEqual(self.payload["global_equality_locus"]["torus_fixed_point_count"], 6_720)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["logical_boundary"]
        self.assertEqual(boundary["full_noncoordinate_equality_locus"], "open")
        self.assertEqual(boundary["fourteen_chow_term_realizability"], "open")
        self.assertFalse(boundary["new_perm8_lower_bound"])
        self.assertFalse(boundary["border_rank_claim"])

    def test_frozen_payload_matches(self) -> None:
        self.assertEqual(
            json.loads(FROZEN.read_text(encoding="utf-8")),
            self.payload,
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "N8_PRODUCT_SHADOW_TANGENT_CONE_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_compatible_pair_count=42", completed.stdout)
        self.assertIn("independent_maximal_component_count=19", completed.stdout)


if __name__ == "__main__":
    unittest.main()
