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
