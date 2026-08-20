from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
import importlib.util
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_global_t16_prolongation_cap.py"
FROZEN = ROOT / "data" / "n6_global_t16_prolongation_cap.json"


def load_script_module():
    spec = importlib.util.spec_from_file_location("n6_global_t16_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reference_mobius_corrections(
    order,
    w_axes,
    masks,
    blocks,
    occurrence_maps,
):
    """Historical direct inclusion-exclusion formula for one test row."""

    w_set = set(w_axes)
    common_blocks = defaultdict(list)
    for block_index, block in enumerate(blocks):
        available = [axis for axis in block.axes if axis not in w_set]
        for axes in combinations(available, order):
            common_blocks[axes].append(block_index)

    corrections = {}
    for axes, block_indices in common_blocks.items():
        value = 0
        for block_index in block_indices:
            block = blocks[block_index]
            old_mask = masks.get(block_index, 0)
            for size in range(order + 1):
                sign = -1 if (order - size) % 2 else 1
                for subset in combinations(axes, size):
                    mask = old_mask
                    for axis in subset:
                        mask |= occurrence_maps[axis][block_index]
                    value += sign * block.nullity(mask)
        if value:
            corrections[axes] = value
    return corrections


class N6GlobalT16ProlongationCapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_complete_fixed_coverage(self) -> None:
        self.assertEqual(self.payload["fixed_W_count"], 18_564)
        self.assertEqual(
            self.payload["fixed_W_orbit_representative_count"], 1_683
        )
        self.assertEqual(self.payload["extra_axis_count"], 4)
        self.assertEqual(
            self.payload["extra_axis_quadruples_per_W"], 1_391_641_251
        )

    def test_cap_and_sample(self) -> None:
        self.assertEqual(
            self.payload["characteristic_zero_prolongation_upper_cap_t16"],
            462,
        )
        sample = self.payload["sample_maximizer"]
        self.assertEqual(sample["base_prolongation_dimension"], 432)
        self.assertEqual(sample["four_axis_increment"], 30)
        self.assertEqual(len(sample["extra_axes"]), 4)

    def test_sparse_pair_bonus_scatter_matches_dense_lookup(self) -> None:
        audit = load_script_module()
        pair_keys = [(0, 1), (0, 3), (2, 4), (4, 5)]
        pair_index = {pair: index for index, pair in enumerate(pair_keys)}
        bonuses = {(0, 3): 7, (1, 5): 11, (4, 5): -2}
        output = np.full(len(pair_keys), 99, dtype=np.int32)
        audit.scatter_indexed_pair_bonuses(bonuses, pair_index, output)
        self.assertEqual(
            output.tolist(),
            [bonuses.get(pair, 0) for pair in pair_keys],
        )

    def test_truncated_mobius_matches_direct_frozen_representative(self) -> None:
        audit = load_script_module()
        (
            _,
            blocks,
            occurrences,
            occurrence_maps,
            representatives,
            _,
        ) = audit.fixed_data()
        w_axes = representatives[484]
        masks, _, _ = audit.base_masks_and_gains(
            w_axes, blocks, occurrences
        )
        expected = tuple(
            reference_mobius_corrections(
                order,
                w_axes,
                masks,
                blocks,
                occurrence_maps,
            )
            for order in (2, 3, 4)
        )
        actual = audit.mobius_corrections_2_to_4(masks, blocks)
        self.assertEqual([len(rows) for rows in actual], [1423, 7925, 8092])
        self.assertEqual(actual, expected)
        self.assertEqual(
            [list(rows) for rows in actual],
            [list(rows) for rows in expected],
        )

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to rebuild the global t16 certificate",
    )
    def test_full_serial_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--workers",
                "1",
                "--verify-json",
                str(FROZEN),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=7_200,
        )
        self.assertIn("t16_cap=462", completed.stdout)
        self.assertIn("N6_GLOBAL_T16_PROLONGATION_CAP_PASS", completed.stdout)

    def test_claim_boundary(self) -> None:
        self.assertIn("alpha-one", self.payload["strict_conclusion"])
        self.assertIn("one-rectangle alpha-two", self.payload["claim_boundary"])
        self.assertIn("lower29", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
