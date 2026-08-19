from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "general_partition_laplace_envelopes.py"
INDEPENDENT_PATH = ROOT / "scripts" / "general_partition_laplace_envelopes_independent.py"
DATA_PATH = ROOT / "data" / "general_partition_laplace_envelopes.json"


def load_primary():
    spec = importlib.util.spec_from_file_location(
        "general_partition_laplace_envelopes", PRIMARY_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(PRIMARY_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GeneralPartitionLaplaceEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primary = load_primary()

    def test_partition_laplace_counts(self) -> None:
        result = self.primary.verify_partition_laplace(m_max=7)
        self.assertGreater(result["partition_shapes_checked"], 0)
        self.assertEqual(result["generated_global_monomials"], 84503)
        self.assertEqual(
            result["support_checks"], result["ordered_column_partitions_checked"]
        )

    def test_cubic_three_term_witness(self) -> None:
        result = self.primary.verify_cubic_witness()
        self.assertEqual(result["groups"], 3)
        self.assertEqual(result["monomials_per_group"], [2, 2, 2])
        self.assertEqual(result["support_sizes"], [5, 5, 5])
        self.assertEqual(result["global_monomials"], 6)

    def test_exact_cubic_mu(self) -> None:
        self.assertEqual(
            [self.primary.cubic_mu(n) for n in range(3, 10)],
            [4, 4, 3, 2, 2, 2, 1],
        )
        self.assertEqual(self.primary.cubic_mu(128), 1)

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(self.primary.build_payload(), expected)

    def test_claim_boundary(self) -> None:
        core = self.primary.build_payload()["core"]
        boundary = core["claim_boundary"]
        self.assertTrue(boundary["new_exact_literal_block_threshold"])
        self.assertFalse(boundary["new_chow_rank_lower_bound"])
        self.assertFalse(boundary["border_rank_improvement"])
        self.assertFalse(boundary["literature_novelty_established"])

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_PARTITION_LAPLACE_ENVELOPES_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
