from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.even_multishadow import (  # noqa: E402
    REVIEWED_WITNESSES,
    best_rational_grid_certificate,
    central_koszul_data,
    central_koszul_lower_bound,
    even_multishadow_bound_at,
    generalized_binomial,
    reviewed_even_certificates,
)


class EvenMultishadowTests(unittest.TestCase):
    def test_generalized_binomial(self) -> None:
        for n in range(2, 20):
            for r in range(n + 1):
                self.assertEqual(generalized_binomial(Fraction(n), r), comb(n, r))
        self.assertEqual(generalized_binomial(Fraction(9, 2), 2), Fraction(63, 8))
        self.assertEqual(generalized_binomial(Fraction(9, 2), 3), Fraction(105, 16))

    def test_reviewed_certificate_values(self) -> None:
        expected = {
            4: (2, 6, 464, 6, 8),
            6: (4, 40, 12_735, 19, 23),
            8: (12, 496, 278_720, 64, 76),
            10: (42, 7_084, 5_597_900, 225, 267),
            12: (179, 125_640, 104_224_320, 789, 968),
            14: (623, 1_673_882, 1_971_511_423, 2_945, 3_568),
            16: (2_422, 25_470_785, 35_751_651_840, 10_890, 13_312),
        }
        actual = {
            certificate.n: (
                certificate.fixed_terms,
                certificate.intersection_dimension_cap,
                certificate.residual_koszul_rank_floor,
                certificate.residual_term_count,
                certificate.lower_bound,
            )
            for certificate in reviewed_even_certificates()
        }
        self.assertEqual(actual, expected)

    def test_frozen_json_matches_exact_certificates(self) -> None:
        payload = json.loads(
            (ROOT / "data" / "even_multishadow_bounds.json").read_text(
                encoding="utf-8"
            )
        )
        frozen = {row["n"]: row for row in payload["certificates"]}
        live = {certificate.n: certificate for certificate in reviewed_even_certificates()}
        self.assertEqual(set(frozen), set(live))
        for n, certificate in live.items():
            row = frozen[n]
            self.assertEqual(row["witness"], str(certificate.witness))
            self.assertEqual(row["fixed_terms"], certificate.fixed_terms)
            self.assertEqual(
                row["intersection_dimension_cap"],
                certificate.intersection_dimension_cap,
            )
            self.assertEqual(
                row["residual_koszul_rank_floor"],
                certificate.residual_koszul_rank_floor,
            )
            self.assertEqual(row["lower_bound"], certificate.lower_bound)

    def test_n6_arithmetic_certificate(self) -> None:
        certificate = even_multishadow_bound_at(6, REVIEWED_WITNESSES[6])
        central_dimension, target_rank, term_cap = central_koszul_data(6)
        self.assertEqual((central_dimension, target_rank, term_cap), (20, 14_175, 705))
        self.assertEqual(central_koszul_lower_bound(6), 21)
        self.assertEqual(certificate.fixed_terms, 4)
        self.assertEqual(certificate.intersection_dimension_cap, 40)
        self.assertEqual(
            certificate.residual_koszul_rank_floor,
            14_175 - 36 * 40,
        )
        self.assertEqual(certificate.residual_term_count, 19)
        self.assertEqual(certificate.lower_bound, 23)

    def test_exact_rational_grid_is_nonregressive(self) -> None:
        self.assertEqual(best_rational_grid_certificate(4, 32).lower_bound, 8)
        self.assertEqual(best_rational_grid_certificate(6, 32).lower_bound, 23)
        self.assertEqual(best_rational_grid_certificate(8, 64).lower_bound, 76)
        for n in range(4, 18, 2):
            self.assertGreaterEqual(
                best_rational_grid_certificate(n, 16).lower_bound,
                central_koszul_lower_bound(n),
            )

    def test_invalid_witnesses_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            even_multishadow_bound_at(5, Fraction(4))
        with self.assertRaises(ValueError):
            even_multishadow_bound_at(6, Fraction(5, 2))
        with self.assertRaises(ValueError):
            even_multishadow_bound_at(6, Fraction(7))
        with self.assertRaises(ValueError):
            best_rational_grid_certificate(6, 0)


if __name__ == "__main__":
    unittest.main()
