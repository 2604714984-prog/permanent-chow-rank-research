# Prolongation pruning of the near-extremal fixed-six layers

**Status.** `PURE_STATE_EXCLUSION`, `EXACT_INTEGER_REPLAY`,
`PARTIAL_LOWER_27_PROGRESS` (N6-046).  The base field is algebraically closed
of characteristic zero.  This note excludes 21 canonical scalar states from
the N6-041 layers `b=61,62,63`.  It does not exclude any complete layer or
prove `ChowRank(perm_6)>=27`.

## 1. Common-quotient criterion

Retain the N6-041 notation

\[
 E_m=\mathcal D_m(\operatorname{perm}_6),\qquad
 H_m=\mathcal D_m(T_1+\cdots+T_6),\qquad
 F_i=\mathcal D_2(T_i).
\]

N6-041 proves

\[
 H_2=F_1+\cdots+F_6.
\tag{1.1}
\]

Consider a scalar state with

\[
 t_2=\dim((E_2+H_2)/E_2)=12
\tag{1.2}
\]

and at least one index `i` satisfying

\[
 (\varepsilon_i,\alpha_i)=(0,0).
\tag{1.3}
\]

Here `alpha_i=0` gives a three-dimensional permanent intersection.  By
N6-043, a factor span of dimension at most five has permanent quadratic
intersection of dimension at most one.  Thus the factor span has dimension
six, so `F_i` is the quadratic derivative space of an independent extremal
six-factor Chow term.  In particular,

\[
 \dim F_i=15,
 \qquad \dim(E_2\cap F_i)=3,
 \qquad \dim q(F_i)=12,
\tag{1.4}
\]

where `q` is the quotient by `E_2`.  Equation (1.1) gives
`q(F_i)\subseteq q(H_2)`, while both sides have dimension twelve by
(1.2)--(1.4).  Hence

\[
 q(F_i)=q(H_2),
 \qquad
 \boxed{E_2+F_i=E_2+H_2=:A}.
\tag{1.5}
\]

## 2. Prolongation contradiction

Every first derivative of `E_3` lies in `E_2`, and every first derivative of
`H_3` lies in `H_2`.  Therefore (1.5) implies

\[
 E_3+H_3\subseteq A^{(1)}.
\tag{2.1}
\]

Writing

\[
 b=\dim(E_3\cap H_3),
 \qquad h=\dim H_3,
\]

we obtain

\[
 \dim A^{(1)}\ge \dim(E_3+H_3)=400+h-b.
\tag{2.2}
\]

N6-044 proves the universal extremal-frame bound

\[
 \dim(E_2+F_i)^{(1)}\le436.
\tag{2.3}
\]

For the N6-041 states under consideration, (2.2) is at least `457`:

\[
\begin{array}{c|c|c}
b&h&400+h-b\\ \hline
61&118\text{ or }120&457\text{ or }459\\
62&120&458\\
63&120&457.
\end{array}
\tag{2.4}
\]

Equations (2.3)--(2.4) contradict one another.  Thus every N6-041 scalar
state satisfying (1.2)--(1.3) is impossible.

## 3. Exact pruning table

The replay preserves the exact sorted order of the frozen N6-041 state table
and assigns identifiers `N6-041-Bb-Snnn`.  It gives

\[
\begin{array}{c|c|c|c}
b&\text{N6-041 states}&\text{excluded}&\text{remaining}\\ \hline
61&73&13&60\\
62&11&4&7\\
63&11&4&7.
\end{array}
\tag{3.1}
\]

The frozen JSON records every excluded and retained identifier.  The excluded
identifiers are:

```text
b=61: N6-041-B61-S003 N6-041-B61-S005 N6-041-B61-S006
      N6-041-B61-S012 N6-041-B61-S013 N6-041-B61-S015
      N6-041-B61-S016 N6-041-B61-S018 N6-041-B61-S019
      N6-041-B61-S020 N6-041-B61-S029 N6-041-B61-S030
      N6-041-B61-S031
b=62: N6-041-B62-S002 N6-041-B62-S003 N6-041-B62-S005
      N6-041-B62-S006
b=63: N6-041-B63-S002 N6-041-B63-S003 N6-041-B63-S005
      N6-041-B63-S006
```

These are exclusions of canonical **scalar states**.  None of the retained
states is asserted to be geometrically realizable, and the counts do not
exclude an entire `b` layer, a hypothetical 26-term decomposition, or border
Chow rank.

## 4. Replay

Run

```text
python scripts/n6_near_extremal_prolongation_pruning.py \
  --json data/n6_near_extremal_prolongation_pruning.json
python -m unittest tests/test_n6_near_extremal_prolongation_pruning.py -v
```

Expected output includes

```text
b=61 excluded=13 remaining=60
b=62 excluded=4 remaining=7
b=63 excluded=4 remaining=7
N6_NEAR_EXTREMAL_PROLONGATION_PRUNING_PASS
```
