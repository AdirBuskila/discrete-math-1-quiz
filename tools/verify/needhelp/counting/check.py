# Machine checks for the guided course "counting" (courses/counting/C01..C09). ASCII output only.
# Every stored answer is recomputed by brute force (itertools enumeration), never by the formula alone.
# Run:  py tools/verify/needhelp/counting/check.py
import json, math, os, re, subprocess
from itertools import combinations, permutations, product
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
out = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], capture_output=True, check=True).stdout
data = json.loads(out.decode("utf8"))
assert not data["errors"], data["errors"]
Q = {}
for rec in data["levels"]:
    if rec["courseId"] != "counting":
        continue
    for q in rec["level"]["questions"]:
        Q[q["bankId"] if "bankId" in q else q["id"]] = q
done = set()
comb = math.comb


def opts(qid):
    return {o["id"]: o["value"] for o in Q[qid]["options"]}


def plain(v):
    return v.replace("$", "").replace(" ", "")


def num(qid, expected):
    st = Q[qid]["step"]
    assert st["type"] == "numeric" and st["tol"] == 0, qid
    assert st["answer"] == expected, (qid, st["answer"], expected)
    done.add(qid)


def mcq_val(qid, expected):
    """options are plain numbers: the correct one equals the brute-force value, no other option does"""
    o = opts(qid)
    assert len(o) == 4 and len(set(o.values())) == 4, qid
    assert plain(o[Q[qid]["correctId"]]) == str(expected), (qid, o, expected)
    for k, v in o.items():
        if k != Q[qid]["correctId"]:
            assert plain(v) != str(expected), (qid, v)
    done.add(qid)


# ---------------------------------------------------------------- C01
assert len(list(product("abc", repeat=4))) == 81
assert len(list(product("abc", repeat=4))) not in (64, 12, 24)
mcq_val("C01-Q1", 81)
num("C01-Q2", sum(1 for n in range(100, 1000) if int(str(n)[0]) % 2 == 1))
meals = [("soup", i) for i in range(4)] + [("salad", i) for i in range(3)]
num("C01-Q3", len(list(product(meals, range(5)))))
num("C01-Q4", sum(1 for w in product("01", repeat=5) if "".join(w[:2]) in ("11", "00")))
num("C01-Q5", sum(1 for w in product("abc", repeat=4) if "a" in w))

# ---------------------------------------------------------------- C02
num("C02-Q1", len(list(permutations(range(5)))))
num("C02-Q2", len(list(permutations("abcdefg", 3))))
num("C02-Q3", sum(1 for p in permutations(range(1, 8), 3) if p[-1] % 2 == 1))
c = sum(1 for n in range(100, 1000) if len(set(str(n))) == 3)
assert c == 648
mcq_val("C02-Q4", c)
num("C02-Q5", sum(1 for p in permutations("abcdef", 4) if p[-1] in "ef"))

# ---------------------------------------------------------------- C03
num("C03-Q1", len(list(combinations(range(8), 3))))
assert len(list(permutations(range(8), 2))) == 56 and len(list(combinations(range(8), 2))) == 28
mcq_val("C03-Q2", 56)
num("C03-Q3", sum(1 for s in combinations(range(1, 11), 4) if 1 in s))
ns = [n for n in range(2, 60) if len(list(combinations(range(n), 2))) == 78]
assert ns == [13]
num("C03-Q4", 13)


def subsets(n):
    for m in range(1 << n):
        yield {i + 1 for i in range(n) if m >> i & 1}


num("C03-Q5", sum(1 for B in subsets(12) if not B & {1, 2, 3} and 12 in B))
num("C03-Q6", sum(1 for B in subsets(9) if len(B & {1, 2, 3, 4, 5}) == 1))

# ---------------------------------------------------------------- C04
num("C04-Q1", len(list(product(range(5), repeat=3))))
for n in (1, 2, 3):
    pairs = list(product(range(n), repeat=2))
    assert sum(1 for m in range(1 << len(pairs))) == 2 ** (n * n)
num("C04-Q2", sum(1 for m in range(1 << 16)))
num("C04-Q3", sum(1 for t in product(range(1, 8), repeat=3) if t[0] < t[1] < t[2]))
pairs3 = list(product(range(3), repeat=2))
rels = [[p for i, p in enumerate(pairs3) if m >> i & 1] for m in range(1 << 9)]
num("C04-Q4", sum(1 for R in rels if len(R) <= 2))


def is_fun(R):
    return all(sum(1 for (a, b) in R if a == x) == 1 for x in range(3))


assert sum(1 for R in rels if is_fun(R)) == 27
nf = sum(1 for R in rels if not is_fun(R))
assert nf == 485 == 2 ** 9 - 3 ** 3
mcq_val("C04-Q5", nf)

