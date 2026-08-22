#!/usr/bin/env python3
"""Exact-prime Koszul audit of the Matlis-dual cospan for the F2 collision.

The essential variables are c,a1,...,a6,b1,...,b6.  The shifted inverse-
system module M=S*T_a+S*T_b is a direct sum through degree three.  We compute
the ranks on Tor_1,2 and Tor_2,3 induced by A_{T_a+T_b} -> M.  The remaining
36 ambient variables act trivially, so the ambient Tor_2,3 image rank is

    rank_ess(Tor_2,3) + 36 rank_ess(Tor_1,2).

Prime-field arithmetic is a diagnostic; the matrices have entries 0,+/-1,
and the report supplies the characteristic-zero structural interpretation.
"""

from itertools import combinations


P = 1_000_003
NV = 13
C = 0
A_VARS = tuple(range(1, 7))
B_VARS = tuple(range(7, 13))
TA = frozenset((C,) + A_VARS)
TB = frozenset((C,) + B_VARS)


def rank_mod(rows, ncols, p=P):
    """Rank of sparse row vectors, represented as dictionaries."""
    pivots = {}
    for src in rows:
        row = {j: v % p for j, v in src.items() if v % p}
        while row:
            j = min(row)
            if j not in pivots:
                inv = pow(row[j], p - 2, p)
                row = {k: (v * inv) % p for k, v in row.items() if v % p}
                pivots[j] = row
                break
            fac = row[j]
            base = pivots[j]
            for k, v in base.items():
                nv = (row.get(k, 0) - fac * v) % p
                if nv:
                    row[k] = nv
                elif k in row:
                    del row[k]
    return len(pivots)


def rref_with_kernel(matrix_rows, ncols, p=P):
    """Return rank and a sparse basis of the right kernel."""
    rows = [{j: v % p for j, v in r.items() if v % p} for r in matrix_rows]
    pivot_cols = []
    prow = 0
    for col in range(ncols):
        hit = next((r for r in range(prow, len(rows)) if rows[r].get(col, 0)), None)
        if hit is None:
            continue
        rows[prow], rows[hit] = rows[hit], rows[prow]
        inv = pow(rows[prow][col], p - 2, p)
        rows[prow] = {j: v * inv % p for j, v in rows[prow].items()}
        for r in range(len(rows)):
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
        if prow == len(rows):
            break
    free = [j for j in range(ncols) if j not in set(pivot_cols)]
    kernel = []
    for f in free:
        vec = {f: 1}
        for r, pc in enumerate(pivot_cols):
            val = rows[r].get(f, 0)
            if val:
                vec[pc] = -val % p
        kernel.append(vec)
    return len(pivot_cols), kernel


def span_basis(polys, p=P):
    """Choose a monomial-echelon basis and return coordinates of each input."""
    mons = sorted({m for poly in polys for m in poly})
    midx = {m: i for i, m in enumerate(mons)}
    pivots = {}
    basis_polys = []
    basis_origin = []
    coords = []
    for idx, poly in enumerate(polys):
        row = {midx[m]: c % p for m, c in poly.items() if c % p}
        coeff = {}
        while row:
            j = min(row)
            if j not in pivots:
                inv = pow(row[j], p - 2, p)
                row = {k: v * inv % p for k, v in row.items()}
                coeff = {k: v * inv % p for k, v in coeff.items()}
                bidx = len(basis_polys)
                pivots[j] = (row, bidx)
                basis_polys.append({m: c % p for m, c in poly.items() if c % p})
                basis_origin.append(idx)
                coeff[bidx] = (coeff.get(bidx, 0) + inv) % p
                break
            base, bidx = pivots[j]
            fac = row[j]
            for k, v in base.items():
                nv = (row.get(k, 0) - fac * v) % p
                if nv:
                    row[k] = nv
                elif k in row:
                    del row[k]
            coeff[bidx] = (coeff.get(bidx, 0) - fac) % p
        coords.append(coeff)
    # Recompute coordinates robustly against the selected original polynomials.
    selected = [polys[i] for i in basis_origin]
    all_mons = sorted({m for poly in selected + polys for m in poly})
    # Dense solve by augmenting selected columns; dimensions here are tiny.
    def coordinates(poly):
        equations = []
        for mon in all_mons:
            row = {j: selected[j].get(mon, 0) for j in range(len(selected))}
            rhs = poly.get(mon, 0) % p
            row[len(selected)] = -rhs
            equations.append(row)
        # Solve B*x=poly via RREF of [B|-poly], so last coordinate is fixed to 1.
        # Instead use elimination retaining the augmented scalar.
        mat = [[selected[j].get(mon, 0) % p for j in range(len(selected))] + [poly.get(mon, 0) % p]
               for mon in all_mons]
        rr = 0
        pc_for_row = []
        for col in range(len(selected)):
            hit = next((r for r in range(rr, len(mat)) if mat[r][col]), None)
            if hit is None:
                continue
            mat[rr], mat[hit] = mat[hit], mat[rr]
            inv = pow(mat[rr][col], p - 2, p)
            mat[rr] = [v * inv % p for v in mat[rr]]
            for r in range(len(mat)):
                if r != rr and mat[r][col]:
                    fac = mat[r][col]
                    mat[r] = [(x - fac * y) % p for x, y in zip(mat[r], mat[rr])]
            pc_for_row.append(col)
            rr += 1
        ans = {}
        for r, col in enumerate(pc_for_row):
            if mat[r][-1]:
                ans[col] = mat[r][-1]
        return ans
    return selected, [coordinates(poly) for poly in polys]


def differentiate(poly, var):
    out = {}
    for mon, coeff in poly.items():
        if var in mon:
            new = frozenset(set(mon) - {var})
            out[new] = (out.get(new, 0) + coeff) % P
    return out


