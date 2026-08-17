# Stabilizer-efficient equivariant orbit envelopes still have ceiling one

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_INTEGER_REPLAYED`.

This note strengthens the full-orbit representation barrier. Instead of
indexing a Chow summand by every group element, it removes all duplicate
projective copies and uses the smallest orbit allowed by the summand's actual
projective apolar stabilizer.

Even after this optimization, every nonnegative exact-additive graded
isotype profile has permanent/one-term ratio at most one.

The theorem introduces no numerical Chow-rank lower bound and is not an upper
bound on actual Chow rank. It does not cover fixed natural maps linear in the
input form, minimal or persistence syzygy functors, nonlinear determinantal
data, valuative arguments, or Chow-realizability defects.

## 1. Projective apolar stabilizers

Let a finite group `G` act linearly on a characteristic-zero vector space
`V`, and put

\[
R=\operatorname{Sym}(V^*).
\]

For a nonzero form `T`, define its projective apolar stabilizer by

\[
H_T
=
\{g\in G:g(T^\perp)=T^\perp\}.
\tag{1.1}
\]

Because a homogeneous Artinian Gorenstein apolar ideal determines its inverse
system line, this is equivalently the projective stabilizer of `[T]`.

The group `H_T` acts on the graded apolar algebra

\[
A_T=R/T^\perp.
\]

Define the stabilizer-efficient orbit envelope

\[
\mathcal O(T)
=
\operatorname{Ind}_{H_T}^{G} A_T
\simeq
\bigoplus_{gH_T\in G/H_T} A_{gT}.
\tag{1.2}
\]

The direct sum is indexed by distinct projective apolar ideals, not by all
group elements.

## 2. Efficient equivariant apolar subquotient

### Theorem 2.1

Let `f` be `G`-invariant and suppose

\[
f=T_1+\cdots+T_r.
\]

Then `A_f` is a graded `G`-equivariant subquotient of

\[
\bigoplus_{i=1}^{r}\mathcal O(T_i).
\tag{2.1}
\]

### Proof

For each summand put `H_i=H_(T_i)` and define

\[
J
=
\bigcap_{i=1}^{r}
\bigcap_{gH_i\in G/H_i}
g(T_i^\perp).
\tag{2.2}
\]

The ideal `J` is `G`-stable. Since the identity coset occurs in every orbit,

\[
J
\subseteq
\bigcap_i T_i^\perp
\subseteq
f^\perp.
\]

Consequently there is a graded `G`-equivariant algebra surjection

\[
R/J\twoheadrightarrow A_f.
\tag{2.3}
\]

The diagonal map

\[
R/J
\longrightarrow
\bigoplus_{i,gH_i}R/g(T_i^\perp)
\tag{2.4}
\]

is injective because its kernel is precisely `J`. The target is the direct
sum in (2.1), with the natural induced `G`-action. Combining (2.3) and (2.4)
proves the subquotient statement. ∎

No equivariant section is used.

## 3. Exact-additive graded isotype scalars

Over characteristic zero, every finite-dimensional `G`-representation is
semisimple. Let `Irr(G)` denote the irreducible representations.

A nonnegative exact-additive graded isotype scalar is an expression

\[
\Phi(M)
=
\sum_{d}
\sum_{U\in\operatorname{Irr}(G)}
c_{U,d}\,m_{U,d}(M),
\qquad
c_{U,d}\ge0,
\tag{3.1}
\]

where `m_(U,d)(M)` is the multiplicity of `U` in `M_d`.

It is additive on direct sums and nonincreasing under graded equivariant
submodules and quotients. Theorem 2.1 therefore gives

\[
\Phi(A_f)
\le
\sum_{i=1}^{r}\Phi(\mathcal O(T_i)).
\tag{3.2}
\]

Thus this route can prove at most

\[
r
\ge
\frac{\Phi(A_f)}
{\displaystyle\max_T\Phi(\mathcal O(T))}.
\tag{3.3}
\]

## 4. Generic independent Chow terms have trivial stabilizer

Now take

\[
G=S_n\times S_n
\]

acting on the matrix-variable space

\[
V_n=\operatorname{span}\{x_{rc}:1\le r,c\le n\}.
\]

### Proposition 4.1

For every `n>=2`, the independent-factor locus of the degree-`n` Chow variety
contains a term with trivial projective `G`-stabilizer.

### Proof

The Chow variety is irreducible, and the locus of products of `n` linearly
independent factors is nonempty and Zariski open.

For every nonidentity `g in G`, its projective fixed locus on the Chow variety
is proper. Indeed the action of `G` on `V_n` is faithful, so one can choose a
linear form `ell` such that `g ell` is not proportional to `ell`; then
`g(ell^n)` is not proportional to `ell^n`.

The union of the finitely many nonidentity fixed loci is a proper closed
subset of the irreducible Chow variety. Its complement meets the
independent-factor open locus because the field is infinite. ∎

For such a term `T`, one has

\[
H_T=\{1\}
\]

and

\[
A_T\simeq B_n
=
k[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2).
\tag{4.1}
\]

Therefore

\[
\mathcal O(T)
\simeq
k[G]\otimes B_n.
\tag{4.2}
\]

In degree `d`, every irreducible `U` occurs with multiplicity

\[
(\dim U)\binom nd.
\tag{4.3}
\]

## 5. The permanent numerator

For the permanent,

\[
(A_{\operatorname{perm}_n})_d
\simeq
M_d\boxtimes M_d,
\tag{5.1}
\]

where `M_d` is the permutation module on `d`-subsets. In characteristic zero,

\[
M_d
\simeq
\bigoplus_{i=0}^{\min(d,n-d)}
S^{(n-i,i)}.
\tag{5.2}
\]

Thus every row-column irreducible pair present in degree `d` occurs with
multiplicity exactly one.

## 6. Ceiling one

### Theorem 6.1

For every nonnegative exact-additive graded isotype scalar `Phi`,

\[
\boxed{
\frac{
\Phi(A_{\operatorname{perm}_n})
}{
\displaystyle\max_T\Phi(\mathcal O(T))
}
\le1.
}
\tag{6.1}
\]

### Proof

Use the trivial-stabilizer independent-factor term from Proposition 4.1 as a
denominator witness.

For each irreducible `U` occurring in the permanent degree `d`, the numerator
multiplicity is one. The generic orbit envelope multiplicity is

\[
(\dim U)\binom nd
\ge1.
\]

The inequality therefore holds coefficient by coefficient in (3.1), and hence
after summing all nonnegative weights. ∎

Consequently the stabilizer-efficient exact-additive representation route
cannot prove even

\[
\operatorname{ChowRank}(\operatorname{perm}_n)\ge2.
\]

## 7. Why removing duplicate orbit copies does not help

A highly symmetric Chow term can have a much smaller orbit than `|G|`.
For example, a permutation-matching term has a large diagonal stabilizer.
The efficient envelope correctly exploits that fact.

However, the denominator in a uniform Chow-rank inequality is the maximum
over **all** Chow terms. The independent-factor Chow locus also contains
terms with trivial stabilizer. Their efficient orbit is already the full
regular envelope, and it dominates every nonnegative exact-additive isotype
profile strongly enough to force (6.1).

Thus the regular-representation tax is not an artifact of indexing duplicate
copies. It is forced by the existence of generic trivial-stabilizer terms.

## 8. Exact finite replay

The primary audit constructs deterministic independent factor frames and
checks every element of `S_n x S_n` for `2<=n<=5`:

```text
group elements checked             15,016
trivial projective stabilizers          4
```

It independently verifies hook dimensions and the regular multiplicity
inequality through `n=12`:

```text
partition dimension checks             270
pointwise isotype checks               921
weighted support checks                341
```

A second implementation uses a different deterministic factor family,
modular Gaussian elimination and a standard-tableau recursion:

```text
group elements checked             15,016
partition dimension checks             137
pointwise isotype checks               508
block checks                              9
```

These computations replay the finite interface. The general theorem is the
ideal-intersection construction and the generic fixed-locus argument.

## 9. Research decision

The following route is now closed:

```text
full-group orbit exact-additive profiles
distinct-orbit / stabilizer-efficient exact-additive profiles
graded exact-additive row-column isotype multiplicities
finite nonnegative combinations of those profiles
```

A representation-sensitive continuation must avoid exact-additive orbit
envelopes. Remaining interfaces include:

1. fixed natural maps linear in the input form;
2. minimal or persistence syzygy functors not determined by `K_0`;
3. nonlinear joint determinantal data;
4. valuative flat-sum information; and
5. uniform Chow-realizability defects.
