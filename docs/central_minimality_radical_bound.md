# Central minimality forces a small relation-pairing radical

## Status and scope

`PROOF_DRAFT_COMPLETE`.

This is an elementary characteristic-zero consequence of the exact central
pairing identity.  It applies when the middle catalecticant itself certifies
the length of a Chow decomposition.  It does not apply merely because a
decomposition is minimum for some other reason.

## 1. Linear-algebra statement

Let `A_1,...,A_q:X -> X^*` be symmetric linear maps over a field of
characteristic different from two, and assume

\[
 \operatorname{rank}A_i\le B
 \quad(1\le i\le q).
\]

Put `U_i=im A_i` and

\[
 R=\ker\left(\bigoplus_iU_i\longrightarrow\sum_iU_i\right),
 \qquad \rho=\dim R.
\]

Each `A_i` induces a nondegenerate symmetric form `beta_i` on `U_i`.  Let
`beta=direct_sum_i beta_i` and set

\[
 \delta=\dim\operatorname{rad}(\beta|_R).
\]

### Theorem 1.1

If

\[
 \operatorname{rank}\left(\sum_{i=1}^qA_i\right)>(q-1)B,
\]

then

\[
 \boxed{
 \rho+\delta<B,
 \qquad
 \delta\le\left\lfloor\frac{B-1}{2}\right\rfloor.
 }
\]

### Proof

Write

\[
 C=\sum_i\operatorname{rank}A_i\le qB.
\]

The exact central relation-pairing identity from
`docs/general_relation_tableau_pairing.md` is

\[
 \operatorname{rank}\left(\sum_iA_i\right)
 =C-2\rho+\operatorname{rank}(\beta|_R).
\]

Since `rank(beta|_R)=rho-delta`, this is

\[
 \operatorname{rank}\left(\sum_iA_i\right)=C-\rho-\delta.
\]

Therefore

\[
 (q-1)B<C-\rho-\delta\le qB-\rho-\delta,
\]

which gives `rho+delta<B`.  Finally `delta<=rho`, so

\[
 2\delta\le\rho+\delta<B.
\]

The asserted integer bound follows.  This proves the theorem.

## 2. Chow consequence

For a degree-`2m` Chow term, the middle catalecticant has rank at most

\[
 B_m=\binom{2m}{m}.
\]

Suppose a polynomial `f` is displayed as a sum of `q` such terms and

\[
 \operatorname{rank}C_{m,m}(f)>(q-1)B_m.
\]

Subadditivity excludes every expression with at most `q-1` terms, so the
displayed expression is minimum.  Theorem 1.1 simultaneously gives

\[
 \delta\le
 \left\lfloor\frac{\binom{2m}{m}-1}{2}\right\rfloor.  \tag{2.1}
\]

For sextics, `m=3` and `B_3=20`, hence

\[
 \boxed{\delta\le9.}                              \tag{2.2}
\]

In particular, for `q>=4`,

\[
 \delta\le9<4(q-1).
\]

The coordinate three-term theorem in
`docs/degree6_three_monomial_radical_classification.md` closes the remaining
one-unit gap in that restricted family, improving nine to the sharp value
eight.

## 3. Research boundary

The theorem explains why a counterexample to a minimum-decomposition radical
cap cannot be found among decompositions whose length is already certified by
the same middle catalecticant.  Any counterexample must have

\[
 \operatorname{rank}C_{m,m}(f)\le(q-1)B_m
\]

and require a different invariant, such as a Koszul flattening, to certify its
minimum length.

The six-term example in
`docs/general_relation_radical_counterexample.md` lies exactly outside the
hypothesis: its middle rank is 50, far below the five-term sextic cap 100.
Thus it disproves an unconditional presentation-wise cap without contradicting
Theorem 1.1.
