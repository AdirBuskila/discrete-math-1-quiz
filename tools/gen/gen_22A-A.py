# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-A.json -- discrete math 1 (20067), semester A 5782, moed A (25.01.2022).
The paper has TWO FORMS ("גרסה 1" / "גרסה 2"). Form 1 is transcribed as Q1-Q4, form 2 as Q5-Q8
(num = form-1 num + 4, "(גרסה 2)" in the stem). The key is handwritten (author unknown) = student-solution,
except the typed definitions and truth table of Q1a = lecturer-solution. Where the key says "same as form 1"
and the printed text is identical, the form-1 solution is reused.
Checks: tools/verify/22A-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_22A-A.py
 - Q1b, Q4b (sub-parts 1,2) and Q3a are ONE item each."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-A.json"


def Q(num, part, kind, topic, points, question, solution, typed=False, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution" if typed else "student-solution",
         "official": bool(typed), "confidence": "high" if typed else "med"}
    q.update(kw)
    return q


def H(num, part, kind, topic, points, question, reason):
    return {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
            "question": question, "hold": reason}


V2 = "(גרסה 2)\n"

# ---------------- shared pieces ----------------
TT = ("טבלת אמת:\n"
      "```\n"
      "p q r | p→q | ¬r | (p→q)∧(¬r) | פסוק מינימלי\n"
      "T T T |  T  |  F |      F      | ¬p∨¬q∨¬r\n"
      "T T F |  T  |  T |      T      | p∧q∧¬r\n"
      "T F T |  F  |  F |      F      | ¬p∨q∨¬r\n"
      "T F F |  F  |  T |      F      | ¬p∨q∨r\n"
      "F T T |  T  |  F |      F      | p∨¬q∨¬r\n"
      "F T F |  T  |  T |      T      | ¬p∧q∧¬r\n"
      "F F T |  T  |  F |      F      | p∨q∨¬r\n"
      "F F F |  T  |  T |      T      | ¬p∧¬q∧¬r\n"
      "```\n")
CNF_S = ("**א. הגדרה לפי הרצאה:** נאמר שהפסוק כתוב בצורת CNF אם הוא כתוב בצורה "
         r"$C_1\wedge C_2\wedge\ldots\wedge C_k$, כאשר כל $C_i$ הוא פסוק מהצורה $A_1\vee A_2\vee\ldots\vee A_{t_i}$ "
         "וכל $A_j$ הוא משתנה פסוקי או שלילה של משתנה פסוקי כלשהו.\n"
         r"**ב.** בנו צורת CNF עבור הפסוק $(p\to q)\wedge\neg r$:"
         "\n" + TT +
         "לכן צורת ה-CNF של הפסוק (מהשורות שבהן הפסוק שקר):\n"
         r"$(\neg p\vee\neg q\vee\neg r)\wedge(\neg p\vee q\vee\neg r)\wedge(\neg p\vee q\vee r)\wedge(p\vee\neg q\vee\neg r)\wedge(p\vee q\vee\neg r)$")
DNF_S = ("**א. הגדרה לפי הרצאה:** נאמר שהפסוק כתוב בצורת DNF אם הוא כתוב בצורה "
         r"$D_1\vee D_2\vee\ldots\vee D_k$, כאשר כל $D_i$ הוא פסוק מהצורה $A_1\wedge A_2\wedge\ldots\wedge A_{t_i}$ "
         "וכל $A_j$ הוא משתנה פסוקי או שלילה של משתנה פסוקי כלשהו.\n"
         r"**ב.** בנו צורת DNF עבור הפסוק $(p\to q)\wedge\neg r$:"
         "\n" + TT +
         "לכן צורת ה-DNF של הפסוק (מהשורות שבהן הפסוק אמת):\n"
         r"$(p\wedge q\wedge\neg r)\vee(\neg p\wedge q\wedge\neg r)\vee(\neg p\wedge\neg q\wedge\neg r)$")

EUC = ("```\n"
       "a    b    [a/b]   d    x     y\n"
       "55   40   1       5    3     -1-3*1 = -4\n"
       "40   15   2       5    -1    1-(-1)*2 = 3\n"
       "15   10   1       5    1     0-1*1 = -1\n"
       "10   5    2       5    0     1-0*2 = 1\n"
       "5    0    -       5    1     0\n"
       "```\n"
       r"$\gcd(55,40)=5=3\cdot55+(-4)\cdot40$, כלומר $x=3,\ y=-4$."
       "\n")

Q2C_Q = ("נסחו את ה-contrapositive של הטענה הבאה:\n"
         r"\"יהיו $A,B,C$ קבוצות לא ריקות. אם $A-B\subseteq C$, אז $A-C\subseteq B$\"."
         "\nהוכיחו את הטענה.")
Q2C_S = (r"ה-contrapositive הוא: \"אם $A-C\not\subseteq B$, אז $A-B\not\subseteq C$\"."
         "\n"
         r"**הוכחת ה-contrapositive:**"
         "\n"
         r"$A-C\not\subseteq B\Rightarrow\exists x\in A-C\ \wedge\ x\notin B\Rightarrow x\in A\wedge x\notin C\wedge x\notin B"
         r"\Rightarrow x\in A-B\wedge x\notin C\Rightarrow A-B\not\subseteq C$."
         "\n"
         r"**בדרך השלילה:** נניח בשלילה ש-$A-B\subseteq C$ וגם $A-C\not\subseteq B$. "
         r"אז $\exists x\in A-C\ \wedge\ x\notin B\Rightarrow x\in A\wedge x\notin C\wedge x\notin B"
         r"\Rightarrow x\in A-B\wedge x\notin C\Rightarrow A-B\not\subseteq C$, סתירה לנתון.")

Q3C_Q = (r"תהיינה $A=\{1,2,3,4,5\}$ ו-$R\subseteq A\times A$. הוכיחו או הפריכו: "
         r"אם $R$ הוא יחס סדר מלא, אז $R$ אינו פונקציה.")
Q3C_S = (r"נתון: $R\subseteq\{1,2,3,4,5\}^2$ סדר מלא."
         "\n"
         r"מכיוון ש-$R$ רפלקסיבי: $(1,1),(2,2)\in R$. ומכיוון ש-$R$ סדר מלא: $(1,2)\in R$ או $(2,1)\in R$."
         "\n"
         r"$(1,1)\in R$ וגם $(1,2)\in R\Rightarrow R\ne$ פונקציה."
         "\n"
         r"או $(2,2)\in R$ וגם $(2,1)\in R\Rightarrow R\ne$ פונקציה."
         "\n"
         r"מסקנה: $R$ אינו פונקציה. הטענה נכונה.")

Q3B_TAB = ("```\n"
           "f(1) = 1 (mod 6) + lcm(2, gcd(2,1)) = 1 + lcm(2,1) = 1 + 2 = 3\n"
           "f(2) = 4 (mod 6) + lcm(2, gcd(2,2)) = 4 + lcm(2,2) = 4 + 2 = 6\n"
           "f(3) = 9 (mod 6) + lcm(2, gcd(2,3)) = 3 + lcm(2,1) = 3 + 2 = 5\n"
           "f(4) = 16 (mod 6) + lcm(2, gcd(2,4)) = 4 + lcm(2,2) = 4 + 2 = 6\n"
           "f(5) = 25 (mod 6) + lcm(2, gcd(2,5)) = 1 + lcm(2,1) = 1 + 2 = 3\n"
           "f(6) = 36 (mod 6) + lcm(2, gcd(2,6)) = 0 + lcm(2,2) = 2\n")

Q4A_Q = r"חשבו את העוצמה של הקבוצה "
Q4A_S = (r"$(0,1)\subseteq A\subseteq\mathbb{R}$."
         "\n"
         r"הפונקציה $f:(0,1)\to A$, $f(x)=x$ לכל $x\in A$, חח\"ע, כי $(0,1)\subseteq A$, ולכן $|(0,1)|\le|A|$."
         "\n"
         r"הפונקציה $g:A\to\mathbb{R}$, $g(x)=x$ לכל $x\in A$, חח\"ע, כי $A\subseteq\mathbb{R}$, ולכן $|A|\le|\mathbb{R}|$."
         "\n"
         r"$|\mathbb{R}|=|(0,1)|\le|A|\le|\mathbb{R}|$, ולכן $|A|=|\mathbb{R}|=\mathfrak{c}$.")
