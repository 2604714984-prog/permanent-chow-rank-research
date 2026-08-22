#!/usr/bin/env python3
"""Fast independent replay for the corrected positive-singleton reduction.

The implementation imports no primary helper. It rebuilds the transposition
Cayley graph, support embeddings, repeated-factor singleton frames, and every
second-order envelope histogram using integer bit masks.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations

ORDER = 4
GROUP = tuple(permutations(range(ORDER)))
INDEX = {value: position for position, value in enumerate(GROUP)}
IDENTITY = tuple(range(ORDER))
TRANSPOSITIONS = tuple(
    tuple(
        right if value == left else left if value == right else value
        for value in range(ORDER)
    )
    for left, right in combinations(range(ORDER), 2)
)

PATTERNS = {
    "square_lollipop": {
        "vertices": 5,
        "pairs": ((0, 1), (1, 2), (2, 3), (3, 0), (3, 4)),
        "singletons": (4,),
    },
    "double_edge_tail": {
        "vertices": 5,
        "pairs": ((0, 1), (0, 1), (0, 2), (2, 3), (3, 4)),
        "singletons": (4,),
    },
    "endpoint_marked_p5": {
        "vertices": 5,
        "pairs": ((0, 1), (1, 2), (2, 3), (3, 4)),
        "singletons": (0, 4),
    },
}

EXPECTED_ORBITS = {
    "square_lollipop": 5,
    "double_edge_tail": 29,
    "endpoint_marked_p5": 18,
}
EXPECTED_EMBEDDINGS = {
    "square_lollipop": 216,
    "double_edge_tail": 696,
    "endpoint_marked_p5": 696,
}
EXPECTED_MAXIMA = {
    "square_lollipop": 22,
    "double_edge_tail": 22,
    "endpoint_marked_p5": 23,
}
EXPECTED_HISTOGRAMS = {
    "square_lollipop": {19: 124, 20: 254, 21: 260, 22: 12},
    "double_edge_tail": {19: 744, 20: 2020, 21: 970, 22: 36},
    "endpoint_marked_p5": {
        19: 61504,
        20: 128996,
        21: 105120,
        22: 8472,
        23: 108,
    },
}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(ORDER))


def inverse(value: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * ORDER
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def conjugate(
    value: tuple[int, ...],
    relabeling: tuple[int, ...],
) -> tuple[int, ...]:
    return compose(relabeling, compose(value, inverse(relabeling)))


ADJACENCY = tuple(
    frozenset(
        INDEX[compose(transposition, value)]
        for transposition in TRANSPOSITIONS
    )
    for value in GROUP
)
MATCHING_MASKS = tuple(
    sum(1 << (row * ORDER + value[row]) for row in range(ORDER))
    for value in GROUP
)


def abstract_automorphisms(
    pattern: dict[str, object],
) -> tuple[tuple[int, ...], ...]:
    vertex_count = int(pattern["vertices"])
    pairs = tuple(pattern["pairs"])
    singletons = tuple(pattern["singletons"])
    target_pairs = Counter(tuple(sorted(pair)) for pair in pairs)
    target_singletons = Counter(singletons)
    result = []
    for relabeling in permutations(range(vertex_count)):
        moved_pairs = Counter(
            tuple(sorted((relabeling[left], relabeling[right])))
            for left, right in pairs
        )
        moved_singletons = Counter(
            relabeling[value] for value in singletons
        )
        if moved_pairs == target_pairs and moved_singletons == target_singletons:
            result.append(relabeling)
    return tuple(result)


def orbit_key(
    values: tuple[int, ...],
    automorphisms: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    candidates = []
    group_values = tuple(GROUP[index] for index in values)
    for automorphism in automorphisms:
        ordered = [
            group_values[automorphism[position]]
            for position in range(len(group_values))
        ]
        left_inverse = inverse(ordered[0])
        normalized = [compose(left_inverse, value) for value in ordered]
        for relabeling in GROUP:
            candidates.append(
                tuple(
                    INDEX[conjugate(value, relabeling)]
                    for value in normalized
                )
            )
    return min(candidates)


@lru_cache(maxsize=None)
def embedding_orbits(name: str) -> dict[tuple[int, ...], int]:
    pattern = PATTERNS[name]
    simple_edges = {tuple(sorted(pair)) for pair in pattern["pairs"]}
    automorphisms = abstract_automorphisms(pattern)
    classes: dict[tuple[int, ...], int] = defaultdict(int)
    for remaining in permutations(
        range(1, len(GROUP)),
        int(pattern["vertices"]) - 1,
    ):
        values = (0,) + remaining
        if all(
            values[right] in ADJACENCY[values[left]]
            for left, right in simple_edges
        ):
            classes[orbit_key(values, automorphisms)] += 1
    require(len(classes) == EXPECTED_ORBITS[name], (name, len(classes)))
    require(sum(classes.values()) == EXPECTED_EMBEDDINGS[name], (name, sum(classes.values())))
    return dict(classes)


@lru_cache(maxsize=1)
def singleton_frames() -> tuple[int, ...]:
    identity_mask = MATCHING_MASKS[0]
    frames = []
    for left, right in combinations_with_replacement(range(ORDER * ORDER), 2):
        frame_mask = identity_mask | (1 << left) | (1 << right)
        contained = sum(
            (matching_mask & frame_mask) == matching_mask
            for matching_mask in MATCHING_MASKS
        )
        if contained == 1:
            frames.append(frame_mask)
    require(len(frames) == 130, len(frames))
    require(
        Counter(mask.bit_count() for mask in frames)
        == Counter({4: 10, 5: 60, 6: 60}),
        Counter(mask.bit_count() for mask in frames),
    )
    return tuple(frames)


@lru_cache(maxsize=None)
def transform_identity_frame(frame_mask: int, base_index: int) -> int:
    base = GROUP[base_index]
    result = 0
    for cell in range(ORDER * ORDER):
        if frame_mask >> cell & 1:
            row, column = divmod(cell, ORDER)
            result |= 1 << (row * ORDER + base[column])
    return result


@lru_cache(maxsize=None)
def envelope_bits(frame_mask: int, leading: tuple[int, ...]) -> int:
    result = 0
    for index, matching_mask in enumerate(MATCHING_MASKS):
        if (matching_mask & frame_mask).bit_count() >= 3:
            result |= 1 << index
            continue
        if any(
            (matching_mask & MATCHING_MASKS[base_index]).bit_count() >= 2
            for base_index in leading
        ):
            result |= 1 << index
    return result


def pair_envelope(left: int, right: int) -> int:
    return envelope_bits(
        MATCHING_MASKS[left] | MATCHING_MASKS[right],
        (left, right),
    )


@lru_cache(maxsize=None)
def pattern_envelope_histogram(name: str) -> Counter[int]:
    frames = singleton_frames()
    histogram: Counter[int] = Counter()
    pattern = PATTERNS[name]
    for key in embedding_orbits(name):
        values = tuple(key)
        base_union = 0
        for left, right in pattern["pairs"]:
            base_union |= pair_envelope(values[left], values[right])
        singleton_vertices = tuple(pattern["singletons"])
        if len(singleton_vertices) == 1:
            base_index = values[singleton_vertices[0]]
            singleton_envelopes = [
                envelope_bits(
                    transform_identity_frame(frame, base_index),
                    (base_index,),
                )
                for frame in frames
            ]
            for singleton_envelope in singleton_envelopes:
                histogram[(base_union | singleton_envelope).bit_count()] += 1
        else:
            left_index = values[singleton_vertices[0]]
            right_index = values[singleton_vertices[1]]
            left_envelopes = [
                envelope_bits(
                    transform_identity_frame(frame, left_index),
                    (left_index,),
                )
                for frame in frames
            ]
            right_envelopes = [
                envelope_bits(
                    transform_identity_frame(frame, right_index),
                    (right_index,),
                )
                for frame in frames
            ]
            for left_envelope in left_envelopes:
                partial = base_union | left_envelope
                for right_envelope in right_envelopes:
                    histogram[(partial | right_envelope).bit_count()] += 1
    require(
        dict(sorted(histogram.items())) == EXPECTED_HISTOGRAMS[name],
        (name, histogram),
    )
    require(max(histogram) == EXPECTED_MAXIMA[name], (name, max(histogram)))
    return histogram


def main() -> int:
    for name in PATTERNS:
        pattern_envelope_histogram(name)
    print(
        "GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_"
        "INDEPENDENT_PASS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
