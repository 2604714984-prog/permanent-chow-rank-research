from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.multishadow_asymptotics import (  # noqa: E402
    EVEN_DEFECT_WITNESS,
    ODD_DEFECT_WITNESS,
    asymptotic_diagnostic,
    even_limiting_constant,
    even_offset_objective,
    even_optimal_defect,
    odd_limiting_constant,
    odd_offset_objective,
    odd_optimal_defect,
    parity_asymptotic_certificate,
    parity_defect_witness,
    reviewed_asymptotic_diagnostics,
)


class MultishadowAsymptoticTests(unittest.TestCase):
    def test_analytic_optimizer_values(self) -> None:
        self.assertAlmostEqual(
            even_offset_objective(0, even_optimal_defect()),
            even_limiting_constant(),
            places=13,
        )
        self.assertAlmostEqual(
            odd_offset_objective(0, odd_optimal_defect()),
            odd_limiting_constant(),
            places=13,
        )
        self.assertAlmostEqual(
            odd_limiting_constant(),
            2.0 * even_limiting_constant(),
            places=13,
        )

    def test_central_offset_dominates_fixed_offsets(self) -> None:
        even_best = even_limiting_constant()
        odd_best = odd_limiting_constant()
        # This is a numerical regression for the closed formulas proved in the
        # note, not a substitute for the calculus argument.
        for offset in range(-8, 9):
            for index in range(0, 4001):
                defect = index / 1000.0
                value_even = even_offset_objective(offset, defect)
                value_odd = odd_offset_objective(offset, defect)
                self.assertLessEqual(value_even, even_best + 1e-12)
                self.assertLessEqual(value_odd, odd_best + 1e-12)

    def test_rational_defect_selection(self) -> None:
        self.assertEqual(parity_defect_witness(20), EVEN_DEFECT_WITNESS)
        self.assertEqual(parity_defect_witness(21), ODD_DEFECT_WITNESS)
        self.assertLess(abs(float(EVEN_DEFECT_WITNESS) - even_optimal_defect()), 1e-9)
        self.assertLess(abs(float(ODD_DEFECT_WITNESS) - odd_optimal_defect()), 1e-9)

    def test_exact_finite_additive_gains(self) -> None:
        expected = {
            20: 4_961,
            21: 17_368,
            40: 1_839_198_345,
            41: 6_883_586_235,
            80: 715_116_497_355_338_793_509,
            81: 2_767_410_273_952_600_090_694,
            120: 428_051_355_842_643_783_932_833_713_089_960,
            121: 1_674_952_182_728_949_172_634_479_266_492_768,
        }
        actual = {
            diagnostic.n: diagnostic.additive_gain
            for diagnostic in reviewed_asymptotic_diagnostics()
        }
        self.assertEqual(actual, expected)

    def test_scaled_gains_track_the_parity_limits(self) -> None:
        even_values = [
            float(asymptotic_diagnostic(n).scaled_gain)
            for n in (20, 40, 80, 120)
        ]
        odd_values = [
            float(asymptotic_diagnostic(n).scaled_gain)
            for n in (21, 41, 81, 121)
        ]
        self.assertEqual(even_values, sorted(even_values, reverse=True))
        self.assertEqual(odd_values, sorted(odd_values))
        self.assertLess(abs(even_values[-1] - even_limiting_constant()), 0.002)
        self.assertLess(abs(odd_values[-1] - odd_limiting_constant()), 0.005)

    def test_finite_certificates_are_exact_multishadow_certificates(self) -> None:
        for n in (20, 21, 40, 41):
            certificate = parity_asymptotic_certificate(n)
            diagnostic = asymptotic_diagnostic(n)
            self.assertEqual(certificate.output_degree, n // 2)
            self.assertEqual(certificate.lower_bound, diagnostic.multishadow_lower_bound)
            self.assertEqual(certificate.fixed_terms, diagnostic.fixed_terms)
            self.assertEqual(
                certificate.complementary_intersection_cap,
                diagnostic.intersection_cap,
            )

    def test_invalid_degree_fails_closed(self) -> None:
        with self.assertRaises(ValueError):
            parity_defect_witness(3)
        with self.assertRaises(ValueError):
            parity_defect_witness(True)


if __name__ == "__main__":
    unittest.main()