def all_derivatives(top_polys, degree):
    polys = list(top_polys)
    for _ in range(degree):
        polys = [differentiate(poly, v) for poly in polys for v in range(NV)]
        polys = [p for p in polys if p]
    return polys


def module_data(top_polys, max_degree=3):
    bases = []
    for d in range(max_degree + 1):
        polys = all_derivatives(top_polys, d)
        basis, _ = span_basis(polys)
        bases.append(basis)
    actions = []
    for d in range(max_degree):
        candidates = [differentiate(poly, v) for poly in bases[d] for v in range(NV)]
        _, coords = span_basis(bases[d + 1] + candidates)
        assert len(span_basis(bases[d + 1] + candidates)[0]) == len(bases[d + 1])
        action_coords = coords[len(bases[d + 1]):]
        actions.append(action_coords)
    return bases, actions


def wedges(size):
    return list(combinations(range(NV), size))


def koszul_matrix(bases, actions, homological_degree, total_degree):
    md = total_degree - homological_degree
    source_wedges = wedges(homological_degree)
    target_wedges = wedges(homological_degree - 1)
    twidx = {w: i for i, w in enumerate(target_wedges)}
    source_dim = len(bases[md]) * len(source_wedges)
    target_dim = len(bases[md + 1]) * len(target_wedges)
    rows = [dict() for _ in range(target_dim)]
    for mb in range(len(bases[md])):
        for wi, w in enumerate(source_wedges):
            scol = mb * len(source_wedges) + wi
            for pos, var in enumerate(w):
                act = actions[md][mb * NV + var]
                w2 = w[:pos] + w[pos + 1:]
                sign = 1 if pos % 2 == 0 else -1
                for mb2, coeff in act.items():
                    row = mb2 * len(target_wedges) + twidx[w2]
                    rows[row][scol] = (rows[row].get(scol, 0) + sign * coeff) % P
    return rows, source_dim


def chain_map(source_bases, target_bases, degree_maps, homological_degree, total_degree):
    md = total_degree - homological_degree
    ws = wedges(homological_degree)
    src_dim = len(source_bases[md]) * len(ws)
    tgt_dim = len(target_bases[md]) * len(ws)
    rows = [dict() for _ in range(tgt_dim)]
    for sb, image in enumerate(degree_maps[md]):
        for wi in range(len(ws)):
            scol = sb * len(ws) + wi
            for tb, coeff in image.items():
                rows[tb * len(ws) + wi][scol] = coeff
    return rows, src_dim, tgt_dim


def map_poly_coordinates(source_bases, target_bases):
    maps = []
    for sbasis, tbasis in zip(source_bases, target_bases):
        combined, coords = span_basis(tbasis + sbasis)
        assert len(combined) == len(tbasis)
        maps.append(coords[len(tbasis):])
    return maps


def matvec_columns(rows, vectors, out_dim):
    """Apply row-matrix to sparse column vectors."""
    out = []
    for vec in vectors:
        col = {}
        for r, row in enumerate(rows):
            val = sum(row.get(j, 0) * c for j, c in vec.items()) % P
            if val:
                col[r] = val
        out.append(col)
    return out


def columns_to_rows(columns, nrows):
    rows = [dict() for _ in range(nrows)]
    for j, col in enumerate(columns):
        for i, val in col.items():
            rows[i][j] = val
    return rows


def homology_map_rank(src, tgt, degree_maps, homological_degree, total_degree):
    s_bases, s_actions = src
    t_bases, t_actions = tgt
    d_src, csrc = koszul_matrix(s_bases, s_actions, homological_degree, total_degree)
    _, zsrc = rref_with_kernel(d_src, csrc)
    dprev_tgt, cprev = koszul_matrix(t_bases, t_actions, homological_degree + 1, total_degree)
    bcols = []
    for j in range(cprev):
        col = {i: row[j] for i, row in enumerate(dprev_tgt) if j in row and row[j] % P}
        bcols.append(col)
    fmap, _, tgt_chain_dim = chain_map(s_bases, t_bases, degree_maps, homological_degree, total_degree)
    fz = matvec_columns(fmap, zsrc, tgt_chain_dim)
    rank_b = rank_mod(columns_to_rows(bcols, tgt_chain_dim), len(bcols))
    allcols = bcols + fz
    rank_all = rank_mod(columns_to_rows(allcols, tgt_chain_dim), len(allcols))
    return {
        "source_cycles": len(zsrc),
        "target_boundaries": rank_b,
        "image_rank_on_homology": rank_all - rank_b,
    }


def main():
    f = {TA: 1, TB: 1}
    ta = {TA: 1}
    tb = {TB: 1}
    A = module_data([f])
    M = module_data([ta, tb])
    maps = map_poly_coordinates(A[0], M[0])
    print("A Hilbert 0..3", [len(x) for x in A[0]])
    print("M Hilbert 0..3", [len(x) for x in M[0]])
    r12 = homology_map_rank(A, M, maps, 1, 2)
    r23 = homology_map_rank(A, M, maps, 2, 3)
    ambient = r23["image_rank_on_homology"] + 36 * r12["image_rank_on_homology"]
    print("Tor_1,2 map", r12)
    print("Tor_2,3 map", r23)
    print("ambient Tor_2,3 image rank", ambient)
    assert [len(x) for x in A[0]] == [1, 13, 42, 70]
    assert [len(x) for x in M[0]] == [2, 14, 42, 70]
    assert r12["image_rank_on_homology"] <= 14
    assert r23["image_rank_on_homology"] <= 84
    assert ambient <= 588
    print("F2_DUAL_COSPAN_PASS")


if __name__ == "__main__":
    main()
