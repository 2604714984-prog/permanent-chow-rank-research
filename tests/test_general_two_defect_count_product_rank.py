from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_two_defect_count_product_rank_audit.py"
FROZEN = ROOT / "data" / "general_two_defect_count_product_rank_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_defect_count_product_rank_audit", SCRIPT)


class GeneralTwoDefectCountProductRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_local_catalog_and_orientation(self) -> None:
        local = self.payload["local_support_certificate"]
        self.assertEqual(local["compatible_supports"], {"1": 0, "2": 1, "3": 18})
        self.assertEqual(local["genuine_supports"], {"1": 0, "2": 1, "3": 11})
        self.assertTrue(local["both_endpoint_coordinates_nonpositive"])
        self.assertEqual(
            local["unique_two_atom_expression"]["support"],
            [["A", "B"], ["B", "A"]],
        )
        self.assertEqual(
            local["unique_two_atom_expression"]["coefficients"],
            ["1/4", "1/4"],
        )

    def test_equal_unary_and_star_boundary(self) -> None:
        equal = self.payload["equal_unary_certificate"]
        self.assertFalse(equal["positive_equal_unary_with_at_most_four_atoms"])
        self.assertEqual(
            equal["equal_unary_value_histogram"]["left"],
            {"-1/2": 42, "0": 10},
        )
        self.assertEqual(
            equal["equal_unary_value_histogram"]["right"],
            {"-1/2": 42, "0": 10},
        )
        self.assertEqual(
            [row["degree"] for row in self.payload["sharp_star_examples"]],
            list(range(3, 10)),
        )

    def test_exact_n4_n5_n6_replays(self) -> None:
        rows = self.payload["exact_replays"]
        self.assertEqual([row["n"] for row in rows], [4, 5, 6])
        self.assertEqual([row["fixed_base_rank"] for row in rows], [16, 25, 36])
        self.assertEqual([row["nonzero_bases"] for row in rows], [4, 8, 16])
        self.assertEqual([row["base_labelled_cost"] for row in rows], [64, 200, 576])
        self.assertEqual(
            [row["exact_post_collection_cost"] for row in rows],
            [None, 200, 576],
        )
        self.assertEqual([row["assignment_checks"] for row in rows], [256, 3125, 46656])

    def test_n6_agrees_with_existing_exhaustive_certificate(self) -> None:
        n6 = self.payload["n6_corollary"]
        self.assertEqual(n6["exact_fixed_base_rank"], 36)
        self.assertEqual(n6["exact_sixteen_base_assignment_cost"], 576)
        self.assertEqual(n6["independent_exhaustive_certificate"], "N6-023")

    def test_frozen_summary(self) -> None:
        local = self.payload["local_support_certificate"]
        equal = self.payload["equal_unary_certificate"]
        compact = {
            "status": self.payload["status"],
            "field": self.payload["field"],
            "theorem": self.payload["theorem"],
            "local_support_certificate": local,
            "equal_unary_certificate": {
                "left": equal["equal_unary_value_histogram"]["left"],
                "right": equal["equal_unary_value_histogram"]["right"],
                "positive_equal_unary_with_at_most_four_atoms": equal[
                    "positive_equal_unary_with_at_most_four_atoms"
                ],
            },
            "global_double_counting": self.payload["global_double_counting"],
            "exact_replays": self.payload["exact_replays"],
            "n6_corollary": self.payload["n6_corollary"],
            "claim_boundary": self.payload["claim_boundary"],
        }
        self.assertEqual(compact, self.frozen)


if __name__ == "__main__":
    unittest.main()
