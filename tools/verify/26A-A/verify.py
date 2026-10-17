# Checks of the official 26A-A answers (pure python + sympy). ASCII output only.
import itertools, math
from sympy import isprime, factorial, summation, symbols, Rational, gcd as sgcd, gcdex

# Q1a truth table
rows = list(itertools.product([True, False], repeat=3))
assert all((not (((p or q) and ((not p) or r)))) or (q or r) for p, q, r in rows)
print("Q1a tautology OK")
# Q1b algebra: m composite -> 2^m-1 composite (small m), and the factorisation identity
for n in range(2, 8):
    for q in range(n, 12):
        m = n * q
        assert (2 ** m - 1) % (2 ** q - 1) == 0 and 1 < 2 ** q - 1 < 2 ** m - 1
print("Q1b factor identity OK (primality of M136279841 is the given premise, not checked)")
# Q1c / Q2c(1): all equivalence relations on {1,2,3} and on 4 elements; intersection = identity
def partitions(s):
    if not s:
        yield []
        return
    f, rest = s[0], s[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[f] + p[i]] + p[i + 1:]
        yield [[f]] + p
for n in (3, 5, 6):
    A = list(range(n))
    inter = None
    for P in partitions(A):
        R = {(a, b) for blk in P for a in blk for b in blk}
        inter = R if inter is None else inter & R
    assert inter == {(a, a) for a in A}
print("Q1c intersection of all equivalence relations = identity OK (n=3,5,6)")
# Q2a telescoping
from fractions import Fraction
for n in range(2, 60):
    assert sum(Fraction(1, k * (k + 1)) for k in range(1, n)) == Fraction(n - 1, n)
print("Q2a identity OK n=2..59")
# Q2b
S = {'a', 'b', 'c', 'd', 'e', 'f'}
cnt = 0
for bits in itertools.product([0, 1], repeat=6):
    B = {x for x, b in zip(sorted(S), bits) if b}
    if B & {'a', 'b'} == {'a'}:
        cnt += 1
assert cnt == 16
print("Q2b = 16 OK")
# Q2c(1): reflexive+symmetric+antisymmetric on {1,2,3} -> identity; sym diff transitive
U = [(a, b) for a in range(1, 4) for b in range(1, 4)]
def refl(R): return all((a, a) in R for a in range(1, 4))
def sym(R): return all((b, a) in R for a, b in R)
def anti(R): return all(not ((a, b) in R and (b, a) in R and a != b) for a, b in R)
def trans(R): return all((a, d) in R for a, b in R for c, d in R if b == c)
good = []
for bits in itertools.product([0, 1], repeat=9):
    R = {u for u, b in zip(U, bits) if b}
    if refl(R) and sym(R) and anti(R):
        good.append(R)
assert all(trans(R1 ^ R2) for R1 in good for R2 in good)
print("Q2c(1) true OK, relations:", len(good))
# Q2c(2): total orders on {1,2}
U2 = [(a, b) for a in (1, 2) for b in (1, 2)]
def total(R, n=2):
    return refl2(R) and anti(R) and trans(R) and all((a, b) in R or (b, a) in R for a in range(1, n + 1) for b in range(1, n + 1))
def refl2(R): return all((a, a) in R for a in (1, 2))
orders = []
for bits in itertools.product([0, 1], repeat=4):
    R = {u for u, b in zip(U2, bits) if b}
    if total(R): orders.append(R)
assert len(orders) == 2 and not total(orders[0] | orders[1])
print("Q2c(2) false OK")
# Q3a: classes mod 5, equivalence, not antisymmetric
Z = range(-30, 31)
R = lambda x, y: (4 * x + y) % 5 == 0
assert all(R(x, x) for x in Z)
assert all(R(y, x) for x in Z for y in Z if R(x, y))
assert all(R(x, z) for x in range(-12, 13) for y in range(-12, 13) for z in range(-12, 13) if R(x, y) and R(y, z))
for r in range(5):
    assert all(R(r, y) == (y % 5 == r) for y in Z) if r else all(R(0, y) == (y % 5 == 0) for y in Z)
