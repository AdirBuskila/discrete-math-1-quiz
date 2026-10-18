# Checks of the 23A-B keys. ASCII output only.
import itertools, math
from math import gcd, factorial
# Q1a
for p,q,r in itertools.product([0,1],repeat=3):
    imp=lambda a,b:(not a) or b
    assert imp(p,q or r)==(imp(p,q) or imp(p,r))
print("Q1a OK")
# Q1b: counterexample not transitive
R2={(1,1),(2,2),(3,3),(1,2),(2,1)}; R1={(1,1),(2,2),(3,3),(2,3),(3,2)}
U=R1|R2
assert (1,2) in U and (2,3) in U and (1,3) not in U
print("Q1b OK")
# Q1c: f(m,n)=2^n(2m+1) hits every 1..N
seen={2**n*(2*m+1) for m in range(0,3000) for n in range(0,14)}
assert all(k in seen for k in range(1,2000))
print("Q1c OK")
# Q2b extended euclid
def eg(a,b):
    if b==0: return a,1,0
    d,x,y=eg(b,a%b); return d,y,x-(a//b)*y
assert 3*55+(-4)*40==5 and 3*55+4*(-40)==5 and gcd(55,-40)==5
print("Q2b OK", eg(55,40))
# Q2c: two distinct total orders on {1,2}, union equivalence? refuted by given example
Rr1={(1,1),(2,2),(1,2)}; Rr2={(1,1),(2,2),(2,1)}
assert Rr1|Rr2=={(1,1),(2,2),(1,2),(2,1)} and Rr1&Rr2=={(1,1),(2,2)}
print("Q2c OK")
# Q3b
A={5**m*9**n for m in range(10) for n in range(10)}
B={5**m*7**n for m in range(10) for n in range(10)}
assert len(A)==100 and len(B)==100 and len(A&B)==10 and len(A|B)==190
print("Q3b OK: 10 + 2^190 + 2^10000")
# Q3c
assert gcd(81**11-1, factorial(22)+24)%46==0
print("Q3c OK")
# Q4a
R=lambda x,y:(x+5*y)%3==0
rng=range(-20,21)
assert all(R(x,x) for x in rng)
assert all(R(y,x) for x in rng for y in rng if R(x,y))
assert all(R(x,z) for x in range(-9,10) for y in range(-9,10) for z in range(-9,10) if R(x,y) and R(y,z))
assert R(0,3) and R(3,0)
assert all((R(x,0))==(x%3==0) and R(x,1)==(x%3==1) and R(x,2)==(x%3==2) for x in rng)
print("Q4a OK")
# Q4b
def lcm(a,b): return abs(a*b)//gcd(a,b) if a and b else 0
for n in range(0,200):
    v=lcm(n-1,n+1)
    if n==0: assert v==1
    elif n==1: assert v==0
    elif n==2: assert v==3
    elif n%2==0: assert v==n*n-1
    else: assert v==(n*n-1)//2
print("Q4b OK")
# Q4c brute force small n
for n in range(1,6):
    full=set(range(1,2*n+2)); odds={x for x in full if x%2}
    cnt=0
    for mask in range(1<<(2*n+1)):
        Bs={i+1 for i in range(2*n+1) if mask>>i&1}
        if Bs|odds==full: cnt+=1
    assert cnt==2**(n+1)
print("Q4c OK")

# ======================= STEPS section (step-author pass) =======================
_CODE = "23A-B"
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


# ---- Q1a: truth table
_rows = list(_it.product([True, False], repeat=3))
_imp = lambda a, b: (not a) or b
_f1 = [(p, q, r) for p, q, r in _rows if not _imp(p, q or r)]
assert len(_rows) - len(_f1) == 7 and _f1 == [(True, False, False)]
assert all(_imp(p, q or r) == (_imp(p, q) or _imp(p, r)) for p, q, r in _rows)
assert not all(_imp(p, q or r) for p, q, r in _rows) and any(_imp(p, q or r) for p, q, r in _rows)
_num(1, "a", 0, 7); _right(1, "a", 1, r"$p=T,\ q=F,\ r=F$"); _nsteps(1, "a", 3)
_w = {(True, True, False), (True, False, True), (False, False, False)}
assert all(_imp(p, q or r) for p, q, r in _w)
print("STEPS Q1a OK")

# ---- Q1b: counterexample
_D = {(1, 1), (2, 2), (3, 3)}
_R2 = _D | {(1, 2), (2, 1)}; _R1 = _D | {(2, 3), (3, 2)}
def _is_eq(R, A=(1, 2, 3)):
    return (all((a, a) in R for a in A) and all((b, a) in R for a, b in R)
            and all((a, d) in R for a, b in R for c, d in R if b == c))
assert _is_eq(_R1) and _is_eq(_R2) and _R1 != _R2
_U = _R1 | _R2
assert len(_U) == 7 and not _is_eq(_U)
assert all((a, a) in _U for a in (1, 2, 3)) and all((b, a) in _U for a, b in _U)   # refl, sym hold
assert (1, 2) in _U and (2, 3) in _U and (1, 3) not in _U
_num(1, "b", 0, 7); _right(1, "b", 1, "טרנזיטיביות"); _nsteps(1, "b", 3)
print("STEPS Q1b OK")

# ---- Q1c
_f = lambda m, n: 2**n * (2 * m + 1)
assert _f(3, 2) == 28 and _f(2, 3) == 40
assert [(m, n) for m in range(0, 60) for n in range(0, 10) if _f(m, n) == 40] == [(2, 3)]
assert [(m, n) for m in range(0, 60) for n in range(0, 10) if _f(m, n) == 45] == [(22, 0)]
assert sorted(_f(m, n) for m in range(0, 200) for n in range(0, 9) if _f(m, n) <= 300) == list(range(1, 301))  # bijective
# solution preimages: q=2^a1*(2m+1) -> f(m,a1)=q; odd q -> f(m,0)=q (the key had the coordinates swapped)
assert all(_f(((q >> ((q & -q).bit_length() - 1)) - 1) // 2, (q & -q).bit_length() - 1) == q for q in range(1, 500))
assert all(_f((q - 1) // 2, 0) == q for q in range(1, 500, 2))
_num(1, "c", 1, 28); _num(1, "c", 2, 2); _right(1, "c", 3, "$(22,0)$"); _nsteps(1, "c", 4)
print("STEPS Q1c OK")

# ---- Q2a
_k = _sp.symbols("k", positive=True)
assert sum(_sp.Rational(1, i * (i + 1)) for i in range(1, 3)) == _sp.Rational(2, 3)
assert _sp.expand((_k - 1) * (_k + 1) + 1) == _k**2 and _sp.expand((_k - 1) * (_k + 1) + 1) != _k**2 - 1
_a1 = (_k - 1) / _k + 1 / (_k * (_k + 1)); _a2 = ((_k - 1) * (_k + 1) + 1) / (_k * (_k + 1))
_a3 = _k**2 / (_k * (_k + 1)); _a4 = _k / (_k + 1)
assert _sp.simplify(_a1 - _a2) == 0 and _sp.simplify(_a2 - _a3) == 0 and _sp.simplify(_a3 - _a4) == 0
assert _sp.simplify((_k**2 - 1) / (_k * (_k + 1)) - _a4) != 0       # findbug line really is wrong
for _n in range(2, 40):
    assert sum(_sp.Rational(1, i * (i + 1)) for i in range(1, _n)) == _sp.Rational(_n - 1, _n)
_num(2, "a", 1, 0.667, 0.001); assert abs(2 / 3 - 0.667) <= 0.001
_right(2, "a", 0, "$n=2$"); _right(2, "a", 2, "$k^2$")
_o = _lines(2, "a", 3); _b = _S(2, "a", 4)
assert len(_o) == 4 and sum(1 for x, y in zip(_o, _b["lines"]) if x != y) == 1 and _o[_b["bugIndex"]] != _b["lines"][_b["bugIndex"]]
_nsteps(2, "a", 5)
print("STEPS Q2a OK")

# ---- Q2b
def _eg(a, b):
    if b == 0: return a, 1, 0
    d, x, y = _eg(b, a % b); return d, y, x - (a // b) * y
assert math.gcd(55, -40) == 5 and _eg(55, 40)[0] == 5
_seq = []; _a, _b2 = 55, 40
while _b2: _seq.append((_a, _b2, _a // _b2, _a % _b2)); _a, _b2 = _b2, _a % _b2
assert _seq == [(55, 40, 1, 15), (40, 15, 2, 10), (15, 10, 1, 5), (10, 5, 2, 0)]
assert _lines(2, "b", 1) == [r"$55=1\cdot40+15$", r"$40=2\cdot15+10$", r"$15=1\cdot10+5$", r"$10=2\cdot5+0$"]
assert [(x, y) for x, y in [(3, 4), (3, -4), (4, 3), (-3, 4)] if 55 * x + (-40) * y == 5] == [(3, 4)]
_num(2, "b", 0, 5); _right(2, "b", 2, "$(3,4)$"); _nsteps(2, "b", 3)
print("STEPS Q2b OK")

# ---- Q2c
_P = [(a, b) for a in (1, 2) for b in (1, 2)]
_tot = []
for _m in range(16):
    R = {_P[i] for i in range(4) if _m >> i & 1}
    refl = all((a, a) in R for a in (1, 2)); anti = all(not ((a, b) in R and (b, a) in R and a != b) for a, b in _P)
    trans = all((a, d) in R for a, b in R for c, d in R if b == c); total = all((a, b) in R or (b, a) in R for a, b in _P)
    if refl and anti and trans and total: _tot.append(R)
assert len(_tot) == 2
_u = _tot[0] | _tot[1]; _i = _tot[0] & _tot[1]
assert len(_u) == 4 and _is_eq(_u, (1, 2)) and _is_eq(_i, (1, 2))
_num(2, "c", 0, 2); _num(2, "c", 1, 4); _nsteps(2, "c", 3)
print("STEPS Q2c OK")

# ---- Q3a
_pw = lambda s: [set(c) for r in range(len(s) + 1) for c in _it.combinations(s, r)]
for _A in _pw(range(4)):
    for _B in _pw(range(4)):
        for _C in _pw(range(4)):
            assert (_B | _C) - _A <= (_B - _A) | (_C - _A)
_nsteps(3, "a", 3)
print("STEPS Q3a OK")

# ---- Q3b
_A = {5**m * 9**n for m in range(10) for n in range(10)}; _B = {5**m * 7**n for m in range(10) for n in range(10)}
assert len(_A & _B) == 10 and len(_A | _B) == 190 and len(_A) * len(_B) == 10000
_num(3, "b", 0, 10); _num(3, "b", 1, 190); _num(3, "b", 2, 10000); _right(3, "b", 3, "$10+2^{190}+2^{10000}$"); _nsteps(3, "b", 4)
print("STEPS Q3b OK")

# ---- Q3c
assert 81**11 == 9**22 and _sp.factorial(22) % 23 == 22 and (_sp.factorial(22) + 24) % 23 == 0 and (81**11 - 1) % 46 == 0
_num(3, "c", 1, 22); _num(3, "c", 2, 22); _num(3, "c", 3, 0); _nsteps(3, "c", 4)
print("STEPS Q3c OK")

# ---- Q4a
_x, _y, _z = _sp.symbols("x y z")
assert _sp.expand((_x + 5 * _y) + (_y + 5 * _x) - 6 * (_x + _y)) == 0
assert all(_sp.expand((_x + 5 * _y) + (_y + 5 * _x) - c * (_x + _y)) != 0 for c in (4, 5))
assert _sp.expand((_x + 5 * _y) + (_y + 5 * _z) - (_x + 5 * _z + 6 * _y)) == 0
_R = lambda a, b: (a + 5 * b) % 3 == 0
_rg = range(-12, 13)
assert all(_R(a, a) for a in _rg) and all(_R(b, a) for a in _rg for b in _rg if _R(a, b))
assert all(_R(a, c) for a in _rg for b in _rg for c in _rg if _R(a, b) and _R(b, c))
assert _R(0, 3) and _R(3, 0)
assert len({frozenset(b for b in _rg if _R(a, b)) for a in _rg}) == 3
_num(4, "a", 0, 3); _right(4, "a", 1, "$6(x+y)$"); _nsteps(4, "a", 4)
print("STEPS Q4a OK")

# ---- Q4b
_lcm = lambda a, b: abs(a * b) // math.gcd(a, b) if a and b else 0
assert all(math.gcd(n - 1, n + 1) in (1, 2) for n in range(0, 300))
assert _lcm(6, 8) == 24 == (49 - 1) // 2 and _lcm(7, 9) == 63 == 64 - 1
assert all(_lcm(n - 1, n + 1) == (n * n - 1) // 2 for n in range(3, 300, 2))
_num(4, "b", 1, 24); _num(4, "b", 2, 63); _right(4, "b", 0, "$1$ או $2$"); _right(4, "b", 3, r"$\frac{n^2-1}{2}$"); _nsteps(4, "b", 4)
print("STEPS Q4b OK")

# ---- Q4c
_n = 6; _full = set(range(1, 2 * _n + 2)); _odds = {v for v in _full if v % 2}; _cnt = 0
for _mask in range(1 << (2 * _n + 1)):
    if {i + 1 for i in range(2 * _n + 1) if _mask >> i & 1} | _odds == _full: _cnt += 1
assert len(_odds) == 7 and _cnt == 128
_num(4, "c", 0, 7); _num(4, "c", 1, 128); _nsteps(4, "c", 3)
print("STEPS Q4c OK")
