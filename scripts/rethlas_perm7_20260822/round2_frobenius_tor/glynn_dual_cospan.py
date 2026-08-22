#!/usr/bin/env python3
"""Walsh-character audit of the complementary Tor map for Glynn's packet.

For normalized signs epsilon=(1,+/-1,...,+/-1), Fourier transform the 64
Glynn generators.  In derivative degree d and a fixed d-subset J of columns,
the shifted canonical module M has basis v_{J,U}, with

    U subset {1,...,6},  |U| <= 7-d.

Differentiation by row a in a new column toggles a in U (row zero does
nothing); characters exceeding the next size cutoff vanish.  The permanent
cyclic submodule maps the row-set basis R to

    U={1,...,6} symmetric_difference (R minus {0}).

The script computes the induced rank on Tor_2,3 independently in the three
column-multidegree types 3, 2+1, and 1+1+1.  All matrices have entries
0,+/-1.  Prime-field output is diagnostic; the character model itself is
valid over characteristic zero (and every characteristic different from 2).
"""

from itertools import combinations, product


P = 1_000_003
N = 7
ROWS = tuple(range(N))
NONTRIV = frozenset(range(1, N))


def subsets(items, max_size=None, exact_size=None):
    items = tuple(items)
    if exact_size is not None:
        sizes = [exact_size]
    else:
        sizes = range(0, (len(items) if max_size is None else max_size) + 1)
    return [frozenset(c) for s in sizes for c in combinations(items, s)]


def module_states(kind, degree, removed):
    if kind == "A":
        return subsets(ROWS, exact_size=degree)
    if kind == "M":
        return subsets(range(1, N), max_size=N - degree)
    if kind == "D":
        return subsets(range(1, N), max_size=N - 1)
    raise ValueError(kind)


def removed_subsets(total_counts, degree):
    available = [c for c, q in enumerate(total_counts) if q]
    return [frozenset(x) for x in combinations(available, degree)]


def wedge_choices(counts):
    """Wedge-variable tuples with prescribed column multiplicities."""
    per_column = []
    for col, q in enumerate(counts):
        if q:
            per_column.append([
                tuple(col * N + r for r in rr)
                for rr in combinations(ROWS, q)
            ])
    if not per_column:
        return [tuple()]
    return [tuple(sorted(sum(parts, tuple()))) for parts in product(*per_column)]


def chain_basis(kind, homological_degree, total_counts):
    degree = 3 - homological_degree
    out = []
    for removed in removed_subsets(total_counts, degree):
        residual = [q - (1 if c in removed else 0) for c, q in enumerate(total_counts)]
        if min(residual) < 0 or sum(residual) != homological_degree:
            continue
        for state in module_states(kind, degree, removed):
            for wedge in wedge_choices(residual):
                out.append((removed, state, wedge))
    return out


def act(kind, degree, state, row):
    if kind == "A":
        if row in state:
            return None
        return frozenset(set(state) | {row})
    toggled = state if row == 0 else frozenset(set(state) ^ {row})
    if kind == "M" and len(toggled) > N - degree - 1:
        return None
    return toggled


def differential_columns(kind, homological_degree, total_counts):
    source = chain_basis(kind, homological_degree, total_counts)
    target = chain_basis(kind, homological_degree - 1, total_counts)
    tidx = {b: i for i, b in enumerate(target)}
    cols = []
    for removed, state, wedge in source:
        colvec = {}
        degree = 3 - homological_degree
        for pos, var in enumerate(wedge):
            c, r = divmod(var, N)
            if c in removed:
                continue
            state2 = act(kind, degree, state, r)
            if state2 is None:
                continue
            removed2 = frozenset(set(removed) | {c})
            wedge2 = wedge[:pos] + wedge[pos + 1:]
            key = (removed2, state2, wedge2)
            j = tidx[key]
            sign = 1 if pos % 2 == 0 else -1
            colvec[j] = (colvec.get(j, 0) + sign) % P
        cols.append({j: v for j, v in colvec.items() if v % P})
    return source, target, cols


def columns_to_rows(columns, nrows):
    rows = [dict() for _ in range(nrows)]
    for j, col in enumerate(columns):
        for i, val in col.items():
            rows[i][j] = val
    return rows


def kernel_basis(columns, nrows, p=P):
    """Sparse RREF kernel of a linear map represented by its columns."""
    rows = columns_to_rows(columns, nrows)
    ncols = len(columns)
    prow = 0
    pivot_cols = []
    for col in range(ncols):
        hit = next((r for r in range(prow, nrows) if rows[r].get(col, 0)), None)
        if hit is None:
            continue
        rows[prow], rows[hit] = rows[hit], rows[prow]
        inv = pow(rows[prow][col], p - 2, p)
        rows[prow] = {j: v * inv % p for j, v in rows[prow].items() if v % p}
        for r in range(nrows):
            if r == prow or not rows[r].get(col, 0):
                continue
            fac = rows[r][col]
            for j, v in rows[prow].items():
                nv = (rows[r].get(j, 0) - fac * v) % p
                if nv:
                    rows[r][j] = nv
                elif j in rows[r]:
                    del rows[r][j]
        pivot_cols.append(col)
        prow += 1
        if prow == nrows:
            break
    pset = set(pivot_cols)
    kernel = []
    for free in (j for j in range(ncols) if j not in pset):
        vec = {free: 1}
        for r, pc in enumerate(pivot_cols):
            val = rows[r].get(free, 0)
            if val:
                vec[pc] = -val % p
        kernel.append(vec)
    return len(pivot_cols), kernel


