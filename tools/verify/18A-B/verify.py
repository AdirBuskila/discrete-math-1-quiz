# Checks of the 18A-B key. ASCII output only.
import itertools
from math import comb, factorial
from sympy import totient, primerange
# Q1a: derangements of {1,2,3,4}
perms = list(itertools.permutations(range(1, 5)))
assert len(perms) == 24
der = [p for p in perms if all(p[i] != i + 1 for i in range(4))]
assert len(der) == 9
assert (2, 1, 4, 3) in der and (1, 3, 4, 2) not in der
print("Q1a OK")
# Q1b2: P(AxB)=P(A)xP(B) fails for A={1},B={2}
A, B = {1}, {2}
AxB = {(a, b) for a in A for b in B}
subsets = lambda S: [frozenset(c) for r in range(len(S) + 1) for c in itertools.combinations(sorted(S), r)]
PA, PB, PAB = subsets(A), subsets(B), set(subsets(AxB))
assert (frozenset({1}), frozenset({2})) in {(x, y) for x in PA for y in PB}
assert (frozenset({1}), frozenset({2})) not in PAB
print("Q1b OK")
# Q2a
for n in range(1, 300):
    assert sum(range(2*n+1, 4*n+2, 2)) == 3*n*n + 4*n + 1
for k in range(1, 300):
    assert (3*k*k + 4*k + 1) - (2*k + 1) + (4*k + 3) + (4*k + 5) == 3*(k+1)**2 + 4*(k+1) + 1
print("Q2a OK")
# Q2b: union of transitive relations
R1, R2 = {(1, 2)}, {(2, 1)}
tr = lambda R: all((a, d) in R for (a, b) in R for (c, d) in R if b == c)
assert tr(R1) and tr(R2) and not tr(R1 | R2)
print("Q2b OK")
# Q2c: 2 | 3x+y  <=> x,y same parity
for x in range(-30, 31):
    for y in range(-30, 31):
        assert ((3*x + y) % 2 == 0) == ((x - y) % 2 == 0)
assert (3*1+3) % 2 == 0 and (3*3+1) % 2 == 0
print("Q2c OK")
# Q3a
f = lambda p: int(totient(int(totient(p*p)))) % 2
assert f(2) == 1 and f(3) == 0 and f(2) + f(3) == 1
for p in primerange(3, 600):
    assert f(p) == 0
assert [p for p in primerange(2, 600) if f(p) == 1] == [2]
print("Q3a OK")
# Q3b
a = [20, 54]
for n in range(2, 40):
    a.append(4*a[n-1] - 4*a[n-2] + 2*3**n)
assert all(a[n] == 2*2**n - 2*n*2**n + 18*3**n for n in range(40))
print("Q3b OK")
# Q4a
for n in range(0, 40):
    s = sum(comb(n, k) * (3**(2*k) + 2**(2*k)) for k in range(n + 1))
    assert s == 10**n + 5**n <= 2 * 10**n
print("Q4a OK")
# Q4b
L = "abcdef"
assert sum(1 for w in itertools.product(L, repeat=4) if w[2:] == ("e", "f")) == 36
assert comb(6, 4) == 15 == len({frozenset(c) for c in itertools.permutations(L, 4)})
n3 = sum(1 for w in itertools.permutations(L, 6) if "abc" in "".join(w) and w[0] in "ad")
assert n3 == 12
print("Q4b OK")
# Q4c: length <= 22 over abcd, #a>=4,#b>=3,#c>=5,#d>=2
vec = 0
words = 0
for na in range(4, 23):
    for nb in range(3, 23):
        for nc in range(5, 23):
            for nd in range(2, 23):
                if na + nb + nc + nd <= 22:
                    vec += 1
                    t = na + nb + nc + nd
                    words += factorial(t) // (factorial(na)*factorial(nb)*factorial(nc)*factorial(nd))
