import importlib.util
import json
import os
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectedKoszulQuotientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cyclic = json.loads(
            (ROOT / "data" / "n7_cyclic_projected_koszul_rank.json").read_text()
        )
        cls.search = json.loads(
            (ROOT / "data" / "n7_character_quotient_koszul_search.json").read_text()
        )

    def test_cyclic_exact_rank_and_threshold(self):
        self.assertEqual(self.cyclic["total_rank"], 33_920)
        self.assertEqual(self.cyclic["independent_chow_term_rank_cap"], 832)
        self.assertEqual(self.cyclic["rank_49_threshold"], 40_768)
        self.assertFalse(self.cyclic["strictly_exceeds_49_terms"])
        self.assertEqual(self.cyclic["flattening_lower_bound"], 41)
        self.assertEqual(self.cyclic["adjacent_k52_exact_rank"], 8_919)
        self.assertEqual(
            self.cyclic["universal_seven_dimensional_central_rank_ceiling"],
            33_956,
        )
        self.assertEqual(
            self.cyclic["universal_seven_dimensional_lower_bound_ceiling"], 41
        )
        self.assertEqual(
            {row["total_rank"] for row in self.cyclic["prime_replays"]},
            {33_920},
        )

    def test_fourier_multiplicities_cover_all_characters(self):
        self.assertEqual(self.cyclic["character_multiplicity_sum"], 49)
        for replay in self.cyclic["prime_replays"]:
            self.assertEqual(
                sum(row["multiplicity"] for row in replay["character_rows"]),
                49,
            )

    def test_character_search_controls_and_best_candidate(self):
        self.assertEqual(self.search["candidate_count_checked_before_search"], 40)
        self.assertEqual(
            self.search["controls"]["row_character_line_total_rank"], 29_120
        )
        self.assertEqual(
            self.search["controls"]["diagonal_character_line_total_rank"],
            33_920,
        )
        self.assertEqual(self.search["best_candidate"]["candidate_index"], 23)
        self.assertEqual(self.search["best_candidate"]["total_rank"], 32_928)
        self.assertEqual(
            self.search["best_candidate_replay"]["total_rank"], 32_928
        )
        self.assertTrue(
            self.search["best_candidate_replay"]["matches_search_prime"]
        )
        self.assertFalse(self.search["strictly_exceeds_49_terms"])
        self.assertEqual(self.search["flattening_lower_bound"], 40)

    def test_live_cyclic_replay(self):
        module = load_script("n7_cyclic_projected_koszul_rank.py")
        live = module.build_payload()
        self.assertEqual(live["total_rank"], self.cyclic["total_rank"])
        self.assertEqual(
            [row["character_rows"] for row in live["prime_replays"]],
            [row["character_rows"] for row in self.cyclic["prime_replays"]],
        )
        self.assertEqual(live["adjacent_k52_exact_rank"], 8_919)

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 for the 40-candidate exact replay",
    )
    def test_full_character_search_replay(self):
        module = load_script("n7_character_quotient_koszul_search.py")

        class Args:
            candidates = 40
            seed = 20260820
            workers = 1

        live = module.build_payload(Args())
        for key in (
            "controls",
            "candidates",
            "best_candidate",
            "best_candidate_replay",
            "strictly_exceeds_49_terms",
            "flattening_lower_bound",
        ):
            self.assertEqual(live[key], self.search[key])


if __name__ == "__main__":
    unittest.main()
