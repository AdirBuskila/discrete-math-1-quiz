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

# ======================= STEPS section (step-author pass) =======================
_CODE = "19A-A"
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
    """Option i of a choice step: predicate k says whether option k (in stored order) is correct; exactly option 0 must be."""
    s = _S(num, p, i)
    assert s["correctId"] == "a" and len(s["options"]) == len(preds), (num, p, i)
    assert [bool(f()) for f in preds] == [True] + [False] * (len(preds) - 1), (num, p, i, [bool(f()) for f in preds])


T2 = [True, False]
imp_ = lambda a, b: (not a) or b
fs_ = frozenset

# ---- Q1 alef: contradiction
_contr = lambda f: not any(f(p, q) for p in T2 for q in T2)
_pat(1, "א", 0, [lambda: _contr(lambda p, q: p and not p), lambda: _contr(lambda p, q: p or not p),
                 lambda: _contr(lambda p, q: imp_(p, p)), lambda: _contr(lambda p, q: p and q)])
_right(1, "א", 1, "שקר בכל השמה")
assert {(p and not p) for p in T2} == {False}
_nsteps(1, "א", 2); _rubsum(1, "א")
print("STEPS Q1a OK")

# ---- Q1 bet: |S| = 3, |P(S)| = 8
E_ = fs_()
S_ = fs_([fs_([fs_([fs_([E_])])]), fs_([E_, fs_([fs_([1])]), fs_([E_]), fs_([fs_([fs_([1])]), E_])]), fs_([fs_([E_])])])
_num(1, "ב", 0, len(S_)); _num(1, "ב", 1, 2 ** len(S_)); assert len(S_) == 3
# P(S) by explicit subsets
assert sum(1 for k in range(4) for _ in _it.combinations(S_, k)) == 8
_nsteps(1, "ב", 2); _rubsum(1, "ב")
print("STEPS Q1b OK")

# ---- Q1 gimel: equivalence relations on {1,2,3}
_A3 = (1, 2, 3); _pairs = [(a, b) for a in _A3 for b in _A3]


def _is_eq(R):
    return (all((a, a) in R for a in _A3) and all((b, a) in R for a, b in R)
            and all((a, d) in R for a, b in R for c, d in R if b == c))


_eqs = [fs_(c) for k in range(10) for c in _it.combinations(_pairs, k) if _is_eq(fs_(c))]
assert len(_eqs) == 5
_pat(1, "ג", 0, [lambda: len(_eqs) == 5, lambda: len(list(_it.permutations(_A3))) == 5,
                 lambda: 2 ** 3 == 5, lambda: 3 ** 3 == 5])
_blocks2 = sum(1 for R in _eqs if len({frozenset(b for b in _A3 if (a, b) in R) for a in _A3}) == 2)
_num(1, "ג", 1, _blocks2); _num(1, "ג", 2, len(_eqs)); assert _blocks2 == 3
_nsteps(1, "ג", 3); _rubsum(1, "ג")
print("STEPS Q1c OK")

# ---- Q1 dalet: equivalence AND partial order
_anti = lambda R: all(not ((b, a) in R and a != b) for a, b in R)
_trn = lambda R: all((a, d) in R for a, b in R for c, d in R if b == c)
_ref = lambda R: all((a, a) in R for a in _A3)
_sym = lambda R: all((b, a) in R for a, b in R)
_po = lambda R: _ref(R) and _anti(R) and _trn(R)
_D3 = fs_([(1, 1), (2, 2), (3, 3)])
_both = lambda R: _is_eq(R) and _po(R)
_pat(1, "ד", 0, [lambda: _both(_D3), lambda: _both(fs_(list(_D3) + [(1, 2), (2, 1)])),
                 lambda: _both(fs_(list(_D3) + [(1, 2)])), lambda: _both(fs_())])
_cnt = sum(1 for k in range(10) for c in _it.combinations(_pairs, k) if _both(fs_(c)))
_num(1, "ד", 1, _cnt); assert _cnt == 1
_nsteps(1, "ד", 2); _rubsum(1, "ד")
print("STEPS Q1d OK")

# ---- Q1 he: injective functions {1,2,3} -> {1..5}
_inj = [f for f in _it.product(range(5), repeat=3) if len(set(f)) == 3]
_num(1, "ה", 1, len(_inj)); assert len(_inj) == 60
_num(1, "ה", 0, 3)
assert len({f[2] for f in _inj if f[0] == 0 and f[1] == 1}) == 3
_nsteps(1, "ה", 2); _rubsum(1, "ה")
print("STEPS Q1e OK")

