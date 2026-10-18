# Checks of the 18B-A key. ASCII output only.
import itertools
from math import comb, gcd
from sympy import totient, isprime, primerange
# Q1a: A1xB1 != B1xA1 for {1},{2}; A2xB2 = B2xA2 for {1},{}
prod = lambda A, B: {(a, b) for a in A for b in B}
assert prod({1}, {2}) != prod({2}, {1})
assert prod({1}, set()) == prod(set(), {1}) == set()
print("Q1a OK")
# Q1b2: |B|<|A|, P(AuB)=P(A)uP(B) => B subset A  (all small finite A,B)
subsets = lambda S: {frozenset(c) for r in range(len(S) + 1) for c in itertools.combinations(sorted(S), r)}
U = range(1, 6)
for a in subsets(set(U)):
    for b in subsets(set(U)):
        if len(b) < len(a) and subsets(a | b) == subsets(a) | subsets(b):
            assert b <= a
# the key's witness when B is not inside A
assert frozenset({1, 2}) in subsets({1, 2}) and frozenset({1, 2}) not in subsets({1}) | subsets({2})
print("Q1b OK")
# Q2a1, Q2a2
for n in range(1, 300):
    assert sum(range(1, 4*n - 2, 4)) == n*(2*n - 1)
    assert n**3 < 10**n
for k in range(1, 300):
    assert k*(2*k - 1) + 4*k + 1 == (k+1)*(2*k + 1)
    assert (k+1)**3 <= 8*k**3 < 10*k**3
print("Q2a OK")
# Q2b1, Q2b2
a = [0, 3]
for n in range(2, 40):
    a.append(7*a[n-1] - 12*a[n-2] - 6)
assert all(a[n] == 4**n - 1 for n in range(40))
assert [n for n in range(0, 40) if isprime(a[n])] == [1]
assert all(a[n] % 3 == 0 and a[n] > 3 for n in range(2, 40))
print("Q2b OK")
# Q2c
for n in range(0, 40):
    s = sum(comb(n, k) * (2**k * 3**k + 5**n) for k in range(n + 1))
    assert s == 7**n + 10**n <= 2 * 10**n <= 2 * 11**n
print("Q2c OK")
# Q3a
assert totient(1) == totient(2) == 1
good = [n for n in range(1, 3000) if isprime(n) and isprime(int(totient(n)))]
assert good == [3]
print("Q3a OK")
# Q3b: R on {1,2}, reflexive, not symmetric -> total order
A = [1, 2]
pairs = [(x, y) for x in A for y in A]
cnt = 0
for r in range(len(pairs) + 1):
    for c in itertools.combinations(pairs, r):
        R = set(c)
        refl = all((x, x) in R for x in A)
        sym = all((y, x) in R for (x, y) in R)
        if refl and not sym:
            cnt += 1
            anti = all(not ((x, y) in R and (y, x) in R) or x == y for x in A for y in A)
            trans = all((a, d) in R for (a, b) in R for (c2, d) in R if b == c2)
            total = all((x, y) in R or (y, x) in R for x in A for y in A)
            assert anti and trans and total
assert cnt == 2
print("Q3b OK")
# Q3c
for x in range(-40, 41):
    assert (x*x + x) % 2 == 0
    for y in range(-40, 41):
        assert ((x*x + y) % 2 == 0) == ((x + y) % 2 == 0)
assert (2*2 + 4) % 2 == 0 and (4*4 + 2) % 2 == 0
print("Q3c OK")
# Q4a: subsets of odd size of a 100-set: 2^99; sum |B| = 100*2^99 (small analog check n=10)
for n in range(1, 16):
    m = sum(comb(n, k) for k in range(1, n + 1, 2))
    s = sum(k * comb(n, k) for k in range(n + 1))
    assert m == 2**(n-1) and s == n * 2**(n-1) and m + s == (n + 1) * 2**(n-1)
assert sum(comb(100, k) for k in range(1, 101, 2)) + sum(k*comb(100, k) for k in range(101)) == 101 * 2**99
print("Q4a OK")
# Q4b: permutations of 1..7 mapping {1,2,3} onto itself
n4 = sum(1 for p in itertools.permutations(range(1, 8)) if {p[0], p[1], p[2]} == {1, 2, 3})
assert n4 == 144 == 6 * 24
print("Q4b OK")
# Q4c: multisets of size 18 over a,b,c with #a>=5,#b>=3,#c>=7 (order irrelevant)
n5 = sum(1 for x in range(5, 19) for y in range(3, 19) for z in range(7, 19) if x + y + z == 18)
assert n5 == 10 == comb(5, 2)
print("Q4c OK")
# Q4d
n = gcd(11, 70**10 - 1)
assert n == 11
v = int(totient(int(totient(n + n*n))))
assert n + n*n == 132 and totient(132) == 40 and v == 16 and v % 8 == 0
print("Q4d OK")

