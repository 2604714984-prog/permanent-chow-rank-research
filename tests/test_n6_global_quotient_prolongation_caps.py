from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_global_quotient_prolongation_caps.py"
FROZEN = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_global_caps", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6GlobalQuotientProlongationCapsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_complete_fixed_point_caps(self) -> None:
        audit = self.payload["fixed_point_cap_audit"]
        self.assertEqual(audit["quadratic_quotient_dimension"], 441)
        self.assertEqual(audit["local_quotient_axis_count"], 18)
        self.assertEqual(audit["fixed_W_count"], 18_564)
        self.assertEqual(audit["fixed_W_orbit_representative_count"], 1_683)
        self.assertEqual(
            audit["characteristic_zero_prolongation_upper_caps"],
            {"12": 436, "13": 440, "14": 448},
        )

    def test_orbit_and_pair_partitions(self) -> None:
        audit = self.payload["fixed_point_cap_audit"]
        orbit_histogram = audit["fixed_W_orbit_size_histogram"]
        self.assertEqual(
            sum(int(size) * count for size, count in orbit_histogram.items()),
            18_564,
        )
        pair_histogram = audit[
            "ambient_axis_pair_shared_cubic_block_histogram"
        ]
        self.assertEqual(sum(pair_histogram.values()), 97_020)

    def test_state_exclusion_counts_and_ids(self) -> None:
        rows = self.payload["state_exclusions"]
        self.assertEqual(
            [
                (
                    row["b"],
                    row["canonical_state_count"],
                    row["excluded_state_count"],
                    row["remaining_state_count"],
                )
                for row in rows
            ],
            [(61, 73, 61, 12), (62, 11, 10, 1), (63, 11, 10, 1)],
        )
        self.assertEqual(rows[0]["excluded_state_ids"][0], "b61_state_000")
        self.assertEqual(rows[0]["excluded_state_ids"][-1], "b61_state_060")
        self.assertEqual(rows[1]["remaining_states"][0]["state_id"], "b62_state_010")
        self.assertEqual(rows[2]["remaining_states"][0]["state_id"], "b63_state_010")

    def test_claim_boundary(self) -> None:
        self.assertIn("remaining counts are 12,1,1", self.payload["strict_conclusion"])
        self.assertIn("does not yet prove", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
