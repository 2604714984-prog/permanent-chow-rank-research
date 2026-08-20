from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_individual_prolongation_barrier.py"
FROZEN = ROOT / "data" / "n6_alpha3_individual_prolongation_barrier.json"


def load_script_module():
    spec = importlib.util.spec_from_file_location("n6_alpha3_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Alpha3IndividualProlongationBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to rebuild the alpha-three certificate",
    )
    def test_full_serial_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--workers",
                "1",
                "--verify-json",
                str(FROZEN),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3_600,
        )
        self.assertIn(
            "same_row_exact_prolongation_dimension=520", completed.stdout
        )
        self.assertIn(
            "N6_ALPHA3_INDIVIDUAL_PROLONGATION_BARRIER_PASS",
            completed.stdout,
        )

    def test_coordinate_support_classification(self) -> None:
        self.assertEqual(
            self.payload["coordinate_support_count_by_rectangle_count"],
            {"0": 1_837_392, "1": 109_800, "3": 600},
        )
        self.assertEqual(
            self.payload["row_column_support_orbit_count_by_rectangle_count"],
            {"0": 76, "1": 12, "3": 2},
        )

    def test_row_multiset_permutation_weight(self) -> None:
        audit = load_script_module()
        self.assertEqual(
            audit.multiset_permutation_count((0, 0, 1, 2, 3, 4)),
            360,
        )
        self.assertEqual(audit.multiset_permutation_count((7,) * 6), 1)

    def test_precomputed_mask_permutations_preserve_canonical_form(self) -> None:
        audit = load_script_module()
        for row_masks in (
            (0, 0, 0, 1, 2, 60),
            (1, 2, 4, 8, 16, 32),
            (3, 3, 12, 12, 48, 48),
        ):
            expected = min(
                tuple(
                    sorted(
                        audit.permute_mask(mask, permutation)
                        for mask in row_masks
                    )
                )
                for permutation in audit.COLUMN_PERMUTATIONS
            )
            self.assertEqual(audit.canonical_row_masks(list(row_masks)), expected)

    def test_static_zero_elimination_is_exact(self) -> None:
        audit = load_script_module()
        constraints = {
            ("a",): {
                ("zero", 1, None),
                ("equal", 0, 1),
                ("equal", 1, 4),
                ("equal", 2, 3),
            },
            ("b",): {
                ("zero", 5, None),
                ("equal", 4, 5),
            },
        }
        live_count, rewritten = audit.live_axis_constraints(
            6, {1, 4}, constraints
        )
        self.assertEqual(live_count, 4)
        self.assertEqual(rewritten[("a",)], ((0, -1), (1, 2)))
        self.assertEqual(rewritten[("b",)], ((3, -1),))

    def test_rollback_enumerator_matches_fresh_components(self) -> None:
        audit = load_script_module()
        alpha2 = audit.load_module(audit.ALPHA2_SCRIPT, "alpha3_test_alpha2")
        base = alpha2.load_base()
        constraints = {
            ("a",): ((0, 1), (4, -1)),
            ("b",): ((1, 2),),
            ("c",): ((2, -1), (3, 4)),
            ("d",): ((0, 4), (3, -1)),
            ("e",): ((1, 3),),
        }
        for excluded_axis_count in range(len(constraints) + 1):
            observed = audit.component_cap_histogram(
                6, constraints, excluded_axis_count
            )
            histogram: Counter[int] = Counter()
            for excluded in combinations(constraints, excluded_axis_count):
                components = base.Components(6)
                for axis in excluded:
                    for left, right in constraints[axis]:
                        if right < 0:
                            components.kill(left)
                        else:
                            components.join(left, right)
                histogram[components.surviving_count()] += 1
            maximum = max(histogram)
            expected = maximum, histogram[maximum], histogram
            self.assertEqual(observed, expected)

    def test_fixed_cap_histograms(self) -> None:
        diagnostics = self.payload["fixed_local_t15_diagnostics"]
        self.assertEqual(diagnostics["0"]["maximum_component_upper_cap"], 520)
        self.assertEqual(diagnostics["1"]["maximum_component_upper_cap"], 458)
        self.assertEqual(
            sum(diagnostics["0"]["component_upper_cap_histogram"].values()), 76
        )
        self.assertEqual(
            sum(diagnostics["1"]["component_upper_cap_histogram"].values()), 12
        )

    def test_actual_same_row_counterexample(self) -> None:
        example = self.payload["same_row_actual_term"]
        self.assertEqual(example["epsilon_alpha"], [0, 3])
        self.assertEqual(example["quadratic_derivative_dimension"], 15)
        self.assertEqual(example["permanent_quadratic_intersection_dimension"], 0)
        self.assertEqual(example["exact_fraction_prolongation_dimension"], 520)
        self.assertEqual(example["modular_prolongation_nullity_mod_1000003"], 520)

    def test_claim_boundary_is_coupled_safe(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("individual-term", boundary)
        self.assertIn("does not refute or exclude a six-term coupled", boundary)
        self.assertIn("may destroy directness", boundary)


if __name__ == "__main__":
    unittest.main()
