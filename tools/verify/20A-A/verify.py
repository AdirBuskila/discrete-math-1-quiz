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
# Formerly held (shipped 2026-10-17, see below): Q2a(2) 7!/2 = 2520 not 2560; Q2b(1) with repeats 4^4*3^3 vs key 144
assert comb(7, 2) * factorial(5) == 2520 == factorial(7) // 2 and 3 * 2 * 120 == 720
assert 4**4 * 3**3 == 6912 and factorial(3) * factorial(4) == 144 and 2 * 6 * 6 == 72
for n in (15, 30, 45, 60):
    assert totient(n) % 8 == 0
print("held-item notes OK")
# --- solver/arbiter 2026-10-17: brute force for the now-shipped Q2a, Q2b, Q2c ---
P7 = list(itertools.permutations(range(1, 8)))
adj = sum(1 for p in P7 if max(p.index(v) for v in (1, 2, 3)) - min(p.index(v) for v in (1, 2, 3)) == 2)
before = sum(1 for p in P7 if p.index(1) < p.index(2))
assert adj == 720 and before == 2520 != 2560
print("Q2a OK: 720 and 2520 (key printed 2560)")
A_, B_ = "abcd", "xyz"
rep = sum(1 for _ in itertools.product(A_, repeat=4)) * sum(1 for _ in itertools.product(B_, repeat=3))
norep = [s + t for s in itertools.product(A_, repeat=4) for t in itertools.product(B_, repeat=3)
         if len(set(s)) == 4 and len(set(t)) == 3]
assert rep == 6912 and len(norep) == 144
part2 = [w for w in itertools.product(A_, repeat=4) for t in itertools.product(B_, repeat=3)
         if len(set(w)) == 4 and len(set(t)) == 3 and w[0] in "ab"]
assert len(part2) == 72
print("Q2b OK: (1) 6912 with repeats (144 without), (2) 72 under both readings")
assert totient(1) == totient(2) == 1
for n in range(15, 15 * 400, 15):
    a = b = 0; m = n
    while m % 3 == 0: m //= 3; a += 1
    while m % 5 == 0: m //= 5; b += 1
    assert totient(n) == 2 * 4 * 3**(a - 1) * 5**(b - 1) * totient(m) and totient(n) % 8 == 0
print("Q2c OK: phi(n) = 2*4*3^(a-1)*5^(b-1)*phi(m), 8 | phi(n)")

# ======================= STEPS section (step-author pass) =======================
_CODE = "20A-A"
# Re-reads tools/raw/<CODE>.json and recomputes every numeric step answer and every choice key independently
# (sympy / brute force). ASCII output only.
import json as _json, pathlib as _pl, itertools as _it
import sympy as _sp

_RAW = _json.loads((_pl.Path(__file__).resolve().parents[2] / "raw" / (_CODE + ".json")).read_text(encoding="utf-8"))
_PART = {"": "", "a": "א", "b": "ב", "c": "ג", "d": "ד", "e": "ה"}


def _Q(num, p=""):
    for q in _RAW["questions"]:
        if q["num"] == num and q.get("part", "") == _PART[p]:
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


def _nsteps(num, p, n):
    assert len(_Q(num, p)["steps"]) == n, (num, p)


def _lines(num, p, i):
    return _S(num, p, i)["lines"]


import math
from math import comb, factorial
from collections import deque
_k, _n = _sp.symbols("k n", integer=True)

# ---- 1a
_P5 = list(_it.permutations(range(1, 6)))
assert sum(1 for p in _P5 if p[0] == 1) == 24 and not [p for p in _P5 if p[0] == 1 and p[0] == 2]
assert sum(1 for p in _P5 if p[0] in (1, 2)) == 48
_num(1, "a", 0, 24); _num(1, "a", 2, 48); _nsteps(1, "a", 3)

# ---- 1b
assert _sp.factorint(120) == {2: 3, 3: 1, 5: 1} and 2**3 * 3 * 5 == 120
assert len({2**2 * 3 * 5, 2**3 * 3**2 * 5, 2 * 3 * 5, 120}) == 4
assert _sp.totient(8) == 4 == len([m for m in range(1, 9) if math.gcd(m, 8) == 1])
assert _sp.totient(120) == 32 == len([m for m in range(1, 121) if math.gcd(m, 120) == 1])
_num(1, "b", 1, 4); _num(1, "b", 2, 32); _nsteps(1, "b", 3)

