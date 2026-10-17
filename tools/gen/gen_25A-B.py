# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-B.json -- discrete math 1, semester A 5785, moed B (09.03.2025).
4 mandatory questions of 25 points. Key: the lecturer's solution (typed tables and handwriting) on the exam pages.
Run: PYTHONUTF8=1 py tools/gen/gen_25A-B.py
A part with numbered sub-claims ((1), (2)) is ONE item."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-B.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution", "official": True, "confidence": "high"}
    q.update(kw)
    return q


INTRO = "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה הקשורה אליו.\n"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "computation", "logic_propositional", 10,
      INTRO + "**המונח:** צורת CNF של פסוק.\n"
      r"**שאלה:** מצאו על ידי טבלת אמת את צורת ה-CNF של הפסוק: $(p\vee\neg q)\to r$",
      "טבלת אמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | ¬q | p∨¬q | (p∨¬q)→r\n"
      "T T T |  F |   T  |    T\n"
      "T T F |  F |   T  |    F\n"
      "T F T |  T |   T  |    T\n"
      "T F F |  T |   T  |    F\n"
      "F T T |  F |   F  |    T\n"
      "F T F |  F |   F  |    T\n"
      "F F T |  T |   T  |    T\n"
      "F F F |  T |   T  |    F\n"
      "```\n"
      "צורת ה-CNF (מכפלה של פסוקיות, אחת לכל שורה שבה הפסוק שקר) היא:\n"
      r"$$(\neg p\vee\neg q\vee r)\wedge(\neg p\vee q\vee r)\wedge(p\vee q\vee r)$$"),

    Q(1, "ב", "computation", "sets_power_set", 8,
      INTRO + "**המונח:** קבוצת החזקה.\n"
      r"**שאלה:** תהי $A=\{1,2,3,\dots,10\}$. כמה תתי-קבוצות $B$ של $A$ מקיימות את התנאי: $\{1,2\}\subseteq B$ ?",
      r"$B$ מקיימת את התנאי אם ורק אם $\{1,2\}\subseteq B\wedge B\subseteq A$. לכן הצורה של $B$ היא: "
      r"$B=\{1,2\}\cup C$, כאשר $C\subseteq\{3,4,\dots,10\}$."
      "\n"
      r"לכן מספר תתי-הקבוצות הוא $2^{|\{3,4,\dots,10\}|}=|P(\{3,4,\dots,10\})|=2^8=256$."),

    Q(1, "ג", "computation", "functions", 7,
      INTRO + "**המונח:** פונקציה על.\n"
      r"**שאלה:** מצאו קבוצה $A$ כך שהפונקציה $f:\mathbb{N}^*\to A$ היא על, כאשר $f$ מוגדרת לפי הכלל "
      r"$f(x)=\gcd(12,x)$ לכל $x\in\mathbb{N}^*$.",
      r"נחשב: $f(1)=\gcd(12,1)=1$, $f(2)=\gcd(12,2)=2$, $f(3)=\gcd(12,3)=3$, $f(4)=\gcd(12,4)=4$, "
      r"$\gcd(12,6)=6=f(6)$, $\gcd(12,12)=12=f(12)$."
      "\n"
      r"לכן עבור $A=\{1,2,3,4,6,12\}$, קבוצת המחלקים של 12, הפונקציה $f:\mathbb{N}^*\to A$ היא על."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 12,
      r"הוכיחו באינדוקציה מתמטית שלכל $1\le n\in\mathbb{N}$ מתקיים: $11\mid(23^n-1)$.",
      r"נסמן $P(n):\ 11\mid(23^n-1)$."
      "\n"
      r"**I. בסיס:** $P(1)$: $11\mid(23^1-1)\iff 11\mid 22\Rightarrow\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=\text{TRUE}\Rightarrow P(k+1)=\text{TRUE}$ עבור $1\le k\in\mathbb{N}$."
      "\n"
      r"$P(k):\ 11\mid(23^k-1)$, $\quad P(k+1):\ 11\mid(23^{k+1}-1)$."
      "\n"
      r"$$23^{k+1}-1=23\cdot 23^k-1=23\cdot 23^k-23+22=23\,(23^k-1)+2\cdot 11$$"
      "\n"
      r"המחובר הראשון מתחלק ב-11 לפי הנחת האינדוקציה, והמחובר השני $2\cdot 11$ מתחלק ב-11. לכן $11\mid(23^{k+1}-1)$, "
      r"כלומר $P(k+1)=\text{TRUE}$."
      "\n"
      r"מסקנה: מ-I ו-II, לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$."),

    Q(2, "ב", "computation", "cardinality_sets", 5,
      r"יהיו הקבוצות: $A=\{5^n\cdot 7^m:\ m,n\in\{0,1,2,\dots,9\}\}$, $B=\{5^n:\ n\in\{0,1,2,\dots,9\}\}$ "
      r"ו-$C=\{7^n:\ n\in\{0,1,2,\dots,9\}\}$."
      "\n"
      r"חשבו את $|P(A)\times P(B\cup C)|$.",
      r"$|A|=100\Rightarrow|P(A)|=2^{100}$."
      "\n"
      r"$B\cup C=\{1,5,\dots,5^9,7,7^2,\dots,7^9\}\Rightarrow|B\cup C|=19\Rightarrow|P(B\cup C)|=2^{19}$."
      "\n"
      r"$$|P(A)\times P(B\cup C)|=|P(A)|\cdot|P(B\cup C)|=2^{100}\cdot 2^{19}=2^{119}$$"),

    Q(2, "ג", "proof", "equivalence_relations", 8,
      r"תהי $A=\{1,2,3,\dots,10\}$. הראו שהיחס $R\subseteq P(A)\times P(A)$ שמוגדר לפי הכלל "
      r"לכל $B,C\in P(A)$ מתקיים: $B\cap\{1\}=C\cap\{1\}\iff BRC$"
      "\n"
      r"הוא יחס שקילות ומצאו את $P(A)/R$.",
      r"**רפלקסיביות:** לכל $B\in P(A)$ מתקיים $B\cap\{1\}=B\cap\{1\}$, ולכן $BRB$."
      "\n"
      r"**סימטריות:** $BRC\iff B\cap\{1\}=C\cap\{1\}\Rightarrow C\cap\{1\}=B\cap\{1\}\Rightarrow CRB$."
      "\n"
      r"**טרנזיטיביות:** $BRC\iff B\cap\{1\}=C\cap\{1\}$ וגם $CRD\iff C\cap\{1\}=D\cap\{1\}$, ולכן $B\cap\{1\}=D\cap\{1\}$, כלומר $BRD$."
      "\n"
      r"לכן $R$ הוא יחס שקילות."
      "\n"
      r"מחלקות השקילות:"
      "\n"
      r"$[\emptyset]=\{B:\ B\in P(A)\wedge BR\emptyset\}=\{B:\ B\in P(A)\wedge 1\notin B\}=P(A-\{1\})$"
      "\n"
      r"$[\{1\}]=\{B:\ B\in P(A)\wedge BR\{1\}\}=\{B:\ B\in P(A)\wedge 1\in B\}=\{B:\ B=\{1\}\cup C\wedge C\subseteq A-\{1\}\}$"
      "\n"
      r"מכיוון ש-$\emptyset\cap\{1\}=\emptyset$ ו-$\{1\}\cap\{1\}=\{1\}$ הן שתי תוצאות שונות, אין עוד מחלקות, ולכן "
      r"$P(A)/R=\{[\emptyset],[\{1\}]\}$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "partial_orders", 12,
      r"תהי $A=\{1,2,3,6,8,9,16,18\}$ ויהי $R\subseteq A\times A$ שמוגדר לפי הכלל הבא: "
      r"לכל $x,y\in A$ מתקיים $xRy\iff x\mid y$."
      "\n"
      r"(1) הוכיחו ש: $R$ הוא יחס סדר חלקי."
      "\n"
      r"(2) האם $R$ הוא יחס סדר מלא ?",
      r"**(1)** **רפלקסיביות:** לכל $x\in A$ מתקיים $x\mid x$, ולכן $xRx$."
      "\n"
      r"**אנטי-סימטריות:** נניח $xRy$ וגם $yRx$. אז $x\mid y$ וגם $y\mid x$, ולכן $1\le x\le y$ וגם $1\le y\le x$, כלומר $x=y$."
      "\n"
      r"**טרנזיטיביות:** נניח $xRy$ וגם $yRz$. אז $x\mid y$ וגם $y\mid z$, ולכן $x\mid z$, כלומר $xRz$."
      "\n"
      r"לכן $R$ הוא יחס סדר חלקי."
      "\n"
      r"**(2)** $R$ אינו יחס סדר מלא: $(2,3)\notin R$ וגם $(3,2)\notin R$, כלומר 2 ו-3 אינם ברי השוואה."),

    Q(3, "ב", "computation", "number_theory_gcd", 7,
      r"מצאו על ידי האלגוריתם המורחב של Euclid שני מספרים $x,y\in\mathbb{Z}$ כך ש: $\gcd(48,84)=48\cdot x+84\cdot y$.",
      "הטבלה של האלגוריתם המורחב (בכל שורה: $d$ הוא ה-gcd, ו-$x\\leftarrow y'$ ו-$y\\leftarrow x'-y'\\cdot\\lfloor a/b\\rfloor$ "
      "מחושבים מהשורה שמתחת):\n"
      "```\n"
      "  a    b    floor(a/b)   d    x    y\n"
      "  84   48        1       12   -1    2\n"
      "  48   36        1       12    1   -1\n"
      "  36   12        3       12    0    1\n"
      "  12    0       --       12    1    0\n"
      "```\n"
      r"$$12=\gcd(48,84)=\gcd(84,48)=(-1)\cdot 84+2\cdot 48$$"
      "\n"
      r"כלומר $x=2,\ y=-1$."),

    Q(3, "ג", "proof", "sets_power_set", 6,
      r"אם $A,B,C$ הן קבוצות לא ריקות, הראו ש:"
      "\n"
      r"$$(B-A)\cup(C-A)\subseteq(B\cup C)-A$$",
      r"$$\forall x\in(B-A)\cup(C-A)\Rightarrow x\in B-A\ \vee\ x\in C-A\Rightarrow"
      r"(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)\Rightarrow"
      r"(x\in B\vee x\in C)\wedge x\notin A\Rightarrow x\in B\cup C\wedge x\notin A\Rightarrow x\in(B\cup C)-A$$"),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "number_theory_gcd", 7,
      r"הוכיחו בדרך השלילה ש: $\sqrt{2}\notin\mathbb{Q}$.",
      r"נניח בשלילה ש-$\sqrt2\in\mathbb{Q}$. אז $\sqrt2=\frac{m}{n}$ כאשר $0<m,n\in\mathbb{N}$ ו-$\gcd(m,n)=1$ "
      r"(אפשר לצמצם את השבר עד שהוא מצומצם לגמרי)."
      "\n"
      r"אז $m^2=2n^2$, ולכן $2\mid m^2$ ולכן $2\mid m$, כלומר $m=2t$."
      "\n"
      r"אז $4t^2=2n^2$, כלומר $n^2=2t^2$, ולכן $2\mid n^2$ ולכן $2\mid n$."
      "\n"
      r"קיבלנו $2\mid m$ וגם $2\mid n$, ולכן $2\le\gcd(m,n)$, בסתירה ל-$\gcd(m,n)=1$."
      "\n"
      r"מסקנה: $\sqrt2\notin\mathbb{Q}$."),

    Q(4, "ב", "proof", "modular_fermat_wilson", 10,
      "(1) הוכיחו או הפריכו: $19<\\gcd(5^{44}-1,\\ 8^{88}+22!)$"
      "\n"
      r"(2) הראו שהקבוצות: $A=(-2,1]\cup(11,21)$ ו-$B=[0,5)\cup(13,25]\cup(30,75]$ שוות עוצמה.",
      r"**(1)** הטענה נכונה. נסמן $a=5^{44}-1=(5^2)^{22}-1=25^{23-1}-1$. כיוון ש-23 ראשוני ו-$23\nmid 25$, לפי Fermat $23\mid a$."
      "\n"
      r"נסמן $b=8^{88}+22!=\big((8^4)^{22}-1\big)+(22!+1)=\big((2^{12})^{23-1}-1\big)+\big((23-1)!+1\big)$."
      "\n"
      r"מחובר ראשון: מתחלק ב-23 לפי Fermat כי 23 ראשוני ו-$23\nmid 2^{12}$. מחובר שני: מתחלק ב-23 לפי Wilson כי 23 ראשוני. לכן $23\mid b$."
      "\n"
      r"מכאן $23\mid a$ וגם $23\mid b$, ולכן $19<23\le\gcd(a,b)$."
      "\n"
      r"**(2)** $(0,1)\subseteq A\subseteq\mathbb{R}\Rightarrow|(0,1)|\le|A|\le|\mathbb{R}|=|(0,1)|\Rightarrow|A|=|(0,1)|$."
      "\n"
      r"$(0,1)\subseteq B\subseteq\mathbb{R}\Rightarrow|(0,1)|\le|B|\le|\mathbb{R}|=|(0,1)|\Rightarrow|B|=|(0,1)|$."
      "\n"
      r"לכן $|A|=|B|$."),

    Q(4, "ג", "proof", "sets_power_set", 8,
      r"יהיו $A,B,C$ קבוצות לא ריקות."
      "\n"
      r"(1) נסחו את ה-contrapositive של הטענה הבאה: ״אם $(A\cap B)\cup C=A\cap(B\cup C)$, אז $C\subseteq A$.״"
      "\n"
      "(2) הוכיחו את הטענה.",
      r"**(1)** ה-contrapositive: אם $C\not\subseteq A$ אז $(A\cap B)\cup C\ne A\cap(B\cup C)$."
      "\n"
      r"**(2)** נוכיח את ה-contrapositive. $C\not\subseteq A\Rightarrow\exists x\in C\wedge x\notin A$."
      "\n"
      r"מכאן $x\in(A\cap B)\cup C$ (כי $x\in C$), אבל $x\notin A\cap(B\cup C)$ (כי $x\notin A$)."
      "\n"
      r"לכן $(A\cap B)\cup C\ne A\cap(B\cup C)$."),
]

