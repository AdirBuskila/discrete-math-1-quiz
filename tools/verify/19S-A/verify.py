# Checks of the 19S-A key. ASCII output only.
import itertools
from fractions import Fraction as Fr
from math import comb, factorial, gcd
from sympy import totient
from sympy.functions.combinatorial.numbers import stirling
fs = frozenset
T = [True, False]
# Q1a2/a3/a4/a5
A = fs([1, 2, 3])
assert A ^ A == fs() and A ^ fs() == A
D = [(1, 1), (2, 2), (3, 3)]
R1, R2 = fs(D + [(1, 2)]), fs(D + [(2, 1)])
tr = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
sym = lambda R: all((b, a) in R for a, b in R)
anti = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
assert tr(R1) and tr(R2) and all((x, x) in R1 and (x, x) in R2 for x in (1, 2, 3))
X = R1 ^ R2
assert X == fs([(1, 2), (2, 1)]) and sym(X) and not anti(X)
P = fs([(1, 1), (2, 2)])
assert tr(P) and anti(P) and all((x, x) in P for x in (1, 2)) and not ((1, 2) in P or (2, 1) in P)
cnt = sum(1 for f in itertools.product(range(1, 6), repeat=5)
          if len(set(f)) == 5 and set(f[:2]) == {1, 2})
assert cnt == 12
print("Q1a OK")
# Q1b
S = lambda p, q, r: (p and q) == ((not q) or r)
rows = [x for x in itertools.product(T, repeat=3) if S(*x)]
assert set(rows) == {(True, True, True), (False, True, False)}
print("Q1b OK")
# Q2a
for n in range(1, 200):
    assert sum(Fr(1, (4 * k - 3) * (4 * k + 1)) for k in range(1, n + 1)) == Fr(n, 4 * n + 1)
print("Q2a OK")
# Q2b
rg = range(10)
Aset = {2 ** n * 3 ** m for m in rg for n in rg}
Bs = {2 ** n for n in rg}
Cs = {3 ** n for n in rg}
assert len(Aset) == 100 and len(Bs) == len(Cs) == 10
BxC = {(b, c) for b in Bs for c in Cs}
BuC = Bs | Cs
assert len({e for e in BxC if e not in BuC}) == 100
assert len(Bs ^ Cs) == 18
assert len(Bs & Cs) == 1
print("Q2b OK (|P(AxB) x C| = 10 * 2^1000 by formula)")
# Q2c
for n in range(0, 30):
    assert sum(comb(n, k) * 4 ** k for k in range(n + 1)) == 5 ** n
assert all((Fr(5, 4) ** n) > 10 ** 6 for n in (80,))
print("Q2c OK")
# Q3a
xs = [x for x in range(-6, 7) if x]
assert all((x * y > 0) == (y * x > 0) for x in xs for y in xs)
assert all(not (x * y > 0 and y * z > 0) or x * z > 0 for x in xs for y in xs for z in xs)
print("Q3a OK")
# Q3b: contrapositive witness
for Aa, Bb in (({1, 2}, {2, 3}), ({1, 2, 3}, {3, 4})):
    assert not Aa <= Bb and not Bb <= Aa
    a = min(Aa - Bb); b = min(Bb - Aa)
    sub = lambda U: {fs(c) for k in range(len(U) + 1) for c in itertools.combinations(sorted(U), k)}
    assert fs([a, b]) in sub(Aa | Bb) and fs([a, b]) not in sub(Aa) | sub(Bb)
print("Q3b OK")
# Q3c
for n in range(10, 15):
    els = range(1, n + 1)
    c = sum(1 for k in range(n + 1) for B in itertools.combinations(els, k)
            if not ({1, 2, 3, 4} & set(B)) and 7 in B) if n <= 13 else None
    if c is not None:
        assert c == 2 ** (n - 5)
