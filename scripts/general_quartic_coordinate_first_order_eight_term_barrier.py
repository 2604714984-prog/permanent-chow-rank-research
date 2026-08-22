#!/usr/bin/env python3
"""Exact coordinate regular first-order barrier for the quartic permanent."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

N = 4
MATCHINGS = tuple(
    frozenset(r * N + p[r] for r in range(N)) for p in permutations(range(N))
)
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


def require(ok: bool, message: object) -> None:
    if not ok:
        raise RuntimeError(message)


def support(frame: tuple[int, ...]) -> frozenset[int]:
    require(len(frame) == 6, frame)
    return frozenset(frame)


def envelope(frame: tuple[int, ...]) -> frozenset[int]:
    cells = support(frame)
    return frozenset(i for i, m in enumerate(MATCHINGS) if len(cells & m) >= 3)


def contained(frame: tuple[int, ...]) -> frozenset[int]:
    cells = support(frame)
    return frozenset(i for i, m in enumerate(MATCHINGS) if m <= cells)


def internal(frame: tuple[int, ...]) -> frozenset[int]:
    """Matchings produced from an internally cancelling squarefree source."""
    multiplicity = Counter(frame)
    out: set[int] = set()
    for i, matching in enumerate(MATCHINGS):
        for triple in combinations(matching, 3):
            triple_set = frozenset(triple)
            if not triple_set <= multiplicity.keys():
                continue
            if any(v >= 2 + int(c in triple_set) for c, v in multiplicity.items()):
                out.add(i)
                break
    return frozenset(out)


def unshared(frame: tuple[int, ...]) -> frozenset[int]:
    return contained(frame) | internal(frame)


def degrees(frame: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rows = [0] * N
    cols = [0] * N
    for cell in support(frame):
        rows[cell // N] += 1
        cols[cell % N] += 1
    return tuple(sorted(rows, reverse=True)), tuple(sorted(cols, reverse=True))


def canonical(frame: tuple[int, ...]) -> tuple[int, ...]:
    counts = Counter(frame)
    candidates = []
    for rp in permutations(range(N)):
        for cp in permutations(range(N)):
            moved = []
            for cell, count in counts.items():
                moved.extend([rp[cell // N] * N + cp[cell % N]] * count)
            candidates.append(tuple(sorted(moved)))
    return min(candidates)


@lru_cache(maxsize=1)
def local_scan() -> dict[str, object]:
    histogram: Counter[tuple[int, int, int, int]] = Counter()
    equality: list[tuple[int, ...]] = []
    for frame in combinations_with_replacement(range(16), 6):
        e, d, k = envelope(frame), contained(frame), internal(frame)
        s = d | k
        profile = (len(e), len(d), len(k), len(s))
        histogram[profile] += 1
        require(s <= e and len(e) + len(s) <= 6, (frame, profile))
        if len(e) + len(s) == 6:
            equality.append(frame)

    require(sum(histogram.values()) == 54264, histogram)
    require(dict(histogram) == EXPECTED, histogram)
    require(len(equality) == 864, len(equality))
    equality_profiles = Counter(
        (len(envelope(f)), len(contained(f)), len(internal(f)), len(unshared(f)))
        for f in equality
    )
    require(equality_profiles == Counter({(6, 0, 0, 0): 288, (4, 0, 2, 2): 576}), equality_profiles)

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
        "equality_profile_histogram": {key(p): n for p, n in sorted(equality_profiles.items())},
        "equality_row_column_orbits": 4,
        "equality_orbit_sizes": sorted(orbits.values()),
        "distinct_equality_orbits": [list(r) for r in sorted(distinct)],
        "repeated_equality_orbits": [list(r) for r in sorted(repeated)],
    }


def q8_sharpness() -> dict[str, object]:
    orders = {0: (1, 2, 3), 1: (0, 3, 2), 2: (3, 0, 1), 3: (2, 1, 0)}
    four = []
    for omitted, (a, b, c) in orders.items():
        four.append(tuple(sorted((a, b, N + b, N + c, 2 * N + omitted, 3 * N + omitted))))
    incidence = [0] * 24
    for frame in tuple(four + four):
        require(not unshared(frame), frame)
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


def theorem_core() -> dict[str, object]:
    rows = {
        str(q): {
            "global_incidence_upper": 6 * q,
            "global_incidence_lower": 48,
            "necessary_condition_holds": 48 <= 6 * q,
        }
        for q in range(1, 9)
    }
    require(all(not rows[str(q)]["necessary_condition_holds"] for q in range(1, 8)), rows)
    require(rows["8"]["necessary_condition_holds"], rows)
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


def payload() -> dict[str, object]:
    core = theorem_core()
    result = dict(core)
    result["core_sha256"] = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = payload()
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_BARRIER_PASS")
    print(result["core_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