Q4A_S = Q4A_S.replace('חח\\"ע', "חד-חד-ערכית")
Q4B2_S = (r"(2) $1<|B|<|A|$: כל תתי-הקבוצות, פחות הקבוצה הריקה ו-$A$ עצמה (2 קבוצות), פחות הקבוצות מגודל 1 ($2n+1$ קבוצות): "
          r"$2^{|A|}-2-(2n+1)=2^{2n+1}-2n-3$.")

questions = []
add = questions.append

# ======================= FORM 1 =======================
add(Q(1, "א", "computation", "logic_propositional", 14,
      r"הגדירו את המונח: צורת CNF של פסוק. בנו צורת CNF עבור הפסוק $(p\to q)\wedge\neg r$ בעזרת טבלת אמת.",
      CNF_S, typed=True))

add(Q(1, "ב", "computation", "number_theory_gcd", 9,
      r"בעזרת האלגוריתם המורחב של EUCLID, מצאו $x,y\in\mathbb{Z}$ כך ש: $\gcd(55,40)=55x+40y$. "
      r"חשבו את $\operatorname{lcm}(-55,40)$.",
      r"נריץ את האלגוריתם המורחב (עמודות: $a,\ b,\ \lfloor a/b\rfloor,\ d,\ x=y',\ y=x'-y'\lfloor a/b\rfloor$):"
      "\n" + EUC +
      r"$$\operatorname{lcm}(-55,40)=\frac{|-55\cdot40|}{\gcd(55,40)}=\frac{55\cdot40}{5}=440$$"))

add(Q(1, "ג", "computation", "modular_fermat_wilson", 7,
      r"חשבו את $\left(16^{15}+7^{60}+37\right)\pmod{31}$.",
      r"$16^{15}+7^{60}+37=4^{2\cdot15}+(7^2)^{30}+31+6=(4^{31-1}-1)+(49^{31-1}-1)+31+8$."
      "\n"
      r"מכיוון ש-31 ראשוני, $31\nmid4$ ו-$31\nmid49$, לפי פרמה: $4^{31-1}-1=31k$ ו-$49^{31-1}-1=31m$ עבור $k,m\in\mathbb{Z}$."
      "\n"
      r"לכן $\left(16^{15}+7^{60}+37\right)\pmod{31}=(31k+31m+31+8)\pmod{31}=(31(k+m+1)+8)\pmod{31}=8$."))

add(Q(2, "א", "proof", "induction", 16,
      r"הוכיחו באינדוקציה מתמטית שלכל $n\in\mathbb{N},\ 1\le n$, מתקיים:"
      "\n"
      r"$$(n+1)+(n+2)+(n+3)+\ldots+(2n)=\frac{n(3n+1)}{2}$$",
      r"$P(n):\ (n+1)+(n+2)+\ldots+(2n)=\frac{n(3n+1)}{2},\ n\ge1$."
      "\n"
      r"**I. בסיס:** $P(1)$: $1+1=\frac{1\cdot(3+1)}{2}\iff2=2\Rightarrow P(1)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=\text{TRUE}$ עבור $1\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ (k+1)+\ldots+(2k)=\frac{k(3k+1)}{2}$ (הנחת האינדוקציה)"
      "\n"
      r"$P(k+1):\ (k+2)+(k+3)+\ldots+(2k+2)=\frac{(k+1)(3k+4)}{2}$"
      "\n"
      r"נפתח את אגף שמאל של $P(k+1)$:"
      "\n"
      r"$$(k+2)+(k+3)+\ldots+(2k)+(2k+1)+(2k+2)=\frac{k(3k+1)}{2}-(k+1)+(2k+1)+(2k+2)$$"
      "\n"
      r"נותר להוכיח: $\frac{k(3k+1)}{2}-(k+1)+(2k+1)+(2k+2)=\frac{(k+1)(3k+4)}{2}$, כלומר (אחרי הכפלה ב-2): "
      r"$3k^2+k-2k-2+4k+2+4k+4=3k^2+4k+3k+4\iff0=0\Rightarrow P(k+1)=\text{TRUE}$."
      "\n"
      r"**III. מסקנה:** מ-I ו-II, לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$."))

add(Q(2, "ב", "computation", "sets_power_set", 6,
      r"יהיו הקבוצות $A=\{3^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,19\}\}$ ו-$B=\{2^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,19\}\}$."
      "\n"
      r"חשבו את: $|A\cap B|+|P(A\times B)|+|P(A-B)|$.",
      r"$x\in A\cap B\iff x=3^0\cdot5^m=2^0\cdot5^m,\ m\in\{0,1,\ldots,19\}\Rightarrow|A\cap B|=20$."
      "\n"
      r"$|A-B|=|A-A\cap B|=|A|-|A\cap B|=400-20=380$."
      "\n"
      r"$|P(A\times B)|=2^{|A\times B|}=2^{|A|\cdot|B|}=2^{400\cdot400}=2^{160000}$."
      "\n"
      r"מסקנה: $$|A\cap B|+|P(A\times B)|+|P(A-B)|=20+2^{160000}+2^{380}$$"))

add(Q(2, "ג", "proof", "sets_power_set", 8, Q2C_Q, Q2C_S))

add(Q(3, "א", "proof", "equivalence_relations", 17,
      r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$ מתקיים "
      r"$xRy\iff3x+5y$ הוא מספר זוגי."
      "\n"
      r"הוכיחו ש-$R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי?",
      r"**$R$ רפלקסיבי:** לכל $x\in\mathbb{Z}$: $xRx\iff3x+5x=8x$ הוא מספר זוגי (TRUE)."
      "\n"
      r"**$R$ סימטרי:** לכל $x,y\in\mathbb{Z}$, אם $xRy$ אז $yRx$. $2k=3x+5y\iff xRy$ עבור $k\in\mathbb{Z}$. "
      r"צריך להראות ש-$3y+5x$ מספר זוגי ($yRx$)."
      "\n"
      r"$3y+5x$ הוא מספר זוגי: $2m=8x+8y=(3x+5y)+(3y+5x)$, ולכן $3y+5x=2m-2k=2(m-k)$ הוא מספר זוגי, כלומר $R$ סימטרי."
      "\n"
      r"**$R$ טרנזיטיבי:** לכל $x,y,z\in\mathbb{Z}$: $xRy$ וגם $yRz$, אז $xRz$. $2k=3x+5y\iff xRy$ ו-$2m=3y+5z\iff yRz$ ($k,m\in\mathbb{Z}$)."
      "\n"
      r"$2(k+m)=2k+2m=3x+5z+8y$, ולכן $3x+5z=2(k+m-4y)$ הוא מספר זוגי, כלומר $xRz$. לכן $R$ יחס שקילות."
      "\n"
      r"$[0]=\{x:\ x\in\mathbb{Z}\wedge0Rx\}=\{x:\ x\in\mathbb{Z}\wedge2\mid(3\cdot0+5x)\}=\{x:\ x\in\mathbb{Z}\wedge2\mid5x\}"
      r"=\{x:\ x\in\mathbb{Z}\wedge2\mid x\}=\{2k:\ k\in\mathbb{Z}\}$, כי $2\nmid5\wedge2\mid5x\Rightarrow2\mid x$."
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}\wedge1Rx\}=\{x:\ x\in\mathbb{Z}\wedge2\mid(3+5x)\}=\{2k+1:\ k\in\mathbb{Z}\}$, "
      r"כי $3$ אי-זוגי ו-$2\mid(3+5x)$ מחייב ש-$5x$ אי-זוגי, כלומר $x$ אי-זוגי."
      "\n"
      r"מסקנה: $\mathbb{Z}/R=\{[0],[1]\}=\{\{2k:\ k\in\mathbb{Z}\},\{2k+1:\ k\in\mathbb{Z}\}\}$."
      "\n"
      r"$R$ אינו יחס סדר חלקי, כי $R$ אינו אנטי-סימטרי: $1R3$ כי $2\mid18=3\cdot1+5\cdot3$, "
      r"ו-$3R1$ כי $2\mid14=3\cdot3+5\cdot1$, אבל $1\ne3$."))

