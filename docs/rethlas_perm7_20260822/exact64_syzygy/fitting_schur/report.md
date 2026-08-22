# Fitting/Schur audit of the degree-\(2\to3\) apolar presentation

## Status

*PRECISE NO-GO FOR PRESENTATION-ONLY FITTING, DETERMINANTAL, AND SCHUR CONSTRUCTIONS.*

No invariant satisfying the requested four gates was constructed. The
standard basis-free constructions from the finite-dimensional
degree-\(2\to3\) presentation are ruled out as follows.

1. A functorial selected subspace or quotient of the homology of a bare
   finite-dimensional presentation complex is necessarily either zero or
   the whole homology. Zero misses the permanent threshold, while the whole
   homology fails on the actual two-term common-factor example \(F_2\).
2. Fitting ideals and determinantal supports of an evaluated matrix over the
   ground field are only Boolean rank thresholds. They cannot select a
   proper part of the \(18816\)-dimensional target homology.
3. Exterior, symmetric, and general Schur functors of the homology fail the
   \(F_2\) gate, or, if their height makes every atom vanish, fail directly
   on Glynn's actual \(64\)-term decomposition.
4. The canonical scheme-theoretic Fitting support obtained from the
   quadratic apolar generators has degreewise capacity at most \(35\), far
   below \(64\).
5. In the bare span fork, the quotient-created target summand has no path to
   the term side. Independent rescaling of that summand forces every
   functorial linear coupling to be zero. Thus one-sided image/rank
   constructions remain below the sharp Glynn liftable ceiling \(18032\).

This is a structural no-go theorem for constructions depending only on the
presentation complex, its matrix-equivalence class, or polynomial functors
of its homology. It does **not** rule out a new invariant using additional
graded multiplication tensors or an explicitly constructed chain-level
operation coupling the two arrows of the apolar span diagram.

Throughout, the field has characteristic zero, \(V\) has dimension \(49\),
\(S=\operatorname{Sym}(V^*)\), and

\[
 H(f)=\operatorname{Tor}_2^S(A_f,\mathbb K)_3,
 \qquad A_f=S/\operatorname{Ann}(f).
\]

For an apolar ideal without linear generators this is the kernel of

\[
 \mu_f:V^*\otimes \operatorname{Ann}(f)_2\longrightarrow S_3,
 \qquad \xi\otimes q\longmapsto \xi q.
 \tag{0.1}
\]

When linear annihilators are present, one uses the canonical degree-three
strand after removing nonminimal generators; equivalently one uses the
degree-three homology of the minimal presentation complex. The categorical
arguments below apply to either model.

The exact numerical inputs, already independently audited in
results/perm7_complete_problem/g2b/hereditary_beta23_report.md, are

\[
\begin{array}{c|r}
\text{object}&\dim H\\ \hline
\operatorname{perm}_7&18816\\
\text{one independent Chow atom}&294\\
F_2=c\prod_{i=1}^6a_i+c\prod_{j=1}^6b_j&2016.
\end{array}
\tag{0.2}
\]

The target threshold for excluding \(63\) atoms is

\[
 63\cdot294+1=18523. \tag{0.3}
\]

For the \(64\)-term Glynn span algebra, only \(18032\) target classes lift
from the \(763\) common quadrics; the remaining \(784\) are created by the
quotient. A successful selection must therefore retain at least

\[
 18523-18032=491 \tag{0.4}
\]

of those created classes. On \(F_2\), the map to the two atom homologies has
rank \(540\) and kernel \(1476\), so a successful construction must kill at
least

\[
 2016-2\cdot294=1428. \tag{0.5}
\]

The permanent number in (0.2) is the specialization at \(n=7\) of the
complete statement of Alper--Rowlands, *Syzygies of the apolar ideals of the
determinant and permanent*, arXiv:1709.09286, Main Theorem (b) and
Proposition thm:dimensions-perm: the permanent's first syzygy module has
\(4\binom{n+1}{3}\binom{n+2}{3}\) linear generators and
\(2\binom n2\binom n4\) quadratic generators, with no other generator
degrees. Only the displayed numerical consequence is used here.

## 1. Rigidity of a functorial homology selection

### Lemma 1.1 (pointwise stabilizer)

Let \(C_\bullet\) be a bounded complex of finite-dimensional vector spaces.
For every \(i\), its chain-automorphism group contains a copy of
\(\mathrm{GL}(H_i(C))\) acting in the standard way on \(H_i(C)\).

### Proof

Split the complex as vector spaces. In degree \(i\) one may write

\[
 C_i=B_i\oplus H_i\oplus B_{i-1},
\]