# ---------------- steps / rubric / pitfalls (ai-draft), derived from the stored solutions ----------------
# Every numeric answer and every findbug line is asserted in tools/verify/25A-B/verify.py (STEPS section),
# which also re-reads tools/raw/25A-B.json and compares.
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def ch(prompt, correct, wrongs, pos, explain):
    """choice step; the correct option is placed at index pos."""
    vals = list(wrongs)
    vals.insert(pos, correct)
    return {"type": "choice", "prompt": prompt, "options": opts(*vals), "correctId": IDS[pos], "explain": explain}


def num(prompt, answer, explain):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": 0, "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, idx, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def withbug(lines, idx, new):
    out = list(lines)
    out[idx] = new
    return out


def add(num_, part, **kw):
    for q in questions:
        if q["num"] == num_ and q.get("part") == part:
            assert sum(r["points"] for r in kw["rubric"]) == q["points"], (num_, part)
            q.update(kw)
            q["rubricSource"] = "ai-draft"
            q["stepsSource"] = "ai-draft"
            return
    raise KeyError((num_, part))


# ---- Q1a ----
add(1, "א",
    rubric=rub((r"טבלת אמת מלאה עם כל 8 ההשמות של $p,q,r$", 4),
               (r"זיהוי השורות שבהן $(p\vee\neg q)\to r$ שקר", 2),
               ("בניית פסוקית לכל שורה כזו, שבה כל משתנה מופיע בשלילת ערכו בשורה", 2),
               (r"חיבור הפסוקיות ב-$\wedge$ לצורת CNF", 2)),
    pitfalls=["לבנות פסוקית מהשורות שבהן הפסוק אמת (זה ה-DNF) במקום מהשורות שבהן הוא שקר.",
              "לא להפוך את הליטרלים: בפסוקית של שורה שקרית כל משתנה מופיע בשלילת ערכו באותה שורה."],
    steps=[num(r"בכמה מ-8 השורות הפסוק $(p\vee\neg q)\to r$ שקר?", 3,
               r"הגרירה שקרית כשהמקדים $p\vee\neg q$ אמת ו-$r=F$: השורות $TTF$, $TFF$, $FFF$ (לפי $p,q,r$), כלומר 3 שורות (נבדק בסקריפט)."),
           ch(r"איזו פסוקית נבנית מהשורה $p=T,\ q=T,\ r=F$?", r"$\neg p\vee\neg q\vee r$",
              [r"$p\vee q\vee\neg r$", r"$p\wedge q\wedge\neg r$", r"$\neg p\wedge\neg q\wedge r$"], 1,
              r"הפסוקית צריכה להיות שקרית בדיוק בשורה הזו, ולכן כל ליטרל מופיע בשלילת ערכו. שתי האפשרויות עם $\wedge$ אינן פסוקיות, והפסוקית $p\vee q\vee\neg r$ אמת בשורה הזו (נבדק בסקריפט)."),
           ch("מהי צורת ה-CNF של הפסוק?", r"$(\neg p\vee\neg q\vee r)\wedge(\neg p\vee q\vee r)\wedge(p\vee q\vee r)$",
              [r"$(p\vee q\vee\neg r)\wedge(p\vee\neg q\vee\neg r)\wedge(\neg p\vee\neg q\vee\neg r)$",
               r"$(\neg p\wedge\neg q\wedge r)\vee(\neg p\wedge q\wedge r)\vee(p\wedge q\wedge r)$",
               r"$(\neg p\vee\neg q\vee r)\wedge(\neg p\vee q\vee r)$"], 2,
              r"נדרשת פסוקית לכל אחת משלוש השורות השקריות ($TTF$, $TFF$, $FFF$). לכל אחת מהאפשרויות האחרות טבלת אמת שונה (נבדק בסקריפט עם sympy).")])

