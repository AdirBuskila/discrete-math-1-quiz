# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-B.json -- discrete math 1 (20067), semester A 5782, moed B (24.02.2022).
The paper has TWO FORMS ("גרסה 1" / "גרסה 2") of every question. Form 1 is transcribed as Q1-Q4, form 2 as Q5-Q8
(num = form-1 num + 4, "(גרסה 2)" in the stem). The handwritten key (several ink colours, author unknown) is
student-solution. Where the key says "same as form 1" and the printed text is identical, the form-1 solution is reused.
Checks: tools/verify/22A-B/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_22A-B.py
 - Q1b (b1+b2) and Q3a (sub-questions) are ONE item each."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-B.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


def H(num, part, kind, topic, points, question, reason):
    return {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
            "question": question, "hold": reason}


V2 = "(גרסה 2)\n"

# Form 2 Q3a (stored Q7a): the key covers form 1 only, so this is a solver write-up (verified in verify.py).
SOL7A_V2 = (r"(המפתח פותר רק את גרסה 1; הפתרון כאן נכתב לפי המספרים של גרסה 2 ונבדק בסקריפט.)"
            "\n"
            r"**$R$ רפלקסיבי:** לכל $x\in\mathbb{Z}$: $3x+7x=10x=2\cdot5x$ זוגי, ולכן $xRx$."
            "\n"
            r"**$R$ סימטרי:** יהיו $x,y\in\mathbb{Z}$ עם $xRy$, כלומר $3x+7y$ זוגי. "
            r"$(3x+7y)+(3y+7x)=10x+10y$ זוגי, ולכן $3y+7x=(10x+10y)-(3x+7y)$ הוא הפרש של שני מספרים זוגיים, כלומר זוגי, ולכן $yRx$."
            "\n"
            r"**$R$ טרנזיטיבי:** יהיו $x,y,z\in\mathbb{Z}$ עם $xRy$ וגם $yRz$, כלומר $3x+7y$ ו-$3y+7z$ זוגיים. "
            r"אז $3x+7z=\big((3x+7y)+(3y+7z)\big)-10y$ הוא הפרש של מספרים זוגיים, ולכן זוגי, כלומר $xRz$."
            "\n"
            r"לכן $R$ הוא יחס שקילות על $\mathbb{Z}$."
            "\n"
            r"$[0]=\{x\in\mathbb{Z}:\ xR0\}=\{x\in\mathbb{Z}:\ 2\mid3x\}=\{x\in\mathbb{Z}:\ 2\mid x\}=\{2k:\ k\in\mathbb{Z}\}$ (כי $2\nmid3$)."
            "\n"
            r"$[1]=\{x\in\mathbb{Z}:\ xR1\}=\{x\in\mathbb{Z}:\ 2\mid(3x+7)\}=\{x\in\mathbb{Z}:\ 2\nmid3x\}=\{x\in\mathbb{Z}:\ 2\nmid x\}=\{2k+1:\ k\in\mathbb{Z}\}$."
            "\n"
            r"$[0]\cup[1]=\mathbb{Z}$, ולכן $\mathbb{Z}/R=\{[0],[1]\}$."
            "\n"
            r"**האם $R$ יחס סדר חלקי?** לא. $0R2$ (כי $3\cdot0+7\cdot2=14$ זוגי) וגם $2R0$ (כי $3\cdot2+7\cdot0=6$ זוגי), "
            r"אבל $0\ne2$. לכן $R$ אינו אנטי-סימטרי, ולכן אינו יחס סדר חלקי.")

# ---------------- shared pieces ----------------
Q1A_DEF = ("הגדרה: אם לפסוקים $A,B$ יש אותה טבלת אמת, אז הם נקראים שקולים לוגית.\n")
Q1B2_Q = r"יהיו $a,b\in\mathbb{N}$ כך ש: $2<b<a$. חשבו את $\gcd(\operatorname{lcm}(a,b),\gcd(a,b))$."
Q1B2_S = (r"נסמן $d=\gcd(a,b)$ ו-$m=\operatorname{lcm}(a,b)$. אז $\gcd(d,m)=d$ כי: "
          r"$d\mid m\Leftarrow d\mid a\wedge a\mid m$, ו-$d\mid d$.")