add(Q(3, "ב", "computation", "functions", 8,
      r"הפונקציה $f:\{1,2,3,4,5,6\}\to A$ מוגדרת לפי הכלל $f(k)=k^2\pmod6+\operatorname{lcm}(2,\gcd(2,k))$ "
      r"לכל $k\in\{1,2,3,4,5,6\}$."
      "\n"
      r"מצאו את $A$ כך ש-$f$ היא פונקציה על.",
      "חישוב הערכים:\n" + Q3B_TAB + "```\n"
      r"$A=f(\{1,2,3,4,5,6\})=\{2,3,5,6\}\iff f$ על, כי לכל $y\in A$ קיים מקור."))

add(Q(3, "ג", "proof", "partial_orders", 5, Q3C_Q, Q3C_S))

add(Q(4, "א", "computation", "cardinality_sets", 5,
      Q4A_Q + r"$A=(-\infty,2)\cup[3,8)$.", Q4A_S))

add(Q(4, "ב", "computation", "sets_power_set", 5,
      r"תהי $A=\{1,2,3,\ldots,2n+1\}$, כאשר $3<n\in\mathbb{N}$."
      "\n"
      r"(1) (3 נק.) חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאי $|B\cap\{1,3,5,7,\ldots,2n+1\}|=1$."
      "\n"
      r"(2) (2 נק.) חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאים: $1<|B|<|A|$.",
      r"(1) $|B\cap\{1,3,5,\ldots,2n+1\}|=1\wedge B\in P(A)\iff B=\{x\}\cup C$, כאשר $x\in\{1,3,\ldots,2n+1\}$ ו-$C\subseteq\{2,4,6,\ldots,2n\}$."
      "\n"
      r"$x\in\{1,3,\ldots,2n+1\}$: יש $n+1$ אפשרויות. $C\in P(\{2,4,6,\ldots,2n\})$: יש $2^n$ אפשרויות "
      r"($2^n=|P(\{2,4,\ldots,2n\})|=2^{|\{2,4,\ldots,2n\}|}$)."
      "\n"
      r"מסקנה: יש $(n+1)\cdot2^n$ תתי-קבוצות $B$ מתאימות."
      "\n" + Q4B2_S))

# ======================= FORM 2 =======================
add(Q(5, "א", "computation", "logic_propositional", 14,
      V2 + r"הגדירו את המונח: צורת DNF של פסוק. בנו צורת DNF עבור הפסוק $(p\to q)\wedge\neg r$ בעזרת טבלת אמת.",
      DNF_S, typed=True))

add(Q(5, "ב", "computation", "number_theory_gcd", 9,
      V2 + r"בעזרת האלגוריתם המורחב של EUCLID, מצאו $x,y\in\mathbb{Z}$ כך ש: $\gcd(55,40)=55x+40y$. "
      r"חשבו את $\operatorname{lcm}(55,-40)$.",
      r"נריץ את האלגוריתם המורחב (עמודות: $a,\ b,\ \lfloor a/b\rfloor,\ d,\ x=y',\ y=x'-y'\lfloor a/b\rfloor$):"
      "\n" + EUC +
      r"$$\operatorname{lcm}(55,-40)=\frac{|55\cdot(-40)|}{\gcd(55,-40)}=\frac{55\cdot40}{5}=440,\ \ \gcd(55,-40)=\gcd(55,40)$$"))

add(Q(5, "ג", "computation", "modular_fermat_wilson", 7,
      V2 + r"חשבו את $\left(36^{15}+8^{60}+47\right)\pmod{31}$.",
      r"$36^{15}+8^{60}+47=6^{30}+64^{30}+31+16=(6^{31-1}-1)+(64^{31-1}-1)+31+18$."
      "\n"
      r"מכיוון ש-31 ראשוני, $31\nmid6$ ו-$31\nmid64$, לפי פרמה: $31\mid6^{31-1}-1$ ו-$31\mid64^{31-1}-1$."
      "\n"
      r"מסקנה: $18\equiv\left(36^{15}+8^{60}+47\right)\pmod{31}$, כלומר התוצאה היא $18$."))

add(Q(6, "א", "proof", "induction", 16,
      V2 + r"הוכיחו באינדוקציה מתמטית שלכל $n\in\mathbb{N},\ 1\le n$, מתקיים:"
      "\n"
      r"$$(n+2)+(n+3)+(n+4)+\ldots+(2n+2)=\frac{(n+1)(3n+4)}{2}$$",
      r"$P(n):\ (n+2)+(n+3)+\ldots+(2n+2)=\frac{(n+1)(3n+4)}{2},\ \forall n\in\mathbb{N},\ n\ge1$."
      "\n"
      r"**I. בסיס:** $P(1)$: $3+4=\frac{2\cdot7}{2}\iff7=7\Rightarrow P(1)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=\text{TRUE}$ עבור $1\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ (k+2)+(k+3)+\ldots+(2k+2)=\frac{(k+1)(3k+4)}{2}$"
      "\n"
      r"$P(k+1):\ (k+3)+\ldots+(2k+4)=\frac{(k+2)(3k+7)}{2}$"
      "\n"
      r"לפי הנחת האינדוקציה נקבל:"
      "\n"
      r"$$(k+3)+\ldots+(2k+2)+(2k+3)+(2k+4)=\frac{(k+1)(3k+4)}{2}-(k+2)+(2k+3)+(2k+4)=\frac{(k+1)(3k+4)}{2}+3k+5$$"
      "\n"
      r"נותר להוכיח: $\frac{(k+1)(3k+4)}{2}+3k+5=\frac{(k+2)(3k+7)}{2}$, כלומר (אחרי הכפלה ב-2): "
      r"$3k^2+4k+3k+4+6k+10=3k^2+7k+6k+14\iff0=0\Rightarrow P(k+1)=\text{TRUE}$."
      "\n"
      r"**III. מסקנה:** מ-I ו-II, לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$."))

add(Q(6, "ב", "computation", "sets_power_set", 6,
      V2 + r"יהיו הקבוצות $A=\{3^n\cdot7^m:\ m,n\in\{0,1,2,\ldots,29\}\}$ ו-$B=\{3^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,29\}\}$."
      "\n"
      r"חשבו את: $|A-B|+|P(A\times B)|+|P(A\cap B)|$.",
      r"**הפתרון הרשמי עם תיקון $|A|\cdot|B|=900\cdot900=810000$ (ולא $300\cdot300=90000$):** הפתרון הרשמי משתמש בעצמו ב-$|A|=30\cdot30=900$ "
      r"(בחישוב $|A-B|=870$), אבל בחישוב $|A\times B|$ כותב $300\cdot300=90000$ ומקבל $870+2^{90000}+2^{30}$. "
      r"התשובה המתוקנת היא $870+2^{810000}+2^{30}$ (נבדק בסקריפט)."
      "\n"
      r"$|A|=|B|=30\cdot30=900$ (לכל זוג $(n,m)$ מתקבל מספר שונה, לפי יחידות הפירוק לראשוניים)."
      "\n"
      r"$A\cap B=\{3^n:\ n\in\{0,\ldots,29\}\}$ (מספר מהצורה $3^n7^m$ שווה ל-$3^k5^j$ רק אם $m=j=0$), ולכן $|A\cap B|=30$ ו-$|P(A\cap B)|=2^{30}$."
      "\n"
      r"$|A-B|=|A|-|A\cap B|=900-30=870$."
      "\n"
      r"$|P(A\times B)|=2^{|A|\cdot|B|}=2^{900\cdot900}=2^{810000}$."
      "\n"
      r"מסקנה: $$870+2^{810000}+2^{30}$$",
      solutionSource="solved", confidence="high"))

