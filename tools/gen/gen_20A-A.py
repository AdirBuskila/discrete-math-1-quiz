# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json -- discrete math 1 (20066), semester B 5780 (folder: sem A), moed A (02.07.2020).
ONE sitting split over three files: "part 1 + solution" (Q1-Q3), "part 2 + solution" (Q4-Q6) and an exam-only file.
The printed question text is taken from the two solution files (typed text with the handwritten key). The exam-only
file prints DIFFERENT numbers in Q1a, Q1e, Q3c, Q4b, Q5a-b, Q6a-c, so it is a different version and was not used.
The key is handwritten (author unknown) = student-solution. Q1 is the mandatory concept question: five parts,
each asks to define a term and answer a short question (5 points each, not printed per part).
Checks: tools/verify/20A-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_20A-A.py
 - Q2a, Q2b, Q2c, Q4b, Q5c, Q6a are ONE item each (sub-parts 1/2/3 inside)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve(⋆⋆).parents[1] / "raw" / "20A-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


def H(num, part, kind, topic, points, question, reason, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "hold": reason}
    q.update(kw)
    return q


HDR = "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"
questions = []
add = questions.append

# ---------------- Q1 (mandatory, 25) ----------------
add(Q(1, "א", "computation", "combinatorics", 5,
      HDR + "**המונח:** תמורה של קבוצה.\n"
      r"**שאלה:** כמה תמורות של הקבוצה $\{1,2,3,4,5\}$ מתחילות ב-1 או ב-2 ?",
      r"הגדרה: תהי $A$ קבוצה בת $n\ge1$ איברים. כל סדרה בלי חזרות של כל איברי $A$ נקראת תמורה של $A$."
      "\n"
      r"או: כל פונקציה חד-חד-ערכית ועל מ-$A$ ל-$A$ נקראת תמורה של $A$."
      "\n"
      r"מספר התמורות המתחילות ב-1 הוא $4!$ (שאר ארבעת האיברים מסודרים בכל סדר), וכך גם מספר התמורות המתחילות ב-2. "
      r"אין תמורה שמתחילה בשניהם, ולכן: $4!\cdot2=48$."))

add(Q(1, "ב", "computation", "modular_fermat_wilson", 5,
      "**המונח:** פונקציית EULER.\n"
      r"**שאלה:** חשבו את $\phi(5!)$.",
      r"הגדרה: הפונקציה $\phi:\mathbb{N}^+\to\mathbb{N}^+$ המוגדרת לפי הכלל "
      r"$\phi(n)=\left|\{m:\ 1\le m\le n\ \wedge\ \gcd(n,m)=1\}\right|$ נקראת פונקציית EULER."
      "\n"
      r"$$\phi(5!)=\phi(120)=\phi(2^3\cdot3\cdot5)=120\cdot\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac15\right)"
      r"=120\cdot\frac12\cdot\frac23\cdot\frac45=32$$"))

add(Q(1, "ג", "computation", "graphs_intro", 5,
      "**המונח:** גרף דו-צדדי שלם.\n"
      r"**שאלה:** חשבו את מספר הצלעות של המשלים של $K_{m,n}=(A,B,E)$.",
      r"הגדרה: הגרף $G=K_{m,n}=(A,B,E)$ הוא גרף דו-צדדי שלם כאשר $A=\{a_1,\ldots,a_m\}$, $B=\{b_1,\ldots,b_n\}$ ו-"
      r"$E=\{(a_i,b_j):\ i=1,\ldots,m;\ j=1,2,\ldots,n\}$."
      "\n"
      r"**פתרון 1:** $\overline{K_{m,n}}=K_m\cup K_n$, ולכן $|\overline E|=\frac{m(m-1)}{2}+\frac{n(n-1)}{2}$."
      "\n"
      r"**פתרון 2:** $|\overline E|=\frac{|V|(|V|-1)}{2}-|E|=\frac{(m+n)(m+n-1)}{2}-m\cdot n$."))

add(Q(1, "ד", "computation", "graphs_intro", 5,
      "**המונח:** גרף לא מכוון קשיר.\n"
      r"**שאלה:** מצאו $2\le n$ עבורו המשלים של $P_n$ הוא קשיר וגם גרף דו-צדדי.",
      r"הגדרה: גרף לא מכוון $G=(V,E)$ הוא קשיר אם לכל זוג צמתים $x,y\in V$ קיים ב-$G$ מסלול מ-$x$ ל-$y$."
      "\n"
      r"$\overline{P_2}$ אינו קשיר, ו-$\overline{P_3}$ אינו קשיר."
      "\n"
      r"$P_4$ הוא המסלול $a-b-c-d$, ולכן $\overline{P_4}$ הוא המסלול $b-d-a-c$ (הצלעות $bd$, $da$, $ac$), שהוא קשיר ודו-צדדי."
      "\n"
      r"מסקנה: עבור $n=4$ בלבד המשלים של $P_n$ הוא קשיר וגם דו-צדדי."))