m = comb(8, 4); assert m == 70 and int(totient(m * m)) == 1680
print("Q3c OK")
# Q4
assert 6 ** 4 == 1296
assert sum(1 for f in itertools.product(range(1, 7), repeat=4) if f[0] > f[1] > f[2] > f[3]) == 15
assert sum(1 for f in itertools.product(range(1, 7), repeat=4) if len(set(f)) == 4 and set(f[:2]) == {1, 2}) == 24
assert stirling(5, 3) == 25
parts = set()
pr = [3, 5, 7, 11, 13]
def rec(i, bl):
    if i == 5:
        if len(bl) == 3:
            parts.add(fs(fs(b) for b in bl))
        return
    for j in range(len(bl)):
        bl[j].append(pr[i]); rec(i + 1, bl); bl[j].pop()
    bl.append([pr[i]]); rec(i + 1, bl); bl.pop()
rec(0, [])
assert len(parts) == 25
evens = sum(1 for w in itertools.permutations(range(1, 7), 4) if w[-1] % 2 == 0)
assert evens == 180
assert sum(1 for w in itertools.permutations(range(1, 7)) if any(set(w[i:i + 3]) == {1, 2, 3} for i in range(4))) == 144
print("Q4 OK")
# Q5
for n in range(6, 600, 3):
    assert totient(3 * n) == 3 * totient(n)
fib = lambda n: (((1 + 5 ** .5) / 2) ** n - ((1 - 5 ** .5) / 2) ** n) / 5 ** .5
a, b = 0, 1
for n in range(0, 40):
    assert abs(a - fib(n)) < 1e-3 * max(1, a)
    a, b = b, a + b
print("Q5 OK")

# ======================= STEPS section (step-author pass) =======================
_CODE = "19S-A"
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
    got = [bool(f()) for f in preds]
    assert got == [True] + [False] * (len(preds) - 1), (num, p, i, got)


T2 = [True, False]
imp_ = lambda a, b: (not a) or b
fs_ = frozenset
E_ = fs_()
from fractions import Fraction as _Fr
import random as _rnd

# ---- Q1 alef
_ncon = lambda s: sum(s.count(c) for c in "&~>")
_pat(1, "א", 0, [lambda: _ncon("p") == 0, lambda: _ncon("p&q") == 0, lambda: _ncon("~p") == 0, lambda: _ncon("p>q") == 0])
_num(1, "א", 1, len(list(_it.product(T2, repeat=2))))
_nsteps(1, "א", 2); _rubsum(1, "א")
print("STEPS Q1a OK")

# ---- Q1 bet
_univ = range(4)
_subs = [fs_(c) for k in range(1, 5) for c in _it.combinations(_univ, k)]        # nonempty A
_cb1 = [lambda A: A, lambda A: E_, lambda A: A | {9}, lambda A: A - {min(A)}]
_pat(1, "ב", 0, [(lambda f=f: all(A ^ f(A) == E_ for A in _subs)) for f in _cb1])
_pat(1, "ב", 1, [(lambda f=f: all(A ^ f(A) == A for A in _subs)) for f in [lambda A: E_, lambda A: A, lambda A: A | {9}, lambda A: A - {min(A)}]])
_num(1, "ב", 2, len(fs_({1, 2, 3}) ^ fs_({3, 4})))
_nsteps(1, "ב", 3); _rubsum(1, "ב")
print("STEPS Q1b OK")

# ---- Q1 gimel
D3 = fs_([(1, 1), (2, 2), (3, 3)])
_trn = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
_ref = lambda R, A=(1, 2, 3): all((a, a) in R for a in A)
_sym = lambda R: all((b, a) in R for a, b in R)
_ant = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
_ok = lambda R1, R2: _ref(R1) and _ref(R2) and _trn(R1) and _trn(R2) and _sym(R1 ^ R2) and not _ant(R1 ^ R2)
_pat(1, "ג", 0, [lambda: _ok(D3 | {(1, 2)}, D3 | {(2, 1)}), lambda: _ok(D3 | {(1, 2)}, D3 | {(1, 2)}),
                 lambda: _ok(D3 | {(1, 2)}, D3 | {(1, 2), (2, 1)}), lambda: _ok(D3, D3 | {(1, 3)})])
