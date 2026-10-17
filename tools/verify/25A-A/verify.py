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
# --- solver/arbiter 2026-10-17: Q3a(2) shipped ---
import sympy as sp
a_, b_, c_, k_, q_ = sp.symbols("a b c k q")
assert sp.expand((3*a_ + 7*b_) + (3*b_ + 7*a_) - 5*(2*a_ + 2*b_)) == 0
# transitivity: 3a+7c = 5(k+q-2b) when 5k=3a+7b, 5q=3b+7c
assert sp.expand(5*((3*a_ + 7*b_)/5 + (3*b_ + 7*c_)/5 - 2*b_) - (3*a_ + 7*c_)) == 0
assert Rr(0, 5) and Rr(5, 0) and 3*0 + 7*5 == 35 and 3*5 + 7*0 == 15
assert not all(not (Rr(x, y) and Rr(y, x)) or x == y for x in rg for y in rg)
print("Q3a(2) OK: R is not antisymmetric (0R5, 5R0), so not a partial order")


# =====================================================================================
# STEPS section: every numeric answer, choice key and findbug line used by gen_25A-A.py
# =====================================================================================
import itertools as _it
from math import gcd as _gcd, factorial as _fac, log as _log, isqrt as _isq
import sympy as sp

EXPECT_NUM = {}
BUG_IDX = {}
_imp = lambda a, b: (not a) or b
_rows3 = list(_it.product([True, False], repeat=3))

# Q1a
_L = [_imp(not p, not (q or r)) for p, q, r in _rows3]
_R = [_imp(q, p) and _imp(r, p) for p, q, r in _rows3]
assert _L == _R and sum(_L) == 5
assert sum(1 for (p, q, r), v in zip(_rows3, _L) if (not p) and v) == 1
assert _L[_rows3.index((False, True, True))] == _R[_rows3.index((False, True, True))] == False
EXPECT_NUM["25A-A-Q1a"] = [5, 1]

# Q1b
assert pow(50, 24, 13) == 1 and _fac(12) % 13 == 12
assert (((50 ** 2) ** 12 - 1) + (_fac(12) - 1)) != 50 ** 24 + _fac(12) and (_fac(12) - 1) % 13 != 0
assert 13 % 13 == 0 and 13 % 26 != 0 and not sp.isprime(26)
assert (71 ** 120 - 1) % 26 == 0 and (50 ** 24 + _fac(12)) % 26 == 0
EXPECT_NUM["25A-A-Q1b"] = [1, 12]; BUG_IDX["25A-A-Q1b"] = 2

