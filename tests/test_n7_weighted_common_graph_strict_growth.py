import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_weighted_common_graph_strict_growth.py"
DATA = ROOT / "data" / "n7_weighted_common_graph_strict_growth.json"
SPEC = importlib.util.spec_from_file_location(
    "n7_weighted_common_graph_strict_growth", SCRIPT
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class WeightedCommonGraphStrictGrowthTests(unittest.TestCase):
    def test_corrected_strata(self) -> None:
        self.assertEqual(
            MODULE.PRE_GROWTH_CANDIDATES,
            ((32, 40), (33, 39), (34, 38), (35, 37), (36, 36)),
        )
        self.assertEqual(
            MODULE.TARGET_COMPATIBLE_STRATA,
            ((33, 39), (34, 38), (35, 37)),
        )
        self.assertEqual(
            MODULE.TARGET_ADMISSIBLE_H5,
            {
                (33, 39): (40,),
                (34, 38): (39, 40),
                (35, 37): (38, 39, 40),
            },
        )

    def test_forbidden_plateaux(self) -> None:
        self.assertEqual(MODULE.admissible_h5_values((36, 36)), ())
        self.assertEqual(MODULE.admissible_h5_values((32, 40)), ())

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