_num(1, "ג", 1, len((D3 | {(1, 2)}) ^ (D3 | {(2, 1)})))
_nsteps(1, "ג", 2); _rubsum(1, "ג")
print("STEPS Q1c OK")

# ---- Q1 dalet
_A2 = (1, 2)
_pairs2 = [(1, 1), (2, 2), (1, 2), (2, 1)]
_pos = [fs_(c) for k in range(5) for c in _it.combinations(_pairs2, k)
        if all((a, a) in c for a in _A2) and _ant(fs_(c)) and _trn(fs_(c))]
_tot = lambda R: all((a, b) in R or (b, a) in R for a in _A2 for b in _A2)
_pt = lambda R: R in _pos and not _tot(R)
_pat(1, "ד", 0, [lambda: _pt(fs_([(1, 1), (2, 2)])), lambda: _pt(fs_([(1, 1), (2, 2), (1, 2)])),
                 lambda: _pt(fs_([(1, 1), (2, 2), (2, 1)])), lambda: _pt(fs_(_pairs2))])
_num(1, "ד", 1, len(_pos)); _num(1, "ד", 2, sum(1 for R in _pos if _tot(R)))
assert len(_pos) == 3
_nsteps(1, "ד", 3); _rubsum(1, "ד")
print("STEPS Q1d OK")

# ---- Q1 he
_cnt = [f for f in _it.product(range(1, 6), repeat=5) if set(f) == {1, 2, 3, 4, 5} and set(f[:2]) == {1, 2}]
assert len(_cnt) == 12
_num(1, "ה", 0, len([f for f in _it.permutations([1, 2])])); _num(1, "ה", 1, len(list(_it.permutations([3, 4, 5])))); _num(1, "ה", 2, len(_cnt))
_nsteps(1, "ה", 3); _rubsum(1, "ה")
print("STEPS Q1e OK")

# ---- Q1 vav
iff_ = lambda a, b: a == b
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

# ---- Q1 zayin: forall x exists (y,z): x > y+z
_rnd.seed(11)
def _orig(A, B, C): return all(any(x > y + z for y in B for z in C) for x in A)
def _o0(A, B, C): return any(all(x <= y + z for y in B for z in C) for x in A)
def _o1(A, B, C): return all(x <= y + z for x in A for y in B for z in C)
def _o2(A, B, C): return any(any(x <= y + z for y in B for z in C) for x in A)
def _o3(A, B, C): return any(all(x < y + z for y in B for z in C) for x in A)


_diff = [False] * 4
for _ in range(5000):
    A = {_rnd.randint(0, 6) for _ in range(_rnd.randint(1, 3))}
    B = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    C = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    for k, fn in enumerate((_o0, _o1, _o2, _o3)):
        if fn(A, B, C) != (not _orig(A, B, C)):
            _diff[k] = True
assert _diff == [False, True, True, True]
_right(1, "ז", 0, r"קיים $x\in A$ כך שלכל זוג $(y,z)\in B\times C$ מתקיים $x\le y+z$")
_cmp = [lambda a: a <= 0, lambda a: a < 0, lambda a: a >= 0, lambda a: a == 0]      # a = x-(y+z); negation of a>0
assert [all((not (a > 0)) == c(a) for a in range(-3, 4)) for c in _cmp] == [True, False, False, False]
_nsteps(1, "ז", 2); _rubsum(1, "ז")
print("STEPS Q1g OK")

