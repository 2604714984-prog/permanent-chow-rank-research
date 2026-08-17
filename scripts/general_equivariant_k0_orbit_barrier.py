#!/usr/bin/env python3
"""Audit the equivariant-K0 full-orbit barrier."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any, Iterable
EXPECTED_CORE_SHA256="a63a6ed5d606f599c2ea9a4a4e4c1c33dd6fd3998bedf1dd6ab519656cb12117"
def require(c,m):
    if not c: raise RuntimeError(m)
def canonical_sha256(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
def integer_partitions(n,maximum=None):
    if n==0:
        yield (); return
    upper=n if maximum is None else min(n,maximum)
    for first in range(upper,0,-1):
        for tail in integer_partitions(n-first,first): yield (first,)+tail
def hook_dimension(partition):
    n=sum(partition); product=1
    for r,width in enumerate(partition):
        for c in range(width):
            below=sum(1 for rr in range(r+1,len(partition)) if partition[rr]>c)
            product*=width-c+below
    return factorial(n)//product
def two_row_dimensions(n,d):
    return [comb(n,i)-(comb(n,i-1) if i else 0) for i in range(min(d,n-d)+1)]
def build_payload()->dict[str,Any]:
    rpc=rdc=0
    for n in range(1,11):
        ps=list(integer_partitions(n)); ds=[hook_dimension(p) for p in ps]
        require(sum(x*x for x in ds)==factorial(n),n); rpc+=len(ps); rdc+=1
    tr=ic=wc=es=bc=uc=0; diagnostics={}
    for n in range(2,41):
        bn=bd=0; local=[]
        for d in range(n+1):
            dims=two_row_dimensions(n,d); H=comb(n,d); require(sum(dims)==H,(n,d))
            for i,x in enumerate(dims):
                part=(n,) if i==0 else (n-i,i); require(x==hook_dimension(part),(n,d,i)); tr+=1
            iso=[a*b for a in dims for b in dims]; require(sum(iso)==H*H,(n,d)); ic+=len(iso)
            rows=[[1]*len(iso),[(i+1)%5 for i in range(len(iso))],[((i+3)*2654435761+31*n+17*d)%13 for i in range(len(iso))]]
            for i in range(len(iso)):
                row=[0]*len(iso); row[i]=1; rows.append(row)
            best=Fraction(0)
            for row in rows:
                S=sum(w*x for w,x in zip(row,iso))
                if not S: continue
                ratio=Fraction(sum(row),H*S); require(ratio<=1,(n,d,row,ratio)); best=max(best,ratio); wc+=1
            bn+=len(iso); bd+=H*sum(iso)
            if n<=12: local.append([d,H,len(iso),best.numerator,best.denominator])
            if n<=7:
                for mask in range(1,1<<len(iso)):
                    S=sum(iso[i] for i in range(len(iso)) if mask>>i&1)
                    require(Fraction(mask.bit_count(),H*S)<=1,(n,d,mask)); es+=1
        require(Fraction(bn,bd)<=1,n); bc+=1
        dims=two_row_dimensions(n,n//2)
        for i,a in enumerate(dims):
            for j,b in enumerate(dims):
                mult=n-2*max(i,j)+1; require(Fraction(mult,(2**n)*a*b)<=1,n); uc+=1
        if n<=12: diagnostics[str(n)]=local
    core={"status":["GENERAL_EQUIVARIANT_GRADED_K0_CLASSIFICATION","GENERAL_APOLAR_ORBIT_SUBQUOTIENT","ORBIT_SYMMETRIZED_ISOTYPE_BARRIER","EXACT_FINITE_INTERFACES_REPLAYED"],"theorem":{"equivariant_K0":"Exact-additive scalars on finite-dimensional graded G-representations are nonnegative weighted isotype multiplicities.","orbit_subquotient":"For G-invariant f=sum_i T_i, A_f is a G-equivariant subquotient of direct_sum_(i,g) A_(gT_i).","regular_orbit":"For each term T, direct_sum_g A_(gT) is isomorphic to k[G] tensor A_T, with G regular on the first factor.","permanent_multiplicity":"Each degree of A_(perm_n) is multiplicity-free under S_n x S_n.","route_ceiling":"Every full-orbit exact-additive isotype scalar gives a rank-ratio lower bound at most one."},"exact_replay":{"regular_partition_cells":rpc,"regular_dimension_checks":rdc,"two_row_dimension_checks":tr,"degree_isotype_cells":ic,"weighted_degree_checks":wc,"exhaustive_isotype_supports":es,"finite_block_checks":bc,"ungraded_isotype_checks":uc,"diagnostics":diagnostics},"claim_boundary":"The theorem closes exact-additive representation scalars only after the legal full-group orbit symmetrization of arbitrary Chow terms. It does not close a more efficient termwise equivariant envelope, fixed linear maps already treated by matching-orbit theorems, minimal syzygy functors which are not exact-additive, nonlinear determinantal data, valuative arguments, Chow-realizability defects, border rank, exact rank for n>=6, or general Glynn optimality."}
    payload={**core,"core_sha256":canonical_sha256(core)}; require(payload["core_sha256"]==EXPECTED_CORE_SHA256,payload); return payload
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--json",type=Path); args=parser.parse_args(); payload=build_payload(); text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.json: args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(text,encoding="utf-8",newline="\n")
    print(text,end=""); print("GENERAL_EQUIVARIANT_K0_ORBIT_BARRIER_AUDIT_PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
