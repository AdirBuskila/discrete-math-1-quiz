# Machine check of every stored answer in courses/number_theory (C01..C07; C08 is bank ids).
# Run: PYTHONUTF8=1 py tools/verify/needhelp/number_theory/check.py   (ASCII output only)
import json, subprocess, os, re
from math import factorial as F, gcd
from sympy import totient, isprime, factorint

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
out = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], capture_output=True, check=True, cwd=ROOT)
data = json.loads(out.stdout.decode("utf8"))
assert not data["errors"], data["errors"]
Q = {}
for e in data["levels"]:
    if e["courseId"] != "number_theory":
        continue
    for q in e["level"]["questions"]:
        Q[q.get("id") or q["bankId"]] = q

# numeric answers: id -> independently computed value
NUM = {
    "C01-Q1": 123 % 7,
    "C01-Q3": (17 * 23 + 8) % 5,
    "C01-Q4": (-17) % 5,
    "C01-Q5": pow(7, 100, 10),
    "C02-Q1": pow(5, 12, 13),
    "C02-Q2": pow(4, 30, 31),
    "C02-Q4": pow(22, 10, 11),
    "C03-Q1": 100 % 6,
    "C03-Q3": pow(5, 100, 7),
    "C03-Q4": pow(2, 100, 13),
    "C03-Q5": pow(38, 25, 13),
    "C03-Q6": (16 ** 15 + 7 ** 60 + 37) % 31,
    "C04-Q1": 36 // 12,
    "C05-Q1": F(10) % 11,
    "C05-Q2": F(12) % 13,
    "C05-Q4": (F(12) + 20) % 13,
    "C06-Q1": int(totient(13)),
    "C06-Q2": int(totient(36)),
    "C06-Q3": int(totient(100)),
    "C06-Q4": int(totient(32) * totient(9)),
    "C06-Q6": pow(7, int(totient(10)), 10),
    "C07-Q1": 41,
    "C07-Q2": 150 // 30,
    "C07-Q4": (50 ** 24 + F(12)) % 13,
}
for qid, want in NUM.items():
    st = Q[qid]["step"]
    assert st["type"] == "numeric" and st["answer"] == want and st["tol"] == 0, (qid, st["answer"], want)
# a few derived claims inside explanations / question setup
assert isprime(41) and isprime(13) and 40 + 1 == 41 and 150 % 30 == 0 and 36 % 12 == 0
assert 3 ** 36 == (3 ** 3) ** 12 and 27 % 13 != 0 and (3 ** 36 - 1) % 13 == 0
assert 100 ** 150 == (100 ** 5) ** 30 and (100 ** 5) % 31 != 0
assert (F(30) + 1) % 31 == 0 and (100 ** 150 - 1) % 31 == 0
assert [pow(7, k, 10) for k in (1, 2, 3, 4)] == [7, 9, 3, 1] and 100 % 4 == 0
assert F(10) % 11 == 10 and 119 == 17 * 7 and 399 == 17 * 23 + 8 and 399 % 5 == 4
assert 100 == 16 * 6 + 4 and pow(2, 4, 7) == 2 and 625 % 7 == 2 and 100 == 8 * 12 + 4 and 38 % 13 == 12
assert 3 ** 50 % 10 == 9 and 50 % 4 == 2 and 26 * 31 + 4 == 810 and 810 % 5 == 0
assert 729 % 7 == 1 and 1024 % 11 == 1 and pow(2, 12, 7) == 1 and (6 * 7 + 1) == 43  # fermat examples
assert 720 % 7 == 6 and 721 == 7 * 103
assert pow(4, 30, 31) == 1 and pow(49, 30, 31) == 1 and pow(4, 30, 31) + pow(49, 30, 31) + 37 == 39 and 39 % 31 == 8
assert pow(5, 3) == 125 and 125 % 7 == 6 and 125 == 17 * 7 + 6 and (5 ** 18 - 1) % 7 == 0
assert totient(10) == 4 and totient(120) == 32 and totient(15) == 8 and totient(4) == 2 and totient(2) ** 2 == 1
assert totient(288) == 96 and totient(32) == 16 and totient(9) == 6