# ---- Q2 alef
_k = _sp.symbols("k")
_s = lambda n: sum(_Fr(1, (4 * i - 3) * (4 * i + 1)) for i in range(1, n + 1))
assert all(_s(n) == _Fr(n, 4 * n + 1) for n in range(1, 40))
_pat(2, "א", 0, [lambda: _s(2) == _Fr(2, 9), lambda: _s(2) == _Fr(1, 5), lambda: _s(2) == _Fr(1, 4), lambda: _s(2) == _Fr(1, 9)])
_pat(2, "א", 1, [(lambda e=e: _sp.expand(e - (4 * _k ** 2 + 5 * _k + 1)) == 0) for e in
                 [(4 * _k + 1) * (_k + 1), (4 * _k + 5) * (_k + 1), (4 * _k + 1) * (_k + 5), (2 * _k + 1) ** 2]])
_si = _lines(2, "א", 2)
assert len(_si) == 5
assert _sp.simplify(_k / (4 * _k + 1) + 1 / ((4 * _k + 1) * (4 * _k + 5)) - (_k + 1) / (4 * _k + 5)) == 0
assert _sp.expand(_k * (4 * _k + 5) + 1 - (4 * _k ** 2 + 5 * _k + 1)) == 0
_b = _bug(2, "א", 3, 3)
assert [i for i in range(5) if _b["lines"][i] != _si[i]] == [3]
assert _sp.expand((4 * _k + 5) * (_k + 1) - (4 * _k ** 2 + 5 * _k + 1)) != 0
_nsteps(2, "א", 4); _rubsum(2, "א")
print("STEPS Q2a OK")

# ---- Q2 bet
_Bs = {2 ** n for n in range(10)}; _Cs = {3 ** n for n in range(10)}
_As = {2 ** n * 3 ** m for n in range(10) for m in range(10)}
assert len(_As) == 100
_num(2, "ב", 0, len(_Bs & _Cs)); _num(2, "ב", 1, len(_Bs ^ _Cs))
_BxC = {(b, c) for b in _Bs for c in _Cs}
_num(2, "ב", 2, len(_BxC - (_Bs | _Cs))); assert len(_BxC - (_Bs | _Cs)) == 100 and len(_Bs ^ _Cs) == 18
_v = [len(_Cs) * 2 ** (len(_As) * len(_Bs)), len(_Cs) * 2 ** 100, 2 ** 1000 + 10, 2 ** 10000]
assert _v[0] == 10 * 2 ** 1000 and all(x != _v[0] for x in _v[1:])
_right(2, "ב", 3, r"$10\cdot2^{1000}$")
_nsteps(2, "ב", 4); _rubsum(2, "ב")
print("STEPS Q2b OK")

# ---- Q2 gimel
_num(2, "ג", 0, sum(_m.comb(3, kk) * 4 ** kk for kk in range(4)))
assert all(sum(_m.comb(n, kk) * 4 ** kk for kk in range(n + 1)) == 5 ** n for n in range(1, 25))
_nmin = min(n for n in range(1, 100) if _Fr(5, 4) ** n > 100)
_num(2, "ג", 2, _nmin); assert _nmin == 21
_L = lambda n: _Fr(4, 5) ** n
assert _L(200) < _Fr(1, 10 ** 15)              # lim 4^n/5^n = 0, not infinity
_right(2, "ג", 1, r"בשלילה: מניחים $5^n\le c_0\cdot4^n$ ומראים ש-$(5/4)^n$ אינו חסום")
assert all(5 ** n > 1 * 4 ** n for n in range(1, 50))      # c0 = 1 never works
_nsteps(2, "ג", 3); _rubsum(2, "ג")
print("STEPS Q2c OK")

