"""Exact diagnostics for the parity-sensitive multishadow asymptotics.

The mathematical proof is in ``docs/general_multishadow_asymptotics.md``.
This module does not prove the gamma-ratio expansion. It supplies transparent
rational witnesses to the already-proved exact multishadow theorem and exact
scaled-gain values for deterministic regression tests.

Floating-point functions expose the limiting objective and constants only for
display and calculus checks. Every finite Chow-rank certificate is evaluated
with :class:`fractions.Fraction` arithmetic.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from math import comb, e, log
from typing import Any, Iterable

from .bounds import best_koszul_bound
from .multishadow import MultishadowCertificate, multishadow_bound_at


# Nine-decimal rational approximations to the two analytic optimizers. The
# fractions are proof witnesses for each finite n; their decimal origin is not
# used as a logical premise.
EVEN_DEFECT_WITNESS = Fraction(3_816_711, 3_125_000)
ODD_DEFECT_WITNESS = Fraction(2_254_211, 3_125_000)


@dataclass(frozen=True, slots=True)
class AsymptoticDiagnostic:
    """A finite exact certificate plus its normalized additive gain."""

    n: int
    parity: str
    output_degree: int
    defect_numerator: int
    defect_denominator: int
    fixed_terms: int
    intersection_cap: int
    residual_terms: int
    global_koszul_bound: int
    multishadow_lower_bound: int
    additive_gain: int
    central_binomial: int
    scaled_gain_numerator: int
    scaled_gain_denominator: int

    @property
    def defect(self) -> Fraction:
        return Fraction(self.defect_numerator, self.defect_denominator)

    @property
    def scaled_gain(self) -> Fraction:
        return Fraction(self.scaled_gain_numerator, self.scaled_gain_denominator)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["defect"] = str(self.defect)
        data["scaled_gain_n_over_central"] = str(self.scaled_gain)
        data["scaled_gain_decimal"] = f"{float(self.scaled_gain):.15f}"
        return data


def even_optimal_defect() -> float:
    """Return ``1/2 + 1/log(4)`` for display and calculus checks."""

    return 0.5 + 1.0 / log(4.0)


def odd_optimal_defect() -> float:
    """Return ``1/log(4)`` for display and calculus checks."""

    return 1.0 / log(4.0)


def even_limiting_constant() -> float:
    """Return the coefficient ``1/(e log 2)``."""

    return 1.0 / (e * log(2.0))


def odd_limiting_constant() -> float:
    """Return the coefficient ``2/(e log 2)``."""

    return 2.0 / (e * log(2.0))


def even_offset_objective(offset: int, defect: float) -> float:
    """Coefficient ``F_even(offset, defect)`` from Theorem 1.2."""

    if not isinstance(offset, int) or isinstance(offset, bool):
        raise ValueError("offset must be an integer")
    if defect < 0:
        raise ValueError("defect must be nonnegative")
    return -2.0 * offset * offset + (
        4.0 * offset + 4.0 * defect - 2.0
    ) * 4.0 ** (-defect)


def odd_offset_objective(offset: int, defect: float) -> float:
    """Coefficient ``F_odd(offset, defect)`` from Theorem 1.2."""

    if not isinstance(offset, int) or isinstance(offset, bool):
        raise ValueError("offset must be an integer")
    if defect < 0:
        raise ValueError("defect must be nonnegative")
    return -2.0 * offset * (offset + 1) + (
        4.0 * offset + 4.0 * defect
    ) * 4.0 ** (-defect)


def parity_defect_witness(n: int) -> Fraction:
    """Return the frozen rational defect for the parity of ``n``."""

    if not isinstance(n, int) or isinstance(n, bool) or n < 4:
        raise ValueError("n must be an integer with n >= 4")
    return EVEN_DEFECT_WITNESS if n % 2 == 0 else ODD_DEFECT_WITNESS


def parity_asymptotic_certificate(n: int) -> MultishadowCertificate:
    """Evaluate the exact theorem at the frozen parity witness."""

    defect = parity_defect_witness(n)
    output_degree = n // 2
    witness = Fraction(n) - defect
    return multishadow_bound_at(n, output_degree, witness)


def asymptotic_diagnostic(n: int) -> AsymptoticDiagnostic:
    """Return an exact normalized-gain diagnostic for one degree."""

    certificate = parity_asymptotic_certificate(n)
    global_bound = best_koszul_bound(n).lower_bound
    gain = certificate.lower_bound - global_bound
    central = comb(n, n // 2)
    scaled = Fraction(gain * n, central)
    defect = parity_defect_witness(n)

    return AsymptoticDiagnostic(
        n=n,
        parity="even" if n % 2 == 0 else "odd",
        output_degree=certificate.output_degree,
        defect_numerator=defect.numerator,
        defect_denominator=defect.denominator,
        fixed_terms=certificate.fixed_terms,
        intersection_cap=certificate.complementary_intersection_cap,
        residual_terms=certificate.residual_term_count,
        global_koszul_bound=global_bound,
        multishadow_lower_bound=certificate.lower_bound,
        additive_gain=gain,
        central_binomial=central,
        scaled_gain_numerator=scaled.numerator,
        scaled_gain_denominator=scaled.denominator,
    )


def reviewed_asymptotic_diagnostics() -> Iterable[AsymptoticDiagnostic]:
    """Yield the frozen finite degrees used by the regression suite."""

    for n in (20, 21, 40, 41, 80, 81, 120, 121):
        yield asymptotic_diagnostic(n)