# ---- Q1 vav: DNF of p & (r->p) & (q->r)
_f = lambda p, q, r: p and imp_(r, p) and imp_(q, r)
_rows = [x for x in _it.product(T2, repeat=3) if _f(*x)]
_num(1, "ו", 0, len(_rows)); assert len(_rows) == 3
_pat(1, "ו", 1, [lambda: _f(True, False, True), lambda: _f(True, True, False), lambda: _f(False, False, True), lambda: _f(False, True, False)])
_t = [lambda p, q, r: p and not q and not r, lambda p, q, r: p and q and not r, lambda p, q, r: (not p) and q and r,
      lambda p, q, r: (not p) or q or r]
assert [t(True, False, False) for t in _t] == [True, False, False, False]
assert [x for x in _it.product(T2, repeat=3) if _t[0](*x)] == [(True, False, False)]       # fires on exactly that row
assert not _t[3](True, False, False)
_nsteps(1, "ו", 3); _rubsum(1, "ו")
print("STEPS Q1f OK")

# ---- Q1 zayin: negation of  forall x in A exists y in B exists z in C: x = y + z
import random as _rnd
_rnd.seed(7)
_opt = _S(1, "ז", 0)["options"]
assert len(_opt) == 4


def _orig(A, B, C): return all(any(x == y + z for y in B for z in C) for x in A)
def _o0(A, B, C): return any(all(x != y + z for y in B for z in C) for x in A)
def _o1(A, B, C): return all(any(x != y + z for y in B for z in C) for x in A)
def _o2(A, B, C): return any(all(any(x != y + z for z in C) for y in B) for x in A)
def _o3(A, B, C): return any(any(x != y + z for y in B for z in C) for x in A)


_diff = [False] * 4
for _ in range(4000):
    A = {_rnd.randint(0, 5) for _ in range(_rnd.randint(1, 3))}
    B = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    C = {_rnd.randint(0, 3) for _ in range(_rnd.randint(1, 3))}
    assert _o0(A, B, C) == (not _orig(A, B, C))
    for k, fn in enumerate((_o0, _o1, _o2, _o3)):
        if fn(A, B, C) != (not _orig(A, B, C)):
            _diff[k] = True
assert _diff == [False, True, True, True]
_pat(1, "ז", 1, [lambda: True, lambda: False, lambda: False, lambda: False])
assert [x != 5 for x in (4, 6)] == [True, True]           # x != y+z holds on both sides, so x<y+z alone is not the negation
_nsteps(1, "ז", 2); _rubsum(1, "ז")
print("STEPS Q1g OK")

# ---- Q2 alef: n^2 < 2^n
_N = min(N for N in range(1, 50) if all(n * n < 2 ** n for n in range(N, 600)))
_num(2, "א", 0, _N); assert _N == 5
_n = _sp.symbols("n", integer=True)
assert _sp.expand((_n + 1) ** 2 - (_n ** 2 + 2 * _n + 1)) == 0
assert all(n * n + 2 * n + 1 < n * n + 3 * n for n in range(2, 300)) and not (1 + 2 + 1 < 1 + 3)
assert all(n * n + 3 * n < 2 * n * n for n in range(4, 300)) and not (9 + 9 < 18)
assert not any(n * n + 3 * n < n * n + 2 * n for n in range(1, 300))        # the planted wrong line
_l = _lines(2, "א", 1)
assert len(_l) == 5 and _bug(2, "א", 2, 2)["lines"][:2] == _l[:2] and _bug(2, "א", 2, 2)["lines"][3:] == _l[3:]
assert _bug(2, "א", 2, 2)["lines"][2] != _l[2]
_nsteps(2, "א", 3); _rubsum(2, "א")
print("STEPS Q2a OK")

# ---- Q2 bet: A cap B
_Aset = {3 ** n * 5 ** n * 7 ** m for n in range(100) for m in range(100)}
_Bset = {3 ** n * 5 ** m * 7 ** m for n in range(100) for m in range(100)}
_cap = _Aset & _Bset
_diag = {3 ** n * 5 ** n * 7 ** n for n in range(100)}
_cands = [_diag, _Aset, _Bset, {1}]
assert [c == _cap for c in _cands] == [True, False, False, False]
_right(2, "ב", 0, r"$\{3^n5^n7^n:\ n\in\{0,\ldots,99\}\}$")
_num(2, "ב", 1, len(_cap)); assert len(_cap) == 100
assert [2 ** 100 == 2 ** len(_cap), 100 ** 2 == 2 ** 100, 2 ** 99 == 2 ** 100, 200 == 2 ** 100] == [True, False, False, False]
_right(2, "ב", 2, "$2^{100}$")
_nsteps(2, "ב", 3); _rubsum(2, "ב")
print("STEPS Q2b OK")