add(Q(6, "ג", "proof", "sets_power_set", 8, V2 + Q2C_Q, Q2C_S))

add(Q(7, "א", "proof", "equivalence_relations", 17,
      V2 + r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$ מתקיים "
      r"$xRy\iff3x+7y$ הוא מספר זוגי."
      "\n"
      r"הוכיחו ש-$R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי?",
      r"(המפתח כותב רק שהפתרון דומה לגרסה 1; הפתרון כאן נכתב לפי המספרים של גרסה 2 ונבדק בסקריפט.)"
      "\n"
      r"**$R$ רפלקסיבי:** לכל $x\in\mathbb{Z}$: $3x+7x=10x=2\cdot5x$ זוגי, ולכן $xRx$."
      "\n"
      r"**$R$ סימטרי:** יהיו $x,y\in\mathbb{Z}$ עם $xRy$, כלומר $3x+7y=2k$ עבור $k\in\mathbb{Z}$. "
      r"מכיוון ש-$(3x+7y)+(3y+7x)=10x+10y$, מתקיים $3y+7x=10x+10y-2k=2(5x+5y-k)$, זוגי, ולכן $yRx$."
      "\n"
      r"**$R$ טרנזיטיבי:** יהיו $x,y,z\in\mathbb{Z}$ עם $xRy$ וגם $yRz$: $3x+7y=2k$ ו-$3y+7z=2m$ ($k,m\in\mathbb{Z}$). "
      r"אז $2k+2m=3x+7z+10y$, ולכן $3x+7z=2(k+m-5y)$ זוגי, כלומר $xRz$. לכן $R$ יחס שקילות."
      "\n"
      r"$[0]=\{x\in\mathbb{Z}:\ 0Rx\}=\{x\in\mathbb{Z}:\ 2\mid7x\}=\{x\in\mathbb{Z}:\ 2\mid x\}=\{2k:\ k\in\mathbb{Z}\}$, כי $2\nmid7$."
      "\n"
      r"$[1]=\{x\in\mathbb{Z}:\ 1Rx\}=\{x\in\mathbb{Z}:\ 2\mid(3+7x)\}=\{2k+1:\ k\in\mathbb{Z}\}$, "
      r"כי $3$ אי-זוגי ו-$2\mid(3+7x)$ מחייב ש-$7x$ אי-זוגי, כלומר $x$ אי-זוגי."
      "\n"
      r"מסקנה: $\mathbb{Z}/R=\{[0],[1]\}=\{\{2k:\ k\in\mathbb{Z}\},\{2k+1:\ k\in\mathbb{Z}\}\}$."
      "\n"
      r"$R$ אינו יחס סדר חלקי, כי $R$ אינו אנטי-סימטרי: $1R3$ כי $2\mid24=3\cdot1+7\cdot3$, "
      r"ו-$3R1$ כי $2\mid16=3\cdot3+7\cdot1$, אבל $1\ne3$.",
      solutionSource="solved", confidence="high"))

add(Q(7, "ב", "computation", "functions", 8,
      V2 + r"הפונקציה $f:\{1,2,3,4,5,6,7\}\to A$ מוגדרת לפי הכלל $f(k)=k^2\pmod6+\operatorname{lcm}(2,\gcd(2,k))$ "
      r"לכל $k\in\{1,2,3,4,5,6,7\}$."
      "\n"
      r"מצאו את $A$ כך ש-$f$ היא פונקציה על.",
      "הפתרון כמעט זהה לגרסה 1. הערכים של $f(1),\\ldots,f(6)$ כמו בגרסה 1, ובנוסף:\n"
      "```\n"
      "f(7) = 49 (mod 6) + lcm(2, gcd(2,7)) = 1 + lcm(2,1) = 1 + 2 = 3\n"
      "```\n"
      r"$A=f(\{1,2,3,4,5,6,7\})=\{2,3,5,6\}\iff f$ על."))

add(Q(7, "ג", "proof", "partial_orders", 5, V2 + Q3C_Q, "הפתרון כמו בגרסה 1.\n" + Q3C_S))

add(Q(8, "א", "computation", "cardinality_sets", 5,
      V2 + Q4A_Q + r"$A=(-5,-2]\cup[-1,\infty)$.", "הפתרון כמו בגרסה 1: " + Q4A_S))

add(Q(8, "ב", "computation", "sets_power_set", 5,
      V2 + r"תהי $A=\{1,2,3,\ldots,2n+1\}$, כאשר $3<n\in\mathbb{N}$."
      "\n"
      r"(1) (3 נק.) חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאי $|B\cap\{2,4,6,8,\ldots,2n\}|=1$."
      "\n"
      r"(2) (2 נק.) חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאים: $1<|B|<|A|$.",
      r"(1) $|B\cap\{2,4,6,\ldots,2n\}|=1\wedge B\subseteq A\iff B=\{x\}\cup C$, כאשר $x\in\{2,4,\ldots,2n\}$ ו-$C\subseteq\{1,3,5,\ldots,2n+1\}$."
      "\n"
      r"$x\in\{2,4,\ldots,2n\}$: יש $n$ אפשרויות. $C\in P(\{1,3,5,\ldots,2n+1\})$: יש $2^{n+1}$ אפשרויות."
      "\n"
      r"מסקנה: יש $n\cdot2^{n+1}$ תתי-קבוצות $B$ מתאימות."
      "\n(2) כמו בגרסה 1: " + Q4B2_S[4:]))


# ---- steps / rubric / pitfalls (ai-draft); every value is machine-checked in tools/verify/<CODE>/verify.py ----
IDS = "abcdefgh"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def ch(prompt, right, *wrong, explain=""):
    return {"type": "choice", "prompt": prompt, "options": opts(right, *wrong), "correctId": "a", "explain": explain}


def num(prompt, answer, explain="", tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def order(prompt, lines, explain=""):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, idx, explain=""):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


def mutate(lines, idx, new):
    ls = list(lines)
    ls[idx] = new
    return ls


def put(num_, part, rubric, pitfalls, steps):
    for q in questions:
        if q["num"] == num_ and q.get("part") == part:
            if "hold" in q:
                raise KeyError("held")
            assert sum(r["points"] for r in rubric) == q["points"], (num_, part, sum(r["points"] for r in rubric))
            assert 2 <= len(steps) <= 5, (num_, part, len(steps))
            q.update(rubric=rubric, rubricSource="ai-verified", pitfalls=pitfalls, steps=steps, stepsSource="ai-verified")
            return
    raise KeyError((num_, part))



# ---- shared builders for the two-form sittings (numbers are parameters; every value is re-derived in verify.py) ----
def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@" + k + "@", str(v))
    return s