# ---- Q1b ----
add(1, "ב",
    rubric=rub(("זיהוי שהתנאי $\\{1,2\\}\\subseteq B$ פירושו $B=\\{1,2\\}\\cup C$", 3),
               (r"$C$ היא תת-קבוצה כלשהי של $\{3,4,\dots,10\}$, שבה 8 איברים", 2),
               (r"מספר תתי-הקבוצות $2^8$", 2),
               ("התוצאה $256$", 1)),
    pitfalls=[r"לספור $2^{10}$ תתי-קבוצות: שני האיברים $1,2$ מקובעים ולא חופשיים.",
              r"לספור $2^{10-2}-1$ או להחסיר את הקבוצה הריקה: $C=\emptyset$ מותרת."],
    steps=[ch(r"איך נראית כל $B\subseteq A$ המקיימת $\{1,2\}\subseteq B$?", r"$B=\{1,2\}\cup C$ עם $C\subseteq\{3,4,\dots,10\}$",
              [r"$B=C-\{1,2\}$ עם $C\subseteq A$", r"$B=\{1,2\}\cap C$ עם $C\subseteq A$", r"$B\subseteq\{3,4,\dots,10\}$"], 0,
              r"$1,2$ חייבים להיות ב-$B$ ושאר 8 האיברים חופשיים. בשאר האפשרויות $1,2\notin B$ או ש-$B$ קטנה מדי (נבדק בסקריפט)."),
           num(r"כמה איברים יש בקבוצה $\{3,4,\dots,10\}$?", 8, "מ-3 עד 10 יש 8 מספרים."),
           num(r"כמה תתי-קבוצות $B$ של $A$ מקיימות $\{1,2\}\subseteq B$?", 256,
               r"$2^8=256$, כמספר תתי-הקבוצות של $\{3,\dots,10\}$ (נבדק בספירה ישירה על כל $2^{10}$ התתי-קבוצות).")])

