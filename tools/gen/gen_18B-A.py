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
      r"עבור $n=1$: $1$ אינו ראשוני."
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

# ---- rubric / pitfalls / steps (ai-draft); every expected value is recomputed in tools/verify/18B-A/verify.py ----
IDS = "abcdefgh"


def ch(prompt, right, wrongs, explain, pos=0):
    vals = list(wrongs)
    vals.insert(pos, right)
    return {"type": "choice", "prompt": prompt,
            "options": [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)],
            "correctId": IDS[pos], "explain": explain}


def nm(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def add(num, part, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError((num, part))


add(1, "א",
    rubric=rub((r"הגדרה נכונה: $A\times B=\{(a,b):a\in A\wedge b\in B\}$", 3),
               (r"דוגמה ל-$A_1\times B_1\ne B_1\times A_1$ עם בדיקה, למשל $\{1\}$ ו-$\{2\}$", 3),
               (r"דוגמה ל-$A_2\times B_2=B_2\times A_2$ עם קבוצות שונות, למשל $\{1\}$ ו-$\varnothing$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לתת דוגמה שבה $A_2=B_2$ (הקבוצות צריכות להיות שונות).",
              r"לכתוב את איברי המכפלה כקבוצות $\{a,b\}$ במקום כזוגות סדורים $(a,b)$."],
    steps=[ch(r"איזו מההגדרות הבאות היא ההגדרה של $A\times B$?", r"$\{(a,b):a\in A\wedge b\in B\}$",
              [r"$\{(a,b):a\in A\vee b\in B\}$", r"$\{\{a,b\}:a\in A\wedge b\in B\}$", r"$\{(b,a):a\in A\wedge b\in B\}$"],
              r"המכפלה הקרטזית היא קבוצת כל הזוגות הסדורים $(a,b)$ עם $a\in A$ **וגם** $b\in B$. האפשרות השלישית מגדירה את $B\times A$, והשנייה מתעלמת מהסדר.", pos=1),
           nm(r"נתון $A_1=\{1\}$ ו-$B_1=\{2\}$. מה גודל $(A_1\times B_1)\cup(B_1\times A_1)$?", 2,
              r"$A_1\times B_1=\{(1,2)\}$ ו-$B_1\times A_1=\{(2,1)\}$ שונות זו מזו, ולכן האיחוד מכיל 2 זוגות."),
           ch(r"איזה זוג קבוצות **שונות** מקיים $A\times B=B\times A$?", r"$A=\{1\}$, $B=\varnothing$",
              [r"$A=\{1\}$, $B=\{2\}$", r"$A=\{1,2\}$, $B=\{1\}$", r"$A=\{1\}$, $B=\{1,2\}$"],
              r"עם $B=\varnothing$ שני הצדדים ריקים. בשאר המקרים המכפלות שונות (נבדק בחישוב ישיר).", pos=0)],
    stepsSource="ai-verified")

add(1, "ב",
    rubric=rub((r"סעיף (1): קביעה שהטענה אינה נכונה והכלה $\mathbb{Q}\cap(-1,1)\subseteq\mathbb{Q}$", 2),
               (r"סעיף (1): $|\mathbb{Q}|=\aleph_0<|\mathbb{R}|$ ולכן העוצמות שונות", 2),
               (r"סעיף (2): קביעה שהטענה נכונה והנחת השלילה $B\not\subseteq A$", 2),
               (r"סעיף (2): קיום $b\in B-A$ וקיום $a\in A-B$ (לפי $|B|<|A|$)", 2),
               (r"סעיף (2): $\{a,b\}\in P(A\cup B)$ אך $\{a,b\}\notin P(A)\cup P(B)$", 2),
               (r"סעיף (2): סתירה והמסקנה $B\subset A$ (הכלה ממש לפי $|B|<|A|$)", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להסיק $|\mathbb{Q}\cap(-1,1)|=|\mathbb{R}|$ מכך שהקבוצה “צפופה” בקטע, במקום להשוות עוצמות.",
              r"לשכוח שהקיום של $a\in A-B$ נובע מ-$|B|<|A|$, ולא נדרש בכלל מהנחת השלילה.",
              r"לסיים ב-$B\subseteq A$ בלי לנמק מדוע ההכלה היא ממש."],
    steps=[ch(r"האם הטענה $|\mathbb{Q}\cap(-1,1)|=|\mathbb{R}|$ נכונה?", "לא נכונה", ["נכונה"],
              r"$|\mathbb{Q}\cap(-1,1)|\le|\mathbb{Q}|=\aleph_0<|\mathbb{R}|$.", pos=0),
           ch(r"האם הטענה בסעיף (2) נכונה: אם $2<|B|<|A|$ ו-$P(A\cup B)=P(A)\cup P(B)$ אז $B\subset A$?", "נכונה", ["לא נכונה"],
              r"הפתרון מוכיח אותה. (נבדק ברוטפורס על כל זוגות הקבוצות של $\{1,\ldots,5\}$.)", pos=1),
           ch("באיזו שיטה משתמש הפתרון בסעיף (2)?",
              r"הוכחה בשלילה: מניחים $B\not\subseteq A$ ומוצאים קבוצה השייכת ל-$P(A\cup B)$ ואינה שייכת ל-$P(A)\cup P(B)$",
              [r"אינדוקציה על $|B|$", r"בניית פונקציה חד-חד-ערכית מ-$B$ אל $A$", r"דוגמה נגדית מפורשת"],
              r"הפתרון מניח $B\not\subseteq A$ ומגיע לסתירה להנחה $P(A\cup B)=P(A)\cup P(B)$.", pos=0),
           {"type": "findbug", "prompt": r"בגרסה הבאה של ההוכחה שורה אחת שונתה. איזו?",
            "lines": [r"נניח בדרך השלילה: $B\not\subseteq A$.",
                      r"אז קיים $b\in B-A$, וקיים $a\in A-B$ (כי $|B|<|A|$).",
                      r"אז $\{a,b\}\in P(A\cup B)$, כי $a,b\in A\cup B$.",
                      r"וגם $\{a,b\}\in P(A)$ (כי $a\in A$), ולכן $\{a,b\}\in P(A)\cup P(B)$.",
                      r"לכן $P(A\cup B)\ne P(A)\cup P(B)$, בסתירה להנחה."],
            "bugIndex": 3,
            "explain": r"בשורה הרביעית (אינדקס 3): $\{a,b\}\not\subseteq A$ כי $b\notin A$, ו-$\{a,b\}\not\subseteq B$ כי $a\notin B$, ולכן $\{a,b\}\notin P(A)\cup P(B)$. הטענה בשורה שגויה (נבדק בספירה)."}],
    stepsSource="ai-verified")

add(1, "ג",
    rubric=rub((r"הפיכת $\exists x\ \text{or}\ \exists y$ ל-$\forall x\ \forall y$", 2),
               (r"הפיכת $\forall z$ ל-$\exists z$", 1),
               (r"שלילת $x\le y+z$ ל-$x>y+z$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להשאיר “או” בין הכמתים במקום להפוך לכמת כללי על שני המשתנים.",
              r"לכתוב $x\ge y+z$ במקום $x>y+z$."],
    steps=[ch(r"הפתרון קורא את הטענה “קיים $x\in A$ או קיים $y\in B$ כך שלכל $z\in C$ מתקיים $x\le y+z$” כקיום זוג $(x,y)$. מה צורת הכמתים בשלילה?",
              r"לכל $x\in A$ ולכל $y\in B$ קיים $z\in C$",
              [r"קיים $x\in A$ וקיים $y\in B$ כך שלכל $z\in C$", r"לכל $x\in A$ ולכל $y\in B$ ולכל $z\in C$", r"לכל $x\in A$ קיים $y\in B$ וקיים $z\in C$"],
              r"שלילה הופכת כל כמת ($\exists\to\forall$, $\forall\to\exists$). כל אחת מהאפשרויות האחרות שונה מהשלילה בדוגמה כלשהי (נבדק על קבוצות סופיות קטנות, כולל ריקות).", pos=0),
           ch(r"מה בא במקום $x\le y+z$ בשלילה (ללא סימן שלילה)?", r"$x>y+z$", [r"$x\ge y+z$", r"$x<y+z$", r"$x\ne y+z$"],
              r"שלילת $\le$ היא $>$; האפשרויות האחרות שונות ממנה כשיש שוויון.", pos=2)],
    stepsSource="ai-verified")

add(2, "א",
    rubric=rub((r"בדיקת בסיס $P(1)$ (בכל אחד משני הסעיפים; די לפתור אחד מהם, כי השאלה היא (1) או (2))", 2),
               (r"ניסוח $P(k)$ ו-$P(k+1)$", 2),
               (r"שימוש בהנחה $P(k)$: ב-(1) $k(2k-1)+4k+1$, ב-(2) $10k^3<10\cdot10^k=10^{k+1}$", 2),
               (r"הצעד עד הסוף: ב-(1) $2k^2+3k+1=(k+1)(2k+1)$, ב-(2) $(k+1)^3\le8k^3<10k^3$ (שימוש ב-$k\ge1$)", 3),
               (r"מסקנה מהבסיס והצעד לכל $n\ge1$", 1)),
    # note: the exam says "או": answering (1) OR (2) alone earns the full 10; each rubric line lists both routes
    rubricSource="ai-verified",
    pitfalls=[r"לבדוק את הצעד של טענה (1) בלי להשתמש בהנחת האינדוקציה, אלא להציב ערכים.",
              r"בסעיף (2) לחסום $(k+1)^3$ ב-$8k^3$ בלי להשתמש בכך ש-$k\ge1$ (כך ש-$k\le k^3$).",
              r"להגדיר בסיס $n=0$ לטענה שמנוסחת רק עבור $n\ge1$."],
    steps=[nm(r"בטענה (1) מחשבים בצעד $k(2k-1)+4k+1$. מה ערכו עבור $k=3$? (צריך להתאים ל-$(k+1)(2k+1)$.)", 28,
              r"$3\cdot5+13=28=4\cdot7$."),
           ch("באיזו שיטה משתמש הפתרון?", r"אינדוקציה רגילה עם בסיס $n=1$ וצעד $P(k)\Rightarrow P(k+1)$",
              ["אינדוקציה חזקה", "הוכחה בשלילה", "אינדוקציה עם שני מקרי בסיס"],
              "בשתי הטענות הפתרון מוכיח בסיס $P(1)$ ואז $P(k)\\Rightarrow P(k+1)$.", pos=0),
           nm(r"בטענה (2): מהו המספר השלם הקטן ביותר $c$ כך ש-$(k+1)^3\le c\cdot k^3$ לכל שלם $k\ge1$?", 8,
              r"$(1+1/k)^3$ יורד ב-$k$, ומקסימומו ב-$k=1$ הוא $8$; הפתרון משתמש ב-$8k^3$."),
           {"type": "findbug", "prompt": r"בגרסה הבאה של צעד האינדוקציה לטענה (2) שורה אחת שונתה. איזו?",
            "lines": [r"$(k+1)^3=k^3+3k^2+3k+1$",
                      r"$\le k^3+3k^3+3k^3+k^3=8k^3$",
                      r"$<10\cdot k^3$",
                      r"$<10\cdot10^k$ (לפי $P(k)$)",
                      r"$=10^{k+2}$"],
            "bugIndex": 4,
            "explain": r"בשורה האחרונה (אינדקס 4): $10\cdot10^k=10^{k+1}$ ולא $10^{k+2}$, וזה בדיוק מה שצריך להוכיח ל-$P(k+1)$."}],
    stepsSource="ai-verified")

add(2, "ב",
    rubric=rub((r"משוואה אופיינית ושורשים $r_1=3$, $r_2=4$ ופתרון הומוגני", 2),
               (r"פתרון פרטי קבוע $A=-1$ (כי $1$ אינו שורש)", 2),
               (r"קבועים $C_1=0$, $C_2=1$ והנוסחה $a_n=4^n-1$", 3),
               (r"סעיף (2): פירוק $4^n-1=3\cdot(4^{n-1}+\cdots+1)$", 2),
               (r"סעיף (2): $a_0=0$, $a_1=3$ ראשוני, ו-$a_n$ פריק לכל $n\ge2$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח לבדוק את $a_0=0$ ($0$ אינו ראשוני) כשקובעים מתי $a_n$ ראשוני.",
              r"לא לוודא שהמנה $4^{n-1}+\cdots+1$ שונה מ-1 עבור $n\ge2$."],
    steps=[nm(r"מהו השורש הגדול של המשוואה האופיינית $r^2-7r+12=0$?", 4, r"$(r-3)(r-4)=0$."),
           nm(r"מהו הקבוע $A$ של הפתרון הפרטי (קבוע) במשוואה $a_n=7a_{n-1}-12a_{n-2}-6$?", -1, r"$A=7A-12A-6\Rightarrow6A=-6$."),
           nm(r"מהו $a_3$? (מהנוסחה המפורשת, ושווה לחישוב מהנסיגה.)", 63, r"$a_2=7\cdot3-0-6=15$ ו-$a_3=7\cdot15-12\cdot3-6=63=4^3-1$."),
           ch(r"האם הטענה “$a_n$ ראשוני אם ורק אם $n=1$” נכונה?", "נכונה", ["לא נכונה"],
              r"$a_0=0$, $a_1=3$, ולכל $n\ge2$ מתקיים $3\mid a_n$ ו-$a_n>3$ (נבדק עבור $n<40$).", pos=1),
           ch("באיזו שיטה משתמש הפתרון להראות ש-$a_n$ אינו ראשוני עבור $n\\ge2$?",
              r"פירוק $4^n-1=(4-1)(4^{n-1}+\cdots+4+1)$",
              ["משפט פרמה הקטן", "אינדוקציה על $n$", "הכלה והפרדה"],
              r"הפתרון מפרק לגורמים לפי $a^n-b^n$ ומראה שהגורם $3$ מחלק, והמנה גדולה מ-1.", pos=0)],
    stepsSource="ai-verified")

add(2, "ג",
    rubric=rub((r"פיצול ל-$S_1=\sum\binom nk6^k$ ול-$S_2=5^n\sum\binom nk$", 1),
               (r"משפט הבינום: $S_1=7^n$", 1),
               (r"$S_2=5^n\cdot2^n=10^n$", 1),
               (r"חסם $7^n+10^n\le2\cdot10^n\le2\cdot11^n$", 1),
               (r"מסקנה $f(n)=O(11^n)$ עם $c_0=2$, $n_0=1$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"להתייחס ל-$5^n$ כאילו תלוי ב-$k$ ולכתוב $\sum\binom nk5^k$.",
              r"לכתוב $\sum\binom nk=2^{n}$ כ-$2^{n-1}$."],
    steps=[ch("איזה כלי משתמש בו הפתרון לחישוב הסכומים?", r"משפט הבינום $(x+1)^n=\sum\binom nkx^k$ עם $x=6$ ועם $x=1$",
              [r"זהות פסקל", r"נוסחת הכלה והפרדה", r"אינדוקציה על $n$"],
              r"$\sum\binom nk6^k=7^n$ ו-$\sum\binom nk=2^n$.", pos=2),
           nm(r"מהו $f(3)=\sum_{k=0}^{3}\binom3k\left(2^k3^k+5^3\right)$?", 1343, r"$7^3+10^3=343+1000=1343$ (נבדק בחישוב ישיר)."),
           nm(r"מהו המספר השלם הקטן ביותר $c$ המקיים $f(n)\le c\cdot11^n$ לכל $n\ge1$?", 2,
              r"$f(n)/11^n=(7/11)^n+(10/11)^n$ יורד ב-$n$, ובמקסימום $n=1$ שווה $17/11<2$, ו-$17/11>1$.")],
    stepsSource="ai-verified")

add(3, "א",
    rubric=rub((r"סעיף (1): קביעה שהטענה אינה נכונה", 1),
               (r"סעיף (1): $\varnothing(1)=\varnothing(2)=1$ עם $1\ne2$", 1),
               (r"סעיף (2): $n=2$ נפסל ($\varnothing(2)=1$) ו-$n=3$ מתאים", 2),
               (r"סעיף (2): עבור ראשוני $n\ge5$, $\varnothing(n)=n-1$ זוגי וגדול מ-2", 1),
               (r"סעיף (2): $n$ פריק אינו מתאים, ולכן $n=3$ יחיד", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"להתעלם מהמקרה $n=1$ ($1$ אינו ראשוני).",
              r"לטעון ש-$\varnothing(p)$ ראשוני לכל ראשוני $p$ בלי לבדוק את הזוגיות של $p-1$."],
    steps=[ch(r"האם פונקציית אוילר $\varnothing$ חד-חד-ערכית?", "לא", ["כן"], r"$\varnothing(1)=\varnothing(2)=1$.", pos=0),
           nm(r"מהו $\varnothing(2)$ (פונקציית אוילר)?", 1, r"רק $1$ זר ל-$2$ בין $1,2$."),
           nm(r"מהו המספר היחיד $n\ge1$ שבו $n$ ו-$\varnothing(n)$ שניהם ראשוניים?", 3, r"$\varnothing(3)=2$. (נבדק לכל $n<3000$.)"),
           ch(r"איך הפתרון פוסל ראשוני $n\ge5$?", r"$\varnothing(n)=n-1$ זוגי וגדול מ-2, ולכן אינו ראשוני",
              [r"$\varnothing(n)=n-1$ אי-זוגי וגדול מ-2", r"$\varnothing(n)=n+1$ ולכן גדול מדי", r"$\varnothing(n)=1$"],
              r"ל-$n\ge5$ ראשוני, $n$ אי-זוגי ולכן $n-1$ זוגי (נבדק לכל ראשוני עד $3000$).", pos=0)],
    stepsSource="ai-verified")

add(3, "ב",
    rubric=rub((r"רפלקסיביות מכריחה $(1,1),(2,2)\in R$", 1),
               (r"אי-סימטריה מכריחה בדיוק אחד מ-$(1,2)$ או $(2,1)$, ולכן שתי אפשרויות", 1),
               (r"בדיקה ש-$R_1,R_2$ רפלקסיביים, אנטי-סימטריים וטרנזיטיביים", 2),
               (r"קשירות (סדר מלא): $(x,y)\in R$ או $(y,x)\in R$ לכל $x,y$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח ש-$R$ שאינו סימטרי חייב להכיל בדיוק אחד משני הזוגות $(1,2)$, $(2,1)$.",
              r"לבדוק סדר חלקי בלבד ולשכוח את הקשירות של סדר מלא."],
    steps=[ch(r"אילו זוגות חייב להכיל כל יחס רפלקסיבי $R$ על $\{1,2\}$?", r"$(1,1)$ ו-$(2,2)$",
              [r"$(1,2)$ ו-$(2,1)$", r"$(1,1)$ ו-$(1,2)$", r"$(2,1)$ ו-$(2,2)$"],
              r"רפלקסיביות פירושה $(x,x)\in R$ לכל $x\in A$.", pos=0),
           nm(r"כמה יחסים על $A=\{1,2\}$ הם רפלקסיביים ואינם סימטריים?", 2, r"$R_1=\{(1,1),(2,2),(1,2)\}$ ו-$R_2=\{(1,1),(2,2),(2,1)\}$ (נבדק בספירת כל 16 היחסים)."),
           ch(r"האם הטענה “כל יחס רפלקסיבי ולא סימטרי על $\{1,2\}$ הוא יחס סדר מלא” נכונה?", "נכונה", ["לא נכונה"],
              r"שני היחסים רפלקסיביים, אנטי-סימטריים, טרנזיטיביים וקשירים (נבדק בבדיקה ישירה).", pos=1)],
    stepsSource="ai-verified")

add(3, "ג",
    rubric=rub((r"רפלקסיביות: $x^2+x=x(x+1)$ זוגי", 3),
               (r"סימטריה: שימוש ב-$(x^2+y)+(y^2+x)=(x^2+x)+(y^2+y)$", 3),
               (r"טרנזיטיביות: $(x^2+y)+(y^2+z)=(y^2+y)+(x^2+z)$", 3),
               (r"מחלקות השקילות $[0]$, $[1]$ ו-$\mathbb{Z}/R=\{[0],[1]\}$", 3),
               (r"$R$ אינו יחס סדר חלקי: אינו אנטי-סימטרי, כי $(2,4),(4,2)\in R$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להסיק ש-$x^2+y$ זוגי רק כש-$x$ זוגי.",
              r"להכריז ש-$R$ יחס סדר חלקי רק כי הוא רפלקסיבי וטרנזיטיבי.",
              r"לשכוח שכל מספר שלם שייך בדיוק למחלקה אחת, ולכן יש שתי מחלקות בלבד."],
    steps=[ch(r"מתי $xRy$, כלומר מתי $x^2+y$ זוגי?", r"כאשר $x$ ו-$y$ בעלי אותה זוגיות",
              [r"כאשר $x$ זוגי", r"כאשר $y$ זוגי", r"כאשר $xy$ זוגי"],
              r"$x^2\equiv x\pmod2$, ולכן $x^2+y\equiv x+y$. ב-$x=y=1$ מתקיים $xRy$ אף ש-$x$ אי-זוגי, ו-$xy=1$ אי-זוגי (נבדק על $-40\le x,y\le40$).", pos=0),
           nm(r"כמה מחלקות שקילות יש ב-$\mathbb{Z}/R$?", 2, r"$\mathbb{Z}/R=\{[0],[1]\}$."),
           ch(r"איזו מתכונות יחס הסדר החלקי נכשלת ב-$R$?", "אנטי-סימטריה", ["רפלקסיביות", "טרנזיטיביות", "סימטריה"],
              r"$(2,4),(4,2)\in R$ ו-$2\ne4$. שאר התכונות מתקיימות.", pos=0),
           {"type": "findbug", "prompt": r"בהוכחת הסימטריה שורה אחת שונתה. איזו?",
            "lines": [r"נניח $x^2+y=2k$ ונוכיח ש-$y^2+x$ זוגי.",
                      r"$(x^2+y)+(y^2+x)=(x^2+x)+(y^2+y)$.",
                      r"$x^2+x=x(x+1)$ ו-$y^2+y=y(y+1)$ זוגיים כי $x$ ו-$y$ זוגיים.",
                      r"לכן הסכום זוגי, ומכיוון ש-$2k$ זוגי גם $y^2+x$ זוגי."],
            "bugIndex": 2,
            "explain": r"בשורה השלישית (אינדקס 2): $x$ ו-$y$ אינם בהכרח זוגיים. הנימוק הנכון הוא שמכפלה של שני מספרים עוקבים תמיד זוגית."}],
    stepsSource="ai-verified")

add(4, "א",
    rubric=rub((r"$m=2^{99}$ (חצי מהתת-קבוצות הן בגודל אי-זוגי)", 2),
               (r"$\sum_{B}|B|=\sum_k k\binom{100}{k}$", 1),
               (r"גזירת $(x+1)^{100}$ והצבת $x=1$: $100\cdot2^{99}$", 2),
               (r"הסכום הסופי $101\cdot2^{99}$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לספור את $\varnothing$ כתת-קבוצה בגודל אי-זוגי.",
              r"לשכוח את הגורם $k$ בסכום או לחשב $\sum\binom{100}{k}=2^{100}$ במקום $\sum k\binom{100}{k}$."],
    steps=[nm(r"כמה תת-קבוצות בגודל אי-זוגי יש לקבוצה בת 4 איברים? (זו הדוגמה הקטנה של $m=2^{n-1}$.)", 8, r"$\binom41+\binom43=4+4=8=2^3$."),
           nm(r"מהו $\sum_{B\in P(A)}|B|$ עבור $|A|=4$?", 32, r"$\sum k\binom4k=4\cdot2^3=32$."),
           nm(r"עבור $|A|=100$: מהו היחס $\dfrac{\sum_{B\in P(A)}|B|}{m}$?", 100, r"$100\cdot2^{99}/2^{99}=100$ (נבדק במספרים שלמים מדויקים), ולכן הסכום הוא $(1+100)\cdot2^{99}=101\cdot2^{99}$."),
           ch("באיזה כלי משתמש הפתרון כדי לחשב את $\\sum k\\binom{100}k$?", r"גזירת $(x+1)^{100}=\sum\binom{100}kx^k$ והצבת $x=1$",
              ["זהות פסקל", "אינדוקציה על 100", "הכלה והפרדה"], r"הנגזרת היא $100(x+1)^{99}=\sum k\binom{100}kx^{k-1}$.", pos=0)],
    stepsSource="ai-verified")

add(4, "ב",
    rubric=rub((r"$f$ הפיכה $\iff$ $f$ תמורה", 2),
               (r"$f(\{1,2,3\})=\{1,2,3\}$ נותן $3!=6$ אפשרויות", 2),
               (r"$f(\{4,5,6,7\})=\{4,5,6,7\}$ נותן $4!=24$ אפשרויות", 1),
               (r"כפל: $3!\cdot4!=144$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לספור $7!$ ולהתעלם מהתנאי $f(\{1,2,3\})=\{1,2,3\}$.",
              r"לחשב $3!+4!$ במקום $3!\cdot4!$."],
    steps=[ch(r"מדוע מתקיים גם $f(\{4,5,6,7\})=\{4,5,6,7\}$?", r"$f$ תמורה, ולכן אם $\{1,2,3\}$ מועתקת על עצמה, שאר האיברים מועתקים על שאר האיברים",
              [r"כי $f$ היא פונקציית הזהות על $\{4,5,6,7\}$", r"כי $f(4)=4$ בהכרח", r"כי $4<7$"],
              r"פונקציית הזהות מניבה רק פונקציה אחת, אך יש $4!=24$ אפשרויות (נבדק בספירה ישירה של 144 הפונקציות).", pos=0),
           nm(r"כמה תמורות של $\{1,2,3\}$ יש?", 6, r"$3!=6$."),
           nm(r"כמה תמורות של $\{4,5,6,7\}$ יש?", 24, r"$4!=24$."),
           nm(r"כמה פונקציות הפיכות $f$ עם $f(\{1,2,3\})=\{1,2,3\}$ יש ב-$\Omega$?", 144, r"$6\cdot24=144$ (נבדק בספירה ישירה על 5040 התמורות).")],
    stepsSource="ai-verified")

add(4, "ג",
    rubric=rub((r"תרגום התנאים: $x_1\ge5$, $x_2\ge3$, $x_3\ge7$ עם $x_1+x_2+x_3=18$", 2),
               (r"הצבה $y_i=x_i-m_i$ (כאשר $m_i$ הוא המינימום של האות) וקבלת $y_1+y_2+y_3=3$", 2),
               (r"מספר הפתרונות $\binom52=10$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לפרש “יותר מ-4” כ-$x_1\ge4$ ולא כ-$x_1\ge5$.",
              r"לספור מילים עם חשיבות לסדר (סידורים) למרות שנאמר שאין חשיבות לסדר האותיות."],
    steps=[nm(r"מהו מספר המופעים המינימלי של האות $a$, כשהיא מופיעה “יותר מ-4 פעמים”?", 5, r"$x_1>4\Rightarrow x_1\ge5$."),
           nm(r"אחרי החסרת המינימום ($5$, $3$, $7$) מ-$x_1+x_2+x_3=18$, מהו הסכום $y_1+y_2+y_3$?", 3, r"$18-5-3-7=3$."),
           nm(r"כמה מילים (ללא חשיבות לסדר האותיות, כלומר כמה שלשות $(x_1,x_2,x_3)$) מקיימות את התנאים?", 10,
              r"$\binom{3+2}{2}=10$ (נבדק בספירה ישירה).")],
    stepsSource="ai-verified")

add(4, "ד",
    rubric=rub((r"שימוש במשפט פרמה הקטן לקבלת $11\mid70^{10}-1$ ו-$n=11$", 2),
               (r"$n^2+n=132=2^2\cdot3\cdot11$", 1),
               (r"$\varnothing(132)=40$", 1),
               (r"$\varnothing(40)=16$", 2),
               (r"מסקנה: $8\mid16$, התשובה כן", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב $\gcd(11,70^{10}-1)=1$ בלי לבדוק את התנאי של משפט פרמה.",
              r"לפרק את $132$ כך ש-$4$ נחשב כגורם ראשוני ולחשב $\varnothing(4)=3$ בטעות."],
    steps=[ch("באיזה משפט משתמש הפתרון כדי לחשב את $\\gcd(11,70^{10}-1)$?", r"משפט פרמה הקטן",
              ["משפט וילסון", "משפט השאריות הסיני", "זהות בזו"],
              r"$11$ ראשוני ו-$11\nmid70$, ולכן $70^{10}\equiv1\pmod{11}$.", pos=0),
           nm(r"מהו $n=\gcd(11,70^{10}-1)$?", 11, r"$11\mid70^{10}-1$, ולכן ה-gcd הוא $11$ (נבדק בחישוב ישיר)."),
           nm(r"מהו $\varnothing(n+n^2)$ (פונקציית אוילר) עבור $n=11$?", 40, r"$132=2^2\cdot3\cdot11$ ו-$\varnothing(132)=2\cdot2\cdot10=40$."),
           nm(r"מהו $(\varnothing\circ\varnothing)(132)$?", 16, r"$\varnothing(40)=\varnothing(2^3)\varnothing(5)=4\cdot4=16$."),
           ch(r"האם $8\mid(\varnothing\circ\varnothing)(n+n^2)$?", "כן", ["לא"], r"$8\mid16$.", pos=0)],
    stepsSource="ai-verified")


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