# ---- 1c (m=3, n=4)
_V = [("A", i) for i in range(3)] + [("B", i) for i in range(4)]
_E = {frozenset((u, v)) for u in _V for v in _V if u[0] == "A" and v[0] == "B"}
_Ec = {frozenset((u, v)) for u in _V for v in _V if u != v} - _E
assert len(_E) == 12 and len(_Ec) == 9 == comb(7, 2) - 12 == comb(3, 2) + comb(4, 2)
assert all(next(iter(e))[0] == sorted(e)[1][0] for e in _Ec)            # every complement edge is inside one side
_num(1, "c", 1, 12); _num(1, "c", 2, 9); _nsteps(1, "c", 3)

# ---- 1d
def _comp_path(n):
    adj = {i: set() for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if j != i + 1: adj[i].add(j); adj[j].add(i)
    return adj
def _conn_bip(adj):
    col = {}
    for s in adj:
        if s in col: continue
        col[s] = 0; dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in col: col[v] = 1 - col[u]; dq.append(v)
                elif col[v] == col[u]: return False, None
    seen = {0}; dq = deque([0])
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if v not in seen: seen.add(v); dq.append(v)
    return len(seen) == len(adj), True
_good = [n for n in range(2, 13) if _conn_bip(_comp_path(n))[0] and _conn_bip(_comp_path(n))[1]]
assert _good == [4]
_a3 = _comp_path(3); assert _a3[0] == {2} and _a3[1] == set()
assert sum(len(v) for v in _comp_path(4).values()) // 2 == 3
_num(1, "d", 0, 2); _num(1, "d", 1, 3); _right(1, "d", 2, "$n=4$"); _nsteps(1, "d", 3)

# ---- 1e
_nsteps(1, "e", 3)
assert _Q(1, "e")["verdict"] is True

# ---- 2a
_P7 = list(_it.permutations(range(1, 8)))
_adj = sum(1 for p in _P7 if max(p.index(v) for v in (1, 2, 3)) - min(p.index(v) for v in (1, 2, 3)) == 2)
_bef = sum(1 for p in _P7 if p.index(1) < p.index(2))
assert _adj == 720 == 6 * 120 and _bef == 2520 == comb(7, 2) * 120 == factorial(7) // 2
assert all(w != 2520 for w in (comb(7, 2) * 2 * 120, factorial(7) // 6, factorial(7)))
_num(2, "a", 0, 120); _num(2, "a", 1, 720); _num(2, "a", 3, 2520); _nsteps(2, "a", 4)

# ---- 2b
_rep = 4**4 * 3**3
assert _rep == 6912 == sum(1 for _ in _it.product("abcd", repeat=4)) * sum(1 for _ in _it.product("xyz", repeat=3))
_c2 = sum(1 for w in _it.product("abcd", repeat=4) for t in _it.product("xyz", repeat=3)
          if len(set(w)) == 4 and len(set(t)) == 3 and w[0] in "ab")
assert _c2 == 72 == 2 * 6 * 6
_num(2, "b", 0, 6912); _num(2, "b", 1, 2); _num(2, "b", 2, 72); _nsteps(2, "b", 3)

# ---- 2c
assert _sp.totient(1) == _sp.totient(2) == 1
assert len({(_sp.totient(a), _sp.totient(b)) for a, b in ((2, 3), (3, 5), (4, 5)) if _sp.totient(a) == _sp.totient(b)}) == 0
assert _sp.totient(15) == 8
for _m in range(15, 15 * 300, 15):
    a = b = 0; r = _m
    while r % 3 == 0: r //= 3; a += 1
    while r % 5 == 0: r //= 5; b += 1
    assert _sp.totient(_m) == 8 * 3**(a - 1) * 5**(b - 1) * _sp.totient(r) and _sp.totient(_m) % 8 == 0
_right(2, "c", 0, r"$\phi(1)=\phi(2)=1$"); _num(2, "c", 1, 8); _nsteps(2, "c", 3)

# ---- 3a
_O = range(1, 101)
_c = lambda d: len([v for v in _O if v % d == 0])
assert _c(3) == 33 and _c(15) + _c(21) + _c(35) == 12 and _c(105) == 0
assert len([v for v in _O if v % 3 and v % 5 and v % 7]) == 45
_num(3, "a", 0, 33); _num(3, "a", 1, 12); _num(3, "a", 2, 0); _num(3, "a", 3, 45); _nsteps(3, "a", 4)

# ---- 3b
_a = [14, 27]
for i in range(2, 31): _a.append(15 * 2**i - _a[i - 2])
_fo = lambda i: 2 * _sp.cos(i * _sp.pi / 2) + 3 * _sp.sin(i * _sp.pi / 2) + 12 * 2**i
assert all(_fo(i) == _a[i] for i in range(31)) and _a[2] == 46
_xs = _sp.symbols("x"); assert _sp.solve(_xs**2 + 1, _xs) == [-_sp.I, _sp.I]
assert _sp.solve(_sp.Symbol("A") * 5 - 60, _sp.Symbol("A")) == [12] and 27 - 24 == 3
_num(3, "b", 1, 12); _num(3, "b", 2, 3); _num(3, "b", 3, 46); _nsteps(3, "b", 4)

# ---- 3c
_g = {i: set() for i in range(15)}
_pe = {(i, i + 1) for i in range(14)}
for i in range(15):
    for j in range(15):
        if i != j and (min(i, j), max(i, j)) not in _pe: _g[i].add(j)
_deg = {v: len(s) for v, s in _g.items()}
assert _deg[0] == _deg[14] == 13 and all(_deg[v] == 12 for v in range(1, 14))
assert sum(1 for v in _deg.values() if v % 2) == 2
_num(3, "c", 0, 13); _num(3, "c", 1, 12); _num(3, "c", 2, 2); _nsteps(3, "c", 4)

# ---- 4a
assert [n for n in range(3, 40) if comb(n, 2) == 55] == [11] and _sp.solve(_n**2 - _n - 110, _n) == [-10, 11]
assert sum(comb(11, k) for k in range(0, 12, 2)) == 1024 == 2**10
assert len({2**10, 2**11, 2**9, 11**2}) == 4
_num(4, "a", 0, 11); _num(4, "a", 2, 1024); _nsteps(4, "a", 3)

# ---- 4b
_fs = list(_it.product(range(1, 7), repeat=4))
assert sum(1 for f in _fs if all(f[i] < f[i + 1] for i in range(3))) == 15 == comb(6, 4)
assert sum(1 for f in _fs if len(set(f)) == 4) == 360 == 6 * 5 * 4 * 3
assert len({f for f in _fs if all(f[i] < f[i + 1] for i in range(3)) and f[0] == 1}) > 1       # "value at 1 only" does not determine it
_num(4, "b", 0, 15); _num(4, "b", 1, 360); _nsteps(4, "b", 3)

# ---- 4c
_s4 = sum(len(c) for r in range(5) for c in _it.combinations(range(4), r))
assert _s4 == 32 == 4 * 2**3
assert all(w != 32 for w in (4 * 2**4, 2**4 - 1, 16 * 2**2))
_nn, _xx = _sp.symbols("nn xx")
assert _sp.expand(_sp.diff((1 + _xx)**4, _xx).subs(_xx, 1)) == 32 and (1 + 1)**4 != 32
_num(4, "c", 0, 32); _nsteps(4, "c", 3)

# ---- 5a  (degree sequence not graphical)
def _graphical(seq):
    seq = sorted(seq, reverse=True)
    while seq:
        d = seq.pop(0)
        if d > len(seq): return False
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0: return False
        seq.sort(reverse=True)
    return True
assert not _graphical([1, 1, 2, 3, 3, 3, 6, 7, 8]) and sum([1, 1, 2, 3, 3, 3, 6, 7, 8]) % 2 == 0
_rest = sorted([d - 1 for d in [1, 1, 2, 3, 3, 3, 6, 7]], reverse=True)
assert _rest == [6, 5, 2, 2, 2, 1, 0, 0] and _rest.count(0) == 2 and (8 - 1 - 2) == 5 < 6
assert _Q(5, "a")["verdict"] is False
_num(5, "a", 1, 2); _num(5, "a", 2, 5); _nsteps(5, "a", 3)

# ---- 5b
_cnt = sum(1 for x1 in range(3, 23) for x2 in range(1, 23) for x3 in range(4, 23) for x4 in range(2, 23) if x1 + x2 + x3 + x4 == 22)
assert _cnt == 455 == comb(15, 3) and 22 - 3 - 1 - 4 - 2 == 12 and len({comb(15, 3), comb(22, 4), comb(12, 3), comb(16, 4)}) == 4
_num(5, "b", 0, 12); _num(5, "b", 2, 455); _nsteps(5, "b", 3)

# ---- Petersen graph read from images/exams/20A-A-c1.png
_ed = ["ab", "bc", "cd", "de", "ea", "af", "bg", "ch", "di", "ej", "fi", "fh", "jg", "jh", "gi"]
_pg = {v: set() for v in "abcdefghij"}
for e in _ed: _pg[e[0]].add(e[1]); _pg[e[1]].add(e[0])
assert all(len(s) == 3 for s in _pg.values()) and len(_ed) == 15
def _dist(g, s):
    d = {s: 0}; dq = deque([s])
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if v not in d: d[v] = d[u] + 1; dq.append(v)
    return d
assert all(max(_dist(_pg, s).values()) == 2 for s in _pg)
_da = _dist(_pg, "a")
assert sorted(v for v, d in _da.items() if d == 1) == list("bef") and sorted(v for v, d in _da.items() if d == 2) == sorted("jgihcd")
_num(6, "c", 0, 3); _num(6, "c", 1, 6); _num(6, "c", 2, 2); _nsteps(6, "c", 3)
# ---- 5c: complement of the Petersen graph
_cg = {v: {u for u in _pg if u != v and u not in _pg[v]} for v in _pg}
assert all(len(s) == 6 for s in _cg.values()) and 6 >= 10 / 2
_hp = any(all(p[i + 1] in _cg[p[i]] for i in range(9)) and p[0] in _cg[p[9]] for p in ((("a",) + q) for q in _it.permutations("bcdefghij")))
assert _hp                                                                     # Hamilton cycle exists
assert "d" in _cg["a"] and "g" in _cg["a"] and "g" in _cg["d"]                 # triangle a,d,g in the complement
for _tri in ("abc", "aef", "dic"):
    assert any(_tri[j] not in _cg[_tri[i]] for i in range(3) for j in range(3) if i != j)
_col = {"a": 0}; _ok = True; _dq = deque(["a"])
while _dq and _ok:
    u = _dq.popleft()
    for v in _cg[u]:
        if v not in _col: _col[v] = 1 - _col[u]; _dq.append(v)
        elif _col[v] == _col[u]: _ok = False; break
assert not _ok                                                                  # not bipartite
_num(5, "c", 0, 6); _num(5, "c", 1, 5); _nsteps(5, "c", 4)

# ---- 6a
assert all(sum(comb(n, j) * 3**j * 5**(n - j) for j in range(n + 1)) == 8**n and
           sum(comb(n, j) * 7**j * 5**(n - j) for j in range(n + 1)) == 12**n for n in range(5, 9))
assert 8**5 * 12**5 == 2**25 * 3**5 and _sp.totient(8**5 * 12**5) == 2**25 * 3**4 == 2717908992
assert len({15**5, 2**5, 7**5 * 5**5}) == 3 and 8**5 != 15**5
assert all(_sp.totient(8**n * 12**n) == 2**(5 * n) * 3**(n - 1) for n in range(5, 9))
assert len({2**25 * 3**4, 2**25 * 3**5, 2**24 * 3**4, 2**24 * 3**5}) == 4
_num(6, "a", 1, 25); _num(6, "a", 2, 2717908992); _nsteps(6, "a", 4)

# ---- 6b
from fractions import Fraction as _Fr
_xs = [_Fr(i, 50) for i in range(1, 50)]
assert all(2 < x + 2 <= 7 for x in _xs) and len({x + 2 for x in _xs}) == len(_xs)
assert any(not (2 < 7 * x <= 7) for x in _xs) and all(not (2 < x - 2) for x in _xs) and any(not (2 < 2 * x) for x in _xs)
_right(6, "b", 1, "$f(x)=x+2$"); _nsteps(6, "b", 2)
print("STEPS 20A-A all OK")
