import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
COMPLETE_FAMILIES = (
    (4, 4, 4),
    (4, 4, 5),
    (4, 5, 4),
    (4, 4, 6),
    (4, 5, 5),
    (4, 6, 4),
    (5, 5, 5),
    (5, 5, 6),
    (5, 6, 5),
    (6, 6, 6),
)


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_higher_overlap_rank_one_shear_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_higher_overlap", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_merge_script():
    path = ROOT / "scripts" / "n7_merge_candidate_chunks.py"
    spec = importlib.util.spec_from_file_location("n7_merge_candidates", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def data_path(overlap_size, left_size, right_size):
    word = {4: "four", 5: "five", 6: "six"}[overlap_size]
    return (
        ROOT
        / "data"
        / f"n7_mixed_glynn_overlap_{word}_{left_size}{right_size}_nilpotent_shear_tail_rank.json"
    )


class HigherOverlapRankOneShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.merge_module = load_merge_script()
        cls.payloads = {
            family: json.loads(data_path(*family).read_text(encoding="utf-8"))
            for family in COMPLETE_FAMILIES
        }
        cls.checkpoint = json.loads(
            (ROOT / "data" / "n7_overlap_four_55_checkpoint_000_075.json").read_text(
                encoding="utf-8"
            )
        )

    def test_parametrizations_are_nilpotent(self):
        for overlap_size in range(4, 7):
            parameters = self.module.parameter_symbols(
                overlap_size, overlap_size, overlap_size
            )
            left_core, scale, ratios, _left_extra, _right_extra = (
                self.module.split_parameters(parameters, overlap_size, 0)
            )
            leading = self.module.leading_right_core_form(left_core, ratios)
            pairing = -scale * leading + left_core[0] * scale + sum(
                coefficient * scale * ratio
                for coefficient, ratio in zip(left_core[1:], ratios)
            )
            self.assertEqual(sp.expand(pairing), 0)

    def test_candidate_inventory_is_bounded_and_complete(self):
        expected_families = {
            (4, 4, 4),
            (4, 4, 5),
            (4, 4, 6),
            (4, 5, 4),
            (4, 5, 5),
            (4, 6, 4),
            (5, 5, 5),
            (5, 5, 6),
            (5, 6, 5),
            (6, 6, 6),
        }
        self.assertEqual(set(self.module.ALLOWED_FAMILIES), expected_families)
        self.assertEqual(
            sum(len(self.module.candidates(*family)) for family in expected_families),
            770,
        )

    def test_completed_family_coverage(self):
        expected_counts = {
            (4, 4, 4): 75,
            (4, 4, 5): 150,
            (4, 5, 4): 150,
            (4, 4, 6): 75,
            (4, 5, 5): 150,
            (4, 6, 4): 75,
            (5, 5, 5): 30,
            (5, 5, 6): 30,
            (5, 6, 5): 30,
            (6, 6, 6): 5,
        }
        for family, payload in self.payloads.items():
            overlap_size, left_size, right_size = family
            self.assertEqual(payload["candidate_count"], expected_counts[family])
            self.assertEqual(len(payload["rows"]), expected_counts[family])
            self.assertEqual(
                payload["status"],
                f"EXACT_ALL_OVERLAP_{self.module.OVERLAP_WORDS[overlap_size]}_{left_size}{right_size}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS",
            )
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
                    for support in self.module.supports(*family)
                    for identity_count in range(1, 6)
                },
            )

    def test_completed_gcds_have_only_recursive_boundary_factors(self):
        expected_term_histograms = {
            (4, 4, 4): {1: 75},
            (4, 4, 5): {1: 150},
            (4, 5, 4): {1: 149, 10: 1},
            (4, 4, 6): {1: 75},
            (4, 5, 5): {1: 149, 10: 1},
            (4, 6, 4): {1: 74, 10: 1},
            (5, 5, 5): {1: 30},
            (5, 5, 6): {1: 30},
            (5, 6, 5): {1: 30},
            (6, 6, 6): {1: 5},
        }
        for family, payload in self.payloads.items():
            overlap_size, left_size, right_size = family
            parameters = self.module.parameter_symbols(*family)
            histogram = {}
            for row in payload["rows"]:
                polynomial = sp.Poly(
                    sp.sympify(row["gcd_factorization"]),
                    *parameters,
                    domain=sp.ZZ,
                )
                covered, exponents, unresolved = (
                    self.module.allowed_boundary_factorization(
                        polynomial,
                        parameters,
                        overlap_size,
                        left_size - overlap_size,
                        right_size - overlap_size,
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
            self.assertEqual(histogram, expected_term_histograms[family])

    def test_historical_55_checkpoint_is_the_complete_family_prefix(self):
        self.assertEqual(
            self.checkpoint["status"],
            "EXACT_CHECKPOINT_OVERLAP_FOUR_55_FIRST_75_OF_150_INVALID_TAIL_MINORS",
        )
        self.assertEqual(self.checkpoint["candidate_count"], 75)
        self.assertEqual(self.checkpoint["full_candidate_count"], 150)
        self.assertEqual(self.checkpoint["candidate_start_index"], 0)
        self.assertEqual(self.checkpoint["candidate_stop_index_exclusive"], 75)
        self.assertEqual(
            self.checkpoint["status_counts"],
            {self.module.ROW_STATUS: 75},
        )
        self.assertEqual(
            self.checkpoint["rows"],
            self.payloads[(4, 5, 5)]["rows"][:75],
        )

    def test_merge_runtime_metadata_accepts_chunks_and_checkpoints(self):
        self.assertEqual(
            self.merge_module.runtime_metadata(
                {"elapsed_seconds": 2.5, "workers": 4}
            ),
            (2.5, {4}),
        )
        self.assertEqual(
            self.merge_module.runtime_metadata(self.checkpoint),
            (self.checkpoint["elapsed_seconds_sum"], {4}),
        )

    def test_merge_selection_metadata_uses_checkpoint_rows(self):
        self.assertEqual(
            self.merge_module.selection_metadata(self.checkpoint),
            {"weighted": 75},
        )
        self.assertEqual(
            self.merge_module.selection_metadata(
                {
                    "weighted_selection": False,
                    "rows": [
                        {},
                        {"weighted_selection": True},
                    ],
                }
            ),
            {"lexicographic": 1, "weighted": 1},
        )


if __name__ == "__main__":
    unittest.main()