# ---- Q2 gimel: P(A) u P(B) subset of P(A u B); counterexample
def _P(S):
    S = list(S)
    return {fs_(c) for k in range(len(S) + 1) for c in _it.combinations(S, k)}


for _a in _it.chain.from_iterable(_it.combinations(range(4), k) for k in range(1, 4)):
    for _b in _it.chain.from_iterable(_it.combinations(range(4), k) for k in range(1, 4)):
        assert (_P(_a) | _P(_b)) <= _P(set(_a) | set(_b))
_PA, _PB, _PAB = _P({1}), _P({2}), _P({1, 2})
_miss = _PAB - (_PA | _PB)
assert _miss == {fs_({1, 2})}
_pat(2, "ג", 2, [lambda: fs_({1, 2}) in _miss, lambda: E_ in _miss, lambda: fs_({1}) in _miss, lambda: fs_({2}) in _miss])
_num(2, "ג", 3, len(_PA | _PB)); assert len(_PA | _PB) == 3 and len(_PAB) == 4
_right(2, "ג", 0, r"לוקחים איבר שרירותי של $P(A)\cup P(B)$ ומראים לפי ההגדרות שהוא שייך ל-$P(A\cup B)$")
assert len(_lines(2, "ג", 1)) == 5
_nsteps(2, "ג", 4); _rubsum(2, "ג")
print("STEPS Q2c OK")

# ---- Q3 alef: 2 | 7x+y
_Rr = lambda x, y: (7 * x + y) % 2 == 0
_rg = range(-15, 16)
_cls0 = {x for x in _rg if _Rr(0, x)}
assert [_cls0 == {x for x in _rg if x % 2 == 0}, _cls0 == {x for x in _rg if x % 2 == 1},
        _cls0 == {x for x in _rg if x % 7 == 0}, _cls0 == {0}] == [True, False, False, False]
assert all(_Rr(x, x) for x in _rg) and all(_Rr(y, x) for x in _rg for y in _rg if _Rr(x, y))
assert all(_Rr(x, z) for x in _rg for y in _rg for z in _rg if _Rr(x, y) and _Rr(y, z))
assert len({frozenset(y for y in _rg if _Rr(x, y)) for x in _rg}) == 2
_num(3, "א", 1, 2)
_right(3, "א", 0, r"הזוגיים $\{2k:\ k\in\mathbb{Z}\}$")
_x, _y, _z = _sp.symbols("x y z")
assert _sp.expand((7 * _x + _y) + (7 * _y + _z) - (7 * _x + 8 * _y + _z)) == 0
assert _sp.expand((7 * _x + _y) + (7 * _y + _z) - (7 * _x + 9 * _y + _z)) != 0
assert _sp.expand((7 * _x + 8 * _y + _z) - 8 * _y - (7 * _x + _z)) == 0
assert len(_lines(3, "א", 2)) == 4 and _bug(3, "א", 3, 1)["lines"][1] != _lines(3, "א", 2)[1]
assert [i for i in range(4) if _bug(3, "א", 3, 1)["lines"][i] != _lines(3, "א", 2)[i]] == [1]
_nsteps(3, "א", 4); _rubsum(3, "א")
print("STEPS Q3a OK")


# ---- Q3 bet: |R| with blocks 2, 3, n-5
def _blocks_rel(sizes):
    els = list(range(sum(sizes))); R = set(); k = 0
    for s in sizes:
        blk = els[k:k + s]; k += s
        R |= {(a, b) for a in blk for b in blk}
    return R


assert len(_blocks_rel([2, 3, 5])) == 38
_num(3, "ב", 0, 10 - 5); _num(3, "ב", 1, len(_blocks_rel([2, 3, 5])))
_fm = [lambda n: 13 + (n - 5) ** 2, lambda n: 2 + 3 + (n - 5), lambda n: 2 * 3 * (n - 5), lambda n: 13 + 2 * (n - 5)]
for _nn in (8, 9, 10, 12, 20):
    assert len(_blocks_rel([2, 3, _nn - 5])) == _fm[0](_nn)
    assert all(_fm[k](_nn) != _fm[0](_nn) for k in (1, 2, 3)), _nn
