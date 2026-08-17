from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_equivariant_k0_orbit_barrier.py"
INDEPENDENT = SCRIPTS / "general_equivariant_k0_orbit_barrier_independent.py"
FROZEN = ROOT / "data" / "general_equivariant_k0_orbit_barrier.json"

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


AUDIT = load_module("general_equivariant_k0_orbit_barrier", SCRIPT)


class GeneralEquivariantK0OrbitBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_regular_and_two_row_interfaces(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["regular_partition_cells"], 138)
        self.assertEqual(replay["regular_dimension_checks"], 10)
        self.assertEqual(replay["two_row_dimension_checks"], 6_388)
        self.assertEqual(replay["degree_isotype_cells"], 67_988)

    def test_weighted_route_interfaces(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["weighted_degree_checks"], 70_556)
        self.assertEqual(replay["exhaustive_isotype_supports"], 200_359)
        self.assertEqual(replay["finite_block_checks"], 39)
        self.assertEqual(replay["ungraded_isotype_checks"], 6_179)

    def test_frozen_theorem_core_and_counts(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen["core_sha256"], self.payload["core_sha256"])
        self.assertEqual(frozen["status"], self.payload["status"])
        self.assertEqual(frozen["theorem"], self.payload["theorem"])
        self.assertEqual(frozen["claim_boundary"], self.payload["claim_boundary"])
        for key, value in frozen["exact_replay"].items():
            self.assertEqual(value, self.payload["exact_replay"][key])
        self.assertEqual(
            self.payload["core_sha256"],
            "e6ac3ce63910c27ef4a89856487caefdf66c7a133c706cd3e6bd5c3d31d17357",
        )

    def test_named_specht_dimensions(self) -> None:
        self.assertEqual(AUDIT.hook_dimension((6,)), 1)
        self.assertEqual(AUDIT.hook_dimension((5, 1)), 5)
        self.assertEqual(AUDIT.hook_dimension((4, 2)), 9)
        self.assertEqual(AUDIT.hook_dimension((3, 3)), 5)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_EQUIVARIANT_K0_ORBIT_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_isotype_cells=249945", completed.stdout)
        self.assertIn("independent_selected_supports=20143", completed.stdout)


if __name__ == "__main__":
    unittest.main()
