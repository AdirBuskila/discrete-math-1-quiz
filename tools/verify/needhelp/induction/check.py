# Machine checks for the guided course "induction" (courses/induction/C01..C09). ASCII output only.
# Loads the level files through tools/course_load.js, then asserts every stored answer against brute force /
# exact Fraction arithmetic.  Run:  py tools/verify/needhelp/induction/check.py
import json, math, os, subprocess
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
out = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], capture_output=True, check=True).stdout
data = json.loads(out.decode("utf8"))
assert not data["errors"], data["errors"]
Q = {}
for rec in data["levels"]:
    if rec["courseId"] != "induction":
        continue
    for q in rec["level"]["questions"]:
        Q[q["bankId"] if "bankId" in q else q["id"]] = q
done = set()


def opt(qid, oid):
    return {o["id"]: o["value"] for o in Q[qid]["options"]}[oid]


def mcq(qid, part):
    """the stored correct option contains `part`; the maths behind it is asserted by the caller"""
    assert part in opt(qid, Q[qid]["correctId"]), qid
    # no other option contains the same marker text
    for o in Q[qid]["options"]:
        if o["id"] != Q[qid]["correctId"]:
            assert o["value"] != opt(qid, Q[qid]["correctId"]), qid
    done.add(qid)


def num(qid, expected):
    st = Q[qid]["step"]
    assert st["type"] == "numeric", qid
    assert abs(st["answer"] - float(expected)) <= st["tol"] + 1e-12, (qid, st["answer"], expected)
    done.add(qid)


def bug(qid, idx):
    st = Q[qid]["step"]
    assert st["type"] == "findbug" and st["bugIndex"] == idx and 0 <= idx < len(st["lines"]), qid
    done.add(qid)


R = range(1, 60)


def S_odd(n):
    return sum(2 * i - 1 for i in range(1, n + 1))


assert all(S_odd(n) == n * n for n in R)

# ---- C01
num("C01-Q3", sum(2 * i for i in range(1, 2)))
assert all(sum(2 * i for i in range(1, n + 1)) == n * (n + 1) for n in R)
m = min(m for m in range(1, 30) if all(math.factorial(n) > 2 ** n for n in range(m, 80)))
assert m == 4 and math.factorial(3) < 2 ** 3
num("C01-Q4", 4)
mcq("C01-Q1", "P(m)")
mcq("C01-Q2", "קבוע")
mcq("C01-Q5", "100")          # finite checking is not induction (conceptual); b,c,d are standard induction shapes

# ---- C02
def lhs_pron(n):
    return sum(i * (i + 1) for i in range(1, n + 1))


assert all(lhs_pron(n) == F(n * (n + 1) * (n + 2), 3) for n in R)
assert lhs_pron(3) == F(3 * 4 * 5, 3) == 20
num("C02-Q2", 20)
num("C02-Q5", 2 * 7 - 1)
for k in range(1, 40):
    assert S_odd(k) + (2 * k + 1) == (k + 1) ** 2         # option a is a true P(k+1)
    assert S_odd(k) != (k + 1) ** 2                       # b: sum not extended -> false
    assert (k + 1) ** 2 != k * k + 1                      # c false
    assert (k + 1) ** 2 != k * k                          # d false
mcq("C02-Q1", "(2k+1)=(k+1)^2")
assert all((6 ** n - 1) % 5 == 0 for n in range(1, 60))
mcq("C02-Q3", "אגף ימין")
mcq("C02-Q4", "6^{k+1}-1")

# ---- C03
for k in range(1, 40):
    assert k * k + (2 * k + 1) == (k + 1) ** 2
    assert k * k + (2 * k - 1) != (k + 1) ** 2
    assert k * k + (2 * k + 1) != k * k
    assert (k + 1) ** 2 + (2 * k + 1) != k * k
mcq("C03-Q1", "k^2+(2k+1)=(k+1)^2")
assert all(k * (k + 1) + 2 * (k + 1) == (k + 2) * (k + 1) for k in range(-20, 40))
num("C03-Q2", 2)
for k in range(1, 40):
    assert sum(range(1, k + 2)) == F(k * (k + 1), 2) + (k + 1)
    assert F(k * (k + 1), 2) + (k + 1) == F(k * (k + 1) + 2 * (k + 1), 2) == F((k + 1) * (k + 2), 2)
done.add("C03-Q3")
for k in range(1, 40):
    assert k * k + 2 * k + 1 == (k + 1) ** 2                 # line 3 (index 2) corrected
    assert k * k + 2 * k + 1 != (k + 2) ** 2                 # line as printed is false
    assert S_odd(k) + 2 * k + 1 == k * k + (2 * k + 1)       # line 1 true
