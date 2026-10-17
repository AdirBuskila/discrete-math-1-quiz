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
# --- solver/arbiter 2026-10-17 ---
# Q6b (form 2 Q2b): corrected answer 121 + 2^1210 + 2^111 (key wrote |A-B|=111 for |P(A-B)|)
val = len(A | B2) + 2**(len(A) * len(B2)) + 2**len(A - B2)
assert val == 121 + 2**1210 + 2**111 and val != 232 + 2**1210
print("Q6b form2 corrected OK: 121 + 2^1210 + 2^111")
# Q7a (form 2 Q3a): 3x+7y even
R2 = lambda x, y: (3 * x + 7 * y) % 2 == 0
assert all(R2(x, x) for x in rng) and all(R2(y, x) for x in rng for y in rng if R2(x, y))
assert all(R2(x, z) for x in rng for y in rng for z in rng if R2(x, y) and R2(y, z))
assert all(R2(x, 0) == (x % 2 == 0) and R2(x, 1) == (x % 2 == 1) for x in rng)
assert R2(0, 2) and R2(2, 0) and (3 * 0 + 7 * 2, 3 * 2 + 7 * 0) == (14, 6)
print("Q7a form2 OK (equivalence, 2 classes, not a partial order)")

# ======================= STEPS section (step-author pass) =======================
_CODE = "22A-B"
# Re-reads tools/raw/<CODE>.json and recomputes every numeric step answer and every choice key independently
# (sympy / brute force). ASCII output only.
import json as _json, pathlib as _pl, itertools as _it
import sympy as _sp

_RAW = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / (_CODE + ".json")).read_text(encoding="utf-8"))
_PART = {"": "", "a": "א", "b": "ב", "c": "ג", "d": "ד", "e": "ה"}


def _Q(num, p=""):
    for q in _RAW["questions"]:
        if q["num"] == num and q.get("part", "") == _PART[p]:
            return q
    raise KeyError((num, p))


def _S(num, p, i):
    return _Q(num, p)["steps"][i]


def _num(num, p, i, expected, tol=0):
    s = _S(num, p, i)
    assert s["type"] == "numeric" and s["answer"] == expected and s.get("tol", 0) == tol, (num, p, i, s["answer"], expected)


def _right(num, p, i, expected):
    s = _S(num, p, i)
    assert s["type"] == "choice"
    got = [o["value"] for o in s["options"] if o["id"] == s["correctId"]][0]
    assert got == expected, (num, p, i, got, expected)


def _nsteps(num, p, n):
    assert len(_Q(num, p)["steps"]) == n, (num, p)


def _lines(num, p, i):
    return _S(num, p, i)["lines"]


import math
from fractions import Fraction as _Fr
_x, _y, _z, _k = _sp.symbols("x y z k")
_rows = list(_it.product([True, False], repeat=3))
_imp = lambda a, b: (not a) or b

# ---- 1a (form 1) / 5a (form 2)
_L1 = lambda p, q, r: _imp(p and q, r); _R1 = lambda p, q, r: _imp(p, (not q) or r)
assert all(_L1(*w) == _R1(*w) for w in _rows)
assert [w for w in _rows if not _L1(*w)] == [(True, True, False)]
assert all(_L1(*w) for w in ((True, False, False), (False, True, False), (True, True, True)))
_L2 = lambda p, q, r: _imp(p, r) and _imp(q, r); _R2 = lambda p, q, r: _imp(p or q, r)
assert all(_L2(*w) == _R2(*w) for w in _rows)
assert len([w for w in _rows if not _R2(*w)]) == 3
assert [w for w in _rows if _L2(*w) and _R2(*w) and not w[2]] == [(False, False, False)]
for _f_ in (_L1, _R1, _L2, _R2):
    assert not all(_f_(*w) for w in _rows) and any(_f_(*w) for w in _rows)         # no tautology, no contradiction
_num(1, "a", 0, 1); _num(5, "a", 0, 3); _nsteps(1, "a", 3); _nsteps(5, "a", 3)
_right(1, "a", 1, r"$p=T,\ q=T,\ r=F$"); _right(5, "a", 1, r"$p=F,\ q=F,\ r=F$")
print("STEPS 1a/5a OK")