Q2C_Q = ("נסחו את ה-contrapositive של הטענה הבאה:\n"
         r"\"יהיו $A,B,C$ קבוצות לא ריקות. אם $A\subseteq B\cup C$, אז $A-B\subseteq C$\"."
         "\nהוכיחו את הטענה.")
Q2C_S = (r"ה-contrapositive הוא: אם $A-B\not\subseteq C$, אז $A\not\subseteq B\cup C$."
         "\n"
         r"**הוכחת הטענה** (הוכחת ה-contrapositive):"
         "\n"
         r"$A-B\not\subseteq C\Rightarrow\exists x\in A-B\ \wedge\ x\notin C\Rightarrow x\in A\wedge x\notin B\wedge x\notin C"
         r"\Rightarrow x\in A\wedge x\notin B\cup C\Rightarrow A\not\subseteq B\cup C$."
         "\n"
         r"**דרך שנייה (בשלילה):** נניח בשלילה ש-$A\subseteq B\cup C$ וגם $A-B\not\subseteq C$. "
         r"אז $\exists x\in A-B\ \wedge\ x\notin C\Rightarrow x\in A\wedge x\notin B\wedge x\notin C"
         r"\Rightarrow x\in A\wedge x\notin B\cup C\Rightarrow A\not\subseteq B\cup C$, סתירה לנתון.")

Q3B_Q = (r"הפונקציה $f:\{1,2,3,4,5,6,7\}\to\{2,3,5,6\}$ מוגדרת לפי הכלל $f(k)=k^2\pmod 6+\operatorname{lcm}(2,\gcd(2,k))$ "
         r"לכל $k\in\{1,2,3,4,5,6,7\}$."
         "\n"
         r"מצאו קבוצה $A\subseteq\{1,2,3,4,5,6,7\}$ כך ש-$f:A\to\{2,3,5,6\}$ היא פונקציה הפיכה ומצאו את $f^{-1}$.")
Q3B_S = ("חישוב הערכים:\n"
         "```\n"
         "f(1) = 1 (mod 6) + lcm(2, gcd(2,1)) = 1 + 2 = 3\n"
         "f(2) = 4 (mod 6) + lcm(2, gcd(2,2)) = 4 + 2 = 6\n"
         "f(3) = 9 (mod 6) + lcm(2, gcd(2,3)) = 3 + 2 = 5\n"
         "f(4) = 16 (mod 6) + lcm(2, gcd(2,4)) = 4 + 2 = 6\n"
         "f(5) = 25 (mod 6) + lcm(2, gcd(2,5)) = 1 + 2 = 3\n"
         "f(6) = 36 (mod 6) + lcm(2, gcd(2,6)) = 0 + 2 = 2\n"
         "f(7) = 49 (mod 6) + lcm(2, gcd(2,7)) = 1 + 2 = 3\n"
         "```\n"
         r"לדוגמה $A=\{1,2,3,6\}$: $1\mapsto3,\ 2\mapsto6,\ 3\mapsto5,\ 6\mapsto2$ (התאמה חח\"ע ועל)."
         "\n"
         r"$f^{-1}(2)=6,\ f^{-1}(3)=1,\ f^{-1}(5)=3,\ f^{-1}(6)=2$.").replace('חח\\"ע', "חד-חד-ערכית")

questions = []
add = questions.append

