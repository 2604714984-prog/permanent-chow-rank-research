import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_b_curve_coupling_probe.py"
DATA = ROOT / "data" / "n7_packet_b_curve_coupling_probe.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_b_curve_coupling_probe", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketBCurveCouplingProbeTests(unittest.TestCase):
    def test_representative_profiles(self) -> None:
        prime = MODULE.coupled.PRIMES[0]
        profiles = []
        for weights in MODULE.REPRESENTATIVES:
            tails = MODULE.moment_curve_tails(weights, prime)
            profiles.append(
                (
                    MODULE.point_code_rank(tails, 3, prime),
                    MODULE.point_code_rank(tails, 4, prime),
                )
            )
        self.assertEqual(profiles, [(30, 42), (31, 41)])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        actual = MODULE.build_payload(
            expected["seed"],
            expected["evaluation_columns"],
            expected["curve_box_classification"]["max_weight"],
        )
        for item in (actual, expected):
            for row in item["rows"]:
                row.pop("elapsed_seconds", None)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
