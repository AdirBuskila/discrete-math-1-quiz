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

# ======================= STEPS section (step-author pass) =======================
_CODE = "19A-B"
# Re-reads tools/raw/<CODE>.json and recomputes every numeric step answer and every choice key independently
# (sympy / brute force). ASCII output only.
import json as _json, pathlib as _pl, itertools as _it, math as _m
import sympy as _sp

_RAW = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / (_CODE + ".json")).read_text(encoding="utf-8"))


def _Q(num, p=""):
    for q in _RAW["questions"]:
        if q["num"] == num and q.get("part", "") == p:
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


def _wrong(num, p, i):
    s = _S(num, p, i)
    return [o["value"] for o in s["options"] if o["id"] != s["correctId"]]


def _nsteps(num, p, n):
    assert len(_Q(num, p)["steps"]) == n, (num, p)


def _lines(num, p, i):
    return _S(num, p, i)["lines"]


def _bug(num, p, i, idx):
    s = _S(num, p, i)
    assert s["type"] == "findbug" and s["bugIndex"] == idx, (num, p, i)
    return s


def _rubsum(num, p):
    q = _Q(num, p)
    assert sum(r["points"] for r in q["rubric"]) == q["points"], (num, p)


def _pat(num, p, i, preds):
    s = _S(num, p, i)
    assert s["correctId"] == "a" and len(s["options"]) == len(preds), (num, p, i)
    assert [bool(f()) for f in preds] == [True] + [False] * (len(preds) - 1), (num, p, i, [bool(f()) for f in preds])


T2 = [True, False]
imp_ = lambda a, b: (not a) or b
iff_ = lambda a, b: a == b
fs_ = frozenset
E_ = fs_()
_all = lambda *a: all(a)


def _P(S):
    S = list(S)
    return {fs_(c) for k in range(len(S) + 1) for c in _it.combinations(S, k)}


# ---- Q1 alef
_ncon = lambda s: sum(s.count(c) for c in "&~")
_pat(1, "א", 0, [lambda: _ncon("p&~q") > 0, lambda: _ncon("p") > 0, lambda: _ncon("q") > 0, lambda: _ncon("r") > 0])
_num(1, "א", 1, len(list(_it.product(T2, repeat=3))))
_nsteps(1, "א", 2); _rubsum(1, "א")
print("STEPS Q1a OK")

# ---- Q1 bet
S_ = fs_([fs_([fs_([fs_([E_])])]), fs_([E_, fs_([fs_([1])]), fs_([E_]), fs_([fs_([fs_([1])]), E_])]), fs_([fs_([E_])])])
_PS = _P({1, 2})
Bs_ = fs_([1, _PS if False else fs_(_PS)])
assert len(S_) == 3 and len(Bs_) == 2
_num(1, "ב", 0, len(S_)); _num(1, "ב", 1, len(Bs_)); _num(1, "ב", 2, len(list(_it.product(S_, Bs_)))); assert len(list(_it.product(S_, Bs_))) == 6
_nsteps(1, "ב", 3); _rubsum(1, "ב")
print("STEPS Q1b OK")


# ---- Q1 gimel: symmetric relations
def _nsym(n):
    pr = [(a, b) for a in range(n) for b in range(n)]
    return sum(1 for k in range(len(pr) + 1) for c in _it.combinations(pr, k) if all((b, a) in c for a, b in c))


_num(1, "ג", 1, _nsym(2)); _num(1, "ג", 2, _nsym(3)); _num(1, "ג", 0, 3)
assert _nsym(2) == 8 and _nsym(3) == 64 == 2 ** 6
_nsteps(1, "ג", 3); _rubsum(1, "ג")
print("STEPS Q1c OK")

