from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_average_sign_germs.py"
FROZEN = ROOT / "data" / "n6_k32_average_sign_germs.json"

spec = importlib.util.spec_from_file_location("n6_k32_average_sign_germs", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-127 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32AverageSignGermsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_three_sign_lines_are_diagonal(self) -> None:
        for profile in self.payload["profiles"][1:]:
            self.assertEqual(profile["linear_rank"], 69)
            self.assertEqual(profile["difference_rank"], 36)
            self.assertTrue(profile["local_germ"]["swap_symmetry_forces_diagonal"])
            self.assertEqual(profile["local_germ"]["consequence_sum_rank"], 6)

    def test_all_positive_quadratic_germ(self) -> None:
        profile = self.payload["profiles"][0]
        self.assertEqual(profile["average_rank"], 34)
        self.assertEqual(profile["difference_rank"], 35)
        germ = profile["local_germ"]
        self.assertEqual(germ["quadratic_generators"], ["x1*x2"])
        self.assertEqual(germ["branch_ranks"]["diagonal"]["sum_rank"], 6)
        self.assertEqual(germ["branch_ranks"]["separating"]["sum_rank"], 9)
        self.assertTrue(germ["formal_sandwich"])


if __name__ == "__main__":
    unittest.main()
