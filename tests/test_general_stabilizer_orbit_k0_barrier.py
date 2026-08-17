from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_stabilizer_orbit_k0_barrier.py"
INDEPENDENT = SCRIPTS / "general_stabilizer_orbit_k0_barrier_independent.py"
FROZEN = ROOT / "data" / "general_stabilizer_orbit_k0_barrier.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_stabilizer_orbit_k0_barrier", SCRIPT)


class GeneralStabilizerOrbitK0BarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_trivial_stabilizer_rows(self) -> None:
        rows = self.payload["finite_replay"]["stabilizer_rows"]
        self.assertEqual([row["n"] for row in rows], [2, 3, 4, 5])
        self.assertTrue(
            all(row["projective_stabilizer_size"] == 1 for row in rows)
        )
        self.assertTrue(all(row["factor_rank"] == row["n"] for row in rows))

    def test_exact_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["stabilizer_group_elements_checked"], 15_016)
        self.assertEqual(replay["partition_dimension_checks"], 270)
        self.assertEqual(replay["pointwise_isotype_checks"], 921)
        self.assertEqual(replay["weighted_support_checks"], 341)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "bf3defd92cc779905b2c676bc507fc7b03c7b5c1ad515f64393793ad2227782f",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_STABILIZER_ORBIT_K0_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_trivial_stabilizer_group_checks=15016",
            completed.stdout,
        )
        self.assertIn(
            "independent_pointwise_isotype_checks=508",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