# ---- Q1 dalet: (0,1] max no min
from fractions import Fraction as _Fr
_ivs = {"(0,1]": (False, True), "[0,1]": (True, True), "(0,1)": (False, False), "[0,1)": (True, False)}
_goal = lambda k: (not _ivs[k][0]) and _ivs[k][1]            # no min (lower open), has max (upper closed)
_pat(1, "ד", 0, [lambda: _goal("(0,1]"), lambda: _goal("[0,1]"), lambda: _goal("(0,1)"), lambda: _goal("[0,1)")])
_pts = [_Fr(k, 1000) for k in range(1, 1001)]
assert max(_pts) == 1 and all(x / 2 < x and x / 2 > 0 for x in _pts)
_num(1, "ד", 1, 1)
_nsteps(1, "ד", 2); _rubsum(1, "ד")
print("STEPS Q1d OK")

# ---- Q1 he: surjections
_surj = [f for f in _it.product(range(3), repeat=3) if len(set(f)) == 3]
_inj = [f for f in _it.product(range(3), repeat=3) if len(set(f)) == 3]
assert _surj == _inj and len(_surj) == 6
_pat(1, "ה", 0, [lambda: all(len(set(f)) == 3 for f in _surj), lambda: all(len(set(f)) == 1 for f in _surj),
                 lambda: all(f == (0, 1, 2) for f in _surj), lambda: all(f[0] < f[1] < f[2] for f in _surj)])
_num(1, "ה", 1, 6); _num(1, "ה", 2, 27 - len(_surj))
_nsteps(1, "ה", 3); _rubsum(1, "ה")
print("STEPS Q1e OK")

# ---- Q1 vav: DNF
_f = lambda p, q, r: iff_(p and q, (not q) or r)
_rows = [x for x in _it.product(T2, repeat=3) if _f(*x)]
assert _rows == [(True, True, True), (False, True, False)]
_num(1, "ו", 0, len(_rows))
_pat(1, "ו", 1, [lambda: _f(False, True, False), lambda: _f(True, True, False), lambda: _f(True, False, True), lambda: _f(False, False, False)])
_t = [lambda p, q, r: (not p) and q and (not r), lambda p, q, r: p and q and r, lambda p, q, r: (not p) and (not q) and (not r),
      lambda p, q, r: p or (not q) or r]
assert [t(False, True, False) for t in _t] == [True, False, False, False]
assert [x for x in _it.product(T2, repeat=3) if _t[0](*x)] == [(False, True, False)]
_nsteps(1, "ו", 3); _rubsum(1, "ו")
print("STEPS Q1f OK")

# ---- Q1 zayin: forall x forall y exists z: y+z<x
import random as _rnd
_rnd.seed(3)
def _orig(A, B, C): return all(any(y + z < x for z in C) for x in A for y in B)
def _o0(A, B, C): return any(all(y + z >= x for z in C) for x in A for y in B)
def _o1(A, B, C): return all(y + z >= x for x in A for y in B for z in C)
def _o2(A, B, C): return any(any(y + z >= x for z in C) for x in A for y in B)
def _o3(A, B, C): return any(all(y + z >= x for y in B for z in C) for x in A)


_diff = [False] * 4
for _ in range(5000):
    A = {_rnd.randint(0, 6) for _ in range(_rnd.randint(1, 3))}
    B = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    C = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    for k, fn in enumerate((_o0, _o1, _o2, _o3)):
        if fn(A, B, C) != (not _orig(A, B, C)):
            _diff[k] = True
assert _diff == [False, True, True, True]
_right(1, "ז", 0, r"קיים $x\in A$ וקיים $y\in B$ כך שלכל $z\in C$ מתקיים $y+z\ge x$")
_cmp = [lambda a: a >= 0, lambda a: a > 0, lambda a: a <= 0, lambda a: a == 0]      # a = y+z-x ; negation of a<0 is a>=0
_vals = range(-3, 4)
assert [all((not (a < 0)) == c(a) for a in _vals) for c in _cmp] == [True, False, False, False]
_nsteps(1, "ז", 2); _rubsum(1, "ז")
print("STEPS Q1g OK")

