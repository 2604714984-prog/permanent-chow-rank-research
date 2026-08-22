from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_c6_maximal_kernel_second_order.py"
DATA = ROOT / "data" / "general_quartic_c6_maximal_kernel_second_order.json"

spec = importlib.util.spec_from_file_location("c6_maximal_kernel_second_order", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load maximal C6 second-order replay")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class C6MaximalKernelSecondOrderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_noncanonical_orbits(self) -> None:
        self.assertEqual(self.payload["noncanonical_row_column_orbits"], 2)
        for representative in self.payload["representatives"]:
            self.assertEqual(representative["shared_sources"], 9)
            self.assertEqual(representative["one_factor_envelope_union"], 12)
            self.assertEqual(representative["outside_target_count"], 12)
            self.assertEqual(representative["maximum_active_source_outside_target_overlap"], 1)

    def test_all_maximal_orbits_closed(self) -> None:
        self.assertEqual(
            self.payload["all_distinct_c6_maximal_kernel_orbits"],
            "SECOND_ORDER_CLOSED",
        )
        self.assertEqual(self.payload["claim_boundary"]["mu_6_4"], "OPEN_IN_[6,7]")


if __name__ == "__main__":
    unittest.main()
