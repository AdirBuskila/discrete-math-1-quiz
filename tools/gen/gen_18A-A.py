# -*- coding: utf-8 -*-
"""Generator for tools/raw/18A-A.json -- discrete math 1 (20066), semester A 5778, moed A (13.02.2018).
4 mandatory questions of 25 points (scan, read by vision). The handwritten key (author unknown) is student-solution.
Checks: tools/verify/18A-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_18A-A.py
 - Q1a (a1+a2), Q1b (b1+b2), Q2c (c1+c2), Q3a (a1-a4), Q4a, Q4b (b1-b3) are ONE item each.
 - Q4c is held: the key counts letter-count vectors (364), the question asks for words."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18A-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


def H(num, part, kind, topic, points, question, reason):
    return {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
            "question": question, "hold": reason}


questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "proof", "functions", 12,
      "**(1)** הגדירו את המושג של **פונקציה חד-חד-ערכית**.\n"
      r"**(2)** תנו 2 דוגמאות של פונקציות $g,f$ כך ש:"
      "\n"
      r"$f:A_1\to B_1$ היא חד-חד-ערכית על **אך לא** על, כאשר $|A_1|=3\ne|B_1|$;"
      "\n"
      r"ו-$g:A_2\to B_2$ היא על **אך לא** חד-חד-ערכית, כאשר $|A_2|=3\ne|B_2|$.",
      r"**(1) הגדרה:** תהי $f:A\to B$ פונקציה. $f$ נקראת חד-חד-ערכית אם מקיימת את התנאי: "
      r"לכל $a_1,a_2\in A$, אם $a_1\ne a_2$ אז $f(a_1)\ne f(a_2)$. "
      r"או, באופן שקול: לכל $a_1,a_2\in A$, אם $f(a_1)=f(a_2)$ אז $a_1=a_2$."
      "\n"
      r"**(2) דוגמאות:**"
      "\n"
      r"$A_1=\{a_1,a_2,a_3\}$, $B_1=\{b_1,b_2,b_3,b_4\}$, ו-$f:A_1\to B_1$ מוגדרת על ידי $f(a_i)=b_i$ לכל $i=1,2,3$. "
      r"$|A_1|=3\ne4=|B_1|$. $f$ אינה על כי ל-$b_4$ אין מקור. $f$ חד-חד-ערכית לפי ההגדרה, כי הערכים $b_1,b_2,b_3$ שונים זה מזה."
      "\n"
      r"$A_2=\{a_1,a_2,a_3\}$, $B_2=\{b_1,b_2\}$, ו-$g:A_2\to B_2$ מוגדרת על ידי $g(a_1)=b_1$ ו-$g(a_2)=g(a_3)=b_2$. "
      r"$|A_2|=3\ne2=|B_2|$. $g$ אינה חד-חד-ערכית כי $a_2\ne a_3$ אך $g(a_2)=g(a_3)=b_2$. "
      r"$g$ על כי לכל איבר ב-$B_2$ יש מקור, כלומר $g(A_2)=B_2$."),

    Q(1, "ב", "proof", "cardinality_sets", 9,
      "הוכיחו או הפריכו:\n"
      r"**(1)** $|\mathbb{Q}-\mathbb{N}|=|\mathbb{Z}|$, כאשר $\mathbb{N}$ היא קבוצת המספרים הטבעיים, "
      r"$\mathbb{Z}$ היא קבוצת המספרים השלמים ו-$\mathbb{Q}$ היא קבוצת המספרים הרציונליים."
      "\n"
      r"**(2)** $P(A)\cup P(B)=P(A\cup B)$ מתקיים לכל 2 קבוצות $A,B$.",
      r"**(1)** הטענה נכונה, כי:"
      "\n"
      r"$\{\ldots,-4,-3,-2,-1\}\subseteq\mathbb{Q}-\mathbb{N}\subseteq\mathbb{Q}$, ולכן "
      r"$|\mathbb{N}|=|\{\ldots,-4,-3,-2,-1\}|\le|\mathbb{Q}-\mathbb{N}|\le|\mathbb{Q}|=|\mathbb{N}|$."
      "\n"
      r"לכן $|\mathbb{Q}-\mathbb{N}|=|\mathbb{N}|$. מכיוון ש-$|\mathbb{N}|=|\mathbb{Z}|$ נקבל $|\mathbb{Q}-\mathbb{N}|=|\mathbb{Z}|$."
      "\n"
      r"**(2)** הטענה אינה נכונה. דוגמה נגדית: $A=\{1\}$, $B=\{2\}$."
      "\n"
      r"$\{1,2\}\in P(A\cup B)$, אך $\{1,2\}\notin P(A)$ וגם $\{1,2\}\notin P(B)$, ולכן $\{1,2\}\notin P(A)\cup P(B)$."
      "\n"
      r"כלומר $P(A\cup B)\ne P(A)\cup P(B)$."),

    Q(1, "ג", "proof", "quantifiers_proofs", 4,
      "שלולו את הטענה:\n"
      "\"לכל $x\\in A$, קיים $y\\in B$ או קיים $z\\in C$, כך ש: $x=y+z$\" "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      r"השלילה: "
      "\"קיים $x\\in A$ כך שלכל $y\\in B$ ולכל $z\\in C$ מתקיים $x\\ne y+z$\"."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 10,
      r"השתמשו באינדוקציה מתמטית כדי להוכיח את נכונות הטענה הבאה: "
      r"$(2n+1)+(2n+3)+(2n+5)+\ldots+(4n-1)=3n^2$ לכל $1\le n\in\mathbb{N}$.",
      r"$P(n):\ (2n+1)+(2n+3)+\ldots+(4n-1)=3n^2$, לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ 3=3\cdot1^2$ — TRUE."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $k\ge1$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ (2k+1)+(2k+3)+\ldots+(4k-1)=3k^2$"
      "\n"
      r"$P(k+1):\ (2(k+1)+1)+(2(k+1)+3)+\ldots+(4(k+1)-1)=3(k+1)^2$"
      "\n"
      r"כלומר: $(2k+3)+(2k+5)+\ldots+(4k-1)+(4k+1)+(4k+3)=3(k+1)^2$."
      "\n"
      r"לפי $P(k)=\text{TRUE}$, הסכום $(2k+3)+\ldots+(4k-1)$ שווה ל-$3k^2-(2k+1)$, ולכן $P(k+1)$ שקול ל:"
      "\n"
      r"$$3k^2-(2k+1)+(4k+1)+(4k+3)=3(k^2+2k+1)$$"
      "\n"
      r"$$3k^2-2k-1+4k+1+4k+3=3k^2+6k+3\ \checkmark$$"
      "\n"
      r"לכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**III.** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $n\in\mathbb{N}$, $n\ge1$."),

    Q(2, "ב", "proof", "relations_properties", 5,
      r"תהי $A$ קבוצה לא ריקה. הוכיחו או הפריכו: אם $R_2,R_1\subseteq A\times A$ יחסים אנטי-סימטריים, אז גם $R_2\cup R_1$ אנטי-סימטרי.",
      r"הטענה אינה נכונה. דוגמה נגדית:"
      "\n"
      r"$A=\{1,2\}$. היחסים $R_1=\{(1,2)\}$ ו-$R_2=\{(2,1)\}$ אנטי-סימטריים."
      "\n"
      r"$R_1\cup R_2=\{(1,2),(2,1)\}$ אינו אנטי-סימטרי, כי $1\ne2$."),

    Q(2, "ג", "proof", "equivalence_relations", 10,
      r"היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ מוגדר לפי הכלל: לכל $x,y\in\mathbb{Z}$, מתקיים $xRy\iff x^2+y^2$ הוא מספר זוגי."
      "\n"
      r"**(1)** בדקו ש-$R$ הוא יחס שקילות על $\mathbb{Z}$ ומצאו את $\mathbb{Z}/R$."
      "\n"
      r"**(2)** האם $R$ הוא יחס סדר חלקי? אם כן הוכיחו, אחרת תנו דוגמא נגדית.",
      r"**(1)** $R$ רפלקסיבי: לכל $x\in\mathbb{Z}$ נכון $xRx$, כי $x^2+x^2=2x^2$ הוא מספר זוגי."
      "\n"
      r"$R$ סימטרי: לכל $x,y\in\mathbb{Z}$, אם $xRy$ אז $yRx$, כי $x^2+y^2=y^2+x^2$ הוא מספר זוגי."
      "\n"
      r"$R$ טרנזיטיבי: לכל $x,y,z\in\mathbb{Z}$, אם $xRy$ ו-$yRz$ אז $xRz$. "
      r"אכן, $xRy\iff x^2+y^2=2k_1$ ו-$yRz\iff y^2+z^2=2k_2$, עבור $k_1,k_2\in\mathbb{Z}$. "
      r"אז $2(k_1+k_2)=x^2+2y^2+z^2$, ולכן $x^2+z^2=2(k_1+k_2-y^2)$ הוא מספר זוגי, כלומר $xRz$ (כי $k_1,k_2,y$ שלמים)."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"מחלקות השקילות: לכל $x\in\mathbb{Z}$ מתקיים $x\in[0]\iff xR0\iff x^2=x^2+0^2$ הוא מספר זוגי $\iff x$ זוגי. לכן $[0]=\{2k:\ k\in\mathbb{Z}\}$."
      "\n"
      r"$1\in\mathbb{Z}$, $1\notin[0]$, ולכל $x\in\mathbb{Z}$ מתקיים $x\in[1]\iff xR1\iff x^2+1$ הוא מספר זוגי $\iff x^2$ הוא מספר אי-זוגי $\iff x$ אי-זוגי. לכן $[1]=\{2k+1:\ k\in\mathbb{Z}\}$."
      "\n"
      r"מכיוון ש-$[0]\cup[1]=\mathbb{Z}$, נקבל $\mathbb{Z}/R=\{[0],[1]\}$."
      "\n"
      r"**הערה:** הטענה “$x^2$ זוגי $\iff x$ זוגי” נכונה, כי: אם $x=2k$ אז $x^2=4k^2=2(2k^2)$ זוגי; "
      r"אם $x=2k+1$ אז $x^2=4k^2+4k+1=2(2k^2+2k)+1$ אי-זוגי."
      "\n"
      r"**(2)** $R$ אינו יחס סדר חלקי, כי הוא אינו אנטי-סימטרי. דוגמה נגדית: $1\ne3$ אך $(1,3),(3,1)\in R$, כי $10=1^2+3^2=3^2+1^2$ הוא מספר זוגי."),

    # ---------------- Q3 ----------------
    Q(3, "א", "computation", "modular_fermat_wilson", 12,
      r"תהי $A$ קבוצת כל המספרים הראשוניים. הפונקציה $f:A\to\mathbb{N}$ מוגדרת לפי הכלל הבא: "
      r"$f(n)=\left(\varnothing(n)^{\varnothing(n)}\right)\pmod n$ לכל $n\in A$, כאשר $\varnothing$ היא הפונקציה של Euler."
      "\n"
      r"**(1)** חשבו: $f(3)+f(5)$;"
      "\n"
      r"**(2)** בדקו האם $f$ היא פונקציה חד-חד-ערכית;"
      "\n"
      r"**(3)** מצאו את הקבוצה $B\subseteq\mathbb{N}$ כך ש: $f:A\to B$ היא פונקציה על."
      "\n"
      r"**(4)** הראו ש: $\left(\varnothing(n)^{\varnothing(n)}\right)(\bmod\ \varnothing(n))<f(n)$ מתקיים לכל $n\in A$.",
      r"**(1)** $f(3)=\left(\varnothing(3)^{\varnothing(3)}\right)\bmod3=2^2\bmod3=4\bmod3=1$."
      "\n"
      r"$f(5)=\varnothing(5)^{\varnothing(5)}\bmod5=4^4\bmod5=256\bmod5=1$."
      "\n"
      r"לכן $f(3)+f(5)=2$."
      "\n"
      r"**(2)** $f$ אינה חד-חד-ערכית: $3\ne5$ אך $f(3)=f(5)=1$."
      "\n"
      r"**(3)** לפי ההגדרה של $f$, לכל $n\in A$ מתקיים: $n$ ראשוני, ולכן $\varnothing(n)=n-1$ "
      r"(כי $\varnothing(n)=n\left(1-\frac1n\right)=n\cdot\frac{n-1}{n}=n-1$). "
      r"אז $f(n)=\left(\varnothing(n)^{\varnothing(n)}\right)\bmod n=(n-1)^{n-1}\bmod n$."
      "\n"
      r"$n$ ראשוני ו-$n\nmid(n-1)$, לכן לפי משפט FERMAT: $(n-1)^{n-1}\bmod n=1$."
      "\n"
      r"מסקנה: $f(n)=1$ לכל $n\in A$, ולכן $f:A\to B=\{1\}$ היא פונקציה על, כלומר $B=\{1\}$."
      "\n"
      r"**(4)** $\left(\varnothing(n)^{\varnothing(n)}\right)\bmod\varnothing(n)=(n-1)^{n-1}\bmod(n-1)=0$, כי $(n-1)\mid(n-1)^{n-1}$."
      "\n"
      r"מסקנה: $\left(\varnothing(n)^{\varnothing(n)}\right)\bmod\varnothing(n)=0<f(n)=1$, לכל $n\in A$."),

    Q(3, "ב", "computation", "recurrence_sums", 13,
      r"מצאו את הצורה המפורשת של $(a_n)$, כאשר: $a_0=25$, $a_1=128$ ו-$a_n=5a_{n-1}-6a_{n-2}+6\cdot5^n$ עבור $2\le n$.",
      r"המשוואה האופיינית: $r^2-5r+6=0$, ולכן $r_1=2$, $r_2=3$."
      "\n"
      r"פתרון הנוסחה ההומוגנית: $a_n^{(h)}=C_1\cdot2^n+C_2\cdot3^n$."
      "\n"
      r"פתרון פרטי של הנוסחה הלא הומוגנית: $a_n^{(p)}=A\cdot5^n\cdot n^k$, כאשר $k=0$ כי $r=5$ אינו שורש של המשוואה האופיינית."
      "\n"
      r"נציב $a_n^{(p)}=A\cdot5^n$, $a_{n-1}^{(p)}=A\cdot5^{n-1}$, $a_{n-2}^{(p)}=A\cdot5^{n-2}$ במשוואה, ונחלק ב-$5^{n-2}$:"
      "\n"
      r"$$25A=5A\cdot5-6A+6\cdot25\ \Rightarrow\ A=25$$"
      "\n"
      r"לכן $a_n^{(p)}=25\cdot5^n$."
      "\n"
      r"הפתרון הכללי: $a_n=a_n^{(h)}+a_n^{(p)}=C_1\cdot2^n+C_2\cdot3^n+25\cdot5^n$."
      "\n"
      r"$a_0=C_1+C_2+25=25\ \Rightarrow\ C_1+C_2=0$"
      "\n"
      r"$a_1=2C_1+3C_2+125=128\ \Rightarrow\ 2C_1+3C_2=3$"
      "\n"
      r"נקבל $C_1=-3$, $C_2=3$."
      "\n"
      r"מסקנה: $a_n=-3\cdot2^n+3\cdot3^n+25\cdot5^n$, לכל $n\in\mathbb{N}$."),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "combinatorics", 5,
      r"חשבו את $f(n)=\sum_{k=0}^{n}\left(\binom{n}{k}\cdot\left(3^k+4^k\right)\right)$ ובדקו האם: $f(n)=O(7^n)$.",
      r"$f(n)=\sum_{k=0}^{n}\binom nk3^k+\sum_{k=0}^{n}\binom nk4^k=\sum_{k=0}^{n}\binom nk3^k1^{n-k}+\sum_{k=0}^{n}\binom nk4^k1^{n-k}$"
      "\n"
      r"$$=(3+1)^n+(4+1)^n=4^n+5^n$$"
      "\n"
      r"כלומר $f(n)=4^n+5^n$, לכל $n\in\mathbb{N}$."
      "\n"
      r"מכיוון ש-$4^n\le7^n$ וגם $5^n\le7^n$ לכל $n\in\mathbb{N}$, נקבל $f(n)=4^n+5^n\le2\cdot7^n$ לכל $n\in\mathbb{N}$."
      "\n"
      r"מסקנה: $f(n)=O(7^n)$."),

    Q(4, "ב", "computation", "combinatorics", 15,
      r"תהי הקבוצה $A=\{a,b,c,d,e,f\}$."
      "\n"
      r"**(1)** מצאו את מספר המילים ב-3 אותיות שניתן ליצור מ-$A$ כך שבכל מילה האות הראשונה היא $a$ או $b$;"
      "\n"
      r"**(2)** מצאו את מספר המילים ב-4 אותיות **שונות** שניתן ליצור מ-$A$;"
      "\n"
      r"**(3)** מצאו את מספר המילים ב-6 אותיות **שונות** שניתן ליצור מ-$A$ כך שבכל מילה מופיע הרצף “ab” ובנוסף האותיות $c,d$ הן נמצאות בסמיכות.",
      r"**(1)** לאות הראשונה יש 2 אפשרויות ($a$ או $b$), ולכל אחת משתי האותיות הנוספות יש 6 אפשרויות: $2\cdot6\cdot6=72$ מילים."
      "\n"
      r"**(2)** לאות הראשונה 6 אפשרויות, לשנייה 5, לשלישית 4 ולרביעית 3: $P(6,4)=6\cdot5\cdot4\cdot3=360$ מילים."
      "\n"
      r"**(3)** נתייחס ל-“ab” כאל יחידה אחת, ול-$c,d$ הצמודות כאל יחידה אחת שיש לה 2 סידורים פנימיים ($cd$ או $dc$). "
      r"נשארות 4 יחידות: “ab”, היחידה של $c,d$, $e$ ו-$f$. "
      r"סה״כ $4!\cdot2!=48$ מילים."),

    H(4, "ג", "computation", "combinatorics", 5,
      r"תהי הקבוצה $A=\{a,b,c,d\}$."
      "\n"
      r"מצאו כמה מילים המורכבות ב-25 אותיות מ-$A$ ניתן ליצור כאשר בכל מילה תופיע:"
      "\n"
      r"האות $a$ לפחות 4 פעמים, האות $b$ לפחות 3 פעמים, האות $c$ לפחות 5 פעמים והאות $d$ לפחות 2 פעמים.",
      "official-key-disagrees: the key answers 364 = C(14,3), the number of letter-count vectors "
      "(x1+x2+x3+x4=25 with the lower bounds), not the number of words; the number of 25-letter words is "
      "746544967234440 (script-checked), so the key does not answer the printed question"),
]

# the held item keeps its key as a note for the orchestrator (not shipped: held items are not in the bank)
exam = {
    "examCode": "18A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשע"ח, מועד א (13.02.2018)',
    "year": 2018,
    "examDate": "13.02.2018",
    "sourceFile": "18A-A exam with handwritten solution, pp.1-12",
    "solutionFile": "18A-A handwritten solution (author unknown), pp.3-12",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
