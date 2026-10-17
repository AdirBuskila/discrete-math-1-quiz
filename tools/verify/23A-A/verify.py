# Checks of the official 23A-A answers. ASCII output only.
import itertools
import random
from math import gcd, factorial, lcm

imp = lambda a, b: (not a) or b
T = [True, False]
rows = list(itertools.product(T, repeat=3))
# Q1a
S = lambda p, q, r: imp(p, q) and (not r)
bad = [x for x in rows if not S(*x)]
assert len(bad) == 5


def clause(x):
    return lambda p, q, r: any((not v) if val else v for v, val in zip((p, q, r), x))


cnf = lambda p, q, r: all(clause(x)(p, q, r) for x in bad)
assert all(S(*x) == cnf(*x) for x in rows)
# the key lists exactly these five clauses
key = {(True, True, True), (True, False, True), (True, False, False), (False, True, True), (False, False, True)}
assert set(bad) == key
print("Q1a OK")
# Q1b
A = [1, 2, 3, 4]
pairs = [(a, b) for a in A for b in A]
random.seed(1)
cnt = 0
for _ in range(20000):
    R = {p for p in pairs if random.random() < 0.3}
    if all((a, d) in R for a, b in R for c, d in R if b == c):
        Ri = {(b, a) for a, b in R}
        assert all((a, d) in Ri for a, b in Ri for c, d in Ri if b == c)
        cnt += 1
print("Q1b OK on", cnt, "transitive relations")
# Q1c
vals = {}
for m in range(1, 25):
    for n in range(1, 25):
        assert 2 ** m * 5 ** n not in vals
        vals[2 ** m * 5 ** n] = 1
assert 3 not in vals
print("Q1c OK")
# Q2a
assert all(n ** 3 < 2 ** n for n in range(10, 500)) and not (9 ** 3 < 2 ** 9)
print("Q2a OK")
# Q2b
assert 65 * -3 + (-40) * (-5) == 5 == gcd(65, -40)
print("Q2b OK")
# Q2c
parts = [{1}, {2, 3, 4}, {5, 6}]
R = {(a, b) for p in parts for a in p for b in p}
assert len(R) == 14
print("Q2c OK")
# Q3a
sub = [frozenset(c) for k in range(5) for c in itertools.combinations(range(4), k)]
assert all((b - a) | (c - a) <= (b | c) - a for a in sub for b in sub for c in sub)
print("Q3a OK")
# Q3b
A_ = {2 ** m * 9 ** n for m in range(10) for n in range(10)}
B_ = {5 ** m * 9 ** n for m in range(10) for n in range(10)}
assert len(A_) == 100 and len(B_) == 100
assert A_ & B_ == {9 ** n for n in range(10)} and len(A_ & B_) == 10
print("Q3b OK")
# Q3c
n = 2 ** 120 - 1
m = 5 ** 20 + factorial(10) + factorial(12)
assert n % 11 == 0 and m % 11 == 0 and gcd(n, m) % 11 == 0
print("Q3c OK")
# Q4a
Rr = lambda x, y: (x + y + 1) % 2 == 1
rg = range(-8, 9)
assert all(Rr(x, x) for x in rg) and all(Rr(y, x) for x in rg for y in rg if Rr(x, y))
assert all(Rr(x, z) for x in rg for y in rg for z in rg if Rr(x, y) and Rr(y, z))
assert Rr(2, 4) and Rr(4, 2)
print("Q4a OK")
# Q4b
isp = lambda n: n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
for n in range(2, 300):
    if isp(n):
        assert lcm(n - 1, n + 1) == (3 if n == 2 else (n * n - 1) // 2)
print("Q4b OK")
# Q4c brute force
for n in (6, 7):
    cnt = sum(1 for m in range(1 << (2 * n + 1))
              if sum(1 for i in range(2 * n + 1) if (m >> i) & 1 and (i + 1) % 2 == 1) == 1)
    assert cnt == (n + 1) * 2 ** n, (n, cnt)
print("Q4c OK")
