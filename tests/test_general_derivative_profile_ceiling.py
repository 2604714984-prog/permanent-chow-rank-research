from __future__ import annotations

import importlib.util
import json
import unittest
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_derivative_profile_ceiling_audit.py"
FROZEN = ROOT / "data" / "general_derivative_profile_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_derivative_profile_ceiling_audit", SCRIPT)


class GeneralDerivativeProfileCeilingTests(unittest.TestCase):
    def test_small_profiles(self) -> None:
        self.assertEqual(AUDIT.term_profile(3), [1, 3, 3, 1])
        self.assertEqual(AUDIT.permanent_profile(3), [1, 9, 9, 1])
        self.assertEqual(AUDIT.term_profile(5), [1, 5, 10, 10, 5, 1])
        self.assertEqual(
            AUDIT.permanent_profile(5),
            [1, 25, 100, 100, 25, 1],
        )

    def test_coordinatewise_ceiling_and_equality_degrees(self) -> None:
        for n in range(2, 31):
            chow = AUDIT.term_profile(n)
            permanent = AUDIT.permanent_profile(n)
            bound = AUDIT.central_bound(n)
            equality = []
            for m in range(n + 1):
                self.assertLessEqual(permanent[m], bound * chow[m])
                if permanent[m] == bound * chow[m]:
                    equality.append(m)
            self.assertEqual(equality, AUDIT.central_degrees(n))

    def test_all_degree_direct_sum_is_not_optimal(self) -> None:
        for n in range(2, 31):
            row = AUDIT.validate_degree(n)
            ratio = row["all_degree_direct_sum_ratio"]
            numerator = ratio["numerator"]
            denominator = ratio["denominator"]
            self.assertLess(numerator, AUDIT.central_bound(n) * denominator)

    def test_exhaustive_boolean_weight_supports(self) -> None:
        # Recheck a separate range in the unit test rather than trusting the
        # frozen count from build_payload().
        checked = 0
        for n in range(2, 9):
            central = set(AUDIT.central_degrees(n))
            bound = AUDIT.central_bound(n)
            for bits in product((0, 1), repeat=n + 1):
                if not any(bits):
                    continue
                ratio = AUDIT.weighted_profile_ratio(n, list(bits))
                support_is_central = all(
                    m in central
                    for m, weight in enumerate(bits)
                    if weight
                )
                self.assertLessEqual(ratio, bound)
                self.assertEqual(ratio == bound, support_is_central)
                checked += 1
        self.assertEqual(checked, sum(2 ** (n + 1) - 1 for n in range(2, 9)))

    def test_glynn_gap(self) -> None:
        self.assertEqual(AUDIT.central_bound(2), 2)
        for n in range(3, 31):
            self.assertGreater(2 ** (n - 1), AUDIT.central_bound(n))

    def test_frozen_payload_matches_replay(self) -> None:
        payload = AUDIT.build_payload(50)
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(payload, frozen)
        self.assertEqual(
            payload["status"],
            "GENERAL_DERIVATIVE_PROFILE_CEILING_REPLAYED",
        )
        self.assertEqual(
            payload["boolean_weight_supports_checked_through_n12"],
            16_365,
        )
        self.assertEqual(payload["validated_degree_count"], 49)


if __name__ == "__main__":
    unittest.main()
