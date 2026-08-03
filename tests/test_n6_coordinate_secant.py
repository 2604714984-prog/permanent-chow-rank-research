from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_coordinate_secant_audit.py"


def load_audit_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("n6_coordinate_secant_audit", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load n6 coordinate audit module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6CoordinateSecantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_audit_module()
        cls.pair_audit = cls.module.pair_distribution()
        cls.tangent_audit = cls.module.tangent_certificate()

    def test_rank_formula_examples(self) -> None:
        self.assertEqual(self.module.line_rank_from_overlap(3, 2), 9)
        self.assertEqual(self.module.line_rank_from_overlap(2, 3), 9)
        self.assertEqual(self.module.line_rank_from_overlap(2, 2), 13)
        self.assertEqual(self.module.line_rank_from_overlap(1, 1), 17)
        self.assertEqual(self.module.line_rank_from_overlap(0, 3), 18)

    def test_complete_pair_distribution(self) -> None:
        self.assertEqual(self.pair_audit["coordinate_basis_size"], 400)
        self.assertEqual(self.pair_audit["unordered_pairs_checked"], 79_800)
        self.assertEqual(
            self.pair_audit["rank_distribution"],
            {
                "9": 3_600,
                "13": 16_200,
                "15": 3_600,
                "16": 32_400,
                "17": 16_200,
                "18": 7_800,
            },
        )
        self.assertEqual(self.pair_audit["next_rank_after_nine"], 13)

    def test_tangent_certificate(self) -> None:
        self.assertEqual(
            self.tangent_audit["tangent_map_rank_mod_prime"],
            381,
        )
        self.assertEqual(
            self.tangent_audit["affine_tangent_dimension_over_Q"],
            19,
        )
        self.assertEqual(
            self.tangent_audit["projective_tangent_dimension_over_Q"],
            18,
        )

    def test_frozen_json_matches_replay(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n6_coordinate_secant_audit.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(frozen["pair_audit"], self.pair_audit)
        self.assertEqual(frozen["tangent_audit"], self.tangent_audit)


if __name__ == "__main__":
    unittest.main()
