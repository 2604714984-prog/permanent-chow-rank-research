# Quotient rigidity of the explicit near-extremal star family

**Status.** `PURE_STAR_QUOTIENT_DISTANCE_THEOREM`,
`EXACT_QQ_REGRESSION`, `CONDITIONAL_SUBLOCUS_EXCLUSION` (N6-045).  This note
excludes explicit star-family subloci inside the remaining `b=61,62,63`
states.  It does not classify the full `alpha=1` locus, exclude any complete
scalar state, or prove `ChowRank(perm_6)>=27`.

Let

\[
 V=A\otimes B,
 \qquad E_2=\mathcal D_2(\operatorname{perm}_6),
 \qquad q:\operatorname{Sym}^2V\longrightarrow
 \operatorname{Sym}^2V/E_2.
\]

We work in characteristic zero.

## 1. The explicit star family

Choose two coordinate rows `r,s`, three coordinate columns

\[
 C=\{c_0,c_1,c_2\},
\]

an outside column `t notin C`, a subset `J subset C` with `|J|>=2`, and
`lambda!=0`.  Put

\[
 w_c=b_c+\mathbf1_{c\in J}\lambda b_t
 \quad(c\in C)
\]

and take the six factors

\[
 \ell_{ic}=a_i\otimes w_c,
 \qquad i\in\{r,s\},\ c\in C.
\tag{1.1}
\]

The transposed construction is included as well.  Write

\[
 F_T=\mathcal D_2(T)
 =\langle\ell_u\ell_v:u<v\rangle,
 \qquad W_T=q(F_T).
\]

N6-043 proves for every term in (1.1) that

\[
 \dim F_T=15,
 \qquad \dim(E_2\cap F_T)=2,
 \qquad \boxed{\dim W_T=13.}
\tag{1.2}
\]

## 2. A three-frame recovery lemma

For independent vectors `w_0,w_1,w_2` define

\[
 R(w)=\langle w_0w_1,w_0w_2,w_1w_2\rangle.
\tag{2.1}
\]

### Lemma 2.1

The subspace `R(w) subset Sym^2 B` determines the unordered projective frame

\[
 \{[w_0],[w_1],[w_2]\}.
\]

### Proof

The span of all first derivatives of all quadrics in `R(w)` is

\[
 L=\langle w_0,w_1,w_2\rangle,
\]

so `L` is intrinsic.  If `z_0,z_1,z_2` is the dual basis, then in
`Sym^2 L^*`

\[
 R(w)^\perp=\langle z_0^2,z_1^2,z_2^2\rangle.
\tag{2.2}
\]

The only Veronese points in the plane on the right are the three axes.  In
fact, if

\[
 (d_0z_0+d_1z_1+d_2z_2)^2
 \in\langle z_0^2,z_1^2,z_2^2\rangle,
\]

then `2d_i d_j=0` for every `i!=j`, so at most one `d_i` is nonzero.  Thus
(2.2) recovers the three dual axes, and duality recovers the unordered
projective frame.  \(\square\)

For the normalized star vectors in Section 1, the recovered frame also
recovers all star data.  At least two frame lines have two-point coordinate
supports `\{c,t\}`.  Their common coordinate is the unique center `t`; the
other endpoints recover `J`, a possible singleton recovers `C-J`, and the
coefficient ratios recover `lambda`.  Hence two normalized stars have the
same `R(w)` only when all their data agree, up to the irrelevant ordering of
the three factors.

## 3. Quotient distance

The permanent quadratic space contains only monomials using two distinct
rows and two distinct columns.  Therefore the quotient retains the canonical
same-row summands

\[
 D_i=\operatorname{Sym}^2(a_i\otimes B)
 \subset \operatorname{Sym}^2V/E_2
\]

and the analogous same-column summands.  Let `pi_i` denote projection to
`D_i`.

For a row-oriented star term on rows `r,s`, row-weight decomposition gives

\[
 W_T=R_r\oplus R_s\oplus C_{rs},
 \qquad
 \dim(R_r,R_s,C_{rs})=(3,3,7),
\tag{3.1}
\]

where each of `R_r,R_s` is a copy of (2.1).  The last dimension follows from
(1.2).

### Theorem 3.1 -- star quotient distance

For two terms `T,T'` in the row-oriented or transposed explicit star family,

