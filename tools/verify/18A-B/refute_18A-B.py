import sympy as sp, itertools, math
from sympy import totient as phi
# 1a
print('perm',math.factorial(4), sum(1 for p in itertools.permutations(range(4)) if all(p[i]!=i for i in range(4))))
# 3a
f=lambda p: int(phi(phi(p*p)))%2
print([ (p,f(p)) for p in sp.primerange(2,200) if f(p)!=0 or p<5])
# 3b
n=sp.symbols('n',integer=True)
a=lambda n:(2-2*n)*2**n+18*3**n
seq=[20,54]
for i in range(2,15): seq.append(4*seq[-1]-4*seq[-2]+2*3**i)
print(all(a(i)==seq[i] for i in range(15)))
# 4a
print(all(sum(math.comb(N,k)*(9**k+4**k) for k in range(N+1))==10**N+5**N for N in range(12)))
# 4b
print('4b1',sum(1 for w in itertools.product('abcdef',repeat=4) if w[2:]==('e','f')))
print('4b2',math.comb(6,4), 'ordered distinct',6*5*4*3)
c=0
for w in itertools.permutations('abcdef'):
    s=''.join(w)
    if 'abc' in s and s[0] in 'ad': c+=1
print('4b3',c)
# 4c ordered / unordered
mins=(4,3,5,2)
from math import factorial
tot=0
for L in range(14,23):
    cnt=0
    for x in itertools.product(range(L+1),repeat=3):
        d=L-sum(x)
        if d<0: continue
        t=x+(d,)
        if all(t[i]>=mins[i] for i in range(4)):
            cnt+=factorial(L)//math.prod(factorial(v) for v in t)
    tot+=cnt
print('4c ordered',tot)
print('4c unordered',sum(1 for t in itertools.product(range(23),repeat=4) if sum(t)<=22 and all(t[i]>=mins[i] for i in range(4))))
# counts per length
