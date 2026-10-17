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
