# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-A.json -- discrete math 1, semester A 5785, moed A (11.02.2025).
4 mandatory questions of 25 points, parts (a)-(c). Key: the lecturer's handwritten solution on the exam pages.
Run: PYTHONUTF8=1 py tools/gen/gen_25A-A.py
Notes:
 - A part with numbered sub-claims ((1), (2)) is ONE item (the id scheme allows a single letter per part).
 - Q3a is held: the official solution proves symmetry and transitivity but never answers sub-question (2)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-A.json"


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
      INTRO + "**המונח:** שקילות לוגית\n"
      "**שאלה:** בדקו על ידי טבלת אמת את נכונות הטענה:\n"
      r"$$\neg p\to\neg(q\vee r)\equiv(q\to p)\wedge(r\to p)$$",
      "טבלת אמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | ¬p→¬(q∨r) | (q→p)∧(r→p)\n"
      "T T T |     T      |      T\n"
      "T T F |     T      |      T\n"
      "T F T |     T      |      T\n"
      "T F F |     T      |      T\n"
      "F T T |     F      |      F\n"
      "F T F |     F      |      F\n"
      "F F T |     F      |      F\n"
      "F F F |     T      |      T\n"
      "```\n"
      "שתי העמודות זהות בכל השורות, ולכן הטענה נכונה: הפסוקים שקולים לוגית."),

    Q(1, "ב", "proof", "modular_fermat_wilson", 8,
      INTRO + "**המונח:** מחלק של מספר שלם.\n"
      r"**שאלה:** הראו שלכל $a,b\in\mathbb{Z}$ המספר $a\cdot(71^{120}-1)+b\cdot(50^{24}+12!)$ מתחלק ב-26.",
      r"המספר $71$ אי-זוגי, ולכן $N=71^{120}$ אי-זוגי ו-$2\mid(71^{120}-1)$."
      "\n"
      r"$71^{120}-1=(71^{10})^{13-1}-1$. כיוון ש-13 ראשוני ו-$13\nmid 71^{10}$, לפי Fermat מתקבל $13\mid(71^{120}-1)$."
      "\n"
      r"מכיוון ש-$\gcd(2,13)=1$ נקבל $26\mid(71^{120}-1)$."
      "\n"
      r"$50^{24}+12!=\big((50^2)^{13-1}-1\big)+(12!+1)$. כיוון ש-$13\nmid 50^2$, לפי Fermat מתקבל $13\mid\big((50^2)^{13-1}-1\big)$, "
      r"ולפי Wilson (13 ראשוני) $13\mid(12!+1)$. לכן $13\mid(50^{24}+12!)$."
      "\n"
      r"המספר $50^{24}+12!$ זוגי (סכום של שני מספרים זוגיים), ולכן $2\mid(50^{24}+12!)$ וכמו קודם $26\mid(50^{24}+12!)$."
      "\n"
      r"לכן $26$ מחלק את $a(71^{120}-1)+b(50^{24}+12!)$ לכל $a,b\in\mathbb{Z}$."),

    Q(1, "ג", "computation", "functions", 7,
      INTRO + "**המונח:** פונקציה חד-חד-ערכית.\n"
      r"**שאלה:** תהי הפונקציה $f:\{1,4,5,6,9,18\}\to\mathbb{Z}$ שמוגדרת לפי הכלל $f(k)=\operatorname{lcm}(3,k)$ "
      r"לכל $k\in\{1,4,5,6,9,18\}$."
      "\n"
      r"מצאו $A\subseteq\mathbb{Z}$ כך ש-$f:\{1,4,5,6,9,18\}\to A$ היא הפיכה ומצאו את $f^{-1}$.",
      r"נחשב את ערכי הפונקציה:"
      "\n"
      r"$f(1)=\operatorname{lcm}(3,1)=3$, $f(4)=\operatorname{lcm}(3,4)=12$, $f(5)=\operatorname{lcm}(3,5)=15$,"
      "\n"
      r"$\operatorname{lcm}(3,6)=6=f(6)$, $\operatorname{lcm}(3,9)=9=f(9)$, $\operatorname{lcm}(3,18)=18=f(18)$."
      "\n"
      r"אז עבור $A=\{3,6,9,12,15,18\}$ הפונקציה $f:\{1,4,5,6,9,18\}\to A$ היא חח״ע ועל, ולכן הפיכה, ו:"
      "\n"
      r"$f^{-1}(3)=1,\ f^{-1}(6)=6,\ f^{-1}(9)=9,\ f^{-1}(12)=4,\ f^{-1}(15)=5,\ f^{-1}(18)=18$."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 12,
      r"הוכיחו באינדוקציה שלכל $1\le n\in\mathbb{N}$ מתקיים:"
      "\n"
      r"$$\frac{1}{1\cdot 5}+\frac{1}{5\cdot 9}+\frac{1}{9\cdot 13}+\dots+\frac{1}{(4n-3)\cdot(4n+1)}=\frac{n}{4n+1}$$",
      r"**I. בסיס:** $P(1)$: $\frac{1}{1\cdot 5}=\frac{1}{4\cdot 1+1}\Rightarrow P(1)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=T$ עבור $1\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=T$."
      "\n"
      r"$P(k):\ \frac{1}{1\cdot 5}+\frac{1}{5\cdot 9}+\dots+\frac{1}{(4k-3)(4k+1)}=\frac{k}{4k+1}$"
      "\n"
      r"$P(k+1):\ \frac{1}{1\cdot 5}+\dots+\frac{1}{(4k+1)(4k+5)}=\frac{k+1}{4k+5}$"
      "\n"
      r"$$\frac{1}{1\cdot 5}+\dots+\frac{1}{(4k-3)(4k+1)}+\frac{1}{(4k+1)(4k+5)}=\frac{k}{4k+1}+\frac{1}{(4k+1)(4k+5)}"
      r"=\frac{4k^2+5k+1}{(4k+1)(4k+5)}=\frac{(4k^2+4k)+(k+1)}{(4k+1)(4k+5)}$$"
      "\n"
      r"$$=\frac{4k(k+1)+(k+1)}{(4k+1)(4k+5)}=\frac{(4k+1)(k+1)}{(4k+1)(4k+5)}=\frac{k+1}{4k+5}\Rightarrow P(k+1)=TRUE$$"
      "\n"
      r"מסקנה: מ-I ו-II לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=TRUE$."),

    Q(2, "ב", "proof", "number_theory_gcd", 5,
      r"הוכיחו בדרך השלילה ש: $\log_3 5\notin\mathbb{Q}$.",
      r"נניח בשלילה ש-$\log_3 5\in\mathbb{Q}$. אז קיימים $a,b\in\mathbb{N}^*$ כך ש-$\log_3 5=\frac{a}{b}$ (הלוגריתם חיובי). לכן:"
      "\n"
      r"$$5=3^{a/b}\iff t=5^b=3^a\quad(t\in\mathbb{N},\ 2\le t)$$"
      "\n"
      r"המספרים 3 ו-5 הם ראשוניים שונים, ולכן לפי המשפט היסודי של האריתמטיקה לכל $t\in\mathbb{N}$, $2\le t$, "
      r"יש פירוק יחיד למכפלת ראשוניים. אבל ל-$t$ שני פירוקים שונים ($5^b$ ו-$3^a$), סתירה."
      "\n"
      r"מסקנה: $\log_3 5\notin\mathbb{Q}$."),

    Q(2, "ג", "proof", "relations_properties", 8,
      "הוכיחו או הפריכו:\n"
      r"(1) קיים יחס $R\subseteq\{1,2,3\}\times\{1,2,3\}$ כך ש: $R$ **לא** רפלקסיבי, $R$ **לא** סימטרי, $R$ **לא** אנטי-סימטרי, "
      r"$R$ **לא** טרנזיטיבי וגם $|R|\le 5$."
      "\n"
      r"(2) **לא** קיימים יחסים שונים וטרנזיטיביים $R_1,R_2\subseteq\{1,2,3\}\times\{1,2,3\}$ כך ש: "
      r"$R_1\cup R_2$ טרנזיטיבי וגם $R_1\cap R_2\ne\emptyset$.",
      r"**(1)** הטענה נכונה. דוגמה: $R=\{(1,2),(2,1),(2,3)\}$."
      "\n"
      r"$(1,1)\notin R$, ולכן $R$ לא רפלקסיבי. $(2,3)\in R$ אך $(3,2)\notin R$, ולכן $R$ לא סימטרי. "
      r"$(1,2),(2,1)\in R$ ו-$1\ne 2$, ולכן $R$ לא אנטי-סימטרי. $(1,2),(2,3)\in R$ אך $(1,3)\notin R$, ולכן $R$ לא טרנזיטיבי. "
      r"וגם $|R|=3\le 5$."
      "\n"
      r"**(2)** הטענה לא נכונה. דוגמה נגדית: $R_2=\{(1,1),(1,3)\}$ ו-$R_1=\{(1,1),(1,2)\}$ יחסים שונים וטרנזיטיביים. "
      r"$R_1\cap R_2\ne\emptyset$ (כי $(1,1)$ בשניהם), ו-$R_1\cup R_2=\{(1,1),(1,2),(1,3)\}$ הוא יחס טרנזיטיבי."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "equivalence_relations", 9,
      r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$, מתקיים "
      r"$xRy\iff 3x+7y$ הוא מספר שמתחלק ב-5."
      "\n"
      r"(1) הוכיחו ש: $R$ הוא יחס סימטרי וטרנזיטיבי."
      "\n"
      r"(2) האם $R$ הוא יחס סדר חלקי ?",
      None,
      hold="no-key: the official solution proves only (1) (symmetric, transitive) and never answers (2)"),

    Q(3, "ב", "computation", "number_theory_gcd", 9,
      r"מצאו על ידי האלגוריתם המורחב של Euclid שני מספרים $x,y\in\mathbb{Z}$ כך ש: $\gcd(48,184)=48\cdot x+184\cdot y$."
      "\n"
      r"וגם מצאו $a,b\in\mathbb{Z}$ כך ש: $\gcd(-48,184)=-48\cdot a+184\cdot b$.",
      "הטבלה של האלגוריתם המורחב (בכל שורה: $d$ הוא ה-gcd, ו-$x\\leftarrow y'$ ו-$y\\leftarrow x'-y'\\cdot\\lfloor a/b\\rfloor$ "
      "מחושבים מהשורה שמתחת):\n"
      "```\n"
      "  a    b    floor(a/b)   d    x    y\n"
      " 184   48        3        8   -1    4\n"
      "  48   40        1        8    1   -1\n"
      "  40    8        5        8    0    1\n"
      "   8    0       --        8    1    0\n"
      "```\n"
      r"$$8=\gcd(184,48)=(-1)\cdot 184+4\cdot 48$$"
      "\n"
      r"$$8=\gcd(184,-48)=(-1)\cdot 184+(-4)\cdot(-48)$$"
      "\n"
      r"כלומר $x=4,\ y=-1$ בסעיף הראשון, ו-$a=-4,\ b=-1$ בסעיף השני."),

    Q(3, "ג", "proof", "sets_power_set", 7,
      r"אם $A,B,C$ הן קבוצות לא ריקות, הראו ש:"
      "\n"
      r"$$(B\cup C)-A\subseteq(B-A)\cup(C-A)$$",
      r"$$\forall x\in(B\cup C)-A\Rightarrow\begin{cases}x\in B\cup C\\ x\notin A\end{cases}\Rightarrow"
      r"\begin{cases}x\in B\vee x\in C\\ x\notin A\end{cases}\Rightarrow(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)$$"
      "\n"
      r"$$\Rightarrow x\in(B-A)\vee x\in(C-A)\Rightarrow x\in(B-A)\cup(C-A)$$"),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "sets_power_set", 10,
      r"תהיינה $A,B$ שתי קבוצות לא ריקות."
      "\n"
      r"נסחו את ה-contrapositive של הטענה הבאה: "
      r"״אם $P(A)\cup P(B)=P(A\cup B)$, אז $A\subseteq B$ או $B\subseteq A$.״"
      "\n"
      "הוכיחו את הטענה.",
      r"ה-contrapositive: אם $A\not\subseteq B$ וגם $B\not\subseteq A$, אז $P(A)\cup P(B)\ne P(A\cup B)$."
      "\n"
      r"הוכחה של ה-contrapositive: $A\not\subseteq B$ ולכן קיים $a\in A$ כך ש-$a\notin B$, ו-$B\not\subseteq A$ ולכן קיים $b\in B$ כך ש-$b\notin A$."
      "\n"
      r"כיוון ש-$\{a,b\}\subseteq A\cup B$ נקבל $\{a,b\}\in P(A\cup B)$."
      "\n"
      r"מצד שני, $\{a,b\}\notin P(B)$ וגם $\{a,b\}\notin P(A)$, ולכן $\{a,b\}\notin P(A)\cup P(B)$."
      "\n"
      r"מכאן $P(A)\cup P(B)\ne P(A\cup B)$, וזה מה שהיה צריך להוכיח."),

    Q(4, "ב", "proof", "number_theory_gcd", 7,
      r"מצאו כל מספר $a\in\mathbb{N}$ כך ש: $a^2+a+2$ הוא מספר ראשוני.",
      r"**מקרה 1:** $a=0$ $\Rightarrow$ $a^2+a+2=2$, מספר ראשוני."
      "\n"
      r"**מקרה 2:** $a\ge 1$. המספר $a(a+1)$ זוגי וגדול או שווה ל-2, ולכן $a^2+a+2=a(a+1)+2$ זוגי וגדול או שווה ל-4, "
      r"ולכן אינו ראשוני."
      "\n"
      r"מסקנה: $a^2+a+2$ ראשוני $\iff$ $a=0$."),

    Q(4, "ג", "proof", "cardinality_sets", 8,
      r"(1) הראו שהקבוצות: $A=(-1,7]\cup(10,20)$ ו-$B=[0,15)\cup(30,35]$ שוות עוצמה."
      "\n"
      r"(2) הראו שהפונקציה $f:\mathbb{N}\times\mathbb{N}\to\mathbb{N}^*$ שמוגדרת לפי הכלל $f(m,n)=3^m\cdot 5^n$ "
      r"לכל $(m,n)\in\mathbb{N}\times\mathbb{N}$ היא חד-חד-ערכית, אך אינה על.",
      r"**(1)** $(0,1)\subseteq(-1,7]\subseteq A\subseteq\mathbb{R}\Rightarrow|(0,1)|\le|A|\le|\mathbb{R}|=|(0,1)|\Rightarrow|A|=|(0,1)|$."
      "\n"
      r"באופן דומה, $(0,1)\subseteq[0,15)\subseteq B\subseteq\mathbb{R}\Rightarrow|(0,1)|\le|B|\le|\mathbb{R}|=|(0,1)|\Rightarrow|B|=|(0,1)|$."
      "\n"
      r"מסקנה: $|A|=|B|\ (=|(0,1)|)$."
      "\n"
      r"**(2)** $f$ חח״ע: לכל $(a,b),(m,n)\in\mathbb{N}\times\mathbb{N}$, אם $f(a,b)=f(m,n)$ אז $q=3^a5^b=3^m5^n$."
      "\n"
      r"אם $q=1$ אז $a=b=m=n=0$, ולכן $(a,b)=(m,n)$."
      "\n"
      r"אם $q\ge 2$, לפי המשפט היסודי של האריתמטיקה הפירוק של $q$ למכפלת ראשוניים יחיד, ולכן $a=m$ ו-$b=n$, כלומר $(a,b)=(m,n)$."
      "\n"
      r"לכן $f$ היא חח״ע."
      "\n"
      r"$f$ אינה על: נבחר $7\in\mathbb{N}^*$. נניח בשלילה שקיימים $m,n\in\mathbb{N}$ כך ש-$3^m\cdot 5^n=7$. "
      r"אבל $7=7^1$ הוא פירוק יחיד למכפלת ראשוניים, בסתירה למשפט היסודי של האריתמטיקה. לכן $f$ אינה על."),
]

exam = {
    "examCode": "25A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ה, מועד א (11.02.2025)',
    "year": 2025,
    "examDate": "11.02.2025",
    "sourceFile": "25A-A exam with lecturer solution, pp.1-7",
    "solutionFile": "25A-A lecturer solution (handwritten and typed), pp.2-7",
    "contexts": {},
    "questions": questions,
}

# a held item carries no solution
for q in exam["questions"]:
    if q.get("solution") is None:
        q.pop("solution", None)
        q.pop("solutionSource", None)
        q.pop("official", None)
        q.pop("confidence", None)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
