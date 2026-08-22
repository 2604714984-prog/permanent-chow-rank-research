# Even-order middle-symbol capacity ceiling

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_ROUTE_BARRIER`, `EXACT_INTEGER_REPLAYED`.

Let

\[
P_n=\operatorname{perm}_n
\]

over an algebraically closed field of characteristic zero, and suppose that
`n=2m` is even. Put

\[
c_n=\binom{n}{m}.
\]

This note extracts the reusable abstract skeleton of the repaired proof of

\[
\operatorname{ChowRank}(P_6)=32
\]

and determines its exact capacity for general even `n`.

The result is a ceiling on one proof architecture:

> a single middle catalecticant, the symmetric image-span inequality, one
> factor-span filtration, and a constant-slope local quotient-symbol estimate
> whose middle-rank defect cancels with coefficient `1/2`.

For every route of this form, the largest ordinary Chow-rank lower bound it can
certify is

\[
\boxed{
B_{\mathrm{mid}}(n)=\binom{n}{n/2}+2n.
}
\]

At `n=6`,

\[
B_{\mathrm{mid}}(6)=20+12=32=2^5,
\]

so the repaired `perm_6` proof exactly saturates the route capacity. For every
even `n>=8`,

\[
\boxed{
B_{\mathrm{mid}}(n)<2^{n-1}.
}
\]

Thus the `perm_6` argument does not scale to the general conjecture by improving
the constant in one middle-layer local lemma. A scalable continuation must
couple several derivative degrees, retain nonlinear relation data, or leave
this route class.

This theorem is not a Chow-rank upper bound, does not weaken any known lower
bound, and makes no border-rank claim.

## 1. The symmetric middle layer

Let

\[
P_n=T_1+\cdots+T_N
\]

be a hypothetical ordinary Chow decomposition, with every `T_i` a product of
`n` linear forms. Let

\[
A_i=C_{m,m}(T_i)
\]

be the symmetric middle catalecticant, viewed as a symmetric linear map. Put

\[
U_i=\operatorname{im}A_i,\qquad
u_i=\dim U_i,\qquad
\delta_i=c_n-u_i,\qquad
\Delta=\sum_i\delta_i.
\]

Since one degree-`n` Chow term has middle catalectic rank at most `c_n`, all
`delta_i` are nonnegative.

Let

\[
U=\sum_iU_i,\qquad
\dim U=c_n^2+h.
\]

The middle catalecticant of the permanent has rank and image dimension
`c_n^2`.

### Lemma 1.1 -- symmetric image-span inequality

For symmetric maps `A_i:W^*->W`, if

\[
D=\dim\sum_i\operatorname{im}A_i,
\]

then

\[
\operatorname{rank}\left(\sum_iA_i\right)
\ge
2D-\sum_i\operatorname{rank}A_i.
\]

### Proof

Choose maps `B_i:k^(r_i)->W` onto the images of `A_i`, where
`r_i=rank(A_i)`. Symmetry implies

\[
A_i=B_iJ_iB_i^*
\]

for an invertible symmetric map `J_i` on the rank quotient. With

\[
B=[B_1\ \cdots\ B_N],
\qquad
J=\operatorname{diag}(J_1,\ldots,J_N),
\]

Sylvester's rank inequality gives

\[
\operatorname{rank}(BJB^*)
\ge
\operatorname{rank}(BJ)+\operatorname{rank}(B^*)-\sum_i r_i
=
2D-\sum_i r_i.
\]

This proves the lemma.

Applying the lemma to the decomposition gives

\[
c_n^2
\ge
2(c_n^2+h)-(Nc_n-\Delta),
\]

hence

\[
\boxed{
h\le
\frac{Nc_n-c_n^2-\Delta}{2}.
}
\tag{1.1}
\]

This is the global upper half of the route.

## 2. Constant-slope quotient-symbol filtration

Let `L_i` be the actual factor span of `T_i`. Order the terms and define the
incremental quotient

\[
P_i:L_i\twoheadrightarrow
L_i/(L_i\cap(L_1+\cdots+L_{i-1})).
\]

Write

\[
d_i=\operatorname{rank}P_i.
\]

Because the permanent is concise in all `n^2` matrix variables, the factor
spans of the summands generate the full variable space. Therefore

\[
\boxed{
\sum_i d_i=n^2.
}
\tag{2.1}
\]

The route class considered here assumes a local quotient-symbol map
`beta_(T,P)` and a uniform constant `s>=0` such that, for every degree-`n`
Chow term `T` and every quotient `P` of its actual factor span,

\[
\boxed{
\operatorname{rank}\beta_{T,P}
+\frac{\delta(T)}2
\ge
s\,\operatorname{rank}P,
}
\tag{2.2}
\]

where

\[
\delta(T)=c_n-\operatorname{rank}C_{m,m}(T).
\]

It also assumes the factor filtration separates these local symbol images, so

\[
h\ge\sum_i\operatorname{rank}\beta_{T_i,P_i}.
\]

Equations (2.1)--(2.2) then give

\[
\boxed{
h\ge sn^2-\frac{\Delta}{2}.
}
\tag{2.3}
\]

Comparing (1.1) and (2.3) cancels the complete termwise middle-rank defect:

\[
sn^2-\frac{\Delta}{2}
\le
\frac{Nc_n-c_n^2-\Delta}{2}.
\]

Thus every decomposition must satisfy

\[
\boxed{
N\ge c_n+\frac{2sn^2}{c_n}.
}
\tag{2.4}
\]

The repaired `perm_6` proof is exactly of this form, with `c_6=20` and
`s=10/3`.

## 3. The full-rank test term forces the slope ceiling

Take the independent Chow term

\[
T_0=z_1\cdots z_n.
\]

Its actual factor span has dimension `n`, and its middle derivative space has
dimension exactly

\[
\operatorname{rank}C_{m,m}(T_0)=c_n.
\]

Hence

\[
\delta(T_0)=0.
\]

Apply (2.2) to the full quotient

\[
P=\operatorname{id}_{L(T_0)},
\qquad
\operatorname{rank}P=n.
\]

The domain of every middle quotient-symbol map in this route is contained in
the `c_n`-dimensional middle derivative space of `T_0`. Consequently,

\[
\operatorname{rank}\beta_{T_0,P}\le c_n.
\]

Equation (2.2) therefore forces

\[
sn\le c_n,
\]

or

\[
\boxed{
s\le\frac{c_n}{n}.
}
\tag{3.1}
\]

Substituting (3.1) into (2.4), the largest lower bound available to the route is

\[
\boxed{
B_{\mathrm{mid}}(n)
=
c_n+2n
=
\binom{n}{n/2}+2n.
}
\tag{3.2}
\]

The argument uses a full-rank term with zero defect, so adding a more generous
nonnegative defect bonus cannot evade the ceiling. The only escape is to use
information not represented by one constant-slope middle symbol.

## 4. Exact comparison with Glynn

Write `n=2m`. The normalized route ratio is

\[
\frac{B_{\mathrm{mid}}(2m)}{2^{2m-1}}
=
\frac{2\binom{2m}{m}}{4^m}
+
\frac{8m}{4^m}.
\tag{4.1}
\]

Both summands decrease with `m`:

\[
\frac{\binom{2m+2}{m+1}/4^{m+1}}
     {\binom{2m}{m}/4^m}
=
\frac{2m+1}{2m+2}<1,
\]

and

\[
\frac{(m+1)/4^{m+1}}{m/4^m}
=
\frac{m+1}{4m}<1.
\]

At `m=4`,

\[
B_{\mathrm{mid}}(8)=70+16=86<128=2^7.
\]

Therefore (4.1) remains strictly below one for every `m>=4`, proving

\[
\boxed{
\binom{n}{n/2}+2n<2^{n-1}
\qquad
\text{for every even }n\ge8.
}
\tag{4.2}
\]

At the preceding even order,

\[
\binom63+12=20+12=32=2^5.
\]

Thus `n=6` is the final even order, and the unique even order at least six,
where this route capacity meets the conjectural Glynn value exactly.

By the central-binomial asymptotic,

\[
\binom{n}{n/2}
=
2^n\sqrt{\frac{2}{\pi n}}\,(1+o(1)),
\]

so

\[
\boxed{
\frac{B_{\mathrm{mid}}(n)}{2^{n-1}}
=
\sqrt{\frac{8}{\pi n}}\,(1+o(1)).
}
\tag{4.3}
\]

The route loses an unbounded factor of order `sqrt(n)`.

## 5. Quantified coupling deficit

Define

\[
G_n
=
2^{n-1}
-
\left(\binom{n}{n/2}+2n\right)
\qquad(n\ge8,\ n\text{ even}).
\]

This is the number of rank units missing from the route ceiling. In the
normalization of (1.1), a successful replacement must supply at least

\[
\boxed{
\Xi_n=\frac{c_nG_n}{2}
}
\tag{5.1}
\]

additional global symbol charge beyond the best constant-slope middle-layer
comparison.

The first values are

```text
n=8:   G_n=42,    Xi_n=1,470
n=10:  G_n=240,   Xi_n=30,240
n=12:  G_n=1,100, Xi_n=508,200
```

These values are not new Chow-rank lower bounds. They are exact promotion
thresholds for a coupled replacement: a proposed multi-degree module should
demonstrate where this additional charge comes from and why its one-term cap
does not grow by the same amount.

## 6. Research consequence

The following continuations are now closed as routes to the general conjecture:

```text
same middle degree with a sharper constant-slope local lemma
same symmetric image-span upper bound
same one-pass factor filtration
same half-defect cancellation
```

The next theorem-bearing object must retain information discarded by this
architecture. The narrowest candidate is a genuinely coupled two-degree
quotient-symbol module, beginning with the two adjacent middle degrees and
their common differentiation relations. Direct block-diagonal stacking is not
enough; it must strictly reduce the joint one-term cap.

## 7. Claim boundary

```text
general exact ChowRank(perm_n)=2^(n-1)        OPEN
new ordinary Chow-rank lower bound             NO
new border-rank lower bound                     NO
single-middle constant-slope route             CLOSED AT c_n+2n
perm_6 exact proof                              EXPLAINS SATURATION ONLY
multi-degree coupled quotient symbols           OPEN
nonlinear relation modules                      OPEN
literature novelty                              NOT ESTABLISHED
```

## 8. Reproduction

```bash
python scripts/general_even_middle_symbol_capacity_ceiling.py \
  --verify-json data/general_even_middle_symbol_capacity_ceiling.json

python scripts/general_even_middle_symbol_capacity_ceiling_independent.py \
  --max-n 64

python -m unittest \
  tests.test_general_even_middle_symbol_capacity_ceiling -v
```

Expected markers:

```text
GENERAL_EVEN_MIDDLE_SYMBOL_CAPACITY_CEILING_PASS
GENERAL_EVEN_MIDDLE_SYMBOL_CAPACITY_CEILING_INDEPENDENT_PASS
```
