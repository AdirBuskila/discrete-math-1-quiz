# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json -- discrete math 1 (20067), semester A 5783, moed B (21.02.2023).
4 questions x 25 points, each with 3 parts. Typed (purple) key parts are lecturer-solution;
handwritten parts are student-solution (author unknown). Checks: tools/verify/23A-B/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_23A-B.py
 - A part with numbered sub-claims is ONE item (Q2c, Q3a)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-B.json"


def Q(num, part, kind, topic, points, question, solution, typed, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution" if typed else "student-solution",
         "official": bool(typed), "confidence": "high" if typed else "med"}
    q.update(kw)
    return q


HDR = "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"
questions = [
    Q(1, "א", "computation", "logic_propositional", 8,
      HDR + "**המונח:** שקילות לוגית.\n"
      r"**שאלה:** האם הפסוקים הבאים הם שקולים לוגית: $p\to(q\vee r)\equiv(p\to q)\vee(p\to r)$",
      "הגדרה: שני פסוקים שקולים לוגית אם יש להם את אותה טבלת אמת.\n"
      "נבנה טבלת אמת:\n"
      "```\n"
      "p q r | q∨r | p→(q∨r) | p→q | p→r | (p→q)∨(p→r)\n"
      "T T T |  T  |    T     |  T  |  T  |      T\n"
      "T T F |  T  |    T     |  T  |  F  |      T\n"
      "T F T |  T  |    T     |  F  |  T  |      T\n"
      "T F F |  F  |    F     |  F  |  F  |      F\n"
      "F T T |  T  |    T     |  T  |  T  |      T\n"
      "F T F |  T  |    T     |  T  |  T  |      T\n"
      "F F T |  T  |    T     |  T  |  T  |      T\n"
      "F F F |  F  |    T     |  T  |  T  |      T\n"
      "```\n"
      "העמודות המודגשות (העמודה p→(q∨r) והעמודה האחרונה) זהות ולכן הוכחנו שהפסוקים הנתונים שקולים לוגית.", True),

    Q(1, "ב", "proof", "equivalence_relations", 8,
      "**המונח:** יחס שקילות.\n"
      r"**שאלה:** יהיו $A=\{1,2,3\}$ ו-$R_1,R_2\subseteq A\times A$ שני יחסי שקילות שונים. "
      r"הוכיחו או הפריכו: $R_2\cup R_1$ הוא יחס שקילות.",
      "הגדרה: כל יחס רפלקסיבי, סימטרי וטרנזיטיבי נקרא יחס שקילות.\n"
      "הטענה לא נכונה. דוגמה נגדית:\n"
      r"$R_2=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}$, $R_1=\{(1,1),(2,2),(3,3),(2,3),(3,2)\}$"
      "\n"
      r"אז $R_2\cup R_1$ אינו טרנזיטיבי ולכן אינו יחס שקילות: "
      r"$(1,2),(2,3)\in R_2\cup R_1$ אך $(1,3)\notin R_2\cup R_1$.", True),

    Q(1, "ג", "proof", "functions", 9,
      "**המונח:** פונקציה על.\n"
      r"**שאלה:** תהי פונקציה $f:\mathbb{N}\times\mathbb{N}\to\mathbb{N}-\{0\}$ מוגדרת לפי הכלל "
      r"$f(m,n)=2^n(2m+1)$ לכל $(m,n)\in\mathbb{N}\times\mathbb{N}$. הראו ש-$f$ היא על.",
      r"הגדרה: הפונקציה $f:A\to B$ נקראת על אם לכל $b\in B$ קיים $a\in A$ כך ש: $f(a)=b$."
      "\n"
      r"או: הפונקציה $f:A\to B$ נקראת על אם לכל $b\in B$ יש מקור."
      "\n"
      r"או: הפונקציה $f:A\to B$ נקראת על אם $f(A)=B$."
      "\n"
      r"למספר $1\in\mathbb{N}-\{0\}$ יש מקור: $f(0,0)=1$."
      "\n"
      r"לפי המשפט היסודי של האריתמטיקה לכל $2\le q\in\mathbb{N}-\{0\}$ יש ייצוג יחיד שבצורה "
      r"$q=(p_1)^{\alpha_1}\cdot(p_2)^{\alpha_2}\cdot\ldots\cdot(p_k)^{\alpha_k}$ כאשר "
      r"$p_1<p_2<\ldots<p_k$ הם מספרים ראשוניים, ולכל $\alpha_i\in\mathbb{N}-\{0\}$."
      "\n"
      r"אם $p_1=2$ אז $2m+1=(p_2)^{\alpha_2}\cdot\ldots\cdot(p_k)^{\alpha_k}$ ולכן $f(\alpha_1,m)=q$."
      "\n"
      r"אם $p_1>2$ אז $2m+1=(p_1)^{\alpha_1}\cdot(p_2)^{\alpha_2}\cdot\ldots\cdot(p_k)^{\alpha_k}$ ולכן $f(0,m)=q$."
      "\n"
      r"מסקנה: $f$ היא פונקציה על.", True),

    Q(2, "א", "proof", "induction", 11,
      r"הוכיחו באינדוקציה מתמטית שלכל $2\le n\in\mathbb{N}$ מתקיים:"
      "\n"
      r"$$\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\frac{1}{3\cdot4}+\cdots+\frac{1}{(n-1)\cdot n}=\frac{n-1}{n}$$",
      r"**I. בסיס:** $P(2)$: $\frac{1}{1\cdot2}=\frac{2-1}{2}\iff\frac12=\frac12\Rightarrow P(2)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=\text{TRUE}$ עבור $2\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ \frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\cdots+\frac{1}{(k-1)\cdot k}=\frac{k-1}{k}$ (נתון: TRUE)"
      "\n"
      r"$P(k+1):\ \frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\cdots+\frac{1}{k(k+1)}=\frac{k}{k+1}$"
      "\n"
      r"לפי הנחת האינדוקציה:"
      "\n"
      r"$$\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\cdots+\frac{1}{(k-1)k}+\frac{1}{k(k+1)}"
      r"=\frac{k-1}{k}+\frac{1}{k(k+1)}"
      r"=\frac{(k-1)(k+1)+1}{k(k+1)}=\frac{k^2}{k(k+1)}=\frac{k}{k+1}$$"
      "\n"
      r"$\Rightarrow P(k+1)=\text{TRUE}$."
      "\n"
      r"מסקנה: מ-I ו-II, לפי עקרון האינדוקציה, לכל $2\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$.", False),

    Q(2, "ב", "computation", "number_theory_gcd", 8,
      r"מצאו $x,y\in\mathbb{Z}$ בעזרת האלגוריתם המורחב של EUCLID כך ש: $\gcd(55,-40)=55x+(-40)y$.",
      r"נריץ את האלגוריתם המורחב על $55,40$ (עמודות: $a,\ b,\ \lfloor a/b\rfloor,\ d,\ x=y',\ y=x'-y'\lfloor a/b\rfloor$):"
      "\n"
      "```\n"
      "a    b    [a/b]   d    x     y\n"
      "55   40   1       5    3     -1-3*1 = -4\n"
      "40   15   2       5    -1    1-(-1)*2 = 3\n"
      "15   10   1       5    1     0-1*1 = -1\n"
      "10   5    2       5    0     1-0*2 = 1\n"
      "5    0    -       5    1     0\n"
      "```\n"
      r"$\gcd(55,40)=5=3\cdot55+(-4)\cdot40$"
      "\n"
      r"$\gcd(55,-40)=5=3\cdot55+4\cdot(-40)$"
      "\n"
      r"$x=3,\ y=4,\ d=5$.", False),

    Q(2, "ג", "proof", "partial_orders", 6,
      r"הוכיחו או הפריכו: אם $R_1,R_2\subseteq\{1,2\}\times\{1,2\}$ יחסי סדר מלא שונים, אז:"
      "\n"
      r"(1) $R_1\cup R_2$ הוא יחס שקילות."
      "\n"
      r"(2) $R_1\cap R_2$ אינו יחס שקילות.",
      r"על הקבוצה $A=\{1,2\}$ ניתן להגדיר שני יחסי סדר מלא שונים בלבד:"
      "\n"
      r"$R_1=\{(1,1),(2,2),(1,2)\}$, $R_2=\{(1,1),(2,2),(2,1)\}$"
      "\n"
      r"$R_1\cap R_2=\{(1,1),(2,2)\}$, $R_1\cup R_2=\{(1,1),(2,2),(1,2),(2,1)\}$"
      "\n"
      r"הם יחסי שקילות. לכן טענה (1) נכונה, וטענה (2) לא נכונה (הפרכה).", False),

    Q(3, "א", "proof", "sets_power_set", 10,
      r"תהיינה 3 קבוצות $C,B,A$ לא ריקות. הוכיחו או הפריכו:"
      "\n"
      r"(1) $(B\cup C)-A\subseteq(B-A)\cup(C-A)$."
      "\n"
      r"(2) $|A|=|\mathbb{R}|$, כאשר $A=(1,2)\cup(5,25]$.",
      r"**(1)** לכל $x\in(B\cup C)-A$: $x\in B\cup C\ \wedge\ x\notin A$, כלומר $(x\in B\vee x\in C)\wedge x\notin A$, "
      r"כלומר $(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)$, כלומר $x\in B-A\ \vee\ x\in C-A$, "
      r"כלומר $x\in(B-A)\cup(C-A)$. הטענה נכונה."
      "\n"
      r"**(2)** הפונקציה $f:(0,1)\to(1,2)$, $f(x)=x+1$ היא התאמה חד-חד-ערכית ועל, לכן $|(0,1)|=|(1,2)|$ "
      r"וגם $|(0,1)|=|\mathbb{R}|$."
      "\n"
      r"מכיוון ש: $(1,2)\subseteq(1,2)\cup(5,25]\subseteq\mathbb{R}$ נקבל: "
      r"$|\mathbb{R}|=|(0,1)|=|(1,2)|\le|A|\le|\mathbb{R}|$, לכן $|A|=|\mathbb{R}|$. הטענה נכונה.", False),

    Q(3, "ב", "computation", "sets_power_set", 9,
      r"תהיינה הקבוצות $A=\{5^m9^n:\ m,n\in\{0,1,2,\ldots,9\}\}$, $B=\{5^m7^n:\ m,n\in\{0,1,2,\ldots,9\}\}$."
      "\n"
      r"חשבו את: $|A\cap B|+|P(A\cup B)|+|P(A\times B)|$.",
      r"$x\in A\cap B\iff x=5^m9^n\in A\ \wedge\ x=5^m7^n\in B\iff x=5^m,\ m\in\{0,\ldots,9\}$, ולכן $|A\cap B|=10$."
      "\n"
      r"$A\cup B=(A-B)\cup(A\cap B)\cup(B-A)$, ולכן $|A\cup B|=|A|+|B|-|A\cap B|=100+100-10=190$."
      "\n"
      r"$$|A\cap B|+|P(A\cup B)|+|P(A\times B)|=10+2^{190}+2^{100\cdot100}$$", False),

    Q(3, "ג", "proof", "modular_fermat_wilson", 6,
      r"הראו ש: $46\mid\gcd\left(81^{11}-1,\ 22!+24\right)$.",
      r"נסמן $m=81^{11}-1=9^{22}-1=9^{23-1}-1$. לפי פרמה (23 מספר ראשוני) $23\mid m$."
      "\n"
      r"$m=81^{11}-1$ הוא מספר זוגי (כי $81^{11}$ אי-זוגי), ולכן $2\mid m$."
      "\n"
      r"$\gcd(2,23)=1$ ולכן $46\mid m$."
      "\n"
      r"נסמן $q=22!+24$. $q$ זוגי ולכן $2\mid q$."
      "\n"
      r"$q=\{(23-1)!+1\}+23$. לפי וילסון (23 ראשוני) $23\mid(23-1)!+1$, ולכן $23\mid q$. מכאן $46\mid q$."
      "\n"
      r"כלומר: $46\mid m$ ו-$46\mid q$, כלומר $46$ מחלק משותף של $m$ ו-$q$, ולכן $46\mid\gcd(m,q)$.", False),

    Q(4, "א", "proof", "equivalence_relations", 14,
      r"יהיה $R\subseteq\mathbb{Z}\times\mathbb{Z}$ היחס שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$ מתקיים: $xRy\iff 3\mid(x+5y)$."
      "\n"
      r"הראו ש: $R$ הוא יחס שקילות ומצאו את $\mathbb{Z}/R$. האם $R$ הוא יחס סדר חלקי?",
      r"**$R$ רפלקסיבי:** לכל $x\in\mathbb{Z}$: $xRx\Leftarrow 3\mid x+5x=6x$ (נכון)."
      "\n"
      r"**$R$ סימטרי:** לכל $x,y\in\mathbb{Z}$ אם $xRy$ אז $yRx$. $xRy\iff 3\mid x+5y$ (נתון: TRUE); "
      r"$yRx\iff 3\mid y+5x$ ?"
      "\n"
      r"$3\mid 6(x+y)=(x+5y)+(y+5x)$. מנתון $3\mid x+5y$ נקבל $3\mid y+5x$, כלומר $yRx$."
      "\n"
      r"**$R$ טרנזיטיבי:** לכל $x,y,z\in\mathbb{Z}$: $xRy\iff 3\mid(x+5y)$ וגם $yRz\iff 3\mid(y+5z)$. "
      r"אז $3\mid(x+5z+6y)$, כלומר $3\mid 6y$ ולכן $3\mid(x+5z)$, כלומר $xRz$."
      "\n"
      r"מסקנה: $R$ יחס שקילות."
      "\n"
      r"$[0]=\{x:\ x\in\mathbb{Z}\wedge 3\mid(x+5\cdot0)\}=\{3k:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}\wedge 3\mid(x+5)\}=\{x:\ x\in\mathbb{Z}\wedge 3\mid((x+2)+3)\}=\{x:\ x\in\mathbb{Z}\wedge 3\mid(x+2)\}=\{3k+1:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[2]=\{x:\ x\in\mathbb{Z}\wedge 3\mid(x+10)\}=\{x:\ x\in\mathbb{Z}\wedge 3\mid((x+1)+9)\}=\{x:\ x\in\mathbb{Z}\wedge 3\mid(x+1)\}=\{3k+2:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$R$ אינו יחס סדר חלקי: $(0,3)\in R\wedge(3,0)\in R$ אך $3\ne0$, ולכן $R$ אינו אנטי-סימטרי."
      "\n"
      r"$$\mathbb{Z}/R=\{[0],[1],[2]\}$$", False),

    Q(4, "ב", "computation", "number_theory_gcd", 6,
      r"חשבו את $\operatorname{lcm}(n-1,n+1)$, כאשר $n\in\mathbb{N}$.",
      r"אם $n=0$, אז נקבל: $\operatorname{lcm}(-1,+1)=\operatorname{lcm}(1,1)=1$"
      "\n"
      r"אם $n=1$, אז נקבל: $\operatorname{lcm}(0,2)=0$"
      "\n"
      r"אם $n=2$, אז נקבל: $\operatorname{lcm}(2-1,2+1)=\operatorname{lcm}(1,3)=3$"
      "\n"
      r"אם $2<n$, אז $\operatorname{lcm}(n-1,n+1)=\dfrac{(n-1)(n+1)}{\gcd(n-1,n+1)}$."
      "\n"
      r"נסמן ב: $\gcd(n-1,n+1)=d$. אז $d\mid(n-1)$ וגם $d\mid(n+1)\Rightarrow d\mid((n+1)-(n-1))\Rightarrow d\mid2\Rightarrow d\in\{1,2\}$."
      "\n"
      r"אם $n$ זוגי, נשיג ש: $(n-1),(n+1)$ אי-זוגיים וגם $d\in\{1,2\}\Leftarrow d=1$. לכן $\operatorname{lcm}(n-1,n+1)=(n^2-1)$."
      "\n"
      r"אם $n$ אי-זוגי, נשיג ש: $2\mid(n-1),\ 2\mid(n+1)$ ואז $2\mid d$. לכן $d=2$ (משום ש-$2\mid d$ וגם $1\le d\le2$) "
      r"$\Leftarrow\operatorname{lcm}(n-1,n+1)=(n^2-1)/2$."
      "\n"
      "מסקנות:\n"
      r"עבור $n=0$: $\operatorname{lcm}(n-1,n+1)=1$"
      "\n"
      r"עבור $n=1$: $\operatorname{lcm}(n-1,n+1)=0$"
      "\n"
      r"עבור $n=2$: $\operatorname{lcm}(n-1,n+1)=3$"
      "\n"
      r"עבור $2<n$ וגם $n$ זוגי: $\operatorname{lcm}(n-1,n+1)=(n^2-1)$"
      "\n"
      r"עבור $2<n$ וגם $n$ אי-זוגי: $\operatorname{lcm}(n-1,n+1)=(n^2-1)/2$",
      True),

    Q(4, "ג", "computation", "sets_power_set", 5,
      r"תהי $A=\{1,2,3,\ldots,2n+1\}$, כאשר $5<n\in\mathbb{N}$."
      "\n"
      r"חשבו כמה תת-קבוצות $B\in P(A)$ מקיימות את התנאי $B\cup\{1,3,5,7,\ldots,2n+1\}=A$.",
      r"$B$ מקיימת את התנאי $\iff B=\{2,4,\ldots,2n\}\cup C$, כאשר $C\subseteq\{1,3,5,7,\ldots,2n+1\}$."
      "\n"
      r"אופציות: $|C|$ יש $2^{n+1}$."
      "\n"
      r"מסקנה: מספר תתי-הקבוצות $B\in P(A)$ המקיימות את התנאי $B\cup\{1,3,5,7,\ldots,2n+1\}=A$ שווה ל: $2^{n+1}$.", True),
]

exam = {
    "examCode": "23A-B",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ג, מועד ב (21.02.2023)',
    "year": 2023,
    "examDate": "21.02.2023",
    "sourceFile": "23A-B exam with solution, pp.1-8",
    "solutionFile": "23A-B solution (typed and handwritten, author unknown), pp.2-8",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