assert vec == 495 == comb(12, 4)
print("Q4c count vectors:", vec, " words:", words)
# independent check of the word count: EGF product, words of length t with letter minimums
from fractions import Fraction
mins = [4, 3, 5, 2]
N = 22
def egf(m):
    return [Fraction(0) if j < m else Fraction(1, factorial(j)) for j in range(N + 1)]
poly = [Fraction(1)] + [Fraction(0)] * N
for m in mins:
    e = egf(m)
    new = [Fraction(0)] * (N + 1)
    for i, ci in enumerate(poly):
        if ci:
            for j in range(N + 1 - i):
                new[i + j] += ci * e[j]
    poly = new
tot = sum(poly[t] * factorial(t) for t in range(N + 1))
assert tot == words and tot.denominator == 1
print("Q4c words cross-check OK")

# ================= step checks (ai-draft steps); every numeric step answer is tied to tools/raw/18A-B.json =================
import json, pathlib
import sympy as sp
RAW = json.loads((pathlib.Path(__file__).resolve().parents[2] / "raw" / "18A-B.json").read_text(encoding="utf-8"))
def numerics(num, part):
    q = [q for q in RAW["questions"] if q["num"] == num and q.get("part") == part][0]
    return [s["answer"] for s in q["steps"] if s["type"] == "numeric"]
def lines_of(num, part, typ):
    q = [q for q in RAW["questions"] if q["num"] == num and q.get("part") == part][0]
    return [s for s in q["steps"] if s["type"] == typ][0]
# Q1a: counts and the choice step (exactly one option is a derangement)
perms = list(itertools.permutations(range(1, 5)))
der = [p for p in perms if all(p[i] != i + 1 for i in range(4))]
assert numerics(1, "א") == [len(perms), len(der), len(perms) - len(der)] == [24, 9, 15]
cands = [(2, 1, 4, 3), (1, 3, 4, 2), (3, 2, 1, 4), (4, 2, 3, 1)]
assert [c in der for c in cands] == [True, False, False, False]
# Q1b: |P(A)xP(B)| = 4, |P(A x B)| = 2 for A={1}, B={2}
assert numerics(1, "ב") == [len(PA) * len(PB), len(PAB)] == [4, 2]
# Q1c: negation checked on all small A,B,C (including empty sets)
import random
def orig(A, B, C):   # forall (x,y) in AxB exists z in C: z <= x+y
    return all(any(z <= x + y for z in C) for x in A for y in B)
def negs(A, B, C):
    return {"official": any(all(z > x + y for z in C) for x in A for y in B),
            "forall-forall": all(all(z > x + y for z in C) for x in A for y in B),
            "exists-exists": any(any(z > x + y for z in C) for x in A for y in B),
            "forall-exists": all(any(z > x + y for z in C) for x in A for y in B),
            ">=": any(all(z >= x + y for z in C) for x in A for y in B),
            "<": any(all(z < x + y for z in C) for x in A for y in B),
            "!=": any(all(z != x + y for z in C) for x in A for y in B)}
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
                            if v != (not o):
                                bad[k] = True
assert all(bad[k] for k in bad if k != "official"), bad
print("Q1c OK (every distractor differs from the negation on some instance)")
# Q2a: step values
assert numerics(2, "א") == [3 + 5, (4*3+3) + (4*3+5) - (2*3+1)] == [8, 25]
k = sp.symbols("k")
assert sp.expand((3*(k+1)**2 + 4*(k+1) + 1) - (3*k**2 + 4*k + 1)) == 6*k + 7
assert sp.expand((3*k**2 + 4*k + 1) - (2*k + 1) + (4*k + 3) + (4*k + 5)) == 3*k**2 + 10*k + 8
assert sp.expand(3*(k+1)**2 + 4*(k+1) + 1) == 3*k**2 + 10*k + 8
assert sp.expand(3*k**2 + 4*k + 1 - 2*k - 1 + 8*k + 8) == 3*k**2 + 10*k + 8 != 3*k**2 + 8*k + 8
fb = lines_of(2, "א", "findbug"); assert fb["bugIndex"] == 2
# Q2b: transitive closure of R1uR2 has 4 pairs, the union 2 -> 2 missing, (1,1) is derivable
U = R1 | R2
cl = set(U)
while True:
    new = {(a, d) for (a, b) in cl for (c, d) in cl if b == c} - cl
    if not new: break
    cl |= new
