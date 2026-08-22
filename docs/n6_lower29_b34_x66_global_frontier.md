# The global \(b=34,\ x_A=66\) frontier

**Status.** PURE_GLOBAL_B34_TO_HEREDITARY_X66_REDUCTION,
EXACT_FIXED_SIX_AND_RELATION_ENVELOPE_REPLAY (N6-100).

This note connects the global fixed-six arithmetic to the local N6-080
packet. It is a strict reduction, not an exclusion of \(b=34\).

## 1. Every seven-set is an equality set

Under a hypothetical 28-term decomposition in the \(b=34\) branch, the
residual central space \(S\) satisfies

\[
 \dim S\ge400-34=366.
\tag{1.1}
\]

For any residual seven-set \(A\), let \(L_A\) be its literal cubic sum and
put

\[
 f_A=\dim(S\cap L_A),\qquad x_A=\dim(E_3\cap L_A).
\]

The complementary fifteen terms have total capacity 300, so N6-074 gives

\[
 66\le f_A\le x_A.
\tag{1.2}
\]

N6-099 gives \(x_A\le66\). Hence equality holds throughout for every
seven-set:

\[
 \boxed{f_A=x_A=66}.                                       \tag{1.3}
\]

Equality in the dimension estimate behind (1.2) also gives

\[
 \dim S=366,\qquad \dim L_{A^c}=300
\tag{1.4}
\]

for every \(A\). Thus every fifteen residual cubic images are 20-dimensional
and literal direct. Every subfamily of at most fifteen terms is therefore
literal direct; in particular \(\dim L_A=140\). The symmetric catalectic
kernel lemma identifies the coupled seven-term image with this literal sum.

Consequently every seven-set lies in one of the thirteen exact N6-080
defect-six states, not merely one specially selected seven-set.

## 2. A critical six-set

Apply the quotient deletion argument of N6-099 inside any seven-set \(A\).
It selects a six-subset \(C\subset A\) for which

\[
 a_C:=\dim\left(E_2\cap\sum_{i\in C}F_i\right)\le75.
\tag{2.1}
\]

The complementary sixteen cubic spaces have capacity 320, so

\[
 \dim(S\cap L_C)\ge366-320=46.                              \tag{2.2}
\]

If \(x_C:=\dim(E_3\cap L_C)\ge47\), choose a 47-plane inside that
intersection. Since \(m_{47}=75\), (2.1) is equality. The
quadratic-dimension-90 case enters N6-078 and the N6-064 flag hook, hence is
excluded by N6-069/N6-072. In the only secondary equality case the
quadratic sum has dimension 89 and quotient dimension 14; the six cubic
spaces are literal direct of dimension 120. Since \(m_{53}=81>75\), their
permanent intersection has dimension at most 52, so the required
prolongation is at least

\[
 400+120-52=468>453,
\]

contradicting the \(t_2=14\) cap.

If instead the quadratic sum has dimension 90 and quotient dimension 15
but contains a term with \(\alpha\le2\), quadratic directness gives the same
120-dimensional cubic sum and the same lower bound 468, now contradicting
the \(t_2=15\) cap 458. The only equality case reaching flag-hook rigidity
therefore consists of six full \(\alpha=3\) terms with common \(W_{15}\).

Thus (2.2) is equality:

\[
 \boxed{\dim(S\cap L_C)=x_C=46}.                            \tag{2.3}
\]

The product-shadow theorem gives

\[
 72=m_{46}\le\dim\partial(E_3\cap L_C)\le a_C\le75.          \tag{2.4}
\]

Equality in (2.2) also forces the complementary sixteen terms to be literal
direct of total dimension 320.

## 3. Strict boundary

The former broad \(b=34\) branch has therefore become a hereditary equality
configuration:

- every seven-set is a \(66\)-plane in one of thirteen exact N6-080 states;
- every seven-set contains a critical six-set satisfying (2.3)--(2.4);
- the complementary sixteen cubic images are literal direct.

The first unresolved object is now the actual Chow/common-section geometry
of a six-term 46-plane whose quadratic shadow has dimension 72 through 75.
Dimension counting alone does not exclude this layer.

This does not prove ordinary lower 29, determine the exact rank, or make a
border-rank claim.

Replay:

    python scripts/n6_lower29_b34_x66_global_frontier.py --verify-json data/n6_lower29_b34_x66_global_frontier.json
    python -m unittest tests.test_n6_lower29_b34_x66_global_frontier -v
