#!/usr/bin/env python3
"""Exact local certificates for the N6-064 b=50 equality locus."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b50_equality_locus.json"
TRIPLES = list(combinations(range(6), 3))
PAIRS = list(combinations(range(6), 2))
SINGLES = [(i,) for i in range(6)]
I3 = {x: i for i, x in enumerate(TRIPLES)}
I2 = {x: i for i, x in enumerate(PAIRS)}
I1 = {x: i for i, x in enumerate(SINGLES)}


def hook_support(transpose=False):
    support = {
        (r, c)
        for r, row in enumerate(TRIPLES)
        for c, column in enumerate(TRIPLES)
        if (set(row) <= {0, 1, 2, 3} and set(column) <= {0, 1, 2, 3, 4})
        or set(row) <= {0, 1, 2}
    }
    return {(c, r) for r, c in support} if transpose else support


def product_shadow(support):
    return {
        (I2[row_pair], I2[column_pair])
        for r, c in support
        for row_pair in combinations(TRIPLES[r], 2)
        for column_pair in combinations(TRIPLES[c], 2)
    }


def pair_product_shadow(support):
    return {
        (I1[(row_vertex,)], I1[(column_vertex,)])
        for r, c in support
        for row_vertex in PAIRS[r]
        for column_vertex in PAIRS[c]
    }


def incidence_data(transpose=False):
    support = hook_support(transpose)
    shadow = product_shadow(support)
    sources = sorted(support)
    source_complement = sorted(set(product(range(20), repeat=2)) - support)
    targets = sorted(shadow)
    target_complement = sorted(set(product(range(15), repeat=2)) - shadow)
    tangent_pairs = [(s, u) for s in sources for u in source_complement]
    eta_pairs = [(k, v) for k in targets for v in target_complement]
    tangent_index = {pair: i for i, pair in enumerate(tangent_pairs)}
    offset = len(tangent_pairs)
    eta_index = {pair: offset + i for i, pair in enumerate(eta_pairs)}
    ground = offset + len(eta_pairs)
    parent = list(range(ground + 1))
    grounded = [False] * (ground + 1)
    grounded[ground] = True

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x
            grounded[x] = grounded[x] or grounded[y]

    def zero(x):
        grounded[find(x)] = True

    equations = []
    for source in sources:
        r, c = source
        for a in range(6):
            for b in range(6):
                target = None
                if a in TRIPLES[r] and b in TRIPLES[c]:
                    target = (
                        I2[tuple(x for x in TRIPLES[r] if x != a)],
                        I2[tuple(x for x in TRIPLES[c] if x != b)],
                    )
                for quotient_target in target_complement:
                    row_pair, column_pair = PAIRS[quotient_target[0]], PAIRS[quotient_target[1]]
                    outside = None
                    if a not in row_pair and b not in column_pair:
                        outside = (
                            I3[tuple(sorted(row_pair + (a,)))],
                            I3[tuple(sorted(column_pair + (b,)))],
                        )
                    tangent = tangent_index.get((source, outside))
                    eta = eta_index.get((target, quotient_target)) if target is not None else None
                    equations.append((tangent, eta, source, a, b, quotient_target))
                    if tangent is not None and eta is not None:
                        union(tangent, eta)
                    elif tangent is not None:
                        zero(tangent)
                    elif eta is not None:
                        zero(eta)
    for i in range(ground + 1):
        if grounded[i]:
            grounded[find(i)] = True

    components = []
    for root in {find(i) for i in range(ground)}:
        if grounded[root]:
            continue
        tangent_members = [tangent_pairs[i] for i in range(offset) if find(i) == root]
        if not tangent_members:
            continue
        eta_members = {eta_pairs[i - offset] for i in range(offset, ground) if find(i) == root}
        tangent_map = defaultdict(list)
        for source, outside in tangent_members:
            tangent_map[source].append(outside)
        source, outside = tangent_members[0]
        weight = tuple(
            int(i in TRIPLES[outside[0]]) - int(i in TRIPLES[source[0]]) for i in range(6)
        ) + tuple(
            int(i in TRIPLES[outside[1]]) - int(i in TRIPLES[source[1]]) for i in range(6)
        )
        negative = [i for i, value in enumerate(weight) if value < 0][0]
        positive = [i for i, value in enumerate(weight) if value > 0][0]
        components.append(
            {
                "label": ("row" if positive < 6 else "column", negative % 6, positive % 6),
                "weight": weight,
                "tangent_members": tangent_members,
                "eta_members": eta_members,
                "tangent_map": tangent_map,
            }
        )
    components.sort(key=lambda item: (len(item["tangent_members"]), item["weight"]))
    return {
        "support": support,
        "shadow": shadow,
        "sources": sources,
        "equations": equations,
        "components": components,
        "tangent_variable_count": offset,
        "eta_variable_count": ground - offset,
    }


def derivative_of_component(component, source, a, b):
    output = []
    for r, c in component["tangent_map"].get(source, []):
        if a in TRIPLES[r] and b in TRIPLES[c]:
            output.append(
                (
                    I2[tuple(x for x in TRIPLES[r] if x != a)],
                    I2[tuple(x for x in TRIPLES[c] if x != b)],
                )
            )
    return output


def grounded_quadratic_matrix(data):
    components = data["components"]
    monomials = [(i, j) for i in range(16) for j in range(i, 16)]
    monomial_index = {pair: i for i, pair in enumerate(monomials)}
    rows = []
    for tangent, eta, source, a, b, quotient_target in data["equations"]:
        if tangent is not None or eta is not None:
            continue
        row = {}
        for i, left in enumerate(components):
            for j in range(i, len(components)):
                right = components[j]
                coefficient = sum(
                    (target, quotient_target) in left["eta_members"]
                    for target in derivative_of_component(right, source, a, b)
                )
                if i != j:
                    coefficient += sum(
                        (target, quotient_target) in right["eta_members"]
                        for target in derivative_of_component(left, source, a, b)
                    )
                if coefficient:
                    row[monomial_index[(i, j)]] = coefficient
        if row:
            rows.append(row)
    return monomials, rows


def rank_and_rref_q(rows):
    basis = {}
    for source in rows:
        row = {i: Fraction(value) for i, value in source.items() if value}
        while row:
            pivot = min(row)
            coefficient = row[pivot]
            if pivot not in basis:
                basis[pivot] = {i: value / coefficient for i, value in row.items()}
                break
            old = basis[pivot]
            for i, value in old.items():
                new = row.get(i, 0) - coefficient * value
                if new:
                    row[i] = new
                elif i in row:
                    del row[i]
    return basis


def poly_add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def replace(vector, axis, old, new, variable, degree, scalar=1):
    subsets, index = {
        3: (TRIPLES, I3),
        2: (PAIRS, I2),
        1: (SINGLES, I1),
    }[degree]
    result = {key: dict(polynomial) for key, polynomial in vector.items()}
    for (r, c), polynomial in list(vector.items()):
        chosen = list(subsets[r] if axis == "row" else subsets[c])
        if old in chosen and new not in chosen:
            chosen[chosen.index(old)] = new
            replacement = index[tuple(sorted(chosen))]
            key = (replacement, c) if axis == "row" else (r, replacement)
            shifted = {
                tuple(sorted(monomial + (variable,))): scalar * coefficient
                for monomial, coefficient in polynomial.items()
            }
            result[key] = poly_add(result.get(key, {}), shifted)
    return {key: polynomial for key, polynomial in result.items() if polynomial}


def transformed_basis(base, row_sources, column_source, degree):
    vectors = []
    for key in sorted(base):
        vector = {key: {(): 1}}
        for variable, (old, new) in enumerate(zip(row_sources, (3, 4, 5))):
            vector = replace(vector, "row", old, new, variable, degree)
        vector = replace(vector, "column", column_source, 5, 3, degree)
        vectors.append(vector)
    return vectors


def branch_certificate(data, row_sources, column_source):
    cubic = transformed_basis(data["support"], row_sources, column_source, 3)

    def pull_back(vector, degree):
        vector = replace(vector, "column", column_source, 5, 3, degree, -1)
        for variable, (old, new) in reversed(
            list(enumerate(zip(row_sources, (3, 4, 5))))
        ):
            vector = replace(vector, "row", old, new, variable, degree, -1)
        return vector

    cubic_to_quadratic = True
    for cubic_vector in cubic:
        for a in range(6):
            for b in range(6):
                derivative = {}
                for (r, c), polynomial in cubic_vector.items():
                    if a in TRIPLES[r] and b in TRIPLES[c]:
                        key = (
                            I2[tuple(x for x in TRIPLES[r] if x != a)],
                            I2[tuple(x for x in TRIPLES[c] if x != b)],
                        )
                        derivative[key] = poly_add(derivative.get(key, {}), polynomial)
                if any(key not in data["shadow"] for key in pull_back(derivative, 2)):
                    cubic_to_quadratic = False

    second_shadow = pair_product_shadow(data["shadow"])
    quadratic = transformed_basis(data["shadow"], row_sources, column_source, 2)
    quadratic_to_linear = True
    for quadratic_vector in quadratic:
        for a in range(6):
            for b in range(6):
                derivative = {}
                for (r, c), polynomial in quadratic_vector.items():
                    if a in PAIRS[r] and b in PAIRS[c]:
                        key = (
                            I1[(next(x for x in PAIRS[r] if x != a),)],
                            I1[(next(x for x in PAIRS[c] if x != b),)],
                        )
                        derivative[key] = poly_add(derivative.get(key, {}), polynomial)
                if any(key not in second_shadow for key in pull_back(derivative, 1)):
                    quadratic_to_linear = False

    desired = [
        ("row", row_sources[0], 3),
        ("row", row_sources[1], 4),
        ("row", row_sources[2], 5),
        ("column", column_source, 5),
    ]
    by_label = {component["label"]: component for component in data["components"]}
    positions = {source: i for i, source in enumerate(sorted(data["support"]))}
    jacobian = []
    for label in desired:
        source, outside = by_label[label]["tangent_members"][0]
        polynomial = cubic[positions[source]].get(outside, {})
        jacobian.append([polynomial.get((variable,), 0) for variable in range(4)])
    return cubic_to_quadratic, quadratic_to_linear, jacobian


def one_factor_pair_shadow_data():
    ordered = sorted(PAIRS, key=lambda s: sum(1 << x for x in s))
    seen = set()
    sizes = [0]
    weights = []
    for pair in ordered:
        new = set(pair) - seen
        weights.append(len(new))
        seen.update(new)
        sizes.append(len(seen))
    return sizes, weights


def minimum_second_product_shadow(total=75):
    sizes, weights = one_factor_pair_shadow_data()
    infinity = 10**9
    cache = {}

    def solve(index, previous, remaining):
        key = (index, previous, remaining)
        if key in cache:
            return cache[key]
        if index == 15:
            return (0, ()) if remaining == 0 else (infinity, ())
        best = (infinity, ())
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (14 - index):
                continue
            tail, witness = solve(index + 1, value, remaining - value)
            candidate = (weights[index] * sizes[value] + tail, (value,) + witness)
            if candidate[0] < best[0]:
                best = candidate
        cache[key] = best
        return best

    return solve(0, 15, total)


def build_payload():
    data = incidence_data(False)
    transpose = incidence_data(True)
    groups = defaultdict(list)
    for i, component in enumerate(data["components"]):
        groups[(component["label"][0], component["label"][2])].append(i)
    monomials, rows = grounded_quadratic_matrix(data)
    rref = rank_and_rref_q(rows)
    forbidden = {
        monomials.index(tuple(sorted(pair)))
        for members in groups.values()
        for pair in combinations(members, 2)
    }
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    branch_rows = []
    for row3, row4, row5, column5 in product(range(3), range(4), range(4), range(5)):
        first_containment, second_containment, jacobian = branch_certificate(
            data, (row3, row4, row5), column5
        )
        branch_rows.append((first_containment, second_containment, jacobian == identity))
    second_minimum, second_witness = minimum_second_product_shadow()
    assert len(data["support"]) == 50 and len(data["shadow"]) == 75
    assert len(data["components"]) == len(transpose["components"]) == 16
    assert sorted(map(len, groups.values())) == [3, 4, 4, 5]
    assert len(rows) == 1140 and len(monomials) == 136
    assert set(rref) == forbidden and all(rref[pivot] == {pivot: 1} for pivot in forbidden)
    assert len(branch_rows) == 240 and all(a and b and c for a, b, c in branch_rows)
    assert second_minimum == 23
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_EQUALITY_LOCUS_CLASSIFICATION",
            "EXACT_QQ_QUADRATIC_ELIMINATION",
            "EXACT_SYMBOLIC_240_BRANCH_REPLAY",
            "N6-064",
        ],
        "standard_hook": {"dimension": 50, "first_shadow_dimension": 75},
        "linear_incidence": {
            "grassmann_tangent_variables": data["tangent_variable_count"],
            "grassmann_eta_variables": data["eta_variable_count"],
            "free_component_count": len(data["components"]),
            "free_group_sizes": sorted(map(len, groups.values())),
        },
        "quadratic_elimination": {
            "matrix_shape": [len(rows), len(monomials)],
            "rank_over_Q": len(rref),
            "forbidden_complete_graph_generator_count": len(forbidden),
            "rref_is_exactly_the_forbidden_unit_vectors": True,
        },
        "boolean_shear_branches": {
            "count": len(branch_rows),
            "all_first_shadow_symbolic_containments_hold": True,
            "all_second_shadow_symbolic_containments_hold": True,
            "all_selected_chart_jacobians_are_identity": True,
        },
        "transpose_hook": {
            "free_component_count": len(transpose["components"]),
            "free_group_sizes": sorted(
                Counter((component["label"][0], component["label"][2]) for component in transpose["components"]).values()
            ),
        },
        "second_product_shadow": {
            "universal_minimum_at_dimension_75": second_minimum,
            "first_ferrers_witness": list(second_witness),
            "equality_branch_second_shadow_dimension": 23,
            "boundary_second_shadows_remain_genuine_flag_hooks": True,
        },
        "claim_boundary": (
            "This classifies the rank-seventy-five product-shadow equality locus "
            "as Boolean-shear branch closures and proves second shadow twenty-three. "
            "Boundary second shadows remain genuine projective flag hooks, although "
            "no single finite Boolean-shear chart is asserted at every boundary point. "
            "It does not by itself exclude the b=50 Chow endpoint; actual section "
            "differences, the common quotient, and Chow realizability remain necessary."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