def parity_item(a, b):
    """R: xRy iff a*x+b*y even (a, b odd)."""
    s = a + b
    rubric = rub(("רפלקסיביות: $x R x$ כי $ax+bx=(a+b)x$ זוגי", 3),
                 ("סימטריה: חיבור $ax+by$ ו-$ay+bx$ לסכום זוגי", 4),
                 ("טרנזיטיביות: חיבור שני המספרים הזוגיים וקבלת $ax+bz$ זוגי", 4),
                 ("מציאת המחלקות $[0]$ ו-$[1]$ (זוגיים ואי-זוגיים) וקבוצת המנה $\\mathbb{Z}/R$", 4),
                 ("$R$ אינו סדר חלקי כי אינו אנטי-סימטרי, עם זוג מפריך", 2))
    pit = ["לבדוק רק רפלקסיביות וסימטריה ולשכוח את הטרנזיטיביות.",
           "לטעות בתיאור המחלקות: $xR0$ בדיוק כש-$x$ זוגי, ו-$xR1$ בדיוק כש-$x$ אי-זוגי.",
           "לבלבל בין יחס שקילות ליחס סדר חלקי: סדר חלקי דורש אנטי-סימטריה, ויחס עם מחלקה של יותר מאיבר אחד אינו אנטי-סימטרי."]
    base = T(r"$@A@x+@B@y$", A=a, B=b)
    steps = [
        num(r"כמה מחלקות שקילות יש ב-$\mathbb{Z}/R$?", 2,
            "$xRy$ בדיוק כש-$x$ ו-$y$ בעלי אותה זוגיות (הוכח בבדיקה), ולכן שתי מחלקות: הזוגיים והאי-זוגיים."),
        ch(T(r"בהוכחת הסימטריה מחברים את $@A@x+@B@y$ ואת $@A@y+@B@x$. מהו הסכום?", A=a, B=b),
           T(r"$@S@(x+y)$", S=s), T(r"$@S1@(x+y)$", S1=s - 2), T(r"$@S2@(x+y)$", S2=s + 2), T(r"$@S@x+@S1@y$", S=s, S1=s - 2),
           explain=T(r"$(@A@x+@B@y)+(@A@y+@B@x)=@S@x+@S@y$, שזוגי.", A=a, B=b, S=s)),
        order("סדרו את הוכחת הטרנזיטיביות.",
              [T(r"נניח ש-$@A@x+@B@y$ זוגי וגם $@A@y+@B@z$ זוגי", A=a, B=b),
               T(r"נחבר: $(@A@x+@B@y)+(@A@y+@B@z)=@A@x+@B@z+@S@y$ זוגי", A=a, B=b, S=s),
               T(r"$@S@y$ זוגי (כי $@S@$ זוגי), ולכן גם $@A@x+@B@z$ זוגי", A=a, B=b, S=s),
               r"כלומר $xRz$ ולכן $R$ טרנזיטיבי"],
              "הנחות, חיבור, הפרשת הכפולה הזוגית, מסקנה."),
        ch("האם $R$ יחס סדר חלקי?",
           r"לא, כי אינו אנטי-סימטרי: $1R3$ וגם $3R1$ אך $1\ne3$",
           "לא, כי אינו רפלקסיבי", "כן, כי הוא יחס שקילות", "לא, כי אינו טרנזיטיבי",
           explain="הוא רפלקסיבי וטרנזיטיבי, אבל לא אנטי-סימטרי, ולכן אינו סדר חלקי."),
    ]
    return rubric, pit, steps


def contra_item(stmt_right, wrong3, lines, bad_idx, bad_line):
    rubric = rub(("ניסוח ה-contrapositive: $\\neg Q\\to\\neg P$", 3),
                 ("הנחה ש-$Q$ שקרית ומציאת איבר $x$ מתאים", 2),
                 ("שרשרת הגרירות עד שלילת $P$", 2),
                 ("מסקנה שהטענה המקורית נכונה", 1))
    pit = ["לבלבל בין contrapositive להפכי: הפיכת כיוון הגרירה בלי שלילת שני הצדדים אינה שקולה.",
           "לשלול את $\\subseteq$ כ'כל איבר אינו ב-...' במקום 'קיים איבר שאינו ב-...'.",
           "להוכיח את הטענה המקורית ישירות במקום לעבוד עם הניסוח ההפוך שנדרש."]
    steps = [
        ch("ה-contrapositive של $P\\to Q$ הוא $\\neg Q\\to\\neg P$. מהו ה-contrapositive של הטענה?", stmt_right, *wrong3,
           explain="שוללים את המסקנה והופכים אותה למקדים, ושוללים את הנתון והופכים אותו למסקנה."),
        order("סדרו את הוכחת ה-contrapositive.", lines, "כל שורה נובעת מהקודמת."),
        bug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", mutate(lines, bad_idx, bad_line), bad_idx,
            "השורה שנשתנתה אינה נובעת מהקודמת."),
    ]
    return rubric, pit, steps



# ---------------- builders for this sitting ----------------
_EUC = [r"$55=1\cdot40+15$", r"$40=2\cdot15+10$", r"$15=1\cdot10+5$", r"$10=2\cdot5+0$"]


def normal_form_item(kind):
    cnf = kind == "cnf"
    rubric = rub(("הגדרה: " + ("CNF הוא קוניונקציה של פסקאות, כל פסקה היא דיסיגנציה של ליטרלים" if cnf
                               else "DNF הוא דיסיגנציה של איברים, כל איבר הוא קוניונקציה של ליטרלים"), 4),
                 ("בניית טבלת אמת מלאה לפסוק $(p\\to q)\\wedge\\neg r$ עם עמודת ביניים", 4),
                 ("בחירת השורות הנכונות: " + ("אלה שבהן הפסוק שקר" if cnf else "אלה שבהן הפסוק אמת"), 2),
                 ("כתיבת " + ("פסקה" if cnf else "איבר") + " לכל שורה נבחרת והרכבת הביטוי הסופי", 4))
    pit = ["לבלבל בין CNF ל-DNF: " + ("ב-CNF כל שורה שקרית נותנת פסקה שהיא דיסיגנציה עם ליטרלים הפוכים" if cnf
                                       else "ב-DNF כל שורה אמיתית נותנת איבר שהוא קוניונקציה"),
           "לבחור שורות מהצד הלא נכון של הטבלה.",
           r"לטעות בטבלת האמת של $p\to q$: היא שקרית רק כש-$p$ אמת ו-$q$ שקר."]
    if cnf:
        steps = [ch("מאילו שורות בטבלה בונים את הפסקאות של ה-CNF?", "מהשורות שבהן הפסוק שקר",
                    "מהשורות שבהן הפסוק אמת", "מכל 8 השורות", "מהשורות שבהן $r$ אמת",
                    explain="פסקה שקרית בדיוק בשורה אחת, ולכן מוציאים כך את השורות השקריות."),
                 num(r"בכמה שורות הפסוק $(p\to q)\wedge\neg r$ שקר?", 5, "בטבלה 3 שורות אמת ו-5 שורות שקר."),
                 ch(r"מהי הפסקה שמתאימה לשורה $p=T,\ q=T,\ r=T$?", r"$\neg p\vee\neg q\vee\neg r$", r"$p\vee q\vee r$",
                    r"$\neg p\vee q\vee r$", r"$p\vee\neg q\vee\neg r$",
                    explain="הפסקה חייבת להיות שקרית בדיוק בשורה הזו, ולכן שוללים כל משתנה שערכו אמת.")]
    else:
        steps = [ch("מאילו שורות בטבלה בונים את האיברים של ה-DNF?", "מהשורות שבהן הפסוק אמת",
                    "מהשורות שבהן הפסוק שקר", "מכל 8 השורות", "מהשורות שבהן $r$ אמת",
                    explain="איבר אמיתי בדיוק בשורה אחת, ולכן מוסיפים איבר לכל שורה אמיתית."),
                 num(r"בכמה שורות הפסוק $(p\to q)\wedge\neg r$ אמת?", 3, "השורות $T,T,F$ ו-$F,T,F$ ו-$F,F,F$."),
                 ch(r"מהו האיבר שמתאים לשורה $p=T,\ q=T,\ r=F$?", r"$p\wedge q\wedge\neg r$", r"$p\wedge q\wedge r$",
                    r"$\neg p\wedge\neg q\wedge\neg r$", r"$p\wedge\neg q\wedge\neg r$",
                    explain="האיבר חייב להיות אמיתי בדיוק בשורה הזו, ולכן $p$, $q$ כמו שהם ו-$r$ שלילי.")]
    return rubric, pit, steps


def euclid_item(lcm_text, lcm_expl):
    rubric = rub(("הרצת האלגוריתם המורחב של Euclid על $55,40$ עם עמודת המנות", 3),
                 (r"הצבה לאחור וקבלת $5=3\cdot55+(-4)\cdot40$, כלומר $x=3,\ y=-4$", 3),
                 (r"חישוב ה-lcm לפי $\frac{|ab|}{\gcd(a,b)}$ עם הערכים המוחלטים", 3))
    pit = ["לשכוח את הערך המוחלט ב-lcm כשאחד המספרים שלילי.",
           r"לטעות בנוסחת העדכון $y=x'-y'\lfloor a/b\rfloor$ בעמודות.",
           "לעצור לפני שהשארית היא 0 ולהחזיר ערך שאינו ה-gcd."]
    steps = [num(r"מהו $\gcd(55,40)$?", 5, "השארית האחרונה שאינה אפס היא 5."),
             order(r"סדרו את שורות החילוק של האלגוריתם על $55,40$.", _EUC, "כל שורה משתמשת בשארית של השורה הקודמת."),
             ch(r"איזה זוג $(x,y)$ מקיים $5=55x+40y$?", r"$(3,-4)$", r"$(3,4)$", r"$(-4,3)$", r"$(4,-3)$",
                explain=r"$55\cdot3-40\cdot4=165-160=5$. בשאר הזוגות התוצאה שונה מ-5."),
             num(lcm_text, 440, lcm_expl)]
    return rubric, pit, steps


