"""Exact certificates for the even-degree multidimensional-shadow bound.

The theorem implemented here applies only to even ``n=2k``. It combines:

* the self-transpose central catalecticant ``C_{k,k}``;
* the first Koszul rank formula;
* Bukh's multidimensional Kruskal--Katona inequality; and
* a rational witness ``x`` that bounds the central derivative-space
  intersection after fixing ``q`` Chow terms.

All arithmetic is exact. A returned certificate is a rigorous lower bound,
not a claim that the chosen rational witness is globally optimal.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from math import comb, factorial
from typing import Any, Iterable


@dataclass(frozen=True, slots=True)
class EvenMultishadowCertificate:
    """A deterministic witness for an even-degree Chow-rank lower bound."""

    n: int
    k: int
    witness_numerator: int
    witness_denominator: int
    fixed_terms: int
    intersection_dimension_cap: int
    permanent_koszul_rank: int
    chow_term_koszul_cap: int
    residual_koszul_rank_floor: int
    residual_term_count: int
    lower_bound: int

    @property
    def witness(self) -> Fraction:
        return Fraction(self.witness_numerator, self.witness_denominator)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["witness"] = str(self.witness)
        return data


def _require_even_n(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool) or n < 4 or n % 2:
        raise ValueError("n must be an even integer with n >= 4")


def _floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -(-numerator // denominator)


def generalized_binomial(x: Fraction, r: int) -> Fraction:
    """Return the polynomial binomial coefficient ``binom(x,r)`` exactly."""

    if not isinstance(x, Fraction):
        x = Fraction(x)
    if not isinstance(r, int) or isinstance(r, bool) or r < 0:
        raise ValueError("r must be a nonnegative integer")
    result = Fraction(1)
    for i in range(r):
        result *= x - i
    return result / factorial(r)


def central_koszul_data(n: int) -> tuple[int, int, int]:
    """Return ``(central_dimension, target_rank, one_term_cap)``."""

    _require_even_n(n)
    k = n // 2
    central_dimension = comb(n, k)
    target_rank = n * n * central_dimension**2 - comb(n, k + 1) ** 2
    one_term_cap = n * n * central_dimension - comb(n, k + 1)
    return central_dimension, target_rank, one_term_cap


def central_koszul_lower_bound(n: int) -> int:
    """Return the ordinary central first-Koszul lower bound."""

    _, target_rank, one_term_cap = central_koszul_data(n)
    return _ceil_div(target_rank, one_term_cap)


def even_multishadow_bound_at(
    n: int,
    witness: Fraction,
) -> EvenMultishadowCertificate:
    """Build a rigorous even-degree multishadow certificate.

    Let ``n=2k`` and ``x=witness``. The certificate fixes

    ``q = floor(binom(x,k-1)^2 / binom(n,k-1))``

    Chow terms and uses

    ``s <= floor(binom(x,k)^2)``

    for the intersection with the permanent's central derivative space.
    The latter implication is Bukh's multidimensional Kruskal--Katona
    theorem applied after a row-column torus degeneration.
    """

    _require_even_n(n)
    witness = Fraction(witness)
    k = n // 2
    if witness < k or witness > n:
        raise ValueError("witness must satisfy n/2 <= witness <= n")

    central_dimension, target_rank, one_term_cap = central_koszul_data(n)
    fixed_terms = _floor_fraction(
        generalized_binomial(witness, k - 1) ** 2
        / comb(n, k - 1)
    )
    if fixed_terms < 1:
        raise ValueError("witness certifies no fixed Chow term")

    base_bound = central_koszul_lower_bound(n)
    if fixed_terms > base_bound:
        raise ValueError(
            "fixed_terms exceeds the unconditional central Koszul lower bound"
        )

    intersection_cap = _floor_fraction(
        generalized_binomial(witness, k) ** 2
    )
    # The intersection is also contained in the sum of q central derivative
    # spaces, each of dimension binom(n,k).
    intersection_cap = min(
        intersection_cap,
        fixed_terms * central_dimension,
        central_dimension**2,
    )

    residual_rank_floor = target_rank - n * n * intersection_cap
    residual_terms = (
        _ceil_div(residual_rank_floor, one_term_cap)
        if residual_rank_floor > 0
        else 0
    )
    lower_bound = fixed_terms + residual_terms

    return EvenMultishadowCertificate(
        n=n,
        k=k,
        witness_numerator=witness.numerator,
        witness_denominator=witness.denominator,
        fixed_terms=fixed_terms,
        intersection_dimension_cap=intersection_cap,
        permanent_koszul_rank=target_rank,
        chow_term_koszul_cap=one_term_cap,
        residual_koszul_rank_floor=residual_rank_floor,
        residual_term_count=residual_terms,
        lower_bound=max(base_bound, lower_bound),
    )


def best_rational_grid_certificate(
    n: int,
    denominator: int = 256,
) -> EvenMultishadowCertificate:
    """Optimize over the transparent grid ``x=j/denominator`` exactly."""

    _require_even_n(n)
    if (
        not isinstance(denominator, int)
        or isinstance(denominator, bool)
        or denominator < 1
    ):
        raise ValueError("denominator must be a positive integer")

    k = n // 2
    best: EvenMultishadowCertificate | None = None
    for numerator in range(k * denominator, n * denominator + 1):
        witness = Fraction(numerator, denominator)
        try:
            candidate = even_multishadow_bound_at(n, witness)
        except ValueError:
            continue
        if best is None or (
            candidate.lower_bound,
            -candidate.intersection_dimension_cap,
            candidate.fixed_terms,
        ) > (
            best.lower_bound,
            -best.intersection_dimension_cap,
            best.fixed_terms,
        ):
            best = candidate

    if best is None:
        raise RuntimeError("the rational grid produced no valid certificate")
    return best


# Exact rational witnesses obtained by a deterministic search and then checked
# entirely with Fraction arithmetic. They certify the displayed bounds; the
# module does not claim that these witnesses are unique or globally optimal.
REVIEWED_WITNESSES: dict[int, Fraction] = {
    4: Fraction(88_545_595, 31_164_492),
    6: Fraction(2_287_212_075, 511_643_399),
    8: Fraction(4_935_666_310, 766_421_433),
    10: Fraction(2_096_245_339, 247_164_687),
    12: Fraction(8_958_427_664, 841_291_077),
    14: Fraction(10_940_892_262, 866_863_999),
    16: Fraction(4_018_217_454, 273_901_939),
}


def reviewed_even_certificates() -> Iterable[EvenMultishadowCertificate]:
    """Yield the frozen small-even-``n`` exact certificates."""

    for n in sorted(REVIEWED_WITNESSES):
        yield even_multishadow_bound_at(n, REVIEWED_WITNESSES[n])