# ---- Q1c ----
add(1, "ג",
    rubric=rub((r"חישוב ערכי $f$ על המחלקים: $f(1)=1,\ f(2)=2,\ f(3)=3,\ f(4)=4$", 2),
               (r"כל ערך של $f$ מחלק את $12$, ולכן התמונה מוכלת בקבוצת המחלקים", 2),
               (r"כל מחלק של $12$ הוא ערך: $f(6)=6$ ו-$f(12)=12$", 2),
               (r"בחירת $A=\{1,2,3,4,6,12\}$ ולכן $f$ על", 1)),
    pitfalls=[r"לבחור $A=\mathbb{N}^*$: $f$ אינה על כי $5$ אינו ערך.",
              r"לשכוח את $12$ או את $6$ ב-$A$, ולכן $f$ אינה על."],
    steps=[num(r"מהו $f(8)=\gcd(12,8)$?", 4, r"$\gcd(12,8)=4$ (נבדק בסקריפט)."),
           num(r"כמה ערכים שונים מקבלת $f$?", 6, r"הערכים הם בדיוק מחלקי 12: $1,2,3,4,6,12$ (נבדק בסקריפט על $x\le2000$)."),
           ch(r"איזו קבוצה $A$ הופכת את $f$ לעל?", r"$A=\{1,2,3,4,6,12\}$",
              [r"$A=\{1,2,3,4,5,6,12\}$", r"$A=\{1,2,3,4,6\}$", r"$A=\{1,2,3,4,5,6,7,8,9,10,11,12\}$"], 2,
              r"על פירושו שכל איבר של $A$ הוא ערך. $5$ אינו ערך של $f$, ו-$12$ חייב להיות ב-$A$ כי הוא ערך (נבדק בסקריפט).")])

