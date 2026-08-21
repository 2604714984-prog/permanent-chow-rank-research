import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_b_curve_target_certificate.py"
DATA = ROOT / "data" / "n7_packet_b_curve_target_certificate.json"
SPEC = importlib.util.spec_from_file_location(
    "n7_packet_b_curve_target_certificate", SCRIPT
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketBCurveTargetCertificateTests(unittest.TestCase):
    def test_degree_six_coordinate_count(self) -> None:
        self.assertEqual(len(MODULE.DEGREE_SIX_COMPOSITIONS), 924)
        self.assertEqual(len(MODULE.SQUAREFREE_TARGETS), 7)

    def test_row_multidegree_blocks_are_disjoint(self) -> None:
        self.assertEqual(len(set(MODULE.MISSING_ROW_MULTIDEGREES)), 7)
        self.assertTrue(
            set(MODULE.MISSING_ROW_MULTIDEGREES).isdisjoint(
                MODULE.PURE_ROW_MULTIDEGREES
            )
        )

    def test_representative_has_seven_collision_witnesses(self) -> None:
        witnesses = MODULE.collision_witnesses((1, 2, 3, 4, 5, 12))
        self.assertEqual(len(witnesses), 7)
        for witness in witnesses:
            collision = tuple(witness["nonsquarefree_collision"])
            target = tuple(witness["target_composition"])
            self.assertNotIn(collision, MODULE.SQUAREFREE_TARGET_SET)
            self.assertEqual(sum(collision), 6)
            self.assertEqual(
                MODULE.weighted_exponent(collision, (1, 2, 3, 4, 5, 12)),
                MODULE.weighted_exponent(target, (1, 2, 3, 4, 5, 12)),
            )

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(expected["max_weight"]), expected)


if __name__ == "__main__":
    unittest.main()