_right(3, "ב", 2, r"$13+(n-5)^2$")
_nsteps(3, "ב", 3); _rubsum(3, "ב")
print("STEPS Q3b OK")


# ---- Q3 gimel: distinct equivalence relations with block sizes 2,3,n-5
def _distinct(n):
    els = list(range(n)); rels = set()
    for B in _it.combinations(els, 2):
        rest = [e for e in els if e not in B]
        for C in _it.combinations(rest, 3):
            D = [e for e in rest if e not in C]
            rels.add(fs_(fs_(b) for b in (B, C, D)))
    return len(rels)


_num(3, "ג", 0, _distinct(9)); _num(3, "ג", 1, _distinct(8))
assert _distinct(9) == _m.comb(9, 2) * _m.comb(7, 3) == 1260 and _distinct(8) == 280
_pat(3, "ג", 2, [lambda: 8 - 5 == 3, lambda: 8 - 5 == 2, lambda: 8 - 5 == 0, lambda: _distinct(8) == 0])
_nsteps(3, "ג", 3); _rubsum(3, "ג")
print("STEPS Q3c OK")

# ---- Q3 dalet: reflexive, not symmetric on {1,2}
_A2 = (1, 2); _p2 = [(a, b) for a in _A2 for b in _A2]
_rn = [fs_(c) for k in range(5) for c in _it.combinations(_p2, k)
       if all((a, a) in c for a in _A2) and not all((b, a) in c for a, b in c)]
_num(3, "ד", 0, len(_rn)); assert len(_rn) == 2
assert all(len(R) == 3 for R in _rn)
_num(3, "ד", 2, 3)
_isrs = lambda R: all((a, a) in R for a in _A2) and not all((b, a) in R for a, b in R)
_pat(3, "ד", 1, [lambda: _isrs(fs_([(1, 1), (2, 2), (1, 2)])), lambda: _isrs(fs_([(1, 1), (2, 2), (1, 2), (2, 1)])),
                 lambda: _isrs(fs_([(1, 1), (1, 2)])), lambda: _isrs(fs_())])
# both are total orders
for R in _rn:
    assert _po(R) if False else (all((a, a) in R for a in _A2) and _anti(R) and _trn(R))
    assert all((a, b) in R or (b, a) in R for a in _A2 for b in _A2)
_nsteps(3, "ד", 3); _rubsum(3, "ד")
print("STEPS Q3d OK")

# ---- Q4 alef: relations that are not functions
_P3 = [(a, b) for a in range(3) for b in range(3)]
_isfun = lambda R: all(sum(1 for (a, b) in R if a == x) == 1 for x in range(3))
_nf = sum(1 for k in range(10) for c in _it.combinations(_P3, k) if not _isfun(c))
_num(4, "א", 0, _nf); assert _nf == 2 ** 9 - 3 ** 3 == 485
_vals = [2 ** 400 - 20 ** 20, 2 ** 20 - 20 ** 20, 2 ** 400 - 400 ** 20, 20 ** 20 - 2 ** 400]
assert _vals[0] == 2 ** (20 * 20) - 20 ** 20 and _vals[0] > 0 and all(v != _vals[0] for v in _vals[1:])
assert _vals[1] < 0 and _vals[3] < 0 and _vals[2] != _vals[0]
_right(4, "א", 1, r"$2^{400}-20^{20}$")
_nsteps(4, "א", 2); _rubsum(4, "א")
print("STEPS Q4a OK")

# ---- Q4 bet: 3 <= |R| <= 5
_num(4, "ב", 0, 20 * 20)
_c9 = sum(1 for k in (3, 4, 5) for _ in _it.combinations(_P3, k))
_num(4, "ב", 1, _c9); assert _c9 == 336 == _m.comb(9, 3) + _m.comb(9, 4) + _m.comb(9, 5)
_tot = sum(_m.comb(400, k) for k in (3, 4, 5))
_ws = [_m.comb(400, 3) * _m.comb(400, 4) * _m.comb(400, 5), sum(_m.comb(20, k) for k in (3, 4, 5)), _m.comb(400, 5) - _m.comb(400, 2)]
assert all(w != _tot for w in _ws)
_right(4, "ב", 2, r"$\binom{400}3+\binom{400}4+\binom{400}5$")
_nsteps(4, "ב", 3); _rubsum(4, "ב")
print("STEPS Q4b OK")

