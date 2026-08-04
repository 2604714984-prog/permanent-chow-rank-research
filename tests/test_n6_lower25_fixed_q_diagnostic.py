from __future__ import annotations

import importlib.util
import json
import unittest
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower25_fixed_q_diagnostic.py"
FROZEN = ROOT / "data" / "n6_lower25_fixed_q_diagnostic.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_lower25_fixed_q_diagnostic",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load n6 lower25 fixed-q diagnostic")
DIAGNOSTIC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DIAGNOSTIC)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def frozen_summary(payload: dict[str, object]) -> dict[str, object]:
    fixed_q_summaries: list[dict[str, object]] = []
    for row in payload["fixed_q_diagnostics"]:
        fixed_q_summaries.append(
            {
                "fixed_terms": row["fixed_terms"],
                "residual_terms": row["residual_terms"],
                "projection_cap": row["projection_cap"],
                "central_intersection_range": row[
                    "central_intersection_range"
                ],
                "state_count_before_component_exclusions": row[
                    "state_count_before_component_exclusions"
                ],
                "route_counts": row["route_counts"],
                "surviving_state_count": row["surviving_state_count"],
                "surviving_b_range": row["surviving_b_range"],
                "relative_prolongation_cap_histogram": row[
                    "relative_prolongation_cap_histogram"
                ],
                "maximum_required_quotient_gain_among_survivors": row[
                    "maximum_required_quotient_gain_among_survivors"
                ],
                "maximum_structural_gain_deficit": row[
                    "maximum_structural_gain_deficit"
                ],
                "layers_sha256": canonical_sha256(row["layers"]),
                "states_sha256": canonical_sha256(row["states"]),
            }
        )

    return {
        "status": payload["status"],
        "target": payload["target"],
        "shadow_certificate_count": len(payload["shadow_certificates"]),
        "shadow_certificates_sha256": canonical_sha256(
            payload["shadow_certificates"]
        ),
        "macaulay_degree_two_successors": payload[
            "macaulay_degree_two_successors"
        ],
        "fixed_q_summaries": fixed_q_summaries,
        "fixed_q_diagnostics_sha256": canonical_sha256(
            payload["fixed_q_diagnostics"]
        ),
        "route_selection": payload["route_selection"],
        "conclusion": payload["conclusion"],
        "claim_boundary": payload["claim_boundary"],
    }


class N6Lower25FixedQDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = DIAGNOSTIC.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        cls.by_q = {
            row["fixed_terms"]: row
            for row in cls.payload["fixed_q_diagnostics"]
        }

    def test_shadow_certificates_are_exact(self) -> None:
        table = DIAGNOSTIC.verify_shadow_certificates()
        self.assertEqual(table["1"]["integer_shadow_lower_bound"], 9)
        self.assertEqual(table["20"]["integer_shadow_lower_bound"], 41)
        self.assertEqual(table["28"]["integer_shadow_lower_bound"], 49)
        self.assertEqual(table["45"]["integer_shadow_lower_bound"], 64)
        self.assertEqual(table["65"]["integer_shadow_lower_bound"], 79)

    def test_fixed_q_ranges_and_state_counts(self) -> None:
        self.assertEqual(
            (
                self.by_q[4]["central_intersection_range"],
                self.by_q[4]["state_count_before_component_exclusions"],
                self.by_q[4]["surviving_state_count"],
            ),
            ([0, 27], 406, 260),
        )
        self.assertEqual(
            (
                self.by_q[5]["central_intersection_range"],
                self.by_q[5]["state_count_before_component_exclusions"],
                self.by_q[5]["surviving_state_count"],
            ),
            ([20, 44], 325, 184),
        )
        self.assertEqual(
            (
                self.by_q[6]["central_intersection_range"],
                self.by_q[6]["state_count_before_component_exclusions"],
                self.by_q[6]["surviving_state_count"],
            ),
            ([40, 64], 325, 179),
        )

    def test_route_histograms(self) -> None:
        self.assertEqual(
            self.by_q[4]["route_counts"],
            {
                "component_central_rank_exclusion": 146,
                "quotient_koszul_already_strict": 6,
                "relative_prolongation_cap_can_close": 60,
                "structural_exclusion_or_stronger_invariant_required": 194,
            },
        )
        self.assertEqual(
            self.by_q[5]["route_counts"],
            {
                "component_central_rank_exclusion": 141,
                "quotient_koszul_already_strict": 3,
                "relative_prolongation_cap_can_close": 34,
                "structural_exclusion_or_stronger_invariant_required": 147,
            },
        )
        self.assertEqual(
            self.by_q[6]["route_counts"],
            {
                "component_central_rank_exclusion": 146,
                "quotient_koszul_already_strict": 3,
                "relative_prolongation_cap_can_close": 35,
                "structural_exclusion_or_stronger_invariant_required": 141,
            },
        )

    def test_relative_prolongation_caps(self) -> None:
        self.assertEqual(
            self.by_q[4]["relative_prolongation_cap_histogram"],
            {"2": 20, "38": 20, "74": 20},
        )
        self.assertEqual(
            self.by_q[5]["relative_prolongation_cap_histogram"],
            {"23": 17, "59": 17},
        )
        self.assertEqual(
            self.by_q[6]["relative_prolongation_cap_histogram"],
            {"8": 17, "44": 18},
        )

    def test_fail_closed_route_selection(self) -> None:
        selection = self.payload["route_selection"]
        self.assertEqual(selection["fewest_surviving_states_fixed_terms"], 6)
        self.assertEqual(selection["fewest_surviving_states"], 179)
        self.assertEqual(selection["fewest_structural_states"], 141)
        self.assertIn("No tested fixed-term count", selection["assessment"])
        self.assertIn(
            "does not extend mechanically",
            self.payload["conclusion"],
        )
        self.assertIn(
            "does not prove ChowRank(perm_6)>=25",
            self.payload["claim_boundary"],
        )

    def test_frozen_summary_matches_replay(self) -> None:
        self.assertEqual(frozen_summary(self.payload), self.frozen)


if __name__ == "__main__":
    unittest.main()
