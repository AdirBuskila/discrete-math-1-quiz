# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-A.json -- discrete math 1, semester A 5783, moed A (30.01.2023).
4 mandatory questions of 25 points, parts (a)-(c). Key: the typed (coloured) official solution printed after each part.
Run: PYTHONUTF8=1 py tools/gen/gen_23A-A.py
A part with numbered sub-claims ((1), (2)) is ONE item."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution", "official": True, "confidence": "high"}
    q.update(kw)
    return q


INTRO = "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "computation", "logic_propositional", 8,
      INTRO + "**המונח:** צורת CNF של פסוק.\n"
      r"**שאלה:** מצאו בעזרת טבלת אמת את צורת ה-CNF של הפסוק $(p\to q)\wedge\neg r$.",
      "טבלת אמת (T = אמת, F = שקר), ובשורות שבהן הפסוק שקר הפסוקית המתאימה:\n"
      "```\n"
      "p q r | p→q | ¬r | (p→q)∧¬r | פסוקית\n"
      "T T T |  T  |  F |     F     | ¬p∨¬q∨¬r\n"
      "T T F |  T  |  T |     T     |\n"
      "T F T |  F  |  F |     F     | ¬p∨q∨¬r\n"
      "T F F |  F  |  T |     F     | ¬p∨q∨r\n"
      "F T T |  T  |  F |     F     | p∨¬q∨¬r\n"
      "F T F |  T  |  T |     T     |\n"
      "F F T |  T  |  F |     F     | p∨q∨¬r\n"
      "F F F |  T  |  T |     T     |\n"
      "```\n"
      r"צורת ה-CNF של $S=(p\to q)\wedge\neg r$ היא:"
      "\n"
      r"$$S\equiv(\neg p\vee\neg q\vee\neg r)\wedge(\neg p\vee q\vee\neg r)\wedge(\neg p\vee q\vee r)\wedge(p\vee\neg q\vee\neg r)\wedge(p\vee q\vee\neg r)$$"),

    Q(1, "ב", "proof", "relations_properties", 8,
      INTRO + "**המונח:** יחס טרנזיטיבי.\n"
      r"**שאלה:** יהיו $A=\{1,2,\dots,10\}$ ו-$R\subseteq A\times A$ יחס טרנזיטיבי."
      "\n"
      r"**הוכיחו או הפריכו:** היחס ההפוך $R^{-1}$ הוא יחס טרנזיטיבי.",
      r"**הגדרה:** יחס $R\subseteq A\times A$ נקרא טרנזיטיבי אם מקיים התנאי: לכל $x,y,z\in A$, אם $(x,y)\in R$ וגם $(y,z)\in R$, אז $(x,z)\in R$."
      "\n"
      r"הטענה נכונה. נניח, בשלילה, שהיחס $R^{-1}$ אינו טרנזיטיבי. אז קיימים $x,y,z\in A$ כך ש: "
      r"$(x,y)\in R^{-1}$ וגם $(y,z)\in R^{-1}$, אך $(x,z)\notin R^{-1}$."
      "\n"
      r"לפי ההגדרה של $R^{-1}$ נשיג: $(y,x)\in R$ וגם $(z,y)\in R$ ולכן $(z,x)\in R$ (כי $R$ טרנזיטיבי). "
      r"אז נקבל $(x,z)\in R^{-1}$, בסתירה להנחה $(x,z)\notin R^{-1}$."
      "\n"
      r"מסקנה: אם $R$ טרנזיטיבי, אז גם $R^{-1}$ הוא יחס טרנזיטיבי."),

    Q(1, "ג", "proof", "functions", 9,
      INTRO + "**המונח:** פונקציה חד-חד-ערכית.\n"
      r"**שאלה:** הפונקציה $f:\mathbb{N}^*\times\mathbb{N}^*\to\mathbb{N}-\{0,1\}$ מוגדרת לפי הכלל "
      r"$f(m,n)=2^m5^n$ לכל $(m,n)\in\mathbb{N}^*\times\mathbb{N}^*$, כאשר $\mathbb{N}^*=\mathbb{N}-\{0\}$."
      "\n"
      r"בדקו האם $f$ היא פונקציה: (1) על ; (2) חד-חד-ערכית.",
      r"**הגדרה:** הפונקציה $f:A\to B$ נקראת חד-חד-ערכית אם מקיימת התנאי: לכל $x,y\in A$, אם $x\ne y$ אז $f(x)\ne f(y)$, "
      r"או: לכל $x,y\in A$, אם $f(x)=f(y)$, אז $x=y$."
      "\n"
      r"**(1)** הפונקציה $f$ אינה על. למספר $3\in\mathbb{N}-\{0,1\}$ אין מקור, כי לפי המשפט היסודי של האריתמטיקה "
      r"לא קיים $(m,n)\in\mathbb{N}^*\times\mathbb{N}^*$ כך ש: $3=2^m5^n$."
      "\n"
      r"**(2)** הפונקציה $f$ הינה חד-חד-ערכית. לכל $(m,n),(x,y)\in\mathbb{N}^*\times\mathbb{N}^*$, אם $f(m,n)=f(x,y)$, אז קיים $2\le q\in\mathbb{N}$ כך ש: "
      r"$q=2^m5^n=2^x5^y$. לפי המשפט היסודי של האריתמטיקה למספר $2\le q\in\mathbb{N}$ יש ייצוג יחיד כמכפלה של מספרים ראשוניים, ולכן $m=x,\ n=y$, "
      r"כלומר $(m,n)=(x,y)$."
      "\n"
      r"מסקנה: $f$ היא פונקציה חד-חד-ערכית."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 11,
      r"הוכיחו באינדוקציה מתמטית ש: $n^3<2^n$ לכל $10\le n\in\mathbb{N}$.",
      r"**I. נבדוק ש:** $P(10)=\text{TRUE}$."
      "\n"
      r"$P(10):\ 10^3<2^{10}\iff 1000<1024\ \dots\ \text{TRUE}$."
      "\n"
      r"**II. נבדוק ש:** אם $P(k)=\text{TRUE}$ עבור $10\le k$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ k^3<2^k$"
      "\n"
      r"$P(k+1):\ (k+1)^3<2^{k+1}$"
      "\n"
      r"$$(k+1)^3=k^3+3k^2+3k+1<k^3+3k^2+3k^2+3k^2=k^3+9k^2<k^3+k\cdot k^2=2\cdot k^3<2\cdot 2^k=2^{k+1}\ \to\ P(k+1)=\text{TRUE}$$"
      "\n"
      r"מסקנה: לפי משפט האינדוקציה המתמטית הטענה נכונה, כי I וגם II מתקיימים, לכל $10\le n\in\mathbb{N}$."),

    Q(2, "ב", "computation", "number_theory_gcd", 8,
      r"מצאו $x,y\in\mathbb{Z}$ בעזרת האלגוריתם המורחב של EUCLID כך ש: $\gcd(65,-40)=65x+(-40)y$.",
      "הטבלה של האלגוריתם המורחב:\n"
      "```\n"
      "  a    b    floor(a/b)   d    x    y\n"
      "  65   40        1        5   -3    5\n"
      "  40   25        1        5    2   -3\n"
      "  25   15        1        5   -1    2\n"
      "  15   10        1        5    1   -1\n"
      "  10    5        2        5    0    1\n"
      "   5    0        -        5    1    0\n"
      "```\n"
      r"$\gcd(65,40)=5=65\cdot(-3)+40\cdot 5\ \Rightarrow$"
      "\n"
      r"$$\gcd(65,-40)=5=65\cdot(-3)+(-40)\cdot(-5)$$"
      "\n"
      r"כלומר $x=-3,\ y=-5$."),

    Q(2, "ג", "computation", "equivalence_relations", 6,
      r"יהיו $A=\{1,2,3,4,5,6\}$, $B=\{1\}$, $C=\{2,3,4\}$, $D=A-(B\cup C)$."
      "\n"
      r"הראו שקיים יחס שקילות $R\subseteq A\times A$ כך ש: $A/R=\{B,C,D\}$ וחשבו את $|R|$.",
      r"הקבוצה $D$ היא $D=\{5,6\}$. המשפחה $\{B,C,D\}$ מגדירה חלוקה של $A$, בגודל 3, כי: "
      r"$B\ne\emptyset,\ C\ne\emptyset,\ D\ne\emptyset$ וגם $B\cap C=B\cap D=C\cap D=\emptyset$ וגם $B\cup C\cup D=A$."
      "\n"
      r"לכן קיים יחס שקילות $R\subseteq A\times A$ כך ש: $A/R=\{B,C,D\}$. אז נקבל ש: $B=[1]$, $C=[2]$ ו-$D=[5]$:"
      "\n"
      r"$$R=\{1\}\times\{1\}\cup\{2,3,4\}\times\{2,3,4\}\cup\{5,6\}\times\{5,6\}\ \Rightarrow\ |R|=14$$"),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "sets_power_set", 10,
      r"יהיו 3 קבוצות $A,B,C$ לא ריקות ושונות. **הוכיחו או הפריכו.**"
      "\n"
      r"(1) $(B-A)\cup(C-A)\subseteq(B\cup C)-A$."
      "\n"
      r"(2) $|A|=|\mathbb{Z}|$, כאשר $A=\mathbb{Q}\cap(1,2)$.",
      r"**(1)** טענה נכונה."
      "\n"
      r"$$\forall x\in(B-A)\cup(C-A)\Rightarrow x\in B-A\ \vee\ x\in C-A\Rightarrow(x\in B\ \vee\ x\in C)\wedge x\notin A\Rightarrow x\in B\cup C\ \wedge\ x\notin A\Rightarrow x\in(B\cup C)-A$$"
      "\n"
      r"מסקנה: $(B-A)\cup(C-A)\subseteq(B\cup C)-A$."
      "\n"
      r"**(2)** טענה נכונה."
      "\n"
      r"מכיוון ש-$A\subseteq\mathbb{Q}$ נקבל $|A|\le|\mathbb{Q}|=|\mathbb{Z}|$. מצד אחד:"
      "\n"
      r"$\{1+\frac12,\ 1+\frac13,\dots,1+\frac1n,\dots\}\subseteq A\Rightarrow\left|\{1+\frac12,\ 1+\frac13,\dots,1+\frac1n,\dots\}\right|=|\mathbb{N}|\le|A|$"
      "\n"
      r"כלומר $|\mathbb{Z}|=|\mathbb{N}|\le|A|\le|\mathbb{Z}|$, ולכן $|A|=|\mathbb{Z}|$, לפי משפט Cantor-Bernstein."),

    Q(3, "ב", "computation", "cardinality_sets", 7,
      r"תהיינה הקבוצות $A=\{2^m9^n:\ m,n\in\{0,1,2,\dots,9\}\}$, $B=\{5^m9^n:\ m,n\in\{0,1,2,\dots,9\}\}$."
      "\n"
      r"חשבו את $|P(A\cap B)|+|P(A\times B)|$.",
      r"לפי ההגדרה של $A,B$ נשיג: $x\in A\cap B\iff x=9^n$ לכל $n\in\{0,1,2,\dots,9\}$. אז:"
      "\n"
      r"$$|P(A\cap B)|+|P(A\times B)|=2^{|A\cap B|}+2^{|A\times B|}=2^{10}+2^{10000}$$"),

    Q(3, "ג", "proof", "modular_fermat_wilson", 8,
      r"תהי $A$ קבוצה בת 120 איברים. הראו ש: $11\mid\gcd(n,\ 5^{20}+10!+12!)$, "
      r"כאשר $n$ שווה למספר תתי-הקבוצות של $A$ ששונות מ-$A$.",
      r"לפי ההגדרה: $n=2^{|A|}-1=2^{120}-1=(2^{12})^{10}-1=(2^{12})^{11-1}-1$."
      "\n"
      r"לכן, לפי משפט FERMAT: $11\mid n$ כי 11 מספר ראשוני ו-$2^{12}$ אינו מתחלק ב-11."
      "\n"
      r"נשאר להראות שגם $m=5^{20}+10!+12!$ מתחלק ב-11. אז ניתן לרשום:"
      "\n"
      r"$$m=25^{10}-1+10!+1+12!=(25^{11-1}-1)+((11-1)!+1)+12!=a+b+c$$"
      "\n"
      r"לפי משפט FERMAT: $11\mid a$ כי 11 מספר ראשוני ו-25 אינו מתחלק ב-11."
      "\n"
      r"לפי משפט WILSON: $11\mid b$ כי 11 מספר ראשוני."
      "\n"
      r"המספר $c$ מתחלק ב-11, כי $c$ שווה למכפלה של המספרים $1,2,\dots,11,12$."
      "\n"
      r"אז $11\mid m$, משום ש: $m=a+b+c$ וגם $11\mid a$, $11\mid b$, $11\mid c$."
      "\n"
      r"אז 11 הוא מחלק משותף של $n$ ו-$m$. לכן גם $11\mid\gcd(n,m)$."),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "equivalence_relations", 14,
      r"יהי היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$ מתקיים "
      r"$xRy\iff x+y+1$ הוא מספר אי-זוגי."
      "\n"
      r"הראו ש: $R$ הוא יחס שקילות ומצאו את $\mathbb{Z}/R$ ? האם $R$ הוא יחס סדר חלקי ?",
      r"היחס $R$ הוא רפלקסיבי כי: $xRx\iff 2x+1=x+x+1$ הוא מספר אי-זוגי לכל $x\in\mathbb{Z}$."
      "\n"
      r"היחס $R$ הוא סימטרי כי: $xRy\iff x+y+1$ הוא מספר אי-זוגי $\iff y+x+1$ הוא מספר אי-זוגי $\iff yRx$."
      "\n"
      r"היחס $R$ הוא טרנזיטיבי כי: $xRy$ וגם $yRz\iff x+y+1$ וגם $y+z+1$ הם מספרים אי-זוגיים. "
      r"אזי $(x+z+1)+(2y+1)=(x+y+1)+(y+z+1)$ הוא מספר זוגי, ולכן $x+z+1$ הוא מספר אי-זוגי "
      r"(משום ש: $2y+1$ הוא אי-זוגי). לכל $xRz\iff R$ הוא טרנזיטיבי."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"נחשב את מחלקות השקילות:"
      "\n"
      r"$[0]=\{x:\ x\in\mathbb{Z}\wedge 0Rx\}=\{x:\ x\in\mathbb{Z}\wedge 0+x+1\text{ is an odd number}\}=\{x:\ x\in\mathbb{Z}\wedge x\text{ is even}\}=\{2k:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}\wedge 1Rx\}=\{x:\ x\in\mathbb{Z}\wedge 1+x+1\text{ is an odd number}\}=\{x:\ x\in\mathbb{Z}\wedge x\text{ is odd}\}=\{2k+1:\ k\in\mathbb{Z}\}$"
      "\n"
      r"מכיוון ש-$[0]\cup[1]=\mathbb{Z}$ אין עוד מחלקות שקילות. לכן $\mathbb{Z}/R=\{[0],[1]\}$."
      "\n"
      r"$R$ אינו יחס סדר חלקי. לדוגמה: $2R4$ וגם $4R2$ אך $2\ne 4$."
      "\n"
      r"פתרון נוסף: $xRy\iff x+y+1$ הוא מספר אי-זוגי $\iff x+y$ הוא מספר זוגי, וההמשך דומה."),

    Q(4, "ב", "computation", "number_theory_gcd", 6,
      r"חשבו את $\operatorname{lcm}(n-1,\ n+1)$, כאשר $n$ מספר ראשוני.",
      r"אם $n=2$, אז נקבל: $\operatorname{lcm}(2-1,\ 2+1)=\operatorname{lcm}(1,3)=3$."
      "\n"
      r"אם $n>2$, אז: $\operatorname{lcm}(n-1,n+1)=(n-1)(n+1)/\gcd(n-1,n+1)$."
      "\n"
      r"נסמן: $\gcd(n-1,n+1)=d$. אז $d\mid(n-1)$ וגם $d\mid(n+1)\Leftarrow d\mid\big((n+1)-(n-1)\big)\Leftarrow d\mid 2\Leftarrow d\in\{1,2\}$."
      "\n"
      r"מכיוון ש-$n$ אי-זוגי (כי הוא ראשוני גדול מ-2), נשיג: $2\mid(n+1)$, $2\mid(n-1)$, אז $2\mid d$."
      "\n"
      r"משום ש-$2\mid d$ וגם $1\le d\le 2$ נקבל $d=2$. לכן $\operatorname{lcm}(n-1,n+1)=(n^2-1)/2$."
      "\n"
      r"מסקנה: $\operatorname{lcm}(n-1,n+1)=3$ עבור $n=2$, ו-$\operatorname{lcm}(n-1,n+1)=(n^2-1)/2$ עבור $n>2$."),

    Q(4, "ג", "computation", "combinatorics", 5,
      r"תהי $A=\{1,2,3,\dots,2n+1\}$, כאשר $5<n\in\mathbb{N}$."
      "\n"
      r"חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות התנאי: $|B\cap\{1,3,5,7,\dots,2n+1\}|=1$.",
      r"$B$ מקיימת התנאים $\iff B=\{x\}\cup C$, כאשר $x\in\{1,3,5,7,\dots,2n+1\}$, ו-$C\in P(\{2,4,6,\dots,2n\})\iff C\subseteq\{2,4,6,\dots,2n\}$:"
      "\n"
      r"$x\in\{1,3,5,7,\dots,2n+1\}\Leftarrow$ יש $n+1$ אופציות."
      "\n"
      r"$C\in P(\{2,4,6,\dots,2n\})\Leftarrow$ יש $2^n$ אופציות."
      "\n"
      r"מסקנה: מספר תתי-הקבוצות $B\in P(A)$ המקיימות התנאי $|B\cap\{1,3,5,7,\dots,2n+1\}|=1$ שווה ל: $(n+1)\cdot 2^n$."),
]

exam = {
    "examCode": "23A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ג, מועד א (30.01.2023)',
    "year": 2023,
    "examDate": "30.01.2023",
    "sourceFile": "23A-A exam with typed official solution, pp.1-8",
    "solutionFile": "23A-A typed official solution, pp.2-8",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
