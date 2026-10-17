# Checks of the official 25A-B answers. ASCII output only.
import itertools
from math import gcd, factorial

imp = lambda a, b: (not a) or b
T = [True, False]
rows = list(itertools.product(T, repeat=3))
# Q1a CNF
S = lambda p, q, r: imp(p or (not q), r)
cnf = lambda p, q, r: ((not p) or (not q) or r) and ((not p) or q or r) and (p or q or r)
assert all(S(*x) == cnf(*x) for x in rows)
assert [x for x in rows if not S(*x)] == [(True, True, False), (True, False, False), (False, False, False)]
print("Q1a OK")
# Q1b
n = sum(1 for m in range(1 << 10) if m & 3 == 3)
assert n == 256
print("Q1b", n)
# Q1c
assert {gcd(12, x) for x in range(1, 500)} == {1, 2, 3, 4, 6, 12}
print("Q1c OK")
# Q2a
assert all((23 ** n - 1) % 11 == 0 for n in range(1, 100))
print("Q2a OK")
# Q2b
A = {5 ** n * 7 ** m for m in range(10) for n in range(10)}
B = {5 ** n for n in range(10)}
C = {7 ** n for n in range(10)}
assert len(A) == 100 and len(B | C) == 19
print("Q2b 2^119 OK")
# Q2c on P({1..4})
subs = [frozenset(c) for k in range(5) for c in itertools.combinations([1, 2, 3, 4], k)]
Rr = lambda b, c: (1 in b) == (1 in c)
assert all(Rr(b, b) for b in subs)
assert all(Rr(c, b) for b in subs for c in subs if Rr(b, c))
assert all(Rr(b, d) for b in subs for c in subs for d in subs if Rr(b, c) and Rr(c, d))
assert len({frozenset(c for c in subs if Rr(b, c)) for b in subs}) == 2
print("Q2c OK")
# Q3a
A = [1, 2, 3, 6, 8, 9, 16, 18]
R = {(x, y) for x in A for y in A if y % x == 0}
assert all((x, x) in R for x in A)
assert all(not ((y, x) in R and x != y) for x, y in R)
assert all((x, z) in R for x, y in R for y2, z in R if y == y2)
assert (2, 3) not in R and (3, 2) not in R
print("Q3a OK")
# Q3b
assert -84 + 2 * 48 == 12 == gcd(48, 84)
print("Q3b OK")
# Q4b
g = gcd(5 ** 44 - 1, 8 ** 88 + factorial(22))
assert g > 19 and g % 23 == 0
print("Q4b OK")


# =====================================================================================
# STEPS section: every numeric answer, choice key and findbug line used by gen_25A-B.py
# =====================================================================================
import itertools as _it
from math import gcd as _gcd, factorial as _fac
import sympy as sp
from sympy.logic.boolalg import Equivalent, And, Or, Not, Implies, simplify_logic
from sympy import symbols as _syms

EXPECT_NUM = {}
BUG_IDX = {}
_imp = lambda a, b: (not a) or b
_rows3 = list(_it.product([True, False], repeat=3))

# Q1a
_F = lambda p, q, r: _imp(p or (not q), r)
_false_rows = [rw for rw in _rows3 if not _F(*rw)]
assert _false_rows == [(True, True, False), (True, False, False), (False, False, False)]
_p, _q, _r = _syms("p q r")
_phi = Implies(Or(_p, Not(_q)), _r)
_good = And(Or(Not(_p), Not(_q), _r), Or(Not(_p), _q, _r), Or(_p, _q, _r))
assert simplify_logic(Equivalent(_phi, _good)) == True
_c = Or(_p, _q, Not(_r))
assert _c.subs({_p: True, _q: True, _r: False}) == True   # p v q v ~r is true at TTF (wrong clause)
assert Or(Not(_p), Not(_q), _r).subs({_p: True, _q: True, _r: False}) == False
for bad in [And(Or(_p, _q, Not(_r)), Or(_p, Not(_q), Not(_r)), Or(Not(_p), Not(_q), Not(_r))),
            Or(And(Not(_p), Not(_q), _r), And(Not(_p), _q, _r), And(_p, _q, _r)),
            And(Or(Not(_p), Not(_q), _r), Or(Not(_p), _q, _r))]:
    assert simplify_logic(Equivalent(_phi, bad)) != True
EXPECT_NUM["25A-B-Q1a"] = [3]

# Q1b
_cnt = sum(1 for bits in _it.product([0, 1], repeat=10) if bits[0] and bits[1])
assert _cnt == 256 == 2 ** len(range(3, 11)) and len(range(3, 11)) == 8
EXPECT_NUM["25A-B-Q1b"] = [8, 256]

# Q1c
assert _gcd(12, 8) == 4
assert {_gcd(12, x) for x in range(1, 2001)} == {1, 2, 3, 4, 6, 12}
assert 5 not in {_gcd(12, x) for x in range(1, 2001)}
EXPECT_NUM["25A-B-Q1c"] = [4, 6]

# Q2a
assert 23 ** 2 - 1 == 528 == 23 * 22 + 22 == 11 * 48
_k = sp.symbols("k")
assert sp.expand(23 * 23 ** _k - 23 + 22 - (23 * (23 ** _k - 1) + 2 * 11)) == 0
assert sp.expand(23 * 23 ** _k - 23 + 22 - (23 * (23 ** _k - 1) + 3 * 11)) != 0
assert all((23 ** n - 1) % 11 == 0 for n in range(1, 60))
EXPECT_NUM["25A-B-Q2a"] = [528]; BUG_IDX["25A-B-Q2a"] = 2

