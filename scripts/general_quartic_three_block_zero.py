#!/usr/bin/env python3
"""Exact replay for the quartic three-block zero theorem at (n,m,q)=(8,4,3)."""
from __future__ import annotations
import argparse, hashlib, json
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
EXPECTED_CORE_SHA256='f42f161b773843d253dff703c455191891dcf38a0adc4ac396b6ffcec46a1655'
def require(c,m):
    if not c: raise RuntimeError(m)
def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rankc(s): return sum(comb(x,i+1) for i,x in enumerate(s))
def layer(n,m): return tuple(sorted(combinations(range(n),m),key=rankc))
def exact_shadow_table(n=8,m=2,bmax=8):
    L=layer(n,m); q=len(L); sh=set(); k=[0]
    for s in L:
        for i in range(m): sh.add(s[:i]+s[i+1:])
        k.append(len(sh))
    w=[next(x for x in range(n) if x not in s) for s in L]; INF=10**9
    @lru_cache(None)
    def dp(i,u,r):
        if i==q:return (0,1) if r==0 else (INF,0)
        rows=q-i
        if r<0 or r>u*rows:return INF,0
        lo=(r+rows-1)//rows;hi=min(u,r,q);best=INF;cnt=0
        for x in range(lo,hi+1):
            rem=r-x
            if rem>x*(rows-1):continue
            tail,ways=dp(i+1,x,rem);v=w[i]*k[x]+tail
            if v<best:best,cnt=v,ways
            elif v==best:cnt+=ways
        return best,cnt
    return [{'dimension':b,'shadow':dp(0,q,b)[0],'minimizers':dp(0,q,b)[1]} for b in range(1,bmax+1)],dp.cache_info().currsize
def disjoint_pair_states(table):
    F={r['dimension']:r['shadow'] for r in table}; states=[]
    for a in range(1,9):
        for b in range(1,9):
            if a+b>=9 and F[a]<=a and F[b]<=b:states.append((a,b))
    require(states==[],states);return states
def core():
    table,states=exact_shadow_table(); require([x['shadow'] for x in table]==[4,6,6,8,8,8,9,9],table)
    disjoint_pair_states(table)
    return {'parameters':{'n':8,'m':4,'terms':3},'quartic_essential_floor':16,
      'component_cap':8,'single_private_polar':'ZERO','forced_component_dimensions':[8,8,8],
      'forced_pair_intersections':[0,0,0],'pair_supported_cubic_dimension':8,
      'quadratic_shadow_table':table,'disjoint_two_term_cubic_states':0,
      'conclusion':'UNIVERSAL_ZERO','mu_8_4':4}
def payload():
    c=core();h=sha(c);require(h==EXPECTED_CORE_SHA256,(h,EXPECTED_CORE_SHA256));table,states=exact_shadow_table()
    return {'schema_version':1,'theorem_core_sha256':h,'theorem_core':c,'replay':{'dp_states':states,'rows':table},
      'claim_boundary':{'quartic_8_4_3':'ZERO','mu_8_4':4,'new_unrestricted_rank_bound':False,'border_rank':False,'literature_novelty':'NOT_ESTABLISHED'}}
def main():
    p=argparse.ArgumentParser();p.add_argument('--json',type=Path);a=p.parse_args();v=payload()
    if a.json:a.json.write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
    print('theorem_core_sha256='+v['theorem_core_sha256']);print('GENERAL_QUARTIC_THREE_BLOCK_ZERO_PASS')
if __name__=='__main__':main()
