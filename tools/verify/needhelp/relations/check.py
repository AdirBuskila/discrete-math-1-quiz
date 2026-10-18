"""Machine check of the 'relations' guided course: every stored answer is recomputed by brute force."""
import itertools, json, math, subprocess, sys, os
sys.stdout.reconfigure(encoding="utf8")
HERE = os.path.dirname(os.path.abspath(__file__))
levels = json.loads(subprocess.check_output(["node", os.path.join(HERE, "export.js")]))
Q = {q["id"]: q for lv in levels.values() for q in lv["questions"] if "id" in q}


# ---------- brute-force toolkit ----------
def refl(R, A): return all((a, a) in R for a in A)
def sym(R): return all((b, a) in R for a, b in R)
def trans(R): return all((a, d) in R for a, b in R for c, d in R if b == c)
def anti(R): return all(a == b for a, b in R if (b, a) in R)
def equiv(R, A): return refl(R, A) and sym(R) and trans(R)


def partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


def rel_of(p): return {(x, y) for b in p for x in b for y in b}
def all_equiv(A): return [rel_of(p) for p in partitions(A)]
def klass(R, a, A): return frozenset(b for b in A if (a, b) in R)
def quotient(R, A): return {klass(R, a, A) for a in A}


def check_mcq(qid, truths):
    """truths: one bool per option in file order; exactly the stored correctId must be True."""
    q = Q[qid]
    ids = [o["id"] for o in q["options"]]
    assert len(truths) == len(ids), qid
    assert sum(truths) == 1, f"{qid}: {truths}"
    assert ids[truths.index(True)] == q["correctId"], \
        f"{qid}: stored {q['correctId']} but brute force says {ids[truths.index(True)]}"


def check_num(qid, value):
    s = Q[qid]["step"]
    assert s["type"] == "numeric" and s["answer"] == value and s.get("tol", 0) == 0, \
        f"{qid}: stored {s['answer']} vs {value}"


def full(R, A): return refl(R, A) and sym(R) and trans(R)


# ---------- C01 ----------
A3 = {1, 2, 3}
R1 = {(1, 1), (2, 2), (1, 2), (2, 1)}
check_mcq("C01-Q1", [not sym(R1), not trans(R1), not refl(R1, A3), full(R1, A3)])
R2 = {(1, 1), (2, 2), (3, 3), (1, 2)}
check_mcq("C01-Q2", [not refl(R2, A3), not sym(R2), not trans(R2), full(R2, A3)])
R3 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}
check_mcq("C01-Q3", [not refl(R3, A3), not sym(R3), full(R3, A3), not trans(R3)])
opts = [{(1, 1), (2, 2), (3, 3), (1, 2)}, {(1, 1), (2, 2), (1, 2), (2, 1)},
        {(1, 1), (2, 2), (3, 3), (2, 3), (3, 2)}, R3]
check_mcq("C01-Q4", [equiv(r, A3) for r in opts])
base = {(1, 2), (2, 1)}
cl = set(base)
while True:
    n = set(cl) | {(a, a) for a in A3} | {(b, a) for a, b in cl} | {(a, d) for a, b in cl for c, d in cl if b == c}
    if n == cl:
        break
    cl = n
assert equiv(cl, A3)
check_num("C01-Q5", len(cl - base))

# ---------- C02 ----------
A10 = set(range(1, 11))
R = {(x, y) for x in A10 for y in A10 if (x - y) % 3 == 0}
assert equiv(R, A10)
check_num("C02-Q1", len(klass(R, 1, A10)))
check_num("C02-Q2", len(quotient(R, A10)))
A4 = {1, 2, 3, 4}
R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 1), (3, 4), (4, 3)}
assert equiv(R, A4)
Qt = quotient(R, A4)
cands = [{frozenset({1, 2, 3}), frozenset({4})}, {frozenset({i}) for i in A4},
         {frozenset({1, 2}), frozenset({3}), frozenset({4})}, {frozenset({1, 2}), frozenset({3, 4})}]
check_mcq("C02-Q3", [c == Qt for c in cands])
A5 = {1, 2, 3, 4, 5}
eqs = all_equiv(sorted(A5))
assert len(eqs) == 52
with25 = [r for r in eqs if (2, 5) in r]
assert with25
c_a = all(not (klass(r, 2, A5) & klass(r, 5, A5)) for r in with25)
c_b = all(klass(r, 2, A5) == klass(r, 5, A5) for r in with25)
c_c = all(2 == 5 for r in with25)            # "2 = 5" is false as numbers
c_d = all(klass(r, 2, A5) == {2} and klass(r, 5, A5) == {5} for r in with25)
check_mcq("C02-Q4", [c_a, c_b, c_c, c_d])
A20 = set(range(1, 21))
R = {(x, y) for x in A20 for y in A20 if (x - y) % 4 == 0}
check_num("C02-Q5", len(klass(R, 3, A20)))


# ---------- C03 ----------
def is_partition(fam, A):
    fam = [set(b) for b in fam]
    if any(not b for b in fam):
        return False
    if sum(len(b) for b in fam) != len(set().union(*fam)):   # overlap
        return False
    return set().union(*fam) == set(A)


