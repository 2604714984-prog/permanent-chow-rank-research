#!/usr/bin/env python3
"""Finite SMT probe for protected Walsh characters with >=3 permutation types."""

from __future__ import annotations

import argparse
import itertools
import json
import re
import subprocess
import time
from pathlib import Path


ZERO3 = "#b000"
ZERO6 = "#b000000"


def xor_all(terms: list[str]) -> str:
    result = terms[0]
    for term in terms[1:]:
        result = f"(bvxor {result} {term})"
    return result


def permutation_value(row: int, column: int) -> str:
    if row == 0:
        return f"#b{column - 1:03b}"
    return f"p{row}_{column}"


def basis_label(value: str) -> str:
    result = "#b100000"
    for index in range(4, -1, -1):
        result = f"(ite (= {value} #b{index:03b}) #b{1 << index:06b} {result})"
    return result


def label_name(row: int, column: int) -> str:
    return f"l{row}_{column}"


def selected_label(row: int, selector: str) -> str:
    result = ZERO6
    for column in range(6, 0, -1):
        label = label_name(row, column)
        result = f"(ite (= {selector} #b{column:03b}) {label} {result})"
    return result


def rows_equal(first: int, second: int) -> str:
    equalities = [
        f"(= {permutation_value(first, column)} {permutation_value(second, column)})"
        for column in range(1, 7)
    ]
    return f"(and {' '.join(equalities)})"


def build_formula(case: str, collision_scope: str = "all_quantified") -> str:
    if case == "nonzero_columns":
        valid_columns = (1, 2, 3, 4, 5, 6)
    elif case == "zero_column":
        valid_columns = (0, 1, 2, 3, 4, 5)
    else:
        raise ValueError(case)

    logic = "BV" if collision_scope == "all_quantified" else "QF_BV"
    lines = [f"(set-logic {logic})", "(set-option :produce-models true)"]
    for row in range(1, 6):
        names = []
        for column in range(1, 7):
            name = permutation_value(row, column)
            names.append(name)
            lines.append(f"(declare-fun {name} () (_ BitVec 3))")
            lines.append(f"(assert (bvule {name} #b101))")
        lines.append(f"(assert (distinct {' '.join(names)}))")
    for row in range(6):
        for column in range(1, 7):
            lines.append(
                f"(define-fun {label_name(row, column)} () (_ BitVec 6) "
                f"{basis_label(permutation_value(row, column))})"
            )

    distinct_triples = []
    for first, second, third in itertools.combinations(range(6), 3):
        distinct_triples.append(
            "(and "
            f"(not {rows_equal(first, second)}) "
            f"(not {rows_equal(first, third)}) "
            f"(not {rows_equal(second, third)}))"
        )
    lines.append(f"(assert (or {' '.join(distinct_triples)}))")

    valid_labels = [
        ZERO6 if column == 0 else label_name(row, column)
        for row, column in enumerate(valid_columns)
    ]
    lines.append(f"(define-fun target () (_ BitVec 6) {xor_all(valid_labels)})")

    if collision_scope == "all_quantified":
        selectors = [f"d{row}" for row in range(6)]
        declarations = " ".join(f"({name} (_ BitVec 3))" for name in selectors)
        in_range = " ".join(f"(bvule {name} #b110)" for name in selectors)
        repetitions = " ".join(
            f"(= {selectors[first]} {selectors[second]})"
            for first, second in itertools.combinations(range(6), 2)
        )
        collision = xor_all(
            [selected_label(row, selector) for row, selector in enumerate(selectors)]
        )
        lines.append(
            f"(assert (forall ({declarations}) "
            f"(=> (and {in_range} (or {repetitions})) (not (= {collision} target)))))"
        )
    elif collision_scope in (
        "valid_pair_changes",
        "single_pair_all",
        "all_explicit",
    ):
        assignments = set()
        if collision_scope == "valid_pair_changes":
            for first, second in itertools.combinations(range(6), 2):
                for repeated_column in range(7):
                    columns = list(valid_columns)
                    columns[first] = repeated_column
                    columns[second] = repeated_column
                    assignments.add(tuple(columns))
        elif collision_scope == "single_pair_all":
            assignments.update(
                columns
                for columns in itertools.product(range(7), repeat=6)
                if len(set(columns)) == 5
            )
        else:
            assignments.update(
                columns
                for columns in itertools.product(range(7), repeat=6)
                if len(set(columns)) < 6
            )
        for columns in sorted(assignments):
            labels = [
                ZERO6 if column == 0 else label_name(row, column)
                for row, column in enumerate(columns)
            ]
            lines.append(f"(assert (not (= {xor_all(labels)} target)))")
    else:
        raise ValueError(collision_scope)
    lines.append("(check-sat)")
    return "\n".join(lines) + "\n"


