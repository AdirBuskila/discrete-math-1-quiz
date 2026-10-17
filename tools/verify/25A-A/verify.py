# Checks of the official 25A-A answers. ASCII output only.
import itertools
from math import gcd, factorial
from fractions import Fraction

T = [True, False]
imp = lambda a, b: (not a) or b
rows = list(itertools.product(T, repeat=3))
# Q1a: not p -> not(q or r)  ==  (q->p) and (r->p)
for p, q, r in rows:
    assert imp(not p, not (q or r)) == (imp(q, p) and imp(r, p))
print("Q1a equivalence OK; last column", [imp(not p, not (q or r)) for p, q, r in rows])
# Q1b
assert (71 ** 120 - 1) % 26 == 0 and (50 ** 24 + factorial(12)) % 26 == 0
print("Q1b OK")
# Q1c
dom = [1, 4, 5, 6, 9, 18]
f = {k: 3 * k // gcd(3, k) for k in dom}
assert sorted(f.values()) == [3, 6, 9, 12, 15, 18] and len(set(f.values())) == 6
print("Q1c", f)
# Q2a
for n in range(1, 40):
    assert sum(Fraction(1, (4 * i - 3) * (4 * i + 1)) for i in range(1, n + 1)) == Fraction(n, 4 * n + 1)
print("Q2a OK")
# Q2b: 5^b = 3^a has no solution with a,b >= 1
assert not any(5 ** b == 3 ** a for a in range(1, 60) for b in range(1, 60))
print("Q2b OK (no small solutions)")
# Q2c(1)
R = {(1, 2), (2, 1), (2, 3)}
refl = all((x, x) in R for x in (1, 2, 3))
sym = all((b, a) in R for a, b in R)
anti = all(not ((b, a) in R and a != b) for a, b in R)
tr = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
assert not refl and not sym and not anti and not tr(R) and len(R) <= 5
print("Q2c1 OK")
# Q2c(2): counterexample
R1 = {(1, 1), (1, 2)}
R2 = {(1, 1), (1, 3)}
assert tr(R1) and tr(R2) and tr(R1 | R2) and R1 != R2 and (R1 & R2)
print("Q2c2 OK")
# Q3a: 3x+7y = 0 mod 5
Rr = lambda x, y: (3 * x + 7 * y) % 5 == 0
rg = range(-10, 11)
assert all(Rr(x, x) for x in rg)
assert all(Rr(y, x) for x in rg for y in rg if Rr(x, y))
assert all(Rr(x, z) for x in rg for y in rg for z in rg if Rr(x, y) and Rr(y, z))
assert Rr(0, 5) and Rr(5, 0)
print("Q3a: reflexive, symmetric, transitive, not antisymmetric OK (official solution omits part 2)")


# Q3b
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = egcd(b, a % b)
    return d, y, x - y * (a // b)


print("Q3b", egcd(184, 48), egcd(184, -48))
assert -184 + 48 * 4 == 8 and (-48) * (-4) + 184 * (-1) == 8 and gcd(48, 184) == 8
# Q4b
isp = lambda n: n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
assert [a for a in range(0, 200) if isp(a * a + a + 2)] == [0]
print("Q4b OK")
# Q4c(2)
vals = {}
for m in range(30):
    for n in range(30):
        assert 3 ** m * 5 ** n not in vals
        vals[3 ** m * 5 ** n] = 1
assert 7 not in vals
print("Q4c OK")
