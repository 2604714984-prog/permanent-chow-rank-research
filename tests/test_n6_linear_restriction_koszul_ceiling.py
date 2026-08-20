from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_linear_restriction_koszul_ceiling.py"
FROZEN = ROOT / "data" / "n6_linear_restriction_koszul_ceiling.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "n6_linear_restriction_koszul_ceiling",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6LinearRestrictionKoszulCeilingTests(unittest.TestCase):
    def test_every_dimension_is_strictly_below_26(self) -> None:
        payload = AUDIT.build_payload()
        self.assertEqual(payload["ambient_dimensions_covered"], [1, 36])
        self.assertLess(Fraction(*payload["global_ratio_upper"]), 26)
        for row in payload["small_dimension_explicit_term_witnesses"]:
            self.assertLess(Fraction(*row["ratio_upper"]), 26)
        for row in payload["dimension_rows_6_through_35"]:
            self.assertLess(Fraction(*row["ratio_upper"]), 26)
            self.assertGreater(row["margin_below_26"], 0)

    def test_derivative_basis_requires_both_matchings(self) -> None:
        active = AUDIT.active_edges(28)
        counts = []
        for degree in (2, 3, 4):
            subsets = tuple(combinations(range(6), degree))
            counts.append(
                sum(
                    AUDIT.derivative_supported(rows, columns, active)
                    for rows in subsets
                    for columns in subsets
                )
            )
        self.assertEqual(counts, [207, 400, 207])
        self.assertNotEqual(active, AUDIT.target_active_edges(28))

    def test_matching_deletion_witness_has_full_derivative_bases(self) -> None:
        active = AUDIT.active_edges(30)
        counts = []
        for degree in (2, 3, 4):
            subsets = tuple(combinations(range(6), degree))
            counts.append(
                sum(
                    AUDIT.derivative_supported(rows, columns, active)
                    for rows in subsets
                    for columns in subsets
                )
            )
        self.assertEqual(counts, [225, 400, 225])

    def test_small_pure_triangular_replay(self) -> None:
        self.assertEqual(
            AUDIT.replay_leading(19),
            AUDIT.LEADING_EXPECTED[19],
        )

    def test_colex_ranks_are_dense_and_unique(self) -> None:
        for ambient in range(1, 9):
            for size in range(ambient + 1):
                subsets = tuple(combinations(range(ambient), size))
                ranks = [AUDIT.combination_colex_rank(row) for row in subsets]
                self.assertEqual(sorted(ranks), list(range(len(subsets))))

    def test_worst_leading_row_bitset_stays_small(self) -> None:
        universe = AUDIT.leading_row_universe_size(28, 4, 4)
        self.assertEqual(universe, 39_312_000)
        self.assertLessEqual((universe + 7) // 8, 5 * 2**20)

    def test_dense_half_weight_codes_preserve_labeled_weights(self) -> None:
        powers, indices, count = AUDIT.dense_half_weight_coding(2, 3)
        self.assertEqual(count, 246)
        self.assertEqual(
            sorted(value for value in indices if value >= 0),
            list(range(246)),
        )
        for rows in combinations(range(6), 2):
            base_code = sum(powers[row] for row in rows)
            for wedge in combinations(range(12), 3):
                wedge_code = sum(powers[variable // 6] for variable in wedge)
                encoded = indices[base_code + wedge_code]
                weight = AUDIT.row_column_weight(rows, (), wedge)[:6]
                direct_code = sum(
                    value * powers[index] for index, value in enumerate(weight)
                )
                self.assertEqual(encoded, indices[direct_code])

    def test_small_compact_restricted_modular_rank(self) -> None:
        active = {6 * index + index for index in range(6)}
        active.update({1, 8})
        self.assertEqual(
            AUDIT.restricted_modular_rank(active),
            {
                "domain_dimension": 840,
                "weight_block_count": 356,
                "maximum_block_column_count": 10,
                "modular_rank": 364,
            },
        )

    def test_strict_modular_certificate_values(self) -> None:
        self.assertEqual(
            AUDIT.MODULAR_R23_EXPECTED,
            {
                30: 650_316,
                31: 749_786,
                32: 856_000,
                33: 968_883,
                34: 1_088_402,
                35: 1_214_569,
            },
        )

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        actual = json.loads(json.dumps(AUDIT.build_payload()))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