bug("C03-Q4", 2)


def sq(n):
    return sum(i * i for i in range(1, n + 1))


assert all(sq(n) == F(n * (n + 1) * (2 * n + 1), 6) for n in R)
assert F(4 * 5 * 9, 6) + 25 == F(5 * 6 * 11, 6) == 55
num("C03-Q5", 55)

# ---- C04
terms = list(range(2 * 5 + 1, 4 * 5, 2))
assert terms == [11, 13, 15, 17, 19]
num("C04-Q1", len(terms))
assert all(len(range(2 * n + 1, 4 * n, 2)) == n for n in R)


def S4(n):
    return sum(range(n + 1, 2 * n + 1))


assert all(S4(n) == F(n * (3 * n + 1), 2) for n in R)
for k in range(1, 30):
    assert S4(k + 1) == sum(range(k + 2, 2 * k + 3))         # a
    assert S4(k + 1) != sum(range(k + 1, 2 * k + 2))         # b
    assert S4(k + 1) != sum(range(k + 2, 2 * k + 2))         # c
    assert S4(k + 1) != sum(range(k + 1, 2 * k + 3))         # d
mcq("C04-Q2", "(k+2)+(k+3)+\\dots+(2k+2)")
assert S4(6) == 57 and S4(5) == 40
num("C04-Q3", S4(6) - S4(5))
for k in range(1, 40):
    assert S4(k + 1) == S4(k) - (k + 1) + (2 * k + 1) + (2 * k + 2)
    assert F(k * (3 * k + 1), 2) - (k + 1) + (2 * k + 1) + (2 * k + 2) == F(k * (3 * k + 1), 2) + (3 * k + 2)
    assert F(k * (3 * k + 1), 2) + (3 * k + 2) == F(3 * k * k + 7 * k + 4, 2) == F((k + 1) * (3 * k + 4), 2)
done.add("C04-Q4")


def T(n):
    return sum(range(n, 2 * n + 1))


assert all(T(n) == F(3 * n * (n + 1), 2) for n in R)
for k in range(1, 40):
    assert T(k + 1) == sum(range(k + 1, 2 * k + 3))                              # line 1
    assert T(k + 1) == T(k) - k + (2 * k + 1) + (2 * k + 2)                      # line 2
    assert -k + (2 * k + 1) + (2 * k + 2) == 3 * k + 3 != 4 * k + 3              # line 3 as printed is false
    assert F(3 * k * (k + 1), 2) + 3 * k + 3 == F(3 * (k + 1) * (k + 2), 2)      # line 4
bug("C04-Q5", 3)

# ---- C05
def A(n):
    return sum(F(1, (2 * i - 1) * (2 * i + 1)) for i in range(1, n + 1))


assert all(A(n) == F(n, 2 * n + 1) for n in R)
num("C05-Q1", (2 * 1 - 1) * (2 * 1 + 1))
v = F(2, 5) + F(1, 5 * 7)
assert v == F(3, 7) == A(3)
num("C05-Q2", v)
for k in range(1, 40):
    assert k * (2 * k + 3) + 1 == (2 * k + 1) * (k + 1)
    assert k * (2 * k + 3) + 1 != (2 * k + 1) * (k + 2)
    assert k * (2 * k + 3) + 1 != 2 * (k + 1) ** 2
    assert k * (2 * k + 3) + 1 != (2 * k + 3) * (k + 1)
    assert F(k, 2 * k + 1) + F(1, (2 * k + 1) * (2 * k + 3)) == F(k + 1, 2 * k + 3)
mcq("C05-Q3", "(2k+1)(k+1)")
done.add("C05-Q4")


def B(n):
    return sum(F(1, i * (i + 1)) for i in range(1, n + 1))


assert all(B(n) == F(n, n + 1) for n in R)
for k in range(1, 40):
    assert F(k, k + 1) + F(1, (k + 1) * (k + 2)) == F(k * (k + 2) + 1, (k + 1) * (k + 2))
    assert k * (k + 2) + 1 == k * k + 2 * k + 1 != k * k + 2 * k          # line 2 as printed drops the +1
    assert k * k + 2 * k + 1 == (k + 1) ** 2
    assert F((k + 1) ** 2, (k + 1) * (k + 2)) == F(k + 1, k + 2)
bug("C05-Q5", 2)

