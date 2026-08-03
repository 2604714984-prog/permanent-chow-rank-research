"""Exact general-degree multidimensional-shadow lower-bound certificates.

For a degree-``n`` permanent and a derivative output degree ``m``, the
complementary degree is ``r=n-m``. The double-quotient argument shows that the
first-Koszul residual rank loses only ``n^2`` times the intersection in the
*row* derivative space ``D_r``. Bukh's two-dimensional shadow theorem bounds
that intersection after fixing actual Chow terms.

All arithmetic is exact. The returned values are rigorous ordinary Chow-rank
lower bounds; no border-rank or global-optimality claim is made.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from math import comb
from typing import Any, Iterable

from .bounds import best_koszul_bound
from .even_multishadow import generalized_binomial


@dataclass(frozen=True, slots=True)
class MultishadowCertificate:
    """A deterministic witness for the general multishadow lower bound."""

    n: int
    output_degree: int
    complementary_degree: int
    witness_numerator: int
    witness_denominator: int
    fixed_terms: int
    complementary_intersection_cap: int
    permanent_koszul_rank: int
    chow_term_koszul_cap: int
    residual_koszul_rank_floor: int
    residual_term_count: int
    local_koszul_bound: int
    global_koszul_bound: int
    lower_bound: int

    @property
    def witness(self) -> Fraction:
        return Fraction(self.witness_numerator, self.witness_denominator)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["witness"] = str(self.witness)
        return data


def _require_parameters(n: int, output_degree: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool) or n < 4:
        raise ValueError("n must be an integer with n >= 4")
    if (
        not isinstance(output_degree, int)
        or isinstance(output_degree, bool)
        or not 2 <= output_degree <= n - 2
    ):
        raise ValueError("output_degree must satisfy 2 <= m <= n-2")


def _floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -(-numerator // denominator)


def koszul_data(n: int, output_degree: int) -> tuple[int, int, int]:
    """Return ``(derivative_dimension, target_rank, one_term_cap)``."""

    _require_parameters(n, output_degree)
    m = output_degree
    derivative_dimension = comb(n, m)
    target_rank = n * n * derivative_dimension**2 - comb(n, m + 1) ** 2
    one_term_cap = n * n * derivative_dimension - comb(n, m + 1)
    return derivative_dimension, target_rank, one_term_cap


def multishadow_bound_at(
    n: int,
    output_degree: int,
    witness: Fraction,
) -> MultishadowCertificate:
    """Build an exact general-degree multidimensional-shadow certificate.

    Put ``r=n-output_degree``. The certificate fixes

    ``q=floor(binom(x,r-1)^2 / binom(n,r-1))``

    terms and bounds the complementary derivative-space intersection by

    ``floor(binom(x,r)^2)``.
    """

    _require_parameters(n, output_degree)
    witness = Fraction(witness)
    m = output_degree
    r = n - m
    if witness < r or witness > n:
        raise ValueError("witness must satisfy n-m <= witness <= n")

    derivative_dimension, target_rank, one_term_cap = koszul_data(n, m)
    fixed_terms = _floor_fraction(
        generalized_binomial(witness, r - 1) ** 2
        / comb(n, r - 1)
    )
    if fixed_terms < 1:
        raise ValueError("witness certifies no fixed Chow term")

    global_base = best_koszul_bound(n).lower_bound
    if fixed_terms > global_base:
        raise ValueError(
            "fixed_terms exceeds the unconditional global Koszul lower bound"
        )

    complementary_dimension = comb(n, r)
    intersection_cap = _floor_fraction(
        generalized_binomial(witness, r) ** 2
    )
    intersection_cap = min(
        intersection_cap,
        fixed_terms * complementary_dimension,
        complementary_dimension**2,
    )

    residual_rank_floor = target_rank - n * n * intersection_cap
    residual_terms = (
        _ceil_div(residual_rank_floor, one_term_cap)
        if residual_rank_floor > 0
        else 0
    )
    local_base = _ceil_div(target_rank, one_term_cap)
    lower_bound = max(global_base, fixed_terms + residual_terms)

    return MultishadowCertificate(
        n=n,
        output_degree=m,
        complementary_degree=r,
        witness_numerator=witness.numerator,
        witness_denominator=witness.denominator,
        fixed_terms=fixed_terms,
        complementary_intersection_cap=intersection_cap,
        permanent_koszul_rank=target_rank,
        chow_term_koszul_cap=one_term_cap,
        residual_koszul_rank_floor=residual_rank_floor,
        residual_term_count=residual_terms,
        local_koszul_bound=local_base,
        global_koszul_bound=global_base,
        lower_bound=lower_bound,
    )


def best_general_grid_certificate(
    n: int,
    denominator: int = 256,
) -> MultishadowCertificate:
    """Optimize all admissible output degrees on a rational grid exactly."""

    if not isinstance(n, int) or isinstance(n, bool) or n < 4:
        raise ValueError("n must be an integer with n >= 4")
    if (
        not isinstance(denominator, int)
        or isinstance(denominator, bool)
        or denominator < 1
    ):
        raise ValueError("denominator must be a positive integer")

    best: MultishadowCertificate | None = None
    for m in range(2, n - 1):
        r = n - m
        for numerator in range(r * denominator, n * denominator + 1):
            witness = Fraction(numerator, denominator)
            try:
                candidate = multishadow_bound_at(n, m, witness)
            except ValueError:
                continue
            if best is None or (
                candidate.lower_bound,
                -candidate.complementary_intersection_cap,
                candidate.fixed_terms,
                -candidate.output_degree,
            ) > (
                best.lower_bound,
                -best.complementary_intersection_cap,
                best.fixed_terms,
                -best.output_degree,
            ):
                best = candidate

    if best is None:
        raise RuntimeError("the rational grid produced no valid certificate")
    return best


# Exact rational witnesses frozen after deterministic search. They certify the
# displayed values but are not asserted to be unique or globally optimal.
REVIEWED_GENERAL_WITNESSES: dict[int, tuple[int, Fraction]] = {
    4: (2, Fraction(88_545_595, 31_164_492)),
    5: (2, Fraction(4_091_533_189, 1_000_000_000)),
    6: (3, Fraction(2_287_212_075, 511_643_399)),
    7: (3, Fraction(763_202_471, 125_000_000)),
    8: (4, Fraction(4_935_666_310, 766_421_433)),
    9: (4, Fraction(8_079_701_609, 1_000_000_000)),
    10: (5, Fraction(2_096_245_339, 247_164_687)),
    11: (5, Fraction(1_273_671_439, 125_000_000)),
    12: (6, Fraction(8_958_427_664, 841_291_077)),
    13: (6, Fraction(6_114_200_309, 500_000_000)),
    14: (7, Fraction(10_940_892_262, 866_863_999)),
    15: (7, Fraction(1_775_481_187, 125_000_000)),
    16: (8, Fraction(4_018_217_454, 273_901_939)),
}


def reviewed_general_certificates() -> Iterable[MultishadowCertificate]:
    """Yield the frozen exact certificates for ``4<=n<=16``."""

    for n in sorted(REVIEWED_GENERAL_WITNESSES):
        output_degree, witness = REVIEWED_GENERAL_WITNESSES[n]
        yield multishadow_bound_at(n, output_degree, witness)