# ---- Q3 alef
_Rr = lambda x, y: x * y > 0
_zs = [z for z in range(-12, 13) if z]
assert all(_Rr(x, x) for x in _zs) and all(_Rr(y, x) for x in _zs for y in _zs if _Rr(x, y))
assert all(_Rr(x, z) for x in _zs for y in _zs for z in _zs if _Rr(x, y) and _Rr(y, z))
_c1 = {x for x in _zs if _Rr(1, x)}
assert [_c1 == {x for x in _zs if x > 0}, _c1 == {x for x in _zs if x < 0}, _c1 == {1}, _c1 == set(_zs)] == [True, False, False, False]
_right(3, "א", 0, r"$\{x\in\mathbb{Z}-\{0\}:\ x>0\}$")
assert len({fs_(y for y in _zs if _Rr(x, y)) for x in _zs}) == 2
_num(3, "א", 1, 2)
_x, _y, _z = _sp.symbols("x y z")
assert _sp.expand((_x * _y) * (_y * _z) - _x * _z * _y ** 2) == 0 and _sp.expand((_x * _y) * (_y * _z) - _x * _z * _y) != 0
_T = _lines(3, "א", 2); _bb = _bug(3, "א", 3, 1)
assert len(_T) == 3 and [i for i in range(3) if _bb["lines"][i] != _T[i]] == [1]
_nsteps(3, "א", 4); _rubsum(3, "א")
print("STEPS Q3a OK")


# ---- Q3 bet: contrapositive of  p -> (a or b),  p: P(AuB)=P(A)uP(B), a: A<=B, b: B<=A
def _fo(p, a, b): return imp_(p, a or b)
_ctr = [lambda p, a, b: imp_((not a) and (not b), not p), lambda p, a, b: imp_(a or b, p),
        lambda p, a, b: imp_(not p, (not a) and (not b)), lambda p, a, b: imp_((not a) or (not b), not p)]
_eqv = lambda g: all(_fo(p, a, b) == g(p, a, b) for p in T2 for a in T2 for b in T2)
_pat(3, "ב", 0, [lambda: _eqv(_ctr[0]), lambda: _eqv(_ctr[1]), lambda: _eqv(_ctr[2]), lambda: _eqv(_ctr[3])])
def _P(S):
    S = list(S)
    return {fs_(c) for k in range(len(S) + 1) for c in _it.combinations(S, k)}
_g = len(_P({1, 2, 3})) - len(_P({1, 2}) | _P({2, 3}))
_num(3, "ב", 1, _g); assert _g == 2
# the actual theorem on small sets
for _a in _it.chain.from_iterable(_it.combinations(range(4), k) for k in range(1, 4)):
    for _bq in _it.chain.from_iterable(_it.combinations(range(4), k) for k in range(1, 4)):
        _eq = _P(_a) | _P(_bq) == _P(set(_a) | set(_bq))
        assert _eq == (set(_a) <= set(_bq) or set(_bq) <= set(_a))
assert len(_lines(3, "ב", 2)) == 3
_nsteps(3, "ב", 3); _rubsum(3, "ב")
print("STEPS Q3b OK")

# ---- Q3 gimel
def _cntB(n):
    return sum(1 for mask in range(1 << n)
               if not any(mask >> (e - 1) & 1 for e in (1, 2, 3, 4)) and mask >> 6 & 1)


assert all(_cntB(n) == 2 ** (n - 5) for n in range(10, 15))
_num(3, "ג", 0, _cntB(10))
assert [2 ** (10 - 5) == _cntB(10), 2 ** (10 - 4) == _cntB(10), 2 ** (10 - 6) == _cntB(10), (10 - 5) == _cntB(10)] == [True, False, False, False]
_right(3, "ג", 1, r"$2^{n-5}$")
_nsteps(3, "ג", 2); _rubsum(3, "ג")
print("STEPS Q3c OK")

# ---- Q3 dalet
_mm = _m.comb(8, 4)
assert sum(1 for _ in _it.combinations(range(8), 4)) == _mm == 70
_num(3, "ד", 0, _mm); _num(3, "ד", 1, int(_sp.totient(70))); _num(3, "ד", 2, int(_sp.totient(70 ** 2)))
assert int(_sp.totient(70 ** 2)) == 1680 == 70 * int(_sp.totient(70))
_nsteps(3, "ד", 3); _rubsum(3, "ד")
print("STEPS Q3d OK")

