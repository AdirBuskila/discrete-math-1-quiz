import itertools, math
from sympy import *
from sympy.utilities.iterables import multiset_partitions
# 1c bell3
print('bell3', len(list(multiset_partitions([1,2,3]))))
print('inj', math.perm(5,3))
# 1f
for p,q,r in itertools.product([0,1],repeat=3):
    v = p and ((not r) or p) and ((not q) or r)
    if v: print('DNF',p,q,r)
# 2b
A={(n,n,m) for n in range(100) for m in range(100)}
B={(n,m,m) for n in range(100) for m in range(100)}
print('AB',len(A&B), all(x[0]==x[1]==x[2] for x in A&B))
# 3b/3c count by brute force for n=8,9,10
def eqcount(n):
    cnt=0
    def parts(s):
        if not s: yield []; return
        f=s[0]
        for p in parts(s[1:]):
            yield [[f]]+p
            for i in range(len(p)):
                yield p[:i]+[[f]+p[i]]+p[i+1:]
    for p in parts(list(range(n))):
        sz=sorted(len(b) for b in p)
        if len(p)==3 and 2 in sz and 3 in sz:
            cnt+=1; 
    return cnt
for n in (8,9,10):
    print(n, eqcount(n), math.comb(n,2)*math.comb(n-2,3))
# 3d
pairs=[(1,1),(1,2),(2,1),(2,2)]
for k in range(16):
    R={pairs[i] for i in range(4) if k>>i&1}
    refl=(1,1) in R and (2,2) in R
    sym=all(((b,a) in R) for a,b in R)
    if refl and not sym:
        antis=all(not((b,a) in R and a!=b) for a,b in R)
        tr=all(((a,d) in R) for a,b in R for c,d in R if b==c)
        tot=all(((a,b) in R or (b,a) in R) for a in (1,2) for b in (1,2))
        print('3d',R,antis,tr,tot)
# 4
print('4b', sum(math.comb(400,k) for k in (3,4,5)))
print('4c', math.factorial(3)*math.factorial(4)*math.factorial(3))
print('4d', 2**5)
print('4e', [m for m in range(1,20) if 2**(m-1)==1024], totient(11), pow(10,10,11))
# 5c
n=symbols('n'); 
print(rsolve(Function('a')(n)-5*Function('a')(n-1)+6*Function('a')(n-2),Function('a')(n),{Function('a')(0):7,Function('a')(1):15}))
# induction check
print([k for k in range(1,60) if k*k>=2**k])
