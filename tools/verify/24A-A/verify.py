# Checks of the official 24A-A answers. ASCII output only.
import itertools
from math import gcd, factorial

imp = lambda a, b: (not a) or b
T = [True, False]
rows = list(itertools.product(T, repeat=3))
# Q1a
assert all(imp(p, q and r) == (imp(p, q) and imp(p, r)) for p, q, r in rows)
print("Q1a OK")


# Q1b
def P(s):
    s = list(s)
    return frozenset(frozenset(c) for k in range(len(s) + 1) for c in itertools.combinations(s, k))


e = frozenset()
x = P(P(P(e)))
assert x == frozenset({e, frozenset({e}), frozenset({frozenset({e})}), frozenset({e, frozenset({e})})})
print("Q1b OK")
# Q1c
assert len({n ** 3 for n in range(-1000, 1001)}) == 2001
print("Q1c OK")
# Q2a
assert all(sum(2 * n + 1 + 2 * i for i in range(n)) == 3 * n * n for n in range(1, 200))
print("Q2a OK")
# Q2b
assert 25 * -3 + 40 * 2 == 5 == gcd(25, 40)
print("Q2b OK")
# Q2c
S = [1, 2, 3]
R1 = {(1, 1), (2, 2), (3, 3)}
R2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}
sym = lambda R: all((b, a) in R for a, b in R)
tr = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
rf = lambda R: all((x, x) in R for x in S)
anti = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
tot = lambda R: all((a, b) in R or (b, a) in R for a in S for b in S)
assert rf(R1) and sym(R1) and tr(R1)
assert rf(R2) and anti(R2) and tr(R2) and tot(R2)
print("Q2c OK")
# Q3a
subs = [frozenset(c) for k in range(5) for c in itertools.combinations(range(4), k)]
assert all(a - (b & c) == (a - b) | (a - c) for a in subs for b in subs for c in subs)
print("Q3a OK")
# Q3b
assert all((x * y) % 2 == 1 for x in range(-21, 22, 2) for y in range(-21, 22, 2))
print("Q3b OK")
# Q3c
assert (factorial(30) + 1) % 31 == 0 and (100 ** 150 - 1) % 31 == 0
assert gcd(factorial(30) + 1, 100 ** 150 - 1) >= 30
assert 100 ** 5 == 10 ** 10 and 100 ** 5 != 10 ** 7
print("Q3c OK; note: the key writes (10^7)^30 but 100^5 = 10^10")
# Q4a
Rr = lambda x, y: (x + 3 * y) % 4 == 0
rg = range(-12, 13)
assert all(Rr(x, x) for x in rg) and all(Rr(y, x) for x in rg for y in rg if Rr(x, y))
assert all(Rr(x, z) for x in rg for y in rg for z in rg if Rr(x, y) and Rr(y, z))
assert Rr(0, 4) and Rr(4, 0)
for r in range(4):
    assert all(Rr(r, x) == ((x + 3 * r) % 4 == 0) for x in rg)
print("Q4a OK")
# Q4b
f = lambda p, q, r: (p and q) == ((not q) or r)
dnf = lambda p, q, r: (p and q and r) or ((not p) and q and (not r))
assert all(f(*x) == dnf(*x) for x in rows)
print("Q4b OK")
# Q4c
isp = lambda n: n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
assert [p for p in range(2, 300) if isp(p) and isp(p ** 3 - 1)] == [2]
print("Q4c OK")
