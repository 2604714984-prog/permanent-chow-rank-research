from __future__ import annotations

import importlib.util
import math
import os
import subprocess
import sys
import unittest
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
GPU_SCRIPT = ROOT / "scripts" / "n6_global_t15_gpu_score.py"
BASE_SCRIPT = ROOT / "scripts" / "n6_global_t15_prolongation_cap.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GPU = load_module("n6_global_t15_gpu_score_test", GPU_SCRIPT)
BASE = load_module("n6_global_t15_gpu_base_test", BASE_SCRIPT)


def by_vertex(triples: list[tuple[int, int, int]], axis_count: int):
    rows = [[] for _ in range(axis_count)]
    for index, triple in enumerate(triples):
        for vertex in triple:
            other = [value for value in triple if value != vertex]
            rows[vertex].append((other[0], other[1], index))
    return [
        tuple(
            np.asarray([row[position] for row in vertex_rows], dtype=np.int32)
            for position in range(3)
        )
        for vertex_rows in rows
    ]


class TestN6GlobalT15GpuScore(unittest.TestCase):
    def score_fixture(self):
        axis_count = 6
        triples = list(combinations(range(axis_count), 3))
        gains = np.ones(axis_count, dtype=np.int16)
        gains[1] = -100
        pair_corrections = np.zeros((axis_count, axis_count), dtype=np.int16)
        triple_corrections = np.zeros(len(triples), dtype=np.int16)
        triple_corrections[triples.index((0, 2, 3))] = 4
        triple_corrections[triples.index((1, 4, 5))] = 4
        return axis_count, triples, gains, pair_corrections, triple_corrections

    def test_real_problem_size_is_bounded(self):
        self.assertEqual(math.comb(441, 3), 14_197_260)
        self.assertEqual(math.comb(429, 3), 13_067_054)
        self.assertEqual(GPU.lookup_size_bytes(441), 171_532_242)
        self.assertLess(GPU.lookup_size_bytes(441), 164 * 2**20)

    def test_lookup_maps_all_six_orderings(self):
        lookup = GPU.build_triple_lookup([(0, 2, 3)], 5)
        for ordering in ((0, 2, 3), (0, 3, 2), (2, 0, 3), (2, 3, 0), (3, 0, 2), (3, 2, 0)):
            flat = (ordering[0] * 5 + ordering[1]) * 5 + ordering[2]
            self.assertEqual(int(lookup[flat]), 0)
        self.assertEqual(int(lookup[(0 * 5 + 1) * 5 + 2]), int(GPU.UINT16_SENTINEL))

    def test_cpu_tie_break_is_third_then_first_then_second(self):
        axis_count, triples, gains, pairs, triple_values = self.score_fixture()
        result = BASE.maximize_three_axis_score(
            gains,
            pairs,
            triple_values,
            by_vertex(triples, axis_count),
        )
        self.assertEqual(result, (7, (2, 3, 0)))

    def test_gpu_matches_cpu_when_cupy_is_available(self):
        available, reason = GPU.cupy_status()
        if not available:
            self.skipTest(reason)
        axis_count, triples, gains, pairs, triple_values = self.score_fixture()
        cpu = BASE.maximize_three_axis_score(
            gains,
            pairs,
            triple_values,
            by_vertex(triples, axis_count),
        )
        gpu = GPU.GpuTripleMaximizer(triples, axis_count)
        actual = gpu.maximize(gains, pairs, triple_values, (1,))
        self.assertEqual(actual, cpu)
        with self.assertRaises(AssertionError):
            gpu.maximize(gains, pairs, triple_values[:-1], (1,))

    @unittest.skipUnless(
        os.environ.get("RUN_GPU_REPLAYS") == "1",
        "set RUN_GPU_REPLAYS=1 inside the GPU virtual environment",
    )
    def test_full_gpu_frozen_replay(self):
        frozen = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
        completed = subprocess.run(
            [
                sys.executable,
                str(BASE_SCRIPT),
                "--workers",
                "1",
                "--gpu",
                "--verify-json",
                str(frozen),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=1_800,
        )
        self.assertIn("score_backend=gpu", completed.stdout)
        self.assertIn("t15_cap=458", completed.stdout)


if __name__ == "__main__":
    unittest.main()
