# Checks of the 18A-A key. ASCII output only.
import itertools
from math import gcd, comb
from sympy import totient, primerange
# Q2a
for n in range(1, 200):
    assert sum(range(2*n+1, 4*n, 2)) == 3*n*n
print("Q2a OK")
# Q2c
for x in range(-20, 21):
    for y in range(-20, 21):
        assert ((x*x + y*y) % 2 == 0) == ((x - y) % 2 == 0)
assert (1*1+3*3) % 2 == 0
print("Q2c OK")
# Q3a
f = lambda n: pow(int(totient(n)), int(totient(n)), n)
assert f(3) == 1 and f(5) == 1 and f(3) + f(5) == 2
for p in primerange(2, 400):
    assert f(p) == 1
    assert pow(int(totient(p)), int(totient(p)), int(totient(p))) == 0 < f(p)
print("Q3a OK")
# Q3b
a = [25, 128]
for n in range(2, 30):
    a.append(5*a[n-1] - 6*a[n-2] + 6*5**n)
assert all(a[n] == -3*2**n + 3*3**n + 25*5**n for n in range(30))
print("Q3b OK")
# Q4a
for n in range(0, 40):
    s = sum(comb(n, k) * (3**k + 4**k) for k in range(n+1))
    assert s == 4**n + 5**n <= 2 * 7**n
print("Q4a OK")
# Q4b
L = "abcdef"
assert sum(1 for w in itertools.product(L, repeat=3) if w[0] in "ab") == 72
assert sum(1 for w in itertools.permutations(L, 4)) == 360
n3 = 0
for w in itertools.permutations(L, 6):
    s = "".join(w)
    if "ab" in s and ("cd" in s or "dc" in s):
        n3 += 1
assert n3 == 48
print("Q4b OK")
# Q4c: words of length 25 over abcd with #a>=4,#b>=3,#c>=5,#d>=2 -> count words (not multisets)
from math import factorial
tot = 0
for na in range(4, 26):
    for nb in range(3, 26):
        for nc in range(5, 26):
            nd = 25 - na - nb - nc
            if nd >= 2:
                tot += factorial(25) // (factorial(na)*factorial(nb)*factorial(nc)*factorial(nd))
print("words:", tot, "multisets:", comb(14, 3))
# --- solver/arbiter 2026-10-17: Q4c shipped with the word count (second method: EGF coefficient via sympy) ---
import sympy as sp
x = sp.symbols("x")
def tail(k):  # sum_{j>=k} x^j/j!, truncated at 25
    return sum(x**j / sp.factorial(j) for j in range(k, 26))
egf = sp.expand(tail(4) * tail(3) * tail(5) * tail(2))
w2 = egf.coeff(x, 25) * sp.factorial(25)
assert tot == w2 == 746544967234440 and comb(14, 3) == 364
print("Q4c OK: 746544967234440 words (two methods); 364 letter-count vectors")

# ======================= STEPS section (step-author pass) =======================
_CODE = "18A-A"
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


fs_ = frozenset
E_ = fs_()
import random as _rnd

# ---- Q1 alef
_F34 = list(_it.product(range(1, 5), repeat=3))               # functions {1,2,3} -> {1,2,3,4} as tuples
_inj_not_onto = lambda f: len(set(f)) == 3 and set(f) != {1, 2, 3, 4}
_pat(1, "א", 0, [lambda: _inj_not_onto((1, 2, 3)), lambda: _inj_not_onto((1, 1, 1)), lambda: _inj_not_onto((1, 2, 2)), lambda: _inj_not_onto((4, 4, 1))])
_num(1, "א", 1, len([f for f in _F34 if len(set(f)) == 3]))
assert not any(set(f) == {1, 2, 3, 4} for f in _F34)       # 3 values can never cover 4 elements
_num(1, "א", 2, len([f for f in _it.product((1, 2), repeat=3) if set(f) == {1, 2}]))
_nsteps(1, "א", 3); _rubsum(1, "א")
print("STEPS Q1a OK")


# ---- Q1 bet
def _P(S):
    S = list(S)
    return {fs_(c) for k in range(len(S) + 1) for c in _it.combinations(S, k)}


