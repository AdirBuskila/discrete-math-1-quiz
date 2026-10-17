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


# =====================================================================================
# STEPS section: every numeric answer, choice key and findbug line used by gen_24A-A.py
# =====================================================================================
import itertools as _it
from math import gcd as _gcd, factorial as _fac
import sympy as sp
from sympy.logic.boolalg import Equivalent, And, Or, Not, simplify_logic
from sympy import symbols as _syms

EXPECT_NUM = {}
BUG_IDX = {}
_imp = lambda a, b: (not a) or b
_rows3 = list(_it.product([True, False], repeat=3))

# Q1a
_L = [_imp(p, q and r) for p, q, r in _rows3]
_R = [_imp(p, q) and _imp(p, r) for p, q, r in _rows3]
assert _L == _R and sum(_L) == 5
assert sum(1 for (p, q, r), v in zip(_rows3, _R) if p and v) == 1
assert _L[_rows3.index((True, True, False))] == _R[_rows3.index((True, True, False))] == False
assert not all(_L)   # the first formula is not a tautology
EXPECT_NUM["24A-A-Q1a"] = [5, 1]


# Q1b
def _P(X):
    X = list(X)
    return frozenset(frozenset(c) for r in range(len(X) + 1) for c in _it.combinations(X, r))


E = frozenset()
P1 = _P(E); P2 = _P(P1); P3 = _P(P2)
assert P1 == frozenset({E})
assert P2 == frozenset({E, frozenset({E})}) and P2 != P1 and P2 != E and P2 != frozenset({frozenset({E})})
assert P3 == frozenset({E, frozenset({E}), frozenset({frozenset({E})}), frozenset({E, frozenset({E})})}) and len(P3) == 4
_d1 = frozenset({frozenset({E}), frozenset({frozenset({E})}), frozenset({E, frozenset({E})})})
_d2 = frozenset({E, frozenset({E}), frozenset({E, frozenset({E})})})
_d3 = frozenset({E, frozenset({E}), frozenset({frozenset({E})})})
assert len({P3, _d1, _d2, _d3}) == 4
EXPECT_NUM["24A-A-Q1b"] = [4]

# Q1c
assert sp.real_root(-27, 3) == -3 and (-3) ** 3 == -27
assert 1 ** 6 == (-1) ** 6 and 1 != -1
assert len({x ** 3 for x in range(-200, 201)}) == 401   # injective on a sample
EXPECT_NUM["24A-A-Q1c"] = [-3]; BUG_IDX["24A-A-Q1c"] = 2


# Q2a
def _S(n):
    return sum(range(2 * n + 1, 4 * n, 2))


for n in range(1, 60):
    assert _S(n) == 3 * n * n
assert _S(4) == 48
_k = sp.symbols("k", positive=True)
assert sp.expand(3 * _k ** 2 + (4 * _k + 1) + (4 * _k + 3) - (2 * _k + 1) - 3 * (_k + 1) ** 2) == 0
assert sp.expand((4 * _k + 1) + (4 * _k + 3) - (2 * _k + 1)) == 6 * _k + 3
assert sp.expand(3 * _k ** 2 + 4 * _k + 3 - 3 * (_k + 1) ** 2) != 0
for k in range(1, 30):   # line 1 of the chain is a true identity
    assert sum(range(2 * k + 3, 4 * k + 4, 2)) == sum(range(2 * k + 1, 4 * k, 2)) + (4 * k + 1) + (4 * k + 3) - (2 * k + 1)
EXPECT_NUM["24A-A-Q2a"] = [48, 6]; BUG_IDX["24A-A-Q2a"] = 2

# Q2b
assert 40 % 25 == 15 and _gcd(25, 40) == 5
assert [25 * x + 40 * y for x, y in [(-3, 2), (2, -3), (3, -2), (-3, -2)]] == [5, -70, -5, -155]
EXPECT_NUM["24A-A-Q2b"] = [15, 5]

# Q2c
_P3 = [(a, b) for a in range(1, 4) for b in range(1, 4)]