assert numerics(2, "ב") == [len(cl) - len(U)] == [2] and (1, 1) in cl and len(cl) == 4
# Q2c: classes, antisymmetry is the only failing property
Z = range(-6, 7)
R = {(x, y) for x in Z for y in Z if (3*x + y) % 2 == 0}
refl = all((x, x) in R for x in Z); symm = all((y, x) in R for (x, y) in R)
trans = all((x, z) in R for (x, y) in R for (y2, z) in R if y == y2)
anti = all(not ((x, y) in R and (y, x) in R) or x == y for x in Z for y in Z)
assert refl and symm and trans and not anti
assert numerics(2, "ג") == [len({frozenset(y for y in Z if (x, y) in R) for x in Z})] == [2]
x, y, z = sp.symbols("x y z")
assert sp.expand((3*x + y) + (3*y + z) - ((3*x + z) + 4*y)) == 0 and sp.expand((3*x + y) + (3*y + z) - ((3*x + z) + 3*y)) != 0
assert lines_of(2, "ג", "findbug")["bugIndex"] == 2
# Q3a
phi = lambda m: int(totient(m))
assert numerics(3, "א") == [phi(9), phi(phi(9)), f(2) + f(3), 2] == [6, 2, 1, 2]
# |B| = 2: a bijection onto {0,1} needs exactly 2 elements; {2,p} works for every odd prime p
assert all(len({f(2), f(p)}) == 2 for p in primerange(3, 200))
assert all(phi(p*p) == p*(p-1) != p*p - 1 for p in primerange(2, 300))
# Q3b
n_ = sp.symbols("n")
Asym = sp.symbols("A")
assert sp.solve(sp.Eq(9*Asym, 12*Asym - 4*Asym + 18), Asym) == [18]
assert sp.simplify(sp.Rational(1) * 0) == 0
# particular-form distractors fail: A*n*3^n has no constant A, A*2^n is not a solution (2 is a double root, rhs 3^n)
for form in (lambda n: n*3**n, lambda n: n**2*3**n, lambda n: 2**n):
    ok = [sp.solve(sp.Eq(Asym*form(m), 4*Asym*form(m-1) - 4*Asym*form(m-2) + 2*3**m), Asym) for m in range(2, 6)]
    assert not (ok[0] and all(ok[0] == o for o in ok)), form
c1, c2 = sp.symbols("c1 c2")
sol = sp.solve([c1 + 18 - 20, 2*c1 + 2*c2 + 54 - 54], [c1, c2])
assert sol == {c1: 2, c2: -2}
a2 = 4*54 - 4*20 + 2*3**2
assert numerics(3, "ב") == [2, 18, -2, 154] and a2 == 154 == 2*4 - 2*2*4 + 18*9
print("Q3 OK")
# Q4a
assert numerics(4, "א") == [sum(comb(3, k) * (9**k + 4**k) for k in range(4)), 2] == [1125, 2]
assert max(sp.Rational(10**m + 5**m, 10**m) for m in range(0, 60)) == 2
# Q4b
words3 = [w for w in itertools.permutations(L, 6) if "abc" in "".join(w) and w[0] in "ad"]
assert numerics(4, "ב") == [36, 15, sum(1 for w in words3 if w[0] == "a"), sum(1 for w in words3 if w[0] == "d"), len(words3)] == [36, 15, 6, 6, 12]
# Q4c: vectors vs words; distractor values
vec_exact22 = sum(1 for na in range(4, 23) for nb in range(3, 23) for nc in range(5, 23) for nd in range(2, 23) if na + nb + nc + nd == 22)
assert vec_exact22 == comb(11, 3) == 165 != 495
assert numerics(4, "ג") == [4 + 3 + 5 + 2, vec, words] == [14, 495, 10726916243718]
print("steps OK")
