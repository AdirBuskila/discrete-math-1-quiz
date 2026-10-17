# Checks of the 23A-B keys. ASCII output only.
import itertools, math
from math import gcd, factorial
# Q1a
for p,q,r in itertools.product([0,1],repeat=3):
    imp=lambda a,b:(not a) or b
    assert imp(p,q or r)==(imp(p,q) or imp(p,r))
print("Q1a OK")
# Q1b: counterexample not transitive
R2={(1,1),(2,2),(3,3),(1,2),(2,1)}; R1={(1,1),(2,2),(3,3),(2,3),(3,2)}
U=R1|R2
assert (1,2) in U and (2,3) in U and (1,3) not in U
print("Q1b OK")
# Q1c: f(m,n)=2^n(2m+1) hits every 1..N
seen={2**n*(2*m+1) for m in range(0,3000) for n in range(0,14)}
assert all(k in seen for k in range(1,2000))
print("Q1c OK")
# Q2b extended euclid
def eg(a,b):
    if b==0: return a,1,0
    d,x,y=eg(b,a%b); return d,y,x-(a//b)*y
assert 3*55+(-4)*40==5 and 3*55+4*(-40)==5 and gcd(55,-40)==5
print("Q2b OK", eg(55,40))
# Q2c: two distinct total orders on {1,2}, union equivalence? refuted by given example
Rr1={(1,1),(2,2),(1,2)}; Rr2={(1,1),(2,2),(2,1)}
assert Rr1|Rr2=={(1,1),(2,2),(1,2),(2,1)} and Rr1&Rr2=={(1,1),(2,2)}
print("Q2c OK")
# Q3b
A={5**m*9**n for m in range(10) for n in range(10)}
B={5**m*7**n for m in range(10) for n in range(10)}
assert len(A)==100 and len(B)==100 and len(A&B)==10 and len(A|B)==190
print("Q3b OK: 10 + 2^190 + 2^10000")
# Q3c
assert gcd(81**11-1, factorial(22)+24)%46==0
print("Q3c OK")
# Q4a
R=lambda x,y:(x+5*y)%3==0
rng=range(-20,21)
assert all(R(x,x) for x in rng)
assert all(R(y,x) for x in rng for y in rng if R(x,y))
assert all(R(x,z) for x in range(-9,10) for y in range(-9,10) for z in range(-9,10) if R(x,y) and R(y,z))
assert R(0,3) and R(3,0)
assert all((R(x,0))==(x%3==0) and R(x,1)==(x%3==1) and R(x,2)==(x%3==2) for x in rng)
print("Q4a OK")
# Q4b
def lcm(a,b): return abs(a*b)//gcd(a,b) if a and b else 0
for n in range(0,200):
    v=lcm(n-1,n+1)
    if n==0: assert v==1
    elif n==1: assert v==0
    elif n==2: assert v==3
    elif n%2==0: assert v==n*n-1
    else: assert v==(n*n-1)//2
print("Q4b OK")
# Q4c brute force small n
for n in range(1,6):
    full=set(range(1,2*n+2)); odds={x for x in full if x%2}
    cnt=0
    for mask in range(1<<(2*n+1)):
        Bs={i+1 for i in range(2*n+1) if mask>>i&1}
        if Bs|odds==full: cnt+=1
    assert cnt==2**(n+1)
print("Q4c OK")