so that the differential is the identity from the last summand to the copy
of \(B_{i-1}\) in degree \(i-1\), and is zero on \(B_i\oplus H_i\).
Every \(g\in\mathrm{GL}(H_i)\), extended by the identity on all boundary and
contractible summands, is a chain automorphism. ∎

Consequently, an isomorphism-natural subspace of \(H_i(C)\) is pointwise
either \(0\) or all of \(H_i(C)\), since those are the only subspaces
invariant under the full general linear group.

### Lemma 1.2 (hereditary subfunctor dichotomy)

Let \(F(C)\subseteq H_i(C)\) be natural for all chain maps between
finite-dimensional complexes. Then \(F=0\) on every complex or
\(F(C)=H_i(C)\) on every complex. The same dichotomy holds for a natural
quotient of \(H_i\).

### Proof

First restrict to complexes concentrated in degree \(i\). This gives a
subfunctor \(G(U)\subseteq U\) of the identity functor on vector spaces. If
\(0\ne u\in G(U)\), choose a functional \(p:U\to\mathbb K\) with
\(p(u)\ne0\). Naturality gives \(G(\mathbb K)=\mathbb K\). For arbitrary
\(w\in W\), the map \(\mathbb K\to W\), \(1\mapsto w\), then gives
\(w\in G(W)\). Hence \(G\) is the identity; otherwise it is zero.

For an arbitrary split complex, chain inclusion and projection between its
homology summand and the complex transfer the same conclusion to \(F(C)\).
A natural quotient is handled by applying the result to its kernel. ∎

### Corollary 1.3

No selected subspace or quotient of \(H(f)\) that is a functor of the bare
presentation complex can meet the requested gates. The zero choice has
permanent value \(0<18523\). The identity choice has

\[
 \dim H(F_2)=2016>588=2\cdot294.
\]

This corollary also explains why a Fitting-rank threshold cannot simply
declare some homology dimensions admissible and others inadmissible. Such a
threshold can be invariant under changes of bases, but it is not hereditary
for presentation maps.

## 2. Fitting ideals, minors, and rank profiles

### 2.1 An evaluated finite-dimensional matrix

Let \(\phi:\mathbb K^m\to\mathbb K^n\) have rank \(r\). The ideal generated
by its \(t\times t\) minors is

\[
 I_t(\phi)=
 \begin{cases}
 \mathbb K,&t\le r,\\
 0,&t>r.
 \end{cases}
\tag{2.1}
\]

Thus all Fitting ideals of \(\operatorname{coker}\phi\), and all their
supports over \(\operatorname{Spec}\mathbb K\), contain exactly the same
information as \(r\). A finite-dimensional arrow is classified up to
independent source and target bases by \((m,n,r)\), so no other
matrix-equivalence invariant can select a proper subspace of its kernel.

The ranks after the standard nonlinear operations are also determined by
\(r\):

\[
 \operatorname{rank}(\Lambda^a\phi)=\binom r a,
 \qquad
 \operatorname{rank}(\operatorname{Sym}^a\phi)
   =\binom{r+a-1}{a},
\tag{2.2}
\]

and, for a partition \(\lambda\),

\[
 \operatorname{rank}(\mathbf S_\lambda\phi)
 =\dim \mathbf S_\lambda(\mathbb K^r).
\tag{2.3}
\]

These nonlinear ranks are not subadditive. For example, if \(\phi_1\) and
\(\phi_2\) are rank-one maps on two direct blocks, then

\[
 \operatorname{rank}\Lambda^2(\phi_1\oplus\phi_2)=1,
 \qquad
 \operatorname{rank}\Lambda^2\phi_1+
 \operatorname{rank}\Lambda^2\phi_2=0.
\tag{2.4}
\]

Similarly, for \(a\ge2\), the symmetric-power ranks are \(a+1\) versus
\(1+1\). These are the smallest manifestations of the mixed terms in the
Cauchy/Littlewood--Richardson direct-sum formula. Ordinary matrix rank
\((a=1)\) retains subadditivity, but then the construction has returned to a
one-sided flattening and does not select the quotient-created homology.

### 2.2 The canonical graded Fitting support

One can instead retain the polynomial ring and use the \(S\)-linear row
presentation

\[
 S(-2)\otimes J_2(f)\longrightarrow S,
 \qquad e_q\longmapsto q.
\tag{2.5}
\]

Its zeroth Fitting ideal is exactly the ideal generated by \(J_2(f)\); all
higher Fitting ideals of this one-row presentation are the unit ideal.
Set-theoretically this still gives no separation in the three decisive
examples. The quadratic ideal contains the square of every coordinate for
\(\operatorname{perm}_7\), an independent atom, and \(F_2\), so the affine
support is the origin and the projective support is empty in all three
cases.

