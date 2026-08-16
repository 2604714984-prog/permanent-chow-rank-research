from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_cross_degree_block_projection.py"
INDEPENDENT = SCRIPTS / "general_cross_degree_block_projection_independent.py"
FROZEN = ROOT / "data" / "general_cross_degree_block_projection.json"

# The theorem audit reuses the canonical exact product-shadow module stored in
# the scripts directory.  Add that directory explicitly before loading the
# audit by path; do not depend on the test runner's working directory.
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_cross_degree_block_projection", SCRIPT)


class GeneralCrossDegreeBlockProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_n7_block_and_bound(self) -> None:
        block = self.payload["n7_block"]
        self.assertEqual(block["single_term_lower_cap"], 3)
        self.assertEqual(block["lower_degree_projected_capacity"], 66)
        self.assertEqual(block["upper_block_cap"], 41)

        application = self.payload["n7_application"]
        self.assertEqual(application["projected_first_shadow_capacity"], 496)
        self.assertEqual(application["outer_intersection_cap"], 263)
        self.assertEqual(application["residual_terms"], 28)
        self.assertEqual(application["ordinary_lower_bound"], 45)

    def test_n8_block_and_bound(self) -> None:
        block = self.payload["n8_block"]
        self.assertEqual(block["single_term_lower_cap"], 6)
        self.assertEqual(block["lower_degree_projected_capacity"], 118)
        self.assertEqual(block["upper_block_cap"], 112)

        application = self.payload["n8_application"]
        self.assertEqual(application["projected_first_shadow_capacity"], 784)
        self.assertEqual(application["outer_intersection_cap"], 560)
        self.assertEqual(application["residual_terms"], 63)
        self.assertEqual(application["ordinary_lower_bound"], 80)

    def test_next_interface(self) -> None:
        row = self.payload["next_interface"]
        self.assertEqual(row["perm8_sufficient_five_term_cap_for_lower81"], 90)
        self.assertEqual(row["maximum_projected_capacity"], 986)
        self.assertEqual(row["first_excluded_outer_shadow"], 987)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_CROSS_DEGREE_BLOCK_PROJECTION_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=45", completed.stdout)
        self.assertIn("independent_perm8_lower_bound=80", completed.stdout)


if __name__ == "__main__":
    unittest.main()
