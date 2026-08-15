# General-`n` route update after factor-span transversality

The exact product-shadow theorem computes the smallest possible derivative
shadow of an arbitrary permanent-derivative subspace. Factor-span
transversality now adds a Chow-realizability correction before any equality
classification is attempted.

For shadow degree `d`, any block of

\[
s\le\left\lfloor\frac{d^2-1}{n}\right\rfloor
\]

degree-`n` Chow terms has combined factor span dimension below `d^2` and is
therefore disjoint from `D_d(perm_n)`. In every fixed-term projection one may
omit such a block, replacing the literal capacity

\[
q\binom nd
\]

by

\[
(q-s)\binom nd.
\]

This converts the first Chow-specific geometric fact into a general arithmetic
improvement. The exact product-shadow instances give

```text
ChowRank(perm_7) >= 43
ChowRank(perm_8) >= 78
```

and the existing reviewed multishadow certificates for `n=9,...,16` improve
by one to three terms without changing their intersection witnesses.

The result remains below the scale needed for Glynn optimality. The next
high-value target is not a larger Ferrers dynamic program. It is a second
Chow-realizability correction for blocks whose combined factor span has just
reached the square threshold:

```text
dim(L)=d^2
```

At this boundary, torus-fixed intersections are complete `d x d` rectangles.
A useful next theorem would classify the full characteristic-zero equality
locus

\[
D_d(perm_n)\cap Sym^d(L)\ne0,
\qquad dim L=d^2,
\]

and then control simultaneous occurrence for several term blocks. Such a
classification could turn the current additive `n/4` saving into a larger
coupled correction. No state registry, solver framework, or generic orbit
manager is authorized before that equality theorem is stated.
