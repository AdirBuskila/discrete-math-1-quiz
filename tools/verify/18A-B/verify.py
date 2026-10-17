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
