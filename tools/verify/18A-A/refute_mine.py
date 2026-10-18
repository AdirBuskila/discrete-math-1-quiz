import itertools, sympy as sp
from math import comb, factorial
from sympy import totient
# 19S-A
p,q,r=sp.symbols('p q r')
rows=[(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1) if bool(a and b)==bool((not b) or c)]
print("1ו true rows (p,q,r):",rows, len(rows))
print("1ה", sum(1 for f in itertools.product(range(1,6),repeat=5) if set(f)=={1,2,3,4,5} and {f[0],f[1]}=={1,2}))
print("2ב", 10*10, 18, "10*2^1000")
n=sp.symbols('n')
print("3ג2", totient(70**2), totient(4900))
print("4א",6**4,"4ב",sum(1 for f in itertools.product(range(1,7),repeat=4) if f[0]>f[1]>f[2]>f[3]))
print("4ג",sum(1 for f in itertools.product(range(1,7),repeat=4) if len(set(f))==4 and {f[0],f[1]}=={1,2}))
# 4ד
primes=[3,5,7,11,13]
cnt=set()
import math
for assign in itertools.product(range(3),repeat=5):
    prods=[1,1,1]
    for pr,a in zip(primes,assign): prods[a]*=pr
    if all(x>1 for x in prods): cnt.add(frozenset(prods))
print("4ד",len(cnt))
print("4ה",sum(1 for t in itertools.permutations(range(1,7),4) if t[-1]%2==0))
print("4ו",sum(1 for t in itertools.permutations(range(1,7)) if max(t.index(1),t.index(2),t.index(3))-min(t.index(1),t.index(2),t.index(3))==2))
for k in (3,6,9): print("3ג1 n=",k+0, 2**(k-5) if k>=5 else None)
print("3ג1 brute n=10", sum(1 for m in range(2**10) if not any(m>>i&1 for i in range(4)) and (m>>6&1)))
# 18A-A
print("3א",[pow(totient(pp),int(totient(pp)),pp) for pp in sp.primerange(2,60)])
a=lambda k:3**(k+1)-3*2**k+5**(k+2)
seq=[25,128]
for k in range(2,12): seq.append(5*seq[-1]-6*seq[-2]+6*5**k)
print("3ב",seq==[a(k) for k in range(12)])
print("4א",all(sum(comb(m,k)*(3**k+4**k) for k in range(m+1))==4**m+5**m for m in range(12)))
print("4ב1",2*36,"2",6*5*4*3,"3",sum(1 for t in itertools.permutations('abcdef') if 'ab' in ''.join(t) and ('cd' in ''.join(t) or 'dc' in ''.join(t))))
tot=0
for A in range(4,26):
 for B in range(3,26-A):
  for C in range(5,26-A-B):
   D=25-A-B-C
   if D>=2: tot+=factorial(25)//(factorial(A)*factorial(B)*factorial(C)*factorial(D))
print("4ג",tot)
# Fibonacci
s5=sp.sqrt(5);F=lambda k:((1+s5)/2)**k-((1-s5)/2)**k
print("5ג",[sp.simplify(F(k)/s5) for k in range(8)])
