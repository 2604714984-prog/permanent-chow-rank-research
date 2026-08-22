# Common-base mixed-split rigidity of Glynn compression

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_DICTIONARY_RIGIDITY`, `GENERAL_LOWER_BOUND`,
`QUARTIC_EQUALITY_CLASSIFIED`.

Fix a common deleted sign `u`, but allow every compressed atom to choose its
own split of the `m` columns into `m-2` shared columns `J` and two tail columns
`K`. For `v!=u`, define

\[
C_{v,u,J}
=
\bigotimes_{j\in J}v_j
\otimes
\left(
\bigotimes_{k\in K}v_k-\bigotimes_{k\in K}u_k
\right).
\]

Each atom belongs to one degree-`m+2` Chow derivative block. This family is
strictly larger than the original one-term compression because the split may
vary independently from atom to atom.

### Theorem

For every `m>=3`, a representation of the Glynn permanent tensor by these
common-base mixed-split atoms requires at least

\[
\boxed{2^{m-1}-1}
\]

atoms. If equality holds, every nonbase sign occurs once and all atoms use one
common column split. Thus the minimal representations are exactly the ordinary
one-term Glynn compressions, with the choices of common base and common split.

At `m=4`, one fixed base gives a 42-atom dictionary. Its exact threshold is
seven, and the only seven-atom representations are the six uniform-split
formulas. Across eight bases there are 48 minimal formulas. No six-atom
common-base mixed-split representation exists.

This does not yet allow the deleted base and the column split to vary
simultaneously, and it does not prove `mu(6,4)=7`.

## 1. Quotient lower bound

Apply the quotient

\[
q_j:V_j\to V_j/\mathbf k u
\]

in every column mode. The base-tail product in every atom contains `u` in two
modes and vanishes. The source product maps to

\[
\bar v^{\otimes m},
\]

independently of the chosen split.

After a diagonal sign normalization take `u=(1,...,1)`. The nonzero quotient
vectors are the nonzero Boolean indicator vectors `1_S` in `k^(m-1)`. Their
degree-`m` Veronese tensors are independent. For each nonempty subset `A`,
choose `a in A` and the degree-`m` monomial

\[
x_a^{m-|A|+1}\prod_{i\in A\setminus\{a\}}x_i.
\]

Its value at `1_S` is one exactly when `A subset S`. The resulting evaluation
matrix is the zeta matrix of the nonempty subset poset, triangular with diagonal
one. Hence all `2^(m-1)-1` quotient directions are necessary.

Equality therefore uses exactly one atom for each nonbase sign, with its Glynn
coefficient.

## 2. Highest defect layer forces one split

The quotient lower bound does not see the base-tail defects. Expand them by the
number of modes projected away from `u`. For a split `J`, the highest component
has quotient-degree `m-2` and equals

\[
\bar v^{\otimes(m-2)}
\]

in exactly the modes of `J`. Different `J` lie in distinct multigraded
components. Thus for every split separately, the signs assigned to that split
must satisfy a signed degree-`m-2` relation.

On the nonzero Boolean points of dimension `d=m-1`, degree `d-1` tensors have
rank `2^d-2`. Indeed, nonempty proper subset zeta monomials give that many
independent rows. Their unique relation is the full-support Walsh relation.
Therefore a subset carrying the fixed Glynn coefficients can sum to zero only
when it is empty or contains every nonbase sign.

The split groups partition the nonbase signs. Exactly one group is full, so all
atoms use the same split.

For `m=4`, the relation can also be read entrywise. If `a_S` indicates whether
a nonempty subset `S subset [3]` belongs to one split group, off-diagonal
entries give

\[
a_{ij}=a_{123},
\]

and diagonal entries then give `a_i=a_(123)`. All seven indicators are equal.

## 3. Exact quartic replay

The primary and independent implementations check all

\[
6^7=279,936
\]

assignments of one of six splits to each of the seven nonbase signs. Exactly six
assignments work:

```text
(0,0,0,0,0,0,0)
...
(5,5,5,5,5,5,5)
```

No mixed assignment survives.

Frozen core:

```text
b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b
```

## Strict boundary

```text
common-base arbitrary-split threshold = 2^(m-1)-1
quartic fixed-base dictionary atoms = 42
quartic threshold = 7
quartic minimal formulas per base = 6
variable base and variable split simultaneously = OPEN
arbitrary six derivative blocks = OPEN
mu(6,4) = OPEN IN [6,7]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