The scheme structure has more information but insufficient capacity. If
inactive linear variables are first removed, an independent atom has the
Boolean complete-intersection Hilbert vector

\[
 h_d(T)=\binom7d,
\]

whereas the permanent has

\[
 h_d(P)=\binom7d^2.
\]

Therefore every nonnegative Hilbert-profile weighting has target-to-atom
ratio at most

\[
 \max_d\frac{h_d(P)}{h_d(T)}
 =\max_d\binom7d=35. \tag{2.6}
\]

The total lengths are \(128\) and \(3432\), giving ratio less than \(27\).
If only the full ambient quadratic piece is imposed, rather than first
quotienting the inactive linears, the \(42\) inactive variables of an atom
survive only in degree one. The corresponding length is \(128+42=170\),
which makes the capacity even smaller.

For reference, the essential quadratic ideal of \(F_2\) is

\[
 (c^2,a_i^2,b_j^2,a_i b_j).
\]

Its quadratic quotient has length

\[
 1+13+2\sum_{d=2}^7\binom7d=254;
\]

adding the \(36\) inactive square-zero degree-one directions gives ambient
length \(290\le2\cdot170\). Thus this support scheme survives the \(F_2\)
test only because it has already fallen far below the permanent capacity
gate.

## 3. Schur and exterior functors of the homology

The following gate rules out every fixed Schur functor, not just low
exterior powers.

### Lemma 3.1 (tableau lower bound)

Let \(\lambda\ne\varnothing\) be a partition of height \(h\le n\). Then

\[
 \dim\mathbf S_\lambda(\mathbb K^n)\ge\binom nh. \tag{3.1}
\]

### Proof

For each \(h\)-subset \(a_1<\cdots<a_h\) of \([n]\), fill every box in row
\(i\) of the Young diagram by \(a_i\). The rows are weakly increasing and
the columns strictly increasing, so these are \(\binom nh\) distinct
semistandard tableaux. ∎

### Proposition 3.2 (Schur gate)

No reduced nonnegative direct sum of fixed Schur functors applied to
\(H(f)\) can simultaneously have atom cap \(294\), permanent value at least
\(18523\), and be subadditive on actual Chow sums.

### Proof

Consider first one nonempty partition \(\lambda\) of height \(h\).

If \(h\le294\), Lemma 3.1 applied to \(H(F_2)\cong\mathbb K^{2016}\) gives

\[
 \dim\mathbf S_\lambda(H(F_2))
 \ge\binom{2016}{h}\ge2016>588.
\tag{3.2}
\]

This violates the two-atom budget whenever the output on each atom is at
most \(294\).

If \(h>294\), the functor vanishes on every atom. If it is nonzero on the
permanent, Glynn's actual decomposition gives the incompatible inequality

\[
 0<\dim\mathbf S_\lambda(H(P))
 \le\sum_{i=1}^{64}\dim\mathbf S_\lambda(H(T_i))=0.
\tag{3.3}
\]

If \(h>18816\), it vanishes on the permanent too and misses the target.
Adding nonnegative Schur summands cannot repair either contradiction. The
word “reduced” only excludes a constant degree-zero summand, which is not a
subquotient of homology and would assign artificial positive charge to the
zero object. ∎

For exterior powers the exact cap-bearing degrees make the obstruction
especially visible:

\[
 \binom{294}{a}\le294,\quad 1\le a\le294,
 \qquad\Longleftrightarrow\qquad
 a\in\{1,293,294\}. \tag{3.4}
\]

At all three degrees, \(\binom{2016}{a}>2\binom{294}{a}\). For
\(295\le a\le2016\), the atoms vanish but \(F_2\) does not. For
\(2017\le a\le18815\), both the atoms and \(F_2\) vanish but the permanent
does not, so Glynn gives (3.3). Symmetric degree \(a\ge2\) already has atom
value

\[
 \binom{293+a}{a}>294,
\]

while degree one is the full, \(F_2\)-defeated homology.

Over characteristic zero, any polynomial functor built from finite tensor,
Schur, exterior, symmetric, direct-sum, and direct-summand operations
decomposes into nonnegative Schur summands. Proposition 3.2 therefore
covers precisely this standard polynomial-functor closure. Virtual
alternating differences are not dimensions of vector spaces and have no
automatic nonnegativity or hereditary injection theorem.

## 4. Why the bare span fork cannot supply the missing correction

Forget the algebra structure momentarily and retain the homology-level fork

\[
 X\xleftarrow{\alpha}R\xrightarrow{\beta}Y,
\tag{4.1}
\]

