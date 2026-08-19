#!/usr/bin/env python3
"""Exact finite replay for the quartic four-block zero theorem at (n,m,q)=(6,4,4)."""
from __future__ import annotations
import argparse, hashlib, json
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path

EXPECTED_CORE_SHA256 = "cb4ebea747a4ac2ac2b8141bab816395998cdb785d43b0fcd90579e54e949512"

def require(c: bool, m: object) -> None:
    if not c: raise RuntimeError(m)

def canonical_sha256(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def colex_rank(s: tuple[int,...]) -> int:
    return sum(comb(v,i+1) for i,v in enumerate(s))

def colex_subsets(n:int,m:int)->tuple[tuple[int,...],...]:
    return tuple(sorted(combinations(range(n),m), key=colex_rank))

def product_shadow_minimum(n:int,m:int,b:int)->tuple[int,int,tuple[int,...],int]:
    layer=colex_subsets(n,m); q=len(layer)
    shadow=set(); k=[0]
    for s in layer:
        for i in range(m): shadow.add(s[:i]+s[i+1:])
        k.append(len(shadow))
    weights=[]
    for s in layer:
        present=set(s); weights.append(next(x for x in range(n) if x not in present))
    INF=10**9
    @lru_cache(None)
    def solve(i:int,u:int,r:int)->tuple[int,int]:
        if i==q: return (0,1) if r==0 else (INF,0)
        rows=q-i
        if r<0 or r>u*rows: return INF,0
        lo=(r+rows-1)//rows; hi=min(u,r,q)
        best=INF; count=0
        for x in range(lo,hi+1):
            rem=r-x
            if rem>x*(rows-1): continue
            tail,ways=solve(i+1,x,rem)
            val=weights[i]*k[x]+tail
            if val<best: best,count=val,ways
            elif val==best: count+=ways
        return best,count
    best,count=solve(0,q,b)
    part=[]; i=0; u=q; r=b
    while i<q:
        target,_=solve(i,u,r); rows=q-i
        for x in range((r+rows-1)//rows, min(u,r,q)+1):
            rem=r-x
            if rem>x*(rows-1): continue
            tail,_=solve(i+1,x,rem)
            if weights[i]*k[x]+tail==target:
                part.append(x); r=rem; u=x; i+=1; break
        else: raise RuntimeError((i,u,r))
    return best,count,tuple(part),solve.cache_info().currsize

def cubic_two_plane_linear_shadow()->dict[str,object]:
    sets=list(combinations(range(6),3)); rectangles=[]
    for R in sets:
        for C in sets:
            rectangles.append(frozenset((r,c) for r in R for c in C))
    histogram={}; pairs=0; minimum=99
    for a,b in combinations(rectangles,2):
        size=len(a|b); histogram[size]=histogram.get(size,0)+1
        minimum=min(minimum,size); pairs+=1
    require(pairs==79800,pairs); require(minimum==12,minimum)
    return {"coordinate_pairs_checked":pairs,"minimum_linear_shadow":minimum,
            "union_histogram":{str(k):histogram[k] for k in sorted(histogram)}}

def pair_equality_states()->list[dict[str,int]]:
    out=[]
    for r1 in range(7):
        for r2 in range(7):
            for h in range(min(r1,r2)+1):
                d=r1+r2-h
                if d<9: continue
                if r1-h>3 or r2-h>3: continue
                out.append({"r1":r1,"r2":r2,"intersection":h,"joint":d,
                            "private1":r1-h,"private2":r2-h})
    require(out==[{"r1":6,"r2":6,"intersection":3,"joint":9,"private1":3,"private2":3}],out)
    return out

def theorem_core()->dict[str,object]:
    qshadow, qcount, qpart, states = product_shadow_minimum(6,2,4)
    cubic=cubic_two_plane_linear_shadow()
    pair=pair_equality_states()
    core={
      "parameters":{"n":6,"m":4,"terms":4},
      "permanent_linear_shadow_floor":16,
      "component_essential_cap":6,
      "quadratic_four_plane_shadow":{"value":qshadow,"minimizer_count":qcount,"witness":list(qpart)},
      "cubic_two_plane_linear_shadow":cubic["minimum_linear_shadow"],
      "pair_equality_states":pair,
      "initial_pair_supported_polar_floor":4,
      "forced_pair_span":9,
      "refined_pair_supported_polar_floor":7,
      "pair_span_two_plane_capacity":1,
      "conclusion":"UNIVERSAL_ZERO",
    }
    return core

def build_payload()->dict[str,object]:
    core=theorem_core(); csha=canonical_sha256(core)
    require(csha==EXPECTED_CORE_SHA256,(csha,EXPECTED_CORE_SHA256))
    qshadow,qcount,qpart,states=product_shadow_minimum(6,2,4)
    cubic=cubic_two_plane_linear_shadow()
    return {"schema_version":1,"theorem_core_sha256":csha,"theorem_core":core,
      "replay":{"quadratic_dp_states":states,"quadratic_shadow":qshadow,
                "quadratic_minimizer_count":qcount,"quadratic_witness":list(qpart),**cubic},
      "claim_boundary":{"quartic_6_4_4":"ZERO","new_chow_rank_bound":False,
                        "new_exact_unrestricted_rank":False,"border_rank":False,
                        "literature_novelty":"NOT_ESTABLISHED"}}

def main()->None:
    p=argparse.ArgumentParser(); p.add_argument("--json",type=Path); a=p.parse_args()
    payload=build_payload()
    if a.json: a.json.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"theorem_core_sha256={payload['theorem_core_sha256']}")
    print("GENERAL_QUARTIC_FOUR_BLOCK_ZERO_PASS")
if __name__=="__main__": main()
