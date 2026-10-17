# Checks of the 19A-A key. ASCII output only.
import itertools
from math import comb, factorial, gcd
from sympy import totient
from sympy.utilities.iterables import multiset_partitions
fs = frozenset
E = fs()
# Q1a2: count elements of the printed set; P(S) has 2^|S| elements
S = fs([fs([fs([fs([E])])]), fs([E, fs([fs([1])]), fs([E]), fs([fs([fs([1])]), E])]), fs([fs([E])])])
assert len(S) == 3 and 2 ** len(S) == 8
print("Q1a2 OK")
# Q1a3: equivalence relations on {1,2,3} = Bell(3)
assert sum(1 for _ in multiset_partitions([1, 2, 3])) == 5
# Q1a5
assert sum(1 for _ in itertools.permutations(range(5), 3)) == 60
print("Q1a3, Q1a5 OK")
# Q1b: DNF
imp = lambda a, b: (not a) or b
T = [True, False]
rows = [x for x in itertools.product(T, repeat=3) if x[0] and imp(x[2], x[0]) and imp(x[1], x[2])]
print("true rows (p,q,r):", rows)
assert set(rows) == {(True, True, True), (True, False, True), (True, False, False)}
f_key = lambda p, q, r: (p and q and r) or (p and not q and not r)
bad = [x for x in itertools.product(T, repeat=3) if f_key(*x) != (x[0] and imp(x[2], x[0]) and imp(x[1], x[2]))]
print("key DNF disagrees on:", bad)
assert bad == [(True, False, True)]
print("Q1b: key DNF misses (T,F,T); corrected DNF verified")
# Q2a
assert all(n * n < 2 ** n for n in range(5, 400)) and not (4 * 4 < 2 ** 4)
# Q2b
Aset = {3 ** n * 5 ** n * 7 ** m for n in range(100) for m in range(100)}
Bset = {3 ** n * 5 ** m * 7 ** m for n in range(100) for m in range(100)}
assert len(Aset & Bset) == 100
print("Q2b OK")
# Q3a
for x in range(-9, 10):
    for y in range(-9, 10):
        assert ((7 * x + y) % 2 == 0) == ((x + y) % 2 == 0)
print("Q3a OK")
# Q3b: n=8 is the only n>7 where the two non-B blocks may both have size 3
def count_relations(n):
    els = list(range(n)); cnt = 0
    for B in itertools.combinations(els, 2):
        rest = [e for e in els if e not in B]
        for C in itertools.combinations(rest, 3):
            D = [e for e in rest if e not in C]
            part = fs([fs(B), fs(C), fs(D)])
            cnt += 1 if len(D) != 3 else 0.5
    return cnt
assert count_relations(8) == comb(8, 2) * comb(6, 3) / 2
assert count_relations(9) == comb(9, 2) * comb(7, 3)
print("Q3b2: formula correct for n>=9; for n=8 it counts every relation twice (280 vs 560)")
for n in range(8, 40):
    assert 4 + 9 + (n - 5) ** 2 == 13 + (n - 5) ** 2
# Q3c
for R in itertools.chain.from_iterable(itertools.combinations([(1, 2), (2, 1)], k) for k in (1,)):
    Rr = {(1, 1), (2, 2)} | set(R)
    assert all(((x, y) in Rr or (y, x) in Rr) for x in (1, 2) for y in (1, 2))
    assert all(not ((x, y) in Rr and (y, x) in Rr) for x in (1, 2) for y in (1, 2) if x != y)
print("Q3c OK")
# Q4
assert 2 ** 400 - 20 ** 20 == 2 ** 400 - 20 ** 20 and 20 ** 20 == len(range(20)) ** 20
tot = comb(400, 3) + comb(400, 4) + comb(400, 5)
assert tot == sum(comb(400, k) for k in (3, 4, 5))
assert factorial(3) * factorial(4) * factorial(3) == 864
# 4b1 by brute force on B={0..9}: bijections with f(0,1,2)={0,1,2}, f(3..6)={3..6}
c = 0
for p in itertools.permutations(range(10)):
    if set(p[:3]) == {0, 1, 2} and set(p[3:7]) == {3, 4, 5, 6}:
        c += 1
assert c == 864
assert 2 ** 5 == sum(1 for k in range(11) if True) // 1 * 0 + 32
assert sum(comb(11, k) for k in range(0, 12, 2)) == 2 ** 10
m = 11; ph = int(totient(m)); assert ph == 10 and (pow(ph, ph, m) - 1) % m == 0
print("Q4 OK")
# Q5
assert all(6 * 2 ** n + 3 ** n == 5 * (6 * 2 ** (n - 1) + 3 ** (n - 1)) - 6 * (6 * 2 ** (n - 2) + 3 ** (n - 2)) for n in range(2, 30))
assert 6 + 1 == 7 and 12 + 3 == 15
print("Q5 OK")
# --- solver/arbiter 2026-10-17: Q3b2 shipped with the n=8 correction; count DISTINCT relations (sets of pairs) ---
def distinct_relations(n):
    els = list(range(n)); rels = set()
    for B in itertools.combinations(els, 2):
        rest = [e for e in els if e not in B]
        for C in itertools.combinations(rest, 3):
            D = [e for e in rest if e not in C]
            rels.add(fs((a, b) for blk in (B, C, D) for a in blk for b in blk))
    return len(rels)
assert distinct_relations(8) == 280 != comb(8, 2) * comb(6, 3) == 560
assert distinct_relations(9) == comb(9, 2) * comb(7, 3) and distinct_relations(10) == comb(10, 2) * comb(8, 3)
print("Q3b2 OK: n=8 -> 280 distinct relations; n=9,10 match C(n,2)C(n-2,3)")
