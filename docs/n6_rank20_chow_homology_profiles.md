# Exact third-Koszul homology profiles of rank-20 Chow terms

**Status.** `EXACT_CHARACTERISTIC_ZERO_REPLAY`, `ROUTE_BARRIER`,
`CANDIDATE_FITTING_INTERFACE` (G-035).  This note does not prove lower 27.
The ordinary interval remains

\[
26\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## 1. Question and result

N6-032 proves that a hypothetical 26-term decomposition forces a twenty-term
residual with middle-catalectic rank at least 384, and that at least twelve of
its summands have individual middle rank 20.  N6-035 computes

\[
\dim H_{3,6}(\operatorname{perm}_6)=40
\]

for the middle third-Koszul complex.  A tempting continuation would assign to
every full-middle-rank Chow term the same scalar homology contribution as an
independent term.  G-035 shows that this is false.

Let

\[
T=\ell_1\ell_2\ell_3\ell_4\ell_5\ell_6,
\qquad L=\langle\ell_1,\ldots,\ell_6\rangle,
\qquad d=\dim L.
\]

For `0<=p<=3`, write

\[
H_p(T;L)=
\frac{
 \ker\bigl(
  \delta_{3,p}:\mathcal D_3(T)\otimes\Lambda^pL
  \longrightarrow
  \mathcal D_2(T)\otimes\Lambda^{p+1}L
 \bigr)
}{
 \operatorname{im}\bigl(
  \delta_{4,p-1}:\mathcal D_4(T)\otimes\Lambda^{p-1}L
  \longrightarrow
  \mathcal D_3(T)\otimes\Lambda^pL
 \bigr)
}.
\tag{1.1}
\]

### Theorem 1.1 -- four exact profiles

The following four displayed sextic Chow terms all have
`dim D_3(T)=20`.  Their exact characteristic-zero profiles are:

| configuration | `d` | `(dim D_2,dim D_3,dim D_4)` | `(dim H_0,H_1,H_2,H_3)` | `dim H_(3,6)(T;V_36)` | `rank delta_(3,3)(T;V_36)` |
|---|---:|---:|---:|---:|---:|
| six independent factors | 6 | `(15,20,15)` | `(0,0,0,20)` | 20 | 133,545 |
| five-span support-5 normal form | 5 | `(15,20,15)` | `(0,0,10,10)` | 320 | 133,245 |
| five-span support-4 normal form | 5 | `(14,20,14)` | `(0,1,20,20)` | 1,105 | 133,055 |
| bracket-open four-span witness | 4 | `(10,20,10)` | `(0,25,48,25)` | 13,961 | 122,682 |

The factors used by the replay are

\[
\begin{array}{ll}
d=6:&e_1,e_2,e_3,e_4,e_5,e_6,\\
d=5, s=5:&e_1,e_2,e_3,e_4,e_5, e_1+e_2+e_3+e_4+e_5,\\
d=5, s=4:&e_1,e_2,e_3,e_4,e_5, e_1+e_2+e_3+e_4,\\
d=4:&e_1,e_2,e_3,e_4,
 e_1+e_2+e_3+e_4,
 e_1+2e_2+3e_3+4e_4.
\end{array}
\tag{1.2}
\]

The two five-dimensional rows are the dependence normal forms from N6-031.
The last row is one exact point of the bracket-open four-dimensional stratum.
It is not asserted to be a normal form for every point of that open stratum.

In particular, middle rank 20 does not determine scalar third-Koszul
homology.  The independent-term value 20 cannot be used as a universal upper
bound for the other full-middle-rank strata.

## 2. Exact construction

The script expands the six displayed integer linear factors, differentiates
the resulting sextic by every monomial differential operator, and obtains
exact bases of `D_2(T)`, `D_3(T)`, and `D_4(T)`.  It then constructs the two
integer differentials in (1.1).  Sparse Gaussian elimination over `Fraction`
gives the following middle and preceding ranks:

| configuration | `rank delta_(3,p)`, `p=0..3` | `rank delta_(4,p-1)`, `p=0..3` |
|---|---:|---:|
| six independent | `(20,105,216,190)` | `(0,15,84,190)` |
| five-span support 5 | `(20,85,121,69)` | `(0,15,69,121)` |
| five-span support 4 | `(20,85,115,65)` | `(0,14,65,115)` |
| four-span witness | `(20,45,36,10)` | `(0,10,36,45)` |

Subtracting these two ranks from
`20 binom(d,p)` gives the four active homology rows in Theorem 1.1.

Now embed `L` in the 36-dimensional permanent variable space and choose
`V=L direct_sum W`.  Because `T` has zero derivative in every `W` direction,
the complex splits by the number of inactive exterior factors.  Therefore

\[
H_{3,6}(T;V)
\simeq
\bigoplus_{p=0}^3
H_p(T;L)\otimes\Lambda^{3-p}W,
\tag{2.1}
\]

and

\[
\dim H_{3,6}(T;V)
=\sum_{p=0}^3
 \binom{36-d}{3-p}\dim H_p(T;L).
\tag{2.2}
\]

The same direct-sum decomposition gives

\[
\operatorname{rank}\delta_{3,3}(T;V)
=\sum_{p=0}^3
 \binom{36-d}{3-p}
 \operatorname{rank}\delta_{3,p}(T;L),
\tag{2.3}
\]

which yields the final two columns of Theorem 1.1.  Thus no large
36-variable matrix is stored or eliminated.

## 3. Twenty factor-labelled cycles

The scalar Betti number forgets structure that is present in a factored Chow
term.  For every three-subset `S` of the six labelled factor positions put

\[
z_S=
\left(\prod_{i\in S}\ell_i\right)
\otimes
\left(\bigwedge_{i\in S}\ell_i\right)
\in \mathcal D_3(T)\otimes\Lambda^3L.
\tag{3.1}
\]

The Leibniz rule gives

\[
\delta_{3,3}(z_S)=0,
\tag{3.2}
\]

because each differentiated factor is wedged with the same factor already
present in the exterior product.  All twenty vectors in (3.1) are nonzero
and independent for the four configurations in (1.2).  Define the labelled
map

\[
\Phi_T:\mathbf k^{\binom63}\longrightarrow H_3(T;L),
\qquad e_S\longmapsto[z_S].
\tag{3.3}
\]

Exact elimination gives

| configuration | `rank span{z_S}` | `rank Phi_T` |
|---|---:|---:|
| six independent | 20 | 20 |
| five-span support 5 | 20 | 10 |
| five-span support 4 | 20 | 16 |
| four-span witness | 20 | 20 |

Thus even this canonical labelled family can partially become a boundary
under factor dependence.  Its scalar rank is not a uniform 20 either.
Nevertheless the presentation-valued map itself and its behavior in a colored
direct sum retain more information than the total homology dimension.  Over
the factor-parameter ring one can form the corresponding universal labelled
family and its Fitting ideals; that parameter-family construction, rather
than the rank of a fixed-field linear map, remains a legitimate candidate
interface for the twenty-term hereditary residual.  No subadditivity or
permanent comparison for that family is proved here.

## 4. Consequence and exact boundary

G-035 rules out the following shortcut:

> every middle-rank-20 Chow term has the independent-term scalar
> `H_(3,6)` contribution 20, so the twelve full terms in N6-032 can be
> counted uniformly.

The displayed four-span term is already a characteristic-zero counterexample,
with scalar homology dimension 13,961.  This does not rule out every possible
use of Koszul homology.  A successful successor may use the factor-labelled
map (3.3), a multigraded initial module, a representation-valued quotient, or
the equation-specific coupling with the six-term complement.  It cannot use
central rank 20 alone to replace all full terms by the independent profile.

Evidence classification:

- pure mathematics: the cycles (3.1), their vanishing (3.2), and the inactive
  splitting (2.1)--(2.3);
- exact computation certificate: all derivative dimensions and displayed
  ranks are integer matrices eliminated over `Fraction`, hence exact over
  `Q` and every characteristic-zero extension;
- finite-field or random evidence: none;
- unresolved: any Fitting, multigraded, or representation-theoretic inequality
  strong enough to exclude the N6-032 twenty-term residual.

## 5. Replay

Run

```text
python scripts/n6_rank20_chow_homology_profiles.py \
  --json data/n6_rank20_chow_homology_profiles.json
python -m unittest tests.test_n6_rank20_chow_homology_profiles -v
```

Expected marker:

```text
G035_RANK20_CHOW_HOMOLOGY_PROFILES_PASS
```
