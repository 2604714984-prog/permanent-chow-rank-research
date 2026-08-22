#!/usr/bin/env python3
"""Optional exact GPU benchmark for the N6-051 three-axis score maximizer.

This is a performance path, not a proof dependency.  The default certificate
continues to use the NumPy implementation in
``n6_global_t15_prolongation_cap.py``.  The GPU kernel uses signed 32-bit
integer arithmetic and preserves the historical CPU tie break exactly.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import time
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_global_t15_prolongation_cap.py"
UINT16_SENTINEL = np.iinfo(np.uint16).max
DEFAULT_LOOKUP_LIMIT_BYTES = 512 * 2**20


CUDA_SOURCE = r"""
extern "C" __global__
void maximize_ordered_pairs(
    const short* gains,
    const short* pair_corrections,
    const unsigned short* triple_lookup,
    const short* triple_corrections,
    const unsigned char* excluded,
    const int axis_count,
    int* output_scores,
    int* output_keys)
{
    const int pair_index = blockDim.x * blockIdx.x + threadIdx.x;
    const int pair_count = axis_count * axis_count;
    if (pair_index >= pair_count) {
        return;
    }

    const int first = pair_index / axis_count;
    const int second = pair_index - first * axis_count;
    const int score_floor = -2147483647;
    const int key_ceiling = 2147483647;
    if (first == second || excluded[first] || excluded[second]) {
        output_scores[pair_index] = score_floor;
        output_keys[pair_index] = key_ceiling;
        return;
    }

    int best_score = score_floor;
    int best_key = key_ceiling;
    const int pair_offset = first * axis_count + second;
    for (int third = 0; third < axis_count; ++third) {
        if (third == first || third == second || excluded[third]) {
            continue;
        }
        int score = (int)gains[first] + (int)gains[second]
            + (int)gains[third]
            + (int)pair_corrections[pair_offset]
            + (int)pair_corrections[first * axis_count + third]
            + (int)pair_corrections[second * axis_count + third];
        const int triple_offset =
            (first * axis_count + second) * axis_count + third;
        const unsigned short correction_index = triple_lookup[triple_offset];
        if (correction_index != 65535u) {
            score += (int)triple_corrections[correction_index];
        }
        const int key = (third * axis_count + first) * axis_count + second;
        if (score > best_score || (score == best_score && key < best_key)) {
            best_score = score;
            best_key = key;
        }
    }
    output_scores[pair_index] = best_score;
    output_keys[pair_index] = best_key;
}
"""


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_base_module():
    spec = importlib.util.spec_from_file_location("n6_t15_gpu_base", BASE_SCRIPT)
    require(spec is not None and spec.loader is not None, BASE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lookup_size_bytes(axis_count: int) -> int:
    return axis_count**3 * np.dtype(np.uint16).itemsize


def build_triple_lookup(
    triples: list[tuple[int, int, int]],
    axis_count: int,
    *,
    byte_limit: int = DEFAULT_LOOKUP_LIMIT_BYTES,
) -> np.ndarray:
    """Map every ordered triple permutation to one sparse correction index."""

    required_bytes = lookup_size_bytes(axis_count)
    require(required_bytes <= byte_limit, (required_bytes, byte_limit))
    require(len(triples) < int(UINT16_SENTINEL), len(triples))
    lookup = np.full(axis_count**3, UINT16_SENTINEL, dtype=np.uint16)
    if not triples:
        return lookup

    rows = np.asarray(triples, dtype=np.int64)
    require(rows.shape == (len(triples), 3), rows.shape)
    require(int(rows.min()) >= 0 and int(rows.max()) < axis_count, rows.shape)
    correction_indices = np.arange(len(triples), dtype=np.uint16)
    first, second, third = rows.T
    for left, middle, right in (
        (first, second, third),
        (first, third, second),
        (second, first, third),
        (second, third, first),
        (third, first, second),
        (third, second, first),
    ):
        flat = (left * axis_count + middle) * axis_count + right
        lookup[flat] = correction_indices
    return lookup


def decode_key(key: int, axis_count: int) -> tuple[int, int, int]:
    third, remainder = divmod(key, axis_count**2)
    first, second = divmod(remainder, axis_count)
    return first, second, third


class GpuTripleMaximizer:
    """Persistent CuPy kernel state; the 164 MiB lookup is uploaded once."""

    def __init__(self, triples: list[tuple[int, int, int]], axis_count: int):
        import cupy as cp

        self.cp = cp
        self.axis_count = axis_count
        self.triple_count = len(triples)
        lookup = build_triple_lookup(triples, axis_count)
        self.triple_lookup = cp.asarray(lookup)
        self.kernel = cp.RawKernel(CUDA_SOURCE, "maximize_ordered_pairs")
        pair_count = axis_count**2
        self.output_scores = cp.empty(pair_count, dtype=cp.int32)
        self.output_keys = cp.empty(pair_count, dtype=cp.int32)

    def maximize(
        self,
        gains: np.ndarray,
        pair_corrections: np.ndarray,
        triple_corrections: np.ndarray,
        excluded_axes: tuple[int, ...],
    ) -> tuple[int, tuple[int, int, int]]:
        cp = self.cp
        axis_count = self.axis_count
        require(gains.shape == (axis_count,), gains.shape)
        require(pair_corrections.shape == (axis_count, axis_count), pair_corrections.shape)
        require(triple_corrections.shape == (self.triple_count,), triple_corrections.shape)
        for values in (gains, pair_corrections, triple_corrections):
            require(np.issubdtype(values.dtype, np.integer), values.dtype)
            if values.dtype != np.int16:
                require(
                    int(values.min()) >= np.iinfo(np.int16).min
                    and int(values.max()) <= np.iinfo(np.int16).max,
                    (values.dtype, int(values.min()), int(values.max())),
                )
        excluded = np.zeros(axis_count, dtype=np.uint8)
        excluded[list(excluded_axes)] = 1
        device_gains = cp.asarray(np.ascontiguousarray(gains, dtype=np.int16))
        device_pairs = cp.asarray(
            np.ascontiguousarray(pair_corrections, dtype=np.int16)
        )
        device_triples = cp.asarray(
            np.ascontiguousarray(triple_corrections, dtype=np.int16)
        )
        device_excluded = cp.asarray(excluded)
        pair_count = axis_count**2
        threads = 256
        blocks = (pair_count + threads - 1) // threads
        self.kernel(
            (blocks,),
            (threads,),
            (
                device_gains,
                device_pairs,
                self.triple_lookup,
                device_triples,
                device_excluded,
                np.int32(axis_count),
                self.output_scores,
                self.output_keys,
            ),
        )
        best_score = int(cp.max(self.output_scores).get())
        best_key = int(
            cp.min(
                cp.where(
                    self.output_scores == best_score,
                    self.output_keys,
                    np.iinfo(np.int32).max,
                )
            ).get()
        )
        return best_score, decode_key(best_key, axis_count)


def cupy_status() -> tuple[bool, str]:
    try:
        import cupy as cp

        count = int(cp.cuda.runtime.getDeviceCount())
        if count < 1:
            return False, "CuPy is installed but no CUDA device is visible"
        return True, cp.cuda.runtime.getDeviceProperties(0)["name"].decode()
    except Exception as exc:  # Optional dependency and driver probe.
        return False, f"{type(exc).__name__}: {exc}"


def benchmark(representative_index: int, warm_runs: int) -> dict[str, object]:
    base = load_base_module()
    base_module = base.load_base_module()
    fixed = base.fixed_combinatorics(base_module)
    (
        _,
        blocks,
        occurrences,
        occurrence_maps,
        representatives,
        _,
        edges,
        triples,
        triple_blocks,
        by_vertex,
    ) = fixed
    require(0 <= representative_index < len(representatives), representative_index)
    w_axes = representatives[representative_index]

    data_started = time.perf_counter()
    base_dimension, gains, pair_corrections, triple_corrections = (
        base.representative_score_data(
            w_axes,
            blocks,
            occurrences,
            occurrence_maps,
            edges,
            triples,
            triple_blocks,
        )
    )
    data_seconds = time.perf_counter() - data_started

    cpu_started = time.perf_counter()
    cpu_result = base.maximize_three_axis_score(
        gains,
        pair_corrections,
        triple_corrections,
        by_vertex,
    )
    cpu_seconds = time.perf_counter() - cpu_started

    setup_started = time.perf_counter()
    gpu = GpuTripleMaximizer(triples, base.AXIS_COUNT)
    setup_seconds = time.perf_counter() - setup_started
    cold_started = time.perf_counter()
    gpu_result = gpu.maximize(
        gains,
        pair_corrections,
        triple_corrections,
        w_axes,
    )
    gpu.cp.cuda.Stream.null.synchronize()
    cold_seconds = time.perf_counter() - cold_started
    require(gpu_result == cpu_result, (cpu_result, gpu_result))

    warm_times = []
    for _ in range(warm_runs):
        started = time.perf_counter()
        repeated = gpu.maximize(
            gains,
            pair_corrections,
            triple_corrections,
            w_axes,
        )
        gpu.cp.cuda.Stream.null.synchronize()
        warm_times.append(time.perf_counter() - started)
        require(repeated == cpu_result, (cpu_result, repeated))

    return {
        "status": "OPTIONAL_GPU_SCORE_BENCHMARK_PASS",
        "representative_index": representative_index,
        "base_dimension": base_dimension,
        "score_result": [cpu_result[0], list(cpu_result[1])],
        "axis_count": base.AXIS_COUNT,
        "ambient_candidate_triple_count": int(base.comb(base.AXIS_COUNT, 3)),
        "effective_candidate_triple_count": int(
            base.comb(base.AXIS_COUNT - len(w_axes), 3)
        ),
        "triple_lookup_bytes": lookup_size_bytes(base.AXIS_COUNT),
        "score_data_seconds": data_seconds,
        "cpu_score_seconds": cpu_seconds,
        "gpu_setup_seconds": setup_seconds,
        "gpu_cold_score_seconds": cold_seconds,
        "gpu_warm_score_seconds": warm_times,
        "gpu_best_warm_seconds": min(warm_times),
        "score_stage_speedup": cpu_seconds / min(warm_times),
        "boundary": (
            "This measures only the exact three-axis maximization stage. "
            "Orbit construction and correction generation remain on CPU."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--representative-index", type=int, default=0)
    parser.add_argument("--warm-runs", type=int, default=3)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--require-gpu", action="store_true")
    args = parser.parse_args()
    require(1 <= args.warm_runs <= 20, args.warm_runs)

    available, device = cupy_status()
    if not available:
        print(f"GPU_BENCHMARK_SKIPPED: {device}")
        print("Install an isolated CuPy CUDA 13 environment to run this benchmark.")
        return 2 if args.require_gpu else 0

    payload = benchmark(args.representative_index, args.warm_runs)
    payload["device"] = device
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