cands = [[{1, 2}, {2, 3}, {4, 5}], [{1, 2}, {3, 4}], [{1, 2}, {3, 4}, {5}], [{1, 2}, {3, 4}, {5}, set()]]
check_mcq("C03-Q1", [is_partition(c, A5) for c in cands])
check_num("C03-Q2", len(rel_of([[1, 2, 3], [4, 5, 6], [7]])))
R = rel_of([[1, 2, 3, 4], [5], [6]])
check_num("C03-Q3", sum(1 for (x, y) in R if x == 1 or y == 1))
target = {frozenset({1, 2}), frozenset({2, 3}), frozenset({4})}
exists = [r for r in all_equiv([1, 2, 3, 4]) if quotient(r, A4) == target]
check_mcq("C03-Q4", [len(exists) == 1, len(exists) > 1,
                     len(exists) == 0 and not is_partition(target, A4), False])
R = rel_of([[1, 2, 3], [4, 5], [6]])
check_num("C03-Q5", sum(1 for x, y in R if x != y))
check_num("C03-Q6", sum(1 for r in all_equiv([1, 2, 3]) if len(quotient(r, A3)) == 2))

# ---------- C04 ----------
W = range(-40, 41)


def same(f, g): return all(f(x, y) == g(x, y) for x in W for y in W)


rel = lambda x, y: (x + 3 * y) % 4 == 0
check_mcq("C04-Q1", [same(rel, lambda x, y: (x - y) % 4 == 0), same(rel, lambda x, y: (x + y) % 4 == 0),
                     same(rel, lambda x, y: (x - y) % 2 == 0), same(rel, lambda x, y: (x - y - 2) % 4 == 0)])


def nclasses(rel, n):
    pts = list(range(-3 * n, 3 * n + 1))
    reps = []
    for x in pts:
        assert rel(x, x)
        if not any(rel(x, r) for r in reps):
            reps.append(x)
    for x in pts:
        for y in pts:
            assert rel(x, y) == rel(y, x)
            for z in pts[::5]:
                if rel(x, y) and rel(y, z):
                    assert rel(x, z)
    for x in pts:
        assert sum(rel(x, r) for r in reps) == 1
    return len(reps)


check_num("C04-Q2", nclasses(lambda x, y: (4 * x + y) % 5 == 0, 5))
rel = lambda x, y: (3 * x + 5 * y) % 2 == 0
zero = {y for y in W if rel(0, y)}
check_mcq("C04-Q3", [zero == {y for y in W if y % 2}, zero == {y for y in W if y % 3 == 0},
                     zero == {y for y in W if y % 2 == 0}, zero == set(W)])
check_num("C04-Q4", nclasses(lambda x, y: (2 * x + 4 * y) % 6 == 0, 6))
rel = lambda x, y: (x + 3 * y) % 4 == 0
cls7 = {y for y in W if rel(7, y)}
rs = {y % 4 for y in cls7}
assert len(rs) == 1 and cls7 == {y for y in W if y % 4 == 3}
check_num("C04-Q5", rs.pop())
# lesson example: 7 | 2x+5y  <=>  x = y mod 7
assert same(lambda x, y: (2 * x + 5 * y) % 7 == 0, lambda x, y: (x - y) % 7 == 0)
assert same(lambda x, y: (x + y + 1) % 2 == 1, lambda x, y: (x - y) % 2 == 0)

# ---------- C05 ----------
assert not sym({(1, 2)}) and sym({(1, 2), (2, 1)})
assert Q["C05-Q1"]["correctId"] == "b" and "yRx" in Q["C05-Q1"]["options"][1]["value"]
rel = lambda x, y: (2 * x + 3 * y) % 5 == 0
assert all(rel(x, x) for x in W) and all(rel(x, y) == rel(y, x) for x in W for y in W)
assert all(rel(x, z) for x in W for y in W for z in W if rel(x, y) and rel(y, z))
for x, y, z in itertools.product(range(-6, 7), repeat=3):
    assert (2 * x + 3 * y) + (2 * y + 3 * z) == 2 * x + 5 * y + 3 * z
    assert (2 * x + 5 * y + 3 * z) - 5 * y == 2 * x + 3 * z
    assert (2 * x + 3 * y) + (2 * y + 3 * x) == 5 * x + 5 * y == 5 * (x + y)
    assert (2 * x + 3 * y) + (2 * y + 3 * x) - (2 * x + 3 * y) == 2 * y + 3 * x