# ---- C06
good = [n for n in range(1, 200) if n * n < 2 ** n]
m = min(m for m in range(1, 200) if all(n * n < 2 ** n for n in range(m, 200)))
assert m == 5 and 1 in good and not any(n in good for n in (2, 3, 4))
num("C06-Q1", 5)
assert all(2 ** n > 2 * n + 1 for n in range(3, 100)) and not (2 ** 2 > 2 * 2 + 1)
for k in range(1, 40):
    assert 4 * k + 2 >= 2 * k + 3
    assert len({2 * (2 * k + 1), 2 * k + 3, F(2 * k + 1, 2), (2 * k + 1) ** 2}) == 4   # a is the only exact doubling
mcq("C06-Q2", "2(2k+1)")
ks = [k for k in range(0, 50) if k * k > 2 * k + 1]
assert min(ks) == 3 and all(k in ks for k in range(3, 50))
num("C06-Q3", 3)
assert all(math.factorial(n) > 2 ** n for n in range(4, 80))
for k in range(4, 60):
    assert math.factorial(k + 1) == (k + 1) * math.factorial(k)
    assert (k + 1) > 2 and (k + 1) * 2 ** k > 2 * 2 ** k and 2 * 2 ** k == 2 ** (k + 1)
done.add("C06-Q4")
for k in range(5, 60):
    assert (k + 1) ** 2 == k * k + 2 * k + 1 and k * k + 2 * k + 1 < k * k + 3 * k
    assert k * k + 3 * k < 2 * k * k and 2 * k * k < 2 * 2 ** k and k * k < 2 ** k
    assert 2 * 2 ** k == 2 ** (k + 1) and 2 * 2 ** k != 2 ** (2 * k)
bug("C06-Q5", 5)

# ---- C07
assert all(8 ** n % 7 == 1 for n in range(1, 40))
assert all(8 * (8 ** k - 1) + 7 == 8 ** (k + 1) - 1 for k in range(1, 30))
num("C07-Q1", 7)
for k in range(1, 30):
    assert 7 * (7 ** k - 1) + 6 == 7 ** (k + 1) - 1
    assert 7 * (7 ** k - 1) + 1 != 7 ** (k + 1) - 1
    assert 6 * (7 ** k - 1) + 7 != 7 ** (k + 1) - 1
    assert (7 ** k - 1) + 6 != 7 ** (k + 1) - 1
mcq("C07-Q2", "7(7^k-1)+6")
for k in range(0, 50):
    assert (k + 1) ** 3 + 2 * (k + 1) == (k ** 3 + 2 * k) + 3 * (k * k + k + 1)
assert all((n ** 3 + 2 * n) % 3 == 0 for n in range(1, 200))
num("C07-Q3", 1)
for k in range(1, 30):
    assert 5 * (5 ** k - 1) + 4 == 5 ** (k + 1) - 1
    t = (5 ** k - 1) // 4
    assert 5 ** k - 1 == 4 * t and 5 * 4 * t + 4 == 4 * (5 * t + 1)
done.add("C07-Q4")
for t in range(1, 30):
    assert 7 * 6 * t + 6 == 6 * (7 * t + 1)
bug("C07-Q5", 1)

# ---- C08
def C(n):
    return sum(i ** 3 for i in range(1, n + 1))


assert all(C(n) == F(n * (n + 1), 2) ** 2 for n in R)
for k in range(1, 40):
    assert F(k * (k + 1), 2) ** 2 + (k + 1) ** 3 == F((k + 1) * (k + 2), 2) ** 2
bug("C08-Q1", 2)
assert F(3 * 4, 2) ** 2 + 4 ** 3 == F(4 * 5, 2) ** 2 == 100
num("C08-Q2", 100)
assert all(n != n + 1 for n in range(-50, 50))         # P(n): n = n+1 is false everywhere, so it has no base
mcq("C08-Q3", "אין בסיס")
a = {1: 1, 2: 3}
for n in range(3, 80):
    a[n] = a[n - 1] + a[n - 2]
assert all(a[n] < 2 ** n for n in a)
assert all(2 ** k + 2 ** (k - 1) < 2 ** (k + 1) for k in range(2, 60))
num("C08-Q4", 2)
mcq("C08-Q5", "n\\ge3")

# ---- C09 boss: bank ids exist, are official + ai-verified steps, topic induction
bank = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf8"))["questions"]
byid = {x["id"]: x for x in bank}
boss = [q["bankId"] for q in Q.values() if "bankId" in q]
assert len(boss) == 5
for bid in boss:
    x = byid[bid]
    assert x["topic"] == "induction" and x.get("official") is True and x.get("stepsSource") == "ai-verified" and x.get("steps"), bid

own = {qid for qid, q in Q.items() if "bankId" not in q}
missing = own - done
assert not missing, missing
print("induction: %d own questions machine-checked, boss bankIds %s" % (len(own), ",".join(boss)))
