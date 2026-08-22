import ast
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_minimal_four_way_obstruction.py"
DATA = ROOT / "data" / "n7_b2_minimal_four_way_obstruction.json"
SPEC = importlib.util.spec_from_file_location(
    "n7_b2_minimal_four_way_obstruction", SCRIPT
)
MODULE = importlib.util.module_from_spec(SPEC)
if SPEC.loader is None:
    raise RuntimeError("failed to load n7 B2 minimal four-way obstruction module")
SPEC.loader.exec_module(MODULE)


class MinimalFourWayObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_all_proper_subpackets_are_zero_defect(self) -> None:
        for profile in self.payload["profiles"].values():
            self.assertEqual(profile["proper_subpacket_count"], 14)
            self.assertTrue(profile["all_proper_subpackets_zero_defect"])
            self.assertEqual(profile["minimal_positive_subset_size"], 4)

    def test_shared_row_orbit_ranks(self) -> None:
        summary = self.payload["profiles"]["shared_row_01_02"]["orbit_summary"]
        self.assertEqual(summary["within_slice_pair"]["rank_tuples"], [[70, 65, 60, 55, 0]])
        self.assertEqual(summary["cross_slice_pair"]["rank_tuples"], [[70, 69, 66, 65, 0]])
        self.assertEqual(summary["triple"]["rank_tuples"], [[105, 95, 85, 75, 0]])
        self.assertEqual(summary["full_join"]["rank_tuples"], [[140, 111, 94, 75, 10]])

    def test_disjoint_orbit_ranks(self) -> None:
        summary = self.payload["profiles"]["disjoint_01_23"]["orbit_summary"]
        self.assertEqual(summary["within_slice_pair"]["rank_tuples"], [[70, 65, 60, 55, 0]])
        self.assertEqual(summary["cross_slice_pair"]["rank_tuples"], [[70, 70, 69, 69, 0]])
        self.assertEqual(summary["triple"]["rank_tuples"], [[105, 98, 88, 81, 0]])
        self.assertEqual(summary["full_join"]["rank_tuples"], [[140, 114, 95, 81, 12]])

    def test_exact_subset_count(self) -> None:
        counts = self.payload["candidate_cardinality_checked_before_materialization"]
        self.assertEqual(counts["nonempty_subsets_per_join"], 15)
        self.assertEqual(counts["exact_subset_rows"], 30)

    def test_no_bare_assert_in_replay(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        bare_asserts = [node.lineno for node in ast.walk(tree) if isinstance(node, ast.Assert)]
        self.assertEqual(bare_asserts, [])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)

    def test_optimized_mode_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(SCRIPT), "--verify-json", str(DATA)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("PASS n7 B2 minimal four-way obstruction", completed.stdout)


if __name__ == "__main__":
    unittest.main()
