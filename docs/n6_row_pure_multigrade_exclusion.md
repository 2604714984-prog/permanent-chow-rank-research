# N6-067: row-pure multigrade collision trees are impossible

**Status.** `PURE_CONDITIONAL_ROW_PURE_MULTIGRADE_EXCLUSION`,
`EXACT_INTEGER_REPLAY` (N6-067).

This note treats arbitrarily many valuation levels at the unresolved
\(b=50\) endpoint, subject to one explicit tensor condition on the final
seventy-five-plane.  It does not assume that the five relative blocks occur
in one grade.  It does assume that, after saturation through all grades, they
remain five full row-pure packets with one shared complete column frame.

## 1. The row-pure hypothesis

Let \(A=C=k^6\) over a field of characteristic zero, with coordinate bases
\(a_0,\ldots,a_5\) and \(c_0,\ldots,c_5\).  Put

\[
 E_A=\langle a_i a_j:i<j\rangle\subset\operatorname{Sym}^2A,
 \qquad
 E_C=\langle c_p c_q:p<q\rangle\subset\operatorname{Sym}^2C.
\tag{1.1}
\]

Under the usual Cauchy polarization
\(\operatorname{Sym}^2A\otimes\operatorname{Sym}^2C
\hookrightarrow\operatorname{Sym}^2(A\otimes C)\), the quadratic permanent
space is

\[
 E_2=E_A\otimes E_C.
\tag{1.2}
\]

Let \(K_0\) be the Grassmann flat limit of the seventy-five-plane at the
\(b=50\) endpoint.  The **row-pure multigrade hypothesis** is that

\[
 K_0=Q\otimes E_C\subset E_2
 \quad\text{for some}\quad
 Q\subset\operatorname{Sym}^2A,
 \qquad \dim Q=5.
\tag{1.3}
\]

For a valuation tree, (1.3) holds if its saturated Smith basis consists of
five full graded packets \(q_e\otimes E_C\), with the five \(q_e\) independent.
The packets may occur at different valuations and at arbitrarily nested
nodes.  Thus their orders and the shape of the rooted tree play no role once
(1.3) is known.

## 2. The row factor is squarefree

Let
\(\pi:\operatorname{Sym}^2A\to\operatorname{Sym}^2A/E_A\) be the quotient.
Choose \(0\ne s\in E_C\).  For every \(q\in Q\), (1.3) gives
\(q\otimes s\in E_A\otimes E_C\), and hence

\[
 0=(\pi\otimes\mathrm{id})(q\otimes s)=\pi(q)\otimes s.
\tag{2.1}
\]

Over a field, a pure tensor with nonzero second factor vanishes only when
its first factor vanishes.  Therefore

\[
 \boxed{Q\subset E_A.}
\tag{2.2}
\]

## 3. A diagonal-codimension lemma

Let

\[
 R=\partial_A Q\subset A,
 \qquad r=\dim R.
\tag{3.1}
\]

Every symmetric tensor in \(Q\) has all of its contraction images in \(R\).
In a decomposition \(A=R\oplus R'\), symmetry then kills both the
\(R\otimes R'\) and \(\operatorname{Sym}^2R'\) blocks.  Thus

\[
 Q\subset\operatorname{Sym}^2R.
\tag{3.2}
\]

### Lemma 3.1

For every \(r\)-plane \(R\subset k^6\),

\[
 \dim\bigl(\operatorname{Sym}^2R\cap E_A\bigr)
 \le \binom r2.
\tag{3.3}
\]

### Proof

Let \(\ell_i=a_i^*|_R\in R^*\).  The six coordinate restrictions span
\(R^*\).  Choose \(r\) independent members.  After using them as coordinates
\(y_1,\ldots,y_r\), their squares are the distinct monomials
\(y_1^2,\ldots,y_r^2\), so they are linearly independent.  Hence

\[
 \dim\langle\ell_0^2,\ldots,\ell_5^2\rangle\ge r.
\tag{3.4}
\]

Let \(\delta:\operatorname{Sym}^2A\to k^6\) record the six diagonal
coefficients.  Then \(E_A=\ker\delta\).  The dual of the restriction of
\(\delta\) to \(\operatorname{Sym}^2R\) has image exactly
\(\langle\ell_i^2\rangle\).  Its rank is therefore at least \(r\), and

\[
 \dim(\operatorname{Sym}^2R\cap E_A)
 \le \binom{r+1}{2}-r=\binom r2.
\]

This proves the lemma. \(\square\)

Equations (2.2), (3.2), and \(\dim Q=5\) now imply

\[
 5\le\binom r2,
 \qquad\text{so}\qquad r\ge4.
\tag{3.5}
\]

## 4. The derivative shadow is at least twenty-four

Contraction of a polarized Cauchy tensor separates into its row and column
contractions.  Since decomposable covectors span
\((A\otimes C)^*=A^*\otimes C^*\),

\[
 \partial(Q\otimes E_C)
   =(\partial_AQ)\otimes(\partial_CE_C).
\tag{4.1}
\]

Every column basis vector is a derivative of some \(c_pc_q\), so
\(\partial_CE_C=C\).  Therefore

\[
 \boxed{\partial K_0=R\otimes C,
 \qquad \dim\partial K_0=6r\ge24.}
\tag{4.2}
\]

On the other hand, N6-064 gives derivative dimension twenty-three on every
nonzero \(b=50\) equality fiber.  Specialization gives at most twenty-three
for its Grassmann limit, while the universal product-shadow bound gives at
least twenty-three.  Hence the actual endpoint limit must satisfy
\(\dim\partial K_0=23\), contradicting (4.2).

Thus no row-pure multigrade valuation tree satisfying (1.3) can realize the
\(b=50\) endpoint.  Transposition gives the corresponding column-pure
statement.

## 5. Scope and replay

If a generic family literally has six complete row slices
\(p_i(t)\otimes C\), with one fixed column squarefree frame and the literal
matching of its fifteen column pairs, then

\[
 K(t)=Q(t)\otimes E_C,
 \qquad
 Q(t)=\langle p_i(t)^2-p_1(t)^2:2\le i\le6\rangle.
\tag{5.1}
\]

The tensor-product map from
\(\operatorname{Gr}(5,\operatorname{Sym}^2A)\) to the corresponding
Grassmannian is regular, so every multigrade limit of such a family
automatically has form (1.3).  This is one concrete class covered without
examining its collision tree node by node.

The theorem does **not** claim that merely having complete row slices in the
special fiber forces (1.3).  Open cases include partial-rank Smith packets,
column jets, different column frames at different nodes, and
\(\operatorname{End}(E_C)\)-valued quotient gauges whose saturated limit is
not \(Q\otimes E_C\).  It does not exclude every collision tree, remove the
full \(b=50\) endpoint, or prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\).

The replay records the only numerical consequence used in the proof:

```text
python scripts/n6_row_pure_multigrade_exclusion.py \
  --json data/n6_row_pure_multigrade_exclusion.json
python -m unittest tests.test_n6_row_pure_multigrade_exclusion -v
```