# ======================= FORM 1 =======================
add(Q(1, "א", "computation", "logic_propositional", 14,
      r"הגדירו את המונח: שקילות לוגית. בדקו על ידי טבלת אמת את נכונות הטענה: "
      r"$(p\wedge q)\to r\equiv p\to(\neg q\vee r)$.",
      Q1A_DEF + "טבלת אמת:\n"
      "```\n"
      "p q r | p∧q | (p∧q)→r | ¬q∨r | p→(¬q∨r)\n"
      "T T T |  T  |    T    |   T   |     T\n"
      "T T F |  T  |    F    |   F   |     F\n"
      "T F T |  F  |    T    |   T   |     T\n"
      "T F F |  F  |    T    |   T   |     T\n"
      "F T T |  F  |    T    |   T   |     T\n"
      "F T F |  F  |    T    |   F   |     T\n"
      "F F T |  F  |    T    |   T   |     T\n"
      "F F F |  F  |    T    |   T   |     T\n"
      "```\n"
      "העמודות (p∧q)→r ו-p→(¬q∨r) זהות. מסקנה: הפסוקים שקולים לוגית."))

add(Q(1, "ב", "computation", "number_theory_gcd", 11,
      r"(1) בעזרת האלגוריתם המורחב של EUCLID, מצאו $x_1,y_1,x_2,y_2\in\mathbb{Z}$ כך ש:"
      "\n"
      r"$\gcd(68,84)=68x_1+84y_1$"
      "\n"
      r"$\gcd(-68,-84)=(-68)x_2+(-84)y_2$"
      "\n"
      "(2) " + Q1B2_Q,
      r"(1) $\gcd(-68,-84)=\gcd(68,84)=\gcd(84,68)$. נריץ את האלגוריתם על $84,68$ "
      r"(עמודות: $a,\ b,\ \lfloor a/b\rfloor,\ d,\ x=y',\ y=x'-y'\lfloor a/b\rfloor$):"
      "\n"
      "```\n"
      "a    b    [a/b]   d    x     y\n"
      "84   68   1       4    -4    1-(-4)*1 = 5\n"
      "68   16   4       4    1     0-1*4 = -4\n"
      "16   4    4       4    0     1-0*4 = 1\n"
      "4    0    -       4    1     0\n"
      "```\n"
      r"$\gcd(84,68)=84\cdot(-4)+68\cdot5$, כלומר $x_1=5,\ y_1=-4$."
      "\n"
      r"$\gcd(-68,-84)=(-68)\cdot(-5)+(-84)\cdot4$, כלומר $x_2=-5,\ y_2=4$."
      "\n"
      "(2) " + Q1B2_S))

add(Q(1, "ג", "proof", "modular_fermat_wilson", 5,
      r"הראו ש: $40<\gcd\left(25^{20}+40!,\ 8^{80}+40\right)$.",
      r"נסמן $a=25^{20}+40!$ ו-$b=8^{80}+40$."
      "\n"
      r"$b=8^{80}+40=64^{40}+40=(64^{41-1}-1)+41$. מכיוון ש-$41\nmid64$ ו-41 ראשוני, לפי פרמה $41\mid64^{41-1}-1$, "
      r"ולכן $41\mid b$."
      "\n"
      r"$a=25^{20}+40!=(5^{41-1}-1)+((41-1)!+1)$. מכיוון ש-$41\nmid5$ ו-41 ראשוני, לפי פרמה $41\mid5^{41-1}-1$; "
      r"ומכיוון ש-41 ראשוני, לפי וילסון $41\mid(41-1)!+1$. לכן $41\mid a$."
      "\n"
      r"מסקנה: $41\mid a\wedge41\mid b\Rightarrow41\le\gcd(a,b)$, ולכן $40<41\le\gcd(a,b)$."))

add(Q(2, "א", "proof", "induction", 16,
      r"הוכיחו באינדוקציה מתמטית שלכל $n\in\mathbb{N},\ 1\le n$, מתקיים: $n^2\le5^n$.",
      r"**I. בסיס:** $P(1)$: $1^2\le5^1\iff1\le5\Rightarrow P(1)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=\text{TRUE}$ עבור $1\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ k^2\le5^k$ $\qquad$ $P(k+1):\ (k+1)^2\le5^{k+1}$"
      "\n"
      r"$$(k+1)^2=k^2+2k+1\le k^2+2\cdot k^2+k^2=4k^2\le5k^2\le5\cdot5^k=5^{k+1}$$"
      "\n"
      r"$\Rightarrow P(k+1)=\text{TRUE}$."
      "\n"
      r"**III. מסקנה:** מ-I ו-II, לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$."))

