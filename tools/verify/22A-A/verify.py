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
# --- solver/arbiter 2026-10-17 ---
# Q6b (form 2 Q2b): corrected answer 870 + 2^810000 + 2^30 (key used 300*300)
assert len(A2) * len(B2) == 900 * 900 == 810000 != 300 * 300
assert {x for x in A2 if x % 5 == 0 or x % 7 == 0} == A2 - {3**n for n in range(30)}
assert A2 & B2 == {3**n for n in range(30)}
val = len(A2 - B2) + 2**(len(A2) * len(B2)) + 2**len(A2 & B2)
assert val == 870 + 2**810000 + 2**30
print("Q6b form2 corrected OK: 870 + 2^810000 + 2^30")
# Q7a (form 2 Q3a): 3x+7y even -> equivalence, classes evens/odds, not a partial order
R2 = lambda x, y: (3*x + 7*y) % 2 == 0
assert all(R2(x, x) for x in rng) and all(R2(y, x) for x in rng for y in rng if R2(x, y))
assert all(R2(x, z) for x in rng for y in rng for z in rng if R2(x, y) and R2(y, z))
assert all(R2(0, x) == (x % 2 == 0) and R2(1, x) == (x % 2 == 1) for x in rng)
assert R2(1, 3) and R2(3, 1) and (3*1+7*3, 3*3+7*1) == (24, 16)
print("Q7a form2 OK (equivalence, 2 classes, not a partial order)")

# ======================= STEPS section (step-author pass) =======================
_CODE = "22A-A"
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
_x, _y, _z, _k = _sp.symbols("x y z k")
_T = {True: "T", False: "F"}
_rows = list(_it.product([True, False], repeat=3))
_imp = lambda a, b: (not a) or b
_fv = lambda p, q, r: _imp(p, q) and (not r)

# ---- 1a (CNF) / 5a (DNF)
_false_rows = [w for w in _rows if not _fv(*w)]; _true_rows = [w for w in _rows if _fv(*w)]
assert len(_false_rows) == 5 and len(_true_rows) == 3
_clauses = {  # clause options for row TTT; each is a disjunction
    "right": lambda p, q, r: (not p) or (not q) or (not r), "w1": lambda p, q, r: p or q or r,
    "w2": lambda p, q, r: (not p) or q or r, "w3": lambda p, q, r: p or (not q) or (not r)}
_rowTTT = (True, True, True)
assert _clauses["right"](*_rowTTT) is False and all(_clauses[k](*_rowTTT) is True for k in ("w1", "w2", "w3"))
assert all(_clauses["right"](*w) for w in _rows if w != _rowTTT)          # false ONLY at TTT
_cnf = lambda p, q, r: all([(not p) or (not q) or (not r), (not p) or q or (not r), (not p) or q or r, p or (not q) or (not r), p or q or (not r)])
assert all(_cnf(*w) == _fv(*w) for w in _rows)
_terms = {"right": lambda p, q, r: p and q and (not r), "w1": lambda p, q, r: p and q and r,
          "w2": lambda p, q, r: (not p) and (not q) and (not r), "w3": lambda p, q, r: p and (not q) and (not r)}
_rowTTF = (True, True, False)
assert _terms["right"](*_rowTTF) is True and all(_terms[k](*_rowTTF) is False for k in ("w1", "w2", "w3"))
assert all(not _terms["right"](*w) for w in _rows if w != _rowTTF)
_dnf = lambda p, q, r: (p and q and not r) or ((not p) and q and not r) or ((not p) and (not q) and not r)
assert all(_dnf(*w) == _fv(*w) for w in _rows)
_num(1, "a", 1, 5); _num(5, "a", 1, 3); _nsteps(1, "a", 3); _nsteps(5, "a", 3)
_right(1, "a", 2, r"$\neg p\vee\neg q\vee\neg r$"); _right(5, "a", 2, r"$p\wedge q\wedge\neg r$")
print("STEPS 1a/5a OK")