add(Q(1, "ה", "truefalse", "cardinality_sets", 5,
      "**המונח:** קבוצות שוות עוצמה.\n"
      r"**שאלה:** האם הקבוצות $\mathbb{Q}$ ו-$A=\{x:\ x\in\mathbb{Z},\ x<-5\}$ שוות עוצמה ?",
      r"הגדרה: הקבוצות $A,B$ נקראות קבוצות שוות עוצמה אם קיימת פונקציה $f:A\to B$ על וגם חד-חד-ערכית."
      "\n"
      r"$A\subseteq\mathbb{Z}\Rightarrow|A|\le|\mathbb{Z}|$."
      "\n"
      r"$A$ אינסופית $\Rightarrow$ קיימת $B\subseteq A$ כך ש: $|B|=|\mathbb{N}|$."
      "\n"
      r"לכן: $|\mathbb{N}|\le|A|\le|\mathbb{Z}|=|\mathbb{N}|=|\mathbb{Q}|\Rightarrow|A|=|\mathbb{Q}|$. כלומר הקבוצות שוות עוצמה.",
      verdict=True))

# ---------------- Q2 (25) ----------------
add(H(2, "א", "computation", "combinatorics", 10,
      r"מהו מספר התמורות של הקבוצה $\{1,2,\ldots,7\}$ שבהן:"
      "\n"
      r"(1) המספרים $1,2,3$ נמצאים בסמיכות ?"
      "\n"
      r"(2) המספר $1$ נמצא לפני $2$ ?",
      "key-disagrees: (1) the key gives 720 = 3!*5!, correct; (2) the key writes C(7,2)*5! = 7!/2 = 2560, but this equals 2520 (script-checked)"))

add(H(2, "ב", "computation", "combinatorics", 8,
      r"תהיינה הקבוצות $A=\{a,b,c,d\}$ וגם $B=\{x,y,z\}$."
      "\n"
      r"(1) כמה סדרות שונות בנות 7 אותיות אפשר ליצור כך שכל סדרה מתחילה ב-4 אותיות מ-$A$ ושאר האותיות מ-$B$ ?"
      "\n"
      r"(2) כמה סדרות מ-(1) מקיימות את התנאים הבאים: כל אות מופיעה פעם אחת בסדרה וכל סדרה מתחילה ב-$a$ או ב-$b$ ?",
      "key-disagrees: the key answers (1) with 144 = 3!*4! (each letter once), but part (2) says 'every letter appears once' as an extra condition, so (1) allows repeated letters (4^4*3^3 = 6912); (2) = 72 = 2*3!*3! matches"))

add(H(2, "ג", "proof", "modular_fermat_wilson", 7,
      r"(1) (2 נק.) האם פונקציית Euler $\phi$ היא חד-חד-ערכית ?"
      "\n"
      r"(2) (5 נק.) אם $n\in\mathbb{N}$ וגם $15\mid n$, הראו ש: $8\mid\phi(n)$.",
      "key-flawed: (1) fine (phi(1)=1=phi(2)); in (2) the key writes phi(n) = 3^a*5^b*m*(1-1/3)(1-1/5)*phi(m), a formula with extra factors m and phi(m) that is not valid; the final line 2*4*3^(a-1)*5^(b-1)*phi(m) is right"))

# ---------------- Q3 (25) ----------------
add(Q(3, "א", "computation", "combinatorics", 10,
      r"כמה מספרים מהקבוצה $\Omega=\{1,2,3,\ldots,100\}$ אינם מתחלקים ב-3 או ב-5 או ב-7 ?",
      r"נסמן: $A_1=\{n\in\Omega:\ 3\mid n\}$, $A_2=\{n\in\Omega:\ 5\mid n\}$, $A_3=\{n\in\Omega:\ 7\mid n\}$."
      "\n"
      r"$|A_1|=\lfloor\frac{100}{3}\rfloor=33$, $|A_2|=\lfloor\frac{100}{5}\rfloor=20$, $|A_3|=\lfloor\frac{100}{7}\rfloor=14$."
      "\n"
      r"$|\Omega-A_1\cup A_2\cup A_3|=|\Omega|-|A_1\cup A_2\cup A_3|=100-S_1+S_2-S_3$ (עקרון ההכלה וההפרדה), כאשר:"
      "\n"
      r"$S_1=|A_1|+|A_2|+|A_3|=67$"
      "\n"
      r"$S_2=|A_1\cap A_2|+|A_1\cap A_3|+|A_2\cap A_3|=\lfloor\frac{100}{15}\rfloor+\lfloor\frac{100}{21}\rfloor+\lfloor\frac{100}{35}\rfloor=6+4+2=12$"
      "\n"
      r"$S_3=|A_1\cap A_2\cap A_3|=\lfloor\frac{100}{3\cdot5\cdot7}\rfloor=\lfloor\frac{100}{105}\rfloor=0$"
      "\n"
      r"מסקנה: $|\Omega-A_1\cup A_2\cup A_3|=100-67+12-0=45$."))

