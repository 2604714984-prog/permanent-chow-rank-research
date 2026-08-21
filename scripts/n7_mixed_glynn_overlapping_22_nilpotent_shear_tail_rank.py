#!/usr/bin/env python3
"""Exact perm7 invalid-tail minors for overlapping (2,2) nilpotent shears."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import os
from pathlib import Path
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_mixed_glynn_two_direction_shear_tail_rank as base  # noqa: E402


TAILS = base.TAILS
SUPPORTS = tuple(itertools.combinations(range(6), 2))
CANDIDATE_COUNT = len(SUPPORTS) * 5


def transformed_coordinate(tail, coordinate, support, ratio, scale):
    first, second = support
    if coordinate not in support:
        return tail[coordinate]
    right_form = scale * (-ratio * tail[first] + tail[second])
    left_coefficient = 1 if coordinate == first else ratio
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(assignment, identity_count, support, ratio, scale):
    feature = []
    for tail in TAILS:
        value = 1
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            value *= (
                tail[coordinate]
                if block < identity_count
                else transformed_coordinate(tail, coordinate, support, ratio, scale)
            )
        feature.append(value)
    return feature


def witness_assignments(identity_count: int, support, ratio=1, scale=1):
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, support, ratio, scale
        )
        base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def exact_determinant(candidate):
    support, identity_count = candidate
    witnesses = witness_assignments(identity_count, support)
    common = {
        "support": list(support),
        "identity_count": identity_count,
        "rank_at_one_one": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return common, witnesses, None
    ratio, scale = sp.symbols("r t")
    matrix = sp.Matrix(
        [
            assignment_feature(assignment, identity_count, support, ratio, scale)
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), ratio, scale, domain=sp.ZZ)
    return common, witnesses, determinant


def trial(candidate):
    common, witnesses, determinant = exact_determinant(candidate)
    if determinant is None:
        return {**common, "status": "RANK_DEFICIENT_AT_ONE_ONE"}
    terms = determinant.terms()
    monomial = len(terms) == 1 and sum(terms[0][0]) > 0 and terms[0][1] != 0
    return {
        **common,
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(terms),
        "determinant_coefficient": str(terms[0][1]) if monomial else None,
        "parameter_exponents": list(terms[0][0]) if monomial else None,
        "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
        "status": "NONZERO_BIVARIATE_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def cover_trial(candidate):
    support, identity_count = candidate
    ratio, scale = sp.symbols("r t")
    gcd_polynomial = None
    minors = []
    witness_sample_sets = []
    for point in ((1, 1), (2, 1), (1, 2), (2, 3), (3, 2)):
        witnesses = witness_assignments(identity_count, support, *point)
        if len(witnesses) != len(TAILS):
            continue
        matrix = sp.Matrix(
            [
                assignment_feature(
                    assignment, identity_count, support, ratio, scale
                )
                for assignment in witnesses
            ]
        ).T
        determinant = sp.Poly(
            matrix.det(method="domain-ge"), ratio, scale, domain=sp.ZZ
        )
        if determinant.is_zero:
            continue
        gcd_polynomial = (
            determinant
            if gcd_polynomial is None
            else sp.gcd(gcd_polynomial, determinant)
        )
        minors.append(
            {
                "selection_point": list(point),
                "determinant_total_degree": determinant.total_degree(),
                "determinant_term_count": len(determinant.terms()),
                "determinant_factorization": str(sp.factor(determinant.as_expr())),
            }
        )
        witness_sample_sets.append(
            {
                "selection_point": list(point),
                "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
            }
        )
        gcd_terms = gcd_polynomial.terms()
        if len(gcd_terms) == 1 and gcd_terms[0][1] != 0:
            break
    gcd_terms = [] if gcd_polynomial is None else gcd_polynomial.terms()
    covered = len(gcd_terms) == 1 and gcd_terms[0][1] != 0
    return {
        "support": list(support),
        "identity_count": identity_count,
        "minor_count": len(minors),
        "minors": minors,
        "gcd_factorization": (
            str(sp.factor(gcd_polynomial.as_expr()))
            if gcd_polynomial is not None
            else None
        ),
        "gcd_exponents": list(gcd_terms[0][0]) if covered else None,
        "witness_sample_sets": witness_sample_sets,
        "status": (
            "DENSE_TORUS_COVERED_BY_EXACT_MINORS"
            if covered
            else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS"
        ),
    }


def factor_probe(candidate):
    common, witnesses, determinant = exact_determinant(candidate)
    if determinant is None:
        return {**common, "status": "RANK_DEFICIENT_AT_ONE_ONE"}
    return {
        **common,
        "determinant": str(determinant.as_expr()),
        "factorization": str(sp.factor(determinant.as_expr())),
        "terms": [
            {"exponents": list(exponents), "coefficient": str(coefficient)}
            for exponents, coefficient in determinant.terms()
        ],
        "witness_assignments": [list(row) for row in witnesses],
        "status": "EXACT_FACTORIZATION_PROBE",
    }


def exceptional_curve_probe(candidate):
    support, identity_count = candidate
    inverse_two = pow(2, base.base.PRIME - 2, base.base.PRIME)
    roots = sp.sqrt_mod(inverse_two, base.base.PRIME, all_roots=True)
    if not roots:
        raise AssertionError("probe prime does not split 2*t^2-1")
    modular_root = int(roots[0])
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, support, 1, modular_root
        )
        base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    witnesses = tuple(pivots[column][1] for column in sorted(pivots))
    if len(witnesses) != len(TAILS):
        return {
            "support": list(support),
            "identity_count": identity_count,
            "rank_mod_prime": len(witnesses),
            "status": "EXCEPTIONAL_CURVE_RANK_DEFICIENT_MOD_PRIME",
        }
    scale = sp.symbols("t")
    matrix = sp.Matrix(
        [
            assignment_feature(assignment, identity_count, support, 1, scale)
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), scale, domain=sp.ZZ)
    relation = sp.Poly(2 * scale**2 - 1, scale, domain=sp.QQ)
    remainder = sp.rem(determinant, relation)
    nonzero_remainder = not remainder.is_zero
    return {
        "support": list(support),
        "identity_count": identity_count,
        "prime": base.base.PRIME,
        "modular_root": modular_root,
        "rank_mod_prime": len(witnesses),
        "new_determinant_degree": determinant.degree(),
        "new_determinant_term_count": len(determinant.terms()),
        "remainder_mod_2t2_minus_1": str(remainder.as_expr()),
        "remainder_nonzero": nonzero_remainder,
        "witness_assignments": [list(row) for row in witnesses],
        "status": (
            "EXACT_FULL_RANK_ON_2T2_MINUS_1"
            if nonzero_remainder
            else "NEW_MINOR_ALSO_VANISHES_ON_2T2_MINUS_1"
        ),
    }


def candidates():
    return [(support, count) for support in SUPPORTS for count in range(1, 6)]


def build_payload(args):
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(cover_trial, candidates(), chunksize=1))
    rows.sort(key=lambda row: (row["support"], row["identity_count"]))
    samples = [
        {
            "support": row["support"],
            "identity_count": row["identity_count"],
            "witness_sample_sets": row["witness_sample_sets"],
        }
        for row in rows[:5]
        if "witness_sample_sets" in row
    ]
    for row in rows:
        row.pop("witness_sample_sets", None)
    status_counts = {}
    for row in rows:
        status = row["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    complete = status_counts == {
        "DENSE_TORUS_COVERED_BY_EXACT_MINORS": CANDIDATE_COUNT
    }
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_OVERLAPPING_22_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_OVERLAPPING_22_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "binom(6,2) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parametrization": "u=(1,r), v=t*(-r,1) on the selected ordered coordinates",
        "nilpotence_identity": "v^T u = 0",
        "workers": args.workers,
        "status_counts": status_counts,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of nonzero rank-one nilpotent updates whose two factor supports coincide on two coordinates.",
            "All 15 coordinate supports and five positive identity/shear multiplicity splits are represented.",
            "On the dense r*t nonzero stratum, the gcd of deterministic exact minors is a coordinate monomial; r=0 is an imported elementary shear and t=0 is the identity control.",
            "The result does not cover larger overlapping supports, non-unipotent rank-one updates, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--factor-probe-index", type=int)
    parser.add_argument("--exception-probe-index", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    probe_modes = sum(
        value is not None
        for value in (
            args.probe_index,
            args.factor_probe_index,
            args.exception_probe_index,
        )
    )
    if probe_modes > 1:
        raise ValueError("choose at most one probe mode")
    if args.exception_probe_index is not None:
        if not 0 <= args.exception_probe_index < CANDIDATE_COUNT:
            raise ValueError("--exception-probe-index is outside the candidate family")
        payload = exceptional_curve_probe(candidates()[args.exception_probe_index])
    elif args.factor_probe_index is not None:
        if not 0 <= args.factor_probe_index < CANDIDATE_COUNT:
            raise ValueError("--factor-probe-index is outside the candidate family")
        payload = factor_probe(candidates()[args.factor_probe_index])
    elif args.probe_index is None:
        payload = build_payload(args)
    else:
        if not 0 <= args.probe_index < CANDIDATE_COUNT:
            raise ValueError("--probe-index is outside the candidate family")
        payload = trial(candidates()[args.probe_index])
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
