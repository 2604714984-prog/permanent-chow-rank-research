# Intrinsic arbitrary-mixed Packet-B complex

## Status

`B2-01--B2-04 EXECUTED; B2-05 UNDERDETERMINED ON THE EQUALITY LOCUS.`

This note supplies the missing basis-level definition of the mixed
Sylvester complex.  It also identifies the extra synchronization needed
before an arbitrary mixed packet can be represented by one degree-three/four
point code.  It does not replace the Sylvester condition by degree-six target
containment.

## 1. Intrinsic labelled packet

Let

\[
 V=U_0\oplus\cdots\oplus U_6\oplus Q,
 \qquad \dim U_a=6,\quad\dim Q=7.
\]

The seven direct terms have factor spans `U_a`.  Retain their seven labelled
factors

\[
 \ell_{a,r}=\sum_{s=1}^6 f_{a,r,s}u_{a,s},
 \qquad r=0,\ldots,6,
\]

including the scalar coefficient of the term in one labelled factor.  At the
slope-ten equality endpoint their factor multisets have the `s=1` or `s=2`
rank-six normal form, but the construction below needs no normalization.

For each of the 42 rank-seven terms choose a quotient frame
`q_{t,0},...,q_{t,6}` of `Q`, an independent graph map

\[
 A_t:Q\longrightarrow U_0\oplus\cdots\oplus U_6,
\]

and seven labelled factors

\[
 \ell_{t,r}=q_{t,r}+A_tq_{t,r}.
\]

Individual factor scalings whose product is the Chow coefficient are retained;
they are not silently identified between different terms.  Thus the quotient
frames, the 42 graph maps, the factor labels, and the coefficients are all
independent data.

## 2. The mixed Sylvester complex

For any term `T_i=product_{r=0}^6 ell_{i,r}`, put

\[
 \widehat K_i=k\langle e_{i,I}:I\subset\{0,\ldots,6\},\ |I|=4\rangle.
\]

There are 35 labelled generators.  Define

\[
 \widehat B_i(e_{i,I})=\prod_{r\in I}\ell_{i,r}
 \quad\hbox{and}\quad
 \widehat C_i(\theta)=
 \sum_{|I|=4}\theta\!\left(\prod_{r\notin I}\ell_{i,r}\right)e_{i,I}.
 \tag{2.1}
\]

The pairing uses divided-power cubic coordinates, so no hidden factorials
occur.  Put `A_i=widehat B_i widehat C_i`.  The intrinsic middle space is the
minimal rank space of this rectangular catalectic:

\[
 K_i=\operatorname{im}\widehat C_i/
 (\operatorname{im}\widehat C_i\cap\ker\widehat B_i),
 \qquad A_i=B_iC_i,                                \tag{2.2}
\]

where `B_i C_i` is any minimal rank factorization.  This distinction is
essential for the `s=2` rank-six normal form: `rank(widehat B_i)=31` and
`rank(widehat C_i)=29`, but their product has rank 25.  Thus quotienting all
of `widehat K_i` by `ker(widehat B_i)` gives the wrong middle space.  For
`s=1` the three ranks are `25,25,25`, and for a rank-seven term they are
`35,35,35`.  Hence the minimal mixed middle has

\[
 \dim K=7\cdot25+42\cdot35=1645.
\]

The actual global maps are

\[
 B=[B_1\ \cdots\ B_{49}]:\bigoplus_iK_i\to\operatorname{Sym}^4V,
 \qquad
 C=(C_1,\ldots,C_{49})^{\mathsf T}:\operatorname{Sym}^3V^*\to\bigoplus_iK_i.
 \tag{2.3}
\]

Rectangular Sylvester equality is precisely

\[
 \boxed{\ker B\subseteq\operatorname{im}C}.        \tag{2.4}
\]

This formula is invariant under factor relabelling, bases of `V`, and bases
of every `K_i`: those operations conjugate the displayed matrices but do not
change the subspace inclusion.

## 3. Mixed target integrability

