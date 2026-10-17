from math import gcd, factorial
import itertools
print(gcd(36**36+factorial(36), 7**72-1))
print(gcd(49,84))
# 2b
n=0
A='abcdef'
for m in range(64):
    B={A[i] for i in range(6) if m>>i&1}
    if B&{'a','b'}=={'a'}: n+=1
print(n)
# 2c(1): R refl sym antisym on {1,2,3}
pairs=[(i,j) for i in(1,2,3) for j in (1,2,3)]
res=set()
for m1 in range(512):
  R1={pairs[i] for i in range(9) if m1>>i&1}
  if all((i,i) in R1 for i in(1,2,3)) and all(((b,a) in R1) for a,b in R1) and all(not((b,a) in R1 and a!=b) for a,b in R1): res.add(frozenset(R1))
print(len(res))
# 3a
print(sorted({(4*x+y)%5==0 for x in range(-10,10) for y in range(-10,10) if (x-y)%5==0}))
print([ (x,y) for x in range(-5,6) for y in range(-5,6) if ((4*x+y)%5==0)!=((x-y)%5==0)])
print(-5*49+3*84)
print(sorted({gcd(12,x) for x in range(1,1000)}))
print([p for p in range(2,200) if all((p*p+3*p+2)%d for d in range(2,p*p+3*p+2)) ][:3])
