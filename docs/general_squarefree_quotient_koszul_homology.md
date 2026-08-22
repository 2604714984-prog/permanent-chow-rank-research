# Exact first Koszul homology cap for squarefree quotient symbols

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_EXACT_LOCAL_THEOREM`,
`FIRST_GENUINE_RELATION_QUOTIENT`, `EXACT_SPARSE_REPLAYED`.

Let `F` be an `n`-dimensional vector space with factor basis
`z_1,...,z_n`, and let `Sq^k(F)` be the squarefree degree-`k` derivative
space of the independent Chow term

\[
T_0=z_1\cdots z_n.
\]

For a rank-`d` quotient `P:F->D`, consider the two-step quotient-symbol
complex

\[
\operatorname{Sq}^{k+1}(F)
\xrightarrow{\partial_0}
D\otimes\operatorname{Sq}^{k}(F)
\xrightarrow{\partial_1}
\bigwedge^2D\otimes\operatorname{Sq}^{k-1}(F),
\tag{0.1}
\]

where

\[
\partial_0(z_I)
=
\sum_{i\in I}P(z_i)\otimes z_{I\setminus\{i\}},
\]

and

\[
\partial_1(y\otimes z_I)
=
\sum_{i\in I}y\wedge P(z_i)\otimes z_{I\setminus\{i\}}.
\]

The composite is zero.  Put

\[
H^1_{n,k}(P)=\ker\partial_1/\operatorname{im}\partial_0.
\]

The exact uniform cap is

\[
\boxed{
\max_{\operatorname{rank}P=d}
\dim H^1_{n,k}(P)
=
d\binom{n-d}{k-1}.
}
\tag{0.2}
\]

Every coordinate quotient attains equality.  Consequently,

\[
\boxed{
\max_P
\left(
\dim H^1_{n,k}(P)+\dim H^1_{n,k+1}(P)
\right)
=
d\binom{n-d+1}{k},
}
\tag{0.3}
\]

and across all positive degrees,

\[
\boxed{
\max_P\sum_{k=1}^n\dim H^1_{n,k}(P)
=
d2^{n-d}.
}
\tag{0.4}
\]

This is the first exact non-block-diagonal relation quotient in the
post-`perm_6` program.  It supplies a uniform cap for the independent
full-factor term, but not yet for arbitrary repeated or dependent factors.
No permanent-side homology or Chow-rank lower bound is claimed.

## 1. Upper semicontinuity reduces the maximum to a coordinate quotient

A rank-`d` quotient is determined, up to a change of basis in `D`, by its
kernel

\[
K\in\operatorname{Gr}(n-d,F).
\]

The dimensions of all three vector spaces in (0.1) are fixed.  In local
Grassmannian coordinates, the two differentials are matrices whose entries
are regular functions of `K`.  Therefore

\[
\dim H^1_{n,k}(P)
=
\dim(D\otimes\operatorname{Sq}^kF)
-
\operatorname{rank}\partial_0
-
\operatorname{rank}\partial_1
\]

is upper semicontinuous.

Its maximum locus is a nonempty closed subvariety of the Grassmannian and is
invariant under the diagonal torus preserving the squarefree spaces.  The
Borel fixed-point theorem gives a torus-fixed kernel in this locus.  Every
such kernel is coordinate.  Hence the maximum is attained by a coordinate
quotient.

It remains only to compute one coordinate quotient exactly.

## 2. Coordinate support decomposition

Let `P` project onto the first `d` factor coordinates.  Call these coordinates
active and the remaining `n-d` coordinates passive.

Fix a passive subset `J` and an active support `S`.  The middle basis vectors
split into two disjoint types.

### 2.1 Off-diagonal type

The distinguished active output label is not contained in the squarefree
monomial.  For fixed `(S,J)`, the relevant piece of (0.1) is

\[
k
\longrightarrow
k^S
\longrightarrow
\bigwedge^2 k^S,
\]

with

\[
1\longmapsto(1,\ldots,1),
\qquad
(v_a)_{a\in S}
\longmapsto
(v_a-v_b)_{a<b}.
\]

The kernel of the second map is the constant line, exactly the image of the
first.  Thus every off-diagonal piece is exact.

### 2.2 Diagonal type

The distinguished active output label is already contained in the monomial.
If `|S|>=2`, each middle basis vector has an output coordinate in the second
map that no other middle basis vector uses.  Hence the second map is
injective on that piece.

If `|S|=1`, the second map is zero and there is no incoming off-diagonal
source.  This produces one homology class for every choice of

```text
one active label              d choices
one passive (k-1)-subset      C(n-d,k-1) choices.
```

Therefore

\[
\dim H^1_{n,k}(P)
=
d\binom{n-d}{k-1},
\]

proving (0.2).

## 3. Adjacent and all-degree caps

The same coordinate quotient maximizes every degree simultaneously.  Thus
summing two adjacent instances of (0.2) and using Pascal's identity gives

\[
d\binom{n-d}{k-1}
+
d\binom{n-d}{k}
=
d\binom{n-d+1}{k},
\]

which proves (0.3).

Summing over all `k=1,...,n` gives

\[
\sum_{k=1}^n d\binom{n-d}{k-1}
=
d2^{n-d},
\]

proving (0.4).

The all-degree cap is largest at `d=1` or `d=2`, where it equals

\[
2^{n-1}.
\]

This equality is a one-term local capacity, not a permanent lower bound.  A
valid global invariant still needs a permanent-side value and monotonicity or
subadditivity under Chow sums.

## 4. Research consequence

The two-step relation quotient does create real compression relative to the
raw block-diagonal symbols, and its exact independent-term cap is now known.
The remaining load-bearing questions are:

1. does a uniform version survive repeated and dependent factors;
2. what is the corresponding permanent-side homology;
3. is the construction monotone under the subquotients created by a Chow sum;
4. can the resulting ratio reach or exceed the current lower bounds.

The next executable task is the degenerate-term stress test.  It should begin
with the one-relation normal forms

\[
x_1\cdots x_{n-1}(x_1+\cdots+x_s),
\]

rather than a generic solver or full parameter sweep.

## 5. Claim boundary

```text
independent full-factor Chow term                 EXACT
arbitrary factor quotient                        EXACT
coordinate quotient equality                     EXACT
repeated/dependent Chow terms                     OPEN
permanent-side relation homology                  OPEN
sum/subquotient inequality                        OPEN
new ordinary Chow-rank lower bound                NO
new border-rank lower bound                       NO
general Glynn optimality                          OPEN
literature novelty                                NOT ESTABLISHED
```
