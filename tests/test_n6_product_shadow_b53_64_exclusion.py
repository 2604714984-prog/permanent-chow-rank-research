from __future__ import annotations

import importlib.util
import json
import unittest
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b53_64_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_product_shadow", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


def independent_table() -> dict[int, tuple[int, int]]:
    triples = sorted(
        combinations(range(6), 3), key=lambda s: sum(1 << x for x in s)
    )
    seen: set[tuple[int, int]] = set()
    k = [0]
    weights = []
    for triple in triples:
        pairs = set(combinations(triple, 2))
        weights.append(len(pairs - seen))
        seen.update(pairs)
        k.append(len(seen))

    @lru_cache(maxsize=None)
    def dp(i: int, last: int, remaining: int) -> tuple[int, int]:
        if i == 20:
            return (0, 1) if remaining == 0 else (10**9, 0)
        best, count = 10**9, 0
        for x in range(min(last, remaining) + 1):
            if remaining - x > x * (19 - i):
                continue
            tail, tail_count = dp(i + 1, x, remaining - x)
            value = weights[i] * k[x] + tail
            if value < best:
                best, count = value, tail_count
            elif value == best:
                count += tail_count
        return best, count

    return {b: dp(0, 20, b) for b in range(40, 66)}


class N6ProductShadowExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_one_factor_data(self) -> None:
        self.assertEqual(
            self.payload["one_factor_initial_shadow_sizes_k_0_through_20"],
            [0, 3, 5, 6, 6, 8, 9, 9, 10, 10, 10, 12, 13, 13, 14, 14, 14, 15, 15, 15, 15],
        )
        self.assertEqual(
            self.payload["first_occurrence_weight_vector"],
            [3, 2, 1, 0, 2, 1, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        )

    def test_independent_dynamic_program(self) -> None:
        rebuilt = independent_table()
        frozen = {
            row["middle_intersection_dimension_b"]: (
                row["exact_product_shadow_minimum"],
                row["minimizing_ferrers_partition_count"],
            )
            for row in self.payload["rows"]
        }
        self.assertEqual(rebuilt, frozen)

    def test_b60_and_excluded_range(self) -> None:
        self.assertEqual(
            self.payload["b60_summary"],
            {
                "minimum": 84,
                "minimizer_count": 30,
                "first_witness": [16, 16, 16, 12] + [0] * 16,
            },
        )
        self.assertEqual(
            self.payload["excluded_middle_dimensions"], list(range(53, 65))
        )
        b60 = self.payload["rows"][20]
        self.assertEqual(b60["memoized_dp_state_count"], 2309)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("do not exclude b=45,...,52", boundary)
        self.assertIn("do not", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
