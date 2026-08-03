from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.multishadow import (  # noqa: E402
    REVIEWED_GENERAL_WITNESSES,
    best_general_grid_certificate,
    koszul_data,
    multishadow_bound_at,
    reviewed_general_certificates,
)


class GeneralMultishadowTests(unittest.TestCase):
    def test_reviewed_values(self) -> None:
        expected = {
            4: (2, 2, 2, 6, 6, 8),
            5: (2, 3, 4, 19, 9, 13),
            6: (3, 3, 4, 40, 19, 23),
            7: (3, 4, 13, 274, 28, 41),
            8: (4, 4, 12, 496, 64, 76),
            9: (4, 5, 43, 3_607, 98, 141),
            10: (5, 5, 42, 7_084, 225, 267),
            11: (5, 6, 175, 60_479, 331, 506),
            12: (6, 6, 179, 125_640, 789, 968),
            13: (6, 7, 668, 907_508, 1_185, 1_853),
            14: (7, 7, 623, 1_673_882, 2_945, 3_568),
            15: (7, 8, 2_388, 12_460_405, 4_491, 6_879),
            16: (8, 8, 2_422, 25_470_785, 10_890, 13_312),
        }
        actual = {
            certificate.n: (
                certificate.output_degree,
                certificate.complementary_degree,
                certificate.fixed_terms,
                certificate.complementary_intersection_cap,
                certificate.residual_term_count,
                certificate.lower_bound,
            )
            for certificate in reviewed_general_certificates()
        }
        self.assertEqual(actual, expected)

    def test_odd_n_certificates(self) -> None:
        for n in range(5, 16, 2):
            output_degree, witness = REVIEWED_GENERAL_WITNESSES[n]
            certificate = multishadow_bound_at(n, output_degree, witness)
            self.assertEqual(output_degree, n // 2)
            self.assertEqual(certificate.complementary_degree, n // 2 + 1)
            self.assertGreater(certificate.lower_bound, certificate.global_koszul_bound)

    def test_n7_exact_arithmetic(self) -> None:
        output_degree, witness = REVIEWED_GENERAL_WITNESSES[7]
        certificate = multishadow_bound_at(7, output_degree, witness)
        derivative_dimension, target_rank, term_cap = koszul_data(7, 3)
        self.assertEqual((derivative_dimension, target_rank, term_cap), (35, 58_800, 1_680))
        self.assertEqual(certificate.fixed_terms, 13)
        self.assertEqual(certificate.complementary_intersection_cap, 274)
        self.assertEqual(certificate.residual_koszul_rank_floor, 45_374)
        self.assertEqual(certificate.residual_term_count, 28)
        self.assertEqual(certificate.lower_bound, 41)

    def test_grid_search_is_nonregressive(self) -> None:
        for n in range(4, 11):
            certificate = best_general_grid_certificate(n, 16)
            self.assertGreaterEqual(
                certificate.lower_bound,
                certificate.global_koszul_bound,
            )
        self.assertGreaterEqual(best_general_grid_certificate(5, 64).lower_bound, 13)
        self.assertGreaterEqual(best_general_grid_certificate(7, 64).lower_bound, 41)

    def test_frozen_json_matches_live_certificates(self) -> None:
        payload = json.loads(
            (ROOT / "data" / "multishadow_bounds.json").read_text(
                encoding="utf-8"
            )
        )
        frozen = {row["n"]: row for row in payload["certificates"]}
        live = {certificate.n: certificate for certificate in reviewed_general_certificates()}
        self.assertEqual(set(frozen), set(live))
        for n, certificate in live.items():
            row = frozen[n]
            self.assertEqual(row["output_degree"], certificate.output_degree)
            self.assertEqual(
                row["complementary_degree"],
                certificate.complementary_degree,
            )
            self.assertEqual(row["fixed_terms"], certificate.fixed_terms)
            self.assertEqual(
                row["complementary_intersection_cap"],
                certificate.complementary_intersection_cap,
            )
            self.assertEqual(row["lower_bound"], certificate.lower_bound)

    def test_invalid_parameters_fail_closed(self) -> None:
        output_degree, witness = REVIEWED_GENERAL_WITNESSES[5]
        with self.assertRaises(ValueError):
            multishadow_bound_at(3, 1, witness)
        with self.assertRaises(ValueError):
            multishadow_bound_at(5, 1, witness)
        with self.assertRaises(ValueError):
            multishadow_bound_at(5, 4, witness)
        with self.assertRaises(ValueError):
            multishadow_bound_at(5, output_degree, 2)
        with self.assertRaises(ValueError):
            best_general_grid_certificate(5, 0)


if __name__ == "__main__":
    unittest.main()
