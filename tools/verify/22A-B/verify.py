# Checks of the 22A-B keys (forms 1 and 2). ASCII output only.
import itertools
from math import gcd, factorial
imp = lambda a, b: (not a) or b
T = [0, 1]
for p, q, r in itertools.product(T, repeat=3):
    assert imp(p and q, r) == imp(p, (not q) or r)           # form 1 Q1a
    assert (imp(p, r) and imp(q, r)) == imp(p or q, r)        # form 2 Q1a
print("Q1a both forms OK")
assert 84 * (-4) + 68 * 5 == 4 == gcd(84, 68)
assert (-68) * (-5) + (-84) * 4 == 4 and (-84) * 4 + (-68) * (-5) == 4
assert 68 * 5 + 84 * (-4) == 4
print("Q1b OK: gcd=4, x1=5,y1=-4 (form1); x2=-5,y2=4")
lcm = lambda a, b: a * b // gcd(a, b)
for a in range(3, 60):
    for b in range(2, a):
        assert gcd(lcm(a, b), gcd(a, b)) == gcd(a, b)
print("Q1b2 OK")
for a, b in ((25**20 + factorial(40), 8**80 + 40), (36**20 + factorial(40), 10**80 + 40)):
    assert a % 41 == 0 and b % 41 == 0 and gcd(a, b) > 40
assert 8**80 == 64**40 and 25**20 == 5**40 and 36**20 == 6**40 and 10**80 == 100**40
print("Q1c OK both forms")
for n in range(1, 300):
    assert n * n <= 5**n and n * n <= 4**n
print("Q2a OK")
A = {3**n * 5**m for n in range(11) for m in range(11)}
B1 = {5**m for m in range(1, 11)}
B2 = {3**n for n in range(1, 11)}
assert len(A) == 121 and B1 <= A and B2 <= A and len(B1) == 10 and len(B2) == 10
assert len(A - B1) == 111 and len(A | B1) == 121 and len(A - B2) == 111
print("Q2b form1: 2^121 + 2^1210 + 111 ; form2 correct value: 121 + 2^1210 + 2^111 (key prints 232+2^1210)")
U = range(3)
subs = [frozenset(s) for k in range(4) for s in itertools.combinations(U, k)]
for a, b, c in itertools.product(subs, repeat=3):
    assert imp(a <= (b | c), (a - b) <= c)
    assert imp(not ((a - b) <= c), not (a <= (b | c)))
print("Q2c OK")
for c in (9, 3 + 6 - 6 + 0):
    pass
R = lambda x, y: (9 * x + 5 * y) % 2 == 0
rng = range(-12, 13)
assert all(R(x, x) for x in rng)
assert all(R(y, x) for x in rng for y in rng if R(x, y))
assert all(R(x, z) for x in rng for y in rng for z in rng if R(x, y) and R(y, z))
assert all(R(x, 0) == (x % 2 == 0) and R(x, 1) == (x % 2 == 1) for x in rng)
assert R(0, 2) and R(2, 0)   # not antisymmetric -> not a partial order
print("Q3a form1 OK (equivalence, 2 classes, NOT a partial order)")
f = lambda k: (k * k) % 6 + lcm(2, gcd(2, k))
tab = {k: f(k) for k in range(1, 8)}
assert tab == {1: 3, 2: 6, 3: 5, 4: 6, 5: 3, 6: 2, 7: 3}, tab
Aset = [1, 2, 3, 6]
assert sorted(tab[k] for k in Aset) == [2, 3, 5, 6]
print("Q3b OK; note key summary line says f(5)=6 but f(5)=3")
# Q3c: reflexive + symmetric + antisymmetric on {1..5} is the identity
cnt = 0
pairs = [(a, b) for a in range(1, 4) for b in range(1, 4)]
for mask in range(1 << len(pairs)):
    Rr = {pairs[i] for i in range(len(pairs)) if mask >> i & 1}
    if all((x, x) in Rr for x in range(1, 4)) and all((y, x) in Rr for (x, y) in Rr) and \
       all(not ((x, y) in Rr and (y, x) in Rr and x != y) for (x, y) in Rr):
        assert Rr == {(x, x) for x in range(1, 4)}
        cnt += 1
assert cnt == 1
print("Q3c OK")
for n in range(4, 7):
    full = set(range(1, 2 * n + 2))
    odds = {x for x in full if x % 2}; evens = full - odds
    c1 = c2 = 0
    for mask in range(1 << (2 * n + 1)):
        Bs = {i + 1 for i in range(2 * n + 1) if mask >> i & 1}
        c1 += (Bs | odds) == full
        c2 += (Bs | evens) == full
    assert c1 == 2**(n + 1) and c2 == 2**n
print("Q4b OK: form1 2^(n+1), form2 2^n")
