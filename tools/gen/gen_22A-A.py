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

add(H(6, "ב", "computation", "sets_power_set", 6,
      V2 + r"יהיו הקבוצות $A=\{3^n\cdot7^m:\ m,n\in\{0,1,2,\ldots,29\}\}$ ו-$B=\{3^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,29\}\}$."
      "\n"
      r"חשבו את: $|A-B|+|P(A\times B)|+|P(A\cap B)|$.",
      "key-disagrees: the key writes |A|*|B| = 300*300 = 90000, giving 870 + 2^90000 + 2^30; with |A|=|B|=900 a script gives 870 + 2^810000 + 2^30"))

add(Q(6, "ג", "proof", "sets_power_set", 8, V2 + Q2C_Q, Q2C_S))

add(H(7, "א", "proof", "equivalence_relations", 17,
      V2 + r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$ מתקיים "
      r"$xRy\iff3x+7y$ הוא מספר זוגי."
      "\n"
      r"הוכיחו ש-$R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי?",
      "no-key"))

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
