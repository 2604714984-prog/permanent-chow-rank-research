# Exact join obstruction for two transposition slices

## Status

`CANONICAL FOUR-TERM JOIN FAMILY GLOBALLY NONCOMPLETABLE; FULL PACKET OPEN.`

The one-transposition survivor does not remain a Sylvester-equality survivor
when two copies are joined in the natural four-term construction. This holds
both when the transpositions share a row and when they are disjoint. The
subpacket obstruction-monotonicity theorem now strengthens the conclusion:
these positive four-term defects cannot be repaired by any later term blocks.

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

Join two copies with identity weights `a` and `1-a`. For `a` different from
zero and one, their sum is exactly the identity-permutation monomial plus the
two selected transposition monomials. It contains four rank-seven Chow terms.

After normalizing the first factor line in (1.1), changing `a` only rescales
the slice-specific coordinate `u_ij` by `a^(-1)`; the remaining change is a
nonzero factor scaling. The two slices use distinct forward `U` coordinates,
so these are independent invertible diagonal ambient changes. Therefore the
three ranks of the joined complex are constant for every nonzero split
`a+(1-a)=1`. The frozen values `-1,1/3,1/2,2/3,2` provide exact rational
controls, not the basis of the all-weight conclusion.

## 2. Shared-row join

Use transpositions `(0 1)` and `(0 2)` in the common 11-variable space

```text
q0,...,q6,u01,u10,u02,u20.
```

The four middle blocks are assembled before any rank is taken. Exact rational
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

Hence the canonical disjoint join also violates Sylvester equality. The two
different defects show that shared-row overlap changes the coupled middle; the
result cannot be obtained by adding two copies of the one-slice ranks.

## 4. Subpacket monotonicity and global consequence

For a label subset `I`, define

\[
 \mathcal O_I
 =\ker B_I/(\ker B_I\cap\operatorname{im}C_I).
\]

If `I` is contained in a larger label set `J`, zero extension of the middle
coordinates induces an injection

\[
 \mathcal O_I\hookrightarrow\mathcal O_J.                         \tag{4.1}
\]

Indeed, if an old kernel vector extended by zero equals `C_Jx`, projection to
the old middle summands gives the same vector as `C_Ix`; it was already an old
boundary. Therefore a positive old obstruction can never become zero after
new term blocks are appended.

The eleven-variable computation remains valid inside the ambient 49-variable
system: restriction

\[
 \operatorname{Sym}^3(V^*)\longrightarrow\operatorname{Sym}^3(W^*)
\]

is surjective for the old eleven-variable subspace `W`, so enlarging the source
does not enlarge the old stacked `C` image.

Consequently every completion containing the exact shared-row join has defect
at least ten, and every completion containing the exact disjoint join has
defect at least twelve. Neither canonical join can occur inside a full
Sylvester-equality Packet B.

The earlier statement that additional terms might repair these defects is
superseded by the general theorem in
`docs/n7_b2_subpacket_obstruction_monotonicity.md`. The numerical rank payload
is unchanged.

## 5. Corrected next gate

This result still does not classify all possible four-term factorizations or
cross-slice graph couplings. A surviving realization of two transposition
slice targets must introduce cross-slice coupling already inside its four
terms and must have zero four-term obstruction. Later term blocks are
irrelevant once the four-term defect is positive.

The next smallest exact problem is therefore:

```text
classify zero-defect four-term cross-slice couplings
subject to U0Q7 identity, U1Q6 zero,
and two prescribed U2Q5 transposition targets.
```

Replay:

```text
python scripts/n7_b2_two_transposition_join_obstruction.py \
  --verify-json data/n7_b2_two_transposition_join_obstruction.json
python scripts/n7_b2_subpacket_obstruction_monotonicity.py \
  --verify-json data/n7_b2_subpacket_obstruction_monotonicity.json
python -m unittest tests.test_n7_b2_two_transposition_join_obstruction -v
python -m unittest tests.test_n7_b2_subpacket_obstruction_monotonicity -v
```