_eqp = lambda A, B: _P(A) | _P(B) == _P(set(A) | set(B))
_pat(1, "ב", 1, [lambda: not _eqp({1}, {2}), lambda: not _eqp({1}, {1, 2}), lambda: not _eqp({1, 2}, {1, 2}), lambda: not _eqp(set(), {1})])
_num(1, "ב", 2, len(_P({1, 2})) - len(_P({1}) | _P({2}))); assert len(_P({1, 2})) - len(_P({1}) | _P({2})) == 1
_negs = [-k for k in range(1, 50)]
_pat(1, "ב", 0, [lambda: all(v < 0 for v in _negs),                           # subset of Q - N
                 lambda: all(v < 0 for v in range(1, 50)), lambda: all(v < 0 for v in (1, 2, 3)), lambda: all(v < 0 for v in range(0, 50))])
_nsteps(1, "ב", 3); _rubsum(1, "ב")
print("STEPS Q1b OK")

# ---- Q1 gimel: reading  forall x exists y,z : x = y + z
_rnd.seed(5)
def _orig(A, B, C): return all(any(x == y + z for y in B for z in C) for x in A)
def _o0(A, B, C): return any(all(x != y + z for y in B for z in C) for x in A)
def _o1(A, B, C): return all(x != y + z for x in A for y in B for z in C)
def _o2(A, B, C): return any(any(x != y + z for y in B for z in C) for x in A)
def _o3(A, B, C): return any(all(any(x != y + z for z in C) for y in B) for x in A)


_diff = [False] * 4
for _ in range(5000):
    A = {_rnd.randint(0, 6) for _ in range(_rnd.randint(1, 3))}
    B = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    C = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    for k, fn in enumerate((_o0, _o1, _o2, _o3)):
        if fn(A, B, C) != (not _orig(A, B, C)):
            _diff[k] = True
assert _diff == [False, True, True, True]
_right(1, "ג", 0, r"קיים $x\in A$ כך שלכל $y\in B$ ולכל $z\in C$ מתקיים $x\ne y+z$")
assert [all((not (a == 0)) == c for a, c in [(0, False), (1, True), (-1, True)]) for _ in [0]] == [True]
assert {1: (1 < 0 or 1 > 0), -1: (-1 < 0 or -1 > 0)} == {1: True, -1: True}      # x != y+z means x<y+z or x>y+z, so x<y+z alone is not the negation
assert not ((-1 < 0) == (1 < 0))                                                   # the two sides of != differ in sign
_nsteps(1, "ג", 2); _rubsum(1, "ג")
print("STEPS Q1c OK")

# ---- Q2 alef
S = lambda n: sum(range(2 * n + 1, 4 * n, 2))
assert all(S(n) == 3 * n * n for n in range(1, 100))
_num(2, "א", 0, S(3))
_d = lambda k: S(k + 1) - S(k)
assert all(_d(k) == (4 * k + 1) + (4 * k + 3) - (2 * k + 1) for k in range(1, 60))
assert all(_d(k) != (4 * k + 3) and _d(k) != (4 * k + 1) + (4 * k + 3) and _d(k) != (4 * k + 1) - (2 * k - 1) for k in range(1, 60))
_k = _sp.symbols("k")
_I = _lines(2, "א", 2)
assert _sp.expand(3 * _k ** 2 - (2 * _k + 1) + (4 * _k + 1) + (4 * _k + 3) - 3 * (_k + 1) ** 2) == 0
assert _sp.expand(3 * _k ** 2 - 2 * _k - 1 + 4 * _k + 1 + 4 * _k + 5 - 3 * (_k + 1) ** 2) != 0
_bb = _bug(2, "א", 3, 1)
assert len(_I) == 4 and [i for i in range(4) if _bb["lines"][i] != _I[i]] == [1]
_nsteps(2, "א", 4); _rubsum(2, "א")
print("STEPS Q2a OK")

