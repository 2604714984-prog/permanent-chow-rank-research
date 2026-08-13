from __future__ import annotations

import importlib.util
import json
import unittest
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
FROZEN = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_lower29_fixed_six_arithmetic", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


def independent_shadow(total: int) -> int:
    triples = sorted(combinations(range(6), 3), key=lambda s: sum(1 << x for x in s))
    seen: set[tuple[int, int]] = set()
    sizes = [0]
    weights = []
    for triple in triples:
        pairs = set(combinations(triple, 2))
        weights.append(len(pairs - seen))
        seen.update(pairs)
        sizes.append(len(seen))

    @lru_cache(maxsize=None)
    def dp(index: int, previous: int, remaining: int) -> int:
        if index == 20:
            return 0 if remaining == 0 else 10**9
        best = 10**9
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (19 - index):
                continue
            best = min(best, weights[index] * sizes[value] + dp(index + 1, value, remaining - value))
        return best

    return dp(0, 20, total)


class N6Lower29FixedSixArithmeticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_low_rank_and_rank_twenty_window(self) -> None:
        rows = self.payload["low_maximum_rank_branches"]
        self.assertEqual(
            [(row["maximum_middle_rank_r"], row["scalar_feasibility_forces_b_at_least"], row["product_shadow_allows_b_at_most"]) for row in rows],
            [(16, 67, 31), (17, 56, 31), (18, 45, 41)],
        )
        self.assertEqual(self.payload["rank_twenty_scalar_window"], [22, 52])

    def test_independent_plateau_shadows(self) -> None:
        self.assertEqual(
            {dimension: independent_shadow(dimension) for dimension in range(47, 53)},
            {47: 75, 48: 75, 49: 75, 50: 75, 51: 78, 52: 78},
        )

    def test_literal_six_endpoints(self) -> None:
        rows = {row["b"]: row for row in self.payload["literal_six_frontier"]}
        self.assertEqual((rows[28]["literal_six_intersection_floor"], rows[28]["exact_product_shadow_at_floor"]), (52, 78))
        self.assertEqual((rows[29]["literal_six_intersection_floor"], rows[29]["exact_product_shadow_at_floor"]), (51, 78))
        self.assertEqual((rows[30]["literal_six_intersection_floor"], rows[30]["exact_product_shadow_at_floor"]), (50, 75))
        self.assertEqual((rows[32]["literal_six_intersection_floor"], rows[32]["exact_product_shadow_at_floor"]), (48, 75))
        self.assertEqual((rows[33]["literal_six_intersection_floor"], rows[33]["exact_product_shadow_at_floor"]), (47, 75))

    def test_q_frontier_has_no_strict_contradiction(self) -> None:
        rows = self.payload["q_frontier_before_ambient_cap_saturation"]
        self.assertEqual([row["b"] for row in rows], list(range(28, 47)))
        self.assertFalse(any(row["strict_shadow_contradiction"] for row in rows))
        by_b = {row["b"]: row for row in rows}
        self.assertEqual(
            (by_b[34]["best_q_before_ambient_cap_saturation"], by_b[34]["literal_q_intersection_floor"], by_b[34]["exact_product_shadow_at_floor"]),
            (7, 66, 87),
        )
        self.assertEqual(
            (by_b[35]["best_q_before_ambient_cap_saturation"], by_b[35]["literal_q_intersection_floor"], by_b[35]["exact_product_shadow_at_floor"]),
            (7, 65, 87),
        )
        self.assertEqual(
            (by_b[37]["best_q_before_ambient_cap_saturation"], by_b[37]["literal_q_intersection_floor"], by_b[37]["exact_product_shadow_at_floor"]),
            (7, 63, 84),
        )
        self.assertEqual(
            (by_b[38]["best_q_before_ambient_cap_saturation"], by_b[38]["literal_q_intersection_floor"], by_b[38]["exact_product_shadow_at_floor"]),
            (7, 62, 84),
        )

    def test_open_boundary_keeps_47_48_49(self) -> None:
        self.assertEqual(self.payload["open_b_after_current_proved_interfaces"], list(range(31, 50)))
        high = {row["b"]: row["status_after_existing_term_caps"] for row in self.payload["high_layers"]}
        self.assertTrue(all("remains_open" in high[b] for b in (47, 48, 49)))
        self.assertIn("does not exclude b=31,...,49", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