# mcq: the correct option is the only one with the property
def only_correct(qid, pred_by_option):
    q = Q[qid]
    ids = [o["id"] for o in q["options"]]
    assert sorted(pred_by_option) == sorted(ids), qid
    good = [i for i in ids if pred_by_option[i]]
    assert good == [q["correctId"]], (qid, good, q["correctId"])

only_correct("C01-Q2", {"a": 35 % 8 == 3, "b": 29 % 8 == 3, "c": 41 % 8 == 3, "d": 18 % 8 == 3})
# C02-Q3: Fermat does NOT apply (and m^10 != 1) exactly for m = 22
only_correct("C02-Q3", {"a": pow(22, 10, 11) != 1, "b": pow(10, 10, 11) != 1, "c": pow(3, 10, 11) != 1, "d": pow(12, 10, 11) != 1})
only_correct("C03-Q2", {"a": 6 == 7 - 1, "b": False, "c": False, "d": False})
# the exponent really cycles with period p-1=6 and NOT with 7 (checked for all bases coprime to 7)
assert all(pow(m, 6, 7) == 1 for m in range(1, 7)) and pow(5, 100, 7) != pow(5, 100 % 7, 7)
only_correct("C04-Q2", {"a": (2 ** 20 - 1) % 11 == 0, "b": (2 ** 15 - 1) % 11 == 0, "c": (2 ** 25 - 1) % 11 == 0, "d": (5 ** 14 - 1) % 11 == 0})
assert (2 ** 15 - 1) % 11 == 9 and (2 ** 25 - 1) % 11 == 9 and (5 ** 14 - 1) % 11 == 8   # explanation: -2, 9, 8
assert (10 ** 8 - 1) % 5 == 4 and (10 ** 8) % 5 == 0 and isprime(5) and 8 % 4 == 0
only_correct("C04-Q3", {"a": (10 ** 8) % 5 == 0 and (10 ** 8 - 1) % 5 == 4, "b": not isprime(5), "c": False, "d": False})
only_correct("C05-Q3", {"a": (F(10) + 1) % 11 == 0, "b": (F(11) + 1) % 11 == 0, "c": (F(10) - 1) % 11 == 0, "d": (F(9) + 1) % 11 == 0})
assert F(11) % 11 == 0 and (F(10) - 1) % 11 == 9 and F(9) % 11 == 1 and (F(9) + 1) % 11 == 2
only_correct("C05-Q5", {"a": F(30) % 29 == 0, "b": F(30) % 31 == 0, "c": F(30) % 37 == 0, "d": F(30) % 41 == 0})
assert all(isprime(p) for p in (29, 31, 37, 41))
# C06-Q5: phi(pq) = (p-1)(q-1) for all distinct prime pairs; the distractors are not
from sympy import primerange
prs = list(primerange(2, 60))
pairs = [(p, q) for p in prs for q in prs if p != q]
assert all(totient(p * q) == (p - 1) * (q - 1) for p, q in pairs)
assert all(totient(p * q) != p * q - 1 for p, q in pairs)
assert any(totient(p * q) != p + q - 2 for p, q in pairs) and totient(15) not in (15 - 1, 3 + 5 - 2, (3 - 1) + (5 - 1) + 1)
only_correct("C06-Q5", {"a": True, "b": False, "c": False, "d": False})
# C07-Q3 (conceptual, checked by brute force): n | gcd(A,B) iff n | A and n | B; for coprime parts, 2|X and 23|X <=> 46|X
assert all(((x % 2 == 0 and x % 23 == 0) == (x % 46 == 0)) for x in range(1, 5000))
# distractors fail: (23|A and 2|B) does not give 46|gcd; 23|A,B alone gives only 23|gcd; 46|(A+B) says nothing
A, B = 23, 2 * 5
assert not (A % 46 == 0 and B % 46 == 0)
A, B = 23, 46 * 7
assert A % 23 == 0 and B % 23 == 0 and gcd(A, B) % 46 != 0
A, B = 1, 45
assert (A + B) % 46 == 0 and gcd(A, B) % 46 != 0
only_correct("C07-Q3", {"a": True, "b": False, "c": False, "d": False})

