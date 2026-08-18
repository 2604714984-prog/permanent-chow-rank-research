# Multiblock polar descent and recursive Chow zero blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

Let

\[
E_d(n)=\mathcal D_d(\operatorname{perm}_n)
\]

and let \(T_1,\ldots,T_q\) be arbitrary degree-\(n\) Chow terms.  This note
proves a recursive lifting principle for permanent-relative zero blocks:

\[
\boxed{
z\text{ terms are zero at output degree }d-1
\Longrightarrow
z+\left\lfloor\frac{d^2-1}{n}\right\rfloor
\text{ terms are zero at output degree }d.
}
\]

Iterating only the strict permanent shadow floor gives the universal count

\[
\boxed{
Z_{n,m}
=
\sum_{d=2}^{m}
\left\lfloor\frac{d^2-1}{n}\right\rfloor .
}
\]

Every block of at most \(Z_{n,m}\) Chow terms has zero intersection with
\(E_m(n)\).

This is an ordinary characteristic-zero theorem.  It does not determine a new
exact Chow rank, improve the current optimized finite-order lower-bound table,
prove a border-rank statement or establish literature novelty.  Its main use
is as a hard Chow-realizability seed for future derivative-tower and
block-projection arguments.

## 1. Zero-block terminology

For fixed \(n,d\), call an integer \(z\ge0\) a **certified zero count** when,
for every \(r\le z\) and every collection of \(r\) degree-\(n\) Chow terms,

\[
E_d(n)\cap\sum_{i=1}^{r}\mathcal D_d(T_i)=0.
\tag{1.1}
\]

The property is explicitly quantified for all \(r\le z\); no padding by
uncontrolled extra terms is used.

The strict factor-span theorem gives the elementary count

\[
\left\lfloor\frac{d^2-1}{n}\right\rfloor,
\tag{1.2}
\]

because that many term factor spaces have total dimension strictly below
\(d^2\).  The new point is that zero counts can be lifted recursively from one
output degree to the next.

## 2. Component essential spaces

Suppose

\[
0\ne f\in E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i)
\tag{2.1}
\]

and choose a literal representation

\[
f=f_1+\cdots+f_q,
\qquad
f_i\in\mathcal D_d(T_i).
\tag{2.2}
\]

Let

\[
M_i=\partial^{d-1}f_i
\]

be the essential variable space of \(f_i\); put \(M_i=0\) when \(f_i=0\).
Every nonzero \(f_i\) is concise on \(M_i\), and

\[
\dim M_i\le n.
\tag{2.3}
\]

Let

\[
M=M_1+\cdots+M_q
\]

and let

\[
U=\partial^{d-1}f
\]

be the essential space of \(f\).  Then

\[
U\subseteq M.
\tag{2.4}
\]

Permanent derivative-shadow rigidity gives

\[
\boxed{\dim U\ge d^2.}
\tag{2.5}
\]

For a degree-\(d\) form regarded as a concise form on \(U\), the first
catalectic map

\[
U^*\longrightarrow\operatorname{Sym}^{d-1}U
\]

is injective.  Thus a covector whose restriction to \(U\) is nonzero has a
nonzero polar of \(f\).

## 3. The multiblock polar descent lemma

### Theorem 3.1

Let \(1\le a<q\).  If

\[
an<d^2,
\tag{3.1}
\]

then every nonzero intersection element in (2.1) produces a nonzero element

\[
0\ne g
\in
E_{d-1}(n)
\cap
\sum_{i\in I}\mathcal D_{d-1}(T_i)
\tag{3.2}
\]

for some label set \(I\) of size

\[
|I|=q-a.
\tag{3.3}
\]

### Proof

Choose any label set \(J\) of size \(a\), and put

\[
W_J=\sum_{j\in J}M_j.
\]

By (2.3),

\[
\dim W_J\le an<d^2\le\dim U.
\tag{3.4}
\]

Hence \(U\) is not contained in \(W_J\).  Equivalently, there is a covector

\[
\beta\in M^*
\]

which annihilates \(W_J\) but does not annihilate \(U\).  Extend \(\beta\) to
the ambient variable space.  Conciseness on \(U\) gives

\[
g=\beta\mathbin{\lrcorner}f\ne0.
\tag{3.5}
\]

For every \(j\in J\), the covector \(\beta\) annihilates the essential space of
\(f_j\), so

\[
\beta\mathbin{\lrcorner}f_j=0.
\]

Therefore

\[
g
=
\sum_{i\notin J}
\beta\mathbin{\lrcorner}f_i.
\tag{3.6}
\]

Differentiation lowers the output degree of a term derivative:

\[
\beta\mathbin{\lrcorner}f_i
\in
\mathcal D_{d-1}(T_i).
\]

Also \(g\in E_{d-1}(n)\), because \(g\) is a derivative of
\(f\in E_d(n)\).  Taking \(I=[q]\setminus J\) proves (3.2)--(3.3). QED.

The theorem uses actual component essential spaces, not full factor spans.
Zero or nonconcise selected components cause no problem: their essential
spaces are simply smaller, which only strengthens (3.4).

## 4. The one-step zero-count lifting theorem

Put

