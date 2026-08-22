import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_colored_mapping_cone_barrier.py"
SPEC = importlib.util.spec_from_file_location("n6_colored_mapping_cone", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ColoredMappingConeBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = MODULE.build_payload()

    def test_exact_counterexample_rows(self):
        rows = self.payload["exact_relation_homology_rows"]
        self.assertEqual(
            [row["ordinary_middle_relation_dimension"] for row in rows],
            [4, 4, 2],
        )
        self.assertEqual(
            [row["labelled_presentation_kernel"] for row in rows],
            [0, 7, 12],
        )

    def test_mapping_cone_excess_is_explicit(self):
        statement = self.payload["mapping_cone_identity"]
        self.assertIn("K_m(P) intersect K_m(H)", statement)
        self.assertIn("J_m^diag", statement)
        self.assertNotIn("K_m(P)+K_m(H)", statement)

    def test_claim_boundary(self):
        self.assertIn("not a permanent decomposition", self.payload["claim_boundary"])
        self.assertIn("weight-refined", self.payload["claim_boundary"])
        self.assertIn("do not exclude every inequality", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
