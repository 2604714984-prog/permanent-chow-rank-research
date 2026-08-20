# Ledger delta: quartic five-to-six-term frontier

## Superseded frontier

```text
5 <= mu(6,4) <= 8
five-block status OPEN
```

## Current proved frontier

```text
6 <= mu(6,4) <= 8
five-block literal sum ZERO
six-block literal sum OPEN
seven-block literal sum OPEN
eight-block literal sum NONZERO
```

## Exact restricted-family thresholds at output degree four

```text
coordinate degree-six blocks                 12
one-factor-per-column blocks                  8
one-factor-per-row blocks                     8
normalized column-uniform sign blocks         8
```

## New structural reductions

```text
partition-Laplace essential formula          PROVED
(2,2) six-generator direct compression       IMPOSSIBLE
isolated fixed-column slice lower bound       INSUFFICIENT
hypothetical six-block quotient relation      UNIQUE FULL-SUPPORT CIRCUIT
```

## Theorem cores

```text
five-block zero:
72a73cc0012e7113f1a483150b61c8e7444310c38542b1d5bca40c9182c15171

coordinate threshold:
4b85646c9b1c96c18b5010206ce7897edba0b330e762f554b7314709ae53b1f9

column-separated reduction:
45a855429fe780db052731a7201713640a0adbe27f656294195399c49fb78623

sign threshold:
af5fbd6fa060649a1a58220f258077d46797013491d89e5623ce2bd7492e0316

partition-Laplace stratification:
1bcbe6b3d3594f649171a21d8837b2a811596858f60dd2b41c52268484525e6c

mixed-slice/circuit:
d82e88706313fb20bd8cf0e51d7ab7a7fadac00d9805d72d2fd1b2ccd1d6d85c
```

## Next task

Classify the common-source images in repeated-column multidegrees
`(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)` under the unique six-element quotient
circuit.  Seek a forced proper subcircuit, a forced separated component, or an
exact witness.
