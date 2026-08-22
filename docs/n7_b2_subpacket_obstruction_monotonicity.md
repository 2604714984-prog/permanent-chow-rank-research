# Subpacket obstruction monotonicity for the labelled Packet-B complex

## Status

`GENERAL LINEAR-ALGEBRA THEOREM; CANONICAL TWO-TRANSPOSITION JOINS GLOBALLY NONCOMPLETABLE.`

This note corrects the former completion boundary of the exact two-transposition
join calculation.  A positive Packet-B coupling defect supported on a subset of
term blocks cannot be killed by appending more term blocks.  Consequently, the
canonical shared-row join with defect ten and the canonical disjoint join with
defect twelve are not merely bad four-term packets: neither can occur as an
exact subpacket of any larger Sylvester-equality completion.

## 1. Abstract labelled maps

Let `X` and `Y` be finite-dimensional vector spaces over an arbitrary field.
For each label `i` let `K_i` be a middle space and let

\[
 C_i:X\longrightarrow K_i,
 \qquad
 B_i:K_i\longrightarrow Y.
\]

For a finite label set `I`, put

\[
 K_I=\bigoplus_{i\in I}K_i,
 \qquad
 C_I=(C_i)_{i\in I}:X\longrightarrow K_I,
 \qquad
 B_I=\sum_{i\in I}B_i:K_I\longrightarrow Y.
\]

No assumption `B_I C_I=0` is required.  Define the middle obstruction space

\[
 \mathcal O_I
   =\frac{\ker B_I}{\ker B_I\cap\operatorname{im}C_I}.             \tag{1.1}
\]

Its dimension is the rank expression used in the Packet-B computations:

\[
 \dim\mathcal O_I
 =\dim K_I-\operatorname{rank}B_I-\operatorname{rank}C_I
       +\operatorname{rank}(B_I C_I).                              \tag{1.2}
\]

Indeed, the kernel of the restriction of `B_I` to `im(C_I)` has dimension
`rank(C_I)-rank(B_I C_I)`.

## 2. Subpacket monotonicity theorem

**Theorem.** If `I` is contained in `J`, zero extension

\[
 e_{I,J}:K_I\longrightarrow K_J
\]

induces an injective linear map

\[
 \overline e_{I,J}:\mathcal O_I\hookrightarrow\mathcal O_J.       \tag{2.1}
\]

In particular,

\[
 \dim\mathcal O_I\leq\dim\mathcal O_J.                            \tag{2.2}
\]

**Proof.** If `z` belongs to `ker(B_I)`, then

\[
 B_J e_{I,J}(z)=B_Iz=0,
\]

so zero extension maps `ker(B_I)` into `ker(B_J)`.  Suppose that the class of
`e_{I,J}(z)` vanishes in `O_J`.  Then there is an `x` in `X` such that

\[
 e_{I,J}(z)=C_Jx.
\]

Projecting this identity from `K_J` to the old coordinate summand `K_I` gives

\[
 z=C_Ix.
\]

Thus `z` already lies in `ker(B_I) intersect im(C_I)`, so its class in `O_I`
was zero.  This proves injectivity.  No rank semicontinuity or genericity
argument is involved.

### Full-equality consequence

If a full label packet `J` satisfies the Sylvester equality condition

\[
 \ker B_J\subseteq\operatorname{im}C_J,
\]

then `O_J=0`.  The theorem forces

\[
 \boxed{\mathcal O_I=0\quad\text{for every }I\subseteq J.}         \tag{2.3}
\]

Therefore every term subpacket of a full equality packet must itself have zero
coupling defect.  A positive defect is a hereditary obstruction, not a deficit
that later labels can repair.

## 3. Local-variable packets inside the ambient 49-variable system

The canonical joins were ranked in an eleven-variable space `W`, whereas a
full `perm_7` packet uses the ambient variable space `V`.  This does not weaken
the theorem.

For an old term whose factors lie in `W`, the ambient source map factors as

\[
 \operatorname{Sym}^3(V^*)
   \longrightarrow \operatorname{Sym}^3(W^*)
   \xrightarrow{\ C_i^W\ }K_i.                                  \tag{3.1}
\]

The first arrow is restriction and is surjective.  Hence

\[
 \operatorname{im}C_i^V=\operatorname{im}C_i^W,                   \tag{3.2}
\]

and the same is true after stacking any fixed old label set.  The `B_i` maps
also have the same ranks after the target is embedded into the ambient target.
Thus the eleven-variable defects inject unchanged into every 49-variable
completion containing those exact terms.

## 4. Canonical two-transposition corollaries

The frozen exact joins give the following rank data.

```text
join type              dim K   rank B   rank C   rank BC   dim O
shared (01),(02)         140      111       94        75       10
disjoint (01),(23)       140      114       95        81       12
```

By (2.1), every larger labelled packet containing the shared-row join has
obstruction dimension at least ten, and every packet containing the disjoint
join has obstruction dimension at least twelve.  Therefore

\[
 \boxed{\text{neither canonical join admits any Sylvester-equality completion}.}
                                                                    \tag{4.1}
\]

An additional rank-seven term cannot reduce either defect.  Nor can any number
of later terms.  The former proposal to compute a one-term "defect-killing
subspace" is therefore unnecessary and invalid as a completion mechanism.

## 5. Corrected Packet-B frontier

This theorem does **not** close the full equality locus.  It excludes exact
subpackets containing the two canonical four-term joins.  A surviving pair of
transposition-slice identities would have to be coupled already inside its
four terms so that its four-term obstruction is zero; cross-slice factor mixing
cannot be postponed to later labels.

The next exact gate is therefore:

```text
classify zero-defect four-term cross-slice couplings
subject to the U0Q7 identity, U1Q6 zero condition,
and the two U2Q5 transposition targets.
```

Any candidate with positive four-term defect should be discarded immediately,
without constructing additional Packet-B blocks.

## 6. Exact replay boundary

The theorem is the written projection argument above.  The script performs two
separate checks:

1. exhaustive verification over `F_2` for all `4096` three-scalar-block systems
   with two-dimensional source and target, covering `49,152` strict subset
   inequalities; and
2. exact reuse of the frozen rational join ranks to produce the global
   noncompletion corollaries.

The finite check is a regression, not the proof of the general theorem.

```text
python scripts/n7_b2_subpacket_obstruction_monotonicity.py \
  --verify-json data/n7_b2_subpacket_obstruction_monotonicity.json
python -m unittest tests.test_n7_b2_subpacket_obstruction_monotonicity -v
```

## Claim boundary

```text
subpacket obstruction monotonicity                 PROVED
field restriction                                  NONE
canonical shared-row join completion               IMPOSSIBLE
a canonical disjoint join completion               IMPOSSIBLE
arbitrary four-term cross-slice coupling            OPEN
full Packet B equality locus                        OPEN
B2-CLOSED                                           false
new lower-50 result                                 false
border-rank claim                                   false
```