# ---- 1b / 5b
assert math.gcd(84, 68) == 4 == math.gcd(-68, -84) == math.gcd(-84, -68)
_seq = []; _a, _b2 = 84, 68
while _b2: _seq.append((_a, _b2, _a // _b2, _a % _b2)); _a, _b2 = _b2, _a % _b2
assert _seq == [(84, 68, 1, 16), (68, 16, 4, 4), (16, 4, 4, 0)]
assert [(a, b) for a, b in [(5, -4), (-4, 5), (5, 4), (4, -5)] if 68 * a + 84 * b == 4] == [(5, -4)]
assert [(a, b) for a, b in [(-4, 5), (5, -4), (4, 5), (-5, 4)] if 84 * a + 68 * b == 4] == [(-4, 5)]
assert all(math.gcd(math.lcm(a, b), math.gcd(a, b)) == math.gcd(a, b) for a in range(3, 70) for b in range(3, a))
_d, _m = math.gcd(84, 68), math.lcm(84, 68)
assert math.gcd(_m, _d) == 4 and _m == 1428 and len({4, _m, 1, 84 * 68}) == 4
for _n in (1, 5):
    _num(_n, "b", 0, 4); _right(_n, "b", 3, "$\\gcd(a,b)$"); _nsteps(_n, "b", 4)
    assert _lines(_n, "b", 1) == [r"$84=1\cdot68+16$", r"$68=4\cdot16+4$", r"$16=4\cdot4+0$"]
_right(1, "b", 2, "$(5,-4)$"); _right(5, "b", 2, "$(-4,5)$")
print("STEPS 1b/5b OK")

# ---- 1c / 5c
for _n, (_a1, _b1) in ((1, (25, 8)), (5, (36, 10))):
    _aa = _a1**20 + math.factorial(40); _bb = _b1**80 + 40; _g = math.gcd(_aa, _bb)
    assert _sp.isprime(41) and _g % 41 == 0 and _g > 40
    assert all(_g % p != 0 for p in (37, 43, 47))
    assert pow(_a1, 20, 41) == 1 and math.factorial(40) % 41 == 40 and _bb % 41 == 0
    _num(_n, "c", 1, 1); _num(_n, "c", 2, 40); _num(_n, "c", 3, 0); _right(_n, "c", 0, "41"); _nsteps(_n, "c", 4)
print("STEPS 1c/5c OK")

# ---- 2a / 6a
for _c in (5, 4):
    for _kk in range(1, 300):
        assert _kk <= _kk**2 and 1 <= _kk**2 and _kk**2 + 2 * _kk + 1 <= 4 * _kk**2 <= _c * _kk**2
    assert all(n * n <= _c**n for n in range(1, 300))
    assert _kk**2 + 2 * _kk**2 + _kk**2 == 4 * _kk**2 != 3 * _kk**2
assert 2**2 > 2 and 2 * 1 + 1 > 1 and 3**2 > 2 * 3 + 1                       # the three false facts fail at k=2, k=1, k=3
for _n in (2, 6):
    _o = _lines(_n, "a", 1); _bg = _S(_n, "a", 2)
    assert len(_o) == 5 and sum(1 for x, y in zip(_o, _bg["lines"]) if x != y) == 1 and _bg["bugIndex"] == 2 != -1
    assert _bg["lines"][2] != _o[2]
    _nsteps(_n, "a", 3)
print("STEPS 2a/6a OK")

# ---- 2b / 6b
_A = {3**n * 5**m for n in range(11) for m in range(11)}
_B1 = {5**m for m in range(1, 11)}; _B2 = {3**n for n in range(1, 11)}
assert len(_A) == 121 and _B1 < _A and _B2 <= _A and len(_A - _B1) == 111 and len(_A) * len(_B1) == 1210
assert len(_A | _B2) == 121 and len(_A - _B2) == 111 and len(_A) * len(_B2) == 1210
_num(2, "b", 0, 121); _num(2, "b", 1, 111); _num(2, "b", 2, 1210); _right(2, "b", 3, "$111+2^{1210}+2^{121}$"); _nsteps(2, "b", 4)
_num(6, "b", 0, 121); _num(6, "b", 1, 111); _num(6, "b", 2, 1210); _right(6, "b", 3, "$121+2^{1210}+2^{111}$"); _nsteps(6, "b", 4)
assert 121 + 111 == 232
print("STEPS 2b/6b OK")

# ---- 2c / 6c  (P: A <= B u C, Q: A-B <= C)
_U = [set(c) for r in range(1, 4) for c in _it.combinations(range(3), r)]
_Pf = lambda A, B, C: A <= (B | C)
_Qf = lambda A, B, C: (A - B) <= C
_trip = [(A, B, C) for A in _U for B in _U for C in _U]
assert all(_imp(_Pf(*t), _Qf(*t)) for t in _trip)
assert all(_imp(not _Qf(*t), not _Pf(*t)) == _imp(_Pf(*t), _Qf(*t)) for t in _trip)
assert any(_Pf(*t) and _Qf(*t) for t in _trip)                                 # "P -> not Q" (wrong option 3) fails on a witness
for A, B, C in _trip:
    for x in A - B:
        if x not in C:
            assert x in A and x not in (B | C)
for _n in (2, 6):
    _o = _lines(_n, "c", 1); _bg = _S(_n, "c", 2)
    assert len(_o) == 4 and sum(1 for x, y in zip(_o, _bg["lines"]) if x != y) == 1 and _bg["bugIndex"] == 2
    _nsteps(_n, "c", 3)
print("STEPS 2c/6c OK")

# ---- 3a / 7a
for _n, (_a_, _b_) in ((3, (9, 5)), (7, (3, 7))):
    _s = _a_ + _b_
    _R = lambda u, v: (_a_ * u + _b_ * v) % 2 == 0
    _rg = range(-10, 11)
    assert all(_R(u, u) for u in _rg) and all(_R(v, u) for u in _rg for v in _rg if _R(u, v))
    assert all(_R(u, w) for u in range(-6, 7) for v in range(-6, 7) for w in range(-6, 7) if _R(u, v) and _R(v, w))
    assert len({frozenset(v for v in _rg if _R(u, v)) for u in _rg}) == 2 and _R(1, 3) and _R(3, 1)
    assert _sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _x) - _s * (_x + _y)) == 0
    assert all(_sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _x) - c * (_x + _y)) != 0 for c in (_s - 2, _s + 2))
    assert _sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _z) - (_a_ * _x + _b_ * _z + _s * _y)) == 0 and _s % 2 == 0
    _num(_n, "a", 0, 2); _right(_n, "a", 1, "$" + str(_s) + "(x+y)$"); _nsteps(_n, "a", 4)
