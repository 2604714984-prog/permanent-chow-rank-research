# Exact join obstruction for two transposition slices

## Status

`CANONICAL FOUR-TERM JOIN FAMILY OBSTRUCTED; FULL PACKET OPEN.`

The one-transposition survivor does not remain a Sylvester-equality survivor
when two copies are joined in the natural four-term construction.  This holds
both when the transpositions share a row and when they are disjoint.

## 1. The exact join family

For a transposition `(i j)` and a nonzero scalar `a`, rescale the survivor as

\[
\begin{aligned}
 &(a/2)(q_i-q_j-a^{-1}u_{ij}-u_{ji})(q_j-u_{ji})
       \prod_{r\ne i,j}q_r\\
 &+(a/2)(q_i+q_j+a^{-1}u_{ij}-u_{ji})(q_j+u_{ji})
       \prod_{r\ne i,j}q_r\\
 &=a\prod_rq_r+u_{ij}u_{ji}\prod_{r\ne i,j}q_r.   \tag{1.1}
\end{aligned}
\]

Join two copies with identity weights `a` and `1-a`.  For `a` different from
zero and one, their sum is exactly the identity-permutation monomial plus the
two selected transposition monomials.  It contains four rank-seven Chow terms.

After normalizing the first factor line in (1.1), changing `a` only rescales
the slice-specific coordinate `u_ij` by `a^(-1)`; the remaining change is a
nonzero factor scaling.  The two slices use distinct forward `U` coordinates,
so these are independent invertible diagonal ambient changes.  Therefore the
three ranks of the joined complex are constant for every nonzero split
`a+(1-a)=1`.  The frozen values `-1,1/3,1/2,2/3,2` provide exact rational
controls, not the basis of the all-weight conclusion.

## 2. Shared-row join

Use transpositions `(0 1)` and `(0 2)` in the common 11-variable space

```text
q0,...,q6,u01,u10,u02,u20.
```

The four middle blocks are assembled before any rank is taken.  Exact rational
linear algebra gives

```text
middle dimension = 140
rank B            = 111
rank C            = 94
rank BC           = 75
coupling defect   = 10
```

Thus the canonical shared-row join violates `ker(B) subset image(C)`.

## 3. Disjoint join

For `(0 1)` and `(2 3)`, using

```text
q0,...,q6,u01,u10,u23,u32,
```

the same unprojected construction gives

```text
middle dimension = 140
rank B            = 114
rank C            = 95
rank BC           = 81
coupling defect   = 12.
```

Hence the canonical disjoint join also violates Sylvester equality.  The two
different defects show that shared-row overlap changes the coupled middle; the
result cannot be obtained by adding two copies of the one-slice ranks.

## 4. Boundary and global ranks

This closes the canonical four-term gluing family for every nonzero identity
weight split.  It does not classify all possible four-term factorizations,
cross-slice graph couplings, or joins involving additional terms.

A positive defect in an 11-variable subpacket can be repaired in principle by
the image of later term blocks.  Therefore defects 10 and 12 do not exclude a
42-complement completion.  Such a completion must be assembled in the
original 49-variable maps and must finish with

\[
 \operatorname{rank}B+\operatorname{rank}C=2870,
 \qquad\operatorname{rank}(BC)=1225.               \tag{4.1}
\]

The next smallest exact problem is to characterize the subspace of the join
kernel missing from `im(C)`, then test whether one additional rank-seven graph
term can cover it without adding an equal or larger new kernel.

Replay:

```text
python scripts/n7_b2_two_transposition_join_obstruction.py \
  --verify-json data/n7_b2_two_transposition_join_obstruction.json
python -m unittest tests.test_n7_b2_two_transposition_join_obstruction -v
```
