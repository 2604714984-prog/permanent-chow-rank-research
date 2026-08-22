"""Exact torus exposed-face audit for the K3,2 full graph chart."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_torus_exposed_weight_faces.json"


BlockLabel = tuple[str, int, int, int, int]


def block_labels() -> tuple[BlockLabel, ...]:
    labels: list[BlockLabel] = []
    for target_row in range(3):
        for source_row in range(3):
            if target_row == source_row:
                continue
            for target_column in range(2):
                for source_column in range(2):
                    labels.append(
                        ("row", target_row, source_row, target_column, source_column)
                    )
    for target_column in range(2):
        for source_column in range(2):
            labels.append(("same", 0, 0, target_column, source_column))
    return tuple(labels)


def character(label: BlockLabel) -> tuple[int, ...]:
    kind, target_row, source_row, target_column, source_column = label
    vector = [0] * 7
    if kind == "row":
        vector[target_row] += 1
        vector[source_row] -= 1
    # Coordinates 3,4 are the two support columns and 5,6 the two
    # complementary columns.  The torus character is target minus source.
    vector[5 + target_column] += 1
    vector[3 + source_column] -= 1
    return tuple(vector)


def witness(label: BlockLabel) -> tuple[int, ...]:
    kind, target_row, source_row, target_column, source_column = label
    if kind != "row":
        raise ValueError("only row-changing labels have the explicit witness")
    vector = [0] * 7
    vector[target_row] += 1
    vector[source_row] -= 1
    vector[5 + target_column] += 1
    vector[3 + source_column] -= 1
    return tuple(vector)


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right, strict=True))


def serial_label(label: BlockLabel) -> list[object]:
    return list(label)


def build_payload() -> dict[str, object]:
    labels = block_labels()
    characters = {label: character(label) for label in labels}
    row_labels = [label for label in labels if label[0] == "row"]
    same_labels = [label for label in labels if label[0] == "same"]

    row_profiles: list[dict[str, object]] = []
    for label in row_labels:
        z = witness(label)
        scores = {other: dot(characters[other], z) for other in labels}
        ordered = sorted(scores.values(), reverse=True)
        require(ordered[0] == 4, (label, ordered[:3]))
        require(ordered[1] <= 3, (label, ordered[:3]))
        winners = [other for other, score in scores.items() if score == ordered[0]]
        require(winners == [label], (label, winners))
        row_profiles.append(
            {
                "label": serial_label(label),
                "character": list(characters[label]),
                "witness": list(z),
                "top_score": ordered[0],
                "second_score": ordered[1],
                "strict_gap": ordered[0] - ordered[1],
            }
        )

    same_profiles: list[dict[str, object]] = []
    for label in same_labels:
        vector = characters[label]
        same_profiles.append(
            {
                "label": serial_label(label),
                "character": list(vector),
                "non_exposure_reason": (
                    "If row potentials are not all equal, an ordered row-changing "
                    "character with the same column difference is larger; if they "
                    "are all equal, that row-changing character ties."
                ),
            }
        )

    require(len(labels) == 28, len(labels))
    require(len(row_labels) == 24, len(row_labels))
    require(len(same_labels) == 4, len(same_labels))
    require(len({characters[label] for label in labels}) == 28, characters)
    return {
        "certificate": "N6-139",
        "status": "EXACT_INTEGER_TORUS_EXPOSED_WEIGHT_FACES",
        "field": "integer character lattice",
        "hypothesis": "full 72-variable graph chart at L=M=A3 tensor P2",
        "character_coordinate_convention": (
            "three row coordinates followed by four column coordinates; each "
            "graph variable has target weight minus source weight"
        ),
        "character_count": len(labels),
        "row_changing_count": len(row_labels),
        "same_row_count": len(same_labels),
        "row_changing_exposed_count": len(row_profiles),
        "same_row_non_exposed_count": len(same_profiles),
        "row_changing_profiles": row_profiles,
        "same_row_profiles": same_profiles,
        "consequence": (
            "All 24 row-changing first-Schur characters are strict exposed faces. "
            "None of the four same-row characters is exposed. Therefore a torus "
            "exposed-face reduction can only isolate the already classified "
            "row-changing directions; it cannot isolate the four average/sign "
            "same-row directions. Those four individual finite germs are already "
            "excluded by N6-125 and N6-127; the remaining issue is mixed-character "
            "sums and their finite-point realization."
        ),
        "boundary": [
            "This is a character-polytope statement, not an integration theorem.",
            "It does not turn a tangent direction into a finite actual Chow pair.",
            "Mixed-character sums and nonlinear same-row lifts remain open.",
            "It does not prove ordinary lower 29 or exact ChowRank(perm_6).",
        ],
    }


def require(condition: bool, detail: object = None) -> None:
    if not condition:
        raise AssertionError(detail)


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
        require(payload == expected, "frozen JSON mismatch")
    if args.json or args.verify_json:
        print("PASS")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
