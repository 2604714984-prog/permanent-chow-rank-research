# Exact middle third-Koszul rank and a lower-27 residual margin

## Status

`PROOF_DRAFT_COMPLETE`, `EXACT_RATIONAL_LOCAL_REPLAY`,
`STRICT_MODULAR_MINOR_REPLAY`, `LOWER_27_INTERFACE` (N6-035).

This note computes one permanent rank exactly and identifies all forty
homology dimensions by explicit characteristic-zero cycles.  It does not
prove lower 27.  The ordinary interval remains

\[
26\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## 1. The map and the result

Let `V` be the 36-dimensional variable space and put

\[
E_m=\mathcal D_m(\operatorname{perm}_6).
\]

Consider the middle third-Koszul map

\[
\delta_{3,3}:E_3\otimes\Lambda^3V
\longrightarrow E_2\otimes\Lambda^4V.
\tag{1.1}
\]

It is preceded by

\[
\delta_{4,2}:E_4\otimes\Lambda^2V
\longrightarrow E_3\otimes\Lambda^3V.
\tag{1.2}
\]

### Theorem 1.1

Over every characteristic-zero field,

\[
\boxed{
\operatorname{rank}\delta_{3,3}(\operatorname{perm}_6)
=2,715,505.
}
\tag{1.3}

Moreover,

\[
\boxed{
\dim\frac{\ker\delta_{3,3}}{\operatorname{im}\delta_{4,2}}
=40.
}
\tag{1.4}

One arbitrary sextic Chow term contributes at most, and an independent term
contributes exactly,

\[
B_{3,3}=133,545.
\tag{1.5}

Thus the exact permanent rank has the strict numerical margin

\[
2,715,505-20B_{3,3}=44,605.
\tag{1.6}

Equation (1.6) is a target for the twenty-term residual forced by N6-032.  It
does not itself show that the rank remains above `20B_(3,3)` after subtracting
the selected six Chow terms.

### Corollary 1.2 -- exact two-sided overlap target

Suppose hypothetically that

\[
\operatorname{perm}_6=H+Q,
\]

where `H` is a sum of six Chow terms and `Q` is a sum of twenty.  Let `A`,
`B`, and `A-B` be the full matrices of `delta_(3,3)` for the permanent, `H`,
and `Q`, respectively.  Put

\[
r=\operatorname{rank}B,
\]

and let `c` and `s` be the dimensions of the intersections of the column
spaces and row spaces of `A` and `B`.  Then

\[
\boxed{c+s-r\geq44,605.}
\tag{1.7}

Indeed the horizontal/vertical double-quotient rank inequality gives

\[
\operatorname{rank}(A-B)
\geq\operatorname{rank}A+r-c-s.
\]

The twenty-term expression gives
`rank(A-B)<=20B_(3,3)`.  Now use (1.6).  Thus lower 27 is reduced at this
flattening to excluding a 44,605-dimensional two-sided aggregate overlap for
six Chow terms.  No such exclusion is asserted here.

## 2. Forty explicit homology cycles

Index variables by `x_(ij)` for `0<=i,j<=5`.  The row-column torus preserves
the Koszul complex.  Fix a three-element row set `A`.  Consider the weight
whose row part is two on `A` and zero on its complement, and whose column
part is one on every column.

The weight space in the source of (1.1) has the following 120-element basis.
Choose a three-element column set `C`, let `C^c` be its complement, and choose
a bijection

\[
\sigma:A\longrightarrow C^c.
\]

The corresponding basis vector is

\[
P_{A,C}\otimes
\bigwedge_{i\in A}x_{i,\sigma(i)},
\tag{2.1}

with the wedge written in the fixed variable order.  There are
`binom(6,3) 3! = 120` such vectors.

### Lemma 2.1

The sum of all 120 basis vectors in (2.1) lies in
`ker(delta_(3,3))`.

### Proof

Differentiate a basis vector (2.1) in an entry `x_(ij)` of the subpermanent,
where `i in A` and `j in C`.  The output is

\[
P_{A\setminus\{i\},C\setminus\{j\}}
\otimes
x_{ij}\wedge\bigwedge_{a\in A}x_{a,\sigma(a)}.
\tag{2.2}

Fix an output basis vector of the form (2.2).  The four-element wedge records
two possible ways to distinguish the newly inserted edge from the matching
edge in its row and column.  They give exactly two source vectors (2.1).
Their exterior insertion positions differ by one transposition, so their
coefficients in (2.2) are opposite.  Hence every output coefficient cancels
pairwise. ∎

No source vector of (1.2) has this weight: a four-row subpermanent already
uses four distinct rows, whereas the chosen weight is supported on only
three rows.  Thus the cycle is not in the preceding image.

There are `binom(6,3)=20` choices of `A`, with distinct weights.  Transposing
rows and columns gives another 20 distinct cycles.  Therefore

\[
\dim\frac{\ker\delta_{3,3}}{\operatorname{im}\delta_{4,2}}
\geq40.
\tag{2.3}

The representative 120-column integer block has exact rational rank 119.
This local computation is not needed to prove that the displayed sum is a
cycle, but independently verifies that its nullspace is exactly one
dimensional.

## 3. Characteristic-zero upper and lower ranks

The middle space has dimension

\[
\dim(E_3\otimes\Lambda^3V)
=\binom63^2\binom{36}{3}
=2,856,000.
\tag{3.1}

The preceding map (1.2) has the already certified exact rank

\[
\operatorname{rank}\delta_{4,2}=140,455.
\tag{3.2}

Since consecutive Koszul differentials compose to zero, equations
(2.3)--(3.2) give

\[
\operatorname{rank}\delta_{3,3}
\leq2,856,000-140,455-40
=2,715,505.
\tag{3.3}

For the reverse inequality, construct (1.1) in the subpermanent bases and
split it by its twelve-component row-column weight.  Every entry is `0`, `1`,
or `-1`.  Sparse elimination modulo the prime `1,000,003` gives

\[
\operatorname{rank}_{\mathbf F_{1000003}}\delta_{3,3}
=2,715,505.
\tag{3.4}

A nonzero minor modulo the prime is a nonzero integer minor.  Hence (3.4) is
a characteristic-zero lower bound.  It agrees with (3.3), proving (1.3).
Subtracting (3.2) from the exact kernel dimension proves (1.4); in particular,
the forty displayed cycles account for the full homology.

The full modular replay has 119,961 weight blocks and maximum block size
2,400 columns.  It reconstructs the integer matrix from the derivative rule;
no large stored matrix is required.

## 4. Exact one-term cap

For an independent term `T=z_1...z_6`, split \(V=L\oplus W\) into its
six-dimensional factor span and a thirty-dimensional inactive complement.
Inside `L`, the wedge-degree ranks at output degree three are

\[
(20,105,216,190,84,15,0).
\]

Preserving the number of inactive wedge factors gives

\[
\begin{aligned}
B_{3,3}
&=190+\binom{30}{1}216
 +\binom{30}{2}105+\binom{30}{3}20\\
&=133,545.
\end{aligned}
\tag{4.1}

These small internal matrices are ranked exactly over the rationals.
Independent factor tuples form a dense open set, so specialization proves
that (4.1) is the maximum for arbitrary dependent or repeated factors as
well.  Equations (1.3) and (4.1) give (1.6).

## 5. Reproduction and exact claim boundary

Lightweight replay:

```text
python scripts/n6_middle_third_koszul_rank.py \
  --json data/n6_middle_third_koszul_rank.json
python -m unittest tests.test_n6_middle_third_koszul_rank -v
```

Full modular minor replay:

```text
python scripts/n6_middle_third_koszul_rank.py --replay-heavy
```

Expected marker:

```text
N6_MIDDLE_THIRD_KOSZUL_RANK_PASS
```

Classification of evidence:

- pure mathematics: the forty explicit cycles, their independence by torus
  weight, the absence of the preceding image, and the upper bound (3.3);
- exact rational replay: the representative block rank 119 and the one-term
  cap;
- strict modular certificate: the characteristic-zero lower rank (3.4);
- unresolved: a stability or relative-rank theorem showing that the N6-032
  residual retains more than `20B_(3,3)` rank, equivalently an upper bound
  below 44,605 for the two-sided defect in Corollary 1.2.

Therefore N6-035 is not a lower-27 theorem and makes no border-rank claim.