def _refl(R): return all((a, a) in R for a in range(1, 4))
def _sym(R): return all((b, a) in R for a, b in R)
def _anti(R): return all(not ((b, a) in R and a != b) for a, b in R)
def _trans(R): return all((a, d) in R for a, b in R for c, d in R if b == c)
def _total(R): return _refl(R) and _anti(R) and _trans(R) and all((a, b) in R or (b, a) in R for a in range(1, 4) for b in range(1, 4))
def _equiv(R): return _refl(R) and _sym(R) and _trans(R)


_o = [{(1, 1), (2, 2), (3, 3)}, {(1, 1), (2, 2), (1, 2)}, {(1, 1), (2, 2), (3, 3), (1, 2)}, {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}]
assert [_equiv(R) for R in _o] == [True, False, False, False]
_t = [{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}, set(_P3), {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}, {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3)}]
assert [_total(R) for R in _t] == [True, False, False, False]
assert (not _anti(_t[1])) and (not _trans(_t[2])) and (not _total(_t[3])) and _trans(_t[3])
_all = [frozenset(u for u, bit in zip(_P3, bits) if bit) for bits in _it.product([0, 1], repeat=9)]
_tot = [R for R in _all if _total(R)]
assert len(_tot) == 6 and all(len(R) == 6 for R in _tot)
EXPECT_NUM["24A-A-Q2c"] = [6]

# Q3a
_Uall = frozenset(range(4))
_ss = [frozenset(c) for r in range(5) for c in _it.combinations(range(4), r)]
for A in _ss:
    for B in _ss:
        for C in _ss:
            assert A - (B & C) == (A - B) | (A - C)
assert any((A & ((_Uall - B) | (_Uall - C))) != (A & (_Uall - (B | C))) for A in _ss for B in _ss for C in _ss)
assert ({1} - ({1} & {2})) == (({1} - {1}) | ({1} - {2})) == {1}
assert not any(((A - B) | (A - C)) < (A - (B & C)) for A in _ss for B in _ss for C in _ss)    # never a strict subset
assert any((not A <= (B & C)) and A - (B & C) == (A - B) | (A - C) for A in _ss for B in _ss for C in _ss)
assert len({1, 2, 3} - ({2, 3} & {3, 4})) == 2
EXPECT_NUM["24A-A-Q3a"] = [2]; BUG_IDX["24A-A-Q3a"] = 2

# Q3b
_a, _b = sp.symbols("a b")
assert sp.expand((2 * _a + 1) * (2 * _b + 1) - (4 * _a * _b + 2 * _a + 2 * _b + 1)) == 0
assert sp.expand((2 * _a + 1) * (2 * _b + 1) - (2 * _a * _b + 2 * _a + 2 * _b + 1)) != 0
assert 2 * 1 * 2 + 1 + 2 == 7 and 3 * 5 == 2 * 7 + 1
for x, y in _it.product(range(-9, 10), repeat=2):
    assert ((x * y) % 2 == 0) == (x % 2 == 0 or y % 2 == 0)
_ps = [(x, y) for x in range(-5, 6) for y in range(-5, 6)]
assert any(x % 2 and y % 2 and (x * y) % 2 == 1 for x, y in _ps)                  # "odd, odd -> even" is false
assert any((x * y) % 2 == 0 for x, y in _ps) and all((x % 2 == 0 or y % 2 == 0) for x, y in _ps if (x * y) % 2 == 0)
assert any((x % 2 == 0 or y % 2 == 0) and (x * y) % 2 == 0 for x, y in _ps)      # "some even -> xy odd" is false
assert not any((x * y) % 2 == 1 and (x % 2 == 0 or y % 2 == 0) for x, y in _ps)  # "xy odd -> some even" never holds
EXPECT_NUM["24A-A-Q3b"] = [7]; BUG_IDX["24A-A-Q3b"] = 1

# Q3c
assert _fac(30) % 31 == 30 and pow(100, 150, 31) == 1
_c2 = [p for p in sp.primerange(2, 80) if (_fac(30) + 1) % p == 0 and (100 ** 150 - 1) % p == 0]
assert _c2 == [31]
for p in (37, 7, 29):
    assert not ((_fac(30) + 1) % p == 0 and (100 ** 150 - 1) % p == 0)