add(Q(2, "ב", "computation", "sets_power_set", 6,
      r"יהיו הקבוצות $A=\{3^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,10\}\}$ ו-$B=\{5^m:\ m\in\{1,2,\ldots,10\}\}$."
      "\n"
      r"חשבו את: $|A-B|+|P(A\times B)|+|P(A\cup B)|$.",
      r"לכל $m\in\{1,\ldots,10\}$: $5^m=3^0\cdot5^m\in A$, ולכן $B\subset A$."
      "\n"
      r"$|A-B|=|A|-|B|=121-10=111$."
      "\n"
      r"$|P(A\times B)|=2^{|A\times B|}=2^{|A|\cdot|B|}=2^{121\cdot10}=2^{1210}$."
      "\n"
      r"$|P(A\cup B)|=|P(A)|=2^{|A|}=2^{121}$."
      "\n"
      r"מסקנה: $$2^{121}+2^{1210}+111$$"))

add(Q(2, "ג", "proof", "sets_power_set", 8, Q2C_Q, Q2C_S))

add(Q(3, "א", "proof", "equivalence_relations", 17,
      r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$, מתקיים "
      r"$xRy\iff9x+5y$ הוא מספר זוגי."
      "\n"
      r"הוכיחו ש-$R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי?",
      r"**$R$ רפלקסיבי:** לכל $x\in\mathbb{Z}$: $xRx\iff9x+5x=14x$ הוא זוגי (נכון)."
      "\n"
      r"**$R$ סימטרי:** לכל $x,y\in\mathbb{Z}$, אם $xRy$ אז $yRx$. $2k=9x+5y$ עבור $k\in\mathbb{Z}$ ($xRy$). "
      r"נראה: $(9x+5y)+(9y+5x)=14x+14y$ זוגי; סכום של שני מספרים הוא זוגי, ואחד מהם זוגי, לכן גם $9y+5x$ זוגי, כלומר $yRx$."
      "\n"
      r"**$R$ טרנזיטיבי:** לכל $x,y,z\in\mathbb{Z}$: $xRy$ וגם $yRz$. $9x+5y$ זוגי ו-$9y+5z$ זוגי, ולכן $(9x+5z)+14y$ זוגי, "
      r"כלומר $9x+5z$ זוגי, כלומר $xRz$."
      "\n"
      r"לכן $R$ הוא יחס שקילות על $\mathbb{Z}$."
      "\n"
      r"$[0]=\{x:\ x\in\mathbb{Z}\wedge xR0\}=\{x:\ x\in\mathbb{Z}\wedge2\mid9x\}=\{x:\ x\in\mathbb{Z}\wedge2\mid x\}=\{2k:\ k\in\mathbb{Z}\}$ "
      r"(כי $2\nmid9$)"
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}\wedge xR1\}=\{x:\ x\in\mathbb{Z}\wedge2\mid(9x+5)\}=\{x:\ x\in\mathbb{Z}\wedge2\nmid9x\}"
      r"=\{x:\ x\in\mathbb{Z}\wedge2\nmid x\}=\{2k+1:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[0]\cup[1]=\mathbb{Z}$, ולכן $\mathbb{Z}/R=\{[0],[1]\}$."
      "\n"
      r"(המפתח אינו עונה על השאלה האחרונה. בדיקה בסקריפט: $R$ אינו יחס סדר חלקי, כי $0R2$ וגם $2R0$ אך $0\ne2$, "
      r"ולכן $R$ אינו אנטי-סימטרי.)"))

add(Q(3, "ב", "computation", "functions", 8, Q3B_Q, Q3B_S))

