#!/usr/bin/env python3
"""Exact replay for the small-excess compressed-center theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any, Iterator

Matrix = list[list[Fraction]]


def require(ok: bool, message: object) -> None:
    if not ok:
        raise RuntimeError(message)


def eye(n: int) -> Matrix:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def zero(rows: int, cols: int) -> Matrix:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def trans(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a, strict=True)] if a else []


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(ar, br, strict=True)] for ar, br in zip(a, b, strict=True)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(ar, br, strict=True)] for ar, br in zip(a, b, strict=True)]


def mul(a: Matrix, b: Matrix) -> Matrix:
    require(a and b and len(a[0]) == len(b), (len(a), len(b)))
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rank(a: Matrix) -> int:
    if not a:
        return 0
    w = [[Fraction(x) for x in row] for row in a]
    rows, cols, pivot = len(w), len(w[0]), 0
    for col in range(cols):
        chosen = next((r for r in range(pivot, rows) if w[r][col]), None)
        if chosen is None:
            continue
        w[pivot], w[chosen] = w[chosen], w[pivot]
        scale = w[pivot][col]
        w[pivot] = [x / scale for x in w[pivot]]
        for r in range(rows):
            if r != pivot and w[r][col]:
                factor = w[r][col]
                w[r] = [x - factor * y for x, y in zip(w[r], w[pivot], strict=True)]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def shear(n: int, i: int, j: int, value: int) -> Matrix:
    out = eye(n)
    out[i][j] = Fraction(value)
    return out


def unimodular_pair(n: int, seed: int) -> tuple[Matrix, Matrix]:
    matrix, inverse = eye(n), eye(n)
    for step in range(2 * n + seed % 2):
        i = (2 * step + 1 + seed) % n
        j = (3 * step + 2 + 2 * seed) % n
        if i == j:
            j = (j + 1) % n
        value = (step + seed) % 3 + 1
        if (step + seed) % 2:
            value = -value
        matrix = mul(shear(n, i, j, value), matrix)
        inverse = mul(inverse, shear(n, i, j, -value))
    require(mul(inverse, matrix) == eye(n), (n, seed))
    return matrix, inverse


def projection(n: int, start: int, size: int) -> Matrix:
    out = zero(n, n)
    for i in range(start, start + size):
        out[i][i] = 1
    return out


def block_hessian(blocks: tuple[int, ...]) -> Matrix:
    out, offset = zero(sum(blocks), sum(blocks)), 0
    for block, size in enumerate(blocks):
        for i in range(size):
            for j in range(size):
                out[offset + i][offset + j] = Fraction(
                    (i + 1) * (j + 1) + (block + 1) * (i + j + 1) + (3 if i == j else 0)
                )
        offset += size
    return out


def compositions(total: int, count: int) -> Iterator[tuple[int, ...]]:
    if count == 1:
        yield (total,)
        return
    for first in range(1, total - count + 2):
        for tail in compositions(total - first, count - 1):
            yield (first, *tail)


def core_hash(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def audit_case(total: int, kernel: int, blocks: tuple[int, ...]) -> dict[str, Any]:
    essential = total - kernel
    require(essential >= 2 and sum(blocks) == total, (total, kernel, blocks))
    seed = total + 7 * kernel + sum((i + 1) * b for i, b in enumerate(blocks))
    mixing, inverse = unimodular_pair(total, seed)
    bmat = [row[:essential] for row in mixing]
    cmat = [row[:] for row in inverse[:essential]]
    require(mul(cmat, bmat) == eye(essential), "CB")
    qmat = mul(bmat, cmat)
    qminus = sub(qmat, eye(total))
    require(rank(qminus) == kernel, "Q-I")

    projections, operators, offset = [], [], 0
    for size in blocks:
        pmat = projection(total, offset, size)
        projections.append(pmat)
        operators.append(mul(mul(cmat, pmat), bmat))
        offset += size
    total_operator = zero(essential, essential)
    for operator in operators:
        total_operator = add(total_operator, operator)
    require(total_operator == eye(essential), "sum")

    lifted = block_hessian(blocks)
    hessian = mul(mul(trans(bmat), lifted), bmat)
    ranks, idem, centers, crosses = [], [], [], []
    for i, operator in enumerate(operators):
        operator_rank = rank(operator)
        ranks.append(operator_rank)
        require(operator_rank <= blocks[i], "operator rank")

        defect = sub(mul(operator, operator), operator)
        idem.append(rank(defect))
        factored = mul(mul(mul(mul(cmat, projections[i]), qminus), projections[i]), bmat)
        require(defect == factored and idem[-1] <= kernel, "idempotence")

        center = sub(mul(hessian, operator), mul(trans(operator), hessian))
        centers.append(rank(center))
        center_factor = mul(
            mul(
                trans(bmat),
                sub(
                    mul(mul(lifted, qminus), projections[i]),
                    mul(mul(projections[i], trans(qminus)), lifted),
                ),
            ),
            bmat,
        )
        require(center == center_factor and centers[-1] <= 2 * kernel, "center")

    for i, j in combinations(range(len(operators)), 2):
        for left, right in ((i, j), (j, i)):
            product = mul(operators[left], operators[right])
            crosses.append(rank(product))
            factored = mul(mul(mul(mul(cmat, projections[left]), qminus), projections[right]), bmat)
            require(product == factored and crosses[-1] <= kernel, "cross")

    rank_excess = sum(ranks) - essential
    require(0 <= rank_excess <= kernel, "rank budget")
    for operator, operator_rank, defect_rank in zip(operators, ranks, idem, strict=True):
        one = essential - rank(sub(operator, eye(essential)))
        zero_dim = essential - operator_rank
        require(one == operator_rank - defect_rank, "one eigenspace")
        require(one + zero_dim >= essential - kernel, "large eigenspaces")

    return {
        "total_dimension": total,
        "essential_dimension": essential,
        "kernel_dimension": kernel,
        "block_sizes": list(blocks),
        "operator_ranks": ranks,
        "idempotence_defects": idem,
        "maximum_cross_defect": max(crosses, default=0),
        "center_defects": centers,
        "rank_excess": rank_excess,
        "eigenspace_checks": len(operators),
    }


def near_endpoint_rows() -> list[dict[str, int]]:
    rows = []
    for n in range(3, 129):
        for m in range(3, n + 1):
            q0 = max(2, (m * m + n - 1) // n)
            for q in range(q0, (m * m + 8) // n + 2):
                s = q * n - m * m
                if 0 <= s <= 8 and s < n:
                    rows.append({
                        "n": n,
                        "m": m,
                        "q": q,
                        "excess": s,
                        "one_eigenspace_floor": max(0, n - s - s // q),
                        "zero_eigenspace_floor": max(0, (q - 1) * n - s),
                        "mixed_hessian_rank_cap": 2 * s,
                        "missing_dimension_cap": s,
                    })
    return rows


def build_payload() -> dict[str, Any]:
    cases = operators = cross_checks = eigenspaces = 0
    maxima = {"idempotence": 0, "cross": 0, "center": 0, "rank_excess": 0}
    sharp: dict[str, dict[str, Any]] = {}
    for total in range(4, 9):
        for count in range(2, min(3, total) + 1):
            for blocks in compositions(total, count):
                for kernel in range(0, min(2, total - 2) + 1):
                    row = audit_case(total, kernel, blocks)
                    cases += 1
                    operators += count
                    cross_checks += count * (count - 1)
                    eigenspaces += count
                    values = {
                        "idempotence": max(row["idempotence_defects"], default=0),
                        "cross": row["maximum_cross_defect"],
                        "center": max(row["center_defects"], default=0),
                        "rank_excess": row["rank_excess"],
                    }
                    for key, value in values.items():
                        maxima[key] = max(maxima[key], value)
                    conditions = {
                        "idempotence_equals_k": values["idempotence"] == kernel,
                        "cross_equals_k": values["cross"] == kernel,
                        "center_equals_2k": values["center"] == 2 * kernel,
                        "rank_excess_equals_k": values["rank_excess"] == kernel,
                    }
                    for label, ok in conditions.items():
                        if kernel and ok and label not in sharp:
                            sharp[label] = row

    require((cases, operators, cross_checks, eigenspaces) == (240, 645, 1_140, 645), "counts")
    require(len(sharp) == 4, sharp)
    frontier = near_endpoint_rows()
    first_excess = [row for row in frontier if row["excess"] == 1]
    require(len(frontier) == 908 and len(first_excess) == 48, "frontier")

    core = {
        "status": [
            "GENERAL_SMALL_EXCESS_COMPRESSED_CENTER_FRAME",
            "LOW_RANK_CENTER_DEFECT",
            "NEAR_SEBASTIANI_THOM_HESSIAN_BOTTLENECK",
            "EXACT_RATIONAL_REPLAYED",
        ],
        "theorem": {
            "defect_ledger": "If q*n=m^2+s and f is a nonzero permanent-relative Chow block intersection, then factor deficit + span-overlap defect + unused-span defect + permanent-shadow excess = s.",
            "compressed_frame": "There are A_i in End(U) with sum A_i=I, rank A_i<=dim L_i, rank(A_i^2-A_i)<=k, rank(A_i A_j)<=k, and rank(H_f A_i-A_i^T H_f)<=2k, where k<=s.",
            "rank_budget": "0<=sum_i rank(A_i)-dim(U)<=k.",
            "hessian_bottleneck": "Some A_i has exact zero/one eigenspaces Z,P with codim (Z direct_sum P)<=s and mixed Hessian rank at most 2s; dim P>=n-s-floor(s/q), dim Z>=(q-1)n-s.",
            "endpoint_recovery": "At s=0 the A_i are exact orthogonal idempotents in the Hessian center, recovering the closed multi-term endpoint.",
            "first_excess": "At s=1, any surviving intersection forces a codimension-one split with mixed Hessian rank at most two.",
        },
        "claim_boundary": "This theorem is a necessary Chow-realizability interface. It does not yet exclude the small-excess regime, improve a finite-n Chow-rank lower bound, control border rank, or prove a uniform lower bound for mixed permanent Hessian cuts. The finite replay checks the exact linear-algebra identities and arithmetic only; the general theorem is the written proof. Literature novelty is not established.",
    }
    replay = {
        "matrix_cases": cases,
        "operator_checks": operators,
        "ordered_cross_checks": cross_checks,
        "eigenspace_checks": eigenspaces,
        "near_endpoint_rows": len(frontier),
        "first_excess_rows": len(first_excess),
        "maximum_observed_idempotence_defect": maxima["idempotence"],
        "maximum_observed_cross_defect": maxima["cross"],
        "maximum_observed_center_defect": maxima["center"],
        "maximum_observed_rank_excess": maxima["rank_excess"],
        "sharp_examples": sharp,
        "first_near_endpoint_rows": frontier[:24],
    }
    return {**core, "exact_replay": replay, "core_sha256": core_hash(core)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_SMALL_EXCESS_COMPRESSED_CENTER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
