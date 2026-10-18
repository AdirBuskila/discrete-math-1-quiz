import itertools, math
from math import gcd, factorial as F
from sympy import isprime, primerange
# 1a
rows=list(itertools.product([1,0],repeat=3))
imp=lambda a,b: (not a) or b
print('1a eq',all(imp(p,q and r)==(imp(p,q) and imp(p,r)) for p,q,r in rows), sum(imp(p,q and r) for p,q,r in rows), sum(1 for p,q,r in rows if p and imp(p,q) and imp(p,r)))
# 1c
print('1c', round(-27**(1/3)) if False else None)
# 2a
print('2a', sum(range(2*4+1,4*4,2)), all(sum(range(2*n+1,4*n,2))==3*n*n for n in range(1,40)), 6*2+3, 4*2+1+4*2+3-(2*2+1))
# 2b
def eg(a,b):
    if b==0: return a,1,0
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
print('2b',eg(25,40),[(x,y,25*x+40*y) for x,y in [(-3,2),(2,-3),(3,-2),(-3,-2)]],40%25)
# 2c
P=[(i,j) for i in range(1,4) for j in range(1,4)]
def refl(R): return all((i,i) in R for i in range(1,4))
def sym(R): return all((j,i) in R for (i,j) in R)
def anti(R): return all(not((j,i) in R and i!=j) for (i,j) in R)
def trans(R): return all((a,d) in R for (a,b) in R for (c,d) in R if b==c)
def total(R): return all((i,j) in R or (j,i) in R for i in range(1,4) for j in range(1,4))
opts1={'a':[(1,1),(2,2),(3,3)],'b':[(1,1),(2,2),(1,2)],'c':[(1,1),(2,2),(3,3),(1,2)],'d':[(1,1),(2,2),(3,3),(1,2),(2,3)]}
for k,v in opts1.items(): R=set(v); print('2c1',k,refl(R) and sym(R) and trans(R))
opts2={'a':[(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)],'b':P,'c':[(1,1),(2,2),(3,3),(1,2),(2,3)],'d':[(1,1),(2,2),(3,3),(1,2),(1,3)]}
for k,v in opts2.items(): R=set(v); print('2c2',k,refl(R) and anti(R) and trans(R) and total(R))
print('2c3 sizes of total orders', {len(R) for k in range(0,10) for R in map(set,itertools.combinations(P,k)) if refl(R) and anti(R) and trans(R) and total(R)})
# 3a
import itertools
U=range(4); subs=[frozenset(c) for k in range(5) for c in itertools.combinations(U,k)]
print('3a', all(A-(B&C)==((A-B)|(A-C)) for A in subs for B in subs for C in subs), len({1,2,3}-({2,3}&{3,4})))
# 3b
print('3b',(2*1*2+1+2),3*5==2*7+1)
# 3c
print('3c',F(30)%31,pow(100,150,31),[ (p,(F(30)+1)%p, (100**150-1)%p) for p in (31,37,7,29)], gcd(F(30)+1,100**150-1)>=30, gcd(F(30)+1,100**150-1))
# 4a
print('4a', all(((x+3*y)%4==0)==((x-y)%4==0) for x in range(-20,20) for y in range(-20,20)))
# 4b
rows=list(itertools.product([1,0],repeat=3))
print('4b',[r for r in rows if bool(r[0] and r[1])==bool((not r[1]) or r[2])])
# 4c
print('4c',[p for p in primerange(2,200) if isprime(p**3-1)])
