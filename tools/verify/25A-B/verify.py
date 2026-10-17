# Checks of the official 25A-B answers. ASCII output only.
import itertools
from math import gcd, factorial

imp = lambda a, b: (not a) or b
T = [True, False]
rows = list(itertools.product(T, repeat=3))
# Q1a CNF
S = lambda p, q, r: imp(p or (not q), r)
cnf = lambda p, q, r: ((not p) or (not q) or r) and ((not p) or q or r) and (p or q or r)
assert all(S(*x) == cnf(*x) for x in rows)
assert [x for x in rows if not S(*x)] == [(True, True, False), (True, False, False), (False, False, False)]
print("Q1a OK")
# Q1b
n = sum(1 for m in range(1 << 10) if m & 3 == 3)
assert n == 256
print("Q1b", n)
# Q1c
assert {gcd(12, x) for x in range(1, 500)} == {1, 2, 3, 4, 6, 12}
print("Q1c OK")
# Q2a
assert all((23 ** n - 1) % 11 == 0 for n in range(1, 100))
print("Q2a OK")
# Q2b
A = {5 ** n * 7 ** m for m in range(10) for n in range(10)}
B = {5 ** n for n in range(10)}
C = {7 ** n for n in range(10)}
assert len(A) == 100 and len(B | C) == 19
print("Q2b 2^119 OK")
# Q2c on P({1..4})
subs = [frozenset(c) for k in range(5) for c in itertools.combinations([1, 2, 3, 4], k)]
Rr = lambda b, c: (1 in b) == (1 in c)
assert all(Rr(b, b) for b in subs)
assert all(Rr(c, b) for b in subs for c in subs if Rr(b, c))
assert all(Rr(b, d) for b in subs for c in subs for d in subs if Rr(b, c) and Rr(c, d))
assert len({frozenset(c for c in subs if Rr(b, c)) for b in subs}) == 2
print("Q2c OK")
# Q3a
A = [1, 2, 3, 6, 8, 9, 16, 18]
R = {(x, y) for x in A for y in A if y % x == 0}
assert all((x, x) in R for x in A)
assert all(not ((y, x) in R and x != y) for x, y in R)
assert all((x, z) in R for x, y in R for y2, z in R if y == y2)
assert (2, 3) not in R and (3, 2) not in R
print("Q3a OK")
# Q3b
assert -84 + 2 * 48 == 12 == gcd(48, 84)
print("Q3b OK")
# Q4b
g = gcd(5 ** 44 - 1, 8 ** 88 + factorial(22))
assert g > 19 and g % 23 == 0
print("Q4b OK")
