#!/usr/bin/env python3
from itertools import combinations
from math import comb

def require(c,m):
    if not c:raise RuntimeError(m)
def rankc(s):return sum(comb(x,i+1) for i,x in enumerate(s))
def parts(total,cap):
    out=[]
    def rec(rem,top,p):
        if rem==0:out.append(tuple(p));return
        for x in range(min(rem,top),0,-1):rec(rem-x,x,p+[x])
    rec(total,cap,[]);return out
def table():
    L=sorted(combinations(range(8),2),key=rankc);seen=set();k=[0]
    for s in L:seen.update((s[0],),(s[1],));k.append(len(seen))
    w=[next(x for x in range(8) if x not in s) for s in L];vals=[]
    for b in range(1,9):
        best=999;count=0
        for p in parts(b,len(L)):
            full=p+(0,)*(len(L)-len(p));v=sum(a*k[x] for a,x in zip(w,full))
            if v<best:best,count=v,1
            elif v==best:count+=1
        vals.append((b,best,count))
    require([v for _,v,_ in vals]==[4,6,6,8,8,8,9,9],vals);return vals
def main():
    vals=table();require(all(sh>b for b,sh,_ in vals),vals)
    print('shadow_table='+','.join(str(x[1]) for x in vals))
    print('disjoint_cubic_pair_states=0')
    print('GENERAL_QUARTIC_THREE_BLOCK_ZERO_INDEPENDENT_PASS')
if __name__=='__main__':main()
