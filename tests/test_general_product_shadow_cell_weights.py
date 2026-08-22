from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "general_exact_product_shadow.py"
DATA_PATH = ROOT / "data" / "general_exact_product_shadow.json"

SPEC = importlib.util.spec_from_file_location(
    "general_exact_product_shadow_for_cell_weights",
    MODULE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def conjugate(partition: tuple[int, ...]) -> tuple[int, ...]:
    width = len(partition)
    return tuple(
        sum(value >= column for value in partition)
        for column in range(1, width + 1)
    )


def objective(
    shadow: object,
    partition: tuple[int, ...],
) -> int:
    return sum(
        weight * shadow.k[value]
        for weight, value in zip(shadow.weights, partition, strict=True)
    )


class GeneralProductShadowCellWeightTests(unittest.TestCase):
    def test_weights_are_shadow_increments(self) -> None:
        for n, m in ((5, 2), (6, 3), (7, 4), (8, 4)):
            shadow = MODULE.ExactProductShadow(n, m)
            increments = tuple(
                shadow.k[index + 1] - shadow.k[index]
                for index in range(shadow.layer_size)
            )
            self.assertEqual(shadow.weights, increments)

    def test_conjugation_invariance(self) -> None:
        for n, m, targets in (
            (7, 4, (238, 239)),
            (8, 4, (560, 561)),
        ):
            shadow = MODULE.ExactProductShadow(n, m)
            for target in targets:
                row = shadow.minimum(target)
                partition = row.minimizing_partition
                transpose = conjugate(partition)
                self.assertEqual(sum(transpose), target)
                self.assertEqual(
                    objective(shadow, partition),
                    objective(shadow, transpose),
                )

    def test_complete_two_element_minimizer_pairs(self) -> None:
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        cases = (
            (7, 4, "n7_application", "cap_partition", 2),
            (8, 4, "n8_application", "cap_partition", 2),
            (8, 4, "n8_application", "first_excluded_partition", 2),
        )
        for n, m, section, key, expected_count in cases:
            shadow = MODULE.ExactProductShadow(n, m)
            partition = tuple(frozen[section][key])
            transpose = conjugate(partition)
            self.assertNotEqual(partition, transpose)
            self.assertEqual(
                objective(shadow, partition),
                objective(shadow, transpose),
            )
            count_key = (
                "cap_partition_count"
                if key == "cap_partition"
                else "first_excluded_partition_count"
            )
            self.assertEqual(frozen[section][count_key], expected_count)


if __name__ == "__main__":
    unittest.main()