def solve_case(
    case: str, collision_scope: str, timeout_seconds: int, memory_mib: int
) -> dict[str, object]:
    formula = build_formula(case, collision_scope)
    started = time.perf_counter()
    process = subprocess.run(
        ["z3", "-in", f"-T:{timeout_seconds}", f"-memory:{memory_mib}"],
        input=formula,
        text=True,
        capture_output=True,
        timeout=timeout_seconds + 10,
        check=False,
    )
    output = process.stdout.strip().splitlines()
    answer = output[0] if output else "no-output"
    model_stdout = process.stdout
    model_exit_code = process.returncode
    model_stderr = process.stderr
    if answer == "sat":
        model_names = [
            permutation_value(row, column)
            for row in range(1, 6)
            for column in range(1, 7)
        ]
        model_formula = formula + f"(get-value ({' '.join(model_names)}))\n"
        model_process = subprocess.run(
            ["z3", "-in", f"-T:{timeout_seconds}", f"-memory:{memory_mib}"],
            input=model_formula,
            text=True,
            capture_output=True,
            timeout=timeout_seconds + 10,
            check=False,
        )
        model_stdout = model_process.stdout
        model_exit_code = model_process.returncode
        model_stderr = model_process.stderr
        output = model_stdout.strip().splitlines()
    row = {
        "case": case,
        "collision_scope": collision_scope,
        "answer": answer,
        "exit_code": model_exit_code,
        "elapsed_seconds": time.perf_counter() - started,
        "stdout_tail": output[-20:],
        "stderr_tail": model_stderr.strip().splitlines()[-20:],
        "formula_utf8_bytes": len(formula.encode("utf-8")),
        "invalid_assignment_count": (
            7**6 - math_permutations(7, 6)
            if collision_scope in ("all_quantified", "all_explicit")
            else 37_800
            if collision_scope == "single_pair_all"
            else None
        ),
    }
    if answer == "sat":
        values = {
            (int(match.group(1)), int(match.group(2))): int(match.group(3), 2)
            for match in re.finditer(
                r"\(p([1-5])_([1-6])\s+#b([01]{3})\)", model_stdout
            )
        }
        if len(values) == 30:
            permutations = [tuple(range(6))]
            permutations.extend(
                tuple(values[(model_row, column)] for column in range(1, 7))
                for model_row in range(1, 6)
            )
            valid_columns = (
                (1, 2, 3, 4, 5, 6)
                if case == "nonzero_columns"
                else (0, 1, 2, 3, 4, 5)
            )

            def label(model_row: int, column: int) -> int:
                return 0 if column == 0 else 1 << permutations[model_row][column - 1]

            target = 0
            for model_row, column in enumerate(valid_columns):
                target ^= label(model_row, column)
            witness = next(
                (
                    columns
                    for columns in itertools.product(range(7), repeat=6)
                    if len(set(columns)) < 6
                    and target
                    == xor_integers(
                        [label(model_row, column) for model_row, column in enumerate(columns)]
                    )
                ),
                None,
            )
            row.update(
                {
                    "model_permutations": permutations,
                    "model_distinct_type_count": len(set(permutations)),
                    "model_valid_columns": valid_columns,
                    "model_target_character": target,
                    "full_invalid_collision_witness": witness,
                }
            )
    return row


def xor_integers(values: list[int]) -> int:
    result = 0
    for value in values:
        result ^= value
    return result


def math_permutations(total: int, chosen: int) -> int:
    result = 1
    for value in range(total - chosen + 1, total + 1):
        result *= value
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case", choices=("nonzero_columns", "zero_column", "both"), default="both"
    )
    parser.add_argument("--timeout-seconds", type=int, default=120)
    parser.add_argument("--memory-mib", type=int, default=8192)
    parser.add_argument(
        "--collision-scope",
        choices=(
            "all_quantified",
            "all_explicit",
            "valid_pair_changes",
            "single_pair_all",
        ),
        default="all_quantified",
    )
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    cases = (
        ("nonzero_columns", "zero_column") if args.case == "both" else (args.case,)
    )
    rows = [
        solve_case(case, args.collision_scope, args.timeout_seconds, args.memory_mib)
        for case in cases
    ]
    answers = [row["answer"] for row in rows]
    payload = {
        "schema_version": 1,
        "status": (
            "EXACT_UNSAT_PROTECTED_CHARACTER_AT_LEAST_THREE_TYPES"
            if answers == ["unsat"] * len(cases)
            and args.collision_scope in ("all_quantified", "all_explicit")
            else "EXACT_UNSAT_PAIR_COLLISION_AT_LEAST_THREE_TYPES"
            if answers == ["unsat"] * len(cases)
            else "DIAGNOSTIC_PROTECTED_CHARACTER_SMT"
        ),
        "solver": "z3",
        "collision_scope": args.collision_scope,
        "cases": rows,
        "claim_boundary": [
            "The two cases normalize a chosen valid distinct-column realization according to whether it uses column zero.",
            "UNSAT in both cases would exclude protected characters for every packet with at least three permutation types.",
            "SAT is a counterexample to that proposed character statement; UNKNOWN or timeout proves nothing.",
            "This character statement alone does not cover general GL(6) graph transforms or border rank.",
        ],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