def fermat_item(b1, b2, k1, k2, c, fin):
    rubric = rub(("כתיבת הבסיסים כחזקות עם מעריך 30 (המעריך של פרמה מודולו 31)", 2),
                 ("שימוש בפרמה לכל חזקה: השארית 1 כי 31 ראשוני ולא מחלק את הבסיס", 3),
                 ("חיבור השאריות עם הקבוע וקבלת התשובה", 2))
    pit = ["להפעיל את פרמה בלי לבדוק ש-31 אינו מחלק את הבסיס.",
           "לא להחזיר את המעריך ל-30 (למשל להישאר עם $16^{15}$ ולהפעיל פרמה ישירות).",
           "לשכוח לצמצם את הקבוע בסוף מודולו 31."]
    steps = [ch("באיזו שיטה משתמש הפתרון?", "משפט פרמה הקטן מודולו 31 על חזקות עם מעריך 30",
                "משפט וילסון", "משפט השאריות הסיניות", "אלגוריתם Euclid המורחב",
                explain="31 ראשוני, ולכן $a^{30}\\equiv1$ לכל $a$ שאינו כפולה של 31."),
             num(T(r"מהי שארית $@B@^{30}$ בחלוקה ב-31, כאשר $@K@=@B@^{30}$?", K=k1, B=b1), 1,
                 "לפי פרמה השארית היא 1."),
             num(T(r"מהי שארית $@B@^{30}$ בחלוקה ב-31, כאשר $@K@=@B@^{30}$?", K=k2, B=b2), 1, "לפי פרמה השארית היא 1."),
             num(T(r"מהי שארית $@K1@+@K2@+@C@$ בחלוקה ב-31?", K1=k1, K2=k2, C=c), fin,
                 T(r"$1+1+@C@\equiv@F@\pmod{31}$.", C=c, F=fin))]
    return rubric, pit, steps


def P_(num_, part, built):
    r, p, s = built
    put(num_, part, r, p, s)


# ================= FORM 1 =================
P_(1, "א", normal_form_item("cnf"))
P_(1, "ב", euclid_item(r"מהו $\operatorname{lcm}(-55,40)$?", r"$\frac{|-55\cdot40|}{5}=440$."))
P_(1, "ג", fermat_item(4, 49, r"16^{15}", r"7^{60}", 37, 8))

_IND1 = [r"$(k+2)+\cdots+(2k+2)=\big[(k+1)+\cdots+2k\big]-(k+1)+(2k+1)+(2k+2)$",
         r"לפי הנחת האינדוקציה: $=\frac{k(3k+1)}{2}-(k+1)+(2k+1)+(2k+2)$",
         r"אחרי חיבור האיברים: $=\frac{3k^2+k+2(3k+2)}{2}=\frac{3k^2+7k+4}{2}$",
         r"פירוק: $=\frac{(k+1)(3k+4)}{2}$, כלומר $P(k+1)$ נכון"]
put(2, "א",
    rub(("בסיס: בדיקת $P(1)$ בשני האגפים", 3),
        ("ניסוח הנחת האינדוקציה $P(k)$ וההוכחה הנדרשת $P(k+1)$", 3),
        ("כתיבת הסכום של $P(k+1)$ באמצעות הסכום של $P(k)$ (הסרת האיבר הראשון והוספת שני האיברים האחרונים)", 5),
        ("הצבת הנחת האינדוקציה והשוואה אלגברית לאגף ימין", 4),
        ("מסקנה לפי עקרון האינדוקציה", 1)),
    ["לשכוח שמחליפים איבר ראשון: בסכום מ-$k+2$ עד $2k+2$ נעלם $k+1$ ונוספים שני איברים.",
     "לבלבל בין מספר האיברים בסכום (שגדל ב-1) לבין ערך האיבר האחרון (שגדל ב-2).",
     "להשתמש ב-$P(k+1)$ בתוך ההוכחה שלו."],
    [num(r"מהו האגף השמאלי $(n+1)+\cdots+(2n)$ עבור $n=3$?", 15, r"$4+5+6=15=\frac{3\cdot10}{2}$."),
     ch(r"איך עוברים מהסכום $(k+1)+\cdots+2k$ אל הסכום $(k+2)+\cdots+(2k+2)$?",
        r"מסירים את $(k+1)$ ומוסיפים את $(2k+1)$ ואת $(2k+2)$",
        r"מסירים את $(k+1)$ ומוסיפים רק את $(2k+2)$", r"מוסיפים את $(2k+1)$ ואת $(2k+2)$ בלי להסיר דבר",
        r"מסירים את $k$ ואת $(k+1)$ ומוסיפים את $(2k+2)$",
        explain=r"בסכום החדש הראשון הוא $k+2$ והאחרון $2k+2$, ולכן $(k+1)$ יוצא ושני האיברים החדשים נכנסים."),
     order("סדרו את שלבי הצעד.", _IND1, "פירוק הסכום, הנחה, חיבור, פירוק לגורמים."),
     bug("בגרסה הבאה של הצעד שורה אחת שגויה. מצאו אותה.",
         mutate(_IND1, 2, r"אחרי חיבור האיברים: $=\frac{3k^2+k+2(3k+1)}{2}=\frac{3k^2+7k+2}{2}$"), 2,
         r"$-(k+1)+(2k+1)+(2k+2)=3k+2$ ולא $3k+1$.")])


def sets_item(fin, wrong3, finprompt, e1, e2, e3):
    return (rub(("חישוב $|A\\cap B|$ מתיאור האיברים", 2), ("חישוב הגודל הנדרש של הקבוצה השנייה ($A-B$ או $A\\times B$)", 2),
                ("הצבה בחזקות של 2 וכתיבת הביטוי הסופי", 2)),
            ["לבלבל בין $|P(X)|=2^{|X|}$ לבין $|X|$ עצמו.",
             "לחשב $|A\\times B|=|A|+|B|$ במקום המכפלה.",
             "לחשוב שהחיתוך גדול ממה שהוא: מספרים עם בסיסים ראשוניים שונים נבדלים."],
            [num(e1[0], e1[1], e1[2]), num(e2[0], e2[1], e2[2]), num(e3[0], e3[1], e3[2]),
             ch(finprompt, fin, *wrong3, explain="מחברים את שלושת הרכיבים לפי הנוסחה.")])


P_(2, "ב", sets_item(r"$20+2^{160000}+2^{380}$",
                      (r"$20+2^{800}+2^{380}$", r"$400+2^{160000}+2^{380}$", r"$20+2^{160000}+380$"),
                      "מהו הביטוי הסופי?",
                      (r"מהו $|A\cap B|$?", 20, r"$3^n5^m=2^{n'}5^{m'}$ רק כש-$n=n'=0$, כלומר $5^m$ עבור 20 ערכי $m$."),
                      (r"מהו $|A-B|$?", 380, r"$|A|-|A\cap B|=400-20=380$."),
                      (r"מהו $|A\times B|$ (המעריך של 2 ב-$|P(A\times B)|$)?", 160000, r"$400\cdot400=160000$.")))

_C1 = [r"נניח $A-C\not\subseteq B$, כלומר קיים $x\in A-C$ כך ש-$x\notin B$",
       r"$x\in A\wedge x\notin C\wedge x\notin B$",
       r"$x\in A-B\wedge x\notin C$",
       r"כלומר $A-B\not\subseteq C$, וזה ה-contrapositive שנדרש"]
