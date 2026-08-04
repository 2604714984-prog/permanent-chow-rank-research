from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower25_fixed_q_diagnostic.py"
FROZEN = ROOT / "data" / "n6_lower25_fixed_q_diagnostic.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_lower25_fixed_q_diagnostic",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load lower-25 fixed-q diagnostic")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6Lower25FixedQDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_shadow_certificates_are_valid_and_monotone(self) -> None:
        certificates = AUDIT.shadow_certificates()
        lowers = [
            row["integer_shadow_lower_bound"]
            for row in certificates
        ]
        self.assertEqual(lowers, sorted(lowers))
        self.assertEqual(lowers[28], 49)
        self.assertEqual(lowers[45], 64)
        self.assertEqual(lowers[65], 79)

        for row in certificates:
            dimension = row["dimension"]
            lower = AUDIT.Fraction(row["lower_separator"])
            upper = AUDIT.Fraction(row["upper_separator"])
            shadow_lower = row["integer_shadow_lower_bound"]
            if row["exact_root"]:
                self.assertEqual(
                    AUDIT.generalized_binomial(lower, 3) ** 2,
                    dimension,
                )
                self.assertEqual(lower, upper)
            else:
                self.assertLess(
                    AUDIT.generalized_binomial(lower, 3) ** 2,
                    dimension,
                )
                self.assertGreater(
                    AUDIT.generalized_binomial(upper, 3) ** 2,
                    dimension,
                )
            self.assertGreater(
                AUDIT.generalized_binomial(lower, 2) ** 2,
                shadow_lower - 1,
            )
            self.assertLessEqual(
                AUDIT.generalized_binomial(upper, 2) ** 2,
                shadow_lower,
            )

    def test_exact_fixed_q_ranges_and_counts(self) -> None:
        expected = {
            4: {
                "range": [0, 27],
                "initial": 406,
                "excluded": 146,
                "post_component": 260,
                "unresolved": 254,
                "routes": {
                    "quotient_budget_already_strict": 6,
                    "relative_prolongation_cap_can_close": 60,
                    "structural_exclusion_or_stronger_invariant_required": 194,
                },
                "caps": {"2": 20, "38": 20, "74": 20},
            },
            5: {
                "range": [20, 44],
                "initial": 325,
                "excluded": 141,
                "post_component": 184,
                "unresolved": 181,
                "routes": {
                    "quotient_budget_already_strict": 3,
                    "relative_prolongation_cap_can_close": 34,
                    "structural_exclusion_or_stronger_invariant_required": 147,
                },
                "caps": {"23": 17, "59": 17},
            },
            6: {
                "range": [40, 64],
                "initial": 325,
                "excluded": 146,
                "post_component": 179,
                "unresolved": 176,
                "routes": {
                    "quotient_budget_already_strict": 3,
                    "relative_prolongation_cap_can_close": 35,
                    "structural_exclusion_or_stronger_invariant_required": 141,
                },
                "caps": {"8": 17, "44": 18},
            },
        }

        for row in self.payload["fixed_q_results"]:
            fixed_terms = row["fixed_terms"]
            target = expected[fixed_terms]
            self.assertEqual(
                row["central_intersection_range"],
                target["range"],
            )
            self.assertEqual(
                row["initial_state_count"],
                target["initial"],
            )
            self.assertEqual(
                row["component_excluded_state_count"],
                target["excluded"],
            )
            self.assertEqual(
                row["state_count_after_component_pruning"],
                target["post_component"],
            )
            self.assertEqual(
                row["unresolved_state_count"],
                target["unresolved"],
            )
            self.assertEqual(
                row["route_histogram_after_component_pruning"],
                target["routes"],
            )
            self.assertEqual(
                row["prolongation_cap_histogram"],
                target["caps"],
            )

    def test_no_route_is_promoted(self) -> None:
        self.assertEqual(
            self.payload["route_selection"],
            {
                "numerically_smallest_fixed_terms": 6,
                "fewest_unresolved_states": 176,
                "selected_for_proof": None,
                "verdict": "NO_COMPACT_FIXED_Q_FRONTIER",
            },
        )

    def test_frozen_certificate_matches_live_replay(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_claim_boundary_remains_fail_closed(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("route diagnostic", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=25", boundary)
        self.assertIn("does not prove any displayed", boundary)
        self.assertIn("24..32", boundary)


if __name__ == "__main__":
    unittest.main()
