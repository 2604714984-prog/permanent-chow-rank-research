# Adversarial review: factor-span zero blocks

## Verdict

```text
MATHEMATICAL_STATUS=PASS_AS_INTERNAL_PROOF_DRAFT
EXISTING_PERMANENT_SHADOW_DEPENDENCY=EXPLICIT
STRICT_INEQUALITY_REQUIRED=true
COUPLED_LITERAL_FIREWALL=PASS
QUOTIENT_EXACTNESS=PASS
NEW_NUMERICAL_CHOW_BOUND=false
EXTERNAL_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed statements are the zero-block theorem

\[
\dim\left(\sum_iL_i\right)<m^2
\Longrightarrow
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i)=0
\]

and its projection and quotient consequences.

## 1. Dependency boundary

The permanent-side lower bound

\[
0\ne f\in\mathcal D_m(\operatorname{perm}_n)
\Longrightarrow
\dim\partial^{m-1}f\ge m^2
\]

is not new in this PR.  It is the `d=m-1` case of the derivative-shadow
theorem in `docs/general_n_koszul_bounds.md`.

The new contribution is to use the actual joint factor span

\[
L_I=\sum_iL_{T_i}
\]

instead of the coarser term-count estimate.  The documentation and ledger must
preserve this attribution.

## 2. Strictness

The proof needs

\[
\dim L_I<m^2.
\]

At equality, the two shadow inequalities are compatible.  The theorem gives
no conclusion when

\[
\dim L_I=m^2.
\]

In particular:

- `n=4,m=2` same-span blocks are not covered;
- `n=8,m=4` pairs with disjoint eight-dimensional factor spans are not
  covered;
- no implementation may change `<` to `<=`.

The tests explicitly retain these boundary failures.

## 3. Degenerate Chow terms

The zero-block theorem does not require independent factors.  For every Chow
term,

\[
\mathcal D_m(T)\subseteq\operatorname{Sym}^mL_T
\]

where \(L_T\) is the span of its factors.  Repetitions only lower
\(\dim L_T\).

The sharper literal cap

\[
\dim(\mathcal D_m(T)\cap\mathcal D_m(U))
\le\binom km
\]

uses the squarefree derivative space of an independent frame.  It is not
promoted for arbitrary degenerate terms.

## 4. Coupled versus literal spaces

For a polynomial sum \(R=\sum_iT_i\), only

\[
\mathcal D_m(R)
\subseteq
\sum_i\mathcal D_m(T_i)
\]

is used.  No equality is asserted.

The zero result for the larger literal sum implies the zero result for the
coupled image, so the direction is safe.  Conversely, the proof does not use a
coupled zero result to infer a literal one.

## 5. Projection lemma

Let

\[
A=E_m\cap\sum_iF_i
\]

and choose a section of the literal sum map over \(A\).  If the projection of
a selected lift to labels outside \(I\) vanishes, the lift is supported on
\(I\), and its sum lies in

\[
E_m\cap\sum_{i\in I}F_i=0.
\]

Because the lift map is a section, the original vector is zero.  Hence the
projection is injective.

No direct-sum assumption among the \(F_i\) is needed.

## 6. Quotient exactness

The equality

\[
\rho(F)\cap\rho(G)=\rho(F\cap G)
\]

requires the stronger hypothesis

\[
E_m\cap(F+G)=0,
\]

not merely \(E_m\cap F=E_m\cap G=0\).

The factor-span theorem supplies exactly the stronger hypothesis when
\(\dim(L_T+L_U)<m^2\).  Under it, equal quotient classes have representatives
whose difference is zero, so the matched-difference image vanishes.

## 7. Literal cap for unequal spans

The identity

\[
\operatorname{Sym}^mL_T\cap\operatorname{Sym}^mL_U
=
\operatorname{Sym}^m(L_T\cap L_U)
\]

is verified by a direct multigrading after choosing complementary subspaces.

For an independent frame \(T\), the dimension of

\[
\mathcal D_m(T)\cap\operatorname{Sym}^mK
\]

is at most \(\binom{\dim K}{m}\).  The torus-orbit closure of \(K\) in the
Grassmannian contains a coordinate plane; intersection dimension with the
fixed squarefree space is upper semicontinuous, so specialization gives an
upper bound in the correct direction.

This statement is not claimed sharp for arbitrary \(K\).

## 8. Relation to previous work

The universal two-term consequence when \(2n<m^2\) can also be recovered from
the older term-count zero-intersection criterion.  It is therefore not the
principal novelty.

The genuine refinement is:

1. actual factor-span dimension replaces `number of terms times n`;
2. arbitrarily many same-span terms may form one certified zero block;
3. the quotient exactness statement closes the matched-difference map on all
   low-total-span strata;
4. the unequal-span literal cap can then be used without an unaccounted
   quotient kernel.

## 9. Strongest objection

The result may remove large low-span clusters while leaving the extremal
decompositions entirely in the boundary or high-span strata.  That objection
is valid.  The theorem does not itself improve a Chow-rank number.

Its value is structural: it closes the same-span matched-difference problem
and reduces the next search to the equality/high-span locus, most concretely

\[
n=8,\quad m=4,\quad
\dim L_T=\dim L_U=8,\quad
L_T\cap L_U=0.
\]

The project should not enlarge the combinatorial state machinery before this
boundary case is understood.
