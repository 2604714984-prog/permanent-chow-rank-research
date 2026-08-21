from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_quartic_coordinate_first_order_eight_term_barrier.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_coordinate_first_order_eight_term_barrier_independent.py"
DATA = ROOT / "data" / "general_quartic_coordinate_first_order_eight_term_barrier.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class CoordinateFirstOrderEightTermBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primary = load_module("coordinate_first_order_primary", PRIMARY)
        cls.local = cls.primary.local_scan()
        cls.payload = cls.primary.payload()

    def test_complete_multiset_scan_and_local_inequality(self) -> None:
        self.assertEqual(self.local["unordered_coordinate_frames_checked"], 54264)
        self.assertEqual(self.local["maximum_envelope_plus_unshared"], 6)
        self.assertEqual(self.local["maximum_contained_matchings"], 2)
        self.assertEqual(self.local["maximum_internal_kernel_matchings"], 2)
        self.assertEqual(self.local["maximum_unshared_matchings"], 2)

    def test_exact_local_profile_histogram(self) -> None:
        self.assertEqual(
            self.local["local_profile_histogram"],
            {
                "envelope_0_contained_0_internal_0_unshared_0": 19584,
                "envelope_1_contained_0_internal_0_unshared_0": 5856,
                "envelope_1_contained_0_internal_1_unshared_1": 7200,
                "envelope_1_contained_1_internal_1_unshared_1": 240,
                "envelope_2_contained_0_internal_0_unshared_0": 4848,
                "envelope_2_contained_0_internal_1_unshared_1": 4032,
                "envelope_2_contained_0_internal_2_unshared_2": 2592,
                "envelope_2_contained_1_internal_1_unshared_1": 864,
                "envelope_2_contained_1_internal_2_unshared_2": 576,
                "envelope_2_contained_2_internal_0_unshared_2": 72,
                "envelope_3_contained_0_internal_0_unshared_0": 1728,
                "envelope_3_contained_0_internal_1_unshared_1": 1152,
                "envelope_3_contained_0_internal_2_unshared_2": 1152,
                "envelope_3_contained_1_internal_0_unshared_1": 864,
                "envelope_4_contained_0_internal_0_unshared_0": 2064,
                "envelope_4_contained_0_internal_2_unshared_2": 576,
                "envelope_4_contained_1_internal_0_unshared_1": 576,
                "envelope_6_contained_0_internal_0_unshared_0": 288,
            },
        )

    def test_equality_profiles_and_orbits(self) -> None:
        self.assertEqual(self.local["equality_frames"], 864)
        self.assertEqual(
            self.local["equality_profile_histogram"],
            {
                "envelope_4_contained_0_internal_2_unshared_2": 576,
                "envelope_6_contained_0_internal_0_unshared_0": 288,
            },
        )
        self.assertEqual(self.local["equality_row_column_orbits"], 4)
        self.assertEqual(self.local["equality_orbit_sizes"], [144, 144, 288, 288])
        self.assertEqual(len(self.local["distinct_equality_orbits"]), 2)
        self.assertEqual(len(self.local["repeated_equality_orbits"]), 2)

    def test_global_coordinate_first_order_minimum(self) -> None:
        global_data = self.payload["global"]
        self.assertEqual(global_data["minimum_coordinate_regular_first_order_term_count"], 8)
        for term_count in range(1, 8):
            self.assertFalse(global_data["q_rows"][str(term_count)]["necessary_condition_holds"])
        self.assertTrue(global_data["q_rows"]["8"]["necessary_condition_holds"])

    def test_q8_support_equality_is_only_support_level(self) -> None:
        equality = self.payload["support_level_q8_equality"]
        self.assertEqual(equality["frame_count"], 8)
        self.assertEqual(equality["incidence_degree_distribution"], {"2": 24})
        self.assertTrue(equality["all_frames_have_empty_unshared_set"])
        self.assertTrue(equality["support_level_equality_only"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text()))

    def test_independent_source_fiber_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--expected-core", self.payload["core_sha256"]],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
