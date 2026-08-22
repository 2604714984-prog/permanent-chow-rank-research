from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower28_fixed_six_partial.py"
FROZEN = ROOT / "data" / "n6_lower28_fixed_six_partial.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_lower28_partial", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


def independent_shadow(total: int) -> int:
    triples = sorted(combinations(range(6), 3), key=lambda s: sum(1 << x for x in s))
    seen = set()
    k = [0]
    weights = []
    for triple in triples:
        pairs = set(combinations(triple, 2))
        weights.append(len(pairs - seen))
        seen.update(pairs)
        k.append(len(seen))

    @lru_cache(maxsize=None)
    def dp(i: int, last: int, remaining: int) -> int:
        if i == 20:
            return 0 if remaining == 0 else 10**9
        values = []
        for x in range(min(last, remaining) + 1):
            if remaining - x <= x * (19 - i):
                values.append(weights[i] * k[x] + dp(i + 1, x, remaining - x))
        return min(values)

    return dp(0, 20, total)


class N6Lower28FixedSixPartialTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_low_maximum_rank_branches(self) -> None:
        rows = self.payload["low_maximum_rank_branches_excluded"]
        observed = [
            (
                row["maximum_individual_middle_rank"],
                row["global_extra_span_z_upper"],
                row["selected_six_middle_rank_lower"],
                row["selected_six_intersection_b_lower"],
                row["fixed_six_quadratic_projection_cap"],
                row["exact_product_shadow_at_b_lower"],
            )
            for row in rows
        ]
        self.assertEqual(
            observed,
            [(16, 16, 90, 74, 58, 90), (17, 29, 91, 62, 58, 84), (18, 43, 92, 49, 68, 75)],
        )

    def test_independent_shadows_and_integer_table(self) -> None:
        rows = self.payload["remaining_integer_rows"]
        self.assertEqual([row["b"] for row in rows], list(range(34, 53)))
        for row in rows:
            self.assertEqual(row["exact_product_shadow_minimum"], independent_shadow(row["b"]))
            expected_selection = AUDIT.ceiling(Fraction(860 - 5 * row["b"], 8))
            self.assertEqual(row["selection_middle_rank_lower"], expected_selection)
        self.assertEqual(
            [row["combined_middle_rank_lower"] for row in rows],
            [87, 86, 85, 85, 84, 84, 83, 82, 88, 88, 98, 98, 98, 112, 112, 112, 112, 120, 120],
        )
        self.assertTrue(all(row["gap_lower_minus_upper"] < 0 for row in rows))

    def test_b34_endpoint(self) -> None:
        endpoint = self.payload["closest_endpoint_b34"]
        self.assertEqual(endpoint["selected_six_middle_rank_integer_window"], [87, 88])
        self.assertEqual(endpoint["residual_middle_rank_lower_if_h87"], 419)
        self.assertEqual(endpoint["h87_relation_pairing_loss_rho_plus_delta_upper"], 1)
        self.assertEqual(endpoint["h88_residual_middle_rank_exact"], 420)
        self.assertEqual(endpoint["h88_relation_dimension_rho"], 0)

    def test_high_layer_pruning(self) -> None:
        pruning = self.payload["high_layer_prolongation_pruning"]
        histogram = {
            layer["b"]: (layer["scalar_case_count"], layer["excluded_case_count"])
            for layer in pruning["layers"]
        }
        self.assertEqual(histogram, {47: (1, 1), 48: (4, 4), 49: (9, 9), 50: (13, 12), 51: (1, 1), 52: (1, 1)})
        survivor = pruning["remaining_b50_scalar_endpoint"]
        self.assertEqual(survivor["epsilon"], [0] * 6)
        self.assertEqual(survivor["alpha"], [3] * 6)
        self.assertEqual((survivor["d2"], survivor["a2"], survivor["t2"], survivor["h"]), (90, 75, 15, 120))
        self.assertEqual(
            self.payload["remaining_intersection_layers_after_existing_caps"],
            list(range(34, 47)) + [50],
        )

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude", boundary)
        self.assertIn("does not", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