where \(X\) is target homology and \(Y\) is the direct sum of the atom
homologies.

### Lemma 4.1 (isolated-cokernel obstruction)

Using only the two arrows in (4.1), there is no nonzero natural linear map
from \(\operatorname{coker}\alpha\) to a subquotient formed from \(R\) and
\(Y\), nor conversely.

### Proof

Choose a vector-space splitting \(X=\operatorname{im}\alpha\oplus C\),
where \(C\cong\operatorname{coker}\alpha\). For every nonzero scalar \(t\),
the map acting by \(t\operatorname{id}\) on \(C\) and by the identity on
\(\operatorname{im}\alpha,R,Y\) is an automorphism of the fork. It acts
trivially on every subquotient formed from \(R,Y\). Naturality of a map
\(\theta:C\to Z\) would give
\(\theta(tc)=\theta(c)\); choosing \(t\ne1\) forces \(\theta=0\). The reverse
direction is identical. ∎

Equivalently, the quiver underlying (4.1) has no oriented path from the
isolated quotient-created summand at \(X\) to \(Y\). Exterior and Schur
functors merely add mixed tensor summands; they do not create a canonical
linear path, and Section 3 shows their dimensions violate the adversarial
gates.

For Glynn, the ordinary quotient-liftable image is at most \(18032\), below
\(18523\) by \(491\). For \(F_2\), following the ordinary Tor map to the two
terms reduces \(2016\) to rank \(540\le588\) by killing \(1476\) classes.
Lemma 4.1 pinpoints why these two desirable effects cannot be joined by a
standard Fitting/path-rank construction on the bare fork: the \(784\)
Glynn-created classes and the \(1476\)-dimensional \(F_2\) kernel live in
independently scalable summands with no connecting arrow.

This also delimits the conclusion. A new chain-level operation could in
principle use multiplication, commutativity homotopies, the Gorenstein
pairing, or another canonical tensor to create an additional arrow. Such
an operation would no longer be a Fitting/Schur invariant of the bare
degree-\(2\to3\) presentation, and its cap and heredity would need new
proofs.

## 5. Candidate audit table

| Construction | Outcome | Decisive gate |
|---|---|---|
| Fitting ideals of the evaluated \(\mathbb K\)-matrix | Only \(0\) or \(\mathbb K\), hence only rank | Cannot select \(18523\) of \(18816\) classes |
| Isomorphism-natural subspace of presentation homology | Pointwise \(0\) or all | \(0\) misses target; all gives \(2016>588\) on \(F_2\) |
| Hereditary subfunctor/subquotient of homology | Globally \(0\) or identity | Lemma 1.2 |
| Exterior/symmetric powers of a matrix | Mixed direct-sum terms; not subadditive | Rank-one block example (2.4) |
| Exterior/Schur functors of \(H(f)\) | Fail \(F_2\), or vanish on atoms and fail Glynn | Proposition 3.2 |
| Projective Fitting support of the quadratic quotient | Empty for target, atom, and \(F_2\) | Every coordinate square lies in the quadratic ideal |
| Scheme length/nonnegative Hilbert profile | Capacity at most \(35\) | Equation (2.6) |
| One-sided image/path rank through the span algebra | At most \(18032\) on Glynn | Misses threshold by \(491\) |
| Coupling bare-fork coker to bare-fork kernel | Natural map is zero | Independent-scaling Lemma 4.1 |

## 6. Surviving interface

The standard Fitting/Schur/determinantal branch is closed. A surviving
relative construction must do all of the following.

1. Use more than the matrix-equivalence class of the degree-\(2\to3\)
   presentation and more than a polynomial functor of \(H(f)\).
2. Produce an explicit new chain-level arrow that couples the quotient
   defect on \(A_f\leftarrow R\) to the injection kernel on
   \(R\to\bigoplus_i A_{T_i}\).
3. Retain at least \(491\) of the \(784\) quotient-created Glynn classes.
4. Kill at least \(1428\) of the \(2016\) \(F_2\) classes.
5. Preserve the uniform cap \(294\) for every dependent or repeated
   seven-factor atom, and prove the comparison for every actual
   decomposition, not merely for block-direct presentations.

No operation meeting these requirements was found in this branch.

## 7. Exact replay

Run

    python results/perm7_theory_first_20260822/exact64_syzygy/fitting_schur/fitting_schur_gate_replay.py

Expected marker:

    FITTING_SCHUR_GATE_REPLAY_PASS

The replay uses exact integer arithmetic and checks the \(F_2\), Glynn,
exterior-power, Schur-height, and Hilbert-capacity inequalities. The
naturality lemmas are elementary proofs over the characteristic-zero ground
field and do not rely on finite-field evidence.
