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
def P_(num_, part, built):
    r, p, s = built
    put(num_, part, r, p, s)


def equiv_item(form):
    rubric = rub(("הגדרה: שני פסוקים שקולים לוגית כשיש להם אותה טבלת אמת", 4),
                 ("בניית טבלת אמת מלאה בת 8 שורות עם עמודות הביניים", 6),
                 ("השוואת שתי העמודות הסופיות", 3),
                 ("מסקנה: הפסוקים שקולים לוגית", 1))
    pit = ["לבדוק רק חלק מהשורות: שקילות דורשת התאמה בכל 8 השורות.",
           r"לטעות בטבלת האמת של גרירה: $p\to q$ שקרית רק כש-$p$ אמת ו-$q$ שקר.",
           "להשוות עמודות ביניים במקום את שתי העמודות הסופיות."]
    if form == 1:
        steps = [num(r"בכמה מתוך 8 השורות הפסוק $(p\wedge q)\to r$ שקר?", 1, "גרירה שקרית רק כשהמקדים אמת והמסקנה שקר."),
                 ch(r"באיזו השמה $(p,q,r)$ הפסוק $(p\wedge q)\to r$ שקר?", r"$p=T,\ q=T,\ r=F$", r"$p=T,\ q=F,\ r=F$",
                    r"$p=F,\ q=T,\ r=F$", r"$p=T,\ q=T,\ r=T$", explain=r"צריך $p\wedge q$ אמת ו-$r$ שקר."),
                 ch("מה המסקנה מהשוואת שתי העמודות האחרונות?", "הפסוקים שקולים לוגית", "הפסוקים אינם שקולים",
                    "הפסוקים סותרים זה את זה", "שני הפסוקים טאוטולוגיות",
                    explain="העמודות זהות בכל 8 השורות, ובשתיהן יש שורה שקרית, ולכן אינם טאוטולוגיות.")]
    else:
        steps = [num(r"בכמה מתוך 8 השורות הפסוק $(p\vee q)\to r$ שקר?", 3, r"צריך $p\vee q$ אמת ו-$r$ שקר: שלוש שורות."),
                 ch(r"באיזו השמה $(p,q,r)$ שני הצדדים $(p\to r)\wedge(q\to r)$ ו-$(p\vee q)\to r$ אמת ו-$r$ שקר?",
                    r"$p=F,\ q=F,\ r=F$", r"$p=T,\ q=F,\ r=F$", r"$p=F,\ q=T,\ r=F$", r"$p=T,\ q=T,\ r=F$",
                    explain=r"כש-$r$ שקר צריך $p$ ו-$q$ שקריים כדי ששני הצדדים יהיו אמת."),
                 ch("מה המסקנה מהשוואת שתי העמודות האחרונות?", "הפסוקים שקולים לוגית", "הפסוקים אינם שקולים",
                    "הפסוקים סותרים זה את זה", "שני הפסוקים טאוטולוגיות",
                    explain="העמודות זהות בכל 8 השורות, ובשתיהן יש שורה שקרית, ולכן אינם טאוטולוגיות.")]
    return rubric, pit, steps


