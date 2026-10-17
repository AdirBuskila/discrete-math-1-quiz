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


# =====================================================================================
# STEPS section: every numeric answer, choice key and findbug line used by gen_23A-A.py
# =====================================================================================
import itertools as _it
from math import gcd as _gcd, factorial as _fac
from fractions import Fraction as _Fr
import sympy as sp
from sympy.logic.boolalg import Equivalent, And, Or, Not, simplify_logic
from sympy import symbols as _syms

EXPECT_NUM = {}
BUG_IDX = {}
_imp = lambda a, b: (not a) or b
_rows3 = list(_it.product([True, False], repeat=3))

# Q1a
_V = lambda p, q, r: _imp(p, q) and (not r)
_false_rows = [rw for rw in _rows3 if not _V(*rw)]
assert len(_false_rows) == 5 and sum(1 for rw in _rows3 if _V(*rw)) == 3
assert (True, False, True) in _false_rows
_p, _q, _r = _syms("p q r")
_cl = lambda c: Or(*[(Not(v) if val else v) for v, val in zip((_p, _q, _r), c)])
assert _cl((True, False, True)) == Or(Not(_p), _q, Not(_r))
_pt = {_p: True, _q: False, _r: True}
assert _cl((True, False, True)).subs(_pt) == False
assert Or(_p, Not(_q), _r).subs(_pt) == True and Or(Not(_p), _q, _r).subs(_pt) == True
_cnf = And(*[_cl(rw) for rw in _false_rows])
assert simplify_logic(Equivalent(_cnf, And(Or(Not(_p), _q), Not(_r)))) == True
assert len(_false_rows) == 5
EXPECT_NUM["23A-A-Q1a"] = [5, 5]

# Q1b
Rr = {(1, 2), (2, 3), (1, 3)}
inv = {(b, a) for a, b in Rr}
assert inv == {(2, 1), (3, 2), (3, 1)} and inv != Rr and inv != {(2, 1), (3, 2)} and inv != {(1, 2), (3, 2), (3, 1)}


def _trans(R): return all((a, d) in R for a, b in R for c, d in R if b == c)


# R^{-1} transitive for every transitive R on {1,2,3}
_P3 = [(a, b) for a in range(1, 4) for b in range(1, 4)]
_rel = [frozenset(u for u, bit in zip(_P3, bits) if bit) for bits in _it.product([0, 1], repeat=9)]
assert all(_trans({(b, a) for a, b in R}) for R in _rel if _trans(R))
# bug: (z,y),(y,x) in R and R transitive does not give (x,z) in R
_R0 = {(3, 2), (2, 1), (3, 1)}
assert _trans(_R0) and (3, 2) in _R0 and (2, 1) in _R0 and (1, 3) not in _R0 and (3, 1) in _R0
EXPECT_NUM["23A-A-Q1b"] = []; BUG_IDX["23A-A-Q1b"] = 2

# Q1c
_f = {(m, n): 2 ** m * 5 ** n for m in range(1, 25) for n in range(1, 25)}
assert min(_f.values()) == 10 and 3 not in _f.values() and len(set(_f.values())) == len(_f)
assert all(v % 2 == 0 for v in _f.values()) and any(v % 2 == 0 for v in _f.values())
assert all(sp.factorint(v).keys() <= {2, 5} for v in _f.values()) and sp.factorint(3) == {3: 1}
# m=y, n=x is wrong: f(1,2)=50 while (m,n)=(1,2) but y=2 != m
assert 2 ** 1 * 5 ** 2 == 50 and 1 != 2
EXPECT_NUM["23A-A-Q1c"] = [10]; BUG_IDX["23A-A-Q1c"] = 2

