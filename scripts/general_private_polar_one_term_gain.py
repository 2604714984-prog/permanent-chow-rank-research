#!/usr/bin/env python3
"""Exact arithmetic audit for the private-polar shifted-count theorem.

The proof is in docs/general_private_polar_one_term_gain.md.  This script
checks only the integer interfaces:

1. the strict shifted-count criterion
       n < (m-1)^2, (q-1)n < m^2;
2. the equality-simplex endpoint
       (q-1)n = m^2, 2n <= (m-1)^2;
3. the fact that these rows genuinely extend the parent excess-m band.

No finite scan is used as a proof of the theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_CORE_SHA256 = "d7d6715b6ca5a6fb5d3c996178cc7dfc596f1323f13e374951e56928b102bf3e"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def strict_new_nmax(m: int, q: int) -> int:
    require(m >= 4 and q >= 2, (m, q))
    return min((m*m-1)//(q-1), (m-1)*(m-1)-1)


def parent_excess_m_nmax(m: int, q: int) -> int:
    require(m >= 4 and q >= 2, (m, q))
    return (m*m+m)//q


def equality_row(m: int, q: int) -> int | None:
    denominator=q-1
    if m*m % denominator:
        return None
    n=m*m//denominator
    if n<m or 2*n>(m-1)*(m-1):
        return None
    return n


def theorem_core() -> dict[str, object]:
    return {
        "status":["GENERAL_PRIVATE_POLAR_SHIFTED_TERM_GAIN","GENERAL_SHIFTED_SIMPLEX_ENDPOINT","EXACT_INTEGER_INTERFACE_REPLAYED"],
        "theorem":{
            "strict_shifted_count":"For m>=4, q>=2, n>=m, if n<(m-1)^2 and (q-1)n<m^2, then D_m(perm_n) intersects sum_i D_m(T_i) trivially.",
            "shifted_equality":"If (q-1)n=m^2 and 2n<=(m-1)^2, the same zero conclusion holds.",
            "pair_corollary":"For m>=4 and n<(m-1)^2, every two-term Chow block is permanent-relative zero in output degree m.",
            "mechanism":"If every private polar vanished, the relation defect k would satisfy (q-1)k>=m^2. In the strict shifted range k<=qn-m^2 contradicts (q-1)n<m^2. At equality all inequalities force an exact vector-space simplex; a two-block polar difference descends to output degree m-1."
        },
        "claim_boundary":"This is an ordinary characteristic-zero zero-intersection theorem for literal Chow derivative-space sums. It is not an exact Chow-rank theorem for n>=6, does not change border rank, and does not cover the cubic rows (4,3,3) and (6,3,2), the support boundary n=(m-1)^2 in the strict shifted case, or the regime (q-1)n>m^2. Literature novelty is not established."
    }


def build_payload() -> dict[str, object]:
    core=theorem_core()
    require(canonical_sha256(core)==EXPECTED_CORE_SHA256, canonical_sha256(core))
    strict_rows=strict_positive_excess_rows=improved_rows=equality_rows=pair_rows=0
    samples=[]; equality_samples=[]
    for m in range(4,129):
        for q in range(2,m+2):
            nmax=strict_new_nmax(m,q)
            if nmax<m:
                continue
            for n in range(m,nmax+1):
                require(n<(m-1)**2,(m,q,n,"support")); require((q-1)*n<m*m,(m,q,n,"shift"))
                strict_rows+=1
                if q*n>m*m:
                    s=q*n-m*m; require((q-1)*s<m*m,(m,q,n,s)); strict_positive_excess_rows+=1
                if q==2: pair_rows+=1
            old=parent_excess_m_nmax(m,q)
            if nmax>old:
                improved_rows+=nmax-max(old,m-1)
                if len(samples)<24: samples.append({"m":m,"q":q,"parent_nmax":max(old,m-1),"new_strict_nmax":nmax,"gain":nmax-max(old,m-1)})
            n_eq=equality_row(m,q)
            if n_eq is not None:
                require((q-1)*n_eq==m*m,(m,q,n_eq)); require(2*n_eq<=(m-1)**2,(m,q,n_eq,"two-block")); equality_rows+=1
                if len(equality_samples)<24: equality_samples.append({"m":m,"q":q,"n":n_eq,"excess":q*n_eq-m*m})
    for m,q,n in [(4,3,7),(5,3,12),(6,2,24),(7,2,35),(8,3,31),(10,3,49)]:
        require(n<=strict_new_nmax(m,q),(m,q,n)); require(q*n>m*m+m,(m,q,n,"not beyond parent"))
    for m,q,n in [(6,4,12),(8,5,16),(10,6,20),(12,7,24)]: require(equality_row(m,q)==n,(m,q,n))
    return {**core,"core_sha256":EXPECTED_CORE_SHA256,"exact_replay":{"m_min":4,"m_max":128,"strict_rows":strict_rows,"strict_positive_excess_rows":strict_positive_excess_rows,"pair_rows":pair_rows,"rows_beyond_parent_excess_m_band":improved_rows,"shifted_equality_rows":equality_rows,"strict_gain_samples":samples,"shifted_equality_samples":equality_samples}}


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--json",type=Path); args=parser.parse_args(); payload=build_payload(); text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.json: args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(text,encoding="utf-8",newline="\n")
    print(text,end=""); print("GENERAL_PRIVATE_POLAR_ONE_TERM_GAIN_AUDIT_PASS"); return 0

if __name__=="__main__": raise SystemExit(main())