add(Q(3, "ג", "proof", "relations_properties", 5,
      r"תהיינה $A=\{1,2,3,4,5\}$ ו-$R\subseteq A\times A$. הוכיחו או הפריכו: "
      r"אם $R$ הוא יחס רפלקסיבי, סימטרי וגם אנטי-סימטרי, אז $R$ הוא יחס שקילות.",
      r"מכיוון ש-$R\subseteq A^2$ רפלקסיבי, לכל $x\in A$ מתקיים $(x,x)\in R$."
      "\n"
      r"נניח ש-$(x,y)\in R$ כך ש: $x\ne y$. מכיוון ש-$R$ סימטרי, $(y,x)\in R$. אז $(x,y),(y,x)\in R$ ו-$x=y$ "
      r"(כי $R$ אנטי-סימטרי), סתירה."
      "\n"
      r"מסקנה: $R=\{(x,x):\ x\in A\}$, ולכן $R$ הוא יחס שקילות. הטענה נכונה."))

add(Q(4, "א", "computation", "cardinality_sets", 5,
      r"חשבו את העוצמה של הקבוצה $S=\mathbb{Q}\cap[3,8)$.",
      r"$S\subseteq\mathbb{Q}\Rightarrow|S|\le|\mathbb{Q}|$."
      "\n"
      r"הקבוצה $B=\left\{3+\frac12,\ 3+\frac1{2^2},\ \ldots,\ 3+\frac1{2^n},\ \ldots\right\}$ היא תת-קבוצה אינסופית של $S$, ו-$|B|=|\mathbb{N}|$."
      "\n"
      r"מכאן: $|\mathbb{N}|=|B|\le|S|\le|\mathbb{Q}|=|\mathbb{N}|\Rightarrow|S|=|\mathbb{N}|$."))

add(Q(4, "ב", "computation", "sets_power_set", 5,
      r"תהי $A=\{1,2,3,\ldots,2n+1\}$, כאשר $3<n\in\mathbb{N}$. "
      r"חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאי $B\cup\{1,3,5,7,\ldots,2n+1\}=A$.",
      r"$B\cup\{1,3,5,\ldots,2n+1\}=A\iff B=\{2,4,6,\ldots,2n\}\cup C\ \wedge\ C\subseteq\{1,3,\ldots,2n+1\}$."
      "\n"
      r"לכן מספר ה-$B$-ים שווה למספר ה-$C$-ים: $|P(\{1,3,\ldots,2n+1\})|=2^{|\{1,3,\ldots,2n+1\}|}=2^{n+1}$."))

# ======================= FORM 2 =======================
add(Q(5, "א", "computation", "logic_propositional", 14,
      V2 + r"הגדירו את המונח: שקילות לוגית. בדקו על ידי טבלת אמת את נכונות הטענה: "
      r"$(p\to r)\wedge(q\to r)\equiv(p\vee q)\to r$.",
      Q1A_DEF + "טבלת אמת:\n"
      "```\n"
      "p q r | p→r | q→r | (p→r)∧(q→r) | p∨q | (p∨q)→r\n"
      "T T T |  T  |  T  |      T       |  T  |    T\n"
      "T T F |  F  |  F  |      F       |  T  |    F\n"
      "T F T |  T  |  T  |      T       |  T  |    T\n"
      "T F F |  F  |  T  |      F       |  T  |    F\n"
      "F T T |  T  |  T  |      T       |  T  |    T\n"
      "F T F |  T  |  F  |      F       |  T  |    F\n"
      "F F T |  T  |  T  |      T       |  F  |    T\n"
      "F F F |  T  |  T  |      T       |  F  |    T\n"
      "```\n"
      "העמודות (p→r)∧(q→r) ו-(p∨q)→r זהות. מסקנה: הפסוקים שקולים לוגית."))

