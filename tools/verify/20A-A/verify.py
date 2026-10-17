# Checks of the 20A-A keys. ASCII output only.
import itertools
from math import comb, factorial, gcd
from sympy import totient
# Q1a
assert 2 * factorial(4) == 48
# Q1b
assert totient(factorial(5)) == 32
# Q1c: complement of K_{m,n}
for m in range(1, 8):
    for n in range(1, 8):
        N = m + n
        assert N * (N - 1) // 2 - m * n == m * (m - 1) // 2 + n * (n - 1) // 2
print("Q1a-c OK")
# graph helpers
def complement(nv, edges):
    return {frozenset(e) for e in itertools.combinations(range(nv), 2)} - {frozenset(e) for e in edges}
def connected(nv, E):
    adj = {i: set() for i in range(nv)}
    for e in E:
        a, b = tuple(e); adj[a].add(b); adj[b].add(a)
    seen, st = {0}, [0]
    while st:
        u = st.pop()
        for w in adj[u] - seen:
            seen.add(w); st.append(w)
    return len(seen) == nv, adj
def bipartite(nv, adj):
    col = {}
    for s in range(nv):
        if s in col: continue
        col[s] = 0; st = [s]
        while st:
            u = st.pop()
            for w in adj[u]:
                if w not in col: col[w] = 1 - col[u]; st.append(w)
                elif col[w] == col[u]: return False
    return True
good = []
for n in range(2, 13):
    E = complement(n, [(i, i + 1) for i in range(n - 1)])
    c, adj = connected(n, E)
    if c and bipartite(n, adj): good.append(n)
assert good == [4], good
print("Q1d OK: only n=4 for 2<=n<=12")
# Q1e: A = integers < -5 is countably infinite, same as Q  (no script needed)
# Q3a
cnt = sum(1 for k in range(1, 101) if k % 3 and k % 5 and k % 7)
assert cnt == 45 and 100 - 67 + 12 - 0 == 45
# Q3b
a = [14, 27]
for n in range(2, 40):
    a.append(15 * 2**n - a[n - 2])
import math
for n in range(40):
    v = 2 * round(math.cos(n * math.pi / 2)) + 3 * round(math.sin(n * math.pi / 2)) + 12 * 2**n
    assert a[n] == v
print("Q3a,b OK")
# Q3c: complement of P15 has exactly 2 odd vertices and is connected
n = 15
E = complement(n, [(i, i + 1) for i in range(n - 1)])
c, adj = connected(n, E)
odd = [v for v in adj if len(adj[v]) % 2]
assert c and len(odd) == 2 and sorted(len(adj[v]) for v in odd) == [13, 13]
assert all(len(adj[v]) == 12 for v in adj if v not in odd)
assert all(len(adj[v]) >= 15 / 2 for v in adj)
print("Q3c OK (Euler path, no circuit)")
# Q4
assert comb(11, 2) == 55 and 2**10 == 1024
assert comb(6, 4) == 15 and 6 * 5 * 4 * 3 == 360
inc = sum(1 for f in itertools.product(range(1, 7), repeat=4) if f[0] < f[1] < f[2] < f[3])
inj = sum(1 for f in itertools.product(range(1, 7), repeat=4) if len(set(f)) == 4)
assert (inc, inj) == (15, 360)
for n in range(3, 9):
    assert sum(k * comb(n, k) for k in range(n + 1)) == n * 2**(n - 1)
print("Q4 OK")
# Q5a: Erdos-Gallai on (1,1,2,3,3,3,6,7,8)
d = sorted([1, 1, 2, 3, 3, 3, 6, 7, 8], reverse=True)
def graphic(d):
    if sum(d) % 2: return False
    for k in range(1, len(d) + 1):
        if sum(d[:k]) > k * (k - 1) + sum(min(x, k) for x in d[k:]): return False
    return True
assert not graphic(d)
print("Q5a OK: not graphic")
# Q5b
assert comb(15, 3) == 455
cnt = sum(1 for x in itertools.product(range(23), repeat=3) if (lambda s: s >= 0 and s[0] if False else True)(x))
tot = 0
for x1 in range(3, 23):
    for x2 in range(1, 23):
        for x3 in range(4, 23):
            x4 = 22 - x1 - x2 - x3
            if x4 >= 2: tot += 1
assert tot == 455
# Q5c / Q6c: Petersen graph
V = "abcdefghij"
ed = ["ab", "bc", "cd", "de", "ea", "af", "bg", "ch", "di", "ej", "fh", "hj", "jg", "gi", "if"]
G = {frozenset(e) for e in ed}
idx = {c: i for i, c in enumerate(V)}
Gi = [(idx[x], idx[y]) for x, y in ed]
adjG = {i: set() for i in range(10)}
for x, y in Gi: adjG[x].add(y); adjG[y].add(x)
assert all(len(adjG[v]) == 3 for v in adjG)
Ec = complement(10, Gi)
c, adjC = connected(10, Ec)
assert c and all(len(adjC[v]) == 6 for v in adjC) and all(len(adjC[v]) >= 5 for v in adjC)  # Dirac: 6>=10/2
assert all(len(adjC[v]) % 2 == 0 for v in adjC)   # Euler circuit
assert not bipartite(10, adjC)
tri = [t for t in itertools.combinations(range(10), 3) if all(frozenset(p) in Ec for p in itertools.combinations(t, 2))]
assert (idx['a'], idx['d'], idx['g']) in tri
# diameter of G
def bfs(s):
    dist = {s: 0}; q = [s]
    for u in q:
        for w in adjG[u]:
            if w not in dist: dist[w] = dist[u] + 1; q.append(w)
    return dist
assert max(max(bfs(s).values()) for s in range(10)) == 2
da = bfs(idx['a']); df = bfs(idx['f'])
assert [v for v in V if da[idx[v]] == 1] == list("bef") and [v for v in V if da[idx[v]] == 2] == list("cdghij"), da
assert sorted(v for v in V if df[idx[v]] == 1) == list("ahi")
print("Q5c/Q6c OK (Dirac, Euler circuit, not bipartite, triangle a,d,g, diameter 2)")
# Q6a
for n in range(5, 9):
    a_ = sum(comb(n, k) * 3**k * 5**(n - k) for k in range(n + 1))
    b_ = sum(comb(n, k) * 7**k * 5**(n - k) for k in range(n + 1))
    assert a_ == 8**n and b_ == 12**n
    assert totient(a_ * b_) == 2**(5 * n) * 3**(n - 1)
print("Q6a OK")
# Held items (not shipped): Q2a(2) 7!/2 = 2520 not 2560; Q2b(1) with repeats 4^4*3^3 vs key 144
assert comb(7, 2) * factorial(5) == 2520 == factorial(7) // 2 and 3 * 2 * 120 == 720
assert 4**4 * 3**3 == 6912 and factorial(3) * factorial(4) == 144 and 2 * 6 * 6 == 72
for n in (15, 30, 45, 60):
    assert totient(n) % 8 == 0
print("held-item notes OK")
