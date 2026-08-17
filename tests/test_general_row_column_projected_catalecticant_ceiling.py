from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
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


AUDIT = load_module(
    "projected_cat",
    SCRIPTS / "general_row_column_projected_catalecticant_ceiling.py",
)
FROZEN = ROOT / "data" / "general_row_column_projected_catalecticant_ceiling.json"


class GeneralRowColumnProjectedCatalecticantCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(
            (
                replay["projector_checks"],
                replay["rectangle_checks"],
                replay["arbitrary_union_checks"],
            ),
            (60, 200, 188),
        )

    def test_frozen(self) -> None:
        self.assertEqual(json.loads(FROZEN.read_text()), self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "19cec02e6c1a9db1a24bfe4b8b13fc1a0e722a61970f36088a8e81d3add900d1",
        )

    def test_n8_central_arbitrary_union(self) -> None:
        row = next(
            value
            for value in self.payload["exact_replay"]["finite"]["8"]
            if value["m"] == 4
        )
        self.assertEqual(row["subset_dimension"], 70)
        self.assertLessEqual(
            row["maximum_union_ratio_numerator"],
            70 * row["maximum_union_ratio_denominator"],
        )

    def test_n9_full_union_attains_ceiling(self) -> None:
        row = next(
            value
            for value in self.payload["exact_replay"]["finite"]["9"]
            if value["m"] == 4
        )
        self.assertEqual(row["subset_dimension"], 126)
        self.assertEqual(
            row["maximum_union_ratio_numerator"],
            126 * row["maximum_union_ratio_denominator"],
        )

    def test_independent(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(
                    SCRIPTS
                    / "general_row_column_projected_catalecticant_ceiling_independent.py"
                ),
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_rectangle_checks=146", completed.stdout)
        self.assertIn("independent_arbitrary_union_checks=132", completed.stdout)


if __name__ == "__main__":
    unittest.main()