# Q1c
_f = {k: 3 * k // _gcd(3, k) for k in [1, 4, 5, 6, 9, 18]}
assert _f[5] == 15 and _f[9] == 9 and _f[4] == 12
_img = set(_f.values()); assert _img == {3, 6, 9, 12, 15, 18} and len(_img) == 6
assert not _img <= {3, 6, 9, 12, 15} and not _img <= {1, 4, 5, 6, 9, 18}
assert 1 not in _img and 2 not in _img   # Z is not the image: f is not onto Z
EXPECT_NUM["25A-A-Q1c"] = [15, 9, 4]

# Q2a
_k = sp.symbols("k", positive=True)
assert sp.simplify(_k / (4 * _k + 1) + 1 / ((4 * _k + 1) * (4 * _k + 5)) - (_k + 1) / (4 * _k + 5)) == 0
assert sp.expand((4 * _k + 1) * (_k + 1)) == 4 * _k ** 2 + 5 * _k + 1 == sp.expand(4 * _k ** 2 + 4 * _k + (_k + 1))
assert sp.expand(4 * _k ** 2 + 4 * _k + (_k - 1)) != 4 * _k ** 2 + 5 * _k + 1
assert 2 * (4 * 2 + 5) + 1 == 27 == (4 * 2 + 1) * (2 + 1)
for _n in range(1, 40):
    assert sum(Fraction(1, (4 * i - 3) * (4 * i + 1)) for i in range(1, _n + 1)) == Fraction(_n, 4 * _n + 1)
EXPECT_NUM["25A-A-Q2a"] = [27]; BUG_IDX["25A-A-Q2a"] = 1

# Q2b
assert int(_log(5, 3)) == 1 and 1 < _log(5, 3) < 2
assert not any(5 ** b == 3 ** a for a in range(1, 80) for b in range(1, 80))
_x = _log(5, 3)
assert abs(3 ** (2 * _x) - 5 ** 2) < 1e-9 and abs(5 ** (2 * _x) - 3 ** 2) > 1   # 3^a=5^b holds, 5^a=3^b does not
assert 5 ** 3 % 2 == 1 and 3 ** 4 % 2 == 1   # both odd: no parity contradiction
EXPECT_NUM["25A-A-Q2b"] = [1]; BUG_IDX["25A-A-Q2b"] = 1

# Q2c
_P3 = [(a, b) for a in range(1, 4) for b in range(1, 4)]
def _refl(R): return all((a, a) in R for a in range(1, 4))
def _sym(R): return all((b, a) in R for a, b in R)
def _anti(R): return all(not ((b, a) in R and a != b) for a, b in R)
def _trans(R): return all((a, d) in R for a, b in R for c, d in R if b == c)
_all = [frozenset(u for u, bit in zip(_P3, bits) if bit) for bits in _it.product([0, 1], repeat=9)]
assert any((not _refl(R)) and (not _sym(R)) and (not _anti(R)) and (not _trans(R)) and len(R) <= 5 for R in _all)
_ex = {(1, 2), (2, 1), (2, 3)}
assert (not _refl(_ex)) and (not _sym(_ex)) and (not _anti(_ex)) and (not _trans(_ex)) and len(_ex) == 3
_tr = [R for R in _all if _trans(R)]
assert any(R1 != R2 and _trans(R1 | R2) and (R1 & R2) for R1 in _tr for R2 in _tr)   # so "no such relations" is false
_R1, _R2 = {(1, 1), (1, 2)}, {(1, 1), (1, 3)}
assert _trans(_R1) and _trans(_R2) and _R1 != _R2 and _trans(_R1 | _R2) and (_R1 & _R2) and len(_R1 | _R2) == 3
assert (2, 1) in _ex and (3, 2) not in _ex
EXPECT_NUM["25A-A-Q2c"] = [3]; BUG_IDX["25A-A-Q2c"] = 2

# Q3a
_a, _b, _c, _kk, _q = sp.symbols("a b c kk q")
assert sp.expand((3 * _a + 7 * _b) + (3 * _b + 7 * _c)).coeff(_b) == 10
assert sp.expand((3 * _a + 7 * _b) + (3 * _b + 7 * _c) - 10 * _b - (3 * _a + 7 * _c)) == 0
assert sp.expand(5 * _kk + 5 * _q - 10 * _b - 5 * (_kk + _q - 2 * _b)) == 0
assert sp.expand(5 * _kk + 5 * _q - 10 * _b - 5 * (_kk + _q - _b)) != 0
_Rr = lambda x, y: (3 * x + 7 * y) % 5 == 0
_Z = range(-15, 16)
assert all(_Rr(x, x) for x in _Z) and all(_Rr(y, x) for x in _Z for y in _Z if _Rr(x, y))
assert all(_Rr(x, z) for x in _Z for y in _Z for z in _Z if _Rr(x, y) and _Rr(y, z))
assert _Rr(0, 5) and _Rr(5, 0)
EXPECT_NUM["25A-A-Q3a"] = [10]; BUG_IDX["25A-A-Q3a"] = 2

# Q3b
assert 184 % 48 == 40 and _gcd(48, 184) == 8
assert [48 * x + 184 * y for x, y in [(4, -1), (-4, 1), (3, -1), (1, 4)]] == [8, -8, -40, 784]
assert [-48 * x + 184 * y for x, y in [(4, -1), (-4, -1), (-4, 1), (1, 4)]] == [-376, 8, 376, 688]
assert _gcd(-48, 184) == 8
EXPECT_NUM["25A-A-Q3b"] = [40, 8]

# Q3c
_U = [0, 1, 2]
_subs = [frozenset(c) for r in range(4) for c in _it.combinations(_U, r)]
for A in _subs:
    for B in _subs:
        for C in _subs:
            assert ((B | C) - A) <= ((B - A) | (C - A)) and (((B - A) | (C - A)) <= ((B | C) - A))
for bx, cx, ax in _it.product([True, False], repeat=3):
    assert ((bx or cx) and not ax) == ((bx and not ax) or (cx and not ax))
assert any((((bx or cx) and not ax)) and not ((bx and not ax) and (cx and not ax)) for bx, cx, ax in _it.product([True, False], repeat=3))
assert len((({2, 3} | {1, 4, 5}) - {1, 2})) == 3
EXPECT_NUM["25A-A-Q3c"] = [3]; BUG_IDX["25A-A-Q3c"] = 2

# Q4a
_U4 = [0, 1, 2, 3]
_s4 = [frozenset(c) for r in range(5) for c in _it.combinations(_U4, r)]
def _pw(X): return {frozenset(c) for r in range(len(X) + 1) for c in _it.combinations(sorted(X), r)}
_d1 = _d2 = _d3 = False
for A in _s4:
    for B in _s4:
        if not A or not B:
            continue
        eq = (_pw(A) | _pw(B)) == _pw(A | B)
        both_not = (not A <= B) and (not B <= A)
        either_not = (not A <= B) or (not B <= A)
        either_sub = A <= B or B <= A
        assert (not both_not) or (not eq)                 # the correct contrapositive holds
        assert eq == either_sub                           # the claim and its converse
        _d1 = _d1 or (either_not and eq)                  # "or"-version conclusion unequal is false
        _d2 = _d2 or (both_not and eq)                    # "both -> equal" would be false (never true)
        _d3 = _d3 or (either_sub and not eq)              # "either_sub -> unequal" would be false (never true)
assert _d1 and (not _d2) and (not _d3)
# so distractors 2 and 3 are false statements (both_not cases exist, either_sub cases exist)
assert any((not A <= B) and (not B <= A) for A in _s4 for B in _s4 if A and B)
assert any(A <= B for A in _s4 for B in _s4 if A and B)
_A, _B = frozenset({1, 2}), frozenset({2, 3})
assert len(_pw(_A) | _pw(_B)) == 6 and len(_pw(_A | _B)) == 8
# bug: if b is also in A then {a,b} <= A, so {a,b} is in P(A)
assert frozenset({1, 2}) in _pw(frozenset({1, 2}))
EXPECT_NUM["25A-A-Q4a"] = [6, 8]; BUG_IDX["25A-A-Q4a"] = 0

# Q4b
assert sum(1 for a in range(0, 11) if sp.isprime(a * a + a + 2)) == 1
assert all((a * (a + 1)) % 2 == 0 for a in range(0, 500)) and all(a * a + a + 2 >= 4 for a in range(1, 500))
assert (1 * 1 + 1 + 2) % 3 != 0 and _isq(2 * 2 + 2 + 2) ** 2 != 2 * 2 + 2 + 2 and (3 * 3 + 3 + 2) % 3 != 0
EXPECT_NUM["25A-A-Q4b"] = [1]; BUG_IDX["25A-A-Q4b"] = 1

# Q4c
_im = {3 ** m * 5 ** n for m in range(0, 30) for n in range(0, 30)}
assert 3 ** 2 * 5 == 45 and 7 not in _im and 3 in _im and 1 in _im
assert len(_im) == 900   # injective on the grid
assert not any(3 ** m + 5 ** n == 7 for m in range(0, 10) for n in range(0, 10))
assert (7 - (-1)) + (20 - 10) == 18 and (15 - 0) + (35 - 30) == 20   # interval lengths 18 vs 20
EXPECT_NUM["25A-A-Q4c"] = [45]; BUG_IDX["25A-A-Q4c"] = 1

# ---- cross-check against the generated raw JSON ----
import json as _json, pathlib as _pl
_raw = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / "25A-A.json").read_text(encoding="utf-8"))
_n = 0
for _q in _raw["questions"]:
    _qid = "25A-A-Q%d%s" % (_q["num"], "abcdefghij"["אבגדהוזחטי".index(_q["part"])])
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
