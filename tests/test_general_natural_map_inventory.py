import json
import unittest

from scripts.general_natural_map_inventory import DEFAULT_JSON, build_payload


class NaturalMapInventoryTests(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(DEFAULT_JSON.read_text(encoding="utf-8"))
        self.assertEqual(build_payload(), expected)

    def test_route_boundaries_are_explicit(self):
        payload = build_payload()
        self.assertIsNone(payload["route_decision"]["promoted_candidate"])
        self.assertEqual(len(payload["entries"]), 6)
        self.assertTrue(all("boundary" in entry for entry in payload["entries"]))

    def test_exact_known_values(self):
        payload = build_payload()
        homology = next(item for item in payload["entries"] if "homology" in item["name"])
        self.assertEqual(homology["permanent_rank"], 127125)
        self.assertEqual(homology["one_term_rank"], 8730)
        self.assertEqual(homology["integer_ratio_lower_bound"], 15)
        wedge = next(item for item in payload["entries"] if "higher-wedge" in item["name"])
        self.assertEqual([row["integer_ratio_lower_bound"] for row in wedge["rows"]], [15, 21, 16])


if __name__ == "__main__":
    unittest.main()
