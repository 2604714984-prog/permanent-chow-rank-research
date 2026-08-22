# N7-007: recursive shadow tower gives ordinary lower 46

## Result

Over characteristic zero,

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge 46.
\]

This is an ordinary-rank statement.  It neither proves border rank 46 nor
identifies the exact ordinary rank, whose current interval is \([46,64]\).

## The quotient lemma

For subspaces \(E,A,B\) of one ambient space, the map

\[
E\cap(A+B)\longrightarrow (A+B)/A
\]

has kernel \(E\cap A\).  Consequently

\[
\dim(E\cap(A+B))
\le \dim(E\cap A)+\dim B-\dim(A\cap B)
\le \dim(E\cap A)+\dim B.                 \tag{1}
\]

Thus internal relations and cross relations can only improve every bound
below; no literal-directness hypothesis is being used.

## The recursive tower

Write \(E_r=D_r(\operatorname{perm}_7)\), and for a Chow term \(T_i\) write

\[
G_i=D_1(T_i),\qquad F_i=D_2(T_i),\qquad U_i=D_3(T_i).
\]

Their dimensions are at most \(7,21,35\), including terms with repeated or
dependent factors.

Choose two terms and put \(K_2=E_2\cap(F_1+F_2)\).  Differentiation gives

\[
\partial K_2\subseteq G_1+G_2,qquad \dim\partial K_2\le14.
\]

The exact two-dimensional Ferrers calculation for the \(r=2\) product shadow
has capacity 22 at budget 14.  Hence \(\dim K_2\le22\).  Adding three more
quadratic spaces through (1) gives

\[
\dim\left(E_2\cap\sum_{i=1}^{5}F_i\right)
\le22+3\cdot21=85.                         \tag{2}
\]

Now put \(K_3=E_3\cap\sum_{i=1}^{5}U_i\).  Its derivative shadow is contained
in the left side of (2).  The exact \(r=3\) product-shadow capacity at budget
85 is 64, so \(\dim K_3\le64\).  Adding fifteen more cubic spaces gives

\[
\dim\left(E_3\cap\sum_{i=1}^{20}U_i\right)
\le64+15\cdot35=589.                       \tag{3}
\]

For the twenty selected terms \(R\), let
\(S=E_4\cap D_4(R)\).  Differentiation and (3) give
\(\dim\partial S\le589\).  The exact \(r=4\) product-shadow capacity at
budget 589 is 341, hence \(b:=\dim S\le341\).

The complementary Koszul estimate is therefore

\[
\operatorname{rank}K_3(\operatorname{perm}_7-R)
\ge58800-49b
\ge58800-49\cdot341
=42091.
\]

Twenty-five Chow terms have Koszul capacity only
\(25\cdot1680=42000\).  At least 26 terms remain, proving \(20+26=46\).

## Exact finite certificate

The script builds the one-dimensional colex shadow tables and the three
Ferrers dynamic programs directly.  The critical sharp values are

- \(r=2\): budget 14, capacity 22;
- \(r=3\): budget 85, capacity 64 (the witness already has shadow 84);
- \(r=4\): budget 589, capacity 341 (the witness has shadow 586, while area
  342 first appears at shadow 590).

It also scans all 7,770 triples \((q,k,\ell)\) with
\(1\le\ell\le k\le q\le35\).  The unique route attaining 46 is
\((q,k,\ell)=(20,5,2)\).

Replay with

```powershell
python scripts/n7_lower46_recursive_shadow_tower.py --verify-json data/n7_lower46_recursive_shadow_tower.json
python -m unittest tests.test_n7_lower46_recursive_shadow_tower -v
```

The four-term Glynn sign-face example has a 35-dimensional cubic section and
therefore refutes a different proposed four-term cap 29.  It does not affect
this proof: the present five-term universal cap is 64, which safely contains
that example.
