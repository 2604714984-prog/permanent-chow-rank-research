from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_hereditary_profile_transversality.py"
FROZEN = ROOT / "data" / "general_hereditary_profile_transversality.json"

SPEC = importlib.util.spec_from_file_location(
    "general_hereditary_profile_transversality",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralHereditaryProfileTransversalityTests(unittest.TestCase):
    def test_safe_profile_witnesses(self) -> None:
        expected = {
            (7, 3): (1, 1),
            (11, 5): (2, 1),
            (15, 7): (4, 2),
            (16, 7): (3, 1),
            (32, 15): (51, 4),
        }
        observed = {}
        for key in expected:
            row = MODULE.profile_safe_omission(*key)
            observed[key] = (
                row["safe_terms"],
                row["witness_output_degree"],
            )
        self.assertEqual(observed, expected)

    def test_hereditary_basis_profiles(self) -> None:
        rows = MODULE.hereditary_profile_rows(8)
        self.assertEqual(rows[0]["derivative_profile"], [1, 4, 1])
        self.assertEqual(
            rows[-1]["derivative_profile"],
            [1, 64, 784, 3136, 4900, 3136, 784, 64, 1],
        )

    def test_general_certificate_refinements(self) -> None:
        rows = MODULE.general_certificate_rows()
        self.assertEqual(
            {row["n"]: row["hereditary_profile_lower_bound"] for row in rows},
            {
                7: 42,
                8: 77,
                9: 142,
                10: 268,
                11: 508,
                12: 970,
                13: 1855,
                14: 3570,
                15: 6883,
                16: 13315,
            },
        )
        n15 = next(row for row in rows if row["n"] == 15)
        self.assertEqual(n15["profile_witness_degree"], 2)
        self.assertEqual(n15["safe_omitted_terms"], 4)

    def test_exact_product_shadow_refinements(self) -> None:
        rows = MODULE.exact_shadow_rows()
        self.assertEqual(
            {
                row["n"]: row["hereditary_profile_exact_shadow_bound"]
                for row in rows
            },
            {7: 43, 8: 78},
        )

    def test_asymptotic_diagnostics(self) -> None:
        rows = MODULE.asymptotic_diagnostics()
        self.assertEqual(
            {row["n"]: row["safe_terms"] for row in rows},
            {16: 3, 20: 6, 24: 13, 32: 51, 40: 205, 50: 1199, 64: 14757},
        )

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, MODULE.build_payload())
        self.assertEqual(
            frozen["core_sha256"],
            "796d45fdabe16a9e27ededf53101ee144fbe8d213e274dcf8d838edb8a245b4c",
        )


if __name__ == "__main__":
    unittest.main()