add(Q(3, "ב", "computation", "recurrence_sums", 10,
      r"מצאו את הצורה המפורשת של $a_n$, כאשר $a_0=14,\ a_1=27$ וגם $a_n+a_{n-2}=15\cdot2^n,\ n\ge2$.",
      r"המשוואה האופיינית: $x^2+1=0\Rightarrow x_{1,2}=\pm i\Rightarrow x_{1,2}=\cos\frac\pi2\pm i\sin\frac\pi2$."
      "\n"
      r"הפתרון הכללי של $a_n+a_{n-2}=0$ הוא: $a_n^{(h)}=C_1\cos\frac{n\pi}{2}+C_2\sin\frac{n\pi}{2}$."
      "\n"
      r"פתרון פרטי של $a_n+a_{n-2}=15\cdot2^n$ (\*\*) הוא מהצורה $a_n^{(p)}=A\cdot2^n$. נציב ב-(\*\*): "
      r"$A\cdot2^n+A\cdot2^{n-2}=15\cdot2^n\ \ |:2^{n-2}\Rightarrow4A+A=15\cdot4\Rightarrow A=12\Rightarrow a_n^{(p)}=12\cdot2^n$."
      "\n"
      r"הפתרון הרקורסיבי הוא: $a_n=C_1\cos\frac{n\pi}{2}+C_2\sin\frac{n\pi}{2}+12\cdot2^n$."
      "\n"
      r"$a_0=C_1+12=14\Rightarrow C_1=2$"
      "\n"
      r"$a_1=C_2+24=27\Rightarrow C_2=3$"
      "\n"
      r"$$a_n=2\cos\frac{n\pi}{2}+3\sin\frac{n\pi}{2}+12\cdot2^n,\quad n\in\mathbb{N}$$"))

add(Q(3, "ג", "proof", "graphs_intro", 5,
      r"הראו שהמשלים של $P_{15}$ הוא גרף בעל מסלול Euler.",
      r"צריך להראות ש-$\overline{P_{15}}$ קשיר ובעל בדיוק 2 צמתים מדרגה אי-זוגית."
      "\n"
      r"$P_{15}$: המסלול $v_1,v_2,\ldots,v_{15}$. $\deg_{P_{15}}(v_1)=1=\deg_{P_{15}}(v_{15})\Rightarrow\deg_{\overline{P_{15}}}(v_1)=\deg_{\overline{P_{15}}}(v_{15})=13$."
      "\n"
      r"לכל $i=2,\ldots,14$: $\deg_{P_{15}}(v_i)=2\Rightarrow\deg_{\overline{P_{15}}}(v_i)=12$."
      "\n"
      r"לכל $v$ מתקיים $\deg_{\overline{P_{15}}}(v)\ge\frac{15}{2}$, ולכן לפי משפט DIRAC הגרף $\overline{P_{15}}$ הוא גרף Hamilton, ובפרט קשיר."
      "\n"
      r"$\overline{P_{15}}$ קשיר, ויש בו בדיוק 2 צמתים מדרגה אי-זוגית. מסקנה: ב-$\overline{P_{15}}$ קיים מסלול EULER."))

# ---------------- Q4 (25) ----------------
add(Q(4, "א", "computation", "combinatorics", 8,
      r"תהי $A=\{1,2,3,\ldots,n\}$, כאשר $n>2$. אם לקבוצה $A$ יש 55 תתי-קבוצות בגודל 2, "
      r"חשבו כמה תתי-קבוצות **בגודל זוגי** יש לקבוצה $A$.",
      r"נתון: $\frac{n(n-1)}{2}=55\iff\binom n2=55$."
      "\n"
      r"$n^2-n-110=0\Rightarrow n_{1,2}=\frac{1\pm\sqrt{441}}{2}=\frac{1\pm21}{2}\Rightarrow n=11$, כלומר $|A|=11$."
      "\n"
      r"מספר תתי-הקבוצות בגודל זוגי: $1024=2^{10}=2^{11-1}$."))

