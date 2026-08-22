# Applying the forty-nine-plane theorem at the two endpoint layers

**Status.** `PURE_ENDPOINT_APPLICATION`, `EXACT_INTEGER_PROFILE_REPLAY`,
`B31_AND_B49_EXCLUDED` (N6-075). The base field is algebraically closed of
characteristic zero.

Assume the N6-074 fixed-six reduction of a hypothetical minimum 28-term
ordinary Chow decomposition of \(\operatorname{perm}_6\). This note reconnects the N6-073
forty-nine-plane extension theorem to two distinct occurrences of a
49-dimensional permanent cubic intersection.

## 1. The hereditary \(b=31\) layer

For the 22 residual terms put

\[
 U_i=\mathcal D_3(T_i),\qquad
 L_A=\sum_{i\in A}U_i,\qquad \ell_A=\dim L_A,
\]

and let \(S=E_3\cap G_3\), where \(G_3\) is their coupled middle space. For
every residual six-subset \(A\), distinguish

\[
 f_A:=\dim(S\cap L_A),\qquad x_A:=\dim(E_3\cap L_A).          \tag{1.1}
\]

Thus \(f_A\leq x_A\); they are not interchangeable. N6-074 gives
\(\dim S\geq400-31=369\).

### 1.1 Initial hereditary bounds

The six-term quadratic projection cap is \(78\), while the exact product
shadow at dimension \(53\) is \(81\). Hence \(x_A\leq52\). Let \(B\) be any
residual 16-subset and \(C=B^c\). The map \(S\to L_{[22]}/L_C\) has kernel
\(S\cap L_C\) and image of dimension at most \(\ell_B\). Therefore

\[
 \ell_B\geq\dim S-f_C\geq369-52=317.                         \tag{1.2}
\]

Enlarging any six-set \(A\) to such a \(B\), the ten added terms contribute at
most \(200\), so

\[
 \ell_A\geq317-200=117.                                      \tag{1.3}
\]

If \(x_A=51\) or \(52\), its exact product shadow is \(78\), equal to the
quadratic projection cap. The defect-zero equality interface gives the
common-\(W_{12}\) configuration and the N6-044 prolongation cap \(436\). But

\[
 \dim(E_3+L_A)=400+\ell_A-x_A
 \geq
 \begin{cases}
 466,&x_A=51,\\
 465,&x_A=52,
 \end{cases}
 >436.                                                        \tag{1.4}
\]

Thus every six-set satisfies \(x_A\leq50\).

### 1.2 First level: exclude \(f_A=50\)

Suppose \(f_A=50\) for some \(A\). Then
\(S\cap L_A=E_3\cap L_A\) is a 50-plane. Also every complementary six-set
\(C\) has \(f_C\leq x_C\leq50\), so (1.2) improves to

\[
 \ell_B\geq369-50=319                                        \tag{1.5}
\]

for every 16-set \(B\). N6-031 says that a non-full individual middle rank is
at most \(18\). A 16-set containing such a term would have literal dimension
at most \(15\cdot20+18=318\), contradicting (1.5). Hence every \(U_i\) has
dimension \(20\). Enlarging the chosen \(A\) to a 16-set now gives

\[
 \ell_A\geq319-10\cdot20=119.                                \tag{1.6}
\]

For \(X=E_3\cap L_A\), the product-shadow lower bound is \(75\). Put
\(F_i=\mathcal D_2(T_i)\),
\(a_2=\dim(E_2\cap\sum_iF_i)\), and
\(t_2=\dim\sum_iF_i-a_2\). Since \(75\leq a_2\leq78\), the omitted-factor
defect is at most \(3\), so some \(\varepsilon_i=0\). If that term had
\(\alpha_i\leq2\), the \(t_2\leq15\) prolongation cap would be \(458\), but

\[
 \dim(E_3+L_A)\geq400+119-50=469>458.                         \tag{1.7}
\]

Thus \(\alpha_i=3\), and its quotient image has dimension
\(12-\varepsilon_i+\alpha_i=15\). The bounds
\(15\leq t_2\leq90-75=15\) force

\[
 (d_2,a_2,t_2)=(90,75,15),\qquad
 \varepsilon=(0^6),\qquad\kappa_2=0.                        \tag{1.8}
\]

Applying the same \(458<469\) cap to the remaining terms forces all six
\(\alpha_i=3\). Consequently the \(F_i\) are literal direct and project
isomorphically onto a common \(W_{15}\). Differentiating a relation among the
\(U_i\), then using the directness of the \(F_i\), shows that the \(U_i\) are
direct. Hence \(\ell_A=120\); symmetry of the middle catalecticants identifies
the literal and coupled middle spaces. N6-064 supplies the flag hook for this
50-plane, and the N6-069/N6-061/N6-059/N6-072 chain contradicts it. Therefore
no \(f_A=50\) exists.

### 1.3 Second level: force literal directness, then exclude \(x_A=50\)

