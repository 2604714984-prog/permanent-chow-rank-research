#!/usr/bin/env python3
"""Independent replay for private-polar shadow amplification."""
from __future__ import annotations
from itertools import combinations
from math import comb

def require(c,m):
    if not c: raise RuntimeError(m)
def colex_rank(S): return sum(comb(v,i+1) for i,v in enumerate(S))
def first_subsets(r,b):
    universe=r; vals=[]
    while len(vals)<b:
        universe+=1; vals=sorted(combinations(range(universe),r),key=colex_rank)[:b]
    return vals
def profiles(r,b):
    subs=first_subsets(r,b); seen=set(); k=[0]; w=[]
    for S in subs:
        seen.update(S); k.append(len(seen)); present=set(S); c=0
        while c in present: c+=1
        w.append(comb(c,r-1) if c>=r-1 else 0)
    return k,w
def partitions(total,length,upper=None):
    if length==0:
        if total==0: yield ()
        return
    if upper is None: upper=total
    for x in range(min(upper,total),-1,-1):
        for tail in partitions(total-x,length-1,x): yield (x,)+tail
def brute_shadow(r,b):
    k,w=profiles(r,b); best=None
    for part in partitions(b,b,b):
        value=sum(wi*k[x] for wi,x in zip(w,part,strict=True))
        if best is None or value<best: best=value
    return best
def main():
    tiers=0
    for r in range(2,11):
        require(brute_shadow(r,1)==r*r,(r,1)); tiers+=1
        for b in range(2,r+2): require(brute_shadow(r,b)==r*(r+1),(r,b)); tiers+=1
        require(brute_shadow(r,r+2)==r*(r+2),(r,r+2)); tiers+=1
    pair_checks=0
    for m in range(4,257):
        nmax=m*m-m-1; require(m*m-nmax==m+1,(m,nmax)); require((m-1)*(m+1)>nmax,(m,nmax)); boundary=m*m-m; require((m-1)*m==boundary,(m,boundary)); pair_checks+=2
    qchecks=0
    for m in range(4,257):
        for q in range(3,m+2):
            n=(m*m-1)//(q-1)
            if n<m: continue
            delta=m*m-(q-1)*n; require(delta>=1,(m,q,n)); F=(m-1)**2 if delta==1 else (m*(m-1) if delta<=m else m*m-1); require(F>n,(m,q,n,delta,F)); qchecks+=1
    print(f"independent_initial_tier_checks={tiers}"); print(f"independent_pair_checks={pair_checks}"); print(f"independent_q_ge_3_checks={qchecks}"); print("GENERAL_PRIVATE_POLAR_SHADOW_AMPLIFICATION_INDEPENDENT_PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