add(Q(5, "ב", "computation", "number_theory_gcd", 11,
      V2 + r"(1) בעזרת האלגוריתם המורחב של EUCLID, מצאו $x_1,y_1,x_2,y_2\in\mathbb{Z}$ כך ש:"
      "\n"
      r"$\gcd(84,68)=84x_1+68y_1$"
      "\n"
      r"$\gcd(-84,-68)=(-84)x_2+(-68)y_2$"
      "\n"
      "(2) " + Q1B2_Q,
      r"(1) הפתרון דומה לגרסה 1. נריץ את האלגוריתם על $84,68$:"
      "\n"
      "```\n"
      "a    b    [a/b]   d    x     y\n"
      "84   68   1       4    -4    1-(-4)*1 = 5\n"
      "68   16   4       4    1     0-1*4 = -4\n"
      "16   4    4       4    0     1-0*4 = 1\n"
      "4    0    -       4    1     0\n"
      "```\n"
      r"$\gcd(84,68)=84\cdot(-4)+68\cdot5$, כלומר $x_1=-4,\ y_1=5$."
      "\n"
      r"$\gcd(-84,-68)=(-84)\cdot4+(-68)\cdot(-5)$, כלומר $x_2=4,\ y_2=-5$."
      "\n"
      "(2) " + Q1B2_S))

add(Q(5, "ג", "proof", "modular_fermat_wilson", 5,
      V2 + r"הראו ש: $40<\gcd\left(36^{20}+40!,\ 10^{80}+40\right)$.",
      r"נסמן $a=36^{20}+40!$ ו-$b=10^{80}+40$."
      "\n"
      r"$a=6^{40}+40!=(6^{41-1}-1)+((41-1)!+1)$. מכיוון ש-$41\nmid6$ ו-41 ראשוני, לפי פרמה $41\mid6^{41-1}-1$; "
      r"ומכיוון ש-41 ראשוני, לפי וילסון $41\mid(41-1)!+1$. לכן $41\mid a$."
      "\n"
      r"$b=10^{80}+40=(100^{41-1}-1)+41$. מכיוון ש-$41\nmid100$ ו-41 ראשוני, לפי פרמה $41\mid100^{41-1}-1$, ולכן $41\mid b$."
      "\n"
      r"מסקנה: $41\mid a\wedge41\mid b\Rightarrow41\le\gcd(a,b)$, ולכן $40<41\le\gcd(a,b)$."))

add(Q(6, "א", "proof", "induction", 16,
      V2 + r"הוכיחו באינדוקציה מתמטית שלכל $n\in\mathbb{N},\ 1\le n$, מתקיים: $n^2\le4^n$.",
      r"**I. בסיס:** כמו בגרסה 1: $P(1)$: $1^2\le4^1\iff1\le4\Rightarrow P(1)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k):\ k^2\le4^k$, $P(k+1):\ (k+1)^2\le4^{k+1}$."
      "\n"
      r"$$(k+1)^2=k^2+2k+1\le k^2+2\cdot k^2+k^2=4k^2\le4\cdot4^k=4^{k+1}$$"
      "\n"
      r"**III. מסקנה:** מ-I ו-II, לכל $1\le n\in\mathbb{N}$ מתקיים $P(n)=\text{TRUE}$."))

add(Q(6, "ב", "computation", "sets_power_set", 6,
      V2 + r"יהיו הקבוצות $A=\{3^n\cdot5^m:\ m,n\in\{0,1,2,\ldots,10\}\}$ ו-$B=\{3^n:\ n\in\{1,2,\ldots,10\}\}$."
      "\n"
      r"חשבו את: $|A\cup B|+|P(A\times B)|+|P(A-B)|$.",
      r"**הפתרון הרשמי עם תיקון $|P(A-B)|=2^{111}$ (ולא $111$):** הפתרון הרשמי מחשב נכון $|A-B|=111$, אבל בשורת הסיכום מציב $111$ במקום "
      r"$|P(A-B)|=2^{|A-B|}=2^{111}$ ומקבל $232+2^{1210}$. התשובה המתוקנת היא $121+2^{1210}+2^{111}$ (נבדק בסקריפט)."
      "\n"
      r"לכל $n\in\{1,\ldots,10\}$: $3^n=3^n\cdot5^0\in A$, ולכן $B\subseteq A$."
      "\n"
      r"$A\cup B=A\Rightarrow|A\cup B|=|A|=11\cdot11=121$."
      "\n"
      r"$|P(A\times B)|=2^{|A\times B|}=2^{|A|\cdot|B|}=2^{121\cdot10}=2^{1210}$."
      "\n"
      r"$|A-B|=|A|-|B|=121-10=111$ (כי $B\subseteq A$), ולכן $|P(A-B)|=2^{111}$."
      "\n"
      r"מסקנה: $$121+2^{1210}+2^{111}$$",
      solutionSource="solved", confidence="high"))