# ---- Q4 alef
_F = list(_it.product(range(6), repeat=4))
_num(4, "א", 0, len(_F)); assert len(_F) == 6 ** 4 == 1296
assert [6 ** 4 == len(_F), 4 ** 6 == len(_F), 6 * 4 == len(_F), _m.comb(6, 4) == len(_F)] == [True, False, False, False]
_right(4, "א", 1, r"$6^4$")
_nsteps(4, "א", 2); _rubsum(4, "א")
print("STEPS Q4a OK")

# ---- Q4 bet
_dec = [f for f in _F if f[0] > f[1] > f[2] > f[3]]
_num(4, "ב", 0, len(_dec)); assert len(_dec) == 15
_num(4, "ב", 1, len([f for f in _dec if set(f) == {1, 2, 3, 4}]))
_nsteps(4, "ב", 2); _rubsum(4, "ב")
print("STEPS Q4b OK")

# ---- Q4 gimel
_inj = [f for f in _F if len(set(f)) == 4 and set(f[:2]) == {0, 1}]
assert len(_inj) == 24
_num(4, "ג", 0, len({f[:2] for f in _inj})); _num(4, "ג", 1, len({f[2:] for f in _inj})); _num(4, "ג", 2, len(_inj))
_nsteps(4, "ג", 3); _rubsum(4, "ג")
print("STEPS Q4c OK")

# ---- Q4 dalet: S(5,3)
from sympy.functions.combinatorial.numbers import stirling
_prod = 3 * 5 * 7 * 11 * 13
_divs = [d for d in range(2, _prod + 1) if _prod % d == 0]
_S3 = {fs_(t) for t in _it.combinations(_divs, 3) if t[0] * t[1] * t[2] == _prod}
assert len(_S3) == 25 == stirling(5, 3)
_cands = [len(_S3), len(list(_it.permutations(range(5)))), _m.comb(5, 3), 3 ** 5]
assert _cands[0] != _cands[1] and _cands[0] != _cands[2] and _cands[0] != _cands[3]
_right(4, "ד", 0, r"חלוקה של $\{3,5,7,11,13\}$ לשלוש קבוצות לא ריקות")
_num(4, "ד", 1, int(stirling(4, 3))); _num(4, "ד", 2, len(_S3))
assert stirling(4, 3) == stirling(3, 2) + 3 * stirling(3, 3) == 6 and stirling(5, 3) == stirling(4, 2) + 3 * stirling(4, 3)
_nsteps(4, "ד", 3); _rubsum(4, "ד")
print("STEPS Q4d OK")

# ---- Q4 he
_ev = [w for w in _it.permutations(range(1, 7), 4) if w[-1] % 2 == 0]
_num(4, "ה", 0, len({w[-1] for w in _ev})); _num(4, "ה", 1, len(_ev)); assert len(_ev) == 180
_nsteps(4, "ה", 2); _rubsum(4, "ה")
print("STEPS Q4e OK")

# ---- Q4 vav
_adj = [p for p in _it.permutations(range(1, 7)) if max(p.index(v) for v in (1, 2, 3)) - min(p.index(v) for v in (1, 2, 3)) == 2]
assert len(_adj) == 144
_num(4, "ו", 0, _m.factorial(4)); _num(4, "ו", 1, _m.factorial(3)); _num(4, "ו", 2, len(_adj))
_nsteps(4, "ו", 3); _rubsum(4, "ו")
print("STEPS Q4f OK")

# ---- Q5 alef
ph = lambda n: int(_sp.totient(n))
assert all(ph(3 * n) == 3 * ph(n) for n in range(3, 400, 3))
assert ph(2 * 2) != ph(2) * ph(2) and all(ph(a * b) == ph(a) * ph(b) for a in range(1, 40) for b in range(1, 40) if _m.gcd(a, b) == 1)
_pat(5, "א", 0, [lambda: all(ph(a * b) == ph(a) * ph(b) for a in range(1, 40) for b in range(1, 40) if _m.gcd(a, b) == 1),
                 lambda: all(ph(a * b) == ph(a) * ph(b) for a in range(1, 20) for b in range(1, 20)),
                 lambda: all(ph(a * a) == ph(a) * ph(a) for a in range(1, 20)),
                 lambda: all(ph(a * b) == ph(a) * ph(b) for a in range(2, 20, 2) for b in range(2, 20, 2))])