assert R(0, 5) and R(5, 0)
print("Q3a classes [r]={5k+r} OK, not antisymmetric OK")
# Q3b
assert math.gcd(49, 84) == 7 and 49 * -5 + 84 * 3 == 7
def ext(a, b):
    if b == 0: return a, 1, 0
    d, x1, y1 = ext(b, a % b)
    return d, y1, x1 - y1 * (a // b)
print("Q3b ext euclid:", ext(49, 84))
rows_t = [(49, 84), (84, 49), (49, 35), (35, 14), (14, 7), (7, 0)]
assert [ext(a, b)[1:] for a, b in rows_t] == [(-5, 3), (3, -5), (-2, 3), (1, -2), (0, 1), (1, 0)]
assert [a // b if b else None for a, b in rows_t][:5] == [0, 1, 1, 2, 2]
print("Q3b table rows OK")
# Q3c / Q4a brute force on subsets of {0,1,2}
def subs(s): return [frozenset(c) for r in range(len(s) + 1) for c in itertools.combinations(s, r)]
U3 = [0, 1, 2]
for A in subs(U3):
    for B in subs(U3):
        for C in subs(U3):
            assert ((B - A) | (C - A)) <= ((B | C) - A)
def pw(X): return set(subs(sorted(X)))
for A in subs(U3):
    for B in subs(U3):
        if A and B:
            lhs = pw(A) | pw(B) == pw(A | B)
            assert lhs == (A <= B or B <= A)   # both the claim and its converse
print("Q3c and Q4a OK")
# Q4b
assert {math.gcd(12, x) for x in range(1, 2000)} == {1, 2, 3, 4, 6, 12}
print("Q4b image OK")
# Q4c
assert not any(isprime(p) and isprime(p * p + 3 * p + 2) for p in range(2, 20000))
print("Q4c no prime OK; p=2 gives", 4 + 6 + 2)
# Q5a
a, b = 36 ** 36 + math.factorial(36), 7 ** 72 - 1
assert a % 74 == 0 and b % 74 == 0 and math.gcd(a, b) >= 74
print("Q5a gcd =", math.gcd(a, b), ">= 74 OK; 37 prime", isprime(37), 49 % 37 != 0, 36 % 37 != 0)
# Q5b
f = lambda x: (x + 1, 2 * x + 5)
vals = [f(x) for x in range(-500, 500)]
assert len(set(vals)) == len(vals) and (1, 1) not in vals
print("Q5b 1-1 and (1,1) not hit OK")
# Q5c: nothing to compute (cardinality argument)
print("ALL OK")

# ======================= STEPS section: guided-step values (numeric answers, false findbug lines) =======================
import json, pathlib
from sympy import symbols, simplify, expand, solve, Eq, Rational
from fractions import Fraction

EXPECT_NUM = {}   # question id -> numeric step answers, in step order
BUG_IDX = {}      # question id -> bugIndex

# Q1a: antecedent true in 4 rows, consequent false in 2, implication false in 0
ant = lambda p, q, r: (p or q) and ((not p) or r)
cons = lambda p, q, r: q or r
assert sum(1 for p, q, r in rows if ant(p, q, r)) == 4
assert sum(1 for p, q, r in rows if not cons(p, q, r)) == 2
assert sum(1 for p, q, r in rows if ant(p, q, r) and not cons(p, q, r)) == 0
EXPECT_NUM["26A-A-Q1a"] = [4, 2, 0]

# Q1b: (2^6-1)/(2^3-1) = 9; the bugged factor (2^q+1) is not a divisor/identity, the true one is
assert (2 ** 6 - 1) % (2 ** 3 - 1) == 0 and (2 ** 6 - 1) // (2 ** 3 - 1) == 9
x = symbols("x")
for n_ in range(2, 7):
    assert expand((x - 1) * sum(x ** i for i in range(n_))) == x ** n_ - 1          # true line
    assert expand((x + 1) * sum(x ** i for i in range(n_))) != x ** n_ - 1          # bugged line is false
EXPECT_NUM["26A-A-Q1b"] = [9]; BUG_IDX["26A-A-Q1b"] = 2

# Q1c: identity is contained in every equivalence relation (n=4, all 15 partitions), the converse inclusion fails
A4 = list(range(4))
ident = {(a, a) for a in A4}
rels = [{(a, b) for blk in P for a in blk for b in blk} for P in partitions(A4)]
assert len(rels) == 15 and all(ident <= R for R in rels)
assert not any(R <= ident for R in rels if R != ident)          # "identity contains every equivalence relation" is false
assert len({(k, k) for k in range(1, 11)}) == 10
EXPECT_NUM["26A-A-Q1c"] = [10]; BUG_IDX["26A-A-Q1c"] = 1

# Q2a: n=4 sum = 3/4; the bugged numerator (k-1)(k+1)-1 breaks the identity
k = symbols("k", positive=True)
assert sum(Fraction(1, i * (i + 1)) for i in range(1, 4)) == Fraction(3, 4)
assert simplify((k - 1) / k + 1 / (k * (k + 1)) - ((k - 1) * (k + 1) + 1) / (k * (k + 1))) == 0
assert simplify((k - 1) / k + 1 / (k * (k + 1)) - ((k - 1) * (k + 1) - 1) / (k * (k + 1))) != 0
assert simplify(((k - 1) * (k + 1) + 1) - k ** 2) == 0
EXPECT_NUM["26A-A-Q2a"] = [0.75]; BUG_IDX["26A-A-Q2a"] = 3

# Q2b: 4 free letters, 16 subsets
free = [c for c in "abcdef" if c not in "ab"]
assert len(free) == 4 and 2 ** len(free) == cnt == 16
EXPECT_NUM["26A-A-Q2b"] = [4, 16]

# Q2c: exactly one refl+sym+antisym relation on {1,2,3}; two total orders on {1,2}; union reflexive but not antisymmetric
assert len(good) == 1
assert len(orders) == 2
Ru = orders[0] | orders[1]
assert refl2(Ru) and not anti(Ru)
EXPECT_NUM["26A-A-Q2c"] = [1, 2]; BUG_IDX["26A-A-Q2c"] = 2

# Q3a: 5 classes mod 5, [4] = residue 4, symmetric-sum identity (true) vs 6x+5y (false)
xx, yy = symbols("xx yy")
assert expand((4 * xx + yy) + (4 * yy + xx) - 5 * (xx + yy)) == 0
assert expand((4 * xx + yy) + (4 * yy + xx) - (6 * xx + 5 * yy)) != 0
Zr = range(-60, 61)
assert len({frozenset(y for y in Zr if R(x_, y)) for x_ in Zr}) == 5
assert all(R(4, y) == (y % 5 == 4) for y in Zr)
zz = symbols("zz")
assert expand((4 * xx + yy) + (4 * yy + zz) - ((4 * xx + zz) + 5 * yy)) == 0   # transitivity line is right
EXPECT_NUM["26A-A-Q3a"] = [5, 4]; BUG_IDX["26A-A-Q3a"] = 1

# Q3b: Euclid divisions and coefficients
seq, a_, b_ = [], 84, 49
while b_:
    seq.append((a_, a_ // b_, b_, a_ % b_)); a_, b_ = b_, a_ % b_
assert seq == [(84, 1, 49, 35), (49, 1, 35, 14), (35, 2, 14, 7), (14, 2, 7, 0)], seq
assert 84 % 49 == 35 and math.gcd(49, 84) == 7 and 49 * -5 + 84 * 3 == 7
EXPECT_NUM["26A-A-Q3b"] = [35, 7, -5]

# Q3c: example sizes; bugged middle step ((B and C) and not A) is not implied
A_, B_, C_ = {1, 2, 3}, {3, 4, 5}, {5, 6}
assert (B_ - A_) | (C_ - A_) == (B_ | C_) - A_ == {4, 5, 6}
cex = [(Aa, Bb, Cc) for Aa in subs(U3) for Bb in subs(U3) for Cc in subs(U3)
       if not ((Bb - Aa) | (Cc - Aa)) <= ((Bb & Cc) - Aa)]
assert cex                                                       # bugged line really fails
EXPECT_NUM["26A-A-Q3c"] = [3]; BUG_IDX["26A-A-Q3c"] = 3

# Q4a: |P(A u B)| - |P(A) u P(B)| = 2 for {1,2},{2,3}; "{a,b} not subset of A  <=>  {a,b} not in P(A)" for a in A\B, b in B\A
Pa, Pb = pw({1, 2}), pw({2, 3})
assert len(pw({1, 2, 3})) == 8 and len(Pa | Pb) == 6 and len(pw({1, 2, 3})) - len(Pa | Pb) == 2
for Aa in subs(U3):
    for Bb in subs(U3):
        for a_e in Aa - Bb:
            for b_e in Bb - Aa:
                s_ = frozenset({a_e, b_e})
                assert s_ in pw(Aa | Bb) and s_ not in pw(Aa) and s_ not in pw(Bb)   # true line; bugged line says "in P(A)"
EXPECT_NUM["26A-A-Q4a"] = [2]; BUG_IDX["26A-A-Q4a"] = 3

# Q4b
assert len([d for d in range(1, 13) if 12 % d == 0]) == 6 and math.gcd(12, 8) == 4
EXPECT_NUM["26A-A-Q4b"] = [6, 4]

# Q4c: p=2 -> 12; odd p -> p+3 even (the bugged line claims odd)
assert 2 ** 2 + 3 * 2 + 2 == 12
assert all((p + 3) % 2 == 0 and (p * (p + 3)) % 2 == 0 for p in range(3, 2000, 2))
EXPECT_NUM["26A-A-Q4c"] = [12]; BUG_IDX["26A-A-Q4c"] = 1

# Q5a: Fermat/Wilson remainders and the bugged decomposition
assert pow(7, 72, 37) == 1 and math.factorial(36) % 37 == 36 and pow(36, 36, 37) == 1
assert 36 ** 36 + math.factorial(36) == (36 ** 36 - 1) + (math.factorial(36) + 1) - 0
assert (36 ** 36 - 1) + (math.factorial(36) - 1) != 36 ** 36 + math.factorial(36)
assert (math.factorial(36) - 1) % 37 != 0
assert math.gcd(36 ** 36 + math.factorial(36), 7 ** 72 - 1) % 74 == 0
EXPECT_NUM["26A-A-Q5a"] = [1, 36]; BUG_IDX["26A-A-Q5a"] = 2

# Q5b
assert f(0) == (1, 5) and solve(Eq(2 * x + 5, 1), x) == [-2] and solve(Eq(2 * x + 5, 1), x) != [-3]
EXPECT_NUM["26A-A-Q5b"] = [5]; BUG_IDX["26A-A-Q5b"] = 2

# Q5c: 1+1/n (n>=2) are distinct rationals in [1,2) -> infinite subset; Z intersect R = Z
seqq = [1 + Fraction(1, n_) for n_ in range(2, 3000)]
assert len(set(seqq)) == len(seqq) and all(1 <= v < 2 for v in seqq)
BUG_IDX["26A-A-Q5c"] = 1

# ---- cross-check against the generated raw JSON ----
raw = json.loads((pathlib.Path(__file__).resolve().parents[2] / "raw" / "26A-A.json").read_text(encoding="utf-8"))
for q in raw["questions"]:
    qid = "26A-A-Q%d%s" % (q["num"], "abcdefghij"["אבגדהוזחטי".index(q["part"])])
    st = q.get("steps", [])
    nums = [s["answer"] for s in st if s["type"] == "numeric"]
    assert nums == EXPECT_NUM.get(qid, []), (qid, nums, EXPECT_NUM.get(qid))
    bugs = [s["bugIndex"] for s in st if s["type"] == "findbug"]
    if qid in BUG_IDX:
        assert bugs == [BUG_IDX[qid]], (qid, bugs)
    elif qid != "26A-A-Q1a":
        assert not bugs, qid
    for s in st:
        if s["type"] == "choice":
            assert s["correctId"] in [o["id"] for o in s["options"]]
print("STEPS: numeric answers and findbug indices verified against raw JSON for", len(raw["questions"]), "items")
print("ALL STEPS OK")
