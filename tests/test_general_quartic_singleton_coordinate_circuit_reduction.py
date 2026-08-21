from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_quartic_singleton_coordinate_circuit_reduction.py"
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_quartic_singleton_coordinate_circuit_reduction_independent.py"
)
DATA = ROOT / "data" / "general_quartic_singleton_coordinate_circuit_reduction.json"
EXPECTED_HASH = "a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f"
PRIMARY_MARKER = "GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_PASS"
INDEPENDENT_MARKER = (
    "GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_INDEPENDENT_PASS"
)


def load_primary():
    spec = importlib.util.spec_from_file_location("quartic_singleton_primary", PRIMARY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load primary singleton module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class QuarticSingletonCoordinateCircuitReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_primary()
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))
        cls.core = cls.payload["theorem_core"]

    def test_support_classification_and_orbits(self) -> None:
        support = self.core["positive_singleton_support_classification"]
        self.assertEqual(support["maximum_singleton_components"], 2)
        self.assertEqual(
            support["families"],
            {
                "one_singleton": ["double_edge_tail", "square_lollipop"],
                "two_singletons": ["endpoint_marked_p5"],
            },
        )
        self.assertEqual(
            support["row_column_orbit_counts"],
            {
                "double_edge_tail": 29,
                "endpoint_marked_p5": 18,
                "square_lollipop": 5,
            },
        )
        self.assertEqual(
            support["embedding_counts_fixed_identity"],
            {
                "double_edge_tail": 888,
                "endpoint_marked_p5": 696,
                "square_lollipop": 216,
            },
        )

    def test_normal_forms_and_first_order_barrier(self) -> None:
        normal_forms = self.core["circuit_normal_forms"]
        self.assertEqual(
            normal_forms["continuous_parameter_counts"],
            {
                "double_edge_tail": 1,
                "endpoint_marked_p5": 0,
                "square_lollipop": 1,
            },
        )
        self.assertTrue(normal_forms["all_five_column_minors_are_units"])
        barrier = self.core["first_order_barrier"]
        self.assertEqual(barrier["global_maximum_matching_support"], 5)
        self.assertTrue(barrier["regular_first_order_perm4_lift_impossible"])

    def test_repeated_factor_singleton_frames(self) -> None:
        frames = self.core["singleton_coordinate_frames"]
        self.assertEqual(frames["unused_factor_multisets_total"], 136)
        self.assertEqual(frames["two_supported_frames_removed"], 6)
        self.assertEqual(frames["singleton_frames_retained"], 130)
        self.assertEqual(
            frames["distinct_frame_size_distribution"],
            {"4": 10, "5": 60, "6": 60},
        )
        self.assertEqual(frames["diagonal_stabilizer_frame_orbits"], 10)
        self.assertEqual(
            frames["diagonal_stabilizer_orbit_sizes"],
            [4, 6, 12, 12, 12, 12, 12, 12, 24, 24],
        )
        self.assertEqual(frames["rooted_adjacent_frame_orbits"], 41)
        self.assertEqual(frames["rooted_adjacent_configurations"], 780)

    def test_universal_second_order_envelope(self) -> None:
        envelope = self.core["second_order_envelope"]
        self.assertEqual(
            envelope["family_maximum_support"],
            {
                "double_edge_tail": 22,
                "endpoint_marked_p5": 23,
                "square_lollipop": 22,
            },
        )
        self.assertEqual(
            envelope["decorated_configuration_counts"],
            {
                "double_edge_tail": 3770,
                "endpoint_marked_p5": 304200,
                "square_lollipop": 650,
            },
        )
        self.assertEqual(envelope["global_maximum_support"], 23)
        self.assertEqual(envelope["perm4_matching_support"], 24)
        self.assertTrue(envelope["regular_second_order_perm4_lift_impossible"])
        combined = self.core["combined_coordinate_boundary"]
        self.assertTrue(combined["all_positive_coordinate_regular_two_jets_closed"])
        self.assertEqual(combined["zero_leading_matching_projection"], "OPEN")
        self.assertEqual(self.payload["theorem_core_sha256"], EXPECTED_HASH)

    def test_cli_and_independent_replays(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "payload.json"
            completed = subprocess.run(
                [sys.executable, "-O", str(PRIMARY), "--json", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=180,
            )
            self.assertIn(PRIMARY_MARKER, completed.stdout)
            self.assertIn(EXPECTED_HASH, completed.stdout)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.payload)

        independent = subprocess.run(
            [sys.executable, "-O", str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn(INDEPENDENT_MARKER, independent.stdout)


if __name__ == "__main__":
    unittest.main()
