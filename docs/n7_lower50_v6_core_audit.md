# `perm_7` v6 core and endpoint audit

## Decision

```text
SLOPE-TEN-AUDIT-PASS
N49-ENDPOINT-CLASSIFICATION-PASS
MIDDLE-PROJECTION-AUDIT-PASS
ENDPOINT-A-AUDIT-PASS
ENDPOINT-B-AUDIT-PASS
WAVE1-DECIDED
WAVE2-MATHEMATICS-PASS
```

The frozen Rethlas proof blob is
`2e322ccc6b823721244962844e43a0815c804402`.  This audit reconstructs the
load-bearing chain in the order duality -> global symbols -> local symbols ->
equality packets -> endpoint contradictions, rather than following the
candidate's presentation order.

The mathematical verdict is `AUDIT-PASS-WITH-MINOR-REPAIRS`.  The repairs
are an explicit arbitrary-`W` Boolean quotient proof, a complete equality
spectrum entry for the rank-five full quotient, and repository-local paths
for the missing finite replays.  No fatal or major finding remains in
Modules 02--06.  Promotion still waits for the evidence and CI gates.

## External quadratic-generation input

Shafiei, arXiv `1212.0515v2`, works over characteristic zero or
characteristic greater than two.  Theorem 2.13 states that the apolar ideal
of the generic permanent is generated in degree two by the `2 x 2` minors
of the differential matrix together with square and same-row/same-column
monomials.  This matches the candidate's sign convention.  For `perm_7`,
it gives

```text
I = (I_2),  R_3 = C_1 R_2,  R_4 = C_1^2 R_2,
E_2^(1) = E_3,  E_3^(1) = E_4.
```

No symmetric-matrix version of the theorem is used.

## Local slope audit

For a term `T`, write `U_4=D_4(T)`, `U_3=D_3(T)`,
`F=D_2(T)`, `R_T=F intersect E_2`, and `delta=35-dim U_3`.
The permanent intersection audit gives

```text
D_3(T) intersect E_3 = 0,
dim(D_2(T) intersect E_2) <= 3.
```

The first statement follows because a nonzero `E_3` element restricts on
one selected row/column `3 x 3` block to a nonzero multiple of `perm_3`,
which has nine essential variables, whereas a cubic derivative of one Chow
term uses at most seven.  For the second, a row-column torus limit turns the
intersection into coordinate `2 x 2` subpermanents without increasing its
collective derivative span.  A bipartite graph on at most seven edges has at
most three four-cycles.

Every rank-six term is equivalent to

```text
x1*x2*x3*x4*x5*x6*(x1+...+xs),  1 <= s <= 6,
```

and the exact middle dimensions are `25,25,31,34,35,35`.  The rational
implementation and an independently written modular implementation at primes
`1000003` and `1000033` agree in all eight degrees for all six forms.

For arbitrary quotient orientation, carry the quotient kernel and the
at-most-three-dimensional relation space in their Grassmannians while the
term degenerates to its positive monomial.  A second generic diagonal
one-parameter subgroup fixing that monomial gives coordinate initial
subspaces simultaneously.  Rank may drop in the special fibre, so the
coordinate symbol ranks are lower bounds for the original maps.  This is the
required semicontinuity direction.

The exact coordinate rows are:

```text
rank 6: 0,22,33,37,41,44,48
rank 7: 0,32,49,56,57,64,67,69
rank 5, (3,1,1,1,1): 0,12,17,21,24,27
rank 5, (2,2,1,1,1): 0,15,22,24,30,34
```

The full-quotient minus map is handled by
`E_2^(1)=E_3` and the zero cubic intersection, not by the raw last table
entry.  Thus the corrected full values are 50 for the minimal rank-five
profile, `u+35` for rank six, and 70 for rank seven.

The positive-increment equality spectrum is:

- rank seven, quotient rank seven;
- rank six, quotient rank six, exactly when `u=25` (`s=1,2`);
- rank five, quotient rank five, when `u=15`.

The last equality type is harmless but must be recorded.  The span floors
make a rank-five term unique and all other terms rank seven.  Putting it
first leaves 44 ambient dimensions, which cannot be a sum of rank-seven
equality increments in `{0,7}`.  Factor ranks one through four are strict by
the explicit symmetric-power kernel bounds in the candidate.

The two exact coordinate implementations agree, and the arbitrary-orientation
modular falsifier completed 4,128 checks at prime `1000033`, seed `20260822`.
The modular result is diagnostic only.

## Global filtration and endpoint packets

The quotient polarizations

```text
H_4 -> V tensor (H_3/E_3),
H_3 -> V tensor (H_2/E_2)
```

