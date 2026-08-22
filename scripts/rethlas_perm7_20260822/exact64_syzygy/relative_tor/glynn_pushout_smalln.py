#!/usr/bin/env python3
"""Exact-prime diagnostic for the relative-Tor pushout on small Glynn packets.

The matrices have entries in {0,+/-1}; ranks are computed over a large prime.
This is only a diagnostic unless a nonzero minor or a symbolic count is supplied.
"""

from itertools import combinations, combinations_with_replacement, product


P = 1_000_003


def monomials(m, degree):
    return list(combinations_with_replacement(range(m), degree))


def rank_mod(rows, p=P):
    """Sparse-row Gaussian elimination; each row is a dict col->value."""
    pivots = {}
    for source in rows:
        row = {c: v % p for c, v in source.items() if v % p}
        while row:
            c = min(row)
            if c not in pivots:
                inv = pow(row[c], p - 2, p)
                row = {j: (v * inv) % p for j, v in row.items() if v % p}
                pivots[c] = row
                break
            fac = row[c]
            base = pivots[c]
            for j, v in base.items():
                nv = (row.get(j, 0) - fac * v) % p
                if nv:
                    row[j] = nv
                elif j in row:
                    del row[j]
    return len(pivots)


def var(row, col, n):
    return col * n + row


def add_vec(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + scale * v
        if out[k] == 0:
            del out[k]
    return out


def glynn_i2_basis(n):
    """Basis of the quadrics common to all normalized Glynn terms."""
    qs = []
    # All quadrics using one matrix column twice.
    for c in range(n):
        for i in range(n):
            for j in range(i, n):
                qs.append({tuple(sorted((var(i, c, n), var(j, c, n)))): 1})
    # For each pair of columns: skew matrices and trace-zero diagonals.
    for c, d in combinations(range(n), 2):
        for i, j in combinations(range(n), 2):
            qs.append({
                tuple(sorted((var(i, c, n), var(j, d, n)))): 1,
                tuple(sorted((var(j, c, n), var(i, d, n)))): -1,
            })
        for i in range(n - 1):
            qs.append({
                tuple(sorted((var(i, c, n), var(i, d, n)))): 1,
                tuple(sorted((var(n - 1, c, n), var(n - 1, d, n)))): -1,
            })
    return qs


def multiplication_rows(n, qs):
    m = n * n
    mons3 = monomials(m, 3)
    row_index = {a: i for i, a in enumerate(mons3)}
    rows = [dict() for _ in mons3]
    for qidx, q in enumerate(qs):
        for a in range(m):
            domain_col = qidx * m + a
            for pair, coeff in q.items():
                mon = tuple(sorted((a,) + pair))
                rows[row_index[mon]][domain_col] = rows[row_index[mon]].get(domain_col, 0) + coeff
    return rows


def normalized_signs(n):
    return [(1,) + tail for tail in product((-1, 1), repeat=n - 1)]


def restrict_same_column_quadric(q, column, eps, n):
    total = 0
    lo = column * n
    hi = lo + n
    for (a, b), coeff in q.items():
        if lo <= a < hi and lo <= b < hi:
            total += coeff * eps[a - lo] * eps[b - lo]
    return total


def term_tor_rows(n, qs):
    """Rows of the map V tensor I2 -> direct sum_epsilon (L_epsilon tensor Q_epsilon)."""
    m = n * n
    signs = normalized_signs(n)
    out_dim_per_term = n * n * (n - 1)
    rows = [dict() for _ in range(len(signs) * out_dim_per_term)]
    for eidx, eps in enumerate(signs):
        for qidx, q in enumerate(qs):
            qscalars = [restrict_same_column_quadric(q, c, eps, n) for c in range(n)]
            for coeff_var in range(m):
                coeff_row = coeff_var % n
                coeff_col = coeff_var // n
                if coeff_row == n - 1:
                    # With complement e_{n-1}/eps_{n-1}, the L coordinates of
                    # a vector are its first n-1 row coefficients.
                    continue
                domain_col = qidx * m + coeff_var
                for qcol, scalar in enumerate(qscalars):
                    if scalar:
                        local = (qcol * n + coeff_col) * (n - 1) + coeff_row
                        outrow = eidx * out_dim_per_term + local
                        rows[outrow][domain_col] = rows[outrow].get(domain_col, 0) + scalar
    return rows


def audit(n):
    m = n * n
    qs = glynn_i2_basis(n)
    mult = multiplication_rows(n, qs)
    tor = term_tor_rows(n, qs)
    rank_mult = rank_mod(mult)
    rank_stacked = rank_mod(mult + tor)
    h_i = m * len(qs) - rank_mult
    rank_persistent = rank_stacked - rank_mult

    # Closed counts from the permanent and common-Glynn quadratic spaces.
    j2 = (n * (n + 1) // 2) ** 2
    a3 = (n * (n - 1) * (n - 2) // 6) ** 2
    s3 = (m + 2) * (m + 1) * m // 6
    h_j = m * j2 - (s3 - a3)
    term_beta = (m - n) * n
    terms = 2 ** (n - 1)
    d_beta = terms * term_beta
    quotient_created = h_j - h_i
    kappa = quotient_created + rank_persistent
    boolean_kernel_per_ordered_column_pair = n * (n * n - 1) // 3
    predicted_persistent_rank = n * n * boolean_kernel_per_ordered_column_pair
    predicted_quotient_created = n * boolean_kernel_per_ordered_column_pair
    assert quotient_created == predicted_quotient_created
    assert rank_persistent == predicted_persistent_rank
    return {
        "n": n,
        "terms": terms,
        "i2": len(qs),
        "H_I": h_i,
        "H_perm": h_j,
        "quotient_created": quotient_created,
        "persistent_rank": rank_persistent,
        "persistent_rank_formula": predicted_persistent_rank,
        "pushout_kappa": kappa,
        "term_beta_total": d_beta,
        "cap_holds": kappa <= d_beta,
    }


if __name__ == "__main__":
    for n in range(3, 8):
        print(audit(n))
    print("GLYNN_PUSHOUT_SMALLN_PASS")
