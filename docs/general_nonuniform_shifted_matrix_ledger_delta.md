# Research-ledger delta: nonuniform shifted matrix images

## Status

This delta belongs to the stacked draft following PR #57. It supplements the
canonical `RESEARCH_LEDGER.md` until the active pull-request stack is
consolidated.

## New general theorem

Let

```text
Phi: direct_sum_a R(-a)^(q_a) -> direct_sum_b R(-b)^(p_b),
R=k[s,t],
```

be a degree-zero graded matrix. Its `(b,a)` shift block has one common entry
degree `a-b` and normal rank `r_(b,a)`.

At a selected degree `d`, write

```text
H_s=binom(n,d-a)
H_t=binom(n,d-b).
```

The full permanent image is contained in the sum of the shift-block images,
while the Boolean one-term envelope of the full matrix dominates the envelope
of every individual block. Therefore

```text
R_(Phi,n,d)
 <= sum_(active b,a)
    ceil(
      min(q_a*H_s^2,p_b*H_t^2)
      /(r_(b,a)*min(H_s,H_t))
    ).
```

Define the active support area

```text
omega_d(Phi)=sum_(active b,a) p_b*q_a.
```

Then

```text
R_(Phi,n,d)
 <= omega_d(Phi)*binom(n,floor(n/2))
 <= p*q*binom(n,floor(n/2)),
```

where `p=sum_b p_b` and `q=sum_a q_a`.

If `p,q<=K_n`, reaching Glynn scale through this one matrix-image mechanism
requires

```text
K_n >= (1+o(1))*(pi*n/8)^(1/4).
```

Thus every bounded-size nonuniform shifted matrix image is closed at central
scale, and square matrix size `o(n^(1/4))` is insufficient for Glynn scale in
this exact mechanism.

## Exact replay

```text
primary shift-block patterns                 6,599
primary degree instances                   442,386
primary active block instances           1,013,292
independent individual shift assignments     14,400
independent support-pattern instances         70,672
independent degree instances               3,604,272
independent active block instances         4,956,408
independent positive direct ratios         2,910,432
focused tests                                  5/5 PASS
```

Frozen theorem-facing core:

```text
8402c0aefdd9c2bde28e7b2ec631f78faaf1ac35c7f0387801e6fe7d51dc8601
```

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
bounded nonuniform shifted matrix images=closed at central scale
sub-n^(1/4) square matrix size reaches Glynn=false for this mechanism
joint Fitting/minor profiles=open
higher syzygy modules=open
representation-valued modules=open
Chow-realizability defects=open
border-rank claim=false
exact rank for n>=6=open
```

## Updated route frontier

The following are no longer default continuations:

```text
another bounded homogeneous matrix
another bounded nonuniform shifted presentation matrix
a finite direct sum of such matrix-image invariants
```

A finite direct sum is itself one larger block-diagonal shifted matrix and is
covered by the same theorem.

The next authorized interfaces are:

1. joint Fitting/minor data or determinantal schemes with a proved
   subquotient-compatible statistic;
2. higher syzygy modules with a proven monotone image functor;
3. `S_n x S_n` representation-valued relation modules;
4. matrix families whose support area grows at least at the required scale;
5. uniform Chow-realizability or valuative defects.

Raw kernels, Betti numbers and Tor dimensions remain fail-closed until their
behavior under both submodules and quotients is proved.