def euclid2_item(form):
    rubric = rub(("הרצת האלגוריתם המורחב של Euclid על $84,68$ עם עמודת המנות", 3),
                 (r"הצבה לאחור וקבלת $4=84\cdot(-4)+68\cdot5$ ותרגום ל-$x_1,y_1$", 2),
                 ("טיפול בסימנים של $\\gcd(-a,-b)$ וקבלת $x_2,y_2$", 2),
                 ("(2): סימון $d=\\gcd(a,b)$ ו-$m=\\operatorname{lcm}(a,b)$", 1),
                 ("(2): הוכחה ש-$d\\mid m$", 2),
                 ("(2): מסקנה $\\gcd(m,d)=d$", 1))
    pit = [r"לטעות בסדר המקדמים: $84x+68y$ שונה מ-$68x+84y$ (המקדמים מתחלפים).",
           r"להניח $\gcd(\operatorname{lcm}(a,b),\gcd(a,b))=1$: הוא שווה ל-$\gcd(a,b)$.",
           "לשכוח שהמקדמים של המספרים השליליים מחליפים סימן."]
    if form == 1:
        ans, wr = r"$(5,-4)$", (r"$(-4,5)$", r"$(5,4)$", r"$(4,-5)$")
        pr = r"איזה זוג $(x_1,y_1)$ מקיים $4=68x_1+84y_1$?"
    else:
        ans, wr = r"$(-4,5)$", (r"$(5,-4)$", r"$(4,5)$", r"$(-5,4)$")
        pr = r"איזה זוג $(x_1,y_1)$ מקיים $4=84x_1+68y_1$?"
    steps = [num(r"מהו $\gcd(84,68)$?", 4, "השארית האחרונה שאינה אפס היא 4."),
             order(r"סדרו את שורות החילוק של האלגוריתם על $84,68$.",
                   [r"$84=1\cdot68+16$", r"$68=4\cdot16+4$", r"$16=4\cdot4+0$"], "כל שורה משתמשת בשארית של השורה הקודמת."),
             ch(pr, ans, *wr, explain=r"הצבה: $84\cdot(-4)+68\cdot5=-336+340=4$."),
             ch(r"מהו $\gcd(\operatorname{lcm}(a,b),\gcd(a,b))$?", r"$\gcd(a,b)$", r"$\operatorname{lcm}(a,b)$", r"$1$", r"$a\cdot b$",
                explain=r"$d=\gcd(a,b)$ מחלק את $m=\operatorname{lcm}(a,b)$, ולכן $\gcd(m,d)=d$ (למשל ב-$84,68$: $\gcd(1428,4)=4$).")]
    return rubric, pit, steps


def fermat41_item(a1, a2, b1, b2):
    """a = a1^20 + 40!, b = b1^80 + 40; a1 = x^2 (x^40), b1 = y^2 (y^80=100^..)."""
    rubric = rub(("שימוש ב-41 הראשוני: $41\\mid b$ בעזרת פרמה והצגת $b$ כ-$(c^{40}-1)+41$", 2),
                 ("$41\\mid a$ בעזרת פרמה על הבסיס ו-וילסון על $40!$", 2),
                 ("מסקנה: $41\\le\\gcd(a,b)$ ולכן $40<\\gcd(a,b)$", 1))
    pit = ["להפעיל את פרמה על בסיס שמתחלק ב-41.",
           r"לשכוח שווילסון נותן $40!\equiv-1\pmod{41}$, כלומר $41\mid40!+1$ ולא $41\mid40!$.",
           "להסיק $\\gcd=41$ במקום $41\\le\\gcd$: מספיק לדעת שהוא לפחות 41."]
    steps = [ch("איזה מספר ראשוני משתמש בו הפתרון הרשמי כדי להראות שה-gcd גדול מ-40?", "41", "37", "43", "47",
                explain="41 מחלק את שני המספרים, ולכן ה-gcd הוא לפחות 41; הראשוניים האחרים אינם מחלקים את ה-gcd."),
             num(T(r"מהי השארית של $@A@^{20}$ בחלוקה ב-41?", A=a1), 1, "לפי פרמה השארית היא 1, כי $a^{20}=(\\ldots)^{40}$."),
             num(r"מהי השארית של $40!$ בחלוקה ב-41?", 40, r"לפי וילסון $40!\equiv-1\equiv40\pmod{41}$."),
             num(T(r"מהי השארית של $@B@^{80}+40$ בחלוקה ב-41?", B=b1), 0, "החזקה נותנת 1 והסכום עם 40 הוא 41, כלומר 0.")]
    return rubric, pit, steps


