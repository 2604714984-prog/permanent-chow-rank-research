from __future__ import annotations

import importlib.util
import json
import unittest
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_literal_six_shadow_b34_47_exclusion.py"
FROZEN = ROOT / "data" / "n6_literal_six_shadow_b34_47_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_literal_six_shadow", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


def independent_shadow_53() -> int:
    triples = sorted(
        combinations(range(6), 3), key=lambda subset: sum(1 << x for x in subset)
    )
    seen: set[tuple[int, int]] = set()
    shadows = [0]
    weights = []
    for triple in triples:
        pairs = set(combinations(triple, 2))
        weights.append(len(pairs - seen))
        seen.update(pairs)
        shadows.append(len(seen))

    @lru_cache(maxsize=None)
    def dp(index: int, previous: int, remaining: int) -> int:
        if index == 20:
            return 0 if remaining == 0 else 10**9
        best = 10**9
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (19 - index):
                continue
            best = min(
                best,
                weights[index] * shadows[value]
                + dp(index + 1, value, remaining - value),
            )
        return best

    return dp(0, 20, 53)


class N6LiteralSixShadowExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_independent_shadow_replay(self) -> None:
        self.assertEqual(independent_shadow_53(), 81)
        self.assertEqual(
            self.payload["exact_product_shadow_at_53"]["minimum"], 81
        )

    def test_every_integer_layer(self) -> None:
        rows = self.payload["rows"]
        self.assertEqual([row["b"] for row in rows], list(range(34, 48)))
        self.assertEqual(
            [row["dim_E3_intersect_literal_six_lower"] for row in rows],
            list(range(66, 52, -1)),
        )
        self.assertTrue(all(row["excluded"] for row in rows))

    def test_frontier_and_boundary(self) -> None:
        self.assertEqual(self.payload["lower_28_frontier_after_N6_060"], [50])
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude", boundary)
        self.assertIn("b=50", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