# ---- Q2a ----
L2a = [r"$23^{k+1}-1=23\cdot23^k-1$",
       r"$=23\cdot23^k-23+22$",
       r"$=23(23^k-1)+2\cdot11$",
       r"המחובר הראשון מתחלק ב-$11$ לפי הנחת האינדוקציה, והמחובר $2\cdot11$ מתחלק ב-$11$, ולכן $11\mid(23^{k+1}-1)$."]
add(2, "א",
    rubric=rub((r"בסיס: $P(1)$, כלומר $11\mid22$", 3),
               (r"ניסוח הנחת האינדוקציה $11\mid(23^k-1)$ והטענה $P(k+1)$", 2),
               (r"פירוק $23^{k+1}-1=23(23^k-1)+22$", 4),
               ("שימוש בהנחה וחלוקה ב-$11$ של שני המחוברים", 1),
               ("מסקנה לפי עקרון האינדוקציה", 2)),
    pitfalls=[r"לא להשתמש בהנחה $11\mid(23^k-1)$ ולבדוק רק ערכים בודדים של $n$.",
              r"לפרק $23^{k+1}-1=23(23^k-1)+1$ בטעות: הקבוע הוא $22$."],
    steps=[ch(r"באיזו שיטה משתמש הפתרון הרשמי להוכחת $11\mid(23^n-1)$ לכל $1\le n$?", "אינדוקציה מתמטית",
              ["בדיקת $n=1,2,3$ בלבד", "ספירה קומבינטורית", "חישוב $23^n-1$ המפורש לכל $n$"], 0,
              r"הפתרון מראה צעד $P(k)\Rightarrow P(k+1)$. בדיקת כמה ערכים אינה הוכחה."),
           num(r"מהו $23^2-1$?", 528, r"$23^2=529$ ולכן $528=23\cdot22+22=11\cdot48$ (נבדק בסקריפט)."),
           order("סדרו את שלבי הצעד.", L2a, "פתיחת החזקה, הוספה והחסרה של 23, הוצאת $23^k-1$ כגורם, מסקנה."),
           bug("בצעד האינדוקציה שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L2a, 2, r"$=23(23^k-1)+3\cdot11$"), 2,
               r"$23\cdot23^k-23+22=23(23^k-1)+22$, כלומר $+2\cdot11$ ולא $+3\cdot11$ (נבדק בסקריפט עם sympy).")])

# ---- Q2b ----
add(2, "ב",
    rubric=rub((r"$|A|=100$ ולכן $|P(A)|=2^{100}$", 1),
               (r"$B\cup C$ כולל 19 איברים, ולכן $|P(B\cup C)|=2^{19}$", 2),
               (r"גודל מכפלה קרטזית של קבוצות הוא מכפלת הגדלים", 1),
               (r"$2^{100}\cdot2^{19}=2^{119}$", 1)),
    pitfalls=[r"לספור $|B\cup C|=20$: המספר $1=5^0=7^0$ משותף ל-$B$ ול-$C$ ונספר פעם אחת.",
              r"לחבר $2^{100}+2^{19}$ במקום לכפול: בחישוב $|X\times Y|$ מכפילים."],
    steps=[num(r"כמה איברים יש ב-$A=\{5^n7^m:\ m,n\in\{0,\dots,9\}\}$?", 100,
               r"כל זוג $(n,m)$ נותן מספר שונה (יחידות הפירוק לראשוניים), ולכן $10\cdot10=100$ (נבדק בסקריפט)."),
           ch(r"מדוע $|B\cup C|=19$ ולא $20$?", r"כי $5^0=7^0=1$ שייך לשתי הקבוצות ונספר פעם אחת",
              [r"כי $5^9$ אינו ב-$B$", r"כי $B$ ו-$C$ זרות", r"כי $7^0=0$"], 0,
              r"$|B|=|C|=10$ והחיתוך הוא $\{1\}$, ולכן $10+10-1=19$ (נבדק בסקריפט)."),
           num(r"כמה איברים יש ב-$B\cup C$?", 19, r"$10+10-|B\cap C|=19$ (נבדק בסקריפט)."),
           num(r"$|P(A)\times P(B\cup C)|=2^k$. מהו $k$?", 119, r"$k=100+19$ (נבדק בסקריפט).")])

# ---- Q2c ----
L2c = [r"רפלקסיביות: $B\cap\{1\}=B\cap\{1\}$, ולכן $BRB$.",
       r"סימטריות: אם $B\cap\{1\}=C\cap\{1\}$ אז $C\cap\{1\}=B\cap\{1\}$, ולכן $CRB$.",
       r"טרנזיטיביות: אם $B\cap\{1\}=C\cap\{1\}$ וגם $C\cap\{1\}=D\cap\{1\}$ אז $B\cap\{1\}=D\cap\{1\}$, ולכן $BRD$.",
       r"$B\cap\{1\}$ הוא $\emptyset$ או $\{1\}$, ולכן יש בדיוק שתי מחלקות: $[\emptyset]=P(A-\{1\})$ ו-$[\{1\}]$ (כל $B$ המכילה את $1$)."]