add(Q(4, "ב", "computation", "combinatorics", 12,
      r"תהי $\Omega$ קבוצת הפונקציות $f:\{1,2,3,4\}\to\{1,2,3,4,5,6\}$."
      "\n"
      r"(1) (6 נק.) כמה פונקציות מ-$\Omega$ הן עולות ממש ?"
      "\n"
      r"(2) (6 נק.) כמה פונקציות מ-$\Omega$ הן חד-חד-ערכיות ?",
      r"(1) $f$ עולה ממש $\iff\{f(1),f(2),f(3),f(4)\}$ היא קבוצה בת 4 איברים (הסדר נקבע בצורה יחידה). "
      r"בוחרים 4 איברים מתוך $\{1,2,\ldots,6\}$, ולכן יש $\binom64=15$ פונקציות עולות ממש."
      "\n"
      r"(2) $f$ חד-חד-ערכית $\iff f(1),f(2),f(3),f(4)$ הם 4 איברים שונים מתוך $\{1,2,\ldots,6\}$ בסדר כלשהו, "
      r"ולכן יש $P(6,4)=360$ פונקציות חד-חד-ערכיות."))

add(Q(4, "ג", "computation", "combinatorics", 5,
      r"תהי $A=\{1,2,3,\ldots,n\}$, כאשר $n>2$. חשבו את המספר $m=\sum_{B\in P(A)}|B|$.",
      r"$m=\sum_{k=0}^{n}k\cdot\binom nk$."
      "\n"
      r"נגזור את $(x+1)^n=\sum_{k=0}^{n}\binom nk x^k$ ונקבל: $n(x+1)^{n-1}=\sum_{k=0}^{n}\binom nk\cdot k\cdot x^{k-1}$."
      "\n"
      r"נציב $x=1$: $n\cdot2^{n-1}=\sum_{k=0}^{n}\binom nk\cdot k$."
      "\n"
      r"מסקנה: $m=n\cdot2^{n-1}$."))

# ---------------- Q5 (25) ----------------
add(Q(5, "א", "truefalse", "graphs_intro", 6,
      r"האם קיים גרף לא מכוון שסדרת הדרגות שלו היא $(1,1,2,3,3,3,6,7,8)$ ?",
      r"נניח בשלילה שקיים גרף לא מכוון $G=(V,E)$ כזה, $V=\{v_i:\ 1\le i\le9\}$, כך ש-$\deg(v_8)=7$ ו-$\deg(v_9)=8$."
      "\n"
      r"אז בגרף $G-v_9$ סדרת הדרגות היא $(0,0,1,2,2,2,5,6)$, וזה אי-אפשר: ל-$v$ מדרגה 6 יש 6 שכנים בין 7 הצמתים האחרים, "
      r"אבל שני צמתים הם מדרגה 0."
      "\n"
      r"מסקנה: לא קיים גרף $G$ שסדרת הדרגות שלו היא $(1,1,\ldots,8)$.",
      verdict=False))

add(Q(5, "ב", "computation", "combinatorics", 10,
      r"תהי הקבוצה $A=\{a,b,c,d\}$. כמה מלים בנות 22 אותיות, בלי חשיבות לסדר, ניתן ליצור מ-$A$ כך שבכל מילה:"
      "\n"
      r"האות $a$ מופיעה לפחות 3 פעמים, האות $b$ מופיעה לפחות פעם אחת,"
      "\n"
      r"האות $c$ מופיעה לפחות 4 פעמים, האות $d$ מופיעה לפחות פעמיים.",
      r"נסמן: $x_1$ מספר ההופעות של $a$ ($3\le x_1$), $x_2$ של $b$ ($1\le x_2$), $x_3$ של $c$ ($4\le x_3$), $x_4$ של $d$ ($2\le x_4$)."
      "\n"
      r"אז $x_1+x_2+x_3+x_4=22$. לכן מספר המילים שווה למספר הפתרונות של: $x_1+x_2+x_3+x_4=22,\ x_1\ge3,\ x_2\ge1,\ x_3\ge4,\ x_4\ge2$."
      "\n"
      r"והוא שווה ל: $D(4,22-3-1-4-2)=D(4,12)=\binom{4-1+12}{4-1}=\binom{15}{3}=\frac{15\cdot14\cdot13}{1\cdot2\cdot3}=455$."))

