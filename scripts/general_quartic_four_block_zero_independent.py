#!/usr/bin/env python3
"""Independent finite audit for the quartic four-block zero theorem."""
from itertools import combinations
from math import comb

def require(c,m):
    if not c: raise RuntimeError(m)
def rank_colex(s): return sum(comb(x,i+1) for i,x in enumerate(s))
def layer(n,m): return sorted(combinations(range(n),m),key=rank_colex)
def partitions4(max_part=15):
    out=[]
    def rec(rem,cap,p):
        if rem==0: out.append(tuple(p)); return
        for x in range(min(cap,rem),0,-1): rec(rem-x,x,p+[x])
    rec(4,max_part,[]); return out

def quadratic_shadow():
    sets=layer(6,2); seen=set(); k=[0]
    for s in sets:
        seen.update((s[0],),(s[1],)); k.append(len(seen))
    weights=[next(x for x in range(6) if x not in s) for s in sets]
    vals=[]
    for p in partitions4():
        full=p+(0,)*(len(sets)-len(p))
        vals.append((sum(w*k[x] for w,x in zip(weights,full)),p))
    best=min(v for v,_ in vals); mins=[p for v,p in vals if v==best]
    require(best==8,(best,mins)); require(len(mins)==4,mins)
    return best,len(mins)

def cubic_pair_scan():
    triples=list(combinations(range(6),3)); rect=[]
    for r in triples:
        for c in triples: rect.append(set((i,j) for i in r for j in c))
    minimum=99; count=0
    for i in range(len(rect)):
        for j in range(i+1,len(rect)):
            minimum=min(minimum,len(rect[i]|rect[j])); count+=1
    require(count==79800,count); require(minimum==12,minimum)
    return minimum,count

def pair_state_scan():
    states=[]
    for a in range(7):
      for b in range(7):
       for h in range(min(a,b)+1):
        joint=a+b-h
        if joint>=9 and max(a-h,b-h)<=3: states.append((a,b,h,joint))
    require(states==[(6,6,3,9)],states); return states

def main():
    q=quadratic_shadow(); c=cubic_pair_scan(); s=pair_state_scan()
    print(f"quadratic_shadow={q[0]} minimizers={q[1]}")
    print(f"cubic_two_plane_linear_shadow={c[0]} pairs={c[1]}")
    print(f"pair_equality_state={s[0]}")
    print("GENERAL_QUARTIC_FOUR_BLOCK_ZERO_INDEPENDENT_PASS")
if __name__=='__main__': main()