have kernels exactly `E_4` and `E_3`.  Filtering by successive factor spans
identifies each diagonal increment with the audited local symbol.  The
rectangular Sylvester factorization gives the reverse inequality.  At 49
terms the two bounds coincide, so every local, filtration, and Sylvester
slack is zero for every ordering.

The ordering argument gives exactly two packets:

1. 49 rank-seven planes forming a simple represented rank-seven
   7-multilinear matroid;
2. seven mutually direct rank-six `s=1,2` planes and 42 rank-seven graph
   complements, with every graph pair spanning at least 12 dimensions.

Repeated terms and coincident planes are covered: the first packet is simple,
and the second packet's pair floor rules out coincident graph planes.  Scalar
splitting pads a shorter nonzero decomposition to 49 terms over the stated
characteristic-zero field.

## Independent middle-projection proof

Let a subpacket `B` give a direct decomposition
`V=direct_sum_(i in B) L_i`.  Correctly graded Gorenstein duality identifies
the dual cokernel of

```text
R_d -> direct_sum_(i in B) (A_i)_d,  d=3,4,
```

with tuples `(F_i)` in the local degree-`d` derivative spaces whose sum lies
in `E_d`.

Order the basis terms first.  For `d=3`, the full minus diagonal block is
injective: a killed cubic has every first derivative in
`D_2(T_i) intersect E_2`, hence lies in `E_2^(1)=E_3`, and is zero by the
cubic-intersection lemma.  For `d=4`, full polarization is injective and
reduction modulo `E_3` stays injective because
`D_3(T_i) intersect E_3=0`.

The global maps are block triangular with these injective diagonal blocks.
Their kernels are exactly the tuples summing into `E_3` or `E_4`; therefore
the dual cokernels vanish.  Both restrictions are onto.  If `M_B` is the
sum of the local middle dimensions, then

```text
dim R_3 >= M_B,  dim R_4 >= M_B,
dim R_3 + dim R_4 <= 490,
```

so `M_B<=245`; equality makes both restrictions isomorphisms.  This uses
algebra multiplication by basis-supported degree-one codewords and does not
revive the false local quadratic-surjectivity lemma.

## Endpoint A

Choose seven basis planes.  Their Boolean middle total is 245, so the
degree-three and degree-four basis restrictions are isomorphisms.  For a
nonbasis plane, represented-matroid rank shows every fundamental-circuit
restriction block is either zero or invertible, and simplicity gives at
least two circuit indices.

Lift a cubic supported on one basis block and multiply by a degree-one
codeword supported on a distinct circuit block.  The product has zero on all
basis blocks, hence is zero by the degree-four isomorphism.  The invertible
circuit block then makes every linear form annihilate the nonbasis cubic
component.  The Boolean algebra has no degree-three socle: for a nonzero
squarefree coefficient choose a missing variable; its resulting coefficient
has a unique source.  Thus the nonbasis projection is zero.  Its dual
cokernel is `D_3(T_t) intersect E_3=0`, so the same projection is onto, a
contradiction.

## Endpoint B and the arbitrary-`W` repair

The seven rank-six blocks and one graph complement form a direct basis with
middle total `7*25+35=210`.  The packet-specific Sylvester upper bound is
420, so both middle restrictions are isomorphisms.

For another graph `L_t=graph(N_t)`, the pair floor gives `rank N_t>=5`.
Basis-supported multiplication kills components sourced in every rank-six
block.  For the graph-source block it gives annihilation by
`W=im(N_t^*)`, where `dim W>=5`.

Here is the missing arbitrary-orientation Boolean proof.  Put
`A=k[e_1,...,e_7]/(e_i^2)` and `B=A/(W)`.  Then `dim B_1<=2`.  If it is at
most one, `B_2=0`.  Otherwise choose two independent images `x,y` among the
seven images of the `e_i`; then `x^2=y^2=0`.  Every other image is
`a*x+b*y`, and its square is `2ab*xy`.  In characteristic zero, either some
`ab` is nonzero and `xy=0`, or every image lies on one of the two coordinate
directions.  In the latter case `B_d=0` for `d>=3`.  In both cases `B_4=0`,
equivalently

```text
W * A_3 = A_4.
```

Perfect degree `(3,4)` pairing then kills every cubic annihilated by `W`.
The graph-source projection is zero, while the same cubic-intersection
duality makes it onto, a contradiction.  No common graph map or tail
synchronization is assumed.

The finite control exhausts all 2,667 five-dimensional subspaces of
`F_2^7`; every multiplication image `W*A_3` has rank 35, and the global
degree-three no-socle map also has rank 35.  This is a falsifier only; the
preceding characteristic-zero argument is the proof.

## Remaining gate

The core mathematics supports lower 50, but repository promotion still
requires selective import of the frozen proof, compact evidence, negative
regressions, full tests, and a successful exact-head GitHub Actions receipt.