def add_to_column_span(vec, pivots, p=P):
    row = {j: v % p for j, v in vec.items() if v % p}
    while row:
        j = min(row)
        if j not in pivots:
            inv = pow(row[j], p - 2, p)
            pivots[j] = {k: v * inv % p for k, v in row.items() if v % p}
            return True
        fac = row[j]
        for k, v in pivots[j].items():
            nv = (row.get(k, 0) - fac * v) % p
            if nv:
                row[k] = nv
            elif k in row:
                del row[k]
    return False


def span_rank(columns):
    pivots = {}
    for col in columns:
        add_to_column_span(col, pivots)
    return len(pivots)


def permanent_to_M_index(total_counts):
    a_basis = chain_basis("A", 2, total_counts)
    m_basis = chain_basis("M", 2, total_counts)
    midx = {b: i for i, b in enumerate(m_basis)}
    mapping = []
    for removed, rowset, wedge in a_basis:
        u = frozenset(set(NONTRIV) ^ set(rowset - {0}))
        mapping.append(midx[(removed, u, wedge)])
    return mapping


def image_rank(total_counts):
    a_c2, a_c1, a_d2 = differential_columns("A", 2, total_counts)
    _, a_cycles = kernel_basis(a_d2, len(a_c1))
    a_c3, _, a_d3 = differential_columns("A", 3, total_counts)
    a_boundary_rank = span_rank(a_d3)
    a_h = len(a_cycles) - a_boundary_rank

    m_c2, _, _ = differential_columns("M", 2, total_counts)
    m_c3, _, m_d3 = differential_columns("M", 3, total_counts)
    pivots = {}
    for col in m_d3:
        add_to_column_span(col, pivots)
    m_boundary_rank = len(pivots)

    amap = permanent_to_M_index(total_counts)
    a_images = []
    for cyc in a_cycles:
        image = {}
        for j, coeff in cyc.items():
            k = amap[j]
            image[k] = (image.get(k, 0) + coeff) % P
        a_images.append(image)
    for image in a_images:
        add_to_column_span(image, pivots)
    added = len(pivots) - m_boundary_rank

    # In degree one, D and M have the same 64 Walsh characters.  Hence their
    # K_2 groups and K_3-boundary spaces are literally equal.  The quotient
    # D->M only weakens the K_2->K_1 differential by deleting the full
    # character in derivative degree two.
    d_c2, d_c1, d_d2 = differential_columns("D", 2, total_counts)
    _, d_cycles = kernel_basis(d_d2, len(d_c1))
    d_c3, _, d_d3 = differential_columns("D", 3, total_counts)
    assert d_c2 == m_c2
    assert d_c3 == m_c3
    assert d_d3 == m_d3

    rank_b = span_rank(m_d3)
    rank_bd = span_rank(m_d3 + d_cycles)
    rank_ba = span_rank(m_d3 + a_images)
    rank_bda = span_rank(m_d3 + d_cycles + a_images)
    d_image_rank = rank_bd - rank_b
    intersection_rank = (
        d_image_rank + (rank_ba - rank_b) - (rank_bda - rank_b)
    )
    target_only_rank = added - intersection_rank
    assert len(m_c3) == len(m_d3)
    return {
        "A_C2": len(a_c2),
        "A_cycles": len(a_cycles),
        "A_boundaries": a_boundary_rank,
        "A_homology": a_h,
        "M_C2": len(m_c2),
        "M_boundaries": m_boundary_rank,
        "map_rank": added,
        "D_homology": len(d_cycles) - span_rank(d_d3),
        "D_image_rank": d_image_rank,
        "A_D_image_intersection": intersection_rank,
        "A_image_outside_D": target_only_rank,
    }


def main():
    cases = {
        "3": (3, 0, 0, 0, 0, 0, 0),
        "21": (2, 1, 0, 0, 0, 0, 0),
        "111": (1, 1, 1, 0, 0, 0, 0),
    }
    results = {}
    for name, counts in cases.items():
        print("auditing", name, flush=True)
        results[name] = image_rank(counts)
        print(name, results[name], flush=True)
    total_h = 7 * results["3"]["A_homology"] + 42 * results["21"]["A_homology"] + 35 * results["111"]["A_homology"]
    total_rank = 7 * results["3"]["map_rank"] + 42 * results["21"]["map_rank"] + 35 * results["111"]["map_rank"]
    total_d = 7 * results["3"]["D_image_rank"] + 42 * results["21"]["D_image_rank"] + 35 * results["111"]["D_image_rank"]
    total_intersection = 7 * results["3"]["A_D_image_intersection"] + 42 * results["21"]["A_D_image_intersection"] + 35 * results["111"]["A_D_image_intersection"]
    total_target_only = 7 * results["3"]["A_image_outside_D"] + 42 * results["21"]["A_image_outside_D"] + 35 * results["111"]["A_image_outside_D"]
    print("total permanent beta23", total_h)
    print("total complementary-Tor image rank", total_rank)
    print("total term-side image rank", total_d)
    print("target/term image intersection", total_intersection)
    print("target image outside term image", total_target_only)
    assert total_h == 18816
    assert total_rank == 6272
    assert total_d == 18816
    assert total_intersection == 5488
    assert total_target_only == 784
    print("GLYNN_DUAL_COSPAN_PASS")


if __name__ == "__main__":
    main()
