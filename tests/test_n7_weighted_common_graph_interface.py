import importlib.util
import itertools
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_weighted_common_graph_interface.py"
DATA = ROOT / "data" / "n7_weighted_common_graph_interface.json"
SPEC = importlib.util.spec_from_file_location(
    "n7_weighted_common_graph_interface", SCRIPT
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class WeightedCommonGraphInterfaceTests(unittest.TestCase):
    def test_rank_strata(self) -> None:
        self.assertEqual(
            MODULE.EQUALITY_RANK_STRATA,
            ((30, 42), (31, 41), (32, 40), (33, 39), (34, 38), (35, 37), (36, 36)),
        )
        self.assertEqual(
            MODULE.TARGET_COMPATIBLE_NUMERICAL_STRATA,
            ((32, 40), (33, 39), (34, 38), (35, 37), (36, 36)),
        )
        self.assertEqual(
            MODULE.TARGET_COMPATIBLE_GEOMETRIC_STRATA,
            ((32, 40), (33, 39), (34, 38), (35, 37)),
        )

    def test_curve_union_construction_cardinality(self) -> None:
        prime = MODULE.coupled.PRIMES[0]
        for curve_degree, curve_count, off_count, _ in MODULE.CURVE_UNION_CONSTRUCTIONS:
            homogeneous_exponents = (0,) + tuple(
                exponent
                for exponent in MODULE.CURVE_TAIL_EXPONENTS[curve_degree]
                if exponent is not None
            )
            self.assertEqual(
                len(
                    {
                        sum(choice)
                        for choice in itertools.combinations_with_replacement(
                            homogeneous_exponents, 3
                        )
                    }
                ),
                3 * curve_degree + 1,
            )
            self.assertEqual(
                len(
                    {
                        sum(choice)
                        for choice in itertools.combinations_with_replacement(
                            homogeneous_exponents, 4
                        )
                    }
                ),
                4 * curve_degree + 1,
            )
            tails = MODULE.rational_curve_union_tails(
                curve_degree, curve_count, off_count, prime
            )
            self.assertEqual(len(tails), 42)
            self.assertEqual(len(set(tails)), 42)

    def test_target_matrix(self) -> None:
        targets = MODULE.degree_six_permanent_targets()
        self.assertEqual(targets.shape, (7, 924))
        self.assertTrue((targets.sum(axis=1) == 1).all())
        self.assertEqual(int(targets.sum()), 7)

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