# ---- 1b / 5b
assert math.gcd(55, 40) == 5 == math.gcd(55, -40) and _sp.ilcm(-55, 40) == 440 == _sp.ilcm(55, -40)
assert [(a, b) for a, b in [(3, -4), (3, 4), (-4, 3), (4, -3)] if 55 * a + 40 * b == 5] == [(3, -4)]
_seq = []; _a, _b2 = 55, 40
while _b2: _seq.append((_a, _b2, _a // _b2, _a % _b2)); _a, _b2 = _b2, _a % _b2
assert _seq == [(55, 40, 1, 15), (40, 15, 2, 10), (15, 10, 1, 5), (10, 5, 2, 0)]
for _n in (1, 5):
    _num(_n, "b", 0, 5); _num(_n, "b", 3, 440); _right(_n, "b", 2, "$(3,-4)$"); _nsteps(_n, "b", 4)
    assert _lines(_n, "b", 1) == [r"$55=1\cdot40+15$", r"$40=2\cdot15+10$", r"$15=1\cdot10+5$", r"$10=2\cdot5+0$"]
print("STEPS 1b/5b OK")

# ---- 1c / 5c
assert 16**15 == 4**30 and 7**60 == 49**30 and pow(4, 30, 31) == 1 and pow(49, 30, 31) == 1
assert (16**15 + 7**60 + 37) % 31 == 8
assert 36**15 == 6**30 and 8**60 == 64**30 and pow(6, 30, 31) == 1 and pow(64, 30, 31) == 1
assert (36**15 + 8**60 + 47) % 31 == 18 and _sp.isprime(31)
for _n, _f in ((1, 8), (5, 18)):
    _num(_n, "c", 1, 1); _num(_n, "c", 2, 1); _num(_n, "c", 3, _f); _nsteps(_n, "c", 4)
print("STEPS 1c/5c OK")

# ---- 2a / 6a  (sums)
_S1 = lambda k: sum(range(k + 1, 2 * k + 1))                    # (k+1)+...+(2k)
_S2 = lambda k: sum(range(k + 2, 2 * k + 3))                    # (k+2)+...+(2k+2)
for _k_ in range(1, 40):
    assert _S1(_k_) == _k_ * (3 * _k_ + 1) // 2 and _S2(_k_) == (_k_ + 1) * (3 * _k_ + 4) // 2
    assert _S1(_k_ + 1) == _S1(_k_) - (_k_ + 1) + (2 * _k_ + 1) + (2 * _k_ + 2)
    assert _S1(_k_ + 1) != _S1(_k_) - (_k_ + 1) + (2 * _k_ + 2)
    assert _S1(_k_ + 1) != _S1(_k_) + (2 * _k_ + 1) + (2 * _k_ + 2)
    assert _S1(_k_ + 1) != _S1(_k_) - _k_ - (_k_ + 1) + (2 * _k_ + 2)
    assert _S2(_k_ + 1) == _S2(_k_) - (_k_ + 2) + (2 * _k_ + 3) + (2 * _k_ + 4)
    assert _S2(_k_ + 1) != _S2(_k_) - (_k_ + 2) + (2 * _k_ + 4)
    assert _S2(_k_ + 1) != _S2(_k_) + (2 * _k_ + 3) + (2 * _k_ + 4)
    assert _S2(_k_ + 1) != _S2(_k_) - (_k_ + 1) - (_k_ + 2) + (2 * _k_ + 4)
assert _S1(3) == 15 and _S2(3) == 26
_h = _sp.Rational(1, 2)
_e = lambda t: _sp.simplify(t)
assert _e(_k * (3 * _k + 1) * _h - (_k + 1) + (2 * _k + 1) + (2 * _k + 2) - (3 * _k**2 + _k + 2 * (3 * _k + 2)) * _h) == 0
assert _e((3 * _k**2 + _k + 2 * (3 * _k + 2)) * _h - (3 * _k**2 + 7 * _k + 4) * _h) == 0
assert _sp.expand((_k + 1) * (3 * _k + 4)) == 3 * _k**2 + 7 * _k + 4
assert _e((3 * _k**2 + _k + 2 * (3 * _k + 1)) * _h - (3 * _k**2 + 7 * _k + 2) * _h) == 0   # bug line is self-consistent...
assert _sp.expand(3 * _k**2 + 7 * _k + 2) != _sp.expand((_k + 1) * (3 * _k + 4))              # ...but wrong
assert _e((_k + 1) * (3 * _k + 4) * _h - (_k + 2) + (2 * _k + 3) + (2 * _k + 4) - ((_k + 1) * (3 * _k + 4) * _h + 3 * _k + 5)) == 0
assert _sp.expand(((_k + 1) * (3 * _k + 4) + 2 * (3 * _k + 5))) == 3 * _k**2 + 13 * _k + 14 == _sp.expand((_k + 2) * (3 * _k + 7))
assert _sp.expand((_k + 1) * (3 * _k + 4) + 2 * (3 * _k + 4)) != _sp.expand((_k + 2) * (3 * _k + 7))   # bug line wrong
for _n, _v in ((2, 15), (6, 26)):
    _num(_n, "a", 0, _v)
    _o = _lines(_n, "a", 2); _bg = _S(_n, "a", 3)
    assert len(_o) == 4 and sum(1 for x, y in zip(_o, _bg["lines"]) if x != y) == 1 and _bg["lines"][_bg["bugIndex"]] != _o[_bg["bugIndex"]]
    _nsteps(_n, "a", 4)
print("STEPS 2a/6a OK")

# ---- 2b / 6b  (sets)
_A = {3**n * 5**m for n in range(20) for m in range(20)}; _B = {2**n * 5**m for n in range(20) for m in range(20)}
assert len(_A) == len(_B) == 400 and len(_A & _B) == 20 and len(_A - _B) == 380 and len(_A) * len(_B) == 160000
_num(2, "b", 0, 20); _num(2, "b", 1, 380); _num(2, "b", 2, 160000); _right(2, "b", 3, "$20+2^{160000}+2^{380}$"); _nsteps(2, "b", 4)
_A = {3**n * 7**m for n in range(30) for m in range(30)}; _B = {3**n * 5**m for n in range(30) for m in range(30)}
assert len(_A) == len(_B) == 900 and len(_A & _B) == 30 and len(_A - _B) == 870 and len(_A) * len(_B) == 810000
assert 900 * 900 != 90000
_num(6, "b", 0, 30); _num(6, "b", 1, 870); _num(6, "b", 2, 810000); _right(6, "b", 3, "$870+2^{810000}+2^{30}$"); _nsteps(6, "b", 4)
print("STEPS 2b/6b OK")

# ---- 2c / 6c  (contrapositive, form 1 statement P: A-B<=C, Q: A-C<=B)
_U = [set(c) for r in range(1, 4) for c in _it.combinations(range(3), r)]            # non-empty subsets of {0,1,2}
_Pf = lambda A, B, C: (A - B) <= C
_Qf = lambda A, B, C: (A - C) <= B
_trip = [(A, B, C) for A in _U for B in _U for C in _U]
assert all(_imp(_Pf(*t), _Qf(*t)) for t in _trip)                                      # the claim is true
assert all(_imp(not _Qf(*t), not _Pf(*t)) == _imp(_Pf(*t), _Qf(*t)) for t in _trip)       # contrapositive == original
assert any(_Pf(*t) and _Qf(*t) for t in _trip)    # "P -> not Q" (wrong option 3) fails on a witness
for _n in (2, 6):
    _o = _lines(_n, "c", 1); _bg = _S(_n, "c", 2)
    assert len(_o) == 4 and sum(1 for x, y in zip(_o, _bg["lines"]) if x != y) == 1 and _bg["bugIndex"] == 2
    _nsteps(_n, "c", 3)
# every x in A-C with x not in B satisfies x in A-B and x not in C; the bug line (x in C) never holds
for A, B, C in _trip:
    for x in A - C:
        if x not in B:
            assert (x in A and x not in B) and x not in C
print("STEPS 2c/6c OK")

# ---- 3a / 7a  (parity relation)
for _n, (_a_, _b_) in ((3, (3, 5)), (7, (3, 7))):
    _s = _a_ + _b_
    _R = lambda u, v: (_a_ * u + _b_ * v) % 2 == 0
    _rg = range(-10, 11)
    assert all(_R(u, u) for u in _rg) and all(_R(v, u) for u in _rg for v in _rg if _R(u, v))
    assert all(_R(u, w) for u in range(-6, 7) for v in range(-6, 7) for w in range(-6, 7) if _R(u, v) and _R(v, w))
    assert len({frozenset(v for v in _rg if _R(u, v)) for u in _rg}) == 2
    assert _R(1, 3) and _R(3, 1)
    assert _sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _x) - _s * (_x + _y)) == 0
    assert all(_sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _x) - c * (_x + _y)) != 0 for c in (_s - 2, _s + 2))
    assert _sp.expand((_a_ * _x + _b_ * _y) + (_a_ * _y + _b_ * _z) - (_a_ * _x + _b_ * _z + _s * _y)) == 0 and _s % 2 == 0
    _num(_n, "a", 0, 2); _right(_n, "a", 1, "$" + str(_s) + "(x+y)$"); _nsteps(_n, "a", 4)
