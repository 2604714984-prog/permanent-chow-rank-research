#!/usr/bin/env python3
"""Independent source-fiber replay of the coordinate first-order barrier."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

N = 4
SUBSETS = tuple(combinations(range(6), 4))
PERMS = tuple(permutations(range(N)))
MATCHINGS = tuple(frozenset(r * N + p[r] for r in range(N)) for p in PERMS)
EXPECTED = {
    (0, 0, 0, 0): 19584, (1, 0, 0, 0): 5856,
    (1, 0, 1, 1): 7200, (1, 1, 1, 1): 240,
    (2, 0, 0, 0): 4848, (2, 0, 1, 1): 4032,
    (2, 0, 2, 2): 2592, (2, 1, 1, 1): 864,
    (2, 1, 2, 2): 576, (2, 2, 0, 2): 72,
    (3, 0, 0, 0): 1728, (3, 0, 1, 1): 1152,
    (3, 0, 2, 2): 1152, (3, 1, 0, 1): 864,
    (4, 0, 0, 0): 2064, (4, 0, 2, 2): 576,
    (4, 1, 0, 1): 576, (6, 0, 0, 0): 288,
}
TRANSFORMS = tuple(
    tuple(rp[c // N] * N + cp[c % N] for c in range(16))
    for rp in PERMS for cp in PERMS
)


def require(ok: bool, message: object) -> None:
    if not ok:
        raise RuntimeError(message)


def envelope(frame: tuple[int, ...]) -> frozenset[int]:
    cells = frozenset(frame)
    return frozenset(i for i, m in enumerate(MATCHINGS) if len(cells & m) >= 3)


def contained(frame: tuple[int, ...]) -> frozenset[int]:
    cells = frozenset(frame)
    return frozenset(i for i, m in enumerate(MATCHINGS) if m <= cells)


def internal(frame: tuple[int, ...]) -> frozenset[int]:
    """Reconstruct the zero-sum source fibers instead of using multiplicities."""
    fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for subset in SUBSETS:
        fibers[tuple(sorted(frame[i] for i in subset))].append(subset)
    out: set[int] = set()
    for fiber in fibers.values():
        if len(fiber) < 2:
            continue
        for label in range(6):
            with_label = [subset for subset in fiber if label in subset]
            if not with_label or len(with_label) == len(fiber):
                continue
            unchanged = frozenset(frame[i] for i in with_label[0] if i != label)
            if len(unchanged) != 3:
                continue
            out.update(i for i, m in enumerate(MATCHINGS) if unchanged <= m)
    return frozenset(out)


def canonical(frame: tuple[int, ...]) -> tuple[int, ...]:
    return min(tuple(sorted(mapping[c] for c in frame)) for mapping in TRANSFORMS)


def degrees(frame: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rows, cols = [0] * N, [0] * N
    for c in frozenset(frame):
        rows[c // N] += 1
        cols[c % N] += 1
    return tuple(sorted(rows, reverse=True)), tuple(sorted(cols, reverse=True))


def local_scan() -> dict[str, object]:
    histogram: Counter[tuple[int, int, int, int]] = Counter()
    equality = []
    for frame in combinations_with_replacement(range(16), 6):
        e, d, k = envelope(frame), contained(frame), internal(frame)
        s = d | k
        profile = (len(e), len(d), len(k), len(s))
        histogram[profile] += 1
        require(s <= e and len(e) + len(s) <= 6, (frame, profile))
        if len(e) + len(s) == 6:
            equality.append(frame)
    require(sum(histogram.values()) == 54264 and dict(histogram) == EXPECTED, histogram)
    require(len(equality) == 864, len(equality))

    eq_profiles = Counter(
        (len(envelope(f)), len(contained(f)), len(internal(f)), len(contained(f) | internal(f)))
        for f in equality
    )
    require(eq_profiles == Counter({(6, 0, 0, 0): 288, (4, 0, 2, 2): 576}), eq_profiles)
    orbits = Counter(canonical(f) for f in equality)
    require(len(orbits) == 4 and sorted(orbits.values()) == [144, 144, 288, 288], orbits)
    distinct = {r: n for r, n in orbits.items() if len(set(r)) == 6}
    repeated = {r: n for r, n in orbits.items() if len(set(r)) == 5}
    require(sorted(distinct.values()) == [144, 144], distinct)
    require(sorted(repeated.values()) == [288, 288], repeated)
    require(all(degrees(r) == ((2, 2, 1, 1), (2, 2, 1, 1)) for r in distinct), distinct)
    require(all(degrees(r) == ((2, 1, 1, 1), (2, 1, 1, 1)) for r in repeated), repeated)

    key = lambda p: f"envelope_{p[0]}_contained_{p[1]}_internal_{p[2]}_unshared_{p[3]}"
    return {
        "unordered_coordinate_frames_checked": 54264,
        "local_profile_histogram": {key(p): n for p, n in sorted(histogram.items())},
        "maximum_envelope_plus_unshared": 6,
        "maximum_contained_matchings": 2,
        "maximum_internal_kernel_matchings": 2,
        "maximum_unshared_matchings": 2,
        "equality_frames": 864,
        "equality_profile_histogram": {key(p): n for p, n in sorted(eq_profiles.items())},
        "equality_row_column_orbits": 4,
        "equality_orbit_sizes": sorted(orbits.values()),
        "distinct_equality_orbits": [list(r) for r in sorted(distinct)],
        "repeated_equality_orbits": [list(r) for r in sorted(repeated)],
    }


def q8_sharpness() -> dict[str, object]:
    orders = {0: (1, 2, 3), 1: (0, 3, 2), 2: (3, 0, 1), 3: (2, 1, 0)}
    four = [
        tuple(sorted((a, b, N + b, N + c, 2 * N + o, 3 * N + o)))
        for o, (a, b, c) in orders.items()
    ]
    incidence = [0] * 24
    for frame in four + four:
        require(not (contained(frame) | internal(frame)), frame)
        for i in envelope(frame):
            incidence[i] += 1
    require(incidence == [2] * 24, incidence)
    return {
        "frame_count": 8,
        "target_matching_count": 24,
        "incidence_degree_distribution": {"2": 24},
        "all_frames_have_empty_unshared_set": True,
        "support_level_equality_only": True,
    }


def core() -> dict[str, object]:
    rows = {
        str(q): {
            "global_incidence_upper": 6 * q,
            "global_incidence_lower": 48,
            "necessary_condition_holds": 48 <= 6 * q,
        }
        for q in range(1, 9)
    }
    return {
        "schema": "general_quartic_coordinate_first_order_eight_term_barrier/v2",
        "field": "characteristic_zero",
        "target": "perm_4_matching_support",
        "local": local_scan(),
        "global": {
            "target_matching_count": 24,
            "local_inequality": "|E(A)|+|S(A)|<=6",
            "non_unshared_target_incidence_floor": 2,
            "minimum_coordinate_regular_first_order_term_count": 8,
            "q_rows": rows,
        },
        "support_level_q8_equality": q8_sharpness(),
        "claim_boundary": {
            "coordinate_regular_first_order_q_le_7": "ZERO",
            "coordinate_regular_first_order_q8_existence": "NOT_PROVED",
            "mu_6_4_exact_value": "OPEN_IN_[6,8]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-core")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = core()
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if args.expected_core:
        require(digest == args.expected_core, (digest, args.expected_core))
    result = dict(payload)
    result["core_sha256"] = digest
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_INDEPENDENT_PASS")
    print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