def ineq_item(c, lines, bug_idx, bug_line):
    rubric = rub(("בסיס: בדיקת $P(1)$", 3), ("ניסוח הנחת האינדוקציה $P(k)$ ומה צריך להוכיח", 3),
                 ("פתיחת $(k+1)^2$ והחסמת $2k+1$ בעזרת $k\\ge1$", 6),
                 ("שימוש בהנחת האינדוקציה לחסם ב-$" + str(c) + "\\cdot" + str(c) + "^k$", 3), ("מסקנה לפי עקרון האינדוקציה", 1))
    pit = ["להשתמש ב-$P(k+1)$ בתוך ההוכחה שלו.",
           "לשכוח את התנאי $k\\ge1$ בחסימה של $2k+1$ על ידי $3k^2$.",
           "להכפיל את שני אגפי ההנחה בקבוע שגוי במקום להשתמש ב-" + str(c) + "."]
    steps = [ch("בצעד מחליפים $2k$ ב-$2k^2$ ואת $1$ ב-$k^2$. איזו עובדה מצדיקה זאת?",
                r"$k\le k^2$ ו-$1\le k^2$ לכל $k\ge1$", r"$k^2\le k$ לכל $k\ge1$", r"$2k+1\le k$ לכל $k\ge1$",
                r"$k^2\le2k+1$ לכל $k\ge1$", explain="לכל $k\\ge1$ מתקיים $k\\le k^2$ וגם $1\\le k^2$."),
             order("סדרו את שלבי הצעד.", lines, "פתיחה, חסימה, איחוד, הנחת האינדוקציה, מסקנה."),
             bug("בגרסה הבאה של הצעד שורה אחת שגויה. מצאו אותה.", mutate(lines, bug_idx, bug_line), bug_idx,
                 "השורה ששונתה אינה נכונה מבחינה חשבונית.")]
    return rubric, pit, steps


def sets2_item(e1, e2, e3, fin, wrong3):
    return (rub(("חישוב הגודל של הקבוצה הנדרשת ($|A|$ או $|A\\cup B|$) מתיאור האיברים", 2),
                ("חישוב $|A-B|$ בעזרת $B\\subseteq A$ וחישוב $|A\\times B|$", 2),
                ("הצבה בחזקות של 2 וכתיבת הביטוי הסופי", 2)),
            ["לבלבל בין $|P(X)|=2^{|X|}$ לבין $|X|$ עצמו.",
             "לשכוח ש-$B\\subseteq A$ ולכן $A\\cup B=A$ ו-$|A-B|=|A|-|B|$.",
             "לחשב $|A\\times B|=|A|+|B|$ במקום המכפלה."],
            [num(*e1), num(*e2), num(*e3), ch("מהו הביטוי הסופי?", fin, *wrong3, explain="מחברים את שלושת הרכיבים לפי הנוסחה.")])


def card_item(inside_b, wrong_b):
    return (rub(("חסם עליון: $S\\subseteq\\mathbb{Q}$ ולכן $|S|\\le|\\mathbb{Q}|=|\\mathbb{N}|$", 2),
                ("חסם תחתון: תת-קבוצה אינסופית בת-מנייה של $S$", 2), ("קנטור-ברנשטיין והמסקנה $|S|=\\aleph_0$", 1)),
            ["לחשוב ש-$S$ בעוצמת הרצף כי היא נמצאת בקטע: רק המספרים הרציונליים שבקטע נכללים.",
             "להראות רק חסם אחד בלי השני.",
             "לבחור תת-קבוצה שאינה מוכלת ב-$S$ (למשל עם מספרים אי-רציונליים)."],
            [ch(r"מהי עוצמת $S$?", r"$\aleph_0$", r"$\mathfrak{c}$", "סופית", r"$2^{\mathfrak{c}}$",
                explain=r"$S$ אינסופית ומוכלת ב-$\mathbb{Q}$ הבת-מנייה."),
             ch(r"איזו תת-קבוצה אינסופית של $S$ משמשת להוכחה?", inside_b, *wrong_b,
                explain="רק הקבוצה הראשונה מורכבת ממספרים רציונליים בתוך הקטע."),
             ch("באיזו שיטה משתמש הפתרון הרשמי?", r"הכלה בשני כיוונים: $|\mathbb{N}|\le|S|\le|\mathbb{Q}|=|\mathbb{N}|$ (קנטור-ברנשטיין)",
                r"בנייה של התאמה מפורשת בין $S$ ל-$\mathbb{N}$", "טיעון אלכסוני", "אינדוקציה",
                explain="שתי הכלות נותנות שוויון עוצמות.")])