# ---- Q2 alef
_k = _sp.symbols("k", integer=True)
S = lambda n: sum(range(n + 1, 2 * n + 1))
assert all(S(n) == n * (3 * n + 1) // 2 for n in range(1, 100))
_num(2, "א", 0, S(3))
assert all(S(kk + 1) - S(kk) == (2 * kk + 1) + (2 * kk + 2) - (kk + 1) for kk in range(1, 50))
assert all(S(kk + 1) - S(kk) != (2 * kk + 2) for kk in range(1, 50)) and all(S(kk + 1) - S(kk) != (2 * kk + 1) + (2 * kk + 2) for kk in range(1, 50))
assert all(S(kk + 1) - S(kk) != (2 * kk + 2) - 2 * kk for kk in range(1, 50))
_L = _lines(2, "א", 2)
assert _sp.simplify(_k * (3 * _k + 1) / 2 - (_k + 1) + (2 * _k + 1) + (2 * _k + 2) - (_k * (3 * _k + 1) / 2 + 3 * _k + 2)) == 0
assert _sp.simplify(_k * (3 * _k + 1) / 2 + 3 * _k + 2 - (3 * _k ** 2 + 7 * _k + 4) / 2) == 0
assert _sp.expand((_k + 1) * (3 * _k + 4) - (3 * _k ** 2 + 7 * _k + 4)) == 0
assert _sp.simplify(_k * (3 * _k + 1) / 2 + 3 * _k + 4 - (3 * _k ** 2 + 7 * _k + 4) / 2) != 0
_bs = _bug(2, "א", 3, 1)
assert [i for i in range(4) if _bs["lines"][i] != _L[i]] == [1]
assert len(_L) == 4
_nsteps(2, "א", 4); _rubsum(2, "א")
print("STEPS Q2a OK")

# ---- Q2 bet
_A = {2 ** m * 5 ** n * 11 ** q for m in range(20) for n in range(20) for q in range(20)}
_B = {3 ** m * 5 ** n * 7 ** q for m in range(20) for n in range(20) for q in range(20)}
assert _A & _B == {5 ** n for n in range(20)} and len(_A) == len(_B) == 8000
_num(2, "ב", 0, len(_A & _B)); _num(2, "ב", 1, len(_A | _B)); assert len(_A | _B) == 15980 == 2 * 20 ** 3 - 20
_e = len(_A | _B)
assert [2 ** (2 * 20 ** 3 - 20) == 2 ** _e, 2 ** (2 * 20 ** 3) == 2 ** _e, 2 ** 20 ** 3 == 2 ** _e, (2 * 20 ** 3 - 20) == 2 ** _e] == [True, False, False, False]
_right(2, "ב", 2, r"$2^{2\cdot20^3-20}$")
_nsteps(2, "ב", 3); _rubsum(2, "ב")
print("STEPS Q2b OK")

# ---- Q2 gimel
_sets = [fs_(), fs_({1}), fs_({2}), fs_({1, 2}), fs_({1, 2, 3})]
_pr = lambda A, B: fs_((a, b) for a in A for b in B)
_eqpairs = [(A, B) for A in _sets for B in _sets if A != B and _pr(A, B) == _pr(B, A)]
assert all(not A or not B for A, B in _eqpairs) and (E_, fs_({1})) in _eqpairs
assert not [1 for A, B in _eqpairs if A and B]
_chk = lambda A, B: A != B and _pr(A, B) == _pr(B, A)
_pat(2, "ג", 0, [lambda: _chk(E_, fs_({1})), lambda: _chk(fs_({1}), fs_({2})), lambda: _chk(fs_({1}), fs_({1, 2})), lambda: _chk(fs_({1, 2}), fs_({1, 2, 3}))])
_num(2, "ג", 1, len(_pr(E_, fs_({1}))))
_nsteps(2, "ג", 2); _rubsum(2, "ג")
print("STEPS Q2c OK")

# ---- Q2 dalet
_subs = [fs_(c) for k in range(1, 4) for c in _it.combinations(range(3), k)]
assert all(_pr(A, B & C) == _pr(A, B) & _pr(A, C) for A in _subs for B in _subs for C in _subs)
_pat(2, "ד", 0, [lambda: True, lambda: False, lambda: False, lambda: False])
_right(2, "ד", 0, "נכונה לכל שלוש קבוצות")
assert not [1 for A in _subs for B in _subs for C in _subs if _pr(A, B & C) != _pr(A, B) & _pr(A, C)]
assert len(_lines(2, "ד", 2)) == 4
_nsteps(2, "ד", 3); _rubsum(2, "ד")
print("STEPS Q2d OK")

# ---- Q3 alef: xy>0 on Q-{0}
_Rq = lambda x, y: x * y > 0
_rat = [_Fr(a, b) for a in range(-6, 7) if a for b in range(1, 5)]
assert all(_Rq(x, x) for x in _rat) and all(_Rq(y, x) for x in _rat for y in _rat if _Rq(x, y))
assert all(_Rq(x, z) for x in _rat for y in _rat for z in _rat if _Rq(x, y) and _Rq(y, z))
_c1 = {x for x in _rat if _Rq(1, x)}
_cands = [{x for x in _rat if x > 0}, {x for x in _rat if x < 0}, {1}, set(_rat)]
assert [c == _c1 for c in _cands] == [True, False, False, False]
_right(3, "א", 0, r"$\{x\in\mathbb{Q}-\{0\}:\ x>0\}$")
assert len({fs_(y for y in _rat if _Rq(x, y)) for x in _rat}) == 2
_num(3, "א", 1, 2)
_x, _y, _z = _sp.symbols("x y z")
assert _sp.expand((_x * _y) * (_y * _z) - _x * _z * _y ** 2) == 0 and _sp.expand((_x * _y) * (_y * _z) - _x * _z * _y) != 0
_T3 = _lines(3, "א", 2); _b3 = _bug(3, "א", 3, 1)
assert len(_T3) == 3 and [i for i in range(3) if _b3["lines"][i] != _T3[i]] == [1]
_nsteps(3, "א", 4); _rubsum(3, "א")
print("STEPS Q3a OK")


# ---- Q3 bet: n = 12, blocks 5, 3, 4
_blocks = [list(range(5)), list(range(5, 8)), list(range(8, 12))]
_Rb = {(a, b) for blk in _blocks for a in blk for b in blk}
_cnt = lambda a: sum(1 for (x, y) in _Rb if x == a or y == a)
_num(3, "ב", 0, 12 - 5 - 3)
assert [_cnt(blk[0]) for blk in _blocks] == [9, 5, 7]
assert all(_cnt(blk[0]) == 2 * len(blk) - 1 for blk in _blocks)
assert all(_cnt(blk[0]) not in (len(blk), len(blk) ** 2, 2 * len(blk)) for blk in _blocks)
_right(3, "ב", 1, r"$2s-1$")
_num(3, "ב", 2, _cnt(0))
_nsteps(3, "ב", 3); _rubsum(3, "ב")
print("STEPS Q3b OK")

# ---- Q3 gimel: binomial sum
fn = lambda n: sum(_m.comb(n, k) * (3 ** (2 * k) + 2 ** (2 * k)) for k in range(n + 1))
assert all(fn(n) == 10 ** n + 5 ** n for n in range(2, 30))
_num(3, "ג", 1, sum(_m.comb(2, k) * 9 ** k for k in range(3))); _num(3, "ג", 2, fn(3))
assert fn(3) == 1125
_nsteps(3, "ג", 3); _rubsum(3, "ג")
print("STEPS Q3c OK")

# ---- Q4 alef
_num(4, "א", 0, 3 ** 3 - _m.factorial(3)); assert 21 == len([f for f in _it.product(range(3), repeat=3) if len(set(f)) < 3])
_v = [10 ** 10 - _m.factorial(10), _m.factorial(10) - 10 ** 10, 10 ** 10 - _m.comb(10, 2), 10 ** 10]
assert _v[0] == 10 ** 10 - _m.factorial(10) > 0 and _v[1] < 0 and _v[2] != _v[0] and _v[3] != _v[0]
_right(4, "א", 1, r"$10^{10}-10!$")
_nsteps(4, "א", 2); _rubsum(4, "א")
print("STEPS Q4a OK")

# ---- Q4 bet
_inc = [f for f in _it.product(range(5), repeat=3) if f[0] < f[1] < f[2]]
assert len(_inc) == 10 == _m.comb(5, 3) and {fs_(f) for f in _inc} == {fs_(c) for c in _it.combinations(range(5), 3)}
assert len({f for f in _inc if f[0] == 0}) > 1                    # f(1) alone does not determine f
_right(4, "ב", 0, r"קבוצת הערכים שלה, שהיא תת-קבוצה של $B$ בגודל $|A|$")
_num(4, "ב", 1, len(_inc)); _num(4, "ב", 2, _m.comb(20, 10)); assert _m.comb(20, 10) == 184756
_nsteps(4, "ב", 3); _rubsum(4, "ב")
print("STEPS Q4b OK")

# ---- Q4 gimel: partition
Om = [fs_({1, 2}), fs_({3}), fs_({4, 5})]
C5 = fs_(range(1, 6))
assert all(Om) and all(not (a & b) for a, b in _it.combinations(Om, 2)) and fs_().union(*Om) == C5
assert not all(len(b) == 2 for b in Om) and not (Om[0] & Om[1] & Om[2]) and len({len(b) for b in Om}) > 1
_right(4, "ג", 0, r"ש-$\Omega$ חלוקה של $C$: איבריה לא ריקים, זרים בזוגות ואיחודם $C$")
_R5 = {(a, b) for blk in Om for a in blk for b in blk}
_num(4, "ג", 1, len(_R5)); assert len(_R5) == 9
_nsteps(4, "ג", 2); _rubsum(4, "ג")
print("STEPS Q4c OK")

# ---- Q4 dalet
_refl = all((a, a) in _R5 for a in range(1, 6)); _trn = all((a, d) in _R5 for a, b in _R5 for c, d in _R5 if b == c)
_ant = all(not ((b, a) in _R5 and a != b) for a, b in _R5)
assert _refl and _trn and not _ant
_num(4, "ד", 0, len(_R5))
_pat(4, "ד", 1, [lambda: not _ant, lambda: _refl and _trn and _ant, lambda: not _refl, lambda: not _trn])
_nsteps(4, "ד", 2); _rubsum(4, "ד")
print("STEPS Q4d OK")

# ---- Q4 he: Fermat product
_pr_ = [x for x in range(3, 60) if _sp.isprime(x)]
for _p in _pr_:
    for _q in _pr_:
        if _p < _q:
            n = (int(_sp.totient(_p)) ** int(_sp.totient(_q)) - 1) * ((1 + int(_sp.totient(_q))) ** int(_sp.totient(_p)) - 1)
            assert n % (_p * _q) == 0
            assert ((_p - 1) ** (_q - 1) - 1) % _q == 0 and (_q ** (_p - 1) - 1) % _q != 0
_right(4, "ה", 0, "משפט Fermat הקטן")
_pat(4, "ה", 1, [lambda: ((3 - 1) ** 4 - 1) % 5 == 0, lambda: (5 ** 2 - 1) % 5 == 0, lambda: False, lambda: (5 ** 2 - 1) % 5 == 0 and ((3 - 1) ** 4 - 1) % 5 == 0])
_num(4, "ה", 2, (2 ** 4 - 1) * (5 ** 2 - 1)); assert 360 % 15 == 0
_nsteps(4, "ה", 3); _rubsum(4, "ה")
print("STEPS Q4e OK")

# ---- Q5 alef: phi
ph = lambda n: int(_sp.totient(n))
_bad = [(m, n) for m in range(1, 80) for n in range(m + 1, 80) if ph(m) % 2 and ph(n) % 2]
assert _bad == [(1, 2)]
_num(5, "א", 0, ph(2))
_pat(5, "א", 1, [lambda: ph(1) % 2 and ph(2) % 2, lambda: ph(2) % 2 and ph(3) % 2, lambda: ph(1) % 2 and ph(3) % 2, lambda: ph(3) % 2 and ph(4) % 2])
_nsteps(5, "א", 2); _rubsum(5, "א")
print("STEPS Q5a OK")

# ---- Q5 bet
assert all(ph(q) % 2 == 0 for q in range(3, 500)) and ph(1) % 2 and ph(2) % 2
_num(5, "ב", 1, len([n for n in range(1, 101) if ph(n) % 2])); _num(5, "ב", 2, ph(8))
_pat(5, "ב", 0, [lambda: all(ph(q) % 2 == 0 for q in range(3, 500)), lambda: all(ph(n) % 2 == 0 for n in range(1, 50)),
                 lambda: all(sum(t) % 2 == 0 for t in _it.combinations(range(1, 20), 3)),
                 lambda: all(ph(n) % 2 == 0 for n in range(2, 50))])
assert not all(ph(n) % 2 == 0 for n in range(1, 50))
_nsteps(5, "ב", 3); _rubsum(5, "ב")
print("STEPS Q5b OK")

# ---- Q5 gimel
_sets5 = [[1 + _Fr(1, n) for n in range(1, 60)], [1 - _Fr(1, n) for n in range(2, 60)], [_Fr(n) for n in range(1, 60)], [5 + _Fr(1, n) for n in range(2, 60)]]
assert [all(1 < v <= 5 for v in S5) for S5 in _sets5] == [True, False, False, False]
_pat(5, "ג", 1, [(lambda S5=S5: all(1 < v <= 5 for v in S5)) for S5 in _sets5])
_right(5, "ג", 0, "חסם מלמעלה (הכלה ב-$\\mathbb{Q}$) וחסם מלמטה (תת-קבוצה אינסופית בת-מנייה), ואז שוויון")
_nsteps(5, "ג", 2); _rubsum(5, "ג")
print("STEPS Q5c OK")

# ---- Q5 dalet
nn = _sp.symbols("n", integer=True)
a_ = [5, 21]
for _i in range(2, 12):
    a_.append(6 * a_[-1] - 9 * a_[-2])
assert all(5 * 3 ** i + 2 * i * 3 ** i == a_[i] for i in range(12))
Cs = _sp.symbols("C1 C2"); sol = _sp.solve([Cs[0] - 5, 3 * Cs[0] + 3 * Cs[1] - 21], Cs)
assert sol == {Cs[0]: 5, Cs[1]: 2}
_num(5, "ד", 1, 2); _num(5, "ד", 2, a_[2]); assert a_[2] == 81
# the candidate forms: which satisfy the recurrence (generic coefficients)?
rec = lambda f: all(f(i) == 6 * f(i - 1) - 9 * f(i - 2) for i in range(2, 10))
assert rec(lambda i: 3 ** i) and rec(lambda i: i * 3 ** i) and not rec(lambda i: (-3) ** i) and not rec(lambda i: 6 ** i) and not rec(lambda i: 9 ** i)
# C1*3^n + C2*3^n has one degree of freedom: a1 = 3*a0 always, but a1 = 21 != 15
assert all(3 * (c1 + c2) != 21 for c1 in range(6) for c2 in range(6) if c1 + c2 == 5)
_right(5, "ד", 0, r"$(C_1+C_2n)3^n$")
_nsteps(5, "ד", 3); _rubsum(5, "ד")
print("STEPS Q5d OK")