add(Q(6, "ג", "proof", "sets_power_set", 8, V2 + Q2C_Q, Q2C_S))

add(Q(7, "א", "proof", "equivalence_relations", 17,
      V2 + r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$, מתקיים "
      r"$xRy\iff3x+7y$ הוא מספר זוגי."
      "\n"
      r"הוכיחו ש-$R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי?",
      SOL7A_V2, solutionSource="solved", confidence="high"))

add(Q(7, "ב", "computation", "functions", 8, V2 + Q3B_Q, Q3B_S))

add(Q(7, "ג", "proof", "relations_properties", 5,
      V2 + r"תהיינה $A=\{1,2,3,4,5\}$ ו-$R\subseteq A\times A$. הוכיחו או הפריכו: "
      r"אם $R$ הוא יחס רפלקסיבי, סימטרי וגם אנטי-סימטרי, אז $R$ הוא יחס סדר חלקי.",
      r"הפתרון דומה לגרסה 1: מכיוון ש-$R$ רפלקסיבי, $(x,x)\in R$ לכל $x\in A$. אם $(x,y)\in R$ עם $x\ne y$, אז מסימטריה "
      r"$(y,x)\in R$, ומאנטי-סימטריה $x=y$, סתירה."
      "\n"
      r"לכן $R=\{(x,x):\ x\in A\}$, ולכן $R$ הוא יחס סדר חלקי. הטענה נכונה."))

add(Q(8, "א", "computation", "cardinality_sets", 5,
      V2 + r"חשבו את העוצמה של הקבוצה $S=(5,9]\cap\mathbb{Q}$.",
      r"$S\subseteq\mathbb{Q}\Rightarrow|S|\le|\mathbb{Q}|=|\mathbb{N}|$."
      "\n"
      r"הקבוצה $B=\left\{5+\frac12,\ 5+\frac1{2^2},\ \ldots,\ 5+\frac1{2^n},\ \ldots\right\}$ היא תת-קבוצה אינסופית של $S$, ו-$|B|=|\mathbb{N}|$."
      "\n"
      r"סה\"כ: $|S|=|\mathbb{N}|=\aleph_0$ כי $|\mathbb{N}|=|B|\le|S|\le|\mathbb{Q}|=|\mathbb{N}|$.".replace('סה\\"כ', "מסקנה")))

add(Q(8, "ב", "computation", "sets_power_set", 5,
      V2 + r"תהי $A=\{1,2,3,\ldots,2n+1\}$, כאשר $3<n\in\mathbb{N}$. "
      r"חשבו כמה תתי-קבוצות $B\in P(A)$ מקיימות את התנאי $B\cup\{2,4,6,8,\ldots,2n\}=A$.",
      r"$B\cup\{2,4,6,\ldots,2n\}=A\iff B=\{1,3,5,\ldots,2n+1\}\cup C\ \wedge\ C\subseteq\{2,4,\ldots,2n\}$."
      "\n"
      r"לכן מספר ה-$B$-ים שווה למספר ה-$C$-ים: $|P(\{2,4,\ldots,2n\})|=2^{|\{2,4,\ldots,2n\}|}=2^n$."))

exam = {
    "examCode": "22A-B",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ב, מועד ב (24.02.2022), שתי גרסאות',
    "year": 2022,
    "examDate": "24.02.2022",
    "sourceFile": "22A-B exam with solution, pp.1-12 (form 1 = Q1-Q4, form 2 = Q5-Q8)",
    "solutionFile": "22A-B handwritten solution (author unknown), pp.2-12",
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