print("STEPS 3a/7a OK")

# ---- 3b / 7b
_fk = lambda k: (k * k) % 6 + math.lcm(2, math.gcd(2, k))
assert _fk(3) == 5 and _fk(6) == 2 and _fk(7) == 3
assert {_fk(k) for k in range(1, 7)} == {2, 3, 5, 6} == {_fk(k) for k in range(1, 8)}
_num(3, "b", 0, 5); _num(3, "b", 1, 2); _num(3, "b", 2, 4); _right(3, "b", 3, r"$\{2,3,5,6\}$"); _nsteps(3, "b", 4)
_num(7, "b", 0, 3); _num(7, "b", 1, 2); _num(7, "b", 2, 4); _right(7, "b", 3, r"$\{2,3,5,6\}$"); _nsteps(7, "b", 4)
print("STEPS 3b/7b OK")

# ---- 3c / 7c
_pairs = lambda perm: {(perm[i], perm[j]) for i in range(5) for j in range(i, 5)}
for _p in _it.permutations(range(1, 6)):
    _Rr = _pairs(_p)
    assert len(_Rr) == 15 and len({a for a, b in _Rr}) == 5 and len(_Rr) != 5          # never a function
_ident = {(i, i) for i in range(1, 6)}
assert all((i, i) in _ident for i in range(1, 6)) and (1, 2) not in _ident and (2, 1) not in _ident   # id: refl, antisym, trans but not total
for _n in (3, 7):
    _nsteps(_n, "c", 3)