add(Q(5, "ג", "proof", "graphs_intro", 9,
      r"יהי $G=(V,E)$ גרף לא מכוון שבציור."
      "\n"
      r"(1) האם המשלים של $G$ הוא גרף Hamilton ?"
      "\n"
      r"(2) האם המשלים של $G$ הוא גרף Euler ?"
      "\n"
      r"(3) האם המשלים של $G$ הוא דו-צדדי ?",
      r"$n=|V|=10$. נסמן ב-$\overline G$ את המשלים של $G$."
      "\n"
      r"(1) לכל $v\in V$: $\deg_{\overline G}(v)=6\ge\frac{10}{2}$, ולכן לפי DIRAC הגרף $\overline G$ הוא גרף Hamilton."
      "\n"
      r"(2) $\overline G$ הוא קשיר (כי הוא גרף Hamilton) ולכל $v\in V$ מתקיים $\deg_{\overline G}(v)=6$, כלומר זוגי, ולכן $\overline G$ הוא גרף Euler."
      "\n"
      r"(3) $\overline G$ אינו דו-צדדי, כי יש בו מעגל באורך אי-זוגי: המעגל $C_3$ על הצמתים $a,d,g$.",
      contextId="c1"))

# ---------------- Q6 (25) ----------------
add(Q(6, "א", "computation", "modular_fermat_wilson", 12,
      r"יהי $4<n\in\mathbb{N}$. חשבו את $\phi(a\cdot b)$, כאשר "
      r"$a=\sum_{k=0}^{n}\binom nk\cdot3^k\cdot5^{n-k}$ וגם $b=\sum_{k=0}^{n}\binom nk\cdot7^k\cdot5^{n-k}$.",
      r"לפי הבינום של Newton: $a=(3+5)^n=8^n$, $b=(7+5)^n=12^n$."
      "\n"
      r"$$\phi(ab)=\phi(8^n\cdot12^n)=\phi(2^{3n}\cdot2^{2n}\cdot3^n)=\phi(2^{5n}\cdot3^n)"
      r"=2^{5n}\cdot3^n\cdot\left(1-\frac12\right)\left(1-\frac13\right)=2^{5n}\cdot3^n\cdot\frac12\cdot\frac23=2^{5n}\cdot3^{n-1}$$"))

add(Q(6, "ב", "proof", "cardinality_sets", 7,
      r"הראו שהקבוצות $(2,7]$ ו-$(0,1)$ שוות עוצמות.",
      r"הפונקציה $f:(0,1)\to(2,7]$, $f(x)=x+2$ היא חד-חד-ערכית, ולכן $|(0,1)|\le|(2,7]|$."
      "\n"
      r"בנוסף, $(2,7]\subseteq\mathbb{R}$, ולכן $|(2,7]|\le|\mathbb{R}|=|(0,1)|$."
      "\n"
      r"מסקנה: $|(0,1)|=|(2,7]|$ (לפי קנטור-ברנשטיין)."))

add(Q(6, "ג", "computation", "graphs_intro", 6,
      r"מצאו את הקוטר של הגרף שבציור הבא:",
      r"מספיק לחשב את המרחק מ-$a$ ומ-$f$ לכל שאר הצמתים ולהסתכל על הגדול ביותר."
      "\n"
      r"$\operatorname{dist}(a,b)=\operatorname{dist}(a,f)=\operatorname{dist}(a,e)=1$, ו-$\operatorname{dist}(a,v)=2$ לכל $v\in\{j,g,i,h,c,d\}$."
      "\n"
      r"$\operatorname{dist}(f,a)=\operatorname{dist}(f,i)=\operatorname{dist}(f,h)=1$, ו-$\operatorname{dist}(f,v)=2$ לכל $v\in\{j,b,c,d,e,g\}$."
      "\n"
      r"מסקנה: $\operatorname{diam}(G)=2$ ($=\max\{\operatorname{dist}(x,y):\ x,y\in V\}$).",
      contextId="c1"))

exam = {
    "examCode": "20A-A",
    "examLabel": "בדידה 1 (20066), מועד א' (02.07.2020)",
    "year": 2020,
    "examDate": "02.07.2020",
    "sourceFile": "20A-A exam with solution, part 1 pp.1-9 and part 2 pp.1-7",
    "solutionFile": "20A-A handwritten solution (author unknown), part 1 pp.2-9 and part 2 pp.2-7",
    "contexts": {
        "c1": {"kind": "image", "title": "הגרף בשאלות 5ג ו-6ג",
               "image": "images/exams/20A-A-c1.png",
               "caption": "גרף לא מכוון על הצמתים a,b,c,d,e,f,g,h,i,j"},
    },
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