# Q2a
assert 10 ** 3 < 2 ** 10
assert all(k ** 3 < 2 ** k for k in range(10, 200)) and not all(k ** 3 < 2 ** k for k in range(1, 12))
assert not (9 ** 3 < 2 ** 9)
assert 11 ** 3 == 1331 and 2 * 10 ** 3 == 2000
_k = sp.symbols("k")
assert sp.expand((_k + 1) ** 3 - (_k ** 3 + 3 * _k ** 2 + 3 * _k + 1)) == 0
assert sp.expand(_k ** 3 + _k * _k ** 2 - 2 * _k ** 3) == 0 and sp.expand(_k ** 3 + _k * _k ** 2 - 3 * _k ** 3) != 0
assert all(3 * k ** 2 + 3 * k + 1 < 9 * k ** 2 and 9 * k ** 2 < k ** 3 for k in range(10, 500))
EXPECT_NUM["23A-A-Q2a"] = [1331]; BUG_IDX["23A-A-Q2a"] = 2

# Q2b
assert 65 % 40 == 25 and _gcd(65, -40) == 5
assert [65 * x + (-40) * y for x, y in [(-3, -5), (-3, 5), (3, 5), (2, 3)]] == [5, -395, -5, 10]
EXPECT_NUM["23A-A-Q2b"] = [25, 5]

# Q2c
_A = {1, 2, 3, 4, 5, 6}; _B = {1}; _C = {2, 3, 4}; _D = _A - (_B | _C)
assert _D == {5, 6} and len(_D) == 2
_Rr = {(a, b) for blk in (_B, _C, _D) for a in blk for b in blk}
assert len(_Rr) == 14 == 1 + 9 + 4
# partition conditions: each alone is insufficient
assert {1, 2, 3} | {3, 4} == {1, 2, 3, 4} and ({1, 2, 3} & {3, 4})            # covers but not disjoint
assert ({1} & {2}) == set() and ({1} | {2}) != {1, 2, 3}                       # disjoint but does not cover
assert {1} <= {1, 2, 3} and {1, 2} <= {1, 2, 3} and ({1} | {1, 2}) != {1, 2, 3}  # inside A only
EXPECT_NUM["23A-A-Q2c"] = [2, 14]

# Q3a
def _sub(n): return [frozenset(c) for r in range(n + 1) for c in _it.combinations(range(n), r)]


for A in _sub(3):
    for B in _sub(3):
        for C in _sub(3):
            assert ((B - A) | (C - A)) <= ((B | C) - A)
seq = [1 + _Fr(1, n) for n in range(2, 4000)]
assert len(set(seq)) == len(seq) and all(1 < v < 2 for v in seq)      # infinite family of rationals in (1,2)
assert not (1 + _Fr(1, 1) < 2)                                           # 1+1/1 = 2 is not in (1,2)
EXPECT_NUM["23A-A-Q3a"] = []; BUG_IDX["23A-A-Q3a"] = 0

# Q3b
_Aa = {2 ** m * 9 ** n for m in range(10) for n in range(10)}
_Bb = {5 ** m * 9 ** n for m in range(10) for n in range(10)}
assert len(_Aa) == len(_Bb) == 100 and _Aa & _Bb == {9 ** n for n in range(10)} and len(_Aa & _Bb) == 10
assert len(_Aa) * len(_Bb) == 10000
_good = 2 ** 10 + 2 ** 10000
assert _good != 2 ** 10 * 2 ** 10000 and _good != 2 ** 10 + 2 ** 200 and _good != 10 + 10000
EXPECT_NUM["23A-A-Q3b"] = [10, 10000]

# Q3c
assert pow(5, 20, 11) == 1 and _fac(10) % 11 == 10 and _fac(12) % 11 == 0
assert (5 ** 20 + _fac(10) + _fac(12)) % 11 == 0 and (2 ** 120 - 1) % 11 == 0 and (2 ** 12) % 11 != 0
assert (25 ** 10 - 1) + (_fac(10) + 1) + _fac(12) == 5 ** 20 + _fac(10) + _fac(12)
assert (_fac(10) - 1) % 11 != 0
assert _gcd(2 ** 120 - 1, 5 ** 20 + _fac(10) + _fac(12)) % 11 == 0
EXPECT_NUM["23A-A-Q3c"] = [1, 10, 0]; BUG_IDX["23A-A-Q3c"] = 2

