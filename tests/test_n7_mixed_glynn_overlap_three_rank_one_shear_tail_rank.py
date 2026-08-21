import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SIZE_PAIRS = ((3, 4), (4, 3))


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_overlap_three_rank_one_shear_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap_three", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapThreeRankOneShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payloads = {
            pair: json.loads(
                (
                    ROOT
                    / "data"
                    / f"n7_mixed_glynn_overlap_three_{pair[0]}{pair[1]}_nilpotent_shear_tail_rank.json"
                ).read_text(encoding="utf-8")
            )
            for pair in SIZE_PAIRS
        }

    def test_complete_sum_seven_families(self):
        for pair, payload in self.payloads.items():
            self.assertEqual(payload["candidate_count"], 300)
            self.assertEqual(payload["candidate_start_index"], 0)
            self.assertEqual(payload["candidate_stop_index_exclusive"], 300)
            self.assertEqual(payload["chunk_count"], 6)
            self.assertEqual(
                payload["status"],
                f"EXACT_ALL_OVERLAP_THREE_{pair[0]}{pair[1]}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS",
            )
            self.assertTrue(
                all(status.startswith("EXACT_ALL_") for status in payload["face_certificates"])
            )

    def test_support_and_multiplicity_coverage(self):
        for pair, payload in self.payloads.items():
            self.assertEqual(
                {
                    (
                        tuple(row["core_support"]),
                        tuple(row["left_extra_support"]),
                        tuple(row["right_extra_support"]),
                        row["identity_count"],
                    )
                    for row in payload["rows"]
                },
                {
                    (*support, identity_count)
                    for support in self.module.supports(*pair)
                    for identity_count in range(1, 6)
                },
            )

    def test_exact_gcds_have_only_recursive_boundary_factors(self):
        expected_term_histograms = {
            (3, 4): {1: 300},
            (4, 3): {1: 294, 3: 1, 5: 5},
        }
        for pair, payload in self.payloads.items():
            parameters = self.module.parameter_symbols(*pair)
            histogram = {}
            for row in payload["rows"]:
                polynomial = sp.Poly(
                    sp.sympify(row["gcd_factorization"]),
                    *parameters,
                    domain=sp.ZZ,
                )
                covered, exponents, unresolved = (
                    self.module.allowed_boundary_factorization(
                        polynomial, parameters, pair[0] - 3, pair[1] - 3
                    )
                )
                self.assertTrue(covered)
                self.assertEqual(unresolved, [])
                self.assertEqual(
                    exponents, row["allowed_boundary_factor_exponents"]
                )
                self.assertEqual(row["status"], self.module.ROW_STATUS)
                self.assertEqual(row["minor_count"], 1)
                term_count = row["minors"][0]["determinant_term_count"]
                histogram[term_count] = histogram.get(term_count, 0) + 1
            self.assertEqual(histogram, expected_term_histograms[pair])


if __name__ == "__main__":
    unittest.main()