_CW1 = (r"אם $A-B\not\subseteq C$, אז $A-C\not\subseteq B$", r"אם $A-C\subseteq B$, אז $A-B\subseteq C$",
        r"אם $A-B\subseteq C$, אז $A-C\not\subseteq B$")
_CR1 = r"אם $A-C\not\subseteq B$, אז $A-B\not\subseteq C$"
P_(2, "ג", contra_item(_CR1, _CW1, _C1, 2, r"$x\in A-B\wedge x\in C$"))

P_(3, "א", parity_item(3, 5))

_F_ = [
    num(r"מהו $f(3)$?", 5, r"$9\bmod6+\operatorname{lcm}(2,\gcd(2,3))=3+2=5$."),
    num(r"מהו $f(6)$?", 2, r"$36\bmod6+\operatorname{lcm}(2,\gcd(2,6))=0+2=2$."),
    num("כמה ערכים שונים מקבלת $f$?", 4, r"הערכים הם $3,6,5,6,3,2$, כלומר $\{2,3,5,6\}$."),
    ch(r"מהי הקבוצה $A$ שעבורה $f$ על?", r"$\{2,3,5,6\}$", r"$\{2,3,5\}$", r"$\{1,2,3,5,6\}$", r"$\{3,5,6\}$",
       explain="$f$ על בדיוק כש-$A$ היא תמונת $f$."),
]
put(3, "ב",
    rub(("חישוב $f(k)$ לכל $k$ בתחום, כולל החישוב מודולו 6", 4), ("איסוף הערכים השונים לקבוצה", 2),
        ("קביעה ש-$A$ שווה לתמונה של $f$ והנימוק ש-$f$ על", 2)),
    ["לטעות בחישוב $k^2\\bmod6$ (למשל $25\\bmod6=1$ ולא 5).",
     r"לשכוח ש-$\operatorname{lcm}(2,\gcd(2,k))$ הוא 2 לכל $k$.",
     "לכלול ב-$A$ ערכים שאינם מתקבלים (על דורשת טווח שווה לתמונה)."],
    _F_)

_R3 = [r"$R$ רפלקסיבי ולכן $(1,1),(2,2)\in R$, ו-$R$ סדר מלא ולכן $(1,2)\in R$ או $(2,1)\in R$",
       r"אם $(1,2)\in R$ אז ל-1 יש שתי תמונות $(1,1),(1,2)$, ואם $(2,1)\in R$ אז ל-2 יש שתי תמונות $(2,2),(2,1)$",
       r"בכל מקרה $R$ אינו פונקציה, והטענה נכונה"]
_R3S = [ch("מהי התשובה לטענה: אם $R$ סדר מלא על $A$ אז $R$ אינו פונקציה?", "הטענה נכונה", "הטענה אינה נכונה",
           explain="בכל סדר מלא יש איבר עם שתי תמונות."),
        ch(r"איזו תכונה של סדר מלא מבטיחה ש-$(1,2)\in R$ או $(2,1)\in R$?",
           "כל שני איברים ניתנים להשוואה", "רפלקסיביות", "אנטי-סימטריה", "טרנזיטיביות",
           explain="רפלקסיביות, אנטי-סימטריה וטרנזיטיביות מתקיימות גם ביחס הזהות, שאינו מכיל את אף אחד מהזוגות."),
        order("סדרו את שלבי ההוכחה.", _R3, "שתי העובדות על $R$ (רפלקסיביות והשוואה), שתי תמונות, מסקנה.")]
put(3, "ג",
    rub(("שימוש ברפלקסיביות: $(1,1),(2,2)\\in R$", 1), ("שימוש בהשוואה: $(1,2)\\in R$ או $(2,1)\\in R$", 1),
        ("הצבעה בשני המקרים על איבר עם שתי תמונות", 2), ("מסקנה: $R$ אינו פונקציה", 1)),
    ["להסיק מהכלה קטנה (כמה זוגות) בלי שני המקרים של ההשוואה.",
     "לחשוב שפונקציה חייבת להיות רפלקסיבית: פונקציה מאפשרת תמונה אחת לכל איבר בלבד.",
     "לבלבל בין סדר מלא לסדר חלקי: במלא כל זוג ניתן להשוואה."],
    _R3S)

def card_item(inside, outs):
    return (rub(("שימוש בהכלה $(0,1)\\subseteq A\\subseteq\\mathbb{R}$", 2), ("הוכחת שתי אי-השוויונות בעזרת פונקציות חד-חד-ערכיות", 2),
                ("קנטור-ברנשטיין והמסקנה $|A|=\\mathfrak{c}$", 1)),
            ["לחשוב שאיחוד של שני קטעים הוא בן-מנייה או שהעוצמה שלו קטנה מ-$\\mathfrak{c}$.",
             "להראות רק חסם אחד (למטה או למעלה) בלי השני.",
             "לבלבל בין $\\aleph_0$ לבין עוצמת הרצף $\\mathfrak{c}$."],
            [ch("מהי עוצמת $A$?", r"$\mathfrak{c}$ (עוצמת הרצף)", r"$\aleph_0$", "סופית", r"$2^{\mathfrak{c}}$",
                explain="$A$ מכילה קטע ומוכלת ב-$\\mathbb{R}$."),
             ch("איזה קטע מוכל ב-$A$?", inside, *outs,
                explain="רק הקטע הראשון מוכל כולו ב-$A$; בשאר יש נקודה שאינה ב-$A$."),
             ch("באיזו שיטה משתמש הפתרון?", r"חסם מלמטה ומלמעלה: $|(0,1)|\le|A|\le|\mathbb{R}|$ וקנטור-ברנשטיין",
                "בנייה של התאמה מפורשת בין $A$ ל-$\\mathbb{N}$", "טיעון אלכסוני", "הוכחה שקבוצה בת-מנייה",
                explain="שתי פונקציות חד-חד-ערכיות לשני הכיוונים נותנות שוויון עוצמות.")])


P_(4, "א", card_item(r"$(0,1)$", (r"$(1,3)$", r"$(2,3)$", r"$[1,4)$")))


def count_item(form):
    if form == 1:
        s1 = [num(r"כמה בחירות יש לאיבר היחיד של $B$ מתוך האי-זוגיים, כש-$n=4$?", 5, "$n+1=5$ איברים אי-זוגיים."),
              num(r"כמה בחירות יש לשאר $B$ (תת-קבוצה של הזוגיים) כש-$n=4$?", 16, "$2^n=2^4=16$."),
              num(r"כמה תת-קבוצות $B$ מקיימות את תנאי (1) כש-$n=4$?", 80, "$5\\cdot16=80=(n+1)2^n$ (הוכח בבדיקת כל 512 הקבוצות)."),
              num(r"כמה תת-קבוצות $B$ מקיימות את תנאי (2) כש-$n=4$?", 501, "$2^9-2-9=501=2^{2n+1}-2n-3$ (הוכח בבדיקה).")]
    else:
        s1 = [num(r"כמה בחירות יש לאיבר היחיד של $B$ מתוך הזוגיים, כש-$n=4$?", 4, "$n=4$ איברים זוגיים."),
              num(r"כמה בחירות יש לשאר $B$ (תת-קבוצה של האי-זוגיים) כש-$n=4$?", 32, "$2^{n+1}=2^5=32$."),
              num(r"כמה תת-קבוצות $B$ מקיימות את תנאי (1) כש-$n=4$?", 128, "$4\\cdot32=128=n\\cdot2^{n+1}$ (הוכח בבדיקת כל 512 הקבוצות)."),
              num(r"כמה תת-קבוצות $B$ מקיימות את תנאי (2) כש-$n=4$?", 501, "$2^9-2-9=501=2^{2n+1}-2n-3$ (הוכח בבדיקה).")]
    return (rub(("תנאי (1): תיאור $B=\\{x\\}\\cup C$ וספירת הבחירות", 3), ("תנאי (2): כל תתי-הקבוצות פחות הריקה, $A$ וקבוצות בגודל 1", 2)),
            ["לשכוח שבתנאי (1) יש בחירה נפרדת לאיבר ה-$x$ ולשאר $B$.",
             r"בתנאי (2) להחסיר רק את $\emptyset$ ו-$A$ ולשכוח את הקבוצות בגודל 1.",
             "לבלבל בין $n$ לבין $|A|=2n+1$."], s1)


