# Universal prolongation caps for `alpha=1` terms

**Status.** `PURE_PROJECTIVE_CLOSURE_THEOREM`,
`EXACT_STATE_PRUNING`, `B62_B63_EXCLUDED` (N6-048). The base field is
algebraically closed of characteristic zero. This note combines its new
`alpha=1` theorem with N6-047. It excludes the complete `b=62` and `b=63`
layers and leaves one canonical state at `b=61`. It does not prove
`ChowRank(perm_6)>=27`.

Put

\[
 E_2=\mathcal D_2(\operatorname{perm}_6),
 \qquad q:\operatorname{Sym}^2V\longrightarrow
 \operatorname{Sym}^2V/E_2.
\]

## 1. The projective incidences

Let

\[
 T=\ell_1\cdots\ell_6,
 \qquad L=\langle\ell_1,\ldots,\ell_6\rangle,
 \qquad F=\mathcal D_2(T)
\]

be an actual term with

\[
 (\varepsilon,\alpha)=(0,1).
\tag{1.1}
\]

Thus `dim F=15` and `dim(E_2 cap F)=2`. N6-043 proves that a space of
dimension at most five has permanent quadratic intersection of dimension at
most one. Since

\[
 E_2\cap F\subseteq E_2\cap\operatorname{Sym}^2L,
\]

the factor span has dimension six and the factors are independent.

For `t in {13,14}`, consider every quadratic space

\[
 A\in\operatorname{Gr}(225+t,\operatorname{Sym}^2V),
 \qquad E_2+F\subseteq A.
\tag{1.2}
\]

Let `Y_(1,t)` be the closure of the resulting triples `(L,F,A)` in the
product of the corresponding three Grassmannians. It is projective and
row-column-torus stable. The closed incidences

\[
 F\subseteq\operatorname{Sym}^2L,
 \qquad F\subseteq A,
 \qquad E_2\subseteq A
\tag{1.3}
\]

and the closed rank condition

\[
 \dim(E_2\cap F)\ge2,
 \qquad
 \dim(E_2\cap\operatorname{Sym}^2L)\ge2
\tag{1.4}
\]

hold everywhere on `Y_(1,t)`. The dimension `dim A=225+t` stays constant by
construction. Notice that (1.2) is only a containment; it allows the one
extra quotient direction needed when `t=14`.

## 2. Fixed boundary classification

For a quadratic space `A`, its first prolongation is

\[
 A^{(1)}=\{g\in\operatorname{Sym}^3V:
 \partial_\xi g\in A\text{ for all }\xi\in V^*\}.
\]

The function `dim A^(1)` is the kernel dimension of a vector-bundle map and
is upper semicontinuous. Its maximum locus on the projective torus-stable
variety `Y_(1,t)` contains a torus fixed point. It therefore suffices to
bound every fixed triple.

At such a point, `L` is coordinate. Its six-edge bipartite graph has at least
two rectangles by (1.4). N6-043 proves that their union must use six edges
and be `K_(2,3)` or `K_(3,2)`; a six-edge graph containing that union equals
it. Hence

\[
 Q_L:=E_2\cap\operatorname{Sym}^2L,
 \qquad \dim Q_L=3.
\tag{2.1}
\]

Because `F subset Sym^2 L`, upper semicontinuity from the actual intersection
dimension two and (2.1) give

\[
 2\le r:=\dim(E_2\cap F)\le3.
\tag{2.2}
\]

There are two cases.

### Case `r=2`

The torus-fixed space `q(F)` is a thirteen-subset of the eighteen local
one-dimensional quotient weights in `q(Sym^2L)`. The fixed `t`-plane `A/E_2`
contains it. Thus for `t=13` it equals `q(F)`; for `t=14` it adds one
arbitrary ambient quotient weight.

N6-047 includes every such possibility. Indeed, select any twelve of the
thirteen local weights as its local `W_12`, use the thirteenth as the first
extra axis, and for `t=14` use the arbitrary ambient direction as the second
extra axis. If that second direction is also local, this simply selects a
fourteen-subset of the same eighteen axes and is still included.

### Case `r=3`

Here `E_2 cap F=Q_L`; hence `q(F)` is one of the twelve-axis fixed extremal
quotients of N6-047. The space `A/E_2` adds one arbitrary ambient quotient
weight for `t=13`, or two for `t=14`. These are precisely the other fixed
incidences enumerated by N6-047.

Its exact modular rank certificate is used only as a characteristic-zero
upper bound and gives in the two cases

\[
 \boxed{
 \dim A^{(1)}\le
 \begin{cases}
 440,&t=13,\\
 448,&t=14.
 \end{cases}}
\tag{2.3}

The projective maximum argument proves:

### Theorem 2.1 -- universal `alpha=1` caps

For every actual term with `(epsilon,alpha)=(0,1)` and every `A` satisfying
(1.2), the bounds (2.3) hold. No classification of the irreducible
components of the general `alpha=1` locus is required.

## 3. Exact state pruning

For a fixed-six state, put

\[
 \mathcal A=E_2+H_2,
 \qquad t_2=\dim(\mathcal A/E_2).
\]

If a fixed term has `(epsilon,alpha)=(0,1)`, then
`E_2+F_i subseteq mathcal A`. For `t_2=13` or `14`, Theorem 2.1 applies to
`mathcal A`. On the other hand,

\[
 E_3+H_3\subseteq\mathcal A^{(1)},
 \qquad
 \dim\mathcal A^{(1)}\ge400+h-b\ge457.
\tag{3.1}

This contradicts the applicable cap `440` or `448`. Thus every such state is
impossible. N6-047 already excludes every state containing an extremal
`(0,0)` term.

Applying these two theorems to the frozen N6-041 table gives

\[
\begin{array}{c|c|c|c}
b&\text{N6-041 states}&\text{excluded}&\text{remaining}\\ \hline
61&73&72&1\\
62&11&11&0\\
63&11&11&0.
\end{array}
\tag{3.2}

The sole survivor, using the zero-based N6-047 identifiers, is

```text
b61_state_072
```

It has `t_2=14` and all six pairs equal `(epsilon,alpha)=(0,2)`. In
particular, neither N6-047 nor Theorem 2.1 applies to it.

Consequently the complete `b=62` and `b=63` layers are impossible. The result
remains conditional on the fixed-six reduction of a hypothetical
twenty-six-term decomposition. The all-`alpha=2` state at `b=61` remains, so
this note does not prove lower 27 and makes no border-rank claim.

## 4. Replay

The script performs no new rank calculation. It checks the exact N6-041
states against the frozen N6-047 caps and records the complete partition.

```text
python scripts/n6_alpha1_prolongation_closure.py \
  --json data/n6_alpha1_prolongation_closure.json
python -m unittest tests.test_n6_alpha1_prolongation_closure -v
```
