# Checks of the 19S-A key. ASCII output only.
import itertools
from fractions import Fraction as Fr
from math import comb, factorial, gcd
from sympy import totient
from sympy.functions.combinatorial.numbers import stirling
fs = frozenset
T = [True, False]
# Q1a2/a3/a4/a5
A = fs([1, 2, 3])
assert A ^ A == fs() and A ^ fs() == A
D = [(1, 1), (2, 2), (3, 3)]
R1, R2 = fs(D + [(1, 2)]), fs(D + [(2, 1)])
tr = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
sym = lambda R: all((b, a) in R for a, b in R)
anti = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
assert tr(R1) and tr(R2) and all((x, x) in R1 and (x, x) in R2 for x in (1, 2, 3))
X = R1 ^ R2
assert X == fs([(1, 2), (2, 1)]) and sym(X) and not anti(X)
P = fs([(1, 1), (2, 2)])
assert tr(P) and anti(P) and all((x, x) in P for x in (1, 2)) and not ((1, 2) in P or (2, 1) in P)
cnt = sum(1 for f in itertools.product(range(1, 6), repeat=5)
          if len(set(f)) == 5 and set(f[:2]) == {1, 2})
assert cnt == 12
print("Q1a OK")
# Q1b
S = lambda p, q, r: (p and q) == ((not q) or r)
rows = [x for x in itertools.product(T, repeat=3) if S(*x)]
assert set(rows) == {(True, True, True), (False, True, False)}
print("Q1b OK")
# Q2a
for n in range(1, 200):
    assert sum(Fr(1, (4 * k - 3) * (4 * k + 1)) for k in range(1, n + 1)) == Fr(n, 4 * n + 1)
print("Q2a OK")
# Q2b
rg = range(10)
Aset = {2 ** n * 3 ** m for m in rg for n in rg}
Bs = {2 ** n for n in rg}
Cs = {3 ** n for n in rg}
assert len(Aset) == 100 and len(Bs) == len(Cs) == 10
BxC = {(b, c) for b in Bs for c in Cs}
BuC = Bs | Cs
assert len({e for e in BxC if e not in BuC}) == 100
assert len(Bs ^ Cs) == 18
assert len(Bs & Cs) == 1
print("Q2b OK (|P(AxB) x C| = 10 * 2^1000 by formula)")
# Q2c
for n in range(0, 30):
    assert sum(comb(n, k) * 4 ** k for k in range(n + 1)) == 5 ** n
assert all((Fr(5, 4) ** n) > 10 ** 6 for n in (80,))
print("Q2c OK")
# Q3a
xs = [x for x in range(-6, 7) if x]
assert all((x * y > 0) == (y * x > 0) for x in xs for y in xs)
assert all(not (x * y > 0 and y * z > 0) or x * z > 0 for x in xs for y in xs for z in xs)
print("Q3a OK")
# Q3b: contrapositive witness
for Aa, Bb in (({1, 2}, {2, 3}), ({1, 2, 3}, {3, 4})):
    assert not Aa <= Bb and not Bb <= Aa
    a = min(Aa - Bb); b = min(Bb - Aa)
    sub = lambda U: {fs(c) for k in range(len(U) + 1) for c in itertools.combinations(sorted(U), k)}
    assert fs([a, b]) in sub(Aa | Bb) and fs([a, b]) not in sub(Aa) | sub(Bb)
print("Q3b OK")
# Q3c
for n in range(10, 15):
    els = range(1, n + 1)
    c = sum(1 for k in range(n + 1) for B in itertools.combinations(els, k)
            if not ({1, 2, 3, 4} & set(B)) and 7 in B) if n <= 13 else None
    if c is not None:
        assert c == 2 ** (n - 5)
m = comb(8, 4); assert m == 70 and int(totient(m * m)) == 1680
print("Q3c OK")
# Q4
assert 6 ** 4 == 1296
assert sum(1 for f in itertools.product(range(1, 7), repeat=4) if f[0] > f[1] > f[2] > f[3]) == 15
assert sum(1 for f in itertools.product(range(1, 7), repeat=4) if len(set(f)) == 4 and set(f[:2]) == {1, 2}) == 24
assert stirling(5, 3) == 25
parts = set()
pr = [3, 5, 7, 11, 13]
def rec(i, bl):
    if i == 5:
        if len(bl) == 3:
            parts.add(fs(fs(b) for b in bl))
        return
    for j in range(len(bl)):
        bl[j].append(pr[i]); rec(i + 1, bl); bl[j].pop()
    bl.append([pr[i]]); rec(i + 1, bl); bl.pop()
rec(0, [])
assert len(parts) == 25
evens = sum(1 for w in itertools.permutations(range(1, 7), 4) if w[-1] % 2 == 0)
assert evens == 180
assert sum(1 for w in itertools.permutations(range(1, 7)) if any(set(w[i:i + 3]) == {1, 2, 3} for i in range(4))) == 144
print("Q4 OK")
# Q5
for n in range(6, 600, 3):
    assert totient(3 * n) == 3 * totient(n)
fib = lambda n: (((1 + 5 ** .5) / 2) ** n - ((1 - 5 ** .5) / 2) ** n) / 5 ** .5
a, b = 0, 1
for n in range(0, 40):
    assert abs(a - fib(n)) < 1e-3 * max(1, a)
    a, b = b, a + b
print("Q5 OK")