The two local labelled relation spaces and the invisible overlap are

\[
 R^{\rm out}_{i,4}=\ker\widehat B_i,
 \quad R^{\rm in}_{i,3}=\ker\widehat C_i,
 \quad J_i=\operatorname{im}\widehat C_i\cap\ker\widehat B_i.
\]

They depend on the seven factors of term `i`; they are not relation spaces of
a shared evaluation code.  Mixed-partial compatibility of the permanent target
is the basis-free identity

\[
 \sum_i B_iC_i=C_{3,4}(\operatorname{perm}_7).      \tag{3.1}
\]

Equality adds (2.4).  Equivalently, the intrinsic mixed obstruction is

\[
 \mathcal O_B=\ker B/(\ker B\cap\operatorname{im}C).\tag{3.2}
\]

Sylvester equality says `O_B=0`.  Changing a local lift in
`im(widehat C_i)` changes it by `J_i` and hence cannot be compared across
terms until (3.1) and (2.4) are imposed.  These two global
conditions may transport relations between different `K_i`, but neither one
by itself identifies quotient frames, graph maps, or local relation spaces.
In particular, containment of the degree-six permanent rows in a span of
sixth powers is a separate necessary condition and says nothing by itself
about (2.4).

## 4. Exact domain of the common-code morphism

Fix a reference frame of `Q`.  A common point-code description requires more
than the fact that every rank-seven plane complements `U`:

1. every quotient frame differs from the reference frame by a monomial
   matrix (permutation and nonzero rescaling of the seven factor lines);
2. after relabelling, `A_t(q_r)` lies in the matching block `U_r`;
3. after fixed identifications `U_r isomorphic to W`, the seven matching
   vectors determine the same projective tail point, with factor scalings
   carried by the term weight.

The executable convention in item 3 requires all seven tails to be nonzero.
Each is normalized by dividing by its first nonzero coordinate, and the seven
normalized vectors must be equal.  Thus identical tails and nonzero scalar
multiples agree, `e_0` and `e_1` disagree, and a zero tail is rejected rather
than assigned an artificial projective point.

Only on this synchronized sublocus is there a canonical morphism to a shared
degree-three/four evaluation code.  A general `GL(Q)` change of a quotient
frame cannot be absorbed by factor relabelling: a product of seven linear
forms is preserved only by a monomial change of its seven factor lines.

Three frozen single-plane controls isolate the three requirements.  First,
inside one legal rank-seven complement plane, replace its seven factor lines by
the sheared quotient frame `I+E_{0,1}`.  The plane is unchanged and remains a
legal complement, although its Chow product changes.  Second, use one legal
complement given by a graph map with an off-diagonal entry `Q_0 -> U_1`.
Third, use one
block-diagonal graph whose seven normalized diagonal tails do not define the
same tail point.  This last control has synchronized frames and block support
but still has no common-code morphism.

These are replacements of one factor frame or one plane.  No generic
completion to a legal 42-plane packet is supplied, and they do not instantiate
42 terms of a permanent identity.  Simultaneous basis change on `Q` does not alter a
relative transition matrix; factor permutations and scalings multiply it on
the two sides by monomial matrices and cannot make it monomial.

Together they falsify a canonical common-code reduction on one arbitrary
complement.  They do not prove the same statement for complete 42-plane
geometry and do not form a counterexample satisfying the permanent identity
and (2.4).
Consequently B2-05 remains unresolved on the equality locus.  No formula in
the present package determines whether (3.1) and (2.4) force the three
synchronization conditions above; asserting that implication would be an
additional theorem, not a basis choice.  The next valid
gate is to impose the permanent equations and (2.4) on these residual frame,
off-block, and diagonal-mismatch moduli; it is not another point-code scan.

Replay:

```text
python scripts/n7_b2_intrinsic_mixed_complex.py \
  --verify-json data/n7_b2_intrinsic_mixed_complex.json
python -m unittest tests.test_n7_b2_intrinsic_mixed_complex -v
```
