# The fixed-six integer frontier for lower 29

**Status.** `PURE_FIXED_SIX_REDUCTION`, `EXACT_INTEGER_REPLAY`,
`LOWER_29_ARITHMETIC_FRONTIER` (N6-074). The base field is algebraically
closed of characteristic zero.

Assume a hypothetical minimum 28-term ordinary Chow decomposition of
`perm_6`. Fix six terms by the usual contracted-submodular averaging argument
and write \(b\) for their coupled middle intersection with
\(E_3=\mathcal D_3(\operatorname{perm}_6)\).

This note freezes the arithmetic frontier. It does not add a product-shadow
equality classification.

## 1. Scalar formulas

If \(r\) is the maximum individual middle rank, the selected six-term middle
rank \(h\) satisfies

\[
 h\geq\left\lceil\frac{4000-118r-10b}{17}\right\rceil,
 \qquad
 h\leq2b+22r-400.
\tag{1.1}
\]

For \(r=16,17,18\), scalar feasibility forces respectively
\(b\geq67,56,45\). Their fixed-six quadratic projection caps are
\(58,58,68\), whereas the exact product shadow permits respectively only
\(b\leq31,31,41\). Thus these branches are impossible. N6-031 excludes
\(r=19\), so \(r=20\).

For \(r=20\), (1.1) first becomes feasible at \(b=22\), where both sides
equal 84. The six-term projection cap 78 and the exact product shadow give
\(b\leq52\). Hence the initial integer window is

\[
 \boxed{22\leq b\leq52.}
\tag{1.2}
\]

## 2. Literal residual subsets

Let \(S=E_3\cap G_3\), where \(G_3\) is the coupled middle space of the 22
residual terms. The double-quotient identity gives

\[
 \dim S\geq400-b.
\tag{2.1}
\]

For any residual \(q\)-subset \(A\), its complement has literal middle
capacity \(20(22-q)\). Therefore

\[
 x_A:=\dim(E_3\cap L_A)
 \geq\dim(S\cap L_A)\geq20q-40-b.
\tag{2.2}
\]

Before the ambient \(225\)-dimensional cap saturates, the omitted-factor
quadratic projection bound is

\[
 \dim\left(E_2\cap\sum_{i\in A}F_i\right)\leq15q-12.
\tag{2.3}
\]

The exact replay evaluates the product-shadow minimum at every positive
floor in (2.2), for every \(b=28,\ldots,46\) and \(q\leq15\). No choice of
\(q\) gives a strict shadow contradiction.

For \(q=6\), (2.2) gives \(x_A\geq80-b\). At \(b=22,\ldots,27\), the
corresponding shadows are strictly larger than 78, so these layers are
excluded. At \(b=28,29\), the floors are 52 and 51 and both shadows equal
78. Equality forces six extremal, literal-direct quadratic spaces with one
common quotient \(W_{12}\); the N6-044 prolongation cap excludes both
layers.

At \(b=30\), every residual six-subset has \(x_A\geq50\). The cases
\(x_A=51,52\) reduce to the preceding \(W_{12}\) contradiction. The case
\(x_A=50\) is the all-alpha-three common-\(W_{15}\) endpoint; N6-064 supplies
the fifty-plane flag hook and N6-072 excludes it. Thus \(b=30\) is excluded.

At \(b=31,32,33\), the literal-six floors are respectively \(49,48,47\).
All lie on the product-shadow-75 plateau. The existing fifty-plane theorem
does not classify these lower-dimensional equality strata.

## 3. The next subset frontiers

Among \(q\leq15\), the least shadow defect for \(b=32,33\) remains at
\(q=6\), giving the 48- and 47-plane portions of the shadow-75 plateau. At
\(b=34,35\), the displayed tie-breaking choice is \(q=7\): the floors 66 and
65 have exact shadow 87 against projection cap 93. The frozen JSON records
the full table through \(b=46\). The same larger-\(q\) tie-breaking convention
selects \(q=7\) at \(b=37,38\); no defect or conclusion changes.

These nonnegative defects are frontier data, not contradictions.

## 4. High layers and strict boundary

The inherited scalar and actual-term prolongation caps leave one
all-alpha-three state at each of \(b=47,48,49,50\). N6-064 and N6-072
exclude only \(b=50\), because their flag-hook input is a theorem about a
fifty-plane. They do not exclude \(b=47,48,49\). The defect-zero
\(b=51,52\) states have \(t_2=12\) and are excluded by the extremal
prolongation cap.

Consequently the presently proved fixed-six frontier is exactly

\[
 \boxed{b=31,32,\ldots,49.}
\tag{4.1}
\]

This is not a proof that
\(\operatorname{ChowRank}(\operatorname{perm}_6)\geq29\), and no
47-, 48-, or 49-plane equality classification is inferred from a numerical
shadow value.

## 5. Replay

```text
python scripts/n6_lower29_fixed_six_arithmetic.py \
  --verify-json data/n6_lower29_fixed_six_arithmetic.json
python -m unittest tests.test_n6_lower29_fixed_six_arithmetic -v
```

The script imports the exact N6-056 Ferrers dynamic program. The test also
recomputes the shadow-75/78 plateau independently.
