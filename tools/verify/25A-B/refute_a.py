import itertools
from math import gcd, factorial as F
# 1a
rows=list(itertools.product([1,0],repeat=3))
f=lambda p,q,r: (not (p or not q)) or r
print('1a false rows',[x for x in rows if not f(*x)])
# CNF c equivalence
c=lambda p,q,r: ((not p) or (not q) or r) and ((not p) or q or r) and (p or q or r)
print('1a c ok',all(bool(f(*x))==bool(c(*x)) for x in rows))
d=lambda p,q,r: ((not p) or (not q) or r) and ((not p) or q or r)
print('1a d ok?',all(bool(f(*x))==bool(d(*x)) for x in rows))
# 1b
A=range(1,11); print('1b',sum(1 for k in range(1<<10) if (k&3)==3))
# 1c
print('1c',sorted({gcd(12,x) for x in range(1,200)}), gcd(12,8))
# 2a
print('2a',[(23**n-1)%11 for n in range(1,8)], 23**2-1)
# 2b
A={5**n*7**m for n in range(10) for m in range(10)}; B={5**n for n in range(10)}; C={7**n for n in range(10)}
print('2b',len(A),len(B|C))
# 2c
print('2c', 2**9)
# 3a
S=[1,2,3,6,8,9,16,18]
print('3a',sum(1 for x in S for y in S if y%x==0))
# 3b
def eg(a,b):
    if b==0: return a,1,0
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
print('3b',eg(48,84),[(x,y,48*x+84*y) for x,y in [(2,-1),(-1,2),(1,-1),(-2,1)]], 84%48)
# 3c
Aa={1,2};Bb={2,3};Cc={1,4,5}; print('3c',len((Bb-Aa)|(Cc-Aa)))
# 4b
a=5**44-1; b=8**88+F(22); g=gcd(a,b); print('4b gcd',g, g>19,[g%p for p in (23,29,31,37)], 5**44%23, F(22)%23)
# 4c
A={1,2};B={2,3};C={3}; print('4c',len((A&B)|C), (A&B)|C, A&(B|C))
# brute: statement (A∩B)∪C = A∩(B∪C) ⇒ C⊆A over subsets of 4
import itertools
U=range(4); subs=[frozenset(c) for k in range(5) for c in itertools.combinations(U,k)]
print('4c stmt', all((not(((A&B)|C)==(A&(B|C)))) or C<=A for A in subs for B in subs for C in subs))
