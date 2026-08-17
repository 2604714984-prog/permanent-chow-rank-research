from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_linear_matrix_barrier.py"
INDEPENDENT = SCRIPTS / "general_two_direction_linear_matrix_barrier_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_linear_matrix_barrier", PRIMARY)


class GeneralTwoDirectionLinearMatrixBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_small_pencil_classification(self) -> None:
        replay = self.payload["finite_replay"]
        counts = replay["classification_counts"]
        self.assertEqual(sum(counts.values()), 6_561)
        self.assertEqual(set(counts), {"regular", "principal", "row_block", "column_block", "zero"})
        self.assertTrue(all(value > 0 for value in counts.values()))

    def test_gorenstein_duality_cells(self) -> None:
        self.assertEqual(
            self.payload["finite_replay"]["gorenstein_row_column_rank_checks"],
            35,
        )

    def test_route_ceilings(self) -> None:
        rows = self.payload["finite_replay"]["rows"]
        self.assertEqual(
            {key: value["overall_2x2_linear_ceiling"] for key, value in rows.items()},
            {
                "3": 3,
                "4": 7,
                "5": 10,
                "6": 20,
                "7": 35,
                "8": 75,
                "9": 126,
                "10": 252,
            },
        )
        for row in rows.values():
            self.assertLess(row["overall_2x2_linear_ceiling"], row["existing_boundary"])
            self.assertEqual(row["class_ceilings"]["row_block"], row["class_ceilings"]["column_block"])

    def test_regular_and_principal_are_sharper(self) -> None:
        rows = self.payload["finite_replay"]["rows"]
        self.assertEqual(rows["4"]["class_ceilings"]["regular"], 4)
        self.assertEqual(rows["6"]["class_ceilings"]["principal"], 15)
        self.assertLessEqual(
            rows["10"]["class_ceilings"]["regular"],
            rows["10"]["central_binomial"],
        )

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_LINEAR_MATRIX_BARRIER_AUDIT_PASS",
            completed.stdout,
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
            "GENERAL_TWO_DIRECTION_LINEAR_MATRIX_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_small_pencil_checks=256", completed.stdout)
        self.assertIn("independent_gorenstein_duality_cells=27", completed.stdout)


if __name__ == "__main__":
    unittest.main()