# order steps: every claim line holds (C02-Q5, C04-Q4)
assert pow(2, 6, 7) == 1 and (2 ** 12 - 1) % 7 == 0 and 7 % 2 != 0
assert 5 ** 18 == 125 ** 6 and (125 ** 6 - 1) % 7 == 0
assert Q["C02-Q5"]["step"]["type"] == "order" and len(Q["C02-Q5"]["step"]["lines"]) == 3
assert Q["C04-Q4"]["step"]["type"] == "order" and len(Q["C04-Q4"]["step"]["lines"]) == 3

# findbug: the buggy line is the false one, every other line true
# C04-Q5  (13 | 8^24 - 1)
assert 8 ** 24 == 64 ** 12 and 64 % 13 != 0 and 64 == 4 * 13 + 12 and pow(64, 12, 13) == 1
assert pow(64, 13, 13) != 1                       # line 2 (the bug) is false
assert Q["C04-Q5"]["step"]["bugIndex"] == 2 and (8 ** 24 - 1) % 13 == 0
# C05-Q6  (17 | 16! + 18)
assert (F(16) + 1) % 17 == 0 and F(16) + 18 == (F(16) + 1) + 17
assert (F(17) + 1) % 17 != 0                      # line 0 (the bug) is false
assert Q["C05-Q6"]["step"]["bugIndex"] == 0 and (F(16) + 18) % 17 == 0
# C07-Q5  (19 < gcd(5^44 - 1, 8^88 + 22!), via 23)
assert isprime(23) and 5 ** 44 == 25 ** 22 and 25 % 23 != 0 and (5 ** 44 - 1) % 23 == 0
assert 8 ** 88 == (2 ** 12) ** 22 and 8 ** 88 + F(22) == ((2 ** 12) ** 22 - 1) + (F(22) + 1)
assert 8 ** 88 != (2 ** 12) ** 23                 # line 2 (the bug) is false
assert ((2 ** 12) ** 22 - 1) % 23 == 0 and (F(22) + 1) % 23 == 0
assert gcd(5 ** 44 - 1, 8 ** 88 + F(22)) % 23 == 0 and 19 < 23 <= gcd(5 ** 44 - 1, 8 ** 88 + F(22))
assert Q["C07-Q5"]["step"]["bugIndex"] == 2

# every stored mcq has exactly the declared correct option present; every level has 4-6 questions
for e in data["levels"]:
    if e["courseId"] != "number_theory":
        continue
    L = e["level"]
    n = len(L["questions"])
    assert (4 <= n <= 6), (L["id"], n)
    for q in L["questions"]:
        if "options" in q:
            assert q["correctId"] in [o["id"] for o in q["options"]]

# boss bank ids (official / lecturer-solution, ai-verified steps), checked against the built bank
bank = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf8"))
bank = {x["id"]: x for x in (bank["questions"] if isinstance(bank, dict) else bank)}
boss = [q["bankId"] for q in Q.values() if "bankId" in q]
assert len(boss) == 4
for b in boss:
    assert bank[b]["topic"] == "modular_fermat_wilson" and bank[b].get("official") is True, b
# the boss claims, recomputed
assert (F(30) + 1) % 31 == 0 and (100 ** 150 - 1) % 31 == 0 and 30 <= gcd(F(30) + 1, 100 ** 150 - 1)
n = 2 ** 120 - 1
assert n % 11 == 0 and (5 ** 20 + F(10) + F(12)) % 11 == 0
assert all((71 ** 120 - 1) % 26 == 0 and (50 ** 24 + F(12)) % 26 == 0 for _ in [0])
assert 74 <= gcd(36 ** 36 + F(36), 7 ** 72 - 1)

print("number_theory check OK:", len(NUM), "numeric,", len(boss), "boss ids")
