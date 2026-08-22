import ast
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_subpacket_obstruction_monotonicity.py"
DATA = ROOT / "data" / "n7_b2_subpacket_obstruction_monotonicity.json"
SPEC = importlib.util.spec_from_file_location(
    "n7_b2_subpacket_obstruction_monotonicity", SCRIPT
)
MODULE = importlib.util.module_from_spec(SPEC)
if SPEC.loader is None:
    raise RuntimeError("failed to load n7 B2 subpacket obstruction module")
SPEC.loader.exec_module(MODULE)


class SubpacketObstructionMonotonicityTests(unittest.TestCase):
    def test_exhaustive_scalar_block_replay(self) -> None:
        replay = MODULE.exhaustive_scalar_block_replay()
        self.assertEqual(replay["systems_checked"], 4096)
        self.assertEqual(replay["strict_subset_pairs_per_system"], 12)
        self.assertEqual(replay["inequalities_checked"], 49152)
        self.assertEqual(replay["violations"], 0)

    def test_canonical_join_corollary(self) -> None:
        corollary = MODULE.canonical_join_corollary()
        self.assertEqual(
            corollary["shared_row_01_02"]["minimum_obstruction_in_every_completion"],
            10,
        )
        self.assertEqual(
            corollary["disjoint_01_23"]["minimum_obstruction_in_every_completion"],
            12,
        )
        self.assertTrue(
            all(
                not row["completion_to_sylvester_equality_possible"]
                for row in corollary.values()
            )
        )

    def test_no_bare_assert_in_proof_replay(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        bare_asserts = [node.lineno for node in ast.walk(tree) if isinstance(node, ast.Assert)]
        self.assertEqual(bare_asserts, [])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)

    def test_optimized_mode_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(SCRIPT), "--verify-json", str(DATA)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("PASS n7 B2 subpacket obstruction monotonicity", completed.stdout)


if __name__ == "__main__":
    unittest.main()