The 16-term capacity gives \(f_A\geq369-320=49\), while the preceding step
gives \(f_A\leq49\). Thus every \(f_A=49\). Applying the exact sequence behind
(1.2) once more yields

\[
 369\leq\dim S\leq f_C+\ell_B\leq49+320=369.                 \tag{1.9}
\]

Hence \(\dim S=369\), every 16-term literal sum has dimension \(320\), and is
therefore direct. Every six-set lies in a 16-set, so \(\ell_A=120\) for every
six-set \(A\). Now \(49=f_A\leq x_A\leq50\). If \(x_A=50\), repeat the profile
argument (1.7)--(1.8), now with

\[
 \dim(E_3+L_A)=400+120-50=470>458.                            \tag{1.10}
\]

It again produces the all-\(\alpha=3\), common-\(W_{15}\), literal-direct
50-plane and is contradicted by N6-064 followed by
N6-069/N6-061/N6-059/N6-072. Therefore every \(x_A=49\).

Finally, for \(X=E_3\cap L_A\), the same profile argument has required
prolongation dimension

\[
 400+120-49=471>458.                                         \tag{1.11}
\]

It forces (1.8) and all six \(\alpha_i=3\). Since the product-shadow lower
bound is \(75\) and \(a_2=75\), now—and only now—

\[
 K:=\partial X=E_2\cap\sum_iF_i,\qquad \dim K=75.             \tag{1.12}
\]

This is the 49-plane input for N6-073.

## 2. The original fixed-six \(b=49\) layer

Here the shadow and defect budget are again \(75\) and \(3\). The exact replay
finds \(13\) scalar states. Twelve contain an \(\varepsilon\)-zero term with
\(\alpha\leq2\) and have \(t_2\leq14\); their required prolongation dimensions
are strictly larger than the applicable caps \(436\), \(440\), or \(453\).

The thirteenth scalar state has \(t_2=15\). If any one of its \(\alpha\)-values
is at most \(2\), the applicable \(t_2=15\) cap is \(458\), still strictly
below the required dimension \(471\). Therefore its only pre-geometric
survivor is

\[
 \varepsilon_i=0,\quad\alpha_i=3,\quad\kappa_2=0,
 \qquad(d_2,a_2,t_2,h)=(90,75,15,120).
\tag{2.1}
\]

The value \(h=120\) equals the total individual middle capacity. Thus the six
middle images are literal direct, and the symmetric-map argument from
Section 1 identifies their literal sum with the coupled middle space. This
again produces an actual 49-plane \(X=E_3\cap H_3\), six literal-direct
quadratic spaces, and one common quotient \(W_{15}\).

## 3. The shared geometric contradiction

For either endpoint, differentiation and the equality dimensions give

\[
 K:=\partial X=E_2\cap\sum_iF_i,\qquad\dim K=75.
\tag{3.1}
\]

N6-073 extends \(X\) to an N6-064 fifty-plane with the same first shadow.
Therefore

\[
 \dim\partial K=23,
\]

and \(\partial K\) is a genuine flag hook, in one of the two orientations.

Let \(s_i:W\to F_i\) be the six quotient sections. The five anchored
difference spaces \((s_i-s_1)(W)\), for \(i=2,\ldots,6\), are direct and span
\(K\). More generally, for every \(i\ne j\), the difference space
\((s_i-s_j)(W)\) is a 15-plane of permanent quadrics, and its first shadow lies
in the sum of the corresponding two factor spans, of dimension at most \(12\).
The universal 15-plane shadow lower bound is \(12\), so equality holds: all
factor spans are six-dimensional and every pair is transverse. Moreover
\(\partial K\) is their sum.

The pure block proof of N6-069 now re-applies to every transverse pair. If
any row or column block is invertible, that pair is commonly separated. The
common-quotient domain argument of N6-061, Section 4, then propagates the
separation to all six frames; its proof uses only \(F_i\subset q^{-1}(W)\),
not the numerical value \(50\). N6-059 would then bound the local permanent
cubic intersection by \(40\), contradicting \(49\).
Therefore every row and column block is singular. N6-072 proves that six
actual all-singular frames cannot lie over a genuine flag hook. This is the
final contradiction in both cases.

Hence N6-075 excludes

\[
 \boxed{b=31\quad\text{and}\quad b=49.}
\]

The current fixed-six frontier is

\[
 \boxed{32\leq b\leq48.}
\]

## 4. Boundary and replay

N6-073 does not classify 47- or 48-dimensional shadow-75 planes. In
particular it cannot yet be applied at \(b=32\) or \(b=48\) without a new
48-to-49 or 48-to-50 same-shadow extension theorem. This note does not prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\geq29\) and makes no
border-rank claim.

```text
python scripts/n6_lower29_b31_b49_exclusion.py \
  --verify-json data/n6_lower29_b31_b49_exclusion.json
python -m unittest tests.test_n6_lower29_b31_b49_exclusion -v
```
