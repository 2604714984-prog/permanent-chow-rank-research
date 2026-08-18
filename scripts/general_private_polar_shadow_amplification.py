#!/usr/bin/env python3
"""Exact finite replay for quantitative private-polar shadow amplification."""
from __future__ import annotations
import argparse, hashlib, json
from functools import lru_cache
from math import comb
from pathlib import Path
EXPECTED_CORE_SHA256="a158faee3d5aa7e5fe5081fdf485ba3168c58877279e7d270fc7ed383bfab6cd"
def require(c,m):
    if not c: raise RuntimeError(m)
def canonical(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def unrank_colex(rank,r):
    vals=[0]*r; rem=rank
    for i in range(r,0,-1):
        lo=i-1; hi=i
        while comb(hi,i)<=rem: hi*=2
        while lo+1<hi:
            mid=(lo+hi)//2
            if comb(mid,i)<=rem: lo=mid
            else: hi=mid
        vals[i-1]=lo; rem-=comb(lo,i)
    require(rem==0,(rank,r,rem)); return tuple(vals)
def exact_linear_shadow(r,b):
    require(r>=2 and b>=1,(r,b)); subs=[unrank_colex(i,r) for i in range(b)]; seen=set(); profile=[0]; weights=[]
    for S in subs:
        seen.update(S); profile.append(len(seen)); present=set(S); c=0
        while c in present: c+=1
        weights.append(comb(c,r-1) if c>=r-1 else 0)
    INF=10**18
    @lru_cache(None)
    def dp(i,upper,remaining):
        if i==b: return 0 if remaining==0 else INF
        rows=b-i
        if remaining<0 or remaining>upper*rows: return INF
        lo=(remaining+rows-1)//rows; hi=min(upper,remaining,b); best=INF
        for x in range(lo,hi+1):
            if remaining-x>x*(rows-1): continue
            best=min(best,weights[i]*profile[x]+dp(i+1,x,remaining-x))
        return best
    return dp(0,b,b)
def core():
    return {"status":["GENERAL_PRIVATE_POLAR_SHADOW_AMPLIFICATION","EXACT_INITIAL_LINEAR_SHADOW_TIERS","PAIR_ZERO_TO_M2_MINUS_M_MINUS_1","EXACT_INTEGER_INTERFACE_REPLAYED"],"theorem":{"private_dimension":"If delta=m^2-(q-1)n>0 and a nonzero intersection survives, some private polar space in D_(m-1)(perm_n) has dimension at least delta.","shadow_criterion":"Such an intersection is impossible whenever F^(m-2)_(n,m-1)(delta)>n.","initial_tiers":"With r=m-1: F(1)=r^2; F(b)=r(r+1) for 2<=b<=r+1; F(r+2)=r(r+2), hence F(b)>=r(r+2) for b>=r+2.","pair_corollary":"For m>=4 and m<=n<=m^2-m-1, every two-term Chow block is permanent-relative zero in output degree m.","q_ge_3_corollary":"For m>=4,q>=3,(q-1)n<m^2, every q-term Chow block is permanent-relative zero."},"claim_boundary":"This is a characteristic-zero literal-intersection zero theorem using the established exact iterated product-shadow theorem. It gives no new exact Chow rank or border-rank result. The pair boundary n=m^2-m, the cubic exceptional rows, shifted equality cases not already covered by the parent simplex theorem, and (q-1)n>=m^2 remain open. Literature novelty is not established."}
def build_payload():
    c=core(); require(canonical(c)==EXPECTED_CORE_SHA256,canonical(c)); tiers=0
    for r in range(2,65):
        require(exact_linear_shadow(r,1)==r*r,(r,1)); tiers+=1
        for b in range(2,r+2): require(exact_linear_shadow(r,b)==r*(r+1),(r,b)); tiers+=1
        require(exact_linear_shadow(r,r+2)==r*(r+2),(r,r+2)); tiers+=1
    pairs=qchecks=0
    for m in range(4,129):
        nmax=m*m-m-1; require(exact_linear_shadow(m-1,m+1)==m*m-1,(m,"pair")); require(m*m-1>nmax,(m,nmax)); pairs+=1
        for q in range(3,m+2):
            n=(m*m-1)//(q-1)
            if n<m: continue
            delta=m*m-(q-1)*n; require(delta>=1,(m,q,n)); require(exact_linear_shadow(m-1,delta)>n,(m,q,n,delta)); qchecks+=1
    stopping=[]
    for m in range(4,33):
        n=m*m-m; F=exact_linear_shadow(m-1,m); require(F==n,(m,n,F)); stopping.append({"m":m,"pair_boundary_n":n,"delta":m,"exact_shadow":F})
    return {**c,"core_sha256":EXPECTED_CORE_SHA256,"exact_replay":{"tier_checks":tiers,"pair_threshold_checks":pairs,"q_ge_3_boundary_checks":qchecks,"pair_stopping_rows":stopping}}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--json",type=Path); a=p.parse_args(); payload=build_payload(); text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if a.json: a.json.parent.mkdir(parents=True,exist_ok=True); a.json.write_text(text,encoding="utf-8",newline="\n")
    print(text,end=""); print("GENERAL_PRIVATE_POLAR_SHADOW_AMPLIFICATION_AUDIT_PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
