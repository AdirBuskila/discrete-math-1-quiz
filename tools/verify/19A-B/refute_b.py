import itertools, math
from sympy import *
for p,q,r in itertools.product([0,1],repeat=3):
    if ((p and q)==((not q) or r)): print('DNF',p,q,r)
# surj 3->3
print(sum(1 for f in itertools.product(range(3),repeat=3) if len(set(f))==3))
# symmetric relations on {1,2}
print(2**3)
A={(m,n,0,q) for m in range(20) for n in range(20) for q in range(20)}  # (2,5,11 exps)
a={2**m*5**n*11**q for m in range(20) for n in range(20) for q in range(20)}
b={3**m*5**n*7**q for m in range(20) for n in range(20) for q in range(20)}
print(len(a),len(b),sorted(a&b)==[5**k for k in range(20)],len(a&b),len(a|b))
# 3b
cls=[5,3,4]; print([2*s-1 for s in cls])
# 3c
k,n=symbols('k n')
for N in (2,3,5): print(sum(binomial(N,j)*(3**(2*j)+2**(2*j)) for j in range(N+1)), 10**N+5**N)
print(10**10-math.factorial(10), math.comb(20,10))
# 4d
cl=[{1,2},{3},{4,5}]; R={(a,b) for c in cl for a in c for b in c}; print(len(R))
print(any((a,b) in R and (b,a) in R and a!=b for a,b in R))
# 4e brute
for p,q in [(3,5),(3,7),(5,7),(5,11),(7,11),(3,13)]:
    nn=(totient(p)**totient(q)-1)*((1+totient(q))**totient(p)-1); print(p,q,nn%(p*q))
# 5ab
odd=[m for m in range(1,500) if totient(m)%2==1]; print(odd)
# 5d
a_=Function('a')
print(rsolve(a_(n)-6*a_(n-1)+9*a_(n-2),a_(n),{a_(0):5,a_(1):21}))
# 2a
for N in range(1,30): assert sum(range(N+1,2*N+1))*2==N*(3*N+1)
