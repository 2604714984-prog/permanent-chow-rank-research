from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_relation_tableau_audit.py"
FROZEN = ROOT / "data" / "general_relation_tableau_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_relation_tableau_audit", SCRIPT)


class GeneralRelationTableauTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_macaulay_composition(self) -> None:
        rows = self.payload["macaulay_two_step_0_through_37"]
        self.assertEqual(rows[16]["kappa_3_cap"], 36)
        self.assertEqual(rows[16]["kappa_4_cap"], 71)
        self.assertEqual(rows[37]["kappa_3_cap"], 121)
        self.assertEqual(rows[37]["kappa_4_cap"], 331)

    def test_squarefree_overlap_ranks(self) -> None:
        rows = self.payload["squarefree_degree_six_pair_overlaps"]
        self.assertEqual([row["formula_rank"] for row in rows], [40, 40, 40, 38, 32, 20, 20])
        self.assertEqual([row["rank_mod_1000003"] for row in rows], [40, 40, 40, 38, 32, 20, 20])
        self.assertTrue(rows[4]["strict_nonmerge_two_term_example"])
        self.assertEqual(rows[4]["relation_pairing_rank"], 0)

    def test_repeated_and_common_factor_boundaries(self) -> None:
        for row in self.payload["repeated_term_boundary"]:
            self.assertEqual(row["coupled_rank"], 20)
        for row in self.payload["common_factor_boundary"]:
            self.assertEqual(row["kappa_2"], 0)
            self.assertEqual(row["kappa_3"], 0)
            self.assertEqual(row["kappa_4"], 0)

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