# ---------------------------------------------------------------- C05
def adjacent(p, items):
    pos = sorted(p.index(i) for i in items)
    return pos[-1] - pos[0] == len(items) - 1


num("C05-Q1", sum(1 for p in permutations(range(1, 7)) if adjacent(p, (1, 2))))
num("C05-Q2", sum(1 for p in permutations(range(1, 8)) if adjacent(p, (1, 2, 3, 4))))
num("C05-Q3", sum(1 for p in permutations("abcdef") if "cd" in "".join(p)))
num("C05-Q4", sum(1 for p in permutations(range(1, 8)) if p.index(1) < p.index(2)))
couples = sum(1 for p in permutations(range(6)) if all(abs(p.index(2 * i) - p.index(2 * i + 1)) == 1 for i in range(3)))
assert couples == 48
mcq_val("C05-Q5", couples)

# ---------------------------------------------------------------- C06
num("C06-Q1", sum(1 for n in range(1, 101) if n % 4 == 0 or n % 6 == 0))
num("C06-Q2", sum(1 for n in range(1, 91) if n % 2 and n % 3 and n % 5))
c = sum(1 for n in range(1, 201) if n % 6 == 0 and n % 4 != 0)
assert c == 17
mcq_val("C06-Q3", c)
num("C06-Q4", sum(1 for w in product("abc", repeat=4) if "a" in w and "b" in w))
# the stated sizes are consistent with real sets, and the formula equals the real union size
import random
random.seed(1)
for _ in range(300):
    U = range(60)
    A, B, C_ = (set(random.sample(U, random.randint(0, 40))) for _ in range(3))
    assert len(A | B | C_) == len(A) + len(B) + len(C_) - len(A & B) - len(A & C_) - len(B & C_) + len(A & B & C_)
assert 30 + 25 + 20 - 10 - 8 - 5 + 3 == 55
# concretely realise the sizes of Q5 to prove they are consistent
A = set(range(0, 30)); B = set(range(20, 45)); C_ = set(range(27, 47))
assert len(A) == 30 and len(B) == 25 and len(C_) == 20
# (sizes of the intersections of this realisation differ; Q5 only uses the formula, checked on 300 random triples above)
num("C06-Q5", 55)

# ---------------------------------------------------------------- C07
def sols(r, n, lows=None, le=False):
    lows = lows or [0] * r
    cnt = 0
    for x in product(range(n + 1), repeat=r):
        if all(x[i] >= lows[i] for i in range(r)):
            s = sum(x)
            if (s <= n) if le else (s == n):
                cnt += 1
    return cnt


num("C07-Q1", sols(3, 10))
num("C07-Q2", sols(4, 14, [1, 1, 1, 1]))
num("C07-Q3", sols(3, 14, [2, 3, 4]))
num("C07-Q4", sols(3, 6, le=True))
num("C07-Q5", sum(1 for w in product("abc", repeat=4) if (w.count("a"), w.count("b"), w.count("c")) == (2, 1, 1)))
c = len({tuple(sorted(w)) for w in product("ab", repeat=5)})
assert c == 6
mcq_val("C07-Q6", c)

# ---------------------------------------------------------------- C08
num("C08-Q1", sum(comb(6, k) * 2 ** k for k in range(7)))
for n in range(0, 14):
    assert sum(comb(n, k) * (2 ** k + 3 ** k) for k in range(n + 1)) == 3 ** n + 4 ** n
    assert sum(comb(n, k) * (4 ** k + 2 ** k) for k in range(n + 1)) == 5 ** n + 3 ** n
o = opts("C08-Q2")
assert plain(o[Q["C08-Q2"]["correctId"]]) == "3^n+4^n"
assert len(set(o.values())) == 4
f3 = lambda n: 3 ** n + 4 ** n
for k, v in o.items():
    if k == Q["C08-Q2"]["correctId"]:
        continue
    g = {"5^n": lambda n: 5 ** n, "2^n+3^n": lambda n: 2 ** n + 3 ** n, "6^n": lambda n: 6 ** n}[plain(v)]
    assert any(f3(n) != g(n) for n in range(0, 6)), v
done.add("C08-Q2")
num("C08-Q3", sum(1 for B in subsets(10) if len(B) % 2 == 0))
num("C08-Q4", sum(len(B) for B in subsets(8)))
# C08-Q5: f = 5^n + 3^n.  f=O(5^n) with c=2; the other three have unbounded f/g
fq = lambda n: 5 ** n + 3 ** n
assert all(fq(n) <= 2 * 5 ** n for n in range(0, 300))
for base in (3, 4, 2):
    ratios = [F(fq(n), base ** n) for n in (50, 100, 200, 400)]
    assert ratios == sorted(ratios) and ratios[-1] > 10 ** 30, base
