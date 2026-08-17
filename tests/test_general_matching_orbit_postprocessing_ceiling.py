from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_matching_orbit_postprocessing_ceiling.py"
INDEPENDENT = ROOT / "scripts" / "general_matching_orbit_postprocessing_ceiling_independent.py"
FROZEN = ROOT / "data" / "general_matching_orbit_postprocessing_ceiling.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load("general_matching_orbit_postprocessing_ceiling", SCRIPT)


class GeneralMatchingOrbitPostprocessingCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = AUDIT.build_payload()

    def test_counts(self):
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["coverage_checks"], 186)
        self.assertEqual(replay["restricted_map_rank_checks"], 179_928)
        self.assertEqual(replay["rank_bound_checks"], 60)
        self.assertEqual(replay["block_sum_checks"], 4)

    def test_frozen(self):
        self.assertEqual(json.loads(FROZEN.read_text()), self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "7d1c559339080ccd46cc5bf1ee881ec6bbb1e1f816eb40119fe037804eb1846d",
        )

    def test_finite_instances(self):
        rows = self.payload["exact_replay"]["rows"]
        self.assertEqual(rows["5"][1]["subset_module_dimension"], 10)
        for n_rows in rows.values():
            for row in n_rows:
                module_dimension = row["subset_module_dimension"]
                for case in row["map_instances"]:
                    self.assertGreaterEqual(
                        module_dimension * case["maximum_matching_restriction_rank"],
                        case["full_rank"],
                    )

    def test_independent(self):
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(
            "GENERAL_MATCHING_ORBIT_POSTPROCESSING_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_kernel_intersection_checks=4752", completed.stdout)


if __name__ == "__main__":
    unittest.main()
