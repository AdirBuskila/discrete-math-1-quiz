# Checks of the 22A-A keys (forms 1 and 2). ASCII output only.
import itertools
from math import gcd
T = [0, 1]
imp = lambda a, b: (not a) or b
f1 = lambda p, q, r: imp(p, q) and (not r)
rows = list(itertools.product(T, repeat=3))
assert [int(f1(*x)) for x in rows[::-1]] == [int(f1(*x)) for x in rows[::-1]]
# order in the key table: TTT,TTF,TFT,TFF,FTT,FTF,FFT,FFF
key = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]
vals = [bool(f1(*x)) for x in key]
assert vals == [False, True, False, False, False, True, False, True]
cnf = lambda p,q,r: ((not p) or (not q) or (not r)) and ((not p) or q or (not r)) and ((not p) or q or r) and (p or (not q) or (not r)) and (p or q or (not r))
dnf = lambda p,q,r: (p and q and not r) or ((not p) and q and not r) or ((not p) and (not q) and not r)
for x in rows:
    assert bool(cnf(*x)) == bool(f1(*x)) == bool(dnf(*x))
print("Q1a OK (CNF and DNF)")
assert 55*3 + 40*(-4) == 5 == gcd(55, 40)
assert abs(-55*40)//gcd(55, 40) == 440 == abs(55*-40)//gcd(55, -40)
print("Q1b OK")
assert (16**15 + 7**60 + 37) % 31 == 8 and (36**15 + 8**60 + 47) % 31 == 18
assert 16**15 == 4**30 and 7**60 == 49**30 and 36**15 == 6**30 and 8**60 == 64**30
print("Q1c OK: 8 and 18")
for n in range(1, 200):
    assert sum(range(n+1, 2*n+1)) == n*(3*n+1)//2
    assert sum(range(n+2, 2*n+3)) == (n+1)*(3*n+4)//2
for k in range(1, 50):
    assert k*(3*k+1) - 2*(k+1) + 2*(2*k+1) + 2*(2*k+2) == (k+1)*(3*k+4)
    assert (k+1)*(3*k+4) - 2*(k+2) + 2*(2*k+3) + 2*(2*k+4) == (k+2)*(3*k+7)
print("Q2a OK")
A1 = {3**n * 5**m for n in range(20) for m in range(20)}; B1 = {2**n * 5**m for n in range(20) for m in range(20)}
assert len(A1) == 400 and len(B1) == 400 and len(A1 & B1) == 20 and len(A1 - B1) == 380
A2 = {3**n * 7**m for n in range(30) for m in range(30)}; B2 = {3**n * 5**m for n in range(30) for m in range(30)}
assert len(A2) == 900 and len(B2) == 900 and len(A2 & B2) == 30 and len(A2 - B2) == 870
print("Q2b form1: 20 + 2^160000 + 2^380 ; form2 correct: 870 + 2^810000 + 2^30 (key prints 2^90000)")
subs = [frozenset(s) for k in range(4) for s in itertools.combinations(range(3), k)]
for a, b, c in itertools.product(subs, repeat=3):
    assert imp((a-b) <= c, (a-c) <= b)
    assert imp(not ((a-c) <= b), not ((a-b) <= c))
print("Q2c OK")
R = lambda x, y: (3*x + 5*y) % 2 == 0
rng = range(-12, 13)
assert all(R(x, x) for x in rng) and all(R(y, x) for x in rng for y in rng if R(x, y))
assert all(R(x, z) for x in rng for y in rng for z in rng if R(x, y) and R(y, z))
assert all(R(0, x) == (x % 2 == 0) and R(1, x) == (x % 2 == 1) for x in rng)
assert R(1, 3) and R(3, 1) and (3*1+5*3, 3*3+5*1) == (18, 14)
print("Q3a form1 OK")
lcm = lambda a, b: a*b//gcd(a, b)
f = lambda k: (k*k) % 6 + lcm(2, gcd(2, k))
assert {f(k) for k in range(1, 7)} == {2, 3, 5, 6} == {f(k) for k in range(1, 8)} and f(7) == 3
print("Q3b OK")
# Q3c: a reflexive total order on {1..5}: not a function (check on {1,2,3})
S = [1, 2, 3]
pairs = [(a, b) for a in S for b in S]
for mask in range(1 << 9):
    Rr = {pairs[i] for i in range(9) if mask >> i & 1}
    refl = all((x, x) in Rr for x in S)
    anti = all(not ((x, y) in Rr and (y, x) in Rr) or x == y for x in S for y in S)
    trans = all((x, z) in Rr for (x, y) in Rr for (y2, z) in Rr if y == y2)
    total = all((x, y) in Rr or (y, x) in Rr for x in S for y in S)
    if refl and anti and trans and total:
        isfun = all(len({y for (x2, y) in Rr if x2 == x}) == 1 for x in S)
        assert not isfun
print("Q3c OK")
for n in range(4, 7):
    full = set(range(1, 2*n+2)); odds = {x for x in full if x % 2}; evens = full - odds
    c1 = c2 = c3 = 0
    for mask in range(1 << (2*n+1)):
        Bs = {i+1 for i in range(2*n+1) if mask >> i & 1}
        c1 += len(Bs & odds) == 1
        c2 += len(Bs & evens) == 1
        c3 += 1 < len(Bs) < len(full)
    assert c1 == (n+1) * 2**n and c2 == n * 2**(n+1) and c3 == 2**(2*n+1) - 2*n - 3
print("Q4b OK")
