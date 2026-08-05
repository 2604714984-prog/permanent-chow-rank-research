from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_defect_sign_block_audit.py"
FROZEN = ROOT / "data" / "n6_two_defect_sign_block_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_two_defect_sign_block_audit", SCRIPT)


class N6TwoDefectSignBlockAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_family_and_exact_block_ranks(self) -> None:
        family = self.payload["family"]
        self.assertEqual(family["global_pairwise_function_dimension"], 406)
        self.assertEqual(family["unique_term_count"], 467_264)
        self.assertEqual(family["indexed_term_count_with_duplicates"], 491_520)
        self.assertEqual(family["exact_span_dimension"], 11_533)
        rows = family["canonical_block_rows"]
        self.assertEqual(
            [row["exact_characteristic_zero_rank"] for row in rows],
            [406, 406, 406, 322, 322, 207],
        )
        self.assertEqual(
            [row["kernel_dimension_in_pairwise_space"] for row in rows],
            [0, 0, 0, 84, 84, 199],
        )
        self.assertTrue(
            all(
                row["modular_crosscheck_rank"]
                == row["exact_characteristic_zero_rank"]
                for row in rows
            )
        )

    def test_separator_and_aggregate_representation(self) -> None:
        separator = self.payload["separator_certificate"]
        self.assertEqual(separator["zero_parity"], 7)
        self.assertEqual(separator["one_parity"], 25)
        self.assertEqual(separator["zero_fiber_values"], {"0": 1200})
        self.assertEqual(separator["one_fiber_values"], {"1": 1200})

        aggregate = self.payload["aggregate_representation_certificate"]
        self.assertEqual(
            aggregate["zero_base_labels"],
            [0, 1, 6, 7, 24, 25, 30, 31],
        )
        self.assertEqual(aggregate["nonzero_base_aggregate_count"], 24)
        self.assertEqual(aggregate["exact_assignment_checks"], 46_656)

    def test_route_is_fail_closed(self) -> None:
        decision = self.payload["route_decision"]
        self.assertFalse(decision["one_defect_32_base_support_argument_extends"])
        self.assertEqual(
            decision["two_defect_base_aggregate_support_upper_bound"],
            24,
        )
        self.assertFalse(decision["two_defect_term_support_determined"])
        self.assertFalse(decision["decomposition_with_at_most_25_terms_found"])
        self.assertFalse(decision["general_chow_rank_changed"])
        self.assertFalse(decision["broad_sparse_optimization_authorized"])

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