# ================= step checks (ai-draft steps); every numeric step answer is tied to tools/raw/18B-A.json =================
import json, pathlib
import sympy as sp
from math import factorial
RAW = json.loads((pathlib.Path(__file__).resolve().parents[2] / "raw" / "18B-A.json").read_text(encoding="utf-8"))
def item(num, part):
    return [q for q in RAW["questions"] if q["num"] == num and q.get("part") == part][0]
def numerics(num, part):
    return [s["answer"] for s in item(num, part)["steps"] if s["type"] == "numeric"]
def step(num, part, typ):
    return [s for s in item(num, part)["steps"] if s["type"] == typ][0]
phi = lambda m: int(totient(m))
# Q1a: wrong definitions differ from AxB; pair choice has exactly one pair with AxB = BxA among the options
defs = {"and": lambda A, B: {(a, b) for a in A for b in B},
        "or": lambda A, B: {(a, b) for a in A | B for b in A | B if a in A or b in B},
        "unordered": lambda A, B: {frozenset((a, b)) for a in A for b in B},
        "swapped": lambda A, B: {(b, a) for a in A for b in B}}
A_, B_ = {1}, {2}
assert defs["or"](A_, B_) != defs["and"](A_, B_) and defs["unordered"](A_, B_) != defs["and"](A_, B_) and defs["swapped"](A_, B_) != defs["and"](A_, B_)
opts_ = [({1}, set()), ({1}, {2}), ({1, 2}, {1}), ({1}, {1, 2})]
assert [prod(a, b) == prod(b, a) for a, b in opts_] == [True, False, False, False]
assert numerics(1, "א") == [len(prod({1}, {2}) | prod({2}, {1}))] == [2]
# Q1b: statement 2 on all pairs from {1..5} with 2<|B|<|A| (rechecked), and the buggy line is false
sub = subsets(set(range(1, 6)))
cnt = 0
for a in sub:
    for b in sub:
        if 2 < len(b) < len(a) and subsets(a | b) == subsets(a) | subsets(b):
            assert b < a; cnt += 1
assert cnt > 0
for a in sub:
    for b in sub:
        for x in a - b:
            for y in b - a:
                S = frozenset({x, y})
                assert S in subsets(a | b) and S not in subsets(a) | subsets(b)
assert step(1, "ב", "findbug")["bugIndex"] == 3
# Q1c: negation (reading: exists a pair (x,y)); official vs distractors on all small A,B,C incl. empty
def orig(A, B, C): return any(all(x <= y + z for z in C) for x in A for y in B)
def negs(A, B, C):
    return {"official": all(any(x > y + z for z in C) for x in A for y in B),
            "exists-exists": any(all(x > y + z for z in C) for x in A for y in B),
            "forall-all": all(all(x > y + z for z in C) for x in A for y in B),
            "forall-exists-exists": all(any(any(x > y + z for z in C) for y in B) for x in A),
            ">=": all(any(x >= y + z for z in C) for x in A for y in B),
            "<": all(any(x < y + z for z in C) for x in A for y in B),
            "!=": all(any(x != y + z for z in C) for x in A for y in B)}
bad = {k: False for k in negs([1], [1], [1])}
univ = [0, 1, 2, 3]
for ra in range(4):
    for rb in range(4):
        for rc in range(4):
            for A in itertools.combinations(univ, ra):
                for B in itertools.combinations(univ, rb):
                    for C in itertools.combinations(univ, rc):
                        n = negs(A, B, C); o = orig(A, B, C)
                        assert n["official"] == (not o)
                        for k, v in n.items():
                            if v != (not o): bad[k] = True
assert all(v for k, v in bad.items() if k != "official"), bad
print("Q1c OK")
# Q2a
k = sp.symbols("k")
assert numerics(2, "א") == [3*(2*3 - 1) + 4*3 + 1, min(c for c in range(1, 100) if all((m + 1)**3 <= c * m**3 for m in range(1, 3000)))] == [28, 8]
assert (3 + 1) * (2*3 + 1) == 28
assert sp.simplify(sp.powsimp(10 * 10**k) - 10**(k + 1)) == 0 and sp.simplify(10 * 10**k - 10**(k + 2)) != 0
for m in range(1, 200):
    assert (m + 1)**3 <= 8 * m**3 < 10 * m**3
