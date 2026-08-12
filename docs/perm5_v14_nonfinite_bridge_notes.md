# Reviewer-facing non-finite bridges for the v14 `perm_5` proof

## Status and scope

This note extracts two characteristic-zero arguments that are already used in
the frozen v14 manuscript and reviewer packet.  It is intended to make the
external-review boundary explicit.  It does not replace the exact finite
certificates, does not call the proof program-free, and does not assert that an
independent human review has been completed.

The two interfaces are:

1. the passage from orbit-0 tangent rigidity to the completed local ring;
2. the relative-Grassmannian specialization used in the five `d=11,12`
   annihilator states.

## 1. Orbit-0 formal column rigidity

Let `k` be a characteristic-zero field.  The column group used at the orbit-0
point is

\[
G=T_B\rtimes S_5,
\]

where `T_B` is a torus.  Thus `G` is linearly reductive.

### Formal linearization lemma

**Lemma.** Let a linearly reductive algebraic group `G` act continuously by
`k`-algebra automorphisms on a complete Noetherian local `k`-algebra
`(R,m)`.  If `G` acts trivially on `m/m^2`, then it acts trivially on `R`.

**Proof.** Multiplication gives a `G`-equivariant surjection

\[
\operatorname{Sym}^d(m/m^2)\longrightarrow m^d/m^{d+1}.
\]

The source is a trivial representation, so every graded quotient
`m^d/m^{d+1}` is trivial.  Induct on `N` in

\[
0\longrightarrow m^{N-1}/m^N
\longrightarrow R/m^N
\longrightarrow R/m^{N-1}
\longrightarrow0.
\]

Linear reductivity splits this sequence `G`-equivariantly.  Both the kernel and
the quotient are trivial representations, hence `R/m^N` is trivial for every
`N`.  Finally,

\[
R\simeq\varprojlim_N R/m^N
\]

because `R` is complete and separated.  Therefore every element of `G` acts as
the identity on `R`.  \(\square\)

### Application to orbit 0

The exact tangent graph has 4,100 vertices, 3,820 one-term equations, 3,960
two-term equations, and tangent-kernel dimension eight over every field.  The
surviving variables have identical column source and target, and the column
containment graph identifies all copies.  Consequently the column torus has
weight zero on the tangent space, while `S_5` only permutes equal-coefficient
components.  Hence `G` acts trivially on the Zariski tangent space.

Apply the lemma to the completed local ring of the full flag incidence at the
orbit-0 point.  The entire formal neighbourhood, not only its first tangent
space, is fixed by `G`.  Column-weight decomposition and `S_5`-transitivity may
therefore be applied to a formal arc and give the tensor-product form used in
the manuscript:

\[
S=U_1\otimes B_3,\qquad
T=R_1\otimes B_2,\qquad
\dim U_1=2,\quad \dim R_1=5,\quad \partial S=T.
\]

The later Boolean shortening and `2215>2205` argument is applied only after
this all-orders statement.  No inference from tangent dimension alone is used.

## 2. The relative `d=11,12` annihilator bridge

Let `S` be a cubic space, let `T` be a quadratic space with
`partial S subset T`, and let `L subset V` have dimension at most five.  Define

\[
W_L=\operatorname{span}\{\partial_xs:s\in S, x\in L^\perp\}\subset T.
\]

For `alpha in T^*`, let

\[
A_\alpha=(1\otimes\alpha)\circ\delta_S:S\longrightarrow V,
\]

where `delta_S:S -> V tensor T` is total differentiation.  Then

\[
W_L^\perp
=\{\alpha\in T^*:A_\alpha(S)\subset L\}.                 \tag{2.1}
\]

This identity converts the required codimension estimate into a closed
incidence statement.

### Closed incidence and retained rank

On

\[
\operatorname{Gr}(5,V)\times\operatorname{Gr}(r,T^*)
\]

let `mathcal L` and `mathcal Z` be the tautological bundles.  The condition
`Z subset W_L^perp` is the vanishing of the universal-bundle map

\[
\mathcal Z\otimes S\longrightarrow V/\mathcal L,
\qquad \alpha\otimes s\longmapsto A_\alpha(s)\bmod\mathcal L. \tag{2.2}
\]