def count_item(form):
    if form == 1:
        s = [num(r"כמה איברים זוגיים יש ב-$A$ כש-$n=4$ ($A=\{1,\ldots,9\}$)?", 4, "$n=4$: האיברים $2,4,6,8$."),
             num(r"כמה איברים אי-זוגיים (חופשיים) יש ב-$A$ כש-$n=4$?", 5, "$n+1=5$."),
             num(r"כמה תת-קבוצות $B$ מקיימות את התנאי כש-$n=4$?", 32, "הזוגיים חייבים להיכלל והאי-זוגיים חופשיים: $2^5=32$ (הוכח בבדיקת כל 512 הקבוצות)."),
             ch("מהי התשובה הכללית?", r"$2^{n+1}$", r"$2^{n}$", r"$2^{2n+1}$", r"$2^{n+1}-1$",
                explain="האיברים האי-זוגיים חופשיים והזוגיים חייבים להיכלל.")]
    else:
        s = [num(r"כמה איברים אי-זוגיים יש ב-$A$ כש-$n=4$ ($A=\{1,\ldots,9\}$)?", 5, "$n+1=5$ האיברים $1,3,5,7,9$."),
             num(r"כמה איברים זוגיים (חופשיים) יש ב-$A$ כש-$n=4$?", 4, "$n=4$."),
             num(r"כמה תת-קבוצות $B$ מקיימות את התנאי כש-$n=4$?", 16, "האי-זוגיים חייבים להיכלל והזוגיים חופשיים: $2^4=16$ (הוכח בבדיקת כל 512 הקבוצות)."),
             ch("מהי התשובה הכללית?", r"$2^{n}$", r"$2^{n+1}$", r"$2^{2n+1}$", r"$2^{n}-1$",
                explain="האיברים הזוגיים חופשיים והאי-זוגיים חייבים להיכלל.")]
    return (rub(("תיאור $B$: מכילה את כל האיברים שאינם בקבוצה הנתונה ותת-קבוצה כלשהי של האחרים", 3), ("ספירת הבחירות החופשיות והתשובה הכללית", 2)),
            ["לחשוב ש-$B$ חייבת להכיל את אברי הקבוצה הנתונה: הם כבר מכוסים על ידה.",
             "לספור את מספר האיברים החופשיים בטעות ($n$ מול $n+1$).",
             "לבלבל בין תנאי האיחוד לתנאי החיתוך."], s)


def rel_item(form):
    last = r"$R$ רפלקסיבי ולכן $(x,x)\in R$ לכל $x\in A$, ואין ב-$R$ זוגות אחרים, לכן $R=\{(x,x):x\in A\}$, וזהו יחס שקילות" if form == 1 else r"$R$ רפלקסיבי ולכן $(x,x)\in R$ לכל $x\in A$, ואין ב-$R$ זוגות אחרים, לכן $R=\{(x,x):x\in A\}$, וזהו יחס סדר חלקי"
    lines = [r"נניח בשלילה ש-$(x,y)\in R$ עבור $x\ne y$",
             r"מסימטריה $(y,x)\in R$, ולכן מאנטי-סימטריה $x=y$, סתירה", last]
    return (rub(("שימוש ברפלקסיביות: $(x,x)\\in R$ לכל $x$", 1), ("הנחה בשלילה על זוג $(x,y)$ עם $x\\ne y$", 1),
                ("סתירה משילוב הסימטריה והאנטי-סימטריה", 2), ("מסקנה: $R$ יחס הזהות, ולכן " + ("יחס שקילות" if form == 1 else "יחס סדר חלקי"), 1)),
            ["להניח שיחס אנטי-סימטרי ובו זוג הפוך אסור תמיד: הוא אסור רק כש-$x\\ne y$.",
             "לשכוח שגם יחס הזהות מקיים את שלוש התכונות ולכן הוא היחיד שנשאר.",
             "להשתמש בטרנזיטיביות כשאין בה צורך."],
            [ch("מהי התשובה לטענה?", "הטענה נכונה", "הטענה אינה נכונה", explain="היחס היחיד שמקיים את שלוש התכונות הוא יחס הזהות."),
             num(r"כמה זוגות סדורים יש ב-$R$, כש-$|A|=5$?", 5, "יחס הזהות על 5 איברים (הוכח בבדיקת כל היחסים על $n\\le4$ ובטיעון על $n=5$)."),
             order("סדרו את שלבי ההוכחה.", lines, "הנחה בשלילה, סתירה, מסקנה (עם הרפלקסיביות).")])