_num(5, "א", 1, ph(12)); _num(5, "א", 2, ph(36)); assert ph(36) == 3 * ph(12)
_al = _sp.symbols("alpha", positive=True)
assert all(ph(3 ** a) == 2 * 3 ** (a - 1) for a in range(1, 10))
assert len(_lines(5, "א", 3)) == 3
_nsteps(5, "א", 4); _rubsum(5, "א")
print("STEPS Q5a OK")

# ---- Q5 bet
_Aset = [_Fr(1, 1) + _Fr(1, n) for n in range(2, 40)]
_inA = lambda v: (v.denominator == 1 and 20.5 <= v <= 100.5) or (1 <= v <= 5)
_cs = [[1 + _Fr(1, n) for n in range(2, 60)], [1 - _Fr(1, n) for n in range(2, 60)], list(map(_Fr, range(21, 101))), [5 + _Fr(1, n) for n in range(2, 60)]]
_inf = [True, True, False, True]            # the third set is finite
assert [all(_inA(v) for v in S) and inf for S, inf in zip(_cs, _inf)] == [True, False, False, False]
_right(5, "ב", 1, r"$\{1+\frac12,1+\frac13,1+\frac14,\ldots\}$")
_right(5, "ב", 0, "חסם מלמעלה בהכלה ב-$\\mathbb{Q}$ וחסם מלמטה בתת-קבוצה אינסופית בת-מנייה, ואז שוויון")
_nsteps(5, "ב", 2); _rubsum(5, "ב")
print("STEPS Q5b OK")

# ---- Q5 gimel
_rr = _sp.symbols("r")
_sols = _sp.solve(_rr ** 2 - _rr - 1, _rr)
_r1, _r2 = sorted(_sols, key=lambda v: float(v))
assert _sp.simplify(_r1 - (1 - _sp.sqrt(5)) / 2) == 0 and _sp.simplify(_r2 - (1 + _sp.sqrt(5)) / 2) == 0
_nr = [sorted([float((1 + _sp.sqrt(5)) / 2), float((1 - _sp.sqrt(5)) / 2)]), sorted([float((-1 + _sp.sqrt(5)) / 2), float((-1 - _sp.sqrt(5)) / 2)]),
       sorted([float(_sp.sqrt(5)), -float(_sp.sqrt(5))]), [-1.0, 1.0]]
_isroot = lambda vs: all(abs(v * v - v - 1) < 1e-9 for v in vs)
_pat(5, "ג", 0, [lambda: _isroot(_nr[0]), lambda: _isroot(_nr[1]), lambda: _isroot(_nr[2]), lambda: _isroot(_nr[3])])
_C2 = 1 / _sp.sqrt(5)
_Fib = [0, 1]
for _i in range(2, 30):
    _Fib.append(_Fib[-1] + _Fib[-2])
assert all(sp_ == 0 for sp_ in [_sp.simplify(_C2 * (_r2 ** n - _r1 ** n) - _Fib[n]) for n in range(0, 15)])
_cs2 = [1 / _sp.sqrt(5), -1 / _sp.sqrt(5), _sp.Rational(1, 2), 1]
_fits = [all(abs(float(c * (_r2 ** n - _r1 ** n)) - _Fib[n]) < 1e-9 for n in range(0, 10)) for c in _cs2]
assert _fits == [True, False, False, False]
_num(5, "ג", 2, _Fib[10]); assert _Fib[10] == 55
_nsteps(5, "ג", 3); _rubsum(5, "ג")
print("STEPS Q5c OK")