assert (100 ** 150 - 1) % 37 == 0 and (100 ** 150 - 1) % 7 == 0 and (_fac(30) + 1) % 37 != 0 and (_fac(30) + 1) % 7 != 0
assert (_fac(30) - 1) % 31 != 0 and _gcd(_fac(30) + 1, 100 ** 150 - 1) >= 31 > 30
EXPECT_NUM["24A-A-Q3c"] = [30, 1]; BUG_IDX["24A-A-Q3c"] = 0

# Q4a
_R4 = lambda x, y: (x + 3 * y) % 4 == 0
_Z = range(-12, 13)
assert all(_R4(x, x) for x in _Z) and all(_R4(y, x) for x in _Z for y in _Z if _R4(x, y))
assert all(_R4(x, z) for x in _Z for y in _Z for z in _Z if _R4(x, y) and _R4(y, z))
assert len({frozenset(y for y in _Z if _R4(x, y)) for x in _Z}) == 4
assert _R4(0, 4) and _R4(4, 0)
assert all((x + 3 * y) % 4 == (x - y) % 4 for x in _Z for y in _Z)
_x, _y, _z = sp.symbols("x y z")
assert sp.expand((_x + 3 * _y) + (_y + 3 * _z) - ((_x + 3 * _z) + 4 * _y)) == 0
assert sp.expand((_x + 3 * _y) + (_y + 3 * _z) - ((_x + 3 * _z) + 3 * _y)) != 0
EXPECT_NUM["24A-A-Q4a"] = [4]; BUG_IDX["24A-A-Q4a"] = 1

# Q4b
_p, _q, _r = _syms("p q r")
_phi = Equivalent(And(_p, _q), Or(Not(_q), _r))
_tr = [rw for rw in _rows3 if (rw[0] and rw[1]) == ((not rw[1]) or rw[2])]
assert _tr == [(True, True, True), (False, True, False)]
_dnf = Or(And(_p, _q, _r), And(Not(_p), _q, Not(_r)))
assert simplify_logic(Equivalent(_phi, _dnf)) == True
for bad in [And(And(_p, _q, _r), And(Not(_p), _q, Not(_r))), Or(And(_p, _q, Not(_r)), And(Not(_p), _q, _r)), And(_p, _q, _r)]:
    assert simplify_logic(Equivalent(_phi, bad)) != True
_t_ = And(Not(_p), _q, Not(_r))
assert _t_.subs({_p: False, _q: True, _r: False}) == True
assert And(_p, Not(_q), _r).subs({_p: False, _q: True, _r: False}) == False
assert And(_p, Not(_q), _r).subs({_p: True, _q: False, _r: True}) == True
assert And(Not(_p), Not(_q), Not(_r)).subs({_p: False, _q: True, _r: False}) == False
assert And(Not(_p), Not(_q), Not(_r)).subs({_p: False, _q: False, _r: False}) == True
EXPECT_NUM["24A-A-Q4b"] = [2]

# Q4c
assert sum(1 for p in sp.primerange(2, 51) if sp.isprime(p ** 3 - 1)) == 1 and 2 ** 3 - 1 == 7
assert 3 ** 3 - 1 == 26 and not sp.isprime(26) and sp.integer_nthroot(26, 2)[1] is False
assert all((p ** 3 - 1) % p == p - 1 for p in sp.primerange(2, 100))
assert (5 ** 3 - 1) % 3 != 0
assert all((p ** 3 - 1) % 2 == 0 and p ** 3 - 1 > 2 for p in sp.primerange(3, 200))
_qq = sp.symbols("qq")
assert sp.expand((2 * _qq + 1) ** 3 - 1 - 2 * (4 * _qq ** 3 + 6 * _qq ** 2 + 3 * _qq)) == 0
assert sp.expand((2 * _qq + 1) ** 3 - 1 - 2 * (4 * _qq ** 3 + 6 * _qq ** 2 + 3 * _qq + 1)) != 0
EXPECT_NUM["24A-A-Q4c"] = [1]; BUG_IDX["24A-A-Q4c"] = 2

# ---- cross-check against the generated raw JSON ----
import json as _json, pathlib as _pl
_raw = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / "24A-A.json").read_text(encoding="utf-8"))
_n = 0
for _q in _raw["questions"]:
    _qid = "24A-A-Q%d%s" % (_q["num"], "abcdefghij"["אבגדהוזחטי".index(_q["part"])])
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