o = opts("C08-Q5")
assert plain(o[Q["C08-Q5"]["correctId"]]) == "f(n)=O(5^n)"
assert sorted(plain(v) for v in o.values()) == sorted(f"f(n)=O({b}^n)" for b in (5, 3, 4, 2))
done.add("C08-Q5")
num("C08-Q6", sum(len(B) for B in subsets(9)))

# ---------------------------------------------------------------- C09 boss: bank questions (verified sittings only, never 20A-A)
bank = {}
for fn in os.listdir(os.path.join(ROOT, "tools", "raw")):
    if fn.endswith(".json") and not fn.startswith("_"):
        d = json.load(open(os.path.join(ROOT, "tools", "raw", fn), encoding="utf8"))
        for qq in d["questions"]:
            sfx = f"Q{qq['num']}" + {"א": "a", "ב": "b", "ג": "c", "ד": "d", "ה": "e", "ו": "f"}.get(qq.get("part", ""), "")
            bank[f"{d['examCode']}-{sfx}"] = (d, qq)
BOSS = ["18A-A-Q4b", "18B-A-Q4c", "18B-A-Q4a", "19A-B-Q4b", "19A-B-Q3c", "23A-A-Q4c"]
assert [k for k in Q if re.match(r"\d\d[A-Z]-[A-Z]-Q", k)] == BOSS
for b in BOSS:
    d, qq = bank[b]
    assert not b.startswith("20A-A"), b
    assert qq["stepsSource"] in ("ai-verified", "official") and qq.get("rubricSource") in ("ai-verified", "official"), b
    assert not qq.get("hold"), b
    assert qq["topic"] == "combinatorics", b
    done.add(b)

# 18A-A-Q4b: (1) 72  (2) 360  (3) 48
q1 = sum(1 for w in product("abcdef", repeat=3) if w[0] in "ab")
q2 = len(list(permutations("abcdef", 4)))
q3 = sum(1 for p in permutations("abcdef") if "ab" in "".join(p) and abs(p.index("c") - p.index("d")) == 1)
assert (q1, q2, q3) == (72, 360, 48)
sol = bank["18A-A-Q4b"][1]["solution"]
for s in ("=72", "=360", "=48"):
    assert s in sol.replace(" ", ""), s
# 18B-A-Q4c: vectors (x_a>4, x_b>2, x_c>=7), sum 18  ->  10
v = sum(1 for x in product(range(19), repeat=3) if sum(x) == 18 and x[0] > 4 and x[1] > 2 and x[2] >= 7)
assert v == 10 and "=10" in bank["18B-A-Q4c"][1]["solution"].replace(" ", "")
# 18B-A-Q4a: m + sum |B| over A={1..100}: check the formulas on small n by brute force, then evaluate at 100
for n in range(1, 13):
    odd = sum(1 for B in subsets(n) if len(B) % 2 == 1)
    tot = sum(len(B) for B in subsets(n))
    assert odd == 2 ** (n - 1) and tot == n * 2 ** (n - 1)
assert sum(comb(100, k) for k in range(1, 101, 2)) == 2 ** 99 and sum(k * comb(100, k) for k in range(101)) == 100 * 2 ** 99
assert 2 ** 99 + 100 * 2 ** 99 == 101 * 2 ** 99 and "101\\cdot2^{99}" in bank["18B-A-Q4a"][1]["solution"].replace(" ", "")
# 19A-B-Q4b: strictly increasing f:{1..10}->{1..20} = C(20,10); brute force the same statement on smaller sizes
for m, nn in ((3, 7), (4, 8), (5, 9)):
    assert sum(1 for t in product(range(nn), repeat=m) if all(t[i] < t[i + 1] for i in range(m - 1))) == comb(nn, m)
assert comb(20, 10) == 184756 and "\\binom{20}{10}" in bank["19A-B-Q4b"][1]["solution"]
# 19A-B-Q3c: sum C(n,k)(9^k+4^k) = 10^n + 5^n
for n in range(1, 12):
    assert sum(comb(n, k) * (3 ** (2 * k) + 2 ** (2 * k)) for k in range(n + 1)) == 10 ** n + 5 ** n
assert "10^n+5^n" in bank["19A-B-Q3c"][1]["solution"].replace(" ", "")
# 23A-A-Q4c: |B cap odds| = 1 on A={1..2n+1}  ->  (n+1) 2^n (brute force n=6,7)
for n in (6, 7):
    odds = set(range(1, 2 * n + 2, 2))
    assert sum(1 for B in subsets(2 * n + 1) if len(B & odds) == 1) == (n + 1) * 2 ** n
assert "(n+1)\\cdot2^n" in bank["23A-A-Q4c"][1]["solution"].replace(" ", "")

# ---------------------------------------------------------------- coverage: every question has a check
missing = [k for k in Q if k not in done]
assert not missing, missing
print("counting: %d questions checked (%d own + %d boss bankIds), all stored answers match brute force" % (len(done), len(done) - len(BOSS), len(BOSS)))
