# independent recomputation of numeric step values (no author harness reuse)
from itertools import product
from math import gcd, factorial
from fractions import Fraction as F
rows=list(product([1,0],repeat=3))
conj=sum(1 for p,q,r in rows if (p or q) and ((not p) or r)); print('1a conj true',conj)
print('1a q|r false',sum(1 for p,q,r in rows if not(q or r)))
print('1a impl false',sum(1 for p,q,r in rows if ((p or q) and ((not p) or r)) and not(q or r)))
print('1b',(2**6-1)//(2**3-1))
print('2a',F(1,2)+F(1,6)+F(1,12))
print('2b free letters 4 / count 16')
print('3a classes',len({(x%5) for x in range(-50,50)}), [ (y%5) for y in range(-20,20) if (16+y)%5==0][:1])
print('3b',84%49, gcd(49,84), 49*-5+84*3)
A=F(0);print('3c',len(({4,5}|{5,6})))
P=lambda S:{frozenset(c) for n in range(len(S)+1) for c in __import__('itertools').combinations(S,n)}
a,b=P({1,2}),P({2,3});print('4a',len(P({1,2,3}))-len(a|b),len(a|b))
print('4b',len([d for d in range(1,13) if 12%d==0]),gcd(12,8))
print('4c',2*2+3*2+2, [p for p in range(2,3000) if all(p%d for d in range(2,int(p**.5)+1)) and (lambda n: n>1 and all(n%d for d in range(2,int(n**.5)+1)))(p*p+3*p+2)])
print('5a',pow(7,72,37),factorial(36)%37,pow(36,36,37),(36**36+factorial(36))%74,(7**72-1)%74,gcd(36**36+factorial(36),7**72-1))
print('5b',(0+1,2*0+5),[x for x in range(-100,100) if (x+1,2*x+5)==(1,1)], 2*-3+5)