print("STEPS 3a/7a OK")

# ---- 3b / 7b
_fk = lambda k: (k * k) % 6 + math.lcm(2, math.gcd(2, k))
assert [_fk(k) for k in range(1, 8)] == [3, 6, 5, 6, 3, 2, 3]
assert len([k for k in range(1, 8) if _fk(k) == 3]) == 3 and [k for k in range(1, 8) if _fk(k) == 5] == [3]
_good = [sub for r in range(8) for sub in _it.combinations(range(1, 8), r)
         if sorted(_fk(k) for k in sub) == [2, 3, 5, 6]]
assert len(_good) == 6
for _n in (3, 7):
    _num(_n, "b", 0, 3); _num(_n, "b", 1, 3); _num(_n, "b", 2, 6); _nsteps(_n, "b", 3)
print("STEPS 3b/7b OK")

# ---- 3c / 7c
def _props(R, A):
    return (all((a, a) in R for a in A), all((b, a) in R for a, b in R),
            all(not ((a, b) in R and (b, a) in R and a != b) for a, b in R),
            all((a, d) in R for a, b in R for c, d in R if b == c))
for _nn in (2, 3, 4):
    _A_ = list(range(_nn)); _allp = [(a, b) for a in _A_ for b in _A_]; _cnt = []
    for _m in range(1 << len(_allp)):
        R = {_allp[i] for i in range(len(_allp)) if _m >> i & 1}
        rf, sy, an, tr = _props(R, _A_)
        if rf and sy and an: _cnt.append(R)
    assert len(_cnt) == 1 and _cnt[0] == {(a, a) for a in _A_}
    rf, sy, an, tr = _props(_cnt[0], _A_); assert rf and sy and an and tr         # identity: equivalence AND partial order
_I5 = {(a, a) for a in range(5)}
assert len(_I5) == 5 and all(_props(_I5, range(5)))
for _a, _b in ((x, y) for x in range(5) for y in range(5) if x != y):          # n=5: any off-diagonal pair breaks sym+antisym
    _Rr = _I5 | {(_a, _b)}
    assert not _props(_Rr, range(5))[1] or not _props(_Rr, range(5))[2]
    _Rs = _Rr | {(_b, _a)}
    assert _props(_Rs, range(5))[1] and not _props(_Rs, range(5))[2]
for _n in (3, 7):
    _num(_n, "c", 1, 5); _nsteps(_n, "c", 3)
print("STEPS 3c/7c OK")

# ---- 4a / 8a
for _c0, _hi in ((3, 8), (5, 9)):
    for _n_ in range(1, 60):
        _v = _Fr(_c0) + _Fr(1, 2**_n_)
        assert _c0 < _v < _hi
        assert not (_sp.sqrt(2) / _n_ + _c0).is_rational
        assert _hi + _Fr(1, _n_) > _hi and _c0 - _Fr(1, 2**_n_) < _c0
_nsteps(4, "a", 3); _nsteps(8, "a", 3)
print("STEPS 4a/8a OK")

# ---- 4b / 8b  (n = 4)
_Af = list(range(1, 10)); _ev = {2, 4, 6, 8}; _od = {1, 3, 5, 7, 9}; _c1 = _c2 = 0
for _m in range(1 << 9):
    _Bs = {_Af[i] for i in range(9) if _m >> i & 1}
    _c1 += (_Bs | _od) == set(_Af); _c2 += (_Bs | _ev) == set(_Af)
assert _c1 == 32 == 2**5 and _c2 == 16 == 2**4 and len(_ev) == 4 and len(_od) == 5
_num(4, "b", 0, 4); _num(4, "b", 1, 5); _num(4, "b", 2, 32); _nsteps(4, "b", 4)
_num(8, "b", 0, 5); _num(8, "b", 1, 4); _num(8, "b", 2, 16); _nsteps(8, "b", 4)
print("STEPS 4b/8b OK")
