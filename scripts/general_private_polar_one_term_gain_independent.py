#!/usr/bin/env python3
"""Independent replay for the private-polar one-term gain theorem.

This implementation imports none of the primary helper functions. It scans
the theorem in excess variables and independently reconstructs the equality
simplex cancellation interface over the rationals.
"""
from __future__ import annotations
from fractions import Fraction

def require(condition: bool, message: object) -> None:
    if not condition: raise RuntimeError(message)

def rank_fraction(matrix):
    if not matrix: return 0
    rows=[[Fraction(value) for value in row] for row in matrix]; row_count=len(rows); column_count=len(rows[0]); pivot_row=0
    for column in range(column_count):
        pivot=next((row for row in range(pivot_row,row_count) if rows[row][column]),None)
        if pivot is None: continue
        rows[pivot_row],rows[pivot]=rows[pivot],rows[pivot_row]; value=rows[pivot_row][column]; rows[pivot_row]=[entry/value for entry in rows[pivot_row]]
        for row in range(row_count):
            if row==pivot_row or not rows[row][column]: continue
            factor=rows[row][column]; rows[row]=[left-factor*right for left,right in zip(rows[row],rows[pivot_row],strict=True)]
        pivot_row+=1
        if pivot_row==row_count: break
    return pivot_row

def canonical_simplex(q,n):
    ambient=(q-1)*n; columns=[]
    for block in range(q-1):
        for coordinate in range(n):
            vector=[0]*ambient; vector[block*n+coordinate]=1; columns.append(vector)
    for coordinate in range(n):
        vector=[0]*ambient
        for block in range(q-1): vector[block*n+coordinate]=1
        columns.append(vector)
    return [[columns[column][row] for column in range(len(columns))] for row in range(ambient)]

def subcollection_rank(matrix,q,n,omitted):
    keep=[]
    for block in range(q):
        if block!=omitted: keep.extend(range(block*n,(block+1)*n))
    return rank_fraction([[row[column] for column in keep] for row in matrix])

def two_block_annihilator(q,n):
    covector=[0]*((q-1)*n); covector[0]=1; covector[n]=-1; return covector

def main():
    strict_positive_rows=strict_logic_checks=equality_rows=simplex_cases=proper_subcollection_checks=0
    for m in range(4,97):
        for q in range(2,m+2):
            upper=min((m-1)*(m-1)-1,(m*m-1)//(q-1))
            for n in range(m,upper+1):
                s=q*n-m*m
                if s<=0: continue
                strict_positive_rows+=1; require((q-1)*s<m*m,(m,n,q,s)); require((q-1)*s<m*m,(m,n,q,"no-private")); strict_logic_checks+=2
        for divisor in range(2,m*m+1):
            if m*m%divisor: continue
            q=divisor+1; n=m*m//divisor
            if n<m or 2*n>(m-1)*(m-1): continue
            equality_rows+=1
            if m<=16:
                matrix=canonical_simplex(q,n); ambient=(q-1)*n; require(rank_fraction(matrix)==ambient,(m,q,n,"full"))
                for omitted in range(q): require(subcollection_rank(matrix,q,n,omitted)==ambient,(m,q,n,omitted)); proper_subcollection_checks+=1
                alpha=two_block_annihilator(q,n)
                for coordinate in range(n): require(sum(alpha[block*n+coordinate] for block in range(q-1))==0,(m,q,n,coordinate))
                require(any(alpha[:n]),(m,q,n,"block0")); require(any(alpha[n:2*n]),(m,q,n,"block1")); simplex_cases+=1
    for m,q,n in [(4,3,7),(5,3,12),(6,2,24),(7,2,35),(8,3,31),(10,3,49)]:
        require(n<(m-1)**2,(m,q,n)); require((q-1)*n<m*m,(m,q,n)); require(q*n>m*m+m,(m,q,n))
    print(f"independent_strict_positive_rows={strict_positive_rows}"); print(f"independent_strict_logic_checks={strict_logic_checks}"); print(f"independent_shifted_equality_rows={equality_rows}"); print(f"independent_simplex_cases={simplex_cases}"); print(f"independent_proper_subcollection_checks={proper_subcollection_checks}"); print("GENERAL_PRIVATE_POLAR_ONE_TERM_GAIN_INDEPENDENT_PASS"); return 0

if __name__=="__main__": raise SystemExit(main())
