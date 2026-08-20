#!/usr/bin/env python3
"""N6-118: exact fixed-point exclusion for 12-plane 3x4/4x3 products.

The certificate is deliberately small.  It counts, for every coordinate
product support in the two N6-101 hooks, the permanent rectangles which can
be block diagonal for a coordinate 6+6 partition.  The maximum is below the
12 rectangle directions required by a twelve-plane section difference.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_34_twelve_pair_exclusion.json"
SHADOW12_SCRIPT = ROOT / "scripts" / "n6_shadow12_nonproduct_collision_exclusion.py"
SIX_MASKS = tuple(sum(1 << i for i in subset) for subset in combinations(range(12), 6))


def load_shadow12_module():
    spec = importlib.util.spec_from_file_location("n6_shadow12_for_n6118", SHADOW12_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SHADOW12_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def local_edges(cells, rectangle_masks, rows, columns):
    selected = [
        index
        for index, (row, column) in enumerate(cells)
        if row in rows and column in columns
    ]
    require(len(selected) == len(rows) * len(columns), (rows, columns, selected))
    local = {global_index: local_index for local_index, global_index in enumerate(selected)}
    cell_to_local = {cells[index]: local[index] for index in selected}
    edge_pairs = []
    for rectangle in rectangle_masks:
        if any(rectangle >> index & 1 for index in range(len(cells)) if index not in local):
            continue
        corners = [cells[index] for index in selected if rectangle >> index & 1]
        if len(corners) != 4:
            continue
        row_pair = sorted({point[0] for point in corners})
        column_pair = sorted({point[1] for point in corners})
        require(len(row_pair) == 2 and len(column_pair) == 2, corners)
        a = cell_to_local[row_pair[0], column_pair[0]]
        b = cell_to_local[row_pair[0], column_pair[1]]
        c = cell_to_local[row_pair[1], column_pair[0]]
        d = cell_to_local[row_pair[1], column_pair[1]]
        edge_pairs.append(((1 << a) | (1 << d), (1 << b) | (1 << c)))
    return tuple(edge_pairs)


def safe_rectangle_count(edge_pairs, left: int) -> int:
    right = ((1 << 12) - 1) ^ left
    count = 0
    for first, second in edge_pairs:
        if all(
            (edge & left in (0, edge)) and (edge & right in (0, edge))
            for edge in (first, second)
        ):
            count += 1
    return count


def product_summary(kind: str, row_size: int, column_size: int) -> dict[str, object]:
    shadow12 = load_shadow12_module()
    cells, rectangle_masks = shadow12.hook_data(kind)
    endpoint_rows = []
    histogram: Counter[str] = Counter()
    for rows in combinations(range(6), row_size):
        for columns in combinations(range(6), column_size):
            selected = [
                index
                for index, (row, column) in enumerate(cells)
                if row in rows and column in columns
            ]
            if len(selected) != row_size * column_size:
                continue
            edges = local_edges(cells, rectangle_masks, rows, columns)
            if len(edges) < 12:
                continue
            maximum = max(safe_rectangle_count(edges, left) for left in SIX_MASKS)
            row_entry = {
                "rows": list(rows),
                "columns": list(columns),
                "rectangle_count": len(edges),
                "maximum_block_diagonal_rectangles": maximum,
            }
            endpoint_rows.append(row_entry)
            histogram[f"{len(edges)}/{maximum}"] += 1
    endpoint_rows.sort(key=lambda row: (row["rows"], row["columns"]))
    return {
        "endpoint_count": len(endpoint_rows),
        "histogram_rectangle_count_over_maximum": dict(sorted(histogram.items())),
        "maximum_over_endpoints": max(
            (row["maximum_block_diagonal_rectangles"] for row in endpoint_rows),
            default=0,
        ),
        "endpoints": endpoint_rows,
    }


def build_payload() -> dict[str, object]:
    products = {}
    for kind in ("standard", "biflag"):
        products[kind] = {}
        for row_size, column_size in ((2, 6), (3, 4), (4, 3)):
            products[kind][f"{row_size}x{column_size}"] = product_summary(
                kind, row_size, column_size
            )

    expected = {
        "standard": {"2x6": 3, "3x4": 30, "4x3": 10},
        "biflag": {"2x6": 0, "3x4": 20, "4x3": 14},
    }
    for kind, shapes in expected.items():
        for shape, count in shapes.items():
            actual = products[kind][shape]["endpoint_count"]
            require(actual == count, (kind, shape, actual, count))

    # The 2x6 case is already a pure theorem in N6-111.  The new finite
    # certificate is needed only for the 3x4 and 4x3 threshold-12 products.
    for kind in products:
        for shape in ("3x4", "4x3"):
            require(products[kind][shape]["maximum_over_endpoints"] < 12, products[kind][shape])

    return {
        "status": "EXACT_COORDINATE_PRODUCT_12_BLOCK_DIAGONAL_OBSTRUCTION",
        "field": "algebraically closed characteristic zero",
        "interfaces": {
            "N6-110": "Every twelve-plane D in E2 intersect (Sym^2 L + Sym^2 M) has derivative L direct-sum M.",
            "N6-111": "The full 2x6 twelve-plane product case has no complementary Chow pair.",
            "N6-112": "The e=12 nonproduct fixed components are diagonal and actual complementary components specialize to product supports.",
        },
        "products": products,
        "fixed_point_lemma": {
            "coordinate_D_has_distinct_rectangle_weights": True,
            "block_diagonal_rectangle_test": "Both opposite-corner edges of every selected permanent rectangle must stay in one side of the coordinate 6+6 partition.",
            "three_by_four_and_four_by_three_maximum": 10,
            "twelve_directions_are_required": True,
            "conclusion": "No coordinate 3x4 or 4x3 product fixed point supports a block-diagonal twelve-plane D.",
        },
        "global_incidence_consequence": "Every torus-fixed 3x4 or 4x3 product endpoint has no coordinate complementary block-diagonal twelve-plane. A noncoordinate formal branch can still specialize to a non-block-diagonal or diagonal boundary point and is not excluded by this certificate.",
        "claim_boundary": "This is an exact coordinate fixed-point obstruction. It does not by itself close the kappa2=0 incidence, ordinary lower 29, ChowRank(perm_6)=32, the a2=73,74,75 layers, or a border-rank bound.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == frozen, args.verify_json)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