assert step(2, "א", "findbug")["bugIndex"] == 4
# Q2b
r = sp.symbols("r")
assert sorted(sp.solve(r**2 - 7*r + 12, r)) == [3, 4] and max(sp.solve(r**2 - 7*r + 12, r)) == 4
A_s = sp.symbols("A")
assert sp.solve(sp.Eq(A_s, 7*A_s - 12*A_s - 6), A_s) == [-1]
seq = [0, 3]
for m in range(2, 10): seq.append(7*seq[m-1] - 12*seq[m-2] - 6)
assert numerics(2, "ב") == [4, -1, seq[3]] == [4, -1, 63] and seq[2] == 15 == 4**2 - 1
# Q2c
assert numerics(2, "ג") == [sum(comb(3, j) * (2**j * 3**j + 5**3) for j in range(4)),
                            min(c for c in range(1, 20) if all(7**m + 10**m <= c * 11**m for m in range(1, 300)))] == [1343, 2]
assert sp.Rational(7 + 10, 11) < 2 and sp.Rational(17, 11) > 1
# Q3a
assert phi(1) == phi(2) == 1
assert numerics(3, "א") == [phi(2), [n for n in range(1, 5000) if isprime(n) and isprime(phi(n))][0]] == [1, 3]
assert [n for n in range(1, 5000) if isprime(n) and isprime(phi(n))] == [3]
assert all(phi(p) % 2 == 0 and phi(p) > 2 for p in primerange(5, 5000))
# Q3b
pairs = [(x, y) for x in (1, 2) for y in (1, 2)]
good = []
for rr in range(len(pairs) + 1):
    for c in itertools.combinations(pairs, rr):
        R_ = set(c)
        if all((x, x) in R_ for x in (1, 2)) and not all((y, x) in R_ for (x, y) in R_):
            good.append(R_)
assert numerics(3, "ב") == [len(good)] == [2]
# Q3c
for x in range(-40, 41):
    for y in range(-40, 41):
        assert ((x*x + y) % 2 == 0) == ((x + y) % 2 == 0)
assert ((1*1 + 1) % 2 == 0) and (1*1) % 2 == 1   # xRy for x=y=1 although x odd and xy odd
Z = range(-6, 7)
R3 = {(x, y) for x in Z for y in Z if (x*x + y) % 2 == 0}
assert all((x, x) in R3 for x in Z) and all((y, x) in R3 for (x, y) in R3)
assert all((x, z) in R3 for (x, y) in R3 for (y2, z) in R3 if y == y2)
assert not all(not ((x, y) in R3 and (y, x) in R3) or x == y for x in Z for y in Z)
assert numerics(3, "ג") == [len({frozenset(y for y in Z if (x, y) in R3) for x in Z})] == [2]
# the buggy line claims x,y even; x=1 is a counterexample (1,1) in R but 1 is odd
assert step(3, "ג", "findbug")["bugIndex"] == 2
# Q4a
oddm = lambda n: sum(comb(n, j) for j in range(1, n + 1, 2))
tot = lambda n: sum(j * comb(n, j) for j in range(n + 1))
assert numerics(4, "א") == [oddm(4), tot(4), tot(100) // oddm(100)] == [8, 32, 100] and tot(100) % oddm(100) == 0
# Q4b: permutations of 1..7 mapping {1,2,3} onto itself; the identity-on-the-rest claim is false
perms7 = [p for p in itertools.permutations(range(1, 8)) if {p[0], p[1], p[2]} == {1, 2, 3}]
assert numerics(4, "ב") == [factorial(3), factorial(4), len(perms7)] == [6, 24, 144]
assert len({p[3:] for p in perms7}) == 24 and any(p[3] != 4 for p in perms7)
# Q4c
assert numerics(4, "ג") == [5, 18 - 5 - 3 - 7, sum(1 for x in range(5, 19) for y in range(3, 19) for z in range(7, 19) if x + y + z == 18)] == [5, 3, 10]
# Q4d
nn = gcd(11, 70**10 - 1)
assert numerics(4, "ד") == [nn, phi(nn + nn*nn), phi(phi(nn + nn*nn))] == [11, 40, 16] and (16 % 8 == 0)
assert pow(70, 10, 11) == 1
print("steps OK")