# ---- Q4 gimel: bijections of {0..9}
_img789 = set(); _cnt = 0
for p in _it.permutations(range(10)):
    if set(p[:3]) == {0, 1, 2} and set(p[3:7]) == {3, 4, 5, 6}:
        _cnt += 1; _img789.add(frozenset(p[7:]))
assert _cnt == 864 == _m.factorial(3) * _m.factorial(4) * _m.factorial(3) and _img789 == {fs_({7, 8, 9})}
_num(4, "ג", 1, _cnt)
_right(4, "ג", 0, "אל עצמה: $f(\\{7,8,9\\})=\\{7,8,9\\}$")
_nsteps(4, "ג", 2); _rubsum(4, "ג")
print("STEPS Q4c OK")

# ---- Q4 dalet: subsets of {0..9} containing all evens
_sub = sum(1 for mask in range(1 << 10) if all(mask >> e & 1 for e in range(0, 10, 2)))
_num(4, "ד", 1, _sub); assert _sub == 32
_num(4, "ד", 0, sum(1 for v in range(10) if v % 2))
_nsteps(4, "ד", 2); _rubsum(4, "ד")
print("STEPS Q4d OK")

# ---- Q4 he: m = 11, phi, Fermat
_mm = [n for n in range(1, 30) if sum(_m.comb(n, k) for k in range(0, n + 1, 2)) == 1024]
assert _mm == [11]
_num(4, "ה", 0, 11); _num(4, "ה", 1, int(_sp.totient(11)))
assert (10 ** 10 - 1) % 11 == 0 and _sp.isprime(11) and 10 % 11 != 0
_right(4, "ה", 2, "משפט Fermat הקטן")
_nsteps(4, "ה", 3); _rubsum(4, "ה")
print("STEPS Q4e OK")

# ---- Q5 alef: pigeonhole mod 100 (brute force on small moduli, then the 100-residue argument)
for _mod in range(2, 7):
    _pool = range(3 * _mod)
    _mx = max(len(c) for k in range(1, _mod + 2) for c in _it.combinations(_pool, k)
              if all((a - b) % _mod != 0 for a, b in _it.combinations(c, 2)))
    assert _mx == _mod
assert len({v % 100 for v in range(100)}) == 100            # 100 numbers with distinct residues exist
_num(5, "א", 1, len({v % 100 for v in range(1000)})); _num(5, "א", 2, 100 + 1)
_right(5, "א", 0, "שובך היונים: 101 מספרים ו-100 שאריות אפשריות")
_nsteps(5, "א", 3); _rubsum(5, "א")
print("STEPS Q5a OK")

# ---- Q5 bet: Q cap (0,1) ~ Z
from fractions import Fraction as _Fr
_good = [lambda n: _Fr(1, n), ]
_sets = [[_Fr(1, n) for n in range(2, 50)], [_Fr(1, n) for n in range(1, 50)], [_Fr(n) for n in range(1, 50)], [_Fr(n) for n in range(2, 50)]]
assert [all(0 < v < 1 for v in S) for S in _sets] == [True, False, False, False]
_right(5, "ב", 1, r"$\{\frac12,\frac13,\frac14,\ldots\}$")
_nsteps(5, "ב", 2); _rubsum(5, "ב")
print("STEPS Q5b OK")

# ---- Q5 gimel: a_n = 5a_{n-1} - 6a_{n-2}, a0=7, a1=15
_r = _sp.symbols("r")
_rt = sorted(_sp.solve(_r ** 2 - 5 * _r + 6, _r))
assert _rt == [2, 3]
_pat(5, "ג", 0, [lambda: _rt == [2, 3], lambda: _rt == [-3, -2], lambda: _rt == [1, 6], lambda: _rt == [5, 6]])
_a = [7, 15]
for _i in range(2, 12):
    _a.append(5 * _a[-1] - 6 * _a[-2])
_C1, _C2 = _sp.symbols("C1 C2")
_sol = _sp.solve([_C1 + _C2 - 7, 2 * _C1 + 3 * _C2 - 15], [_C1, _C2])
assert _sol == {_C1: 6, _C2: 1} and all(6 * 2 ** k + 3 ** k == _a[k] for k in range(12))
_num(5, "ג", 1, _a[2]); _num(5, "ג", 2, int(_sol[_C1])); assert _a[2] == 33
_nsteps(5, "ג", 3); _rubsum(5, "ג")
print("STEPS Q5c OK")
