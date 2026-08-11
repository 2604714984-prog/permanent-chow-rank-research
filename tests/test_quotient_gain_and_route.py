from __future__ import annotations

import ast
import os
import subprocess
import sys
import unittest
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SCRIPTS = ROOT / "scripts"
for path in (SRC, SCRIPTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from n6_multishadow_route_barrier import build_payload as build_route_payload  # noqa: E402
from n6_quotient_gain_audit import build_payload as build_gain_payload  # noqa: E402
from permanent_chow_rank.even_multishadow import generalized_binomial  # noqa: E402
from permanent_chow_rank.multishadow import koszul_data  # noqa: E402


class QuotientGainAndRouteTests(unittest.TestCase):
    def test_n6_one_step_route_stops_at_23(self) -> None:
        payload = build_route_payload()
        self.assertEqual(payload["maximum_certified_lower_bound_within_route"], 23)
        self.assertEqual(
            payload["maximizers"],
            [
                {
                    "output_degree": 3,
                    "fixed_terms": 4,
                    "minimum_bukh_intersection_cap": 40,
                    "residual_terms": 19,
                },
                {
                    "output_degree": 3,
                    "fixed_terms": 5,
                    "minimum_bukh_intersection_cap": 60,
                    "residual_terms": 18,
                },
            ],
        )
        self.assertEqual(
            payload["sharp_q4_coordinate_family"],
            {
                "left_family_size": 10,
                "right_family_size": 4,
                "family_size": 40,
                "left_shadow_size": 10,
                "right_shadow_size": 6,
                "simultaneous_shadow_size": 60,
            },
        )

    def test_diagonal_term_has_full_705_quotient_gain(self) -> None:
        payload = build_gain_payload()
        self.assertEqual(payload["permanent_koszul_rank_mod_prime"], 14_175)
        self.assertEqual(payload["diagonal_term_koszul_rank_mod_prime"], 705)
        self.assertEqual(payload["combined_koszul_rank_mod_prime"], 14_880)
        self.assertEqual(payload["quotient_koszul_gain_mod_prime"], 705)

    def test_quotient_gain_audit_has_no_optimized_away_asserts(self) -> None:
        script = SCRIPTS / "n6_quotient_gain_audit.py"
        tree = ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
        bare_asserts = [
            node.lineno
            for node in ast.walk(tree)
            if isinstance(node, ast.Assert)
        ]
        self.assertEqual(bare_asserts, [])

    def test_fail_closed_check_survives_optimized_mode(self) -> None:
        environment = os.environ.copy()
        python_path = [str(SCRIPTS)]
        if environment.get("PYTHONPATH"):
            python_path.append(environment["PYTHONPATH"])
        environment["PYTHONPATH"] = os.pathsep.join(python_path)
        result = subprocess.run(
            [
                sys.executable,
                "-O",
                "-c",
                (
                    "from n6_quotient_gain_audit import require_equal; "
                    "require_equal('optimized-mode probe', 1, 2)"
                ),
            ],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("optimized-mode probe mismatch", result.stderr)

    def test_odd_ratio_identity_and_local_koszul_ratio(self) -> None:
        c = Fraction(721_347_521, 1_000_000_000)
        for k in range(2, 20):
            n = 2 * k + 1
            x = Fraction(n) - c
            central = comb(n, k)
            ratio_k = generalized_binomial(x, k) / central
            ratio_k_plus_one = generalized_binomial(x, k + 1) / central
            self.assertEqual(
                ratio_k_plus_one,
                ratio_k * (1 - c / (k + 1)),
            )

            _, target_rank, term_cap = koszul_data(n, k)
            self.assertEqual(target_rank, (n * n - 1) * central**2)
            self.assertEqual(term_cap, (n * n - 1) * central)
            self.assertEqual(Fraction(target_rank, term_cap), central)


if __name__ == "__main__":
    unittest.main()
