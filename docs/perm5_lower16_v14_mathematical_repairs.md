# Mathematical repairs for the v14 `perm_5` lower-16 draft

## Status and scope

This note addresses the two load-bearing gaps identified in the external audit
of PR #26.  It does not treat a passing computation as a substitute for the
geometric reduction, and it does not call the resulting argument program-free.

The repaired draft claims

```text
ChowRank(perm_5) = 16
```

as an internal computer-assisted theorem over characteristic-zero fields.  A
fresh external mathematical review remains pending.

## Notation

Let `V=A tensor B`, with both factors five-dimensional, and write `x_ia` for
the matrix variables.  Put

```text
E = image C_(3,2)(perm_5)
  = span{x_ia x_jb + x_ib x_ja : i<j, a<b}
```

inside `Sym^2 V`, and let `pi: Sym^2 V -> Q=(Sym^2 V)/E` be the quotient.  For
a ten-plane `W` in `Q`, define

```text
p(W) = dim ker(Phi_W) - 100,
Phi_W: Sym^3 V -> V tensor (Q/W),
```

where `Phi_W` is polarized differentiation followed by quotient projection.
The permanent derivative space satisfies `E^(1)=D` and `dim D=100`.

For a quintic Chow term `T=l_1...l_5`, write

```text
L_T = span(l_1,...,l_5),
F_T = span(l_i l_j : i<j).
```

The low-rank theorem in the manuscript proves

```text
dim(E intersect Sym^2 L) <= 1 when dim L <= 5.                 (1)
```

## Universal one-intersection flag theorem

**Theorem.** Suppose that `dim F_T=10` and `dim(E intersect F_T)=1`.  Put
`Z=pi(F_T)`, so `dim Z=9`.  For every ten-plane `W` satisfying `Z subset W`,

```text
p(W) <= 26.                                                   (2)
```

### Closed incidence and quotient-image preservation

Work first over an algebraic closure.  Since `F_T subset Sym^2 L_T` and
`dim F_T=10`, the dimension `d=dim L_T` is either four or five.  Let `Torus` be
the diagonal row-column torus.  For fixed `d`, consider tuples

```text
(L,F,Z',W',[q])
```

in

```text
Gr(d,V) x Gr(10,Sym^2 V) x Gr(9,Q) x Gr(10,Q) x P(E)
```

that satisfy

```text
F subset Sym^2 L,
q in F,
F subset pi^(-1)(Z'),
Z' subset W'.                                                 (3)
```

Each condition is the vanishing of a natural map of universal bundles.
Consequently the incidence space is projective, closed, and torus-stable.

Choose nonzero `q` in `E intersect F_T`.  The original data define a point of
this incidence space.  The closure of its torus orbit is complete, so the Borel
fixed-point theorem gives a torus-fixed endpoint

```text
(L_0,F_0,Z_0,W_0,[q_0]).
```

At that endpoint, (1) and nonzero `q_0 in E intersect F_0` imply

```text
E intersect F_0 = span(q_0).
```

It follows that `dim pi(F_0)=9`.  Condition (3) gives
`pi(F_0) subset Z_0`, while `Z_0` is a nine-plane.  Hence

```text
Z_0 = pi(F_0).                                                (4)
```

This is the missing rank-preservation step.  It does not assume that quotient
rank is a closed condition.

### Classification of fixed endpoints

All 25 weights of `V` are distinct, so `L_0` is a coordinate plane.  The 100
weight lines of `E` are the rectangle permanents.  Hence `q_0` is one rectangle
permanent and its essential four-dimensional variable space lies in `L_0`.

If `d=4`, then `L_0` is exactly that rectangle and
`F_0=Sym^2 L_0`.  Its quotient image consists of nine distinct quotient
weights.

If `d=5`, then `L_0` is a rectangle plus one coordinate cell.  Up to row and
column permutations and transpose there are two cases:

- attached: the fifth cell shares a rectangle row or column;
- external: it shares neither.

There are 100 rectangles, with 12 attached and 9 external fifth cells, giving
1,200 and 900 coordinate five-planes.  By (1), `pi(Sym^2 L_0)` has dimension
14, with fourteen one-dimensional quotient weights.  Equation (4) says that
`Z_0` is a coordinate nine-subset of those fourteen weights.

