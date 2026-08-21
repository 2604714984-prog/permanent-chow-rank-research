import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_b_coupling_probe.py"
DATA = ROOT / "data" / "n7_packet_b_coupling_probe.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_b_coupling_probe", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketBCouplingProbeTests(unittest.TestCase):
    def test_factor_tensor_and_term_ranks(self) -> None:
        prime = MODULE.coupled.PRIMES[0]
        factors = MODULE.identity_packet_b_factor_coefficients(prime)
        self.assertEqual(factors.shape, (49, 7, 49))
        rng = np.random.default_rng(17)
        evaluations = rng.integers(0, prime, size=(49, 48), dtype=np.int64)
        output, input_map, dimensions = MODULE.labelled_middle_maps(
            factors, evaluations, evaluations, prime
        )
        self.assertEqual(dimensions, [25] * 7 + [35] * 42)
        self.assertEqual(output.shape[1], MODULE.EXPECTED_MIDDLE_DIMENSION)
        self.assertEqual(input_map.shape[0], MODULE.EXPECTED_MIDDLE_DIMENSION)

    def test_too_few_full_probe_columns_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_payload(1, MODULE.EXPECTED_MIDDLE_DIMENSION - 1)

    def test_exact_walsh_dictionary_ranks(self) -> None:
        self.assertEqual(MODULE.walsh_dictionary_rank(3), 35)
        self.assertEqual(MODULE.walsh_dictionary_rank(4), 41)

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        actual = MODULE.build_payload(
            expected["seed"], expected["rows"][0]["evaluation_columns"]
        )
        for row in actual["rows"]:
            row.pop("elapsed_seconds", None)
        for row in expected["rows"]:
            row.pop("elapsed_seconds", None)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
