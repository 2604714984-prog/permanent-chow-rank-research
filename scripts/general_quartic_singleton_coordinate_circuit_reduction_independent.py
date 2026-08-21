#!/usr/bin/env python3
"""Independent replay for the positive-singleton coordinate reduction.

This implementation imports none of the primary helpers. It reconstructs the
transposition Cayley graph, enumerates support embeddings and repeated-factor
singleton frames, and checks the universal second-order matching envelope.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations

ORDER = 4
GROUP = tuple(permutations(range(ORDER)))
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
        "pairs": ((0, 1), (0, 1), (0, 2), (1, 2), (2, 3)),
        "singletons": (3,),
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
    "double_edge_tail": 888,
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
    "endpoint_marked_p5": {19: 61504, 20: 128996, 21: 105120, 22: 8472, 23: 108},
}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(ORDER))


def inverse(value: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * ORDER
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def conjugate(value: tuple[int, ...], relabeling: tuple[int, ...]) -> tuple[int, ...]:
    return compose(relabeling, compose(value, inverse(relabeling)))


def adjacency() -> dict[tuple[int, ...], set[tuple[int, ...]]]:
    return {
        value: {compose(transposition, value) for transposition in TRANSPOSITIONS}
        for value in GROUP
    }


def abstract_automorphisms(pattern: dict[str, object]) -> tuple[tuple[int, ...], ...]:
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
        moved_singletons = Counter(relabeling[value] for value in singletons)
        if moved_pairs == target_pairs and moved_singletons == target_singletons:
            result.append(relabeling)
    return tuple(result)


def orbit_key(values: tuple[tuple[int, ...], ...], automorphisms: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    index = {value: position for position, value in enumerate(GROUP)}
    candidates = []
    for automorphism in automorphisms:
        ordered = [values[automorphism[position]] for position in range(len(values))]
        left_inverse = inverse(ordered[0])
        normalized = [compose(left_inverse, value) for value in ordered]
        for relabeling in GROUP:
            candidates.append(
                tuple(index[conjugate(value, relabeling)] for value in normalized)
            )
    return min(candidates)


def embedding_orbits(name: str) -> dict[tuple[int, ...], int]:
    graph = adjacency()
    pattern = PATTERNS[name]
    simple_edges = set(tuple(sorted(pair)) for pair in pattern["pairs"])
    automorphisms = abstract_automorphisms(pattern)
    classes: dict[tuple[int, ...], int] = defaultdict(int)
    for remaining in permutations(GROUP[1:], int(pattern["vertices"]) - 1):
        values = (IDENTITY,) + remaining
        if all(values[right] in graph[values[left]] for left, right in simple_edges):
            classes[orbit_key(values, automorphisms)] += 1
    require(len(classes) == EXPECTED_ORBITS[name], (name, len(classes)))
    require(sum(classes.values()) == EXPECTED_EMBEDDINGS[name], (name, sum(classes.values())))
    return dict(classes)


def matching_edges(value: tuple[int, ...]) -> frozenset[int]:
    return frozenset(row * ORDER + value[row] for row in range(ORDER))


def frame_cells_from_unused(unused: tuple[int, int]) -> frozenset[int]:
    return frozenset(set(matching_edges(IDENTITY)) | set(unused))


def singleton_frames() -> tuple[frozenset[int], ...]:
    frames = []
    for unused in combinations_with_replacement(range(ORDER * ORDER), 2):
        frame = frame_cells_from_unused(unused)
        contained = sum(matching_edges(value) <= frame for value in GROUP)
        if contained == 1:
            frames.append(frame)
    require(len(frames) == 130, len(frames))
    require(Counter(map(len, frames)) == Counter({4: 10, 5: 60, 6: 60}), Counter(map(len, frames)))
    return tuple(frames)


def normalize_frame(frame: frozenset[int], base: tuple[int, ...]) -> frozenset[int]:
    result = set()
    for cell in frame:
        row, column = divmod(cell, ORDER)
        result.add(row * ORDER + inverse(base)[column])
    return frozenset(result)


def pair_frame(left: tuple[int, ...], right: tuple[int, ...]) -> frozenset[int]:
    return matching_edges(left) | matching_edges(right)


def support_envelope(frame: frozenset[int], leading: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    result = set()
    for matching in GROUP:
        edges = matching_edges(matching)
        if len(edges & frame) >= 3:
            result.add(matching)
            continue
        if any(len(edges & matching_edges(base)) >= 2 for base in leading):
            result.add(matching)
    return result


def pattern_envelope_histogram(name: str) -> Counter[int]:
    frames = singleton_frames()
    histogram: Counter[int] = Counter()
    for key in embedding_orbits(name):
        values = tuple(GROUP[index] for index in key)
        pattern = PATTERNS[name]
        pair_data = [
            (pair_frame(values[left], values[right]), (values[left], values[right]))
            for left, right in pattern["pairs"]
        ]
        singleton_vertices = tuple(pattern["singletons"])
        if len(singleton_vertices) == 1:
            vertex = singleton_vertices[0]
            base = values[vertex]
            for normalized in frames:
                frame = normalize_frame(normalized, inverse(base))
                union = set()
                for pair_support, leading in pair_data:
                    union.update(support_envelope(pair_support, leading))
                union.update(support_envelope(frame, (base,)))
                histogram[len(union)] += 1
        else:
            left_vertex, right_vertex = singleton_vertices
            left_base = values[left_vertex]
            right_base = values[right_vertex]
            for left_normalized in frames:
                left_frame = normalize_frame(left_normalized, inverse(left_base))
                for right_normalized in frames:
                    right_frame = normalize_frame(right_normalized, inverse(right_base))
                    union = set()
                    for pair_support, leading in pair_data:
                        union.update(support_envelope(pair_support, leading))
                    union.update(support_envelope(left_frame, (left_base,)))
                    union.update(support_envelope(right_frame, (right_base,)))
                    histogram[len(union)] += 1
    require(dict(sorted(histogram.items())) == EXPECTED_HISTOGRAMS[name], (name, histogram))
    require(max(histogram) == EXPECTED_MAXIMA[name], (name, max(histogram)))
    return histogram


def main() -> None:
    for name in PATTERNS:
        pattern_envelope_histogram(name)
    print("GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
