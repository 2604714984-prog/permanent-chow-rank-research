from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_second_koszul_homology_audit.py"
FROZEN = ROOT / "data" / "n6_second_koszul_homology_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_second_koszul_homology_audit", SCRIPT)


class N6SecondKoszulHomologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_output_degree_two_closure(self) -> None:
        self.assertEqual(
            self.payload["permanent"][
                "quadratic_homology_dimension_beta_2_4"
            ],
            450,
        )
        self.assertEqual(
            self.payload["permanent"][
                "exact_characteristic_zero_second_koszul_rank"
            ],
            127_125,
        )
        self.assertEqual(
            self.payload["single_independent_chow_term"][
                "quadratic_homology_dimension_beta_2_4"
            ],
            15,
        )
        self.assertEqual(
            self.payload["single_independent_chow_term"][
                "exact_characteristic_zero_second_koszul_rank"
            ],
            8_730,
        )
        self.assertEqual(
            self.payload["certified_integer_rank_ratio_lower_bound"],
            15,
        )

    def test_common_factor_family_exact_formula(self) -> None:
        rows = self.payload["common_factor_family"]["rows"]
        self.assertEqual(
            [row["exact_quadratic_homology_dimension"] for row in rows],
            [15, 55, 120, 210, 325, 465],
        )
        self.assertEqual(
            [row["exact_characteristic_zero_second_koszul_rank"] for row in rows],
            [8_730, 17_435, 26_115, 34_770, 43_400, 52_005],
        )
        self.assertTrue(
            all(
                row["modular_second_koszul_rank"]
                == row["exact_characteristic_zero_second_koszul_rank"]
                for row in rows
            )
        )
        self.assertGreater(
            rows[-1]["exact_quadratic_homology_dimension"],
            self.payload["permanent"][
                "quadratic_homology_dimension_beta_2_4"
            ],
        )

    def test_route_is_fail_closed(self) -> None:
        decision = self.payload["route_decision"]
        self.assertEqual(decision["output_degree_two_rank_window"], "closed_exactly")
        self.assertEqual(decision["base_rank_ratio"], "no_improvement_over_15")
        self.assertEqual(
            decision["scalar_homology_dimension"],
            "rejected_as_a_monotone_upper_bound_route_for_lower_26",
        )
        self.assertEqual(
            decision["multigraded_or_representation_structure"],
            "open_not_promoted",
        )
        self.assertEqual(decision["route_selected"], "none")

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