# Q4a
_Ro = lambda x, y: (x + y + 1) % 2 == 1
_Z = range(-12, 13)
assert all(_Ro(x, x) for x in _Z) and all(_Ro(y, x) for x in _Z for y in _Z if _Ro(x, y))
assert all(_Ro(x, z) for x in _Z for y in _Z for z in _Z if _Ro(x, y) and _Ro(y, z))
assert len({frozenset(y for y in _Z if _Ro(x, y)) for x in _Z}) == 2
assert _Ro(2, 4) and _Ro(4, 2)
_x, _y, _z = sp.symbols("x y z")
assert sp.expand((_x + _y + 1) + (_y + _z + 1) - ((_x + _z + 1) + (2 * _y + 1))) == 0
assert all((2 * y + 1) % 2 == 1 for y in range(-50, 50))
EXPECT_NUM["23A-A-Q4a"] = [2]; BUG_IDX["23A-A-Q4a"] = 2

# Q4b
assert sp.ilcm(1, 3) == 3 and sp.ilcm(4, 6) == 12 == (5 * 5 - 1) // 2
for p in sp.primerange(3, 400):
    assert _gcd(p - 1, p + 1) == 2 and sp.ilcm(p - 1, p + 1) == (p * p - 1) // 2
assert _gcd(2 - 1, 2 + 1) == 1
EXPECT_NUM["23A-A-Q4b"] = [3, 12]

# Q4c
def _count(n):
    A = list(range(1, 2 * n + 2)); odds = set(range(1, 2 * n + 2, 2))
    return sum(1 for bits in _it.product([0, 1], repeat=len(A)) if sum(1 for a, b in zip(A, bits) if b and a in odds) == 1)


assert _count(6) == 7 * 2 ** 6 == 448 and _count(7) == 8 * 2 ** 7 == 1024
assert len(range(1, 14, 2)) == 7 and len(range(2, 13, 2)) == 6
for n in (6, 7):
    assert (n + 1) * 2 ** n not in (2 ** (2 * n + 1), (n + 1) + 2 ** n, n * 2 ** (n + 1))
EXPECT_NUM["23A-A-Q4c"] = [7, 64]

# ---- cross-check against the generated raw JSON ----
import json as _json, pathlib as _pl
_raw = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / "23A-A.json").read_text(encoding="utf-8"))
_n = 0
for _q in _raw["questions"]:
    _qid = "23A-A-Q%d%s" % (_q["num"], "abcdefghij"["אבגדהוזחטי".index(_q["part"])])
    _st = _q.get("steps", [])
    assert _st, _qid + " has no steps"
    assert 2 <= len(_st) <= 5, (_qid, len(_st))
    assert _q["stepsSource"] == "ai-draft" and _q["rubricSource"] == "ai-draft"
    assert sum(r["points"] for r in _q["rubric"]) == _q["points"], _qid
    _nums = [s["answer"] for s in _st if s["type"] == "numeric"]
    assert _nums == EXPECT_NUM.get(_qid, []), (_qid, _nums, EXPECT_NUM.get(_qid))
    _bugs = [s["bugIndex"] for s in _st if s["type"] == "findbug"]
    assert _bugs == ([BUG_IDX[_qid]] if _qid in BUG_IDX else []), (_qid, _bugs)
    for s in _st:
        if s["type"] == "choice":
            assert s["correctId"] in [o["id"] for o in s["options"]]
            _v = [o["value"] for o in s["options"]]
            assert len(set(_v)) == len(_v), (_qid, "duplicate option")
    _n += 1
print("STEPS: numeric answers and findbug indices verified against raw JSON for", _n, "items")
print("ALL STEPS OK")
