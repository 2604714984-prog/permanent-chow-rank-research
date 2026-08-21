#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations, permutations
from collections import Counter, defaultdict
import hashlib, json

N=4
CELLS=tuple(range(16))
MATCHINGS=tuple(frozenset(r*N+p[r] for r in range(N)) for p in permutations(range(N)))

def env(A): return frozenset(i for i,M in enumerate(MATCHINGS) if len(A&M)>=3)

def rowcol_deg(A):
    r=[0]*4;c=[0]*4
    for x in A:r[x//4]+=1;c[x%4]+=1
    return tuple(sorted(r,reverse=True)),tuple(sorted(c,reverse=True))

def has_matching(A): return any(M<=A for M in MATCHINGS)

def canonical(A):
    outs=[]
    for rp in permutations(range(4)):
      for cp in permutations(range(4)):
        outs.append(tuple(sorted(rp[x//4]*4+cp[x%4] for x in A)))
    return min(outs)

def payload():
    hist=Counter(); eq=[]
    total=0
    for s in range(7):
      for t in combinations(CELLS,s):
        A=frozenset(t); total+=1
        k=len(env(A)); hist[k]+=1
        if k==6:eq.append(A)
    assert total==14893
    assert max(hist)==6 and len(eq)==288
    assert all(len(A)==6 and not has_matching(A) and rowcol_deg(A)==((2,2,1,1),(2,2,1,1)) for A in eq)
    orbits=defaultdict(int)
    for A in eq:orbits[canonical(A)]+=1
    assert len(orbits)==2 and sorted(orbits.values())==[144,144]
    orders={0:(1,2,3),1:(0,3,2),2:(3,0,1),3:(2,1,0)}
    frames=[]
    for c,(p,s,q) in orders.items():
      A=frozenset((p,s,4+s,4+q,8+c,12+c));frames.append(A)
    Es=[env(A) for A in frames]
    assert [len(e) for e in Es]==[6]*4
    assert len(set().union(*Es))==24 and sum(len(e) for e in Es)==24
    return {
      'supports_checked':total,'maximum_first_order_matching_envelope':6,
      'equality_supports':len(eq),'equality_row_column_orbits':len(orbits),
      'orbit_sizes':sorted(orbits.values()),
      'equality_degree_sequences':[[2,2,1,1],[2,2,1,1]],
      'z_support_bounds':{str(z):(None if z==5 else 6+5*z) for z in range(7)},
      'first_order_surviving_zero_counts':[4,6],
      'explicit_four_frame_cover_sizes':[len(e) for e in Es],
      'explicit_four_frame_cover_union':len(set().union(*Es)),
    }

def main():
    p=payload(); core=json.dumps(p,sort_keys=True,separators=(',',':')).encode(); p['core_sha256']=hashlib.sha256(core).hexdigest(); print(json.dumps(p,indent=2,sort_keys=True))
if __name__=='__main__': main()