P_(4, "ב", count_item(1))

# ================= FORM 2 =================
P_(5, "א", normal_form_item("dnf"))
P_(5, "ב", euclid_item(r"מהו $\operatorname{lcm}(55,-40)$?", r"$\frac{|55\cdot(-40)|}{5}=440$."))
P_(5, "ג", fermat_item(6, 64, r"36^{15}", r"8^{60}", 47, 18))

_IND2 = [r"$(k+3)+\cdots+(2k+4)=\big[(k+2)+\cdots+(2k+2)\big]-(k+2)+(2k+3)+(2k+4)$",
         r"לפי הנחת האינדוקציה: $=\frac{(k+1)(3k+4)}{2}-(k+2)+(2k+3)+(2k+4)$",
         r"אחרי חיבור האיברים: $=\frac{(k+1)(3k+4)}{2}+3k+5=\frac{3k^2+13k+14}{2}$",
         r"פירוק: $=\frac{(k+2)(3k+7)}{2}$, כלומר $P(k+1)$ נכון"]
put(6, "א",
    rub(("בסיס: בדיקת $P(1)$ בשני האגפים", 3),
        ("ניסוח הנחת האינדוקציה $P(k)$ וההוכחה הנדרשת $P(k+1)$", 3),
        ("כתיבת הסכום של $P(k+1)$ באמצעות הסכום של $P(k)$ (הסרת האיבר הראשון והוספת שני האיברים האחרונים)", 5),
        ("הצבת הנחת האינדוקציה והשוואה אלגברית לאגף ימין", 4),
        ("מסקנה לפי עקרון האינדוקציה", 1)),
    ["לשכוח שמחליפים איבר ראשון: בסכום מ-$k+3$ עד $2k+4$ נעלם $k+2$ ונוספים שני איברים.",
     "לבלבל בין מספר האיברים בסכום (שגדל ב-1) לבין ערך האיבר האחרון (שגדל ב-2).",
     "להשתמש ב-$P(k+1)$ בתוך ההוכחה שלו."],
    [num(r"מהו האגף השמאלי $(n+2)+\cdots+(2n+2)$ עבור $n=3$?", 26, r"$5+6+7+8=26=\frac{4\cdot13}{2}$."),
     ch(r"איך עוברים מהסכום $(k+2)+\cdots+(2k+2)$ אל הסכום $(k+3)+\cdots+(2k+4)$?",
        r"מסירים את $(k+2)$ ומוסיפים את $(2k+3)$ ואת $(2k+4)$",
        r"מסירים את $(k+2)$ ומוסיפים רק את $(2k+4)$", r"מוסיפים את $(2k+3)$ ואת $(2k+4)$ בלי להסיר דבר",
        r"מסירים את $(k+1)$ ואת $(k+2)$ ומוסיפים את $(2k+4)$",
        explain=r"בסכום החדש הראשון הוא $k+3$ והאחרון $2k+4$, ולכן $(k+2)$ יוצא ושני האיברים החדשים נכנסים."),
     order("סדרו את שלבי הצעד.", _IND2, "פירוק הסכום, הנחה, חיבור, פירוק לגורמים."),
     bug("בגרסה הבאה של הצעד שורה אחת שגויה. מצאו אותה.",
         mutate(_IND2, 2, r"אחרי חיבור האיברים: $=\frac{(k+1)(3k+4)}{2}+3k+4=\frac{3k^2+13k+12}{2}$"), 2,
         r"$-(k+2)+(2k+3)+(2k+4)=3k+5$ ולא $3k+4$.")])
P_(6, "ב", sets_item(r"$870+2^{810000}+2^{30}$",
                      (r"$870+2^{90000}+2^{30}$", r"$870+2^{810000}+30$", r"$900+2^{810000}+2^{30}$"),
                      "מהו הביטוי הסופי?",
                      (r"מהו $|A\cap B|$?", 30, r"$3^n7^m=3^{n'}5^{m'}$ רק כש-$m=m'=0$, כלומר $3^n$ עבור 30 ערכי $n$."),
                      (r"מהו $|A-B|$?", 870, r"$|A|-|A\cap B|=900-30=870$."),
                      (r"מהו $|A\times B|$ (המעריך של 2 ב-$|P(A\times B)|$)?", 810000, r"$900\cdot900=810000$.")))

_C2 = [r"נניח $A-C\not\subseteq B$, כלומר קיים $x\in A-C$ כך ש-$x\notin B$",
       r"$x\in A\wedge x\notin C\wedge x\notin B$",
       r"$x\in A-B\wedge x\notin C$",
       r"כלומר $A-B\not\subseteq C$, וזה ה-contrapositive שנדרש"]
P_(6, "ג", contra_item(_CR1, _CW1, _C2, 2, r"$x\in A-B\wedge x\in C$"))

P_(7, "א", parity_item(3, 7))
put(7, "ב", rub(("חישוב $f(k)$ לכל $k$ בתחום, כולל החישוב מודולו 6", 4), ("איסוף הערכים השונים לקבוצה", 2),
                ("קביעה ש-$A$ שווה לתמונה של $f$ והנימוק ש-$f$ על", 2)),
    ["לטעות בחישוב $k^2\\bmod6$ (למשל $25\\bmod6=1$ ולא 5).",
     r"לשכוח ש-$\operatorname{lcm}(2,\gcd(2,k))$ הוא 2 לכל $k$.",
     "לכלול ב-$A$ ערכים שאינם מתקבלים (על דורשת טווח שווה לתמונה)."],
    [num(r"מהו $f(7)$?", 3, r"$49\bmod6+\operatorname{lcm}(2,\gcd(2,7))=1+2=3$."),
     num(r"מהו $f(6)$?", 2, r"$36\bmod6+\operatorname{lcm}(2,\gcd(2,6))=0+2=2$."),
     num("כמה ערכים שונים מקבלת $f$?", 4, r"הערכים הם $3,6,5,6,3,2,3$, כלומר $\{2,3,5,6\}$."),
     ch(r"מהי הקבוצה $A$ שעבורה $f$ על?", r"$\{2,3,5,6\}$", r"$\{2,3,5\}$", r"$\{1,2,3,5,6\}$", r"$\{3,5,6\}$",
        explain="$f$ על בדיוק כש-$A$ היא תמונת $f$.")])
put(7, "ג", rub(("שימוש ברפלקסיביות: $(1,1),(2,2)\\in R$", 1), ("שימוש בהשוואה: $(1,2)\\in R$ או $(2,1)\\in R$", 1),
                ("הצבעה בשני המקרים על איבר עם שתי תמונות", 2), ("מסקנה: $R$ אינו פונקציה", 1)),
    ["להסיק מהכלה קטנה (כמה זוגות) בלי שני המקרים של ההשוואה.",
     "לחשוב שפונקציה חייבת להיות רפלקסיבית: פונקציה מאפשרת תמונה אחת לכל איבר בלבד.",
     "לבלבל בין סדר מלא לסדר חלקי: במלא כל זוג ניתן להשוואה."],
    _R3S)
P_(8, "א", card_item(r"$(0,1)$", (r"$(-3,-1)$", r"$(-2,-1)$", r"$(-6,-4)$")))
P_(8, "ב", count_item(2))


exam = {
    "examCode": "22A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ב, מועד א (25.01.2022), שתי גרסאות',
    "year": 2022,
    "examDate": "25.01.2022",
    "sourceFile": "22A-A exam with solution, pp.1-16 (form 1 = Q1-Q4, form 2 = Q5-Q8)",
    "solutionFile": "22A-A handwritten solution (author unknown) with typed definitions, pp.2-15",
    "contexts": {},
    "questions": questions,
}
for _q in questions:
    for _k in ("question", "solution"):
        if _k in _q:
            _q[_k] = _q[_k].replace('\\"', '"')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