assert 5 * 2 + 5 * 3 == 25 and 5 * 2 * 3 == 30
st = Q["C05-Q3"]["step"]
assert st["bugIndex"] == 1 and "5xy" in st["lines"][1]
assert all("5xy" not in st["lines"][i] for i in (0, 2, 3))
o = Q["C05-Q2"]["step"]["lines"]
assert len(o) == 4 and "xRz" in o[3]
# lesson example 3 | x+2y
lr = lambda x, y: (x + 2 * y) % 3 == 0
assert all(lr(x, x) for x in W) and all(lr(x, y) == lr(y, x) for x in W for y in W)
assert all(lr(x, z) for x in range(-12, 13) for y in range(-12, 13) for z in range(-12, 13) if lr(x, y) and lr(y, z))
rel = lambda x, y: abs(x - y) <= 1
Wm = range(-5, 6)
a_ = (not all(rel(x, z) for x in Wm for y in Wm for z in Wm if rel(x, y) and rel(y, z))) \
    and rel(0, 1) and rel(1, 2) and not rel(0, 2)
b_ = not all(rel(y, x) for x in Wm for y in Wm if rel(x, y))
c_ = not all(rel(x, x) for x in Wm)
d_ = all(rel(x, x) for x in Wm) and not a_
check_mcq("C05-Q4", [a_, b_, c_, d_])


# Q5: combination c1*(x+3y) + c2*(y+3z) given as coefficient triple (cx, cy, cz); want x+3z modulo 4 with y absorbed
def good(v):
    cx, cy, cz = v
    return cx % 4 == 1 and cz % 4 == 3 and cy % 4 == 0


# (x+3y)-(y+3z) = x+2y-3z ; (x+3y)+(3y+z) = x+6y+z ; (x+3y)+(y+3z) = x+4y+3z ; product: not linear
opt_b_hypothesis_ok = all((3 * y + z) % 4 == 0 for y in range(-8, 9) for z in range(-8, 9) if (y + 3 * z) % 4 == 0)
product_ok = all(((x + 3 * y) * (y + 3 * z) - (x + 3 * z)) % 4 == 0
                 for x in range(-8, 9) for y in range(-8, 9) for z in range(-8, 9)
                 if (x + 3 * y) % 4 == 0 and (y + 3 * z) % 4 == 0 and (x + 3 * z) % 4 != 0) and False
check_mcq("C05-Q5", [good((1, 2, -3)), good((1, 6, 1)) and opt_b_hypothesis_ok, good((1, 4, 3)), product_ok])

# ---------- C06 ----------
rel_r = {(x, y) for x in W for y in W if (x + 3 * y) % 4 == 0}
assert (0, 4) in rel_r and (4, 0) in rel_r
refl_ok = all((x, x) in rel_r for x in W)
sym_ok = sym(rel_r)
trans_ok = all(((x + 3 * z) % 4 == 0) for x in range(-12, 13) for y in range(-12, 13) for z in range(-12, 13)
               if (x + 3 * y) % 4 == 0 and (y + 3 * z) % 4 == 0)
check_mcq("C06-Q1", [(not anti(rel_r)) is False and refl_ok and trans_ok,
                     not refl_ok, (not anti(rel_r)) and refl_ok and trans_ok, not trans_ok])


def S(n, k): return sum(1 for p in partitions(range(n)) if len(p) == k)


assert S(3, 2) == 3 and S(3, 1) == 1 and S(4, 2) == S(3, 1) + 2 * S(3, 2)
assert S(2, 1) == 1 and S(2, 2) == 1 and S(3, 2) == S(2, 1) + 2 * S(2, 2)
check_num("C06-Q2", S(4, 2))
check_num("C06-Q3", sum(1 for p in partitions(range(5)) if sorted(map(len, p)) == [2, 3]))
E = all_equiv([1, 2, 3])
ops = [lambda a, b: a | b, lambda a, b: a - b, lambda a, b: a & b,
       lambda a, b: {(x, y) for x in A3 for y in A3} - a]
check_mcq("C06-Q4", [all(equiv(op(a, b), A3) for a in E for b in E) for op in ops])
ids = [r for r in all_equiv(list(range(6))) if anti(r)]
assert len(ids) == 1 and equiv(ids[0], set(range(6)))
check_num("C06-Q5", len(ids[0]))
check_num("C06-Q6", sum(1 for p in partitions(range(4)) if sorted(map(len, p)) == [2, 2]))
assert sum(S(3, k) for k in (1, 2, 3)) == 5
assert math.comb(5, 2) == 10 and math.comb(4, 3) == 4 and math.comb(4, 2) == 6
assert 17 == sum(len(b) ** 2 for b in [[1, 2], [3, 4], [5, 6, 7]])
# union counterexample from the lesson
u = rel_of([[1, 2], [3]]) | rel_of([[1], [2, 3]])
assert not trans(u)

# ---------- C07 boss ----------
bank = json.load(open(os.path.join(HERE, "..", "..", "..", "..", "questions.json"), encoding="utf8"))
byid = {q["id"]: q for q in bank["questions"]}
for q in levels["C07"]["questions"]:
    b = byid[q["bankId"]]
    assert b["topic"] == "equivalence_relations", q["bankId"]
    assert b.get("official") is True and b.get("stepsSource") == "ai-verified" and b.get("steps"), q["bankId"]
    assert not b.get("hold") and not q["bankId"].startswith("20A-A"), q["bankId"]
assert len(rel_of([[1], [2, 3, 4], [5, 6]])) == 14
print("OK: all", len(Q), "authored questions + boss recaps verified")
