# Apolar multiplication tensors as a nonlinear Chow-rank interface

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_FRAMEWORK`,
`EXACT_RATIONAL_AND_INTEGER_REPLAYED`.

This note opens a nonlinear algebra-structure route after the scalar,
fixed-linear-map, Fitting, Betti and exact-additive representation barriers.
It proves that multiplication tensors of apolar algebras pass safely through
a Chow decomposition and that every individual Chow term is controlled by one
square-zero Boolean algebra.

For the permanent it gives the baseline bounds

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
\left\lceil
\frac{\binom{2n}{n}}{2^n}
\right\rceil
}
\tag{0.1}
\]

from border multiplication rank, and

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
\left\lceil
\frac{2\binom{2n}{n}-1}
{(n+2)2^{n-1}}
\right\rceil
}
\tag{0.2}
\]

from ordinary bilinear complexity and a published rank decomposition of tensor
powers of the three-factor `W` tensor.

The first bound is exactly the equal-weight all-degree scalar-profile ratio
already recorded in the repository; the second is asymptotically weaker.
Neither changes a current numerical boundary.  The new contribution is the
algebra-subquotient framework and the resulting precise tensor-complexity
frontier.

The note does not determine the tensor rank or border rank of the permanent
apolar multiplication tensor, prove smoothability or nonsmoothability, improve
the current unrestricted finite-`n` bounds, determine an exact Chow rank for
`n>=6`, or prove Glynn optimality.

## 1. Multiplication tensors

For a finite-dimensional unital algebra `A`, let

\[
\mu_A:A\otimes A\longrightarrow A
\]

be multiplication, viewed as a tensor in

\[
A^*\otimes A^*\otimes A.
\]

Write

\[
R(\mu_A)
\quad\text{and}\quad
\underline R(\mu_A)
\]

for its tensor rank and border rank after scalar extension to an algebraic
closure.  A lower bound after scalar extension is a lower bound for a
decomposition over the original characteristic-zero field.

### Lemma 1.1 -- algebra subquotients do not increase multiplication complexity

If `C` is a subalgebra of `A`, then

\[
R(\mu_C)\le R(\mu_A),
\qquad
\underline R(\mu_C)\le\underline R(\mu_A).
\tag{1.1}
\]

If `A` surjects onto an algebra `Q`, then

\[
R(\mu_Q)\le R(\mu_A),
\qquad
\underline R(\mu_Q)\le\underline R(\mu_A).
\tag{1.2}
\]

For finite direct products,

\[
R\!\left(\mu_{\prod_i A_i}\right)
\le\sum_iR(\mu_{A_i}),
\qquad
\underline R\!\left(\mu_{\prod_i A_i}\right)
\le\sum_i\underline R(\mu_{A_i}).
\tag{1.3}
\]

### Proof

For a subalgebra, restrict both input legs to `C` and compose the output with
any linear projection `A -> C` that is the identity on `C`.  For a quotient,
choose a linear section on the two input legs and apply the quotient map on the
output.  Tensor rank and border rank do not increase under linear maps on the
three tensor legs.  The multiplication tensor of a direct product is the
direct sum of the individual multiplication tensors, and concatenating
decompositions proves (1.3). ∎

No exact direct-sum additivity theorem is required.

## 2. Every Chow-term apolar algebra is a Boolean algebra subquotient

Let

\[
T=\ell_1\cdots\ell_n\in\operatorname{Sym}^nV
\]

be an arbitrary nonzero Chow term; the factors may be linearly dependent or
repeated.  Put

\[
R=\operatorname{Sym}(V^*)
\]

and let

\[
B_n
=
k[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2).
\tag{2.1}
\]

Define the algebra homomorphism

\[
\psi:R\longrightarrow B_n
\]

on a linear differential operator `alpha` by

\[
\psi(\alpha)
=
\sum_{i=1}^n\alpha(\ell_i)z_i.
\tag{2.2}
\]

Let

\[
C_T=\operatorname{im}\psi\subseteq B_n
\]

and let `lambda` be the coefficient of the top squarefree monomial

\[
z_1\cdots z_n.
\]

Define the homogeneous ideal

\[
\operatorname{Ann}_{C_T}(\lambda)
=
\{c\in C_T:\lambda(cC_T)=0\}.
\tag{2.3}
\]

### Theorem 2.1 -- Boolean algebra envelope

\[
\boxed{
A_T=R/T^\perp
\simeq
C_T/\operatorname{Ann}_{C_T}(\lambda).
}
\tag{2.4}
\]

In particular, `A_T` is a quotient of a subalgebra of `B_n`.

### Proof

For homogeneous differential operators `P,Q` whose degrees sum to `n`,
expanding (2.2) gives

\[
\lambda(\psi(P)\psi(Q))
=
(PQ)\mathbin{\lrcorner}T.
\tag{2.5}
\]

Both sides sum over assignments of the `n` differential factors to the `n`
linear factors of `T`; the square-zero relations retain exactly the bijective
assignments.

Now fix homogeneous `P`.  The polynomial `P \lrcorner T` is zero if and only
if every complementary differential operator `Q` kills it.  By (2.5), this is
equivalent to

\[
\lambda(\psi(P)\psi(Q))=0
\]

for every complementary `Q`, hence to

\[
\psi(P)\in\operatorname{Ann}_{C_T}(\lambda).
\]

Thus

\[
T^\perp
=
\psi^{-1}\!\left(\operatorname{Ann}_{C_T}(\lambda)\right),
\]

and the first isomorphism theorem proves (2.4).  The set in (2.3) is an ideal
because

\[
\lambda((ac)b)=\lambda(c(ab)).
\]

∎

For independent factors, `psi` identifies `C_T` with the whole Boolean
algebra and the top pairing is nondegenerate, so

\[
A_T\simeq B_n.
\tag{2.6}
\]

## 3. The apolar algebra of a sum is an algebra subquotient

Let

\[
f=T_1+\cdots+T_r
\]

and put

\[
I=\bigcap_{i=1}^rT_i^\perp.
\]

Then

\[
I\subseteq f^\perp.
\]

The natural algebra map

\[
R/I\longrightarrow\prod_{i=1}^rA_{T_i}
\]

is injective, while

\[
R/I\twoheadrightarrow A_f
\]

is surjective.  Hence `A_f` is an algebra quotient of a subalgebra of the
termwise direct product.

Combining this observation with Lemma 1.1 and Theorem 2.1 gives:

### Theorem 3.1 -- multiplication-tensor Chow inequality

\[
\boxed{
R(\mu_{A_f})
\le
rR(\mu_{B_n}),
\qquad
\underline R(\mu_{A_f})
\le
r\underline R(\mu_{B_n}).
}
\tag{3.1}
\]

Therefore

\[
\boxed{
\operatorname{ChowRank}(f)
\ge
\max\left\{
\left\lceil
\frac{R(\mu_{A_f})}{R(\mu_{B_n})}
\right\rceil,
\left\lceil
\frac{\underline R(\mu_{A_f})}
{\underline R(\mu_{B_n})}
\right\rceil
\right\}.
}
\tag{3.2}
\]

The denominator is exact as a maximum over one Chow term because an
independent-factor term realizes `B_n`.

This is not a linear flattening in `f`.  Its validity comes from the algebra
subquotient, not from matrix-rank subadditivity of a map linear in `f`.

## 4. Permanent apolar algebra as a diagonal Segre product

For row and column subsets of equal size, write

\[
e_{R,C}\in A_{\operatorname{perm}_n}.
\]

It is represented by any matching differential monomial from `R` to `C`.
Different matchings with the same row and column sets have the same class
because they give the same derivative of the permanent.  A differential
monomial with a repeated row or column is zero in the apolar algebra.

The product is therefore

\[
e_{R,C}e_{R',C'}
=
\begin{cases}
e_{R\cup R',\,C\cup C'},
&
R\cap R'=C\cap C'=\varnothing,
\\
0,
&
\text{otherwise}.
\end{cases}
\tag{4.1}
\]

Let `B_n[d]` be the degree-`d` Boolean level.  Equation (4.1) gives an algebra
isomorphism

\[
\boxed{
A_{\operatorname{perm}_n}
\simeq
B_n\#B_n
:=
\bigoplus_{d=0}^n B_n[d]\otimes B_n[d].
}
\tag{4.2}
\]

Consequently,

\[
\dim A_{\operatorname{perm}_n}
=
\sum_{d=0}^n\binom nd^2
=
\binom{2n}{n}.
\tag{4.3}
\]

The diagonal Segre product is a subalgebra of `B_n tensor B_n`.

## 5. Border multiplication baseline

The multiplication tensor of every unital algebra is concise: multiplication
by the unit makes both input flattenings injective, and the output is spanned
by products.  Hence

\[
\underline R(\mu_A)\ge\dim A.
\tag{5.1}
\]

For

\[
B_1=k[z]/(z^2),
\]

the multiplication tensor becomes the three-factor `W` tensor after swapping
the two output basis vectors.  It has border rank two because

\[
W
=
\lim_{\varepsilon\to0}
\frac{
(e_0+\varepsilon e_1)^{\otimes3}
-e_0^{\otimes3}
}{\varepsilon}.
\tag{5.2}
\]

Since

\[
B_n\simeq B_1^{\otimes n},
\]

border-rank submultiplicativity gives an upper bound `2^n`, while conciseness
gives the matching lower bound:

\[
\boxed{
\underline R(\mu_{B_n})=2^n.
}
\tag{5.3}
\]

Equations (3.2), (4.3), (5.1), and (5.3) prove (0.1).

This value is

\[
\frac{\binom{2n}{n}}{2^n},
\]

the same equal-weight all-degree ratio already identified by the scalar
derivative-profile audit.  The algebra framework has not yet extracted
additional border complexity.

## 6. Ordinary bilinear-complexity baseline

The algebra `A_(perm_n)` is connected graded and therefore local.  The
Alder--Strassen bound gives

\[
R(\mu_{A_{\operatorname{perm}_n}})
\ge
2\binom{2n}{n}-1.
\tag{6.1}
\]

The multiplication tensor of `B_1` is `W_3`, so that of `B_n` is
`W_3^{\otimes n}`.  Canino, Casarotti, and Santarsiero prove the explicit
tensor-rank upper bound

\[
R(W_{d_1}\otimes\cdots\otimes W_{d_k})
\le
2^{k-1}
(d_1+\cdots+d_k-2k+2).
\]

Taking every `d_i=3` gives

\[
R(\mu_{B_n})
\le
(n+2)2^{n-1}.
\tag{6.2}
\]

Combining (3.2), (6.1), and (6.2) proves (0.2).  A fully self-contained but
weaker fallback is

\[
R(\mu_{B_n})\le3^n,
\tag{6.3}
\]

obtained by tensoring the elementary three-product algorithm for `B_1`.

The asymptotic forms are

\[
\frac{\binom{2n}{n}}{2^n}
=
\left(1+o(1)\right)
\frac{2^n}{\sqrt{\pi n}},
\tag{6.4}
\]

and

\[
\frac{2\binom{2n}{n}-1}{(n+2)2^{n-1}}
=
\left(\frac4{\sqrt\pi}+o(1)\right)
\frac{2^n}{n^{3/2}}.
\tag{6.5}
\]

The border baseline is stronger and still below the central catalecticant by
an asymptotic factor `sqrt(2)`.

### External inputs

- The Alder--Strassen lower bound is recorded, for example, in Markus
  Bläser, *A Complete Characterization of the Algebras of Minimal Bilinear
  Complexity*, SIAM J. Comput. 34 (2004), 277--298.
- The `W`-product upper bound is S. Canino, A. Casarotti, and
  P. Santarsiero, *A new bound on the rank of tensor product of W-states*,
  arXiv:2512.05828 (2025).

No novelty is claimed for either external tensor-complexity theorem.

## 7. Route ceiling and the actual open problem

Since (4.2) embeds the permanent apolar algebra in

\[
B_n\otimes B_n,
\]

one has

\[
R(\mu_{A_{\operatorname{perm}_n}})
\le R(\mu_{B_n})^2
\]

and similarly for border rank.  Therefore the multiplication-tensor rank
ratios themselves satisfy

\[
\boxed{
\frac{R(\mu_{A_{\operatorname{perm}_n}})}
{R(\mu_{B_n})}
\le
R(\mu_{B_n}),
}
\tag{7.1}
\]

\[
\boxed{
\frac{\underline R(\mu_{A_{\operatorname{perm}_n}})}
{2^n}
\le
2^n.
}
\tag{7.2}
\]

The border ceiling is only a factor two above the conjectural Glynn value, so
this theorem does **not** close the route.

The concrete remaining questions are:

1. Is the algebra `A_(perm_n)` smoothable?  A positive answer would force its
   multiplication tensor to have minimal border rank and would close the
   border route at (0.1).
2. If it is not smoothable, how large is the border-rank excess above
   `binom(2n,n)`?
3. What is the ordinary bilinear complexity of the diagonal Segre algebra
   `B_n#B_n`, and how does it compare with that of `B_n`?
4. Can a homogeneous multiplication slice or an asymptotic tensor functional
   produce a larger ratio while retaining the termwise Boolean envelope?

These are algebra-structure questions not covered by the fixed-linear-map,
graded-`K_0`, Fitting, Betti, or full-orbit representation barriers.

## 8. Exact replay

The primary implementation verifies the Boolean top-pairing construction on
dependent and dependent factor examples, including

```text
x^4
x*y*(x+y)
x*y*z*(x+y+z)
x_1*x_2*x_3*x_4.
```

For every degree, the rank of the restricted Boolean top pairing equals the
direct catalecticant rank.

It also reconstructs the diagonal-Segre multiplication table through `n=6`
and checks the exact bound arithmetic through `n=40`.

```text
Boolean top-pairing checks                 19
permanent multiplication-table checks  84,720
associativity checks                    89,224
bound arithmetic checks                    120
```

The independent implementation uses modular catalecticants and a separately
constructed squarefree pairing:

```text
independent top-pairing checks              23
independent multiplication checks       56,540
independent arithmetic checks              150
```

The finite calculations replay the algebra interfaces.  They do not determine
any tensor rank.