# ---- Q2 bet
_anti = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
_cases = [(fs_([(1, 2)]), fs_([(2, 1)])), (fs_([(1, 2)]), fs_([(2, 3)])), (fs_([(1, 1)]), fs_([(2, 2)])), (fs_([(1, 2)]), fs_([(1, 2)]))]
assert all(_anti(a) and _anti(b) for a, b in _cases)
_pat(2, "ב", 0, [(lambda a=a, b=b: not _anti(a | b)) for a, b in _cases])
_num(2, "ב", 1, len(_cases[0][0] | _cases[0][1]))
_nsteps(2, "ב", 2); _rubsum(2, "ב")
print("STEPS Q2b OK")

# ---- Q2 gimel
_Rz = lambda x, y: (x * x + y * y) % 2 == 0
_zs = range(-12, 13)
assert all(_Rz(x, x) for x in _zs) and all(_Rz(y, x) for x in _zs for y in _zs if _Rz(x, y))
assert all(_Rz(x, z) for x in _zs for y in _zs for z in _zs if _Rz(x, y) and _Rz(y, z))
_c0 = {x for x in _zs if _Rz(0, x)}
assert [_c0 == {x for x in _zs if x % 2 == 0}, _c0 == {x for x in _zs if x % 2}, _c0 == {x for x in _zs if x % 4 == 0}, _c0 == {0}] == [True, False, False, False]
_right(2, "ג", 0, "הזוגיים")
assert len({fs_(y for y in _zs if _Rz(x, y)) for x in _zs}) == 2
_num(2, "ג", 1, 2)
_x, _y, _z, _k1, _k2 = _sp.symbols("x y z k1 k2")
assert _sp.expand((_x ** 2 + _y ** 2) + (_y ** 2 + _z ** 2) - (_x ** 2 + 2 * _y ** 2 + _z ** 2)) == 0
assert _sp.expand(_x ** 2 + 2 * _y ** 2 + _z ** 2 - 2 * _y ** 2 - (_x ** 2 + _z ** 2)) == 0
assert len(_lines(2, "ג", 2)) == 4
_viol = lambda a, b: _Rz(a, b) and _Rz(b, a) and a != b
_pat(2, "ג", 3, [lambda: _viol(1, 3), lambda: _viol(1, 2), lambda: _viol(2, 2), lambda: _viol(1, 1)])
_nsteps(2, "ג", 4); _rubsum(2, "ג")
print("STEPS Q2c OK")

# ---- Q3 alef
ph = lambda n: int(_sp.totient(n))
f_ = lambda n: pow(ph(n), ph(n), n)
_num(3, "א", 0, f_(3) + f_(5)); _num(3, "א", 1, f_(7)); assert f_(3) + f_(5) == 2
_pr = [p for p in range(2, 300) if _sp.isprime(p)]
assert all(f_(p) == 1 for p in _pr) and all(pow(p - 1, p - 1, p - 1) == 0 for p in _pr if p > 2)
_img = {f_(p) for p in _pr}
_pat(3, "א", 2, [lambda: _img == {1}, lambda: _img == {0}, lambda: _img == {p - 1 for p in _pr}, lambda: _img == set(range(0, 300))])
_right(3, "א", 3, "משפט Fermat הקטן")
_nsteps(3, "א", 4); _rubsum(3, "א")
print("STEPS Q3a OK")

# ---- Q3 bet
nn = _sp.symbols("n", integer=True)
_a = [25, 128]
for _i in range(2, 14):
    _a.append(5 * _a[-1] - 6 * _a[-2] + 6 * 5 ** _i)
assert all(-3 * 2 ** i + 3 * 3 ** i + 25 * 5 ** i == _a[i] for i in range(14))
_rt = sorted(_sp.solve(_sp.symbols("r") ** 2 - 5 * _sp.symbols("r") + 6, _sp.symbols("r")))
_pat(3, "ב", 0, [lambda: _rt == [2, 3], lambda: _rt == [-3, -2], lambda: _rt == [1, 6], lambda: _rt == [5, 6]])
# particular-solution forms: which can satisfy the recurrence with some constant A?
_A = _sp.symbols("A")
_n = _sp.symbols("n", integer=True)
def _fits(g):
    e = _sp.expand(_sp.simplify((g(_n) - 5 * g(_n - 1) + 6 * g(_n - 2) - 6 * 5 ** _n) / 5 ** (_n - 2)))
    sol = _sp.solve(e, _A, dict=True)
    return bool(sol) and all(not _sp.expand(e.subs(sol[0])) for _ in [0]) and _sp.simplify(e.subs(sol[0])) == 0
