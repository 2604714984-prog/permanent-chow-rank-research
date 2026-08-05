from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_one_defect_sign_independent_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_one_defect_sign_independent_audit", SCRIPT)


class N6OneDefectSignIndependentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_ranks(self) -> None:
        rows = self.payload["canonical_parity_rows"]
        self.assertEqual(
            [row["exact_characteristic_zero_rank"] for row in rows],
            [31, 31, 31, 31, 31, 26],
        )
        self.assertEqual(
            [row["explicit_kernel_dimension"] for row in rows],
            [5, 5, 5, 5, 5, 10],
        )
        self.assertEqual(self.payload["one_defect_span_dimension"], 987)

    def test_independent_prime(self) -> None:
        self.assertEqual(self.payload["prime"], 1_000_033)
        self.assertEqual(
            self.payload["status"],
            "N6_ONE_DEFECT_SIGN_INDEPENDENT_AUDIT_PASS",
        )


if __name__ == "__main__":
    unittest.main()
