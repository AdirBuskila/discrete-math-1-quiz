import itertools
from math import gcd, factorial as F, lcm
from sympy import primerange
rows=list(itertools.product([1,0],repeat=3))
imp=lambda a,b:(not a) or b
print('1a',[r for r in rows if not (imp(r[0],r[1]) and not r[2])], sum(1 for r in rows if not (imp(r[0],r[1]) and not r[2])))
# 1b R^-1
R={(1,2),(2,3),(1,3)}; print('1b',{(b,a) for a,b in R})
def trans(R): return all((a,d) in R for (a,b) in R for (c,d) in R if b==c)
P=[(i,j) for i in range(1,4) for j in range(1,4)]
print('1b all', all(trans({(b,a) for a,b in R}) for k in range(10) for R in map(set,itertools.combinations(P,k)) if trans(R)))
# 1c
vals={2**m*5**n for m in range(1,10) for n in range(1,10)}; print('1c',min(vals), 3 in vals, len(vals)==81)
# 2a
print('2a',[n for n in range(1,40) if not n**3<2**n], 11**3)
# 2b
def eg(a,b):
    if b==0: return a,1,0
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
print('2b',eg(65,40),gcd(65,-40),[(x,y,65*x+(-40)*y) for x,y in [(-3,5),(3,5),(-3,-5),(2,3)]],65%40)
# 2c
D={5,6};print('2c',len(D),1+9+4)
# 3a
Qs=0
# 3b
A={2**m*9**n for m in range(10) for n in range(10)};B={5**m*9**n for m in range(10) for n in range(10)}
print('3b',len(A&B),len(A),len(B))
# 3c
n=2**120-1; m=5**20+F(10)+F(12)
print('3c',n%11,m%11,5**20%11,F(10)%11,F(12)%11,gcd(n,m)%11)
# 4a
print('4a',all(((x+y+1)%2==1)==((x-y)%2==0) for x in range(-20,20) for y in range(-20,20)))
# 4b
print('4b',[(p,lcm(p-1,p+1),(p*p-1)//2) for p in primerange(2,30)])
# 4c
for n in (6,7,8):
    A=range(1,2*n+2); od=[x for x in A if x%2]; ev=[x for x in A if x%2==0]
    cnt=sum(1 for k in range(1<<len(A)) if sum(1 for i,x in enumerate(A) if k>>i&1 and x%2)==1)
    print('4c',n,cnt,(n+1)*2**n,len(od),2**len(ev))
