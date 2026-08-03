#!/usr/bin/env python3
"""Independent clean-room mathematical audit for the 20260802 v9 AMS hardened reviewer package.

Scope deliberately limited to claims reconstructible from the PDF alone.
No author certificate, project module, SAT instance, DRAT proof, or manifest is imported.

Checks:
1. The old literal-space coupling counterexample and corrected catalectic ranks.
2. Shifted shadow data at s=19,21,22.
3. The s=19 equality-shadow count (800) and the 24 relative orbits under the
   stabilizer of a fixed pure row-edge hyperplane.
4. The n=5 base Koszul rank modulo 1,000,003.
5. The 100 pure row/column edge hyperplanes have p_Fp=35.
6. Their 21,510 unique one-coordinate extensions have p_Fp<=50.
7. The fixed-six budget arithmetic leaves only (19,9,45,54).

Finite-field results are used only in the valid direction:
rank_Q >= rank_Fp, hence nullity_Q <= nullity_Fp.
This script does NOT certify the manuscript's global p9 classification, the
58-state partition, the 19 reused finite-geometry certificates, or the 24
CNF/DRAT boundary instances.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Sequence
import hashlib

P = 1_000_003


def rational_rank(rows: Sequence[Sequence[int]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(x) for x in row] for row in rows]
    nr, nc = len(matrix), len(matrix[0])
    rank = 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pv = matrix[rank][col]
        matrix[rank] = [x / pv for x in matrix[rank]]
        for r in range(nr):
            if r == rank or not matrix[r][col]:
                continue
            f = matrix[r][col]
            matrix[r] = [matrix[r][c] - f * matrix[rank][c] for c in range(nc)]
        rank += 1
        if rank == nr:
            break
    return rank


def derivative_space_sum_dimension(terms: Sequence[frozenset[int]], degree: int) -> int:
    out: set[frozenset[int]] = set()
    for term in terms:
        out.update(frozenset(x) for x in combinations(sorted(term), degree))
    return len(out)


def catalectic_rank_squarefree_sum(terms: Sequence[frozenset[int]], output_degree: int) -> int:
    total_degree = len(terms[0])
    derivative_order = total_degree - output_degree
    variables = sorted(set().union(*terms))
    operators = list(combinations(variables, derivative_order))
    outputs = list(combinations(variables, output_degree))
    out_index = {frozenset(x): i for i, x in enumerate(outputs)}
    matrix = [[0 for _ in operators] for _ in outputs]
    for j, operator in enumerate(operators):
        op = frozenset(operator)
        for term in terms:
            if op <= term:
                matrix[out_index[term - op]][j] += 1
    return rational_rank(matrix)


Triple = tuple[int, int, int]
Pair = tuple[int, int]


def componentwise_leq(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    return all(x <= y for x, y in zip(a, b))


def base_order_ideals(poset: Sequence[Triple]) -> list[int]:
    ans: list[int] = []
    for mask in range(1 << len(poset)):
        valid = True
        for j in range(len(poset)):
            if not ((mask >> j) & 1):
                continue
            for i in range(len(poset)):
                if componentwise_leq(poset[i], poset[j]) and not ((mask >> i) & 1):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            ans.append(mask)
    return ans


def cover_predecessors(poset: Sequence[Triple]) -> list[list[int]]:
    ans: list[list[int]] = []
    for j in range(len(poset)):
        pred: list[int] = []
        for i in range(j):
            if not componentwise_leq(poset[i], poset[j]):
                continue
            if any(
                k not in (i, j)
                and componentwise_leq(poset[i], poset[k])
                and componentwise_leq(poset[k], poset[j])
                for k in range(len(poset))
            ):
                continue
            pred.append(i)
        ans.append(pred)
    return ans


def enumerate_product_order_ideals(
    target: int,
    poset: Sequence[Triple],
    ideals: Sequence[int],
    predecessors: Sequence[Sequence[int]],
) -> list[tuple[int, ...]]:
    full = (1 << len(poset)) - 1
    subideals = {b: [x for x in ideals if not (x & ~b)] for b in ideals}
    assignment = [0] * len(poset)
    output: list[tuple[int, ...]] = []

    def rec(pos: int, size: int) -> None:
        if size > target:
            return
        if pos == len(poset):
            if size == target:
                output.append(tuple(assignment))
            return
        bound = full
        for pred in predecessors[pos]:
            bound &= assignment[pred]
        for fibre in subideals[bound]:
            nxt = size + fibre.bit_count()
            if nxt <= target:
                assignment[pos] = fibre
                rec(pos + 1, nxt)

    rec(0, 0)
    return output


def assignment_to_bits(assignment: Sequence[int]) -> int:
    out = 0
    for r, fibre in enumerate(assignment):
        for c in range(10):
            if (fibre >> c) & 1:
                out |= 1 << (10 * r + c)
    return out


def singleton_shadow_masks(triples: Sequence[Triple], pairs: Sequence[Pair]) -> list[int]:
    pair_index = {p: i for i, p in enumerate(pairs)}
    triple_masks: list[int] = []
    for triple in triples:
        mask = 0
        for pair in combinations(triple, 2):
            mask |= 1 << pair_index[pair]
        triple_masks.append(mask)
    ans: list[int] = []
    for r in range(10):
        for c in range(10):
            shadow = 0
            for rp in range(10):
                if not ((triple_masks[r] >> rp) & 1):
                    continue
                for cp in range(10):
                    if (triple_masks[c] >> cp) & 1:
                        shadow |= 1 << (10 * rp + cp)
            ans.append(shadow)
    return ans


def family_shadow(bits: int, singleton: Sequence[int]) -> int:
    out = 0
    rem = bits
    while rem:
        low = rem & -rem
        idx = low.bit_length() - 1
        out |= singleton[idx]
        rem -= low
    return out


def permutation_maps(objects: Sequence[tuple[int, ...]]) -> list[list[int]]:
    index = {obj: i for i, obj in enumerate(objects)}
    ans: list[list[int]] = []
    for perm in permutations(range(5)):
        ans.append([index[tuple(sorted(perm[x] for x in obj))] for obj in objects])
    return ans


def transform_bipartite(bits: int, row_map: Sequence[int], col_map: Sequence[int], transpose: bool = False) -> int:
    out = 0
    rem = bits
    while rem:
        low = rem & -rem
        idx = low.bit_length() - 1
        r, c = divmod(idx, 10)
        if transpose:
            nr, nc = col_map[c], row_map[r]
        else:
            nr, nc = row_map[r], col_map[c]
        out |= 1 << (10 * nr + nc)
        rem -= low
    return out


# ---------- Sparse Koszul rank over F_p ----------

N = 5
VARS = {(i, a): 5 * i + a for i in range(5) for a in range(5)}
WEDGE_PAIRS = list(combinations(range(25), 2))
WEDGE_INDEX = {x: i for i, x in enumerate(WEDGE_PAIRS)}


def output_index(first: int, a: int, b: int) -> tuple[int | None, int]:
    if a == b:
        return None, 0
    if a < b:
        return first * len(WEDGE_PAIRS) + WEDGE_INDEX[(a, b)], 1
    return first * len(WEDGE_PAIRS) + WEDGE_INDEX[(b, a)], -1


def delta_column(q: dict[tuple[int, int], int], w: int, p: int = P) -> dict[int, int]:
    out: dict[int, int] = {}
    for (u, v), coeff in q.items():
        idx, sign = output_index(v, u, w)
        if idx is not None:
            out[idx] = (out.get(idx, 0) + coeff * sign) % p
        idx, sign = output_index(u, v, w)
        if idx is not None:
            out[idx] = (out.get(idx, 0) + coeff * sign) % p
    return {k: v for k, v in out.items() if v}


def sparse_basis(columns: Iterable[dict[int, int]], p: int = P) -> dict[int, dict[int, int]]:
    pivots: dict[int, dict[int, int]] = {}
    for column in columns:
        vector = dict(column)
        while vector:
            pivot = max(vector)
            if pivot not in pivots:
                inv = pow(vector[pivot], p - 2, p)
                pivots[pivot] = {k: (v * inv) % p for k, v in vector.items() if v % p}
                break
            factor = vector[pivot]
            for k, value in pivots[pivot].items():
                new = (vector.get(k, 0) - factor * value) % p
                if new:
                    vector[k] = new
                elif k in vector:
                    del vector[k]
    return pivots


def reduce_column(column: dict[int, int], pivots: dict[int, dict[int, int]], p: int = P) -> dict[int, int]:
    vector = dict(column)
    while True:
        available = [r for r in vector if r in pivots]
        if not available:
            return vector
        pivot = max(available)
        factor = vector[pivot]
        for k, value in pivots[pivot].items():
            new = (vector.get(k, 0) - factor * value) % p
            if new:
                vector[k] = new
            elif k in vector:
                del vector[k]


def sparse_rank(columns: Iterable[dict[int, int]], p: int = P) -> int:
    return len(sparse_basis(columns, p))


def build_E_basis() -> list[dict[tuple[int, int], int]]:
    basis = []
    for i, j in combinations(range(5), 2):
        for a, b in combinations(range(5), 2):
            m1 = tuple(sorted((VARS[(i, a)], VARS[(j, b)])))
            m2 = tuple(sorted((VARS[(i, b)], VARS[(j, a)])))
            basis.append({m1: 1, m2: 1})
    return basis


def build_quotient_coordinates() -> tuple[list[dict[tuple[int, int], int]], list[tuple]]:
    basis: list[dict[tuple[int, int], int]] = []
    labels: list[tuple] = []
    for i in range(5):
        for a in range(5):
            u = VARS[(i, a)]
            basis.append({(u, u): 1})
            labels.append(("sq", i, a))
    for i in range(5):
        for a, b in combinations(range(5), 2):
            basis.append({tuple(sorted((VARS[(i, a)], VARS[(i, b)]))): 1})
            labels.append(("row", i, a, b))
    for a in range(5):
        for i, j in combinations(range(5), 2):
            basis.append({tuple(sorted((VARS[(i, a)], VARS[(j, a)]))): 1})
            labels.append(("col", a, i, j))
    for i, j in combinations(range(5), 2):
        for a, b in combinations(range(5), 2):
            # One matching monomial is a valid lift of the 1-d quotient weight.
            basis.append({tuple(sorted((VARS[(i, a)], VARS[(j, b)]))): 1})
            labels.append(("cross", i, j, a, b))
    assert len(basis) == 225
    return basis, labels


def main() -> None:
    pdf = Path('/mnt/data/perm345_v9_ams_hardened_reviewer.pdf')
    print(f"PDF_SHA256={hashlib.sha256(pdf.read_bytes()).hexdigest()}")

    # Coupling semantics counterexample.
    terms = [frozenset({0, 1, 2, 3, 4}), frozenset({0, 1, 2, 3, 5})]
    assert derivative_space_sum_dimension(terms, 3) == 16
    assert derivative_space_sum_dimension(terms, 2) == 14
    assert catalectic_rank_squarefree_sum(terms, 3) == 10
    assert catalectic_rank_squarefree_sum(terms, 2) == 10
    print("COUPLING_LITERAL_CUBIC_SUM_DIM=16")
    print("COUPLING_LITERAL_QUADRATIC_SUM_DIM=14")
    print("COUPLED_C23_RANK=10")
    print("COUPLED_C32_RANK=10")

    # Shadow enumerations.
    triples: list[Triple] = list(combinations(range(5), 3))
    pairs: list[Pair] = list(combinations(range(5), 2))
    ideals = base_order_ideals(triples)
    predecessors = cover_predecessors(triples)
    singleton = singleton_shadow_masks(triples, pairs)
    data: dict[int, tuple[int, Counter[int], set[int]]] = {}
    for size in (19, 20, 21, 22, 23):
        families = enumerate_product_order_ideals(size, triples, ideals, predecessors)
        shadows = [family_shadow(assignment_to_bits(x), singleton) for x in families]
        dist = Counter(x.bit_count() for x in shadows)
        minimum = min(dist)
        minimizers = {x for x in shadows if x.bit_count() == minimum}
        data[size] = (len(families), dist, minimizers)
        print(f"SHIFTED_SIZE_{size}_COUNT={len(families)}")
        print(f"SHIFTED_SIZE_{size}_MIN_SHADOW={minimum}")
        print(f"SHIFTED_SIZE_{size}_MINIMIZER_FAMILY_COUNT={dist[minimum]}")
        print(f"SHIFTED_SIZE_{size}_DISTINCT_MIN_SHADOWS={len(minimizers)}")
    assert data[19][0] == 3957 and min(data[19][1]) == 45 and data[19][1][45] == 2
    assert data[20][0] == 5209 and min(data[20][1]) == 48
    assert data[21][0] == 6778 and min(data[21][1]) == 48 and data[21][1][48] == 4
    assert data[22][0] == 8700 and min(data[22][1]) == 48 and data[22][1][49] == 0
    assert data[23][0] == 11035 and min(data[23][1]) == 52
    print("FIXED_SIX_SHADOW_CUTOFF=m23=52>51")

    pair_maps = permutation_maps(pairs)
    equality_shadows_19: set[int] = set()
    for rm in pair_maps:
        for cm in pair_maps:
            for shadow in data[19][2]:
                equality_shadows_19.add(transform_bipartite(shadow, rm, cm, False))
                equality_shadows_19.add(transform_bipartite(shadow, rm, cm, True))
    assert len(equality_shadows_19) == 800
    print("S19_EQUALITY_SHADOWS=800")

    # Stabilizer of W = all squarefree edges in matrix row 0 except column edge {0,1}.
    pair_index = {x: i for i, x in enumerate(pairs)}
    row_perms = [p for p in permutations(range(5)) if p[0] == 0]
    col_perms = [p for p in permutations(range(5)) if frozenset((p[0], p[1])) == frozenset((0, 1))]
    stabilizer_maps = []
    for rp in row_perms:
        rm = [pair_index[tuple(sorted((rp[a], rp[b])))] for a, b in pairs]
        for cp in col_perms:
            cm = [pair_index[tuple(sorted((cp[a], cp[b])))] for a, b in pairs]
            stabilizer_maps.append((rm, cm))
    assert len(stabilizer_maps) == 288
    canonical = {
        min(transform_bipartite(shadow, rm, cm, False) for rm, cm in stabilizer_maps)
        for shadow in equality_shadows_19
    }
    assert len(canonical) == 24
    print("PURE_EDGE_STABILIZER_SIZE=288")
    print("S19_RELATIVE_SHADOW_ORBITS=24")

    # Koszul/coker calculations modulo P.
    E_basis = build_E_basis()
    E_pivots = sparse_basis(delta_column(q, w) for q in E_basis for w in range(25))
    assert len(E_pivots) == 2400
    print(f"N5_BASE_KOSZUL_RANK_MOD_{P}=2400")

    quotient_basis, labels = build_quotient_coordinates()
    reduced: list[list[dict[int, int]]] = []
    for q in quotient_basis:
        reduced.append([reduce_column(delta_column(q, w), E_pivots) for w in range(25)])
    label_to_index = {label: i for i, label in enumerate(labels)}

    def p_mod(indices: Sequence[int]) -> int:
        rank_added = sparse_rank(reduced[i][w] for i in indices for w in range(25))
        return 25 * len(indices) - rank_added

    edge_hyperplanes: list[tuple[int, ...]] = []
    for row in range(5):
        edges = [label_to_index[("row", row, a, b)] for a, b in combinations(range(5), 2)]
        for omitted in edges:
            edge_hyperplanes.append(tuple(sorted(x for x in edges if x != omitted)))
    for col in range(5):
        edges = [label_to_index[("col", col, i, j)] for i, j in combinations(range(5), 2)]
        for omitted in edges:
            edge_hyperplanes.append(tuple(sorted(x for x in edges if x != omitted)))
    assert len(edge_hyperplanes) == 100 and len(set(edge_hyperplanes)) == 100
    edge_p = Counter(p_mod(x) for x in edge_hyperplanes)
    assert edge_p == Counter({35: 100})
    print("PURE_ROW_COLUMN_EDGE_HYPERPLANES=100")
    print(f"PURE_EDGE_P9_MOD_{P}=35")

    # Exact-Q replay for one representative, blockwise by the 5+5 torus weight.
    # All 100 representatives are conjugate under row/column permutations.
    representative = edge_hyperplanes[0]
    representative_H = E_basis + [quotient_basis[i] for i in representative]

    def variable_weight(index: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
        row, col = divmod(index, 5)
        rw = [0] * 5
        cw = [0] * 5
        rw[row] = 1
        cw[col] = 1
        return tuple(rw), tuple(cw)

    def add_weight(left, right):
        return (
            tuple(a + b for a, b in zip(left[0], right[0])),
            tuple(a + b for a, b in zip(left[1], right[1])),
        )

    def quadratic_weight(q):
        u, v = next(iter(q))
        return add_weight(variable_weight(u), variable_weight(v))

    def delta_column_integer(q, w):
        out = {}
        for (u, v), coeff in q.items():
            idx, sign = output_index(v, u, w)
            if idx is not None:
                out[idx] = out.get(idx, 0) + coeff * sign
            idx, sign = output_index(u, v, w)
            if idx is not None:
                out[idx] = out.get(idx, 0) + coeff * sign
        return {k: value for k, value in out.items() if value}

    exact_blocks = {}
    for q in representative_H:
        qw = quadratic_weight(q)
        for w in range(25):
            weight = add_weight(qw, variable_weight(w))
            exact_blocks.setdefault(weight, []).append(delta_column_integer(q, w))

    exact_rank = 0
    for columns in exact_blocks.values():
        row_indices = sorted(set().union(*(column.keys() for column in columns)))
        exact_rank += rational_rank([[column.get(row, 0) for column in columns] for row in row_indices])
    exact_nullity = 25 * len(representative_H) - exact_rank
    assert exact_rank == 2590 and exact_nullity == 135 and exact_nullity - 100 == 35
    print("PURE_EDGE_P9_EXACT_Q=35")
    print(f"PURE_EDGE_WEIGHT_BLOCKS_NONEMPTY={len(exact_blocks)}")

    extensions: set[tuple[int, ...]] = set()
    universe = set(range(225))
    for hyperplane in edge_hyperplanes:
        h = set(hyperplane)
        for extra in universe - h:
            extensions.add(tuple(sorted((*hyperplane, extra))))
    assert len(extensions) == 21_510
    extension_distribution = Counter(p_mod(x) for x in extensions)
    assert max(extension_distribution) == 50
    assert extension_distribution == Counter({35: 19000, 36: 2000, 39: 200, 40: 300, 50: 10})
    print("PURE_EDGE_UNIQUE_ONE_DIRECTION_EXTENSIONS=21510")
    print(f"PURE_EDGE_EXTENSION_P10_MAX_MOD_{P}=50")
    print("PURE_EDGE_EXTENSION_P10_DISTRIBUTION=" + repr(dict(sorted(extension_distribution.items()))))

    # Fixed-six low-coupling budget arithmetic.
    m19 = 45
    row_loss = 25 * 19 - m19
    assert row_loss == 430
    lower_d10 = 2400 + (25 * 10 - 50) - row_loss
    lower_d11 = 2400 + (25 * 11 - 75) - row_loss
    assert lower_d10 == lower_d11 == 2170
    assert 2170 > 9 * 240 == 2160
    assert 55 - 19 == 36 and 56 - 19 == 37
    equality_lower = 2400 + (25 * 9 - 35) - row_loss
    assert equality_lower == 2160
    print("FIXED_SIX_S19_ROW_LOSS=430")
    print("FIXED_SIX_D10_LOWER_BOUND=2170")
    print("FIXED_SIX_D11_LOWER_BOUND=2170")
    print("FIXED_SIX_RESIDUAL_NINE_TERM_CAP=2160")
    print("FIXED_SIX_UNIQUE_NUMERIC_EQUALITY_STATE=(19,9,45,54)")

    # Independently regenerate the 58-state fixed-six integer frontier and
    # the 38/19/1 routing partition stated in Appendix B.3.
    states = []
    for s_value, d_max, shadow_minimum in ((19, 15, 45), (20, 12, 48), (21, 12, 48), (22, 12, 48)):
        for d_value in range(9, d_max + 1):
            for t_value in range(shadow_minimum, min(51, 60 - d_value) + 1):
                states.append((s_value, d_value, t_value, t_value + d_value))
    assert len(states) == 58 and len(set(states)) == 58

    routes = Counter()
    for state in states:
        s_value, d_value, t_value, h_value = state
        if state == (19, 9, 45, 54):
            route = "new_p9_equality_shadow_prolongation_obstruction"
        elif s_value == 19:
            route = "new_global_p_bound_integer_budget"
        elif d_value == 9 and not (s_value == 22 and t_value == 48):
            # p(W)>=h-s is strictly larger than the global p9 bound 35.
            assert h_value - s_value > 35
            route = "new_global_p_bound_integer_budget"
        else:
            assert h_value >= 57
            route = "legacy_geometry_only_after_H_equals_U"
        routes[route] += 1
    assert routes == Counter({
        "new_global_p_bound_integer_budget": 38,
        "legacy_geometry_only_after_H_equals_U": 19,
        "new_p9_equality_shadow_prolongation_obstruction": 1,
    })
    print("FIXED_SIX_STATE_COUNT=58")
    print("FIXED_SIX_ROUTE_HISTOGRAM=" + repr(dict(routes)))
    print("FIXED_SIX_LOW_COUPLING_STATES=" + repr([x for x in states if x[3] < 57]))

    print("INDEPENDENT_PARTIAL_AUDIT_PASS")
    print("NOT_VERIFIED_BY_THIS_SCRIPT=global_p9_exhaustion,19_legacy_finite_geometry_semantics,24_CNF_DRAT_semantics,omitted_10GB_lower15_SAT_layer")


if __name__ == '__main__':
    main()
