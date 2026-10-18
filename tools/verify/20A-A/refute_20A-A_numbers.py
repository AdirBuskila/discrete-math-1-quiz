from math import gcd, factorial as F, comb
from sympy import totient, factorint
print('22A-A 1c', (pow(16,15,31)+pow(7,60,31)+37)%31, '5c',(pow(36,15,31)+pow(8,60,31)+47)%31)
print('22A-B 1c', gcd(25**20+F(40), 8**80+40) if False else gcd(25**20+F(40), 8**80+40), factorint(gcd(25**20+F(40), 8**80+40)))
print('22A-B 5c', gcd(36**20+F(40), 10**80+40), factorint(gcd(36**20+F(40), 10**80+40)))
print('23A-B 3c', gcd(81**11-1, F(22)+24), gcd(81**11-1, F(22)+24)%46)
print('20A-A phi120',totient(120),'3a',sum(1 for x in range(1,101) if x%3 and x%5 and x%7))
import itertools
print('2a1',sum(1 for p in itertools.permutations(range(1,8)) if abs(p.index(1)-p.index(2))<3 and max(p.index(i) for i in (1,2,3))-min(p.index(i) for i in (1,2,3))==2), sum(1 for p in itertools.permutations(range(1,8)) if p.index(1)<p.index(2)))
# 2b2
cnt=0
for p in itertools.permutations('abcdxyz'):
    if set(p[:4])==set('abcd') and p[0] in 'ab': cnt+=1
print('2b2',cnt)
# 5b
print('5b',sum(1 for a in range(23) for b in range(23) for c in range(23) for d in range(23) if a+b+c+d==22 and a>=3 and b>=1 and c>=4 and d>=2))
# recurrence
a=[14,27]
for n in range(2,12): a.append(15*2**n-a[n-2])
import math
print(a[:10],[12*2**n+2*round(math.cos(n*math.pi/2))+3*round(math.sin(n*math.pi/2)) for n in range(10)])
# 4b
print(comb(6,4), 6*5*4*3)
# 6a
n=5
A=sum(comb(n,k)*3**k*5**(n-k) for k in range(n+1));B=sum(comb(n,k)*7**k*5**(n-k) for k in range(n+1))
print(A==8**n,B==12**n,totient(A*B),2**(5*n)*3**(n-1))
# 4b 22A-A
for n in (4,5,6):
    print(n,sum(1 for m in range(2**(2*n+1)) if bin(m&sum(1<<(i-1) for i in range(1,2*n+2,2))).count('1')==1)==(n+1)*2**n,
      sum(1 for m in range(2**(2*n+1)) if 1<bin(m).count('1')<2*n+1)==2**(2*n+1)-2*n-3)
# 4c 23A-B
    A_=range(1,2*n+2);odd=sum(1<<(i-1) for i in range(1,2*n+2,2));full=(1<<(2*n+1))-1
    print(sum(1 for m in range(1<<(2*n+1)) if m|odd==full)==2**(n+1))
# degree seq
import networkx as nx
print(nx.is_graphical([1,1,2,3,3,3,6,7,8]))
# 4b lcm
for n in range(0,10): print(n, math.lcm(n-1,n+1) if n>0 else 1, end='; ')
print()
