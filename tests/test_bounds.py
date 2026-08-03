from __future__ import annotations

import sys
import unittest
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.bounds import (  # noqa: E402
    best_koszul_bound,
    best_shadow_removal_bound,
    border_chow_koszul_bound,
    central_koszul_bound,
    central_koszul_closed_form_ratio,
    central_koszul_ratio,
    central_catalecticant_bound,
    derivative_shadow_per_term_cap,
    derivative_shadow_target,
    glynn_upper_bound,
    permanent_derivative_dimension,
    shadow_removal_capacity,
)


class BoundTests(unittest.TestCase):
    def test_derivative_dimensions(self) -> None:
        for n in range(3, 20):
            for m in range(n + 1):
                self.assertEqual(permanent_derivative_dimension(n, m), comb(n, m) ** 2)

    def test_known_generalized_koszul_values(self) -> None:
        expected = {
            3: 4,
            4: 7,
            5: 11,
            6: 21,
            7: 36,
            8: 71,
            9: 127,
            10: 253,
            11: 463,
            12: 925,
            13: 1718,
            14: 3434,
            15: 6440,
            16: 12875,
        }
        actual = {n: best_koszul_bound(n).lower_bound for n in expected}
        self.assertEqual(actual, expected)

    def test_known_shadow_removal_values(self) -> None:
        expected = {
            3: 4,
            4: 7,
            5: 11,
            6: 22,
            7: 37,
            8: 72,
            9: 128,
            10: 255,
            11: 466,
            12: 928,
            13: 1721,
            14: 3438,
            15: 6444,
            16: 12881,
        }
        actual = {n: best_shadow_removal_bound(n).lower_bound for n in expected}
        self.assertEqual(actual, expected)

    def test_central_plus_one_corollary(self) -> None:
        for n in range(3, 101):
            self.assertGreaterEqual(
                best_koszul_bound(n).lower_bound,
                central_catalecticant_bound(n) + 1,
            )

    def test_central_closed_form_identity(self) -> None:
        for n in range(3, 301):
            self.assertEqual(
                central_koszul_ratio(n),
                central_koszul_closed_form_ratio(n),
            )
            self.assertGreaterEqual(
                central_koszul_bound(n),
                central_catalecticant_bound(n) + 1,
            )

    def test_central_degree_is_global_optimizer(self) -> None:
        for n in range(3, 301):
            certificate = best_koszul_bound(n)
            self.assertEqual(certificate.m, (n + 1) // 2)
            self.assertEqual(certificate.lower_bound, central_koszul_bound(n))

    def test_border_certificate_matches_closed_rank_obstruction(self) -> None:
        for n in range(3, 101):
            self.assertEqual(
                border_chow_koszul_bound(n),
                best_koszul_bound(n),
            )

    def test_bounds_do_not_exceed_glynn(self) -> None:
        for n in range(3, 101):
            self.assertLessEqual(
                best_shadow_removal_bound(n).lower_bound,
                glynn_upper_bound(n),
            )

    def test_shadow_capacity_is_strict(self) -> None:
        for n in range(4, 30):
            for m in range(2, n):
                for d in range(1, n - m + 1):
                    q = shadow_removal_capacity(n, m, d)
                    target = derivative_shadow_target(n, m, d)
                    per_term = derivative_shadow_per_term_cap(n, m, d)
                    self.assertLess(q * per_term, target)
                    self.assertGreaterEqual((q + 1) * per_term, target)

    def test_n6_certificate(self) -> None:
        cert = best_shadow_removal_bound(6)
        self.assertEqual(cert.lower_bound, 22)
        self.assertEqual((cert.m, cert.derivative_order, cert.removed_terms), (3, 1, 1))


if __name__ == "__main__":
    unittest.main()
