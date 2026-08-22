from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower50_proof_contract.py"
SPEC = importlib.util.spec_from_file_location("n7_lower50_proof_contract", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Lower50ProofContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = MODULE.PROOF.read_text(encoding="utf-8")

    def test_integrated_contract(self) -> None:
        MODULE.audit_text(self.text)
        MODULE.audit_payloads()

    def assert_mutation_fails(self, old: str, new: str) -> None:
        self.assertIn(old, self.text)
        with self.assertRaises(ValueError):
            MODULE.audit_text(self.text.replace(old, new, 1))

    def test_reversed_apolar_degree_fails(self) -> None:
        self.assert_mutation_fails(
            "For \\(d=3,4\\), correctly graded Gorenstein duality",
            "For \\(d=2,5\\), correctly graded Gorenstein duality",
        )

    def test_wrong_semicontinuity_direction_fails(self) -> None:
        self.assert_mutation_fails(
            "symbol ranks are lower bounds for the original symbols",
            "symbol ranks are upper bounds for the original symbols",
        )

    def test_wrong_graph_dual_orientation_fails(self) -> None:
        self.assert_mutation_fails(
            "W=\\sum_{c=1}^7\\operatorname{im}P_{tc}=\\operatorname{im}N_t^*",
            "W=\\ker N_t",
        )

    def test_arbitrary_W_boolean_step_cannot_disappear(self) -> None:
        self.assert_mutation_fails("its square is \\(2abxy\\)", "its square is zero")


if __name__ == "__main__":
    unittest.main()