Its zero locus is closed and projective.  In the relative flag problem one
adds the Grassmann factors carrying `mathcal S` and `mathcal T`, together with
the closed vanishing condition `partial mathcal S subset mathcal T`.  Thus a
bad general-fibre pair `(L,Z)` extends, after a finite DVR extension if
necessary, to an actual Grassmann point in the special fibre.

The dimension of `Z` is retained because `Z` belongs to a fixed
Grassmannian; no equality of ranks is being treated as a closed condition.
Equivalently, (2.1) identifies `dim W_L^perp` with the kernel dimension of a
universal-bundle map, so under specialization

\[
\dim W_{L_0}^\perp\ge \dim W_{L_\eta}^\perp.              \tag{2.3}
\]

This is the upper-semicontinuity direction needed for the contradiction.

### Coordinate endpoint bound

The row-column torus preserves (2.2).  Borel fixed point therefore reduces a
nonempty bad incidence to coordinate `L` and `Z`.  The parent-functional count
for the seven row-occupancy partitions

\[
5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1^5
\]

is

| flag type | 5 | 4+1 | 3+2 | 3+1+1 | 2+2+1 | 2+1+1+1 | 1^5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `S22` | 4 | 4 | 2 | 1 | 1 | 0 | 0 |
| `S21`, delete core-inner | 4 | 4 | 2 | 1 | 1 | 0 | 0 |
| `S21`, delete core-with-4 | 4 | 4 | 5 | 2 | 5 | 2 | 0 |
| `S21`, delete side | 4 | 7 | 3 | 5 | 2 | 2 | 0 |

Consequently `codim_T W_L <= 4` for the full `S22,T48` flag and
`codim_T W_L <= 7` for each deleted-point flag.  The table is a finite hand
classification.  The enumeration of all `binom(25,5)=53,130` coordinate
five-planes is an exact diagnostic that independently reproduces its maxima;
it is not a substitute for the closed-incidence reduction.

### Relative form

Let `R` be a DVR and let `mathscr S,mathscr T` be free relative flag bundles
with

\[
\partial\mathscr S\subset\mathscr T,
\qquad \operatorname{rank}\mathscr T=48+e,
\]

whose special fibre is one of the four flag types above.  If the generic fibre
had

\[
\operatorname{codim}_{\mathscr T_\eta}W_{L_\eta}\ge8+e,
\]

choose an `(8+e)`-plane `Z_eta` in its annihilator and specialize the closed
incidence.  Since `partial S_0=T48 subset mathscr T_0`, the endpoint satisfies

\[
\operatorname{codim}_{\mathscr T_0}W_{L_0}
\le e+\operatorname{codim}_{T48}W_{L_0}
\le e+7,
\]

contradicting the retained `(8+e)`-plane.  Hence

\[
\operatorname{codim}_{\mathscr T_\eta}W_{L_\eta}\le7+e. \tag{2.4}
\]

This specializes the actual Grassmann points `L` and `Z`; it never identifies
an initial space of a moving `W_L` with the special-fibre `W_L`.

### The five routed states

| `(s,d,t,h)` | lower rank | six-coordinate upper rank | contradiction |
|---|---:|---:|---:|
| `(21,11,48,59)` | 43 | `6*7=42` | `43>42` |
| `(22,11,48,59)` | 43 | `6*7=42` | `43>42` |
| `(21,11,49,60)` | 49 | `6*8=48` | `49>48` |
| `(22,11,49,60)` | 49 | `6*8=48` | `49>48` |
| `(22,12,48,60)` | 48 | `6*7=42` | `48>42` |

For the two `h=59` states the lower rank is `48-5=43`, because the canonical
quotient map has kernel dimension at most five.  For `h=60` the six quadratic
and cubic blocks are direct sums, so the combined coordinate projection has
rank `48+e`.  Formula (2.4) bounds each of its six components by `7+e`.
The only torsion case has `e=1`; the Petersen unit-defect argument excludes
shadow size 49 and retains the `T48` special-fibre input.  These are exactly the
five states assigned to the relative-annihilator route.

## Evidence boundary

- The two closedness/formal arguments above are characteristic-zero proofs.
- The four-row parent table is a finite hand classification.
- The 53,130-plane parent-table replay and orbit-0 tangent graph are exact
  computations.
- Finite-order formal tests, if run, are diagnostics only; the formal lemma is
  the all-orders theorem-bearing step.
- The repository status remains a computer-assisted proof draft pending a
  named independent human review of the final clean main-target head.
