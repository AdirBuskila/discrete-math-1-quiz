import itertools, math
from math import factorial as F, gcd
print('1b', (71**120-1)%26, (50**24+F(12))%26, F(12)%13, 71**120-1 % 26)
print('gcd 71^120-1, 50^24+12!', gcd(71**120-1,50**24+F(12)))
# 2c1
P=[(i,j) for i in range(1,4) for j in range(1,4)]
def refl(R): return all((i,i) in R for i in range(1,4))
def sym(R): return all((j,i) in R for (i,j) in R)
def anti(R): return all(not((j,i) in R and i!=j) for (i,j) in R)
def trans(R): return all((a,d) in R for (a,b) in R for (c,d) in R if b==c)
cnt=0;ex=None
for k in range(0,6):
    for R in itertools.combinations(P,k):
        R=set(R)
        if not refl(R) and not sym(R) and not anti(R) and not trans(R):
            cnt+=1; ex=ex or sorted(R)
print('2c1',cnt,ex)
# 2c2: distinct transitive R1,R2 union transitive, intersection nonempty
subs=[set(c) for k in range(10) for c in itertools.combinations(P,k)]
T=[R for R in subs if trans(R)]
found=[(sorted(a),sorted(b)) for a in T for b in T if a!=b and a&b and trans(a|b)]
print('2c2',len(found),found[:2])
# 3a
print('3a',all(((3*x+7*y)%5==0)==((x-y)%5==0) for x in range(-20,20) for y in range(-20,20)))
# 3b
def eg(a,b):
    if b==0: return a,1,0
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
print('3b',eg(48,184),eg(-48,184), 48*4-184, -48*-4+184*-1)
# 1c
print('1c',{k:3*k//gcd(3,k) for k in [1,4,5,6,9,18]})
# 4b
print('4b',[a for a in range(0,50) if all((a*a+a+2)%d for d in range(2,a*a+a+2)) and a*a+a+2>1])
# 2a
from fractions import Fraction as Fr
print('2a',all(sum(Fr(1,(4*k-3)*(4*k+1)) for k in range(1,n+1))==Fr(n,4*n+1) for n in range(1,30)))
# 4c(2): 3^m 5^n
print('4c2 image has 1,2?', 1 in {3**m*5**n for m in range(5) for n in range(5)})
