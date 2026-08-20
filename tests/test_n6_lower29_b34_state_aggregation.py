import json
import unittest

from scripts.n6_lower29_b34_state_aggregation import DEFAULT_JSON, build_payload


class B34StateAggregationTests(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(DEFAULT_JSON.read_text(encoding="utf-8"))
        self.assertEqual(build_payload(), expected)

    def test_biflag_state_is_removed(self):
        payload = build_payload()
        closed = {
            (row["a2"], row["kappa2"], row["t2"])
            for row in payload["closed_states"]
        }
        self.assertEqual(closed, {(72, 1, 17), (72, 2, 16), (72, 3, 15)})
        self.assertEqual(payload["initial_scalar_state_count"], 10)
        self.assertEqual(payload["current_open_state_count"], 7)

    def test_current_frontier_keeps_only_a72_k0_and_a73_plus(self):
        payload = build_payload()
        states = {
            (row["a2"], row["kappa2"], row["t2"])
            for row in payload["current_open_states"]
        }
        self.assertEqual(
            states,
            {
                (72, 0, 18),
                (73, 0, 17),
                (74, 0, 16),
                (75, 0, 15),
                (73, 1, 16),
                (74, 1, 15),
                (73, 2, 15),
            },
        )


if __name__ == "__main__":
    unittest.main()
