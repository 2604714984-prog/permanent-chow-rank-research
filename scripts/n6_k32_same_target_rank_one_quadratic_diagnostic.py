"""Exact quadratic diagnostic for the remaining same-target rank-one support."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_k32_rank_one_support_germs import (
        cross_matrix,
        kernel_operator,
        quadratic_initial_generators,
        require,
        schur_jacobian,
    )
except ModuleNotFoundError:  # Direct script execution.
    from n6_k32_rank_one_support_germs import (
        cross_matrix,
        kernel_operator,
        quadratic_initial_generators,
        require,
        schur_jacobian,
    )


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_same_target_rank_one_quadratic_diagnostic.json"


def support_operator() -> sp.Matrix:
    operator = sp.zeros(6)
    operator[0, 2] = 1
    operator[0, 3] = 1
    return operator


def branch_substitutions(
    variables: tuple[sp.Symbol, ...],
) -> list[tuple[list[str], dict[sp.Symbol, int | sp.Symbol]]]:
    x0, x1, x2, x3, x4, x5, x6, x7 = variables
    return [
        (["x4", "x3", "x1", "x5"], {x4: 0, x3: 0, x1: 0, x5: 0}),
        (["x4", "x3", "x6", "x7"], {x4: 0, x3: 0, x6: 0, x7: 0}),
        (
            ["x4", "x0-x2", "x1", "x5", "x6", "x7"],
            {x4: 0, x0: x2, x1: 0, x5: 0, x6: 0, x7: 0},
        ),
    ]


def build_payload() -> dict[str, object]:
    operator = support_operator()
    jacobian, derivatives, pivot_info = schur_jacobian(operator)
    kernel = jacobian.nullspace()
    require(jacobian.rank() == 64, jacobian.rank())
    require(len(kernel) == 8, len(kernel))
    generators, variables, quadratic = quadratic_initial_generators(
        operator, jacobian, derivatives, pivot_info, kernel
    )
    expected = {
        sp.expand(variables[3] * (variables[0] - variables[2])),
        sp.expand(variables[4] * (variables[0] - variables[2])),
        sp.expand(variables[1] * variables[3]),
        sp.expand(variables[1] * variables[4]),
        sp.expand(variables[1] * variables[6]),
        sp.expand(variables[1] * variables[7]),
        sp.expand(variables[3] * variables[4]),
        sp.expand(variables[3] * variables[5]),
        sp.expand(variables[3] * variables[6]),
        sp.expand(variables[3] * variables[7]),
        sp.expand(variables[4] ** 2),
        sp.expand(variables[4] * variables[5]),
        sp.expand(variables[4] * variables[6]),
        sp.expand(variables[4] * variables[7]),
        sp.expand(variables[5] * variables[6]),
        sp.expand(variables[5] * variables[7]),
    }
    require({sp.expand(item) for item in generators} == expected, generators)
    operator_family = operator + sum(
        (variables[index] * kernel_operator(vector) for index, vector in enumerate(kernel)),
        sp.zeros(6),
    )
    branches: list[dict[str, object]] = []
    for equations, substitution in branch_substitutions(variables):
        branch_operator = operator_family.subs(substitution)
        cross_rank = int(cross_matrix(branch_operator).rank())
        operator_rank = int(branch_operator.rank())
        branches.append(
            {
                "equations": equations,
                "generic_cross_rank": cross_rank,
                "generic_operator_rank": operator_rank,
                "generic_sum_rank": 6 + operator_rank,
                "generic_cross_rank_at_most_six": cross_rank <= 6,
            }
        )
    require(
        [branch["generic_cross_rank"] for branch in branches] == [6, 6, 6],
        branches,
    )
    require(
        [branch["generic_sum_rank"] for branch in branches] == [7, 8, 7],
        branches,
    )
    return {
        "certificate": "N6-138",
        "status": "EXACT_QQ_SAME_TARGET_RANK_ONE_QUADRATIC_DIAGNOSTIC",
        "field": "characteristic zero",
        "hypothesis": (
            "finite K3,2 graph pair L=graph(D), M=graph(-D) with D supported "
            "on one target row and two source columns"
        ),
        "base_cross_rank": int(cross_matrix(operator).rank()),
        "jacobian_shape": list(jacobian.shape),
        "jacobian_rank": int(jacobian.rank()),
        "kernel_dimension": len(kernel),
        "quadratic_generator_count": len(generators),
        "quadratic_initial_generators": [str(item) for item in generators],
        "quadratic_coefficient_rank": int(quadratic.rank()),
        "quadratic_support_components": len(branches),
        "branches": branches,
        "generic_integrated_straight_branch_count": sum(
            branch["generic_cross_rank_at_most_six"] for branch in branches
        ),
        "consequence": (
            "The radical of the quadratic support has three linear components. "
            "All three are generic straight rank-at-most-six families, but "
            "their operator ranks are one, two, and one, so their sums have "
            "ranks seven, eight, and seven and none is complementary."
        ),
        "boundary": [
            "does not prove that higher-order nonlinear lifts outside this quadratic support have no solutions",
            "does not give a full completed-germ sandwich",
            "does not cover non-graph charts or coupled six-term cocycles",
            "does not close the full K3,2 or K2,3 normal cone",
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
    print("certificate=N6-138")
    print("jacobian_rank=64")
    print("quadratic_components=3")
    print("integrated_straight_components=3")
    print("status=PASS")


if __name__ == "__main__":
    main()
