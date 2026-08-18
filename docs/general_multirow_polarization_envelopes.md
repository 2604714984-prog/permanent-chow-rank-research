# Dyadic multirow polarization envelopes for permanent derivative spaces

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_EXPLICIT_NONZERO_FAMILY`,
`EXACT_WALSH_INTERFACE_REPLAYED`.

This note extends the two-row construction at the sharp pair threshold to an
entire multirow family.

For every characteristic-zero field, every pair of integers

\[
1\le t\le m,
\]

and every

\[
n\ge n_t:=m(m-t+1),
\]

there exist

\[
q_t:=2^{t-1}
\]

degree-\(n\) Chow terms \(T_\varepsilon\) such that

\[
\boxed{
0\ne \operatorname{perm}_m
\in
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{\varepsilon}\mathcal D_m(T_\varepsilon).
}
\tag{0.1}
\]

Here \(\operatorname{perm}_m\) denotes one chosen \(m\times m\) coordinate
subpermanent inside \(\operatorname{perm}_n\).

The family gives the staircase

\[
\boxed{
(q,n)=
\left(2^s,\;m(m-s)\right),
\qquad
0\le s\le m-1.
}
\tag{0.2}
\]

Its three endpoints are:

```text
s=0:       one coordinate envelope at n=m^2
s=1:       the sharp two-envelope construction at n=m(m-1)
s=m-1:     the 2^(m-1)-term Glynn decomposition at n=m.
```

For intermediate \(s\), equation (0.2) is an explicit nonzero
derivative-space construction. It is not claimed to be the first possible
nonzero degree or the smallest possible term count.

## 1. Selected rows and Walsh characters

Fix one \(m\times m\) coordinate block

\[
X=(x_{rj})_{0\le r,j<m}.
\]

Select its first \(t\) rows. Let

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_{t-1})
\in\{\pm1\}^{t-1},
\]

and set

\[
\varepsilon_0=1,
\qquad
\chi(\varepsilon)=\prod_{r=1}^{t-1}\varepsilon_r.
\tag{1.1}
\]

For each column \(j\), define

\[
\ell_{\varepsilon,j}
=
\sum_{r=0}^{t-1}\varepsilon_r x_{rj}.
\tag{1.2}
\]

When \(t=1\), the sign set has one empty element, its character is one, and
\(\ell_{\varepsilon,j}=x_{0j}\).

## 2. The multirow Fourier selector

Let \(C\subseteq[m]\) have size \(t\). Write
\(\operatorname{perm}(X_{[t],C})\) for the \(t\times t\) permanent on the
selected rows and columns.

### Lemma 2.1 -- exact Walsh selector

\[
\boxed{
\operatorname{perm}(X_{[t],C})
=
2^{1-t}
\sum_{\varepsilon\in\{\pm1\}^{t-1}}
\chi(\varepsilon)
\prod_{j\in C}\ell_{\varepsilon,j}.
}
\tag{2.1}
\]

### Proof

Expand one product on the right. Every term is indexed by a map

\[
\phi:C\longrightarrow\{0,\ldots,t-1\},
\]

and has monomial

\[
\prod_{j\in C}x_{\phi(j),j}.
\]

Put

\[
c_r=|\phi^{-1}(r)|.
\]

Its normalized coefficient in the right side of (2.1) is

\[
2^{1-t}
\sum_{\varepsilon}
\prod_{r=1}^{t-1}\varepsilon_r^{\,1+c_r}.
\tag{2.2}
\]

The sign variables separate. The sum is nonzero exactly when every
\(1+c_r\) is even for \(1\le r<t\), or equivalently when every \(c_r\) for
\(r\ge1\) is odd.

There are \(t-1\) such counts and their total is at most \(t\). Hence each of
them must equal one. The remaining count \(c_0\) also equals one. Thus the
surviving maps are precisely the bijections from \(C\) to the selected rows.
For each bijection the sum in (2.2) equals \(2^{t-1}\), so its normalized
coefficient is one.

The surviving monomials are exactly the monomials of the displayed
\(t\times t\) permanent. ∎

This is a multilinear Walsh-Fourier projection. Unlike the usual homogeneous
polarization formula, it has no factorial denominator because the columns are
already distinct slots.

## 3. Laplace expansion across the selected rows

For \(C\subseteq[m]\) with \(|C|=t\), let

\[
P_{\widehat C}
\]

be the permanent on rows \(t,\ldots,m-1\) and columns
\([m]\setminus C\). When \(t=m\), use the empty permanent
\(P_{\widehat C}=1\).

Laplace expansion across the first \(t\) rows gives

\[
\operatorname{perm}_m
=
\sum_{\substack{C\subseteq[m]\\|C|=t}}
\operatorname{perm}(X_{[t],C})P_{\widehat C}.
\tag{3.1}
\]

For every sign vector, define

\[
G_\varepsilon
=
\sum_{\substack{C\subseteq[m]\\|C|=t}}
\left(
\prod_{j\in C}\ell_{\varepsilon,j}
\right)
P_{\widehat C}.
\tag{3.2}
\]

Substituting Lemma 2.1 into (3.1) yields

\[
\boxed{
\operatorname{perm}_m
=
2^{1-t}
\sum_{\varepsilon\in\{\pm1\}^{t-1}}
\chi(\varepsilon)G_\varepsilon.
}
\tag{3.3}
\]

For \(t=2\), this is the inherited two-row identity

\[
\operatorname{perm}_m=\frac12G_{+}-\frac12G_{-}.
\]

For \(t=m\), each \(G_\varepsilon\) is one product
\(\prod_j\ell_{\varepsilon,j}\), and (3.3) is the usual sign decomposition of
the permanent.

## 4. One Chow envelope for each Walsh character

Define

\[
T_\varepsilon^{(0)}
=
\left(
\prod_{j=0}^{m-1}\ell_{\varepsilon,j}
\right)
\left(
\prod_{r=t}^{m-1}\prod_{j=0}^{m-1}x_{rj}
\right).
\tag{4.1}
\]

The factors in (4.1) are linearly independent:

- the \(m\) forms \(\ell_{\varepsilon,j}\) use disjoint column-variable
  blocks; and
- the remaining coordinate factors use rows not present in those forms.

The number of factors is

\[
m+m(m-t)=m(m-t+1)=n_t.
\tag{4.2}
\]

Hence \(T_\varepsilon^{(0)}\) is a degree-\(n_t\) Chow term with an independent
factor frame.

Every monomial in \(G_\varepsilon\) consists of

- \(t\) distinct factors \(\ell_{\varepsilon,j}\), indexed by \(j\in C\); and
- one coordinate factor from each of the remaining \(m-t\) rows and each
  column outside \(C\).

It is therefore a product of exactly \(m\) distinct factors from
\(T_\varepsilon^{(0)}\). For a product of independent linear factors, the
output-degree-\(m\) derivative space is the span of all squarefree
\(m\)-factor subproducts. Consequently,

\[
\boxed{
G_\varepsilon
\in
\mathcal D_m(T_\varepsilon^{(0)}).
}
\tag{4.3}
\]

Combining (3.3) and (4.3) gives

\[
0\ne\operatorname{perm}_m
\in
\sum_{\varepsilon}
\mathcal D_m(T_\varepsilon^{(0)})
\tag{4.4}
\]

at degree \(n_t=m(m-t+1)\).

## 5. Extension to every larger permanent order

Let \(n\ge n_t\). Choose \(n-n_t\) additional independent linear forms

\[
y_1,\ldots,y_{n-n_t}
\]

outside every displayed factor frame and put

\[
T_\varepsilon
=
T_\varepsilon^{(0)}
\prod_{a=1}^{n-n_t}y_a.
\tag{5.1}
\]

There are enough ambient directions: if \(n>m\), then

\[
n^2-m^2=(n-m)(n+m)\ge n-m\ge n-n_t.
\]

Each \(T_\varepsilon\) is now a degree-\(n\) Chow term. Differentiating away
all added factors shows

\[
\mathcal D_m(T_\varepsilon^{(0)})
\subseteq
\mathcal D_m(T_\varepsilon).
\tag{5.2}
\]

The chosen \(m\times m\) coordinate subpermanent belongs to
\(\mathcal D_m(\operatorname{perm}_n)\). Equations (4.4)--(5.2) prove (0.1).

If a block is allowed to contain more than \(q_t=2^{t-1}\) terms, append
arbitrary extra Chow terms. The same witness remains in the larger literal
sum.

## 6. The dyadic nonzero staircase

Write

\[
s=t-1.
\]

Then \(0\le s\le m-1\), the number of envelopes is \(2^s\), and their first
constructed degree is

\[
n_s=m(m-s).
\tag{6.1}
\]

Thus:

\[
\boxed{
0\ne \mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{i=1}^{2^s}\mathcal D_m(T_i)
\quad
\text{for every }n\ge m(m-s).
}
\tag{6.2}
\]

Selected rows of the staircase are

```text
terms       first constructed degree
1           m^2
2           m(m-1)
4           m(m-2)
8           m(m-3)
...
2^(m-1)    m.
```

### Corollary 6.1 -- arbitrary available term count

For \(q\ge1\), put

\[
s(q,m)=\min\{m-1,\lfloor\log_2 q\rfloor\}.
\tag{6.3}
\]

Then some \(q\)-term Chow block has nonzero permanent-relative
output-degree-\(m\) intersection for every

\[
\boxed{
n\ge m\bigl(m-s(q,m)\bigr).
}
\tag{6.4}
\]

Only \(2^{s(q,m)}\) of the available labels are needed.

### Corollary 6.2 -- fixed \(n,m\)

Let \(\mu(n,m)\) be the minimum \(q\) for which some \(q\)-term block has a
nonzero intersection with \(\mathcal D_m(\operatorname{perm}_n)\). The
construction gives

\[
\boxed{
\mu(n,m)
\le
2^{\,\min\{m-1,\max\{0,m-\lfloor n/m\rfloor\}\}}.
}
\tag{6.5}
\]

At the exact staircase points \(n=m(m-s)\), the right side is \(2^s\).

### Corollary 6.3 -- ceiling on universal zero theorems

For a fixed \(m,q\), no universal \(q\)-term zero theorem can include every
degree

\[
n\ge m\bigl(m-s(q,m)\bigr).
\tag{6.6}
\]

Equivalently, the largest possible universal-zero endpoint is at most one
less than the degree in (6.6).

This is an upper boundary supplied by explicit counterexamples. It is exact
for the inherited cases \(q=1\) and \(q=2\), but not claimed exact for
\(q\ge3\).

## 7. Relation to the existing general-\(n\) program

The construction unifies three previously separate objects.

### One envelope

At \(t=1\),

\[
T^{(0)}=\prod_{0\le r,j<m}x_{rj},
\]

and \(\operatorname{perm}_m\in\mathcal D_m(T^{(0)})\) at \(n=m^2\).

### Two envelopes

At \(t=2\), equation (3.3) is exactly the two-row construction at

\[
n=m(m-1).
\]

The parent theorem proves this pair threshold is sharp.

### All rows

At \(t=m\), the remaining permanent is empty, every
\(G_\varepsilon\) is itself a Chow term, and (3.3) becomes the
\(2^{m-1}\)-term Glynn decomposition of \(\operatorname{perm}_m\).

The intermediate rows therefore interpolate, inside derivative spaces,
between the one-envelope coordinate construction and the top-degree Glynn
decomposition.

## 8. Firewall and limitations

The forms \(G_\varepsilon\) are generally sums of many monomials. The theorem
places each \(G_\varepsilon\) inside the derivative space of one Chow term.
It does **not** assert that \(G_\varepsilon\) is itself a Chow term.

Likewise, equation (3.3) is used only to produce a literal derivative-space
intersection. No literal direct sum is identified with the catalectic image
of \(\sum_\varepsilon T_\varepsilon\).

The result does not establish:

- minimality of \(2^{t-1}\) for \(2<t<m\);
- sharpness of the degree \(m(m-t+1)\) for \(q\ge3\);
- a new exact Chow rank for any order at least six;
- a new Chow-rank lower bound;
- a border-Chow-rank statement; or
- literature novelty.

The next mathematical interface is to close or separate the gaps between the
known universal zero regions and the dyadic nonzero staircase, beginning with
three- and four-envelope blocks.

## 9. Reproduction

Run

```bash
python scripts/general_multirow_polarization_envelopes.py \
  --json /tmp/general_multirow_polarization_envelopes.json
python scripts/general_multirow_polarization_envelopes_independent.py
python -m unittest tests.test_general_multirow_polarization_envelopes -v
```

Expected markers:

```text
GENERAL_MULTIROW_POLARIZATION_ENVELOPES_AUDIT_PASS
GENERAL_MULTIROW_POLARIZATION_ENVELOPES_INDEPENDENT_PASS
```