add(2, "ג",
    rubric=rub(("רפלקסיביות", 1), ("סימטריות", 1), ("טרנזיטיביות", 2),
               (r"המחלקה $[\emptyset]=P(A-\{1\})$", 2),
               (r"המחלקה $[\{1\}]$ ושתי המחלקות בלבד: $P(A)/R=\{[\emptyset],[\{1\}]\}$", 2)),
    pitfalls=[r"לחשוב שהמחלקות נקבעות לפי גודל $B$ ולא לפי השאלה אם $1\in B$.",
              r"לשכוח להראות שאין מחלקות נוספות: $B\cap\{1\}$ יכול להיות רק $\emptyset$ או $\{1\}$."],
    steps=[ch(r"מה קובע את מחלקת השקילות של $B\in P(A)$?", r"האם $1\in B$",
              [r"גודל $B$", r"האם $10\in B$", r"האם $B=A$"], 0,
              r"$BRC$ אם ורק אם $B\cap\{1\}=C\cap\{1\}$, כלומר אם ורק אם שתיהן מכילות את $1$ או שאף אחת אינה מכילה (נבדק בסקריפט)."),
           num(r"כמה מחלקות שקילות יש ל-$R$?", 2, r"$B\cap\{1\}\in\{\emptyset,\{1\}\}$ (נבדק בסקריפט בספירה על כל $P(A)$ עבור $|A|=10$)."),
           num(r"כמה איברים יש במחלקה $[\emptyset]$?", 512, r"$|P(A-\{1\})|=2^9=512$ (נבדק בסקריפט)."),
           bug("שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L2c, 3, r"$B\cap\{1\}$ הוא $\emptyset$, $\{1\}$ או $\{1,2\}$, ולכן יש בדיוק שלוש מחלקות."), 3,
               r"החיתוך עם $\{1\}$ הוא תת-קבוצה של $\{1\}$ ולכן לא יכול להיות $\{1,2\}$ (נבדק בסקריפט).")])

# ---- Q3a ----
L3a_anti = [r"נניח $xRy$ וגם $yRx$, כלומר $x\mid y$ וגם $y\mid x$.",
            r"מחלק חיובי אינו גדול מהמחולק, ולכן $x\le y$ וגם $y\le x$.",
            r"לכן $x=y$, כלומר $R$ אנטי-סימטרי."]
L3a_tr = [r"נניח $xRy$ וגם $yRz$, כלומר $x\mid y$ וגם $y\mid z$.",
          r"אז קיימים שלמים $s,t$ כך ש-$y=sx$ ו-$z=ty$.",
          r"לכן $z=ty=t(sx)=(ts)x$, כלומר $x\mid z$ ו-$xRz$."]
add(3, "א",
    rubric=rub(("רפלקסיביות: $x\\mid x$", 2),
               ("אנטי-סימטריות", 3),
               ("טרנזיטיביות", 3),
               (r"(2) קביעה ש-$R$ אינו סדר מלא", 1),
               (r"(2) זוג שאינו בר-השוואה: $2\nmid3$ וגם $3\nmid2$", 3)),
    pitfalls=[r"להסיק $x\le y$ מ-$x\mid y$ בלי לציין שהמספרים חיוביים (ב-$\mathbb{Z}$ גם $-3\mid3$ וגם $3\mid-3$).",
              r"להניח שסדר חלקי בהכרח סדר מלא: צריך זוג שאינו בר-השוואה."],
    steps=[num(r"כמה זוגות $(x,y)\in A\times A$ מקיימים $x\mid y$ (כלומר מהו $|R|$)?", 25,
               r"ספירה ישירה בכל 64 הזוגות נותנת 25 (נבדק בסקריפט)."),
           order("סדרו את הוכחת האנטי-סימטריות.", L3a_anti, "הנחת שני הכיוונים, אי-שוויונות, מסקנה."),
           bug("בהוכחת הטרנזיטיביות שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L3a_tr, 2, r"לכן $z=ty=t(sx)=(t+s)x$, כלומר $x\mid z$ ו-$xRz$."), 2,
               r"$t(sx)=(ts)x$ ולא $(t+s)x$ (נבדק בסקריפט עם sympy)."),
           ch(r"איזה זוג מוכיח ש-$R$ אינו יחס סדר מלא?", r"$2$ ו-$3$: אף אחד מהם אינו מחלק את השני",
              [r"$2$ ו-$6$", r"$3$ ו-$18$", r"$1$ ו-$16$"], 1,
              r"בכל אחד משאר הזוגות המספר הקטן מחלק את הגדול, כלומר הם ברי-השוואה (נבדק בסקריפט).")])

# ---- Q3b ----
add(3, "ב",
    rubric=rub(("שלבי החילוק של Euclid: $84=1\\cdot48+36$, $48=1\\cdot36+12$, $36=3\\cdot12$", 3),
               (r"$\gcd(48,84)=12$", 1),
               (r"הצבה לאחור: $12=48-36=48-(84-48)=2\cdot48-84$", 3)),
    pitfalls=[r"להחליף בין $x$ ל-$y$ בסוף ההצבה לאחור.",
              r"לעצור אחרי ה-gcd בלי להפיק את $x,y$."],
    steps=[num(r"מהי השארית בחילוק $84$ ב-$48$?", 36, r"$84=1\cdot48+36$ (נבדק בסקריפט)."),
           num(r"מהו $\gcd(48,84)$?", 12, r"השארית האחרונה השונה מאפס היא $12$ (נבדק בסקריפט)."),
           ch(r"איזה זוג $(x,y)$ מקיים $48x+84y=12$?", r"$(x,y)=(2,-1)$",
              [r"$(x,y)=(-1,2)$", r"$(x,y)=(1,-1)$", r"$(x,y)=(-2,1)$"], 0,
              r"$48\cdot2-84=12$. בשאר הזוגות מתקבלים $120$, $-36$ ו-$-12$ (נבדק בסקריפט).")])

