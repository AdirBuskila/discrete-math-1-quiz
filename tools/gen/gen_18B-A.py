# -*- coding: utf-8 -*-
"""Generator for tools/raw/18B-A.json -- discrete math 1 (21166), semester B 5778, moed A (08.07.2018).
4 mandatory questions of 25 points (scan, read by vision). The handwritten key (blue ink, author unknown) is student-solution.
The printed cover reads "semester A, moed B" (copy of the March cover); the folder and the date say the July sitting.
Checks: tools/verify/18B-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_18B-A.py
 - Q1a, Q1b (b1+b2), Q2a (the two alternative claims, "or"), Q2b (b1+b2), Q3a (a1+a2) are ONE item each (the id scheme
   allows a single letter per part); the key proves both Q2a claims."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18B-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q



questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "proof", "sets_power_set", 8,
      r"הגדירו את המושג של **מכפלה קרטזית** של 2 קבוצות."
      "\n"
      r"תנו דוגמאות של קבוצות שונות וסופיות $A_1,B_1,A_2,B_2$ כך ש: $A_1\times B_1\ne B_1\times A_1$ ו: $A_2\times B_2=B_2\times A_2$.",
      r"**הגדרה:** תהיינה $A,B$ קבוצות. המכפלה הקרטזית של $A$ ו-$B$ היא $A\times B=\{(a,b):\ a\in A\wedge b\in B\}$."
      "\n"
      r"**דוגמאות:**"
      "\n"
      r"$B_1=\{2\}$, $A_1=\{1\}$: $A_1\times B_1=\{(1,2)\}\ne\{(2,1)\}=B_1\times A_1$."
      "\n"
      r"$B_2=\varnothing$, $A_2=\{1\}$: $A_2\times B_2=\varnothing=B_2\times A_2$."),

    Q(1, "ב", "proof", "cardinality_sets", 12,
      "הוכיחו או הפריכו:\n"
      r"**(1)** $|\mathbb{Q}\cap(-1,1)|=|\mathbb{R}|$."
      "\n"
      r"**(2)** אם $2<|B|<|A|$ ו-$P(A\cup B)=P(A)\cup P(B)$, אזי $B\subset A$.",
      r"**(1)** הטענה אינה נכונה, כי: $\mathbb{Q}\cap(-1,1)\subseteq\mathbb{Q}$, ולכן $|\mathbb{Q}\cap(-1,1)|\le|\mathbb{Q}|<|\mathbb{R}|$, "
      r"כי $|\mathbb{Q}|=\aleph_0<|\mathbb{R}|$."
      "\n"
      r"**(2)** הטענה נכונה. נניח בדרך השלילה: $B\not\subseteq A$."
      "\n"
      r"אז קיים $b\in B-A$ (כי $B\not\subseteq A$), וקיים $a\in A-B$ (כי $|B|<|A|$)."
      "\n"
      r"אז $\{a,b\}\in P(A\cup B)$, אבל $\{a,b\}\notin P(A)\cup P(B)$ (כי $b\notin A$ ו-$a\notin B$)."
      "\n"
      r"לכן $P(A\cup B)\ne P(A)\cup P(B)$, בסתירה להנחה. לכן $B\subseteq A$, ומכיוון ש-$|B|<|A|$, $B\subset A$."),

    Q(1, "ג", "proof", "quantifiers_proofs", 5,
      "שלולו את הטענה:\n"
      "\"קיים $x\\in A$ או קיים $y\\in B$, כך שלכל $z\\in C$ מתקיים: $x\\le y+z$\" "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      "השלילה: "
      "\"לכל $x\\in A$ ולכל $y\\in B$ קיים $z\\in C$ כך ש: $x>y+z$\"."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 10,
      r"השתמשו באינדוקציה מתמטית כדי להוכיח את נכונות הטענה הבאה:"
      "\n"
      r"**(1)** לכל $n\in\mathbb{N}$, $1\le n$, מתקיים: $1+5+9+\ldots+(4n-3)=n(2n-1)$."
      "\n"
      r"**או (2)** לכל $n\in\mathbb{N}$, $1\le n$, מתקיים: $n^3<10^n$.",
      r"**(1)** $P(n):\ 1+5+9+\ldots+(4n-3)=n(2n-1)$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ 1=1\cdot(2-1)$ — TRUE."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $k\ge1$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ 1+5+\ldots+(4k-3)=k(2k-1)$"
      "\n"
      r"$P(k+1):\ 1+5+\ldots+(4k+4-3)=(k+1)(2k+2-1)$"
      "\n"
      r"$1+5+\ldots+(4k+1)=1+5+\ldots+(4k-3)+(4k+1)$, ולפי $P(k)=\text{TRUE}$:"
      "\n"
      r"$$k(2k-1)+4k+1=2k^2-k+4k+1=2k^2+3k+1$$"
      "\n"
      r"וגם $(k+1)(2k+2-1)=(k+1)(2k+1)=2k^2+3k+1$."
      "\n"
      r"האגפים שווים, ולכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**III.** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**(2)** $P(n):\ n^3<10^n$, לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ 1^3<10^1$ — TRUE."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $1\le k\in\mathbb{N}$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ k^3<10^k$"
      "\n"
      r"$P(k+1):\ (k+1)^3<10^{k+1}$"
      "\n"
      r"$$(k+1)^3=k^3+3k^2+3k+1\le k^3+3k^3+3k^3+k^3=8k^3<10\cdot k^3<10\cdot10^k=10^{k+1}$$"
      "\n"
      r"(האי-שוויון האחרון לפי הנחת האינדוקציה $P(k)=\text{TRUE}$.) לכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**III.** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $n\in\mathbb{N}$, $n\ge1$."),

    Q(2, "ב", "computation", "recurrence_sums", 10,
      r"**(1)** מצאו את הצורה המפורשת של $(a_n)$, כאשר: $a_n=7a_{n-1}-12a_{n-2}-6$, $a_0=0$, $a_1=3$."
      "\n"
      r"**(2)** הוכיחו או הפריכו: $a_n$ הוא מספר ראשוני אם ורק אם $n=1$, כאשר $a_n$ הוא הפתרון של סעיף (1).",
      r"**(1)** המשוואה האופיינית: $r^2=7r-12\iff r^2-7r+12=0$, ולכן $r_1=3$, $r_2=4$."
      "\n"
      r"פתרון הנוסחה ההומוגנית: $a_n^{(h)}=C_1\cdot3^n+C_2\cdot4^n$."
      "\n"
      r"פתרון פרטי: $a_n^{(p)}=A\cdot n^s$, כאשר $s=0$ כי $r=1$ אינו שורש של $r^2-7r+12=0$, ולכן $a_n^{(p)}=A$."
      "\n"
      r"נציב: $A=7A-12A-6\iff6A=-6\Rightarrow A=-1$."
      "\n"
      r"הפתרון הכללי: $a_n=a_n^{(h)}+a_n^{(p)}=C_1\cdot3^n+C_2\cdot4^n-1$."
      "\n"
      r"$a_0=C_1+C_2-1=0$ ו-$a_1=3C_1+4C_2-1=3$, כלומר $C_1+C_2=1$ ו-$3C_1+4C_2=4$. נקבל $C_2=1$, $C_1=0$."
      "\n"
      r"מסקנה: $a_n=4^n-1$, לכל $n\in\mathbb{N}$."
      "\n"
      r"**(2)** $a_0=0$, $a_1=3$ (ראשוני)."
      "\n"
      r"לכל $2\le n\in\mathbb{N}$: $a_n=4^n-1=4^n-1^n=(4-1)\left(4^{n-1}+4^{n-2}+\ldots+4+1\right)=3\cdot\left(4^{n-1}+4^{n-2}+\ldots+1\right)$."
      "\n"
      r"הגורם $4^{n-1}+\ldots+1$ שונה מ-1 ($n\ge2$), ולכן $a_n\ne3$ ו-$a_n$ אינו ראשוני."
      "\n"
      r"מסקנה: $a_n$ ראשוני $\iff n=1$. הטענה נכונה."),

    Q(2, "ג", "proof", "combinatorics", 5,
      r"חשבו את $f(n)=\sum_{k=0}^{n}\left(\binom{n}{k}\cdot\left(2^k\cdot3^k+5^n\right)\right)$ והראו ש: $f(n)=O(11^n)$.",
      r"$f(n)=\sum_{k=0}^{n}\binom nk(2\cdot3)^k+5^n\cdot\sum_{k=0}^{n}\binom nk=S_1+S_2$."
      "\n"
      r"$(x+1)^n=\sum_{k=0}^{n}\binom nkx^k$. עבור $x=6$: $S_1=\sum_{k=0}^{n}\binom nk6^k=7^n$. עבור $x=1$: $S_2=\sum_{k=0}^{n}\binom nk=2^n$."
      "\n"
      r"$$f(n)=7^n+5^n\cdot2^n=7^n+10^n\le2\cdot10^n\le2\cdot11^n=c_0\cdot11^n$$"
      "\n"
      r"עבור $c_0=2$ ו-$n_0=1\le n\in\mathbb{N}$. מסקנה: $f(n)=O(11^n)$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "modular_fermat_wilson", 6,
      "הוכיחו או הפריכו:\n"
      r"**(1)** הפונקציה $\varnothing$ של Euler היא פונקציה חד-חד-ערכית;"
      "\n"
      r"**(2)** קיים מספר $n\in\mathbb{N}$, $1\le n$, והוא יחיד, המקיים: $n$ ו-$\varnothing(n)$ שניהם מספרים ראשוניים. כאן $\varnothing$ היא פונקציית Euler.",
      r"**(1)** הטענה אינה נכונה: $\varnothing(1)=1=\varnothing(2)$ אך $1\ne2$, ולכן $\varnothing$ אינה חד-חד-ערכית."
      "\n"
      r"**(2)** הטענה נכונה."
      "\n"
      r"עבור $n=2$: $\varnothing(2)=1$ אינו ראשוני."
      "\n"
      r"עבור $n=3$: $3$ ראשוני, ו-$\varnothing(3)=2$ ראשוני."
      "\n"
      r"עבור $n>3$: אם $n$ אינו ראשוני, התנאי אינו מתקיים. אם $n>3$ ראשוני, אז $n\ge5$ ו-$\varnothing(n)=n-1$. "
      r"$n-1$ מתחלק ב-1, ב-$n-1$ וגם ב-2 (כי $n-1$ זוגי), ו-$2\ne n-1$, ולכן $\varnothing(n)=n-1$ אינו ראשוני."
      "\n"
      r"לכן $n=3$ הוא המספר היחיד המקיים את התנאי, והטענה נכונה."),

    Q(3, "ב", "proof", "partial_orders", 5,
      r"הוכיחו או הפריכו: אם $A=\{1,2\}$ ו-$R\subseteq A\times A$ הוא יחס רפלקסיבי ולא סימטרי, אזי $R$ הוא יחס סדר מלא.",
      r"הטענה נכונה."
      "\n"
      r"$R\subseteq A\times A$ ו-$A=\{1,2\}$. $R$ רפלקסיבי, ולכן $(1,1),(2,2)\in R$. $R$ אינו סימטרי, ולכן $(1,2)\in R$ (או $(2,1)\in R$)."
      "\n"
      r"לכן יש 2 אפשרויות:"
      "\n"
      r"$R_1=\{(1,1),(2,2),(1,2)\}$"
      "\n"
      r"$R_2=\{(1,1),(2,2),(2,1)\}$"
      "\n"
      r"$R_1$ ו-$R_2$ רפלקסיביים, אנטי-סימטריים וטרנזיטיביים, ולכן הם יחסי סדר חלקי. $R_1$ הוא יחס סדר מלא כי לכל $x,y\in A$ מתקיים $(x,y)\in R_1$ או $(y,x)\in R_1$. "
      r"$R_2$ הוא ההופכי של $R_1$, ולכן גם הוא יחס סדר מלא."),

    Q(3, "ג", "proof", "equivalence_relations", 14,
      r"היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ מוגדר לפי הכלל: לכל $x,y\in\mathbb{Z}$, מתקיים $xRy\iff x^2+y$ הוא מספר זוגי."
      "\n"
      r"בדקו ש-$R$ הוא יחס שקילות מעל $\mathbb{Z}$ ומצאו את $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי? אם כן הוכיחו, אחרת תנו דוגמה נגדית.",
      r"**(1)** $R$ רפלקסיבי: לכל $x\in\mathbb{Z}$ נכון $xRx$, כי $x^2+x=x(x+1)$ הוא מספר זוגי (כי $x$ או $x+1$ זוגי)."
      "\n"
      r"$R$ סימטרי: לכל $x,y\in\mathbb{Z}$, אם $xRy$ אז $yRx$. נניח $xRy$, כלומר $x^2+y=2k$ (זוגי). "
      r"נוכיח $yRx$, כלומר ש-$y^2+x=m$ זוגי: $m+2k=(x^2+y)+(y^2+x)=(x^2+x)+(y^2+y)$ הוא זוגי (סכום של שני זוגיים), ולכן $m=(m+2k)-2k$ זוגי."
      "\n"
      r"$R$ טרנזיטיבי: לכל $x,y,z\in\mathbb{Z}$, אם $xRy$ ו-$yRz$ אז $xRz$. נניח $x^2+y=2k$ ו-$y^2+z=2q$. אז "
      r"$2k+2q=(x^2+y)+(y^2+z)=(y^2+y)+(x^2+z)$ הוא זוגי, ו-$y^2+y$ זוגי, ולכן $x^2+z$ זוגי, כלומר $xRz$."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"מחלקות השקילות: $[0]=\{x\in\mathbb{Z}:0Rx\}=\{x\in\mathbb{Z}:0^2+x=2k\}=\{2k:\ k\in\mathbb{Z}\}$."
      "\n"
      r"$[1]=\{x\in\mathbb{Z}:1Rx\}=\{x\in\mathbb{Z}:1^2+x=2k\}=\{x\in\mathbb{Z}:x=2k-1\}$."
      "\n"
      r"$[0]\cup[1]=\mathbb{Z}$, ולכן $\mathbb{Z}/R=\{[0],[1]\}$."
      "\n"
      r"**(2)** $R$ אינו יחס סדר חלקי, כי הוא אינו אנטי-סימטרי. דוגמה נגדית: $(2,4)\in R$ כי $2^2+4=8$ זוגי, ו-$(4,2)\in R$ כי $4^2+2=18$ זוגי, אך $2\ne4$."),

    # ---------------- Q4 ----------------
    Q(4, "א", "computation", "combinatorics", 6,
      r"תהי $A=\{1,2,\ldots,100\}$. חשבו את $m+\sum_{B\in P(A)}|B|$ כאשר $m$ הוא מספר תת-הקבוצות בגודל אי-זוגי שקיימים ב-$A$.",
      r"$m=2^{100-1}=2^{99}$, כי:"
      "\n"
      r"$\binom{100}{0}+\binom{100}{1}+\ldots+\binom{100}{100}=2^{100}$, ו-$\binom{100}{0}+\binom{100}{2}+\ldots+\binom{100}{100}=\binom{100}{1}+\binom{100}{3}+\ldots+\binom{100}{99}=\frac{2^{100}}2=2^{99}$."
      "\n"
      r"יש $\binom{100}{k}$ תת-קבוצות $B\in P(A)$ בגודל $k$, לכל $0\le k\le100$ (בפרט $\binom{100}{0}$ עבור $B=\varnothing$ עם $|B|=0$), ולכן:"
      "\n"
      r"$$\sum_{B\in P(A)}|B|=0\cdot|\varnothing|+1\cdot\binom{100}{1}+2\cdot\binom{100}{2}+\ldots+100\cdot\binom{100}{100}=\sum_{k=0}^{100}\binom{100}{k}\cdot k$$"
      "\n"
      r"$(x+1)^{100}=\sum_{k=0}^{100}\binom{100}{k}x^k\ \Rightarrow\ 100(x+1)^{99}=\sum_{k=0}^{100}\binom{100}{k}kx^{k-1}$. עבור $x=1$: $100\cdot2^{99}=\sum_{k=0}^{100}\binom{100}{k}\cdot k$."
      "\n"
      r"$$m+\sum_{B\in P(A)}|B|=2^{99}+100\cdot2^{99}=101\cdot2^{99}$$"),

    Q(4, "ב", "computation", "functions", 6,
      r"תהי קבוצת הפונקציות $\Omega=\{f\,/\,f:\{1,2,3,4,5,6,7\}\to\{1,2,3,4,5,6,7\}\}$."
      "\n"
      r"כמה פונקציות ב-$\Omega$ הן הפיכות ומקיימות התנאי: $f(\{1,2,3\})=\{1,2,3\}$?",
      r"$f$ הפיכה $\iff f$ חד-חד-ערכית ועל $\iff f$ תמורה של $\{1,2,\ldots,7\}$."
      "\n"
      r"בנוסף: $f(\{1,2,3\})=\{1,2,3\}$ $\Rightarrow$ $3!$ אפשרויות; ולכן $f(\{4,5,6,7\})=\{4,5,6,7\}$ $\Rightarrow$ $4!$ אפשרויות."
      "\n"
      r"מסקנה: $3!\cdot4!=144$ פונקציות מתאימות."),

    Q(4, "ג", "computation", "combinatorics", 6,
      r"תהי הקבוצה $A=\{a,b,c\}$. מצאו כמה מילים ב-18 אותיות מ-$A$ ניתן ליצור, כאשר בכל מילה אין חשיבות לסדר האותיות ובנוסף יופיעו:"
      "\n"
      r"האות $a$ יותר מ-4 פעמים, האות $b$ יותר מפעמיים, האות $c$ לפחות 7 פעמים.",
      r"נסמן ב-$x_1,x_2,x_3$ את מספר המופעים של $a,b,c$ במילה. אז:"
      "\n"
      r"$x_1+x_2+x_3=18$, $x_1>4\Rightarrow x_1\ge5$, $x_2>2\Rightarrow x_2\ge3$, $x_3\ge7$, כאשר $x_i\in\mathbb{Z}$."
      "\n"
      r"מספר המילים שווה למספר הפתרונות של המערכת. נסמן $y_1=x_1-5$, $y_2=x_2-3$, $y_3=x_3-7$. אז $y_i\ge0$ ו-$x_i=y_i+5,\,y_i+3,\,y_i+7$ בהתאמה, ולכן:"
      "\n"
      r"$x_1+x_2+x_3=18\iff y_1+5+y_2+3+y_3+7=18\iff y_1+y_2+y_3=3$, $y_i\in\mathbb{N}$."
      "\n"
      r"מספר הפתרונות: $D(3,3)=\binom52=10$."),

    Q(4, "ד", "computation", "modular_fermat_wilson", 7,
      r"בדקו האם $8\mid(\varnothing\circ\varnothing)(n+n^2)$, כאשר $n=\gcd(11,\,70^{10}-1)$.",
      r"$11$ ראשוני ו-$11\nmid70$, ולכן לפי משפט FERMAT: $11\mid70^{10}-1$."
      "\n"
      r"לכן $\gcd(11,70^{10}-1)=11$, כלומר $n=11$."
      "\n"
      r"$n^2+n=121+11=132=4\cdot33=2^2\cdot3\cdot11$."
      "\n"
      r"$\varnothing(132)=132\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac1{11}\right)=2^2\cdot3\cdot11\cdot\frac12\cdot\frac23\cdot\frac{10}{11}=40$."
      "\n"
      r"$(\varnothing\circ\varnothing)(132)=\varnothing(\varnothing(132))=\varnothing(40)=\varnothing(2^3\cdot5)=2^3\cdot5\left(1-\frac12\right)\left(1-\frac15\right)=8\cdot5\cdot\frac12\cdot\frac45=16$."
      "\n"
      r"מסקנה: $8\mid16$, ולכן $8\mid(\varnothing\circ\varnothing)(n^2+n)$. התשובה: כן."),
]

exam = {
    "examCode": "18B-A",
    "examLabel": 'בדידה 1, סמסטר ב\' תשע"ח, מועד א (08.07.2018)',
    "year": 2018,
    "examDate": "08.07.2018",
    "sourceFile": "18B-A exam with handwritten solution, pp.1-11",
    "solutionFile": "18B-A handwritten solution (author unknown), pp.3-11",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