_F7 = [
    num(r"כמה ערכי $k\in\{1,\ldots,7\}$ מקיימים $f(k)=3$?", 3, r"$f(1)=f(5)=f(7)=3$."),
    num(r"מהו הערך היחיד של $k$ שעבורו $f(k)=5$ (כלומר $f^{-1}(5)$)?", 3, r"רק $f(3)=5$."),
    num(r"כמה קבוצות $A\subseteq\{1,\ldots,7\}$ מקיימות ש-$f:A\to\{2,3,5,6\}$ הפיכה?", 6,
        "צריך בדיוק מקור אחד לכל ערך: $3$ אפשרויות לערך 3, $2$ לערך 6, ו-$1$ לכל אחד משני האחרים, כלומר $3\\cdot2=6$."),
]
_F7R = (rub(("חישוב $f(k)$ לכל $k\\in\\{1,\\ldots,7\\}$", 3), ("זיהוי הערכים בעלי יותר ממקור אחד", 2), ("בחירת $A$ עם מקור אחד לכל ערך", 1),
            ("חישוב $f^{-1}$ בעזרת המקורות שנבחרו", 2)),
        ["לבחור $A$ שמכילה שני מקורות לאותו ערך: אז $f$ אינה חד-חד-ערכית.",
         "לשכוח שהטווח הנתון הוא $\\{2,3,5,6\\}$ ולכן כל ערך חייב מקור ב-$A$.",
         "לטעות בחישוב $k^2\\bmod6$ (למשל $25\\bmod6=1$ ולא 5)."], _F7)

# ================= FORM 1 =================
P_(1, "א", equiv_item(1))
P_(1, "ב", euclid2_item(1))
P_(1, "ג", fermat41_item(25, None, 8, None))

_I1 = [r"$(k+1)^2=k^2+2k+1$",
       r"$k^2+2k+1\le k^2+2k^2+k^2$, כי $k\le k^2$ ו-$1\le k^2$ לכל $k\ge1$",
       r"$k^2+2k^2+k^2=4k^2\le5k^2$",
       r"$5k^2\le5\cdot5^k$ לפי הנחת האינדוקציה $k^2\le5^k$",
       r"$5\cdot5^k=5^{k+1}$, כלומר $P(k+1)$ נכון"]
P_(2, "א", ineq_item(5, _I1, 2, r"$k^2+2k^2+k^2=3k^2\le5k^2$"))

P_(2, "ב", sets2_item((r"מהו $|A|$?", 121, r"$11\cdot11=121$ (הערכים של $n$ ושל $m$ נותנים מספרים שונים)."),
                       (r"מהו $|A-B|$?", 111, r"$B\subset A$ ולכן $121-10=111$."),
                       (r"מהו $|A\times B|$ (המעריך של 2 ב-$|P(A\times B)|$)?", 1210, r"$121\cdot10=1210$."),
                       r"$111+2^{1210}+2^{121}$", (r"$111+2^{1210}+121$", r"$2^{111}+2^{1210}+2^{121}$", r"$111+2^{121}+2^{121}$")))

