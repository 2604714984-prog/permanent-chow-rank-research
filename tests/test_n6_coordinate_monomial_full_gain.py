from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_coordinate_monomial_full_gain_audit.py"
FROZEN = ROOT / "data" / "n6_coordinate_monomial_full_gain.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_coordinate_monomial_full_gain_audit",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load coordinate-monomial audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6CoordinateMonomialFullGainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_frozen_json_matches_full_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)

    def test_all_coordinate_orbits_have_full_gain(self) -> None:
        self.assertEqual(self.payload["coordinate_monomial_orbits"], 167)
        self.assertEqual(
            self.payload["rectangle_orbit_distribution"],
            {"0": 151, "1": 15, "3": 1},
        )

        for row in self.payload["multiplicity_partition_certificates"].values():
            self.assertEqual(
                row["exact_quotient_koszul_gain"],
                row["exact_term_koszul_rank"],
            )

    def test_k23_exact_minors(self) -> None:
        certificate = self.payload["k23_exact_minor_certificate"]
        self.assertEqual(
            certificate,
            {
                "quadratic_first_koszul_minor_order": 18,
                "quadratic_first_koszul_minor_determinant": -1,
                "next_koszul_minor_order": 45,
                "next_koszul_minor_determinant": -1,
            },
        )

    def test_squarefree_coordinate_terms_have_full_705_gain(self) -> None:
        row = self.payload["multiplicity_partition_certificates"][
            "1,1,1,1,1,1"
        ]
        self.assertEqual(row["orbit_count"], 50)
        self.assertEqual(row["exact_term_koszul_rank"], 705)
        self.assertEqual(row["exact_quotient_koszul_gain"], 705)

    def test_claim_boundary_remains_fail_closed(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("coordinate fixed points only", boundary)
        self.assertIn("does not prove", boundary)


if __name__ == "__main__":
    unittest.main()
