# The exact two-term factor-span threshold

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_SHARP_COUNTEREXAMPLE`,
`EXACT_COMBINATORIAL_INTERFACE_REPLAYED`.

This note is stacked on the private-polar shadow-amplification theorem.  That
theorem proves that, for every `m>=3`, arbitrary two-term Chow blocks have
zero permanent-relative intersection throughout

\[
m\le n\le m^2-m-1.
\]

The present note proves that the next row is already nonzero and that the same
construction persists for every larger degree.  Hence the universal two-term
zero range is exact:

\[
\boxed{
\begin{array}{ll}
m\le n\le m^2-m-1:
&
\mathcal D_m(\operatorname{perm}_n)
\cap
\bigl(\mathcal D_m(T)+\mathcal D_m(U)\bigr)=0
\quad\text{for all }T,U,
\\[2mm]
n\ge m^2-m:
&
\text{there exist }T,U\text{ with a nonzero intersection.}
\end{array}
}
\]

The theorem is ordinary characteristic-zero algebra.  It is a sharpness
result for a literal derivative-space intersection theorem.  It is not a
two-term Chow decomposition of the permanent, a new Chow-rank lower bound, a
border-rank statement, or an exact-rank result for any order at least six.

## 1. The threshold block

Fix `m>=3` and put

\[
n_0=m(m-1).
\]

Inside the variable space of \(\operatorname{perm}_n\), choose an \(m\times m\)
coordinate block

\[
X=(x_{ij})_{0\le i,j<m}.
\]

For every column \(j\), define

\[
a_j=x_{0j}+x_{1j},
\qquad
b_j=x_{0j}-x_{1j}.
\tag{1.1}
\]

Let \(Y\) denote the remaining \(m-2\) rows of the block.  For two distinct
columns \(c,d\), write

\[
P_{\widehat{c,d}}
=
\operatorname{perm}
\left(
x_{ij}
\right)_{
2\le i<m,\;
j\in [m]\setminus\{c,d\}
}.
\]

For `m=2`, the empty permanent is one; the main theorem below starts at
`m=3`.

Define two degree-\(m\) forms

\[
G_a
=
\sum_{0\le c<d<m}
a_ca_dP_{\widehat{c,d}},
\qquad
G_b
=
\sum_{0\le c<d<m}
b_cb_dP_{\widehat{c,d}}.
\tag{1.2}
\]

## 2. The two-row polarization identity

Expanding the permanent along the first two rows gives

\[
\operatorname{perm}_m
=
\sum_{c<d}
\left(
x_{0c}x_{1d}
+
x_{0d}x_{1c}
\right)
P_{\widehat{c,d}}.
\tag{2.1}
\]

The change of variables (1.1) yields

\[
x_{0c}x_{1d}+x_{0d}x_{1c}
=
\frac12(a_ca_d-b_cb_d).
\tag{2.2}
\]

Therefore

\[
\boxed{
\operatorname{perm}_m
=
\frac12G_a-\frac12G_b.
}
\tag{2.3}
\]

This is not a two-term Chow decomposition: \(G_a\) and \(G_b\) are generally
large sums.  The relevant fact is that each one lies in the derivative space
of a single higher-degree Chow term.

## 3. Two degree-\(n_0\) Chow envelopes

Let

\[
L_a
=
\operatorname{span}
\left(
a_0,\ldots,a_{m-1},
x_{ij}:2\le i<m,\;0\le j<m
\right),
\]

and define \(L_b\) analogously with the \(b_j\).  Both spaces have dimension

\[
m+m(m-2)=m(m-1)=n_0.
\]

Define the degree-\(n_0\) Chow terms

\[
T_a^{(0)}
=
\left(\prod_{j=0}^{m-1}a_j\right)
\left(\prod_{i=2}^{m-1}\prod_{j=0}^{m-1}x_{ij}\right),
\tag{3.1}
\]

\[
T_b^{(0)}
=
\left(\prod_{j=0}^{m-1}b_j\right)
\left(\prod_{i=2}^{m-1}\prod_{j=0}^{m-1}x_{ij}\right).
\tag{3.2}
\]

All factors in either term are linearly independent.

For a product of \(N\) independent linear factors, the output-degree-\(m\)
derivative space is the span of all products of \(m\) distinct factors.
Every monomial in \(G_a\) consists of

- two distinct \(a\)-factors; and
- one variable from each of the remaining \(m-2\) rows,

so it is a product of \(m\) distinct factors of \(T_a^{(0)}\).  Hence

\[
G_a\in\mathcal D_m(T_a^{(0)}).
\tag{3.3}
\]

Similarly,

\[
G_b\in\mathcal D_m(T_b^{(0)}).
\tag{3.4}
\]

Combining (2.3), (3.3), and (3.4) gives

\[
0\ne\operatorname{perm}_m
\in
\mathcal D_m(T_a^{(0)})
+
\mathcal D_m(T_b^{(0)}).
\tag{3.5}
\]

## 4. Extension to every \(n\ge n_0\)

Now let \(n\ge n_0\).  Choose \(n-n_0\) additional independent linear forms

\[
y_1,\ldots,y_{n-n_0}
\]

outside the displayed factor frames, and put

\[
T_a=T_a^{(0)}\prod_s y_s,
\qquad
T_b=T_b^{(0)}\prod_s y_s.
\tag{4.1}
\]

These are degree-\(n\) Chow terms.  Differentiating away all added factors and
all unselected original factors shows

\[
\mathcal D_m(T_a^{(0)})\subseteq\mathcal D_m(T_a),
\qquad
\mathcal D_m(T_b^{(0)})\subseteq\mathcal D_m(T_b).
\tag{4.2}
\]

The chosen \(m\times m\) subpermanent is an output-degree-\(m\) derivative of
\(\operatorname{perm}_n\).  Therefore

\[
\boxed{
0\ne\operatorname{perm}_m
\in
\mathcal D_m(\operatorname{perm}_n)
\cap
\left(
\mathcal D_m(T_a)+\mathcal D_m(T_b)
\right)
}
\tag{4.3}
\]

for every \(n\ge m(m-1)\).

## 5. Exact pair threshold

The parent private-polar shadow theorem proves the universal zero statement

\[
m\le n\le m^2-m-1
\quad\Longrightarrow\quad
\mathcal D_m(\operatorname{perm}_n)
\cap
\left(
\mathcal D_m(T)+\mathcal D_m(U)
\right)
=0
\tag{5.1}
\]

for every pair of degree-\(n\) Chow terms, for all \(m\ge3\).  The cubic end
\(m=3,n=5\) is supplied by the previously closed first-excess theorem.

Equation (4.3) supplies a counterexample at the next integer and at every
larger integer.

### Theorem 5.1 -- sharp universal two-term threshold

Over every characteristic-zero field, for all \(m\ge3\) and \(n\ge m\),

\[
\boxed{
\begin{aligned}
n\le m^2-m-1
&\Longrightarrow
\text{every two-term Chow block is permanent-relative zero},
\\
n\ge m^2-m
&\Longrightarrow
\text{some two-term Chow block has nonzero intersection}.
\end{aligned}
}
\]

In particular, the unresolved cubic row

\[
(n,m,q)=(6,3,2)
\]

is a sharp nonzero counterexample.  The only cubic excess-\(m\) row still open
after this theorem is

\[
(n,m,q)=(4,3,3).
\]

## 6. Geometry of the construction

The identity is the symmetric-row analogue of diagonalizing the bilinear
form carried by the first two permanent rows.

Let

\[
P=\operatorname{span}\{a_j\}_{j=0}^{m-1},
\qquad
Q=\operatorname{span}\{b_j\}_{j=0}^{m-1},
\]

and let \(K\) be the span of the remaining \(m-2\) rows.  Then

\[
L_a=K\oplus P,
\qquad
L_b=K\oplus Q,
\]

\[
\dim K=m(m-2),
\qquad
\dim L_a=\dim L_b=m(m-1),
\]

\[
L_a+L_b=K\oplus P\oplus Q
\]

has dimension \(m^2\).  The two selected components share exactly the
\(m(m-2)\)-dimensional core \(K\).  This realizes all dimension equalities at
the stopping point of the private-polar shadow argument.

The equality frontier is therefore not merely a failure of the current
estimate.  It contains an explicit, uniform Chow-realizable family.

## 7. Consequences for the research program

The following frontier is now closed sharply:

```text
two-term blocks:
  n <= m^2-m-1     universal zero theorem
  n >= m^2-m       explicit nonzero family
```

Accordingly, no stronger universal two-term zero theorem can cross
\(n=m^2-m\).

The next legitimate small-excess target is not the pair equality row.  It is

```text
cubic q=3 row:
  (n,m,q)=(4,3,3)
```

or a quantitative theorem for \(q\ge3\) at and beyond

\[
(q-1)n=m^2.
\]

The counterexample also shows that equality classification must retain the
actual Chow derivative origin.  Pure scalar-shadow estimates are exactly
saturated here.

## 8. Claim boundary

```text
status=PROOF_DRAFT_COMPLETE_AND_EXACT_COMBINATORIAL_INTERFACE_REPLAYED
new exact Chow rank=false
new optimized finite-n lower bound=false
universal two-term zero threshold=SHARP
pair n=m^2-m=EXPLICIT NONZERO
pair n>m^2-m=EXPLICIT NONZERO BY EXTRA FACTORS
cubic (6,3,2)=RESOLVED NONZERO
cubic (4,3,3)=OPEN
border-rank improvement=NO
general Glynn optimality=OPEN
literature novelty=NOT_ESTABLISHED
hosted full CI=PENDING
```