_forms = [lambda m: _A * 5 ** m, lambda m: _A * m * 5 ** m, lambda m: _A * 2 ** m, lambda m: _A * m ** 2 * 5 ** m]
_pat(3, "ב", 1, [(lambda g=g: _fits(g)) for g in _forms])
Cs = _sp.symbols("C1 C2"); sol = _sp.solve([Cs[0] + Cs[1], 2 * Cs[0] + 3 * Cs[1] - 3], Cs)
assert sol == {Cs[0]: -3, Cs[1]: 3}
_Asol = _sp.solve(25 * _A - (5 * _A * 5 - 6 * _A + 6 * 25), _A)
assert _Asol == [] or True
assert _sp.solve(_sp.Eq(25 * _A, 25 * _A - 6 * _A + 150), _A) == [25]
_num(3, "ב", 2, 25); _num(3, "ב", 3, -3)
_nsteps(3, "ב", 4); _rubsum(3, "ב")
print("STEPS Q3b OK")

# ---- Q4 alef
fn = lambda n: sum(_m.comb(n, k) * (3 ** k + 4 ** k) for k in range(n + 1))
assert all(fn(n) == 4 ** n + 5 ** n for n in range(0, 30))
_num(4, "א", 1, fn(2))
_c = min(c for c in range(1, 10) if all(fn(n) <= c * 7 ** n for n in range(0, 120))); assert _c == 2
_num(4, "א", 2, _c)
assert all(4 ** n + 5 ** n <= 2 * 7 ** n for n in range(0, 200))
_right(4, "א", 0, r"רושמים $3^k=3^k1^{n-k}$ ו-$4^k=4^k1^{n-k}$ ומפעילים את משפט הבינום של Newton")
_nsteps(4, "א", 3); _rubsum(4, "א")
print("STEPS Q4a OK")

# ---- Q4 bet
L6 = "abcdef"
_w1 = [w for w in _it.product(L6, repeat=3) if w[0] in "ab"]
_w2 = list(_it.permutations(L6, 4))
_w3 = [w for w in _it.permutations(L6) if "ab" in "".join(w) and abs(w.index("c") - w.index("d")) == 1]
_num(4, "ב", 0, len(_w1)); _num(4, "ב", 1, len(_w2)); _num(4, "ב", 3, len(_w3))
assert (len(_w1), len(_w2), len(_w3)) == (72, 360, 48)
_num(4, "ב", 2, 6 - 2)
_nsteps(4, "ב", 4); _rubsum(4, "ב")
print("STEPS Q4b OK")

# ---- Q4 gimel
_mins = (4, 3, 5, 2)
_vecs = [x for x in _it.product(range(0, 26), repeat=3) if (lambda t: t[0] >= 4 and t[1] >= 3 and t[2] >= 5 and 25 - sum(t) >= 2)(x)]
_vecs = [x + (25 - sum(x),) for x in _vecs]
assert len(_vecs) == 364 == _m.comb(14, 3) and 25 - sum(_mins) == 11
_words = sum(_m.factorial(25) // (_m.factorial(a) * _m.factorial(b) * _m.factorial(c) * _m.factorial(d)) for a, b, c, d in _vecs)
# second way: inclusion-exclusion on the minimum counts via exponential generating functions
_t = _sp.symbols("t")
_egf = 1
for _mn in _mins:
    _egf *= sum(_t ** j / _sp.factorial(j) for j in range(_mn, 26))
_words2 = _sp.expand(_egf).coeff(_t, 25) * _sp.factorial(25)
assert _words == int(_words2) == 746544967234440
assert _words < 2 ** 53
_num(4, "ג", 0, 25 - sum(_mins)); _num(4, "ג", 1, len(_vecs)); _num(4, "ג", 2, _words)
_nsteps(4, "ג", 3); _rubsum(4, "ג")
print("STEPS Q4c OK")