# ---- Q3c ----
L3c = [r"יהי $x\in(B-A)\cup(C-A)$: אז $x\in B-A$ או $x\in C-A$.",
       r"כלומר $(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)$.",
       r"לכן $(x\in B\vee x\in C)\wedge x\notin A$ (הוצאת $x\notin A$ כגורם משותף).",
       r"כלומר $x\in B\cup C$ וגם $x\notin A$, ולכן $x\in(B\cup C)-A$."]
add(3, "ג",
    rubric=rub(("לקיחת $x$ שרירותי באגף שמאל", 1),
               (r"פירוק ההגדרה ל-$(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)$", 1),
               (r"הוצאת $x\notin A$ כגורם משותף", 2),
               (r"חזרה להגדרת האיחוד וההפרש: $x\in(B\cup C)-A$", 2)),
    pitfalls=[r"להוציא כגורם משותף ולהחליף $\vee$ ב-$\wedge$: $(x\in B\wedge x\in C)$ הוא חיתוך.",
              r"להראות את ההכלה ההפוכה במקום זו שנתבקשה."],
    steps=[ch("איך מתחילים הוכחת הכלה $X\\subseteq Y$?", r"לוקחים $x\in X$ שרירותי ומראים $x\in Y$",
              [r"לוקחים $x\in Y$ שרירותי ומראים $x\in X$", "בודקים דוגמה אחת", r"מראים ש-$|X|\le|Y|$"], 1,
              r"ההגדרה של $X\subseteq Y$ היא: כל $x\in X$ שייך ל-$Y$. דוגמה אחת אינה הוכחה, והשוואת גדלים אינה מספיקה."),
           num(r"עבור $A=\{1,2\}$, $B=\{2,3\}$, $C=\{1,4,5\}$: כמה איברים יש ב-$(B-A)\cup(C-A)$?", 3,
               r"$B-A=\{3\}$ ו-$C-A=\{4,5\}$, ולכן 3 איברים (נבדק בסקריפט)."),
           order("סדרו את שלבי ההוכחה.", L3c, "פירוק ההגדרה, כתיבה לוגית, גורם משותף, חזרה להגדרה."),
           bug("שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L3c, 2, r"לכן $(x\in B\wedge x\in C)\wedge x\notin A$ (הוצאת $x\notin A$ כגורם משותף)."), 2,
               r"הוצאת גורם משותף משאירה $\vee$ בין $x\in B$ ל-$x\in C$ ולא $\wedge$ (נבדק בסקריפט בטבלת אמת).")])

# ---- Q4a ----
L4a = [r"נניח בשלילה $\sqrt2=\frac mn$ עם $0<m,n\in\mathbb{N}$ ו-$\gcd(m,n)=1$.",
       r"$m^2=2n^2$, ולכן $2\mid m^2$, ולכן $2\mid m$, כלומר $m=2t$.",
       r"$4t^2=2n^2$, כלומר $n^2=2t^2$, ולכן $2\mid n^2$ ולכן $2\mid n$.",
       r"$2\mid m$ וגם $2\mid n$, ולכן $2\le\gcd(m,n)$, בסתירה ל-$\gcd(m,n)=1$."]
add(4, "א",
    rubric=rub((r"הנחת השלילה: $\sqrt2=\frac mn$ בצורה מצומצמת", 2),
               (r"$m^2=2n^2$ ולכן $m$ זוגי", 2),
               (r"$n^2=2t^2$ ולכן $n$ זוגי", 2),
               (r"סתירה ל-$\gcd(m,n)=1$ ומסקנה", 1)),
    pitfalls=[r"לשכוח להניח שהשבר מצומצם ($\gcd(m,n)=1$), ולכן לא לקבל סתירה.",
              r"להסיק $2\mid m$ מ-$2\mid m^2$ בלי נימוק: צריך שהמספר 2 ראשוני."],
    steps=[ch(r"באיזו שיטה משתמש הפתרון הרשמי להוכחת $\sqrt2\notin\mathbb{Q}$?", "הוכחה בדרך השלילה",
              ["אינדוקציה על המכנה", r"חישוב ספרות $\sqrt2$ עד לחזרה מחזורית", "ספירה קומבינטורית"], 0,
              r"הפתרון מניח ש-$\sqrt2$ רציונלי ומגיע לסתירה. $\sqrt2$ אינו מחזורי ולכן החישוב לא יסתיים."),
           ch(r"מה מניחים על $m,n$ בנוסף ל-$\sqrt2=\frac mn$?", r"$\gcd(m,n)=1$, כלומר השבר מצומצם",
              [r"ש-$m$ ו-$n$ זוגיים", r"ש-$m=n$", r"ש-$m,n$ ראשוניים"], 0,
              r"אם $m=n$ אז $\sqrt2=1$, ואין סיבה ש-$m,n$ יהיו ראשוניים. ההנחה שהשבר מצומצם היא שנותנת את הסתירה."),
           order("סדרו את שלבי ההוכחה.", L4a, "הנחה, $m$ זוגי, $n$ זוגי, סתירה."),
           bug("שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L4a, 2, r"$4t^2=2n^2$, כלומר $n^2=4t^2$, ולכן $2\mid n^2$ ולכן $2\mid n$."), 2,
               r"$4t^2=2n^2$ נותן $n^2=2t^2$ ולא $n^2=4t^2$ (נבדק בסקריפט עם sympy).")])

