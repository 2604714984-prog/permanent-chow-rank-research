#!/usr/bin/env python3
from itertools import combinations, permutations
import json, hashlib
N=4
MATCHINGS=tuple(sum(1<<(r*N+p[r]) for r in range(N)) for p in permutations(range(N)))
ALL24=(1<<24)-1
RPS=tuple(permutations(range(4)))
def pc(x): return x.bit_count()
def env(A):
    z=0
    for i,M in enumerate(MATCHINGS):
        if pc(A&M)>=3:z|=1<<i
    return z
def transform(A,rp,cp):
    z=0
    for x in range(16):
        if A>>x&1:z|=1<<(rp[x//4]*4+cp[x%4])
    return z
def canon_cover(frames):
    best=None
    for rp in RPS:
      for cp in RPS:
        rep=tuple(sorted(transform(A,rp,cp) for A in frames))
        if best is None or rep<best:best=rep
    return best
def contained(A):
    z=0
    for i,M in enumerate(MATCHINGS):
        if M & ~A == 0:z|=1<<i
    return z
def pair_motion(A,B,forbid_matching_q=False):
    I=A&B
    if pc(I)<4:return 0
    z=0
    for i,M in enumerate(MATCHINGS):
        T=M&A
        if pc(T)!=3 or T & ~B:continue
        for j in range(16):
            if I>>j&1 and not (T>>j&1):
                Q=T|(1<<j)
                if forbid_matching_q and Q in MATCHINGS:continue
                z|=1<<i;break
    return z
def equality_frames():
    out=[]
    for t in combinations(range(16),6):
        A=sum(1<<x for x in t)
        if pc(env(A))==6 and contained(A)==0:out.append(A)
    assert len(out)==288
    return out
def exact_covers(eq):
    by_env={env(A):A for A in eq}; envs=list(by_env); covers=set()
    for e0 in envs:
      if not (e0&1):continue
      others=[e for e in envs if not (e&e0)]
      for a in range(len(others)):
        e1=others[a]
        for b in range(a+1,len(others)):
          e2=others[b]
          if e1&e2:continue
          rem=ALL24^(e0|e1|e2)
          if rem in by_env and not (rem&(e0|e1|e2)):
            covers.add(tuple(sorted((by_env[e0],by_env[e1],by_env[e2],by_env[rem]))))
    return tuple(covers)
def payload():
    eq=equality_frames(); covers=exact_covers(eq); assert len(covers)==2016
    orbits={}
    for C in covers:orbits.setdefault(canon_cover(C),C)
    assert len(orbits)==18
    bests=[]
    for C in orbits.values():
      best=0
      for M in MATCHINGS:
        rem=[x for x in range(16) if not (M>>x&1)]
        positives=[M|(1<<a)|(1<<b) for a,b in combinations(rem,2)]
        for bi,B in enumerate(positives):
          for D in positives[bi:]:
            frames=list(C)+[B,D]; total=0
            for i,A in enumerate(frames):
              R=contained(A)
              for j,E in enumerate(frames):
                if i!=j:R|=pair_motion(A,E,forbid_matching_q=(i<4))
              total|=R
            best=max(best,pc(total))
      bests.append(best)
    assert max(bests)==7
    return {'equality_frames':288,'exact_24_matching_covers':2016,'row_column_cover_orbits':18,'orbit_maximum_reachable_matching_counts':sorted(bests),'global_maximum_reachable_matching_count':7,'perm4_matching_count':24,'extremal_four_zero_cover_first_order':'EXCLUDED'}
def main():
    p=payload();core=json.dumps(p,sort_keys=True,separators=(',',':')).encode();p['core_sha256']=hashlib.sha256(core).hexdigest();print(json.dumps(p,indent=2,sort_keys=True))
if __name__=='__main__':main()
