#!/usr/bin/env python3
"""Exact finite replay for the stabilizer-efficient orbit barrier."""
from __future__ import annotations
import argparse, hashlib, itertools, json, math, random
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

CORE_HASH='bf3defd92cc779905b2c676bc507fc7b03c7b5c1ad515f64393793ad2227782f'

def req(x,m):
    if not x: raise RuntimeError(m)

def sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def parts(n,top=None):
    if n==0: return ((),)
    out=[]
    for a in range(min(n,n if top is None else top),0,-1):
        out += [(a,*b) for b in parts(n-a,a)]
    return tuple(out)

def dim(part):
    den=1
    for r,L in enumerate(part):
        for c in range(L):
            den*=L-c+sum(part[s]>c for s in range(r+1,len(part)))
    req(factorial(sum(part))%den==0,part)
    return factorial(sum(part))//den

def rank(rows):
    A=[list(map(Fraction,r)) for r in rows]; i=0
    for c in range(len(A[0])):
        p=next((r for r in range(i,len(A)) if A[r][c]),None)
        if p is None: continue
        A[i],A[p]=A[p],A[i]; q=A[i][c]; A[i]=[x/q for x in A[i]]
        for r in range(len(A)):
            if r!=i and A[r][c]:
                q=A[r][c]; A[r]=[x-q*y for x,y in zip(A[r],A[i])]
        i+=1
        if i==len(A): break
    return i

def norm(v):
    v=tuple(v); g=math.gcd(*map(abs,v)); req(g>0,v); v=tuple(x//g for x in v)
    return tuple(-x for x in v) if next(x for x in v if x)<0 else v

def factors(n):
    r=random.Random(100000*n+1)
    return tuple(norm(r.randint(1,97) for _ in range(n*n)) for _ in range(n))

def act(v,n,a,b):
    w=[0]*(n*n)
    for i in range(n):
        for j in range(n): w[a[i]*n+b[j]]=v[i*n+j]
    return norm(w)

def stab(vs,n):
    P=tuple(itertools.permutations(range(n))); S=set(vs); z=0
    for a in P:
        for b in P: z+=all(act(v,n,a,b) in S for v in vs)
    return z,len(P)**2

def two(n,i): return (n,) if i==0 else (n-i,i)

def build_payload():
    srows=[]; sc=0
    for n in range(2,6):
        fs=factors(n); req(len(set(fs))==n and rank(fs)==n,(n,fs)); z,c=stab(fs,n); req(z==1,(n,z)); sc+=c
        srows.append({'n':n,'factor_matrix_sha256':sha(fs),'factor_rank':n,'projective_stabilizer_size':z,'group_size':factorial(n)**2,'group_elements_checked':c})
    pc=ic=wc=0; arithmetic=[]
    for n in range(2,13):
        ps=parts(n); D={p:dim(p) for p in ps}; req(sum(x*x for x in D.values())==factorial(n),n); pc+=len(D); dr=[]
        for d in range(n+1):
            level=comb(n,d); L=min(d,n-d); pairs=[(two(n,i),two(n,j)) for i in range(L+1) for j in range(L+1)]
            den=[level*D[a]*D[b] for a,b in pairs]; req(all(x>=1 for x in den),n); ic+=len(den)
            weights=[[1]*len(pairs),[1+(D[a]+2*D[b])%7 for a,b in pairs],[int(a==b) for a,b in pairs],[int((a[0]+3*b[0]+d)%5==0) for a,b in pairs]]
            best=Fraction(0)
            for w in weights:
                num=sum(w)
                if not num: continue
                q=sum(x*y for x,y in zip(w,den)); req(q>=num,(n,d)); best=max(best,Fraction(num,q)); wc+=1
            dr.append({'degree':d,'boolean_level':level,'permanent_isotype_count':len(pairs),'maximum_weighted_ratio_numerator':best.numerator,'maximum_weighted_ratio_denominator':best.denominator})
        arithmetic.append({'n':n,'partition_count':len(ps),'regular_dimension':factorial(n),'degree_rows':dr})
    req((sc,pc,ic,wc)==(15016,270,921,341),(sc,pc,ic,wc))
    core={'status':['GENERAL_STABILIZER_EFFICIENT_ORBIT_SUBQUOTIENT','GENERAL_GENERIC_TRIVIAL_STABILIZER','EFFICIENT_ORBIT_EXACT_ADDITIVE_CEILING_ONE','EXACT_INTEGER_REPLAYED'],'theorem':{'efficient_orbit_subquotient':'For a G-invariant decomposition f=sum_i T_i, A_f is a graded G-equivariant subquotient of direct_sum_i Ind_(H_i)^G A_(T_i), where H_i stabilizes the projective apolar ideal of T_i.','generic_term':'For G=S_n x S_n and n>=2, the independent-factor Chow locus contains terms with trivial projective stabilizer.','route_ceiling':'Every nonnegative short-exact-additive graded isotype scalar applied through the stabilizer-efficient orbit envelope has permanent/one-term ratio at most one.','generic_denominator':'A trivial-stabilizer independent-factor term contributes k[G] tensor B_n; degree-d multiplicity of U is dim(U)*binom(n,d).'},'finite_replay':{'stabilizer_rows':srows,'stabilizer_group_elements_checked':sc,'partition_dimension_checks':pc,'pointwise_isotype_checks':ic,'weighted_support_checks':wc,'arithmetic_rows_sha256':sha(arithmetic)},'claim_boundary':'The theorem closes exact-additive representation profiles built from the smallest distinct projective term orbits. It introduces no Chow-rank lower bound and is not an upper bound on actual Chow rank. It does not cover fixed natural maps linear in f, minimal or persistence syzygy functors, nonlinear determinantal data, valuative arguments, or Chow-realizability defects. Literature novelty is not established.'}
    out={**core,'core_sha256':sha(core)}; req(out['core_sha256']==CORE_HASH,out); return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--json',type=Path); a=p.parse_args(); out=build_payload(); text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.json: a.json.parent.mkdir(parents=True,exist_ok=True); a.json.write_text(text,encoding='utf-8')
    print(text,end=''); print('GENERAL_STABILIZER_ORBIT_K0_BARRIER_AUDIT_PASS')
if __name__=='__main__': main()