The quotient `Q` has 225 distinct one-dimensional weights: 25 squares, 50
same-row edges, 50 same-column edges, and 100 rectangle crossing weights.
Therefore `W_0` is the nine weights of `Z_0` plus an arbitrary new weight among
all 225 weights.  In particular, the tenth weight is not restricted to the
fourteen-weight universe.

### Exact endpoint certificate and the characteristic-zero direction

In a divided-power coordinate basis, every coordinate endpoint map `Phi_W0`
has an integer matrix with entries in `{0,+1,-1}`.  Let `bar(Phi_W0)` denote
entrywise reduction of that integer matrix modulo 3.  This does not identify
the divided-power lattice with the usual symmetric power in characteristic 3;
no such identification is needed.  For the same integer matrix,

```text
rank_F3 bar(Phi_W0) <= rank_Q Phi_W0,
dim_Q ker Phi_W0 <= dim_F3 ker bar(Phi_W0).                    (5)
```

The standalone verifier reconstructs all matrices from polarized
differentiation.  It finds that the reduced base matrix has kernel dimension
100, equal to the characteristic-zero base dimension `dim D`.  It then checks:

| factor span | flags checked | maximum reduced relative kernel |
|---|---:|---:|
| 4 | 21,600 | 22 |
| 5, attached | 432,432 | 26 |
| 5, external | 432,432 | 22 |

Thus (5) gives `p(W_0)<=26` in characteristic zero.

Finally, `p(tW)=p(W)` for every row-column torus element `t`, because `E` and
polarized differentiation are equivariant.  Kernel dimension is upper
semicontinuous on `Gr(10,Q)`.  Specializing the orbit to the fixed endpoint
therefore gives

```text
p(W) <= p(W_0) <= 26.
```

Matrix rank is unchanged by characteristic-zero scalar extension, so the
result descends from the algebraic closure.  This proves (2).

## Squarefree cubic spaces contain no nonzero binary cubic

**Lemma.** Let `z_1,...,z_m` be a basis over a characteristic-zero field, and
let

```text
J = span{z_i z_j z_k : i,j,k pairwise distinct}.
```

For every subspace `L` of dimension at most two,

```text
J intersect Sym^3 L = 0.                                    (6)
```

**Proof.** Every `f` in `J` satisfies `partial_(z_i)^2 f=0` for all `i`.  The
restrictions of the coordinate covectors span `L^*`.

If `dim L=1`, write `f=c u^3` and choose a coordinate covector `alpha` that is
nonzero on `L`.  Then

```text
partial_alpha^2 f = 6 c alpha(u)^2 u,
```

so `c=0`.

If `dim L=2`, choose two coordinate covectors whose restrictions `alpha,beta`
form a basis of `L^*`.  In dual coordinates `u,v`, write

```text
f = a u^3 + b u^2 v + c u v^2 + d v^3.
```

The two vanishing second derivatives are

```text
0 = partial_u^2 f = 6 a u + 2 b v,
0 = partial_v^2 f = 2 c u + 6 d v.
```

Characteristic zero gives `a=b=c=d=0`, proving (6).

In the `k=2` branch of the coupling lemma, every cubic relation component lies
in the same binary cubic space.  An independent five-factor component is
squarefree in the factor basis, so (6) makes it zero.  Every nonzero component
therefore comes from a four-dimensional factor span.  The remaining argument
then gives a common three-dimensional quadratic relation space, contradicting
`k=2` exactly as required.

## Reproducibility and evidence labels

The canonical independent verifier is

```text
scripts/perm5_one_intersection_flag_standalone_exact.py
```

It uses only the Python standard library, imports no project generator, reads
no frozen result, contains no proof-facing bare `assert`, and writes no file
unless `--output` is explicitly supplied.  Run:

```text
python -O scripts/perm5_one_intersection_flag_standalone_exact.py
python evidence/small_n/v14_repaired/verify_assets.py --replay
```

Evidence classification:

- characteristic-zero proof: low-rank intersection, closed incidence,
  quotient-image preservation, torus endpoint classification, binary-cubic
  exclusion, and semicontinuity;
- exact theorem premise: the 886,464-endpoint integer-matrix reduction
  certificate;
- redundant diagnostics: the other finite-table replay programs in the packet;
- unresolved: fresh external mathematical review, proof-assistant
  formalization, and literature novelty review.
