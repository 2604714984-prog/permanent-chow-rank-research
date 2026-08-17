from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_two_sided_matching_source_ceiling.py"
INDEPENDENT = SCRIPTS / "general_two_sided_matching_source_ceiling_independent.py"
FROZEN = ROOT / "data" / "general_two_sided_matching_source_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_sided_matching_source_ceiling", SCRIPT)


class GeneralTwoSidedMatchingSourceCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_source_and_coverage_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["source_graph_checks"], 48_616)
        self.assertEqual(replay["coordinate_coverage_checks"], 1_262)

    def test_dense_compression_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["dense_restriction_rank_computations"], 1_146)
        self.assertEqual(replay["dense_average_trace_checks"], 18)

    def test_isotype_and_block_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["isotype_dimension_cells"], 23_195)
        self.assertEqual(replay["isotype_support_checks"], 91_040)
        self.assertEqual(replay["finite_block_sum_checks"], 29)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "72fb06b3ca6201e2b31e0d0aafb22370cf2b7572eaf9e43a3eb0d0f6096c4533",
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
            "GENERAL_TWO_SIDED_MATCHING_SOURCE_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_partial_matching_checks=31748", completed.stdout)
        self.assertIn(
            "independent_coordinate_restriction_ranks=206384",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
