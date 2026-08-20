from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_all_koszul_young_ceiling.py"
FROZEN = ROOT / "data" / "n6_all_koszul_young_ceiling.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "n6_all_koszul_young_ceiling",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6AllKoszulYoungCeilingTests(unittest.TestCase):
    def test_exact_internal_term_table(self) -> None:
        self.assertEqual(
            AUDIT.internal_rank_table(),
            {
                1: [6, 15, 20, 15, 6, 1, 0],
                2: [15, 70, 105, 84, 35, 6, 0],
                3: [20, 105, 216, 190, 84, 15, 0],
                4: [15, 84, 190, 216, 105, 20, 0],
                5: [6, 35, 84, 105, 70, 15, 0],
                6: [1, 6, 15, 20, 15, 6, 0],
            },
        )

    def test_exactness_bridges(self) -> None:
        self.assertEqual(
            AUDIT.HEAVY_EXPECTED[(5, 2)],
            36 * AUDIT.comb(36, 2) - 36,
        )

    def test_weight_orbit_compression_matches_uncompressed_small_cases(self) -> None:
        for output_degree, wedge_degree in ((1, 0), (1, 1), (2, 1)):
            with self.subTest(output_degree=output_degree, wedge_degree=wedge_degree):
                compressed = AUDIT.permanent_rank(output_degree, wedge_degree)
                uncompressed = AUDIT.permanent_rank(
                    output_degree,
                    wedge_degree,
                    orbit_compression=False,
                )
                self.assertEqual(compressed, uncompressed)

    def test_heavy_orbit_representative_counts(self) -> None:
        self.assertEqual(
            len(AUDIT.descriptor_blocks(5, 2, orbit_compression=True)),
            8,
        )
        self.assertEqual(
            len(AUDIT.descriptor_blocks(4, 3, orbit_compression=True)),
            31,
        )
        self.assertEqual(
            len(AUDIT.descriptor_blocks(2, 3, orbit_compression=True)),
            31,
        )
        self.assertEqual(
            AUDIT.HEAVY_EXPECTED[(4, 3)],
            AUDIT.comb(6, 4) ** 2 * AUDIT.comb(36, 3)
            - AUDIT.HEAVY_EXPECTED[(5, 2)],
        )

    def test_every_refined_candidate_is_strictly_below_26(self) -> None:
        payload = AUDIT.build_payload(False)
        self.assertEqual(
            [
                (row["output_degree"], row["wedge_degree"])
                for row in payload["raw_dimension_candidates_above_26"]
            ],
            [(3, p) for p in range(10, 15)]
            + [(4, p) for p in range(21, 26)],
        )
        for row in payload["refined_representatives"]:
            self.assertGreater(row["margin_below_26_terms"], 0)
            self.assertLess(
                Fraction(
                    row["permanent_rank_upper"],
                    row["single_term_rank"],
                ),
                26,
            )
        self.assertLess(
            Fraction(*payload["global_strict_ratio_upper"]),
            26,
        )

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        actual = json.loads(json.dumps(AUDIT.build_payload(False)))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