# ---- Q4b ----
L4b2 = [r"$(0,1)\subseteq A\subseteq\mathbb{R}$, ולכן $|(0,1)|\le|A|\le|\mathbb{R}|$.",
        r"$|\mathbb{R}|=|(0,1)|$, ולכן $|A|=|(0,1)|$ (קנטור-ברנשטיין).",
        r"באופן דומה $(0,1)\subseteq B\subseteq\mathbb{R}$ ולכן $|B|=|(0,1)|$.",
        r"לכן $|A|=|B|$."]
add(4, "ב",
    rubric=rub((r"(1) $23\mid(5^{44}-1)$ לפי Fermat", 3),
               (r"(1) $23\mid(8^{88}+22!)$ לפי Fermat ו-Wilson", 3),
               (r"(1) $23\le\gcd$ ולכן $19<\gcd$", 1),
               (r"(2) $|A|=|(0,1)|$", 1),
               (r"(2) $|B|=|(0,1)|$ ולכן $|A|=|B|$", 2)),
    pitfalls=[r"להשתמש ב-Wilson על $22!$ במקום $22!+1$.",
              r"בסעיף (2) להשוות אורכי קטעים: $A$ ו-$B$ באורכים שונים אך אותה עוצמה."],
    steps=[num(r"מהי השארית של $5^{44}$ בחלוקה ב-$23$?", 1,
               r"$5^{44}=25^{22}$ ו-$25^{22}\equiv1\pmod{23}$ לפי Fermat (נבדק בסקריפט)."),
           num(r"מהי השארית של $22!$ בחלוקה ב-$23$?", 22, r"לפי Wilson $22!\equiv-1\equiv22\pmod{23}$ (נבדק בסקריפט)."),
           ch(r"איזה ראשוני הגדול מ-$19$ מחלק את שני המספרים $5^{44}-1$ ו-$8^{88}+22!$?", "$23$",
              ["$29$", "$31$", "$37$"], 0,
              r"רק $23$ מחלק את שניהם; בשאר הראשוניים לפחות אחד המספרים אינו מתחלק (נבדק בסקריפט)."),
           bug("בסעיף (2) שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L4b2, 1, r"$|\mathbb{R}|=|\mathbb{N}|$, ולכן $|A|=|\mathbb{N}|$ (קנטור-ברנשטיין)."), 1,
               r"$\mathbb{R}$ אינה בת מנייה: $|\mathbb{R}|=|(0,1)|>|\mathbb{N}|$.")])

# ---- Q4c ----
L4c = [r"$C\not\subseteq A$, ולכן קיים $x\in C$ עם $x\notin A$.",
       r"$x\in(A\cap B)\cup C$ כי $x\in C$, אבל $x\notin A\cap(B\cup C)$ כי $x\notin A$.",
       r"לכן $(A\cap B)\cup C\ne A\cap(B\cup C)$."]
add(4, "ג",
    rubric=rub((r"(1) ניסוח ה-contrapositive", 3),
               (r"(2) קיום $x\in C$ עם $x\notin A$", 1),
               (r"(2) $x\in(A\cap B)\cup C$", 2),
               (r"(2) $x\notin A\cap(B\cup C)$ ומסקנה", 2)),
    pitfalls=[r"להשאיר את התוצאה ״$C\subseteq A$״ בלי לשלול אותה בניסוח.",
              r"להניח $A\cap B=\emptyset$ או מקרה פרטי אחר."],
    steps=[ch("מהו ה-contrapositive של הטענה?",
              r"אם $C\not\subseteq A$ אז $(A\cap B)\cup C\ne A\cap(B\cup C)$",
              [r"אם $C\not\subseteq A$ אז $(A\cap B)\cup C=A\cap(B\cup C)$",
               r"אם $C\subseteq A$ אז $(A\cap B)\cup C\ne A\cap(B\cup C)$",
               r"אם $A\not\subseteq C$ אז $(A\cap B)\cup C\ne A\cap(B\cup C)$"], 0,
              r"ה-contrapositive שולל את המסקנה ($C\subseteq A$) והופך אותה לתנאי, ושולל את התנאי ($=$) והופך אותו למסקנה. שלוש האחרות שקריות (נבדק בסקריפט על כל הקבוצות מעל 3 איברים)."),
           num(r"עבור $A=\{1,2\}$, $B=\{2,3\}$, $C=\{3\}$ ($C\not\subseteq A$): כמה איברים יש ב-$(A\cap B)\cup C$?", 2,
               r"$A\cap B=\{2\}$ ולכן האיחוד עם $C$ הוא $\{2,3\}$, בעוד ש-$A\cap(B\cup C)=\{2\}$ (נבדק בסקריפט)."),
           order("סדרו את הוכחת ה-contrapositive.", L4c, "בחירת העד, בדיקת שני האגפים, מסקנה."),
           bug("שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
               withbug(L4c, 1, r"$x\in(A\cap B)\cup C$ כי $x\in A\cap B$, אבל $x\notin A\cap(B\cup C)$ כי $x\notin A$."), 1,
               r"$x\notin A$ ולכן $x\notin A\cap B$; הוא באיחוד רק בגלל $x\in C$ (נבדק בסקריפט).")])


exam = {
    "examCode": "25A-B",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ה, מועד ב (09.03.2025)',
    "year": 2025,
    "examDate": "09.03.2025",
    "sourceFile": "25A-B exam with lecturer solution, pp.1-7",
    "solutionFile": "25A-B lecturer solution (handwritten and typed), pp.2-7",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