# Q2b
_A = {5 ** n * 7 ** m for m in range(10) for n in range(10)}
_B = {5 ** n for n in range(10)}; _C = {7 ** n for n in range(10)}
assert len(_A) == 100 and len(_B | _C) == 19 and _B & _C == {1} and len(_B) == len(_C) == 10
assert 100 + 19 == 119
EXPECT_NUM["25A-B-Q2b"] = [100, 19, 119]

# Q2c
def _subsets(n):
    return [frozenset(i for i in range(1, n + 1) if bits[i - 1]) for bits in _it.product([0, 1], repeat=n)]
_PA = _subsets(10)
_cls = {}
for X in _PA:
    _cls.setdefault(X & {1}, []).append(X)
assert len(_cls) == 2 and set(_cls) == {frozenset(), frozenset({1})}
assert len(_cls[frozenset()]) == 512 == 2 ** 9
assert all((X & {1}) <= {1} for X in _PA) and not any((X & {1}) == frozenset({1, 2}) for X in _PA)
EXPECT_NUM["25A-B-Q2c"] = [2, 512]; BUG_IDX["25A-B-Q2c"] = 3

# Q3a
_AA = [1, 2, 3, 6, 8, 9, 16, 18]
assert sum(1 for x in _AA for y in _AA if y % x == 0) == 25
_inc = [(x, y) for x in _AA for y in _AA if y % x and x % y]
assert (2, 3) in _inc
for x, y in [(2, 6), (3, 18), (1, 16)]:
    assert y % x == 0
assert -3 % 3 == 0 and 3 % -3 == 0            # divisibility over Z is not antisymmetric
_s, _t, _x = sp.symbols("s t x")
assert sp.expand(_t * (_s * _x) - (_t * _s) * _x) == 0 and sp.expand(_t * (_s * _x) - (_t + _s) * _x) != 0
EXPECT_NUM["25A-B-Q3a"] = [25]; BUG_IDX["25A-B-Q3a"] = 2

# Q3b
assert 84 % 48 == 36 and _gcd(48, 84) == 12
assert [48 * x + 84 * y for x, y in [(2, -1), (-1, 2), (1, -1), (-2, 1)]] == [12, 120, -36, -12]
EXPECT_NUM["25A-B-Q3b"] = [36, 12]

# Q3c
assert len((({2, 3} - {1, 2}) | ({1, 4, 5} - {1, 2}))) == 3
for ax, bx, cx in _it.product([True, False], repeat=3):
    assert (((bx and not ax) or (cx and not ax)) == ((bx or cx) and not ax))
assert any(((bx or cx) and not ax) and not ((bx and cx) and not ax) for ax, bx, cx in _it.product([True, False], repeat=3))
EXPECT_NUM["25A-B-Q3c"] = [3]; BUG_IDX["25A-B-Q3c"] = 2

# Q4a
_n, _tt = sp.symbols("n tt")
assert sp.solve(sp.Eq(4 * _tt ** 2, 2 * _n ** 2), _n ** 2)[0] == 2 * _tt ** 2
assert sp.solve(sp.Eq(4 * _tt ** 2, 2 * _n ** 2), _n ** 2)[0] != 4 * _tt ** 2
EXPECT_NUM["25A-B-Q4a"] = []; BUG_IDX["25A-B-Q4a"] = 2

# Q4b
assert pow(5, 44, 23) == 1 and _fac(22) % 23 == 22
_both = [p for p in sp.primerange(2, 60) if (5 ** 44 - 1) % p == 0 and (8 ** 88 + _fac(22)) % p == 0]
assert 23 in _both and [p for p in _both if p > 19] == [23]
for pp in (29, 31, 37):
    assert not ((5 ** 44 - 1) % pp == 0 and (8 ** 88 + _fac(22)) % pp == 0)
assert _gcd(5 ** 44 - 1, 8 ** 88 + _fac(22)) > 19
EXPECT_NUM["25A-B-Q4b"] = [1, 22]; BUG_IDX["25A-B-Q4b"] = 1

# Q4c
_U = _subsets(4)
_ok = lambda A, B, C: ((A & B) | C) == (A & (B | C))
for A in _U:
    for B in _U:
        for C in _U:
            if A and B and C:
                assert _ok(A, B, C) == (C <= A)
                # correct contrapositive: C not<= A -> unequal  (follows); distractors false:
# distractor "C not<= A -> equal" is false: such cases exist and they are unequal
assert not any((not C <= A) and _ok(A, B, C) for A in _U for B in _U for C in _U if A and B and C)
assert any((not C <= A) for A in _U for B in _U for C in _U if A and B and C)
# distractor "C <= A -> unequal" is false: such cases exist and are equal
assert any((C <= A) and _ok(A, B, C) for A in _U for B in _U for C in _U if A and B and C)
# distractor "A not<= C -> unequal" is false: A={1,2}, C={1}? C<=A so equal
assert any((not A <= C) and _ok(A, B, C) for A in _U for B in _U for C in _U if A and B and C)
assert len(({1, 2} & {2, 3}) | {3}) == 2 and len({1, 2} & ({2, 3} | {3})) == 1
EXPECT_NUM["25A-B-Q4c"] = [2]; BUG_IDX["25A-B-Q4c"] = 1

# ---- cross-check against the generated raw JSON ----
import json as _json, pathlib as _pl
_raw = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / "25A-B.json").read_text(encoding="utf-8"))
_n = 0
for _q in _raw["questions"]:
    _qid = "25A-B-Q%d%s" % (_q["num"], "abcdefghij"["אבגדהוזחטי".index(_q["part"])])
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
