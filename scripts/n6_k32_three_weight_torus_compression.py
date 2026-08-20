"""Exact three-weight torus compression for the K3,2 first-Schur rays.

This certificate is deliberately narrower than a full tangent-cone theorem.
It uses the 44 exact rank-three rays from N6-126 and the exact pair-pencil
test from N6-128 to control supports whose characters are affinely independent.
"""

from __future__ import annotations

import argparse
import ast
import json
from itertools import combinations
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_k32_two_line_pencil_classification import candidate_data
except ModuleNotFoundError:  # Direct script execution.
    from n6_k32_two_line_pencil_classification import candidate_data


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_three_weight_torus_compression.json"
PAIR_SAMPLES = (1, 2, 3, 5)


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def parse_weight(name: str) -> tuple[int, ...]:
    """Return the row/column torus character of one candidate ray.

    A graph variable from source (row, column) to target (row, column) has
    character ``e_target_row-e_source_row`` together with
    ``f_target_column-f_source_column``.  The columns are 0,1 in the base
    and 2,3 in the complementary plane.
    """

    _kind, rest = name.split(":", 1)
    key_text, _vector_text = rest.rsplit(":", 1)
    key = ast.literal_eval(key_text)
    if key[0] == 1:
        _tag, target_row, source_row, target_column, source_column = key
    else:
        _tag, target_column, source_column = key
        target_row = source_row = 0
    row = [0, 0, 0]
    row[target_row] += 1
    row[source_row] -= 1
    column = [0, 0, 0, 0]
    column[target_column + 2] += 1
    column[source_column] -= 1
    return tuple(row + column)


def exact_rank_sum(
    left: list[list[int]], right: list[list[int]], value: int
) -> int:
    matrix = sp.Matrix(
        [
            [value * left[row][column] + right[row][column] for column in range(15)]
            for row in range(33)
        ]
    )
    return int(matrix.rank())


def compatible_pairs(
    matrices: list[list[list[int]]],
) -> list[tuple[int, int]]:
    """Classify identically rank-three pair pencils over QQ.

    Every 4 by 4 minor of ``t*A+B`` has degree at most three because both
    endpoints have rank three.  Four finite exact samples therefore suffice
    to certify that all minors vanish identically.
    """

    result: list[tuple[int, int]] = []
    for left, right in combinations(range(len(matrices)), 2):
        if all(
            exact_rank_sum(matrices[left], matrices[right], value) <= 3
            for value in PAIR_SAMPLES
        ):
            result.append((left, right))
    return result


def affine_rank(weights: list[tuple[int, ...]], indices: tuple[int, ...]) -> int:
    base = weights[indices[0]]
    rows = [
        [value - reference for value, reference in zip(weights[index], base, strict=True)]
        for index in indices[1:]
    ]
    return int(sp.Matrix(rows).rank()) if rows else 0


def cliques_of_size_four(
    adjacency: list[set[int]],
) -> list[tuple[int, int, int, int]]:
    result: list[tuple[int, int, int, int]] = []
    for clique in combinations(range(len(adjacency)), 4):
        if all(right in adjacency[left] for left, right in combinations(clique, 2)):
            result.append(clique)
    return result


def build_payload() -> dict[str, object]:
    names, matrices = candidate_data()
    require(len(names) == 44, len(names))
    weights = [parse_weight(name) for name in names]
    pairs = compatible_pairs(matrices)
    require(len(pairs) == 102, len(pairs))

    adjacency = [set() for _ in names]
    for left, right in pairs:
        adjacency[left].add(right)
        adjacency[right].add(left)

    triangles: list[tuple[int, int, int]] = []
    for left in range(len(names)):
        for middle in sorted(index for index in adjacency[left] if index > left):
            for right in sorted(
                index for index in adjacency[left] & adjacency[middle] if index > middle
            ):
                triangles.append((left, middle, right))
    require(len(triangles) == 52, len(triangles))

    triangle_affine_histogram: dict[str, int] = {}
    degenerate_compatible = 0
    for triangle in triangles:
        rank = affine_rank(weights, triangle)
        key = str(rank)
        triangle_affine_histogram[key] = triangle_affine_histogram.get(key, 0) + 1
        if rank < 2:
            degenerate_compatible += 1

    cliques = cliques_of_size_four(adjacency)
    require(len(cliques) == 13, len(cliques))
    triangles_outside = sum(
        not any(set(triangle).issubset(clique) for clique in cliques)
        for triangle in triangles
    )
    require(triangles_outside == 0, triangles_outside)

    # A five-clique would extend one of the listed four-cliques.  This avoids
    # any five-subset materialization while certifying the graph clique bound.
    four_clique_extensions = 0
    for clique in cliques:
        common = set.intersection(*(adjacency[index] for index in clique))
        if common.difference(clique):
            four_clique_extensions += 1
    require(four_clique_extensions == 0, four_clique_extensions)

    coefficient_symbols = sp.symbols("a0:4")
    four_clique_ranks: list[int] = []
    for clique in cliques:
        rows = [
            [
                sum(
                    coefficient_symbols[position] * matrices[clique[position]][row][column]
                    for position in range(4)
                )
                for column in range(15)
            ]
            for row in range(33)
        ]
        rank = int(sp.Matrix(rows).rank())
        four_clique_ranks.append(rank)
        require(rank == 3, (clique, rank))

    return {
        "certificate": "N6-135",
        "status": "EXACT_QQ_THREE_WEIGHT_TORUS_COMPRESSION",
        "field": "characteristic zero",
        "hypothesis": "full 72-variable Grassmann graph chart at L=M=A3 tensor P2",
        "candidate_count": len(names),
        "candidate_names": names,
        "character_convention": "(target row-source row, target column-source column)",
        "pair_samples": list(PAIR_SAMPLES),
        "pair_count": len(names) * (len(names) - 1) // 2,
        "identically_rank_three_pair_count": len(pairs),
        "compatible_pairs": [list(pair) for pair in pairs],
        "triangle_count": len(triangles),
        "triangle_affine_rank_histogram": triangle_affine_histogram,
        "degenerate_compatible_triangle_count": degenerate_compatible,
        "four_clique_count": len(cliques),
        "four_cliques": [list(clique) for clique in cliques],
        "four_clique_names": [
            [names[index] for index in clique] for clique in cliques
        ],
        "four_clique_symbolic_ranks": four_clique_ranks,
        "triangles_outside_four_cliques": triangles_outside,
        "four_clique_extension_count": four_clique_extensions,
        "consequence": (
            "If three distinct candidate rays have nonzero coefficients and "
            "affinely independent torus characters, a rank-at-most-three "
            "point in their span has a dense torus orbit in the projective "
            "plane. The closed determinantal locus then contains the whole "
            "three-ray span, so its three pairs are compatible. The exact "
            "graph forces that triangle into one of the 13 listed four-ray "
            "rank-three subspaces. No compatible triangle is affine-degenerate, "
            "and the graph has no five-clique."
        ),
        "boundary": [
            "does not classify affine-degenerate character triples",
            "does not classify repeated rays in one same-row character block",
            "does not classify supports with four or more distinct weights "
            "whose character span is not the full projective span",
            "does not classify nonlinear lifts or arbitrary invertible graph operators",
            "does not prove ordinary lower 29 or exact Chow rank 32",
            "does not make a border-rank claim",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, "frozen payload mismatch")
    print("certificate=N6-135")
    print("candidate_count=44")
    print("compatible_pairs=102")
    print("triangles=52")
    print("four_cliques=13")
    print("status=PASS")


if __name__ == "__main__":
    main()
