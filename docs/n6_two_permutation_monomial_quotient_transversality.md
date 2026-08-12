# Two permutation monomials remain quotient-Koszul transverse

## Status and scope

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

This is an exact characteristic-zero theorem for pairs of degree-six
permutation monomials in the 36 matrix variables.  It does not control pairs
of arbitrary coordinate monomials or arbitrary Chow terms.

## 1. Statement

For a permutation `sigma in S_6`, put

\[
 M_\sigma=\prod_{i=0}^5x_{i,\sigma(i)},
 \qquad Y_\sigma=\operatorname{im}K_3(M_\sigma),
\]

and let

\[
 Y_P=\operatorname{im}K_3(\operatorname{perm}_6).
\]

### Theorem 1.1

For every `sigma,tau in S_6`,

\[
 \boxed{(Y_\sigma+Y_\tau)\cap Y_P=0.}              \tag{1.1}
\]

Consequently, for `R=M_sigma+M_tau`,

\[
 \boxed{
 \Gamma_{\mathcal D_3(P)}(\mathcal D_3(R))
 =\operatorname{rank}K_3(R).
 }                                                   \tag{1.2}

Thus the full quotient-gain theorem extends from one term to every pair in
the permutation-monomial subfamily.

## 2. Reduction to eleven cases

Independent row and column permutations send the first permutation monomial
to the diagonal monomial.  The stabilizer of the diagonal acts on the relative
permutation by conjugation.  Hence an ordered pair is determined, for the
rank calculation, by the cycle type of `sigma^(-1) tau`.  There are eleven
partitions of six.

The central first-Koszul target decomposes under the row-column torus.  Every
column used below is homogeneous for the twelve-component weight consisting
of its six row counts and six column counts.  The permanent image decomposes
into 5,625 such weight blocks.  Exact rational elimination in each block gives

\[
 \dim Y_P=14175.
\]

Let `S=Y_id+Y_tau`.  The audit computes both `dim S` and

\[
 \dim\frac{Y_P+S}{Y_P}
\]

over `Q`.  Their difference is exactly `dim(S intersect Y_P)`.

## 3. Exact table

| relative cycle type | shared edges | `dim S` | quotient dimension | `eta` | `j` |
|---|---:|---:|---:|---:|---:|
| `1+1+1+1+1+1` | 6 | 705 | 705 | 705 | 0 |
| `1+1+1+1+2` | 4 | 1267 | 1267 | 143 | 0 |
| `1+1+1+3` | 3 | 1374 | 1374 | 36 | 0 |
| `1+1+2+2` | 2 | 1410 | 1410 | 0 | 0 |
| `1+1+4` | 2 | 1410 | 1410 | 0 | 0 |
| `1+2+3` | 1 | 1410 | 1410 | 0 | 0 |
| `1+5` | 1 | 1410 | 1410 | 0 | 0 |
| `2+2+2` | 0 | 1410 | 1410 | 0 | 0 |
| `2+4` | 0 | 1410 | 1410 | 0 | 0 |
| `3+3` | 0 | 1410 | 1410 | 0 | 0 |
| `6` | 0 | 1410 | 1410 | 0 | 0 |

Here

\[
 \eta=705+705-\dim S,
 \qquad
 j=\dim S-\dim((Y_P+S)/Y_P).
\]

Every row has `j=0`, proving (1.1).  Since

\[
 \operatorname{im}K_3(M_\sigma+M_\tau)
 \subseteq Y_\sigma+Y_\tau,
\]

the coupled image of the sum also meets `Y_P` trivially, which proves (1.2).

The table also separates internal overlap from collision with the permanent:
sharing four factors creates 143 internal output relations, and sharing three
creates 36, but neither overlap produces an aggregate collision with `Y_P`.

## 4. Exact certificate

Run

```bash
python scripts/n6_two_permutation_monomial_quotient_audit.py
python -m unittest tests.test_n6_two_permutation_monomial_quotient -v
```

The script reconstructs the integer Koszul columns and performs sparse
Gaussian elimination with `Fraction` in every row-column torus block.  The
finite-field routines in the earlier coordinate audit are not used for these
ranks.  The eleven cycle types, all block ranks, and the frozen summary are
reconstructed deterministically.

## 5. Boundary for lower 26

The theorem shows that the aggregate collision `j` from G-028 does not appear
for two permutation monomials.  It does not imply the same statement for:

- three or more permutation monomials;
- two coordinate monomials with repeated variables or non-permutation support;
- two arbitrary six-factor Chow terms; or
- the six, seven, or eight fixed terms in the lower-26 diagnostic.

Therefore it supplies a positive exact unit test for the quotient relation
budget, not an unrestricted lower-bound improvement.