\[
a_{n,d}
=
\left\lfloor\frac{d^2-1}{n}\right\rfloor
=
\left\lceil\frac{d^2}{n}\right\rceil-1.
\tag{4.1}
\]

Then

\[
a_{n,d}n<d^2.
\tag{4.2}
\]

### Theorem 4.1

If \(z\) is a certified zero count for \(E_{d-1}(n)\), then

\[
\boxed{z+a_{n,d}}
\tag{4.3}
\]

is a certified zero count for \(E_d(n)\).

### Proof

Take any \(q\le z+a_{n,d}\).

If \(q\le a_{n,d}\), then

\[
qn\le a_{n,d}n<d^2,
\]

so the strict factor-span theorem already gives zero intersection.

Assume \(q>a_{n,d}\) and suppose a nonzero intersection element exists.
Apply Theorem 3.1 with

\[
a=a_{n,d}.
\]

It produces a nonzero degree-\((d-1)\) intersection supported on

\[
q-a_{n,d}\le z
\]

of the same Chow terms.  This contradicts the definition of the lower-degree
certified zero count. QED.

This is a genuine recursive Chow-realizability statement.  It is stronger
than applying the strict factor-span inequality independently at each output
degree, because zero counts accumulated at lower degrees are carried upward.

## 5. Closed form from the strict seed

Set

\[
Z_{n,1}=0
\]

and recursively define

\[
Z_{n,d}
=
Z_{n,d-1}
+
\left\lfloor\frac{d^2-1}{n}\right\rfloor.
\tag{5.1}
\]

Repeated application of Theorem 4.1 gives:

### Corollary 5.1

For every \(1\le m\le n\),

\[
\boxed{
Z_{n,m}
=
\sum_{d=2}^{m}
\left\lfloor\frac{d^2-1}{n}\right\rfloor
}
\tag{5.2}
\]

is a certified zero count:

\[
\boxed{
E_m(n)\cap
\sum_{i=1}^{q}\mathcal D_m(T_i)=0
\qquad
(q\le Z_{n,m}).
}
\tag{5.3}
\]

More generally, any independently proved direct seed
\(\sigma_{n,d}\) can be inserted through the closure

\[
\widehat Z_{n,d}
=
\max\left\{
\sigma_{n,d},
\widehat Z_{n,d-1}
+
\left\lfloor\frac{d^2-1}{n}\right\rfloor
\right\}.
\tag{5.4}
\]

Thus the endpoint, private-polar and post-simplex zero blocks in the current
stack can be propagated to every higher output degree without repeating their
geometry.

## 6. Direct rank consequence and asymptotics

At top output degree,

\[
E_n(n)=\operatorname{span}\{\operatorname{perm}_n\},
\]

and

\[
\mathcal D_n(T_i)=\operatorname{span}\{T_i\}.
\]

Therefore (5.3) gives

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
1+
\sum_{d=2}^{n}
\left\lfloor\frac{d^2-1}{n}\right\rfloor.
}
\tag{6.1}
\]

This reproduces the exact lower bound four at \(n=3\), but from \(n=4\)
onward it is no stronger than the existing central-binomial lower bound.  It
is not promoted as a new best numerical result.

For

\[
m=\lfloor\alpha n\rfloor,
\qquad
0<\alpha\le1,
\]

the sum of squares and the total floor error give

\[
\boxed{
Z_{n,m}
=
\frac{\alpha^3}{3}n^2+O(n).
}
\tag{6.2}
\]

Thus repeated polar descent converts the linear-size direct factor-span seed
into a quadratic-size guaranteed zero block when the output degree is linear
in \(n\).  This remains polynomial in \(n\), so the direct top-degree
consequence does not approach Glynn's exponential upper bound.

Selected exact values are:

\[
\begin{array}{c|c|c}
(n,m)&
\lfloor(m^2-1)/n\rfloor&
Z_{n,m}\\
\hline
(8,5)&3&5\\
(9,6)&3&6\\
(10,8)&6&16\\
(12,8)&5&14\\
(16,12)&8&35\\
(32,16)&7&40\\
(64,32)&15&164\\
(100,50)&24&404.
\end{array}
\]

The gap between the last two columns is precisely the accumulated
lower-degree Chow-realizability information.

## 7. Coupled/literal firewall

The proof never asserts

\[
\mathcal D_d\!\left(\sum_iT_i\right)
=
\sum_i\mathcal D_d(T_i).
\]

Its input is one actual element of the literal intersection and one chosen
literal representation (2.2).  The covector is applied to the equality
\(f=\sum_i f_i\), so the descendant is an actual derivative of \(f\) and
simultaneously belongs to the stated lower-degree literal sum.  For an actual
polynomial decomposition, only the valid containment of the coupled
catalectic image in the literal sum is needed.

## 8. Research consequence

The theorem supplies a new hard-zero interface for the exact derivative
tower.  The natural next task is to insert the recursively closed counts
\(\widehat Z_{n,d}\) into the prefix min-plus capacity recurrence and determine
whether they improve finite thresholds or the scalar-tower polynomial
ceiling.

The theorem itself does not claim such an improvement.  It also does not
classify the remaining cubic rows, prove border-rank bounds or solve general
Glynn optimality.
