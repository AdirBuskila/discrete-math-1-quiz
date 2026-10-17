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
