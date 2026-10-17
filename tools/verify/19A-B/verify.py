# Checks of the 19A-B key. ASCII output only.
import itertools
from math import comb, factorial
from sympy import totient, primerange
fs = frozenset
E = fs()
imp = lambda a, b: (not a) or b
T = [True, False]
# Q1a2
X = fs([fs([fs([fs([E])])]), fs([E, fs([fs([1])]), fs([E]), fs([fs([fs([1])]), E])]), fs([fs([E])])])
pp = fs([E, fs([1]), fs([2]), fs([1, 2])])
assert len(X) == 3 and len(pp) == 4 and len(X) * 2 == 6
# Q1a3: symmetric relations on {1,2}
pairs = [(a, b) for a in (1, 2) for b in (1, 2)]
cnt = 0
for k in range(5):
    for R in itertools.combinations(pairs, k):
        if all((b, a) in R for a, b in R):
            cnt += 1
assert cnt == 8
# Q1a5: onto functions {1,2,3}->{1,2,3}
assert sum(1 for f in itertools.product(range(3), repeat=3) if len(set(f)) == 3) == 6
print("Q1a OK")
# Q1b
S = lambda p, q, r: (p and q) == ((not q) or r)
rows = [x for x in itertools.product(T, repeat=3) if S(*x)]
assert set(rows) == {(True, True, True), (False, True, False)}
print("Q1b OK")
# Q2a
for n in range(1, 300):
    assert sum(range(n + 1, 2 * n + 1)) == n * (3 * n + 1) // 2
print("Q2a OK")
# Q2b (printed definitions: A=2^m 5^n 11^q, B=3^m 5^n 7^q)
rg = range(20)
A = {2 ** m * 5 ** n * 11 ** q for m in rg for n in rg for q in rg}
B = {3 ** m * 5 ** n * 7 ** q for m in rg for n in rg for q in rg}
assert A & B == {5 ** n for n in rg}
assert len(A | B) == 2 * 20 ** 3 - 20 == 15980
print("Q2b OK: |AuB| =", len(A | B))
# Q2c1, Q2c2
assert fs(itertools.product([], [1])) == fs(itertools.product([1], []))
sub = [fs(c) for k in range(4) for c in itertools.combinations(range(3), k)]
pr = lambda X, Y: fs(itertools.product(X, Y))
assert all(pr(a, b & c) == pr(a, b) & pr(a, c) for a in sub for b in sub for c in sub)
print("Q2c OK")
# Q3a: R on Q-{0}: x R y iff x*y>0
from fractions import Fraction as F
vals = [F(a, b) for a in range(-6, 7) if a for b in range(1, 5)]
assert all((x * y > 0) == (y * x > 0) for x in vals for y in vals)
assert all(not (x * y > 0 and y * z > 0) or x * z > 0 for x in vals for y in vals for z in vals)
assert all((x * 1 > 0) == (x > 0) and (x * -1 > 0) == (x < 0) for x in vals)
print("Q3a OK")
# Q3b: pairs of R containing a, |A|=12, |B|=5, |C|=3, |D|=4
def pairs_with_a(size):
    return 1 + 2 * (size - 1)
assert (pairs_with_a(3), pairs_with_a(5), pairs_with_a(4)) == (5, 9, 7)
n = 12
res = set()
import random
els = list(range(n)); random.seed(2)
for _ in range(50):
    random.shuffle(els)
    cls = [els[:5], els[5:8], els[8:]]
    R = {(x, y) for c in cls for x in c for y in c}
    for a in els:
        res.add(sum(1 for (x, y) in R if x == a or y == a))
assert res == {5, 9, 7}
print("Q3b OK")
# Q3c
for n in range(1, 40):
    assert sum(comb(n, k) * (9 ** k + 4 ** k) for k in range(n + 1)) == 10 ** n + 5 ** n
print("Q3c OK")
# Q4a
assert 10 ** 10 - factorial(10) == 10 ** 10 - 3628800
assert sum(1 for _ in itertools.combinations(range(20), 10)) == comb(20, 10)
# increasing functions {1..4}->{1..7} test
for k, m in ((3, 6), (4, 7), (5, 8)):
    assert sum(1 for f in itertools.product(range(m), repeat=k) if all(f[i] < f[i + 1] for i in range(k - 1))) == comb(m, k)
print("Q4a OK")
# Q4b
Om = [{1, 2}, {3}, {4, 5}]
R = {(x, y) for c in Om for x in c for y in c}
assert len(R) == 9 and (1, 2) in R and (2, 1) in R
print("Q4b OK")
# Q4c
for p in primerange(3, 60):
    for q in primerange(p + 1, 120):
        nn = (pow(int(totient(p)), int(totient(q))) - 1) * ((1 + int(totient(q))) ** int(totient(p)) - 1)
        assert nn % (p * q) == 0
print("Q4c OK")
# Q5
assert totient(1) == totient(2) == 1
assert all(totient(q) % 2 == 0 for q in range(3, 2000))
assert all(5 * 3 ** n + 2 * n * 3 ** n == 6 * (5 * 3 ** (n - 1) + 2 * (n - 1) * 3 ** (n - 1)) - 9 * (5 * 3 ** (n - 2) + 2 * (n - 2) * 3 ** (n - 2)) for n in range(2, 30))
assert 5 * 1 + 0 == 5 and 15 + 6 == 21
print("Q5 OK")