print("STEPS 3c/7c OK")

# ---- 4a / 8a
from sympy import Interval, Union, oo
_A1 = Union(Interval.open(-oo, 2), Interval.Ropen(3, 8)); _A2 = Union(Interval.Lopen(-5, -2), Interval.Ropen(-1, oo))
assert Interval.open(0, 1).is_subset(_A1) and Interval.open(0, 1).is_subset(_A2)
for _iv in (Interval.open(1, 3), Interval.open(2, 3), Interval.Ropen(1, 4)):
    assert not _iv.is_subset(_A1)
for _iv in (Interval.open(-3, -1), Interval.open(-2, -1), Interval.open(-6, -4)):
    assert not _iv.is_subset(_A2)
_nsteps(4, "a", 3); _nsteps(8, "a", 3)
_right(4, "a", 1, "$(0,1)$"); _right(8, "a", 1, "$(0,1)$")
print("STEPS 4a/8a OK")

# ---- 4b / 8b  (n = 4, |A| = 9)
_n_ = 4; _Aset = list(range(1, 2 * _n_ + 2)); _odd = {v for v in _Aset if v % 2}; _even = {v for v in _Aset if v % 2 == 0}
_c1 = _c2 = _c3 = 0
for _m in range(1 << 9):
    _Bs = {_Aset[i] for i in range(9) if _m >> i & 1}
    _c1 += len(_Bs & _odd) == 1; _c3 += len(_Bs & _even) == 1; _c2 += 1 < len(_Bs) < 9
assert (_c1, _c2, _c3) == (80, 501, 128) and (_n_ + 1) * 2**_n_ == 80 and _n_ * 2**(_n_ + 1) == 128 == 4 * 32
assert len(_odd) == 5 and len(_even) == 4 and 2**4 == 16 and 2**5 == 32 and 2**9 - 2 - 9 == 501
_num(4, "b", 0, 5); _num(4, "b", 1, 16); _num(4, "b", 2, 80); _num(4, "b", 3, 501); _nsteps(4, "b", 4)
_num(8, "b", 0, 4); _num(8, "b", 1, 32); _num(8, "b", 2, 128); _num(8, "b", 3, 501); _nsteps(8, "b", 4)
print("STEPS 4b/8b OK")
