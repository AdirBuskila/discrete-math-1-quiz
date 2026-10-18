import sympy as sp, itertools, math
from sympy import totient as phi
seq=[0,3]
for i in range(2,12): seq.append(7*seq[-1]-12*seq[-2]-6)
print(seq==[4**i-1 for i in range(12)], [i for i in range(12) if sp.isprime(seq[i])])
print([n for n in range(1,3000) if sp.isprime(n) and sp.isprime(phi(n))], phi(1)==phi(2))
print(all(n**3<10**n for n in range(1,200)))
print(all(sum(math.comb(N,k)*(2**k*3**k+5**N) for k in range(N+1))==7**N+10**N for N in range(10)))
print('4a',2**99+100*2**99==101*2**99, sum(math.comb(100,k) for k in range(1,101,2))==2**99)
c=sum(1 for p in itertools.permutations(range(1,8)) if set(p[:3])=={1,2,3}); print('4b',c)
print('4c',sum(1 for a in range(19) for b in range(19) if a>=5 and b>=3 and 18-a-b>=7))
n=math.gcd(11,70**10-1); print(n, phi(phi(n+n*n)), phi(phi(n+n*n))%8)
# 1b2 brute: small sets, B subset A check
U=range(5)
def P(S): return {frozenset(c) for r in range(len(S)+1) for c in itertools.combinations(S,r)}
bad=0
for A in P(U):
  for B in P(U):
    if 2<len(B)<len(A) and P(A|B)==(P(A)|P(B)) and not (B<A): bad+=1
print('1b2 counter',bad)
# 3b
R0={(1,1),(2,2)}
for extra in [(1,2),(2,1)]:
    R=R0|{extra}
    print(R,'total',all((a,b) in R or (b,a) in R for a in (1,2) for b in (1,2)),'antisym',all(not((a,b) in R and (b,a) in R) or a==b for a in (1,2) for b in (1,2)))