\[
 \boxed{
 W_T\ne W_{T'}
 \quad\Longrightarrow\quad
 \dim(W_T\cap W_{T'})\le11.
 }
\tag{3.2}
\]

Moreover,

\[
 \boxed{W_T=W_{T'}\Longrightarrow F_T=F_{T'}.}
\tag{3.3}
\]

### Proof

First suppose both terms are row-oriented.  If their two row pairs are
different, their row-weight supports have at most one common same-row block,
so their intersection has dimension at most three.  Suppose the row pairs
are equal.  If their three-spaces `R(w)` are equal, Lemma 2.1 and the star
support recovery following it give the same six projective factor lines.
Consequently `F_T=F_{T'}` and `W_T=W_{T'}`.  Otherwise

\[
 \dim(R(w)\cap R(w'))\le2.
\]

Using (3.1) in the three distinct row-weight blocks gives

\[
 \dim(W_T\cap W_{T'})
 \le2+2+7=11.
\tag{3.4}
\]

The column-oriented case follows by transposition.

It remains to compare opposite orientations.  Let `pi_D` be projection onto
the sum of all same-row blocks.  For a row-oriented term,

\[
 \dim\ker(\pi_D|W_T)=7,
\]

and its image consists of two three-dimensional row blocks.  For a
column-oriented star, its outside row contributes a three-dimensional block
`Sym^2` of the two active columns, while each of its three base rows
contributes one line.  Hence the intersection of the two projected spaces has
dimension at most

\[
 3+1=4.
\]

For `Z=W_T\cap W_{T'}`, rank-nullity applied to `pi_D|Z` now gives

\[
 \dim Z\le7+4=11.
\]

This also prevents equality across opposite orientations and completes both
(3.2) and (3.3).  \(\square\)

## 4. Coupling consequence for `b=61,62,63`

Let

\[
 \mathcal W=(E_2+H_2)/E_2,
 \qquad \dim\mathcal W=t_2.
\]

Every surviving N6-041 state has

\[
 t_2\le14,
 \qquad \kappa_2\le2,
\tag{4.1}
\]

where

\[
 \kappa_2
 =\dim\ker\left(
 \bigoplus_{i=1}^6F_i\longrightarrow\sum_{i=1}^6F_i
 \right).
\tag{4.2}
\]

If two `(epsilon,alpha)=(0,1)` terms belong to the explicit star family,
then their thirteen-dimensional quotient spaces lie in `mathcal W`.  Thus

\[
 \dim(W_i\cap W_j)
 \ge13+13-t_2
 \ge12.
\tag{4.3}
\]

Theorem 3.1 forces `W_i=W_j` and then `F_i=F_j`.  But the kernel in (4.2)
contains

\[
 \{(f,-f):f\in F_i\},
\]

so `kappa_2>=dim F_i=15`, contradicting (4.1).  We have proved:

### Corollary 4.1

In any surviving `b=61,62,63` fixed-six state, at most one
`(epsilon,alpha)=(0,1)` term can belong to the explicit N6-043 star family.

The exact N6-041 table contains the following state-contingent subloci to
which this corollary applies:

| `b` | all canonical states | states with at least two `(0,1)` entries | their `t_2` distribution |
|---:|---:|---:|---:|
| 61 | 73 | 37 | `22` at 13, `15` at 14 |
| 62 | 11 | 5 | `5` at 13 |
| 63 | 11 | 5 | `5` at 13 |

For each row, the excluded sublocus is the locus where at least two of the
displayed `(0,1)` terms are members of the explicit star family.  The table
does **not** say that the 37, 5, or 5 complete scalar states are excluded.
Other components of the unclassified `alpha=1` locus may still realize them.

## 5. Exact regression and boundary

The replay performs a separate exact-`QQ` regression at the standard two-row
support.  For the four choices of `J` and
`lambda in {-2,-1,1,2}`, all sixteen quotient spaces are distinct.  Their
pairwise intersection histogram is

\[
 \{5:78,\ 7:42\},
\]

and the corresponding full quadratic-space intersection histogram is

\[
 \{4:78,\ 6:42\}.
\]

This finite replay checks the formulas but is not a premise of Theorem 3.1.

Run

```text
python scripts/n6_near_extremal_star_quotient_rigidity.py \
  --json data/n6_near_extremal_star_quotient_rigidity.json
python -m unittest tests.test_n6_near_extremal_star_quotient_rigidity -v
```

No floating-point, random, or finite-field computation is used.
