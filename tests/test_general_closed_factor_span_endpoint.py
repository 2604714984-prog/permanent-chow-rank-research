from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_closed_factor_span_endpoint.py"
INDEPENDENT = SCRIPTS / "general_closed_factor_span_endpoint_independent.py"
FROZEN = ROOT / "data" / "general_closed_factor_span_endpoint.json"

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


AUDIT = load_module("general_closed_factor_span_endpoint", PRIMARY)


class ClosedFactorSpanEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_endpoint_sizes(self) -> None:
        self.assertEqual(AUDIT.closed_zero_block_size(8, 4), 2)
        self.assertEqual(AUDIT.closed_zero_block_size(9, 6), 4)
        self.assertEqual(AUDIT.closed_zero_block_size(12, 6), 3)
        self.assertEqual(AUDIT.closed_zero_block_size(18, 6), 2)

    def test_sharp_exceptions(self) -> None:
        self.assertEqual(AUDIT.closed_zero_block_size(4, 2), 0)
        self.assertEqual(AUDIT.closed_zero_block_size(9, 3), 0)
        self.assertEqual(
            self.payload["finite_replay"]["quadratic_counterexample"]["q"],
            2,
        )

    def test_projection_cap(self) -> None:
        self.assertEqual(AUDIT.projection_cap(8, 4, 7), 5 * 70)
        self.assertEqual(AUDIT.projection_cap(12, 6, 10), 7 * 924)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "7d78c0e595d25130a9bf2f9dd843ef88f3be737004f33b3f85f3be1170eb376a",
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
            "GENERAL_CLOSED_FACTOR_SPAN_ENDPOINT_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_endpoint_triples=258", completed.stdout)
        self.assertIn(
            "independent_proper_endpoint_triples=132",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
