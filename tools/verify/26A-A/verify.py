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