_C = [r"נניח $A-B\not\subseteq C$, כלומר קיים $x\in A-B$ כך ש-$x\notin C$",
      r"$x\in A\wedge x\notin B\wedge x\notin C$",
      r"$x\in A\wedge x\notin B\cup C$",
      r"לכן $A\not\subseteq B\cup C$, וזה ה-contrapositive שנדרש"]
_CW = (r"אם $A\not\subseteq B\cup C$, אז $A-B\not\subseteq C$", r"אם $A-B\subseteq C$, אז $A\subseteq B\cup C$",
       r"אם $A\subseteq B\cup C$, אז $A-B\not\subseteq C$")
_CR = r"אם $A-B\not\subseteq C$, אז $A\not\subseteq B\cup C$"
P_(2, "ג", contra_item(_CR, _CW, _C, 2, r"$x\in A\wedge x\in B\cup C$"))

P_(3, "א", parity_item(9, 5))
put(3, "ב", _F7R[0], _F7R[1], _F7R[2])
P_(3, "ג", rel_item(1))
P_(4, "א", card_item(r"$\{3+\frac{1}{2^n}:\ n\in\mathbb{N},\ n\ge1\}$",
                     (r"$\{3+\frac{\sqrt2}{n}:\ n\in\mathbb{N},\ n\ge1\}$", r"$\{8+\frac1n:\ n\in\mathbb{N},\ n\ge1\}$",
                      r"$\{3-\frac{1}{2^n}:\ n\in\mathbb{N},\ n\ge1\}$")))
P_(4, "ב", count_item(1))

# ================= FORM 2 =================
P_(5, "א", equiv_item(2))
P_(5, "ב", euclid2_item(2))
P_(5, "ג", fermat41_item(36, None, 10, None))

_I2 = [r"$(k+1)^2=k^2+2k+1$",
       r"$k^2+2k+1\le k^2+2k^2+k^2$, כי $k\le k^2$ ו-$1\le k^2$ לכל $k\ge1$",
       r"$k^2+2k^2+k^2=4k^2$",
       r"$4k^2\le4\cdot4^k$ לפי הנחת האינדוקציה $k^2\le4^k$",
       r"$4\cdot4^k=4^{k+1}$, כלומר $P(k+1)$ נכון"]
P_(6, "א", ineq_item(4, _I2, 2, r"$k^2+2k^2+k^2=3k^2$"))

P_(6, "ב", sets2_item((r"מהו $|A\cup B|$?", 121, r"$B\subseteq A$ ולכן $A\cup B=A$ ו-$|A|=11\cdot11=121$."),
                       (r"מהו $|A-B|$?", 111, r"$121-10=111$."),
                       (r"מהו $|A\times B|$ (המעריך של 2 ב-$|P(A\times B)|$)?", 1210, r"$121\cdot10=1210$."),
                       r"$121+2^{1210}+2^{111}$", (r"$232+2^{1210}$", r"$121+2^{1210}+111$", r"$121+2^{1210}+2^{121}$")))

P_(6, "ג", contra_item(_CR, _CW, _C, 2, r"$x\in A\wedge x\in B\cup C$"))
P_(7, "א", parity_item(3, 7))
put(7, "ב", _F7R[0], _F7R[1], _F7R[2])
P_(7, "ג", rel_item(2))
P_(8, "א", card_item(r"$\{5+\frac{1}{2^n}:\ n\in\mathbb{N},\ n\ge1\}$",
                     (r"$\{5+\frac{\sqrt2}{n}:\ n\in\mathbb{N},\ n\ge1\}$", r"$\{9+\frac1n:\ n\in\mathbb{N},\ n\ge1\}$",
                      r"$\{5-\frac{1}{2^n}:\ n\in\mathbb{N},\ n\ge1\}$")))
P_(8, "ב", count_item(2))


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
