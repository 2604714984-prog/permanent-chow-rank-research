from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_coordinate_second_order_equality_collapse.py"
DATA = ROOT / "data" / "general_quartic_coordinate_second_order_equality_collapse.json"
EXPECTED_CORE = "938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9"


def load_module():
    spec = importlib.util.spec_from_file_location("second_order_equality_collapse", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load second-order equality collapse")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class CoordinateSecondOrderEqualityCollapseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.frozen = json.loads(DATA.read_text(encoding="utf-8"))
        cls.core = cls.module.build_core()

    def test_complete_multiset_scan(self) -> None:
        local = self.core["local_over_envelope"]
        self.assertEqual(local["unordered_coordinate_frames_checked"], 54264)
        self.assertEqual(local["profile_count"], 27)
        self.assertEqual(local["maximum_E2_plus_S2_tilde"], 20)
        self.assertEqual(local["equality_frames"], 288)

    def test_equality_orbits_and_structure(self) -> None:
        local = self.core["local_over_envelope"]
        self.assertEqual(local["equality_row_column_orbits"], 2)
        self.assertEqual(local["equality_orbit_sizes"], [144, 144])
        self.assertEqual(local["equality_profile"], {"E2": 12, "D": 0, "K2_tilde": 8, "S2_tilde": 8})
        structure = self.core["equality_structure"]
        self.assertEqual(structure["multiplicity_pattern"], [2, 1, 1, 1, 1])
        self.assertEqual(structure["E1_matching_support"], 0)

    def test_integrability_claim_boundary(self) -> None:
        claim = self.core["claim_boundary"]
        self.assertEqual(claim["single_component_internal_two_jet_on_equality_frames"], "MATCHING_ZERO")
        self.assertEqual(claim["global_six_component_second_order"], "OPEN")
        self.assertEqual(claim["mu_6_4"], "OPEN_IN_[6,8]")
        self.assertFalse(claim["unrestricted_chow_rank_improvement"])

    def test_frozen_core(self) -> None:
        value = dict(self.core)
        import hashlib
        digest = hashlib.sha256(
            json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        self.assertEqual(digest, EXPECTED_CORE)
        frozen = dict(self.frozen)
        self.assertEqual(frozen.pop("core_sha256"), EXPECTED_CORE)
        self.assertEqual(frozen, self.core)


if __name__ == "__main__":
    unittest.main()
