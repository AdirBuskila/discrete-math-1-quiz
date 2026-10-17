# -*- coding: utf-8 -*-
"""Generator for tools/raw/26A-A.json -- discrete math 1, semester A 5786, moed A (03.02.2026).
Flagship sitting: 5 questions, each with parts (a)-(c), official lecturer solution transcribed.
Run: PYTHONUTF8=1 py tools/gen/gen_26A-A.py
Notes on structure:
 - A part with numbered sub-claims ((1), (2)) is ONE item (the id scheme allows a single letter per part).
 - Q5 prints the label (b) twice; the second one is transcribed as part (c)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26A-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution", "official": True, "confidence": "high"}
    q.update(kw)
    return q


questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "computation", "logic_propositional", 9,
      "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה הקשורה אליו.\n"
      "**המונח:** טאוטולוגיה\n"
      r"**שאלה:** האם הפסוק $(p\vee q)\wedge(\neg p\vee r)\to(q\vee r)$ הוא טאוטולוגיה ?",
      "טבלת אמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | p∨q | ¬p∨r | (p∨q)∧(¬p∨r) | q∨r | (p∨q)∧(¬p∨r)→(q∨r)\n"
      "T T T |  T  |  T   |      T        |  T  |         T\n"
      "F T T |  T  |  T   |      T        |  T  |         T\n"
      "T F T |  T  |  T   |      T        |  T  |         T\n"
      "F F T |  F  |  T   |      F        |  T  |         T\n"
      "T T F |  T  |  F   |      F        |  T  |         T\n"
      "F T F |  T  |  T   |      T        |  T  |         T\n"
      "T F F |  T  |  F   |      F        |  F  |         T\n"
      "F F F |  F  |  T   |      F        |  F  |         T\n"
      "```\n"
      "העמודה האחרונה כולה T, ולכן הפסוק הוא טאוטולוגיה."),

    Q(1, "ב", "proof", "number_theory_gcd", 8,
      "**המונח:** מספר ראשוני\n"
      r"**שאלה:** המספר הראשוני הגדול ביותר שידוע להיום הוא $2^{136279841}-1$. "
      r"האם גם המספר $m=136279841$ הוא מספר ראשוני ?",
      r"נניח ש-$m$ פריק. אז קיימים מספרים טבעיים $1<n\le q<m$ כך ש: $m=n\cdot q$. לכן נקבל:"
      "\n"
      r"$$2^{136279841}-1=2^{nq}-1=(2^q)^n-1^n=(2^q-1)\left((2^q)^{n-1}+(2^q)^{n-2}+\dots+1\right)$$"
      "\n"
      r"מכיוון ש: $1\ne 2^q-1$ (כי $1<q$) נקבל ש: $2^{136279841}-1$ לא ראשוני, בסתירה לנתון."
      "\n"
      r"מסקנה: $m$ הוא מספר ראשוני."),

    Q(1, "ג", "truefalse", "equivalence_relations", 8,
      "**המונח:** יחס שקילות\n"
      r"**שאלה:** יהיו $R_1,R_2,\dots,R_k$ **כל יחסי השקילות** על הקבוצה $A=\{1,2,\dots,10\}$. "
      r"האם היחס $R_1\cap R_2\cap\dots\cap R_k$ הוא פונקציה?",
      r"$$\{(1,1),(2,2),\dots,(10,10)\}=R_1\cap R_2\cap\dots\cap R_k$$"
      "\n"
      r"כי יחס הזהות $\{(1,1),(2,2),\dots,(10,10)\}$ הוא יחס שקילות שמוכל בכל יחס שקילות, "
      r"ולכל $k\in A$ יש זוג יחיד $(k,k)\in R$. לכן הטענה נכונה.",
      verdict=True),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 12,
      r"הראו שלכל $2\le n\in\mathbb{N}$ מתקיים:"
      "\n"
      r"$$\frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\frac{1}{3\cdot 4}+\dots+\frac{1}{(n-1)\cdot n}=\frac{n-1}{n}$$",
      r"**I. בסיס:** $P(2)$: $\frac{1}{1\cdot 2}=\frac{2-1}{2}\iff\frac12=\frac12\Rightarrow P(2)=\text{TRUE}$."
      "\n"
      r"**II. צעד:** $P(k)=T$ עבור $2\le k\in\mathbb{N}$ $\Rightarrow$ $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ \frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\dots+\frac{1}{(k-1)\cdot k}=\frac{k-1}{k}$"
      "\n"
      r"$P(k+1):\ \frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\dots+\frac{1}{(k-1)k}+\frac{1}{k(k+1)}=\frac{k}{k+1}$"
      "\n"
      r"לפי הנחת האינדוקציה, הסכום של $k-1$ האיברים הראשונים שווה ל-$\frac{k-1}{k}$, ולכן:"
      "\n"
      r"$$\frac{1}{1\cdot 2}+\dots+\frac{1}{(k-1)k}+\frac{1}{k(k+1)}=\frac{k-1}{k}+\frac{1}{k(k+1)}"
      r"=\frac{(k-1)(k+1)+1}{k(k+1)}=\frac{k^2-1+1}{k(k+1)}=\frac{k^2}{k(k+1)}=\frac{k}{k+1}$$"
      "\n"
      r"$\Rightarrow P(k+1)=T$."
      "\n"
      r"מסקנה: מ-I ו-II, לפי עקרון האינדוקציה, לכל $2\le n\in\mathbb{N}$ מתקיים $P(n)=T$."
      "\n"
      "אפשרות אחרת: לפרק לסכום טלסקופי."),

    Q(2, "ב", "computation", "sets_power_set", 5,
      r"תהי הקבוצה $A=\{a,b,c,d,e,f\}$."
      "\n"
      r"כמה תתי-קבוצות $B$ של $A$ מקיימות את התנאי: $B\cap\{a,b\}=\{a\}$ ?",
      r"בכל תת-קבוצה $B$ צריך שתהיה האות $a$ (כי היא בחיתוך), ושלא תהיה האות $b$ "
      r"(כי לא בחיתוך), שאר האותיות $\{c,d,e,f\}$ יכולות להופיע ויכולות גם לא להופיע."
      "\n"
      r"לכן כל תת-קבוצה $B$ היא מהצורה $B=\{a\}\cup C$, כאשר $C$ היא תת-קבוצה של $\{c,d,e,f\}$. "
      r"מספר תתי הקבוצות של $\{c,d,e,f\}$ הוא $2^4$, וכל תת קבוצה כזו אנו נאחד עם $\{a\}$."
      "\n"
      r"לכן התשובה היא $2^4=16$."),

    Q(2, "ג", "proof", "relations_properties", 8,
      "הוכיחו או הפריכו:\n"
      r"(1) אם $R_1,R_2\subseteq\{1,2,3\}\times\{1,2,3\}$ יחסים רפלקסיביים, סימטריים וגם אנטי-סימטריים, "
      r"אז $R_1\,\triangle\,R_2$ הוא יחס טרנזיטיבי."
      "\n"
      r"(2) אם $R_1,R_2\subseteq\{1,2\}\times\{1,2\}$ הם יחסי סדר מלא שונים על הקבוצה $\{1,2\}$, "
      r"אז גם $R_1\cup R_2$ הוא יחס סדר מלא על $\{1,2\}$.",
      r"**(1)** טענה זו נכונה. נוכיח אותה: $R_1,R_2\subseteq\{1,2,3\}\times\{1,2,3\}$ יחסים רפלקסיביים. "
      r"לכן $\{(1,1),(2,2),(3,3)\}\subseteq R_1\cap R_2$. מכיוון ש: $R_1,R_2$ הם יחסים סימטריים וגם "
      r"אנטי-סימטריים, נשיג ש: אם $a\ne b$, אז $(a,b)\notin R_1$ וגם $(a,b)\notin R_2$."
      "\n"
      r"מסקנה: $R_1=R_2=\{(1,1),(2,2),(3,3)\}$ ולכן $R_1\triangle R_2=\emptyset$ וזהו יחס טרנזיטיבי."
      "\n"
      r"**(2)** על הקבוצה $\{1,2\}$ יש רק 2 יחסי סדר מלא שונים והם: "
      r"$R_1=\{(1,1),(2,2),(1,2)\}$ ו-$R_2=\{(1,1),(2,2),(2,1)\}$."
      "\n"
      r"אז $R_2\cup R_1=\{(1,1),(2,2),(1,2),(2,1)\}$ אינו סדר חלקי (כי הוא לא אנטי-סימטרי)."
      "\n"
      "מסקנה: טענה זו לא נכונה."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "equivalence_relations", 10,
      r"יהי נתון היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: "
      r"לכל $x,y\in\mathbb{Z}$, מתקיים $xRy\iff 4x+y$ הוא מספר שמתחלק ב-5."
      "\n"
      r"(1) הוכיחו ש-$R$ הוא יחס שקילות ומצאו את $\mathbb{Z}/R$."
      "\n"
      r"(2) האם $R$ הוא יחס סדר חלקי ?",
      "**(1)** נוכיח יחס שקילות:\n"
      r"**רפלקסיביות:** צ״ל: $\forall x\in\mathbb{Z},\ (x,x)\in R$. ואכן:"
      "\n"
      r"$$\forall x\in\mathbb{Z},\ 5\mid 5x\Rightarrow 5\mid(4x+x)\Rightarrow(x,x)\in R$$"
      "\n"
      r"**סימטריות:** נתון $(x,y)\in R$ כלומר $5\mid(4x+y)$, נוכיח ש-$(y,x)\in R$. כלומר $5\mid(4y+x)$. ואכן:"
      "\n"
      r"$$\forall x,y\in\mathbb{Z}:\ (x,y)\in R\Rightarrow 5\mid(4x+y)$$"
      "\n"
      r"$4x+y+4y+x=5x+5y=5(x+y)\Rightarrow 5\mid(4x+y+4y+x)$"
      "\n"
      r"לפי משפט: אם $c\mid a$ וגם $c\mid b$ אז $c\mid(a-b)$, לכן:"
      "\n"
      r"$$\Rightarrow 5\mid\big((4x+y+4y+x)-(4x+y)\big)\Rightarrow 5\mid(4y+x)\Rightarrow(y,x)\in R$$"
      "\n"
      r"**טרנזיטיביות:** נתון: $(x,y)\in R$ וגם $(y,z)\in R$, צ״ל ש: $(x,z)\in R$. ואכן:"
      "\n"
      r"$$\forall x,y,z\in\mathbb{Z}:\ (x,y)\in R\wedge(y,z)\in R\Rightarrow 5\mid(4x+y)\wedge 5\mid(4y+z)$$"
      "\n"
      r"לפי משפט: אם $c\mid a$ וגם $c\mid b$ אז $c\mid(a+b)$, לכן:"
      "\n"
      r"$$5\mid\big((4x+y)+(4y+z)\big)\Rightarrow 5\mid\big((4x+z)+5y\big),\ y\in\mathbb{Z}$$"
      "\n"
      r"שוב לפי משפט: אם $c\mid a$ וגם $c\mid b$ אז $c\mid(a-b)$, לכן:"
      "\n"
      r"$$5\mid\big((4x+z)+5y\big)\ \wedge\ 5\mid 5y\Rightarrow 5\mid(4x+z)\Rightarrow(x,z)\in R$$"
      "\n"
      r"מסקנה: $R$ הוא יחס רפלקסיבי, סימטרי וטרנזיטיבי ולכן הוא יחס שקילות."
      "\n"
      "נחשב את מחלקות השקילות:\n"
      r"$[0]=\{y:y\in\mathbb{Z}\wedge 0Ry\}=\{y:y\in\mathbb{Z}\wedge 5\mid(0x+y)\}=\{y:y\in\mathbb{Z}\wedge 5\mid y\}=\{5k:k\in\mathbb{Z}\}$"
      "\n"
      r"$[1]=\{y:y\in\mathbb{Z}\wedge 1Ry\}=\{y:y\in\mathbb{Z}\wedge 5\mid(4+y)\}=\{5k-4:k\in\mathbb{Z}\}=\{5k+1:k\in\mathbb{Z}\}$"
      "\n"
      r"$[2]=\{y:y\in\mathbb{Z}\wedge 2Ry\}=\{y:y\in\mathbb{Z}\wedge 5\mid(8+y)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+3+5)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+3)\}=\{5k-3:k\in\mathbb{Z}\}=\{5k+2:k\in\mathbb{Z}\}$"
      "\n"
      r"$[3]=\{y:y\in\mathbb{Z}\wedge 3Ry\}=\{y:y\in\mathbb{Z}\wedge 5\mid(12+y)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+2+10)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+2)\}=\{5k-2:k\in\mathbb{Z}\}=\{5k+3:k\in\mathbb{Z}\}$"
      "\n"
      r"$[4]=\{y:y\in\mathbb{Z}\wedge 4Ry\}=\{y:y\in\mathbb{Z}\wedge 5\mid(16+y)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+1+15)\}=\{y:y\in\mathbb{Z}\wedge 5\mid(y+1)\}=\{5k-1:k\in\mathbb{Z}\}=\{5k+4:k\in\mathbb{Z}\}$"
      "\n"
      r"מכיוון ש-$[0]\cup[1]\cup[2]\cup[3]\cup[4]=\mathbb{Z}$ אין עוד מחלקות שקילות. "
      r"לכן $\mathbb{Z}/R=\{[0],[1],[2],[3],[4]\}$."
      "\n"
      r"**(2)** $R$ אינו יחס סדר חלקי כי אינו אנטי סימטרי. לדוגמה: $(0,5)\in R$ וגם $(5,0)\in R$ אך $0\ne 5$."),

    Q(3, "ב", "computation", "number_theory_gcd", 8,
      r"מצאו על ידי האלגוריתם המורחב של Euclid שני מספרים $x,y\in\mathbb{Z}$ כך ש: "
      r"$\gcd(49,84)=49\cdot x+84\cdot y$.",
      "הטבלה של האלגוריתם המורחב (בכל שורה: $d$ הוא ה-gcd, ו-$x\\leftarrow y'$ ו-$y\\leftarrow x'-y'\\cdot\\lfloor a/b\\rfloor$ "
      "מחושבים מהשורה שמתחת):\n"
      "```\n"
      "  a    b    floor(a/b)   d    x    y\n"
      " 49   84        0        7   -5    3\n"
      " 84   49        1        7    3   -5\n"
      " 49   35        1        7   -2    3\n"
      " 35   14        2        7    1   -2\n"
      " 14    7        2        7    0    1\n"
      "  7    0       --        7    1    0\n"
      "```\n"
      r"$$\gcd(49,84)=7=49\cdot(-5)+84\cdot 3$$"),

    Q(3, "ג", "proof", "sets_power_set", 7,
      r"אם $A,B,C$ הן קבוצות לא ריקות, הראו ש:"
      "\n"
      r"$$(B-A)\cup(C-A)\subseteq(B\cup C)-A$$",
      "נוכיח את הטענה:\n"
      r"$$\forall x\in(B-A)\cup(C-A)\Rightarrow x\in(B-A)\vee x\in(C-A)\Rightarrow$$"
      "\n"
      r"$$(x\in B\wedge x\notin A)\vee(x\in C\wedge x\notin A)\Rightarrow(x\in B\vee x\in C)\wedge(x\notin A)\Rightarrow$$"
      "\n"
      r"$$\Rightarrow x\in(B\cup C)\wedge x\notin A\Rightarrow x\in(B\cup C)-A$$"
      "\n"
      "הסבר המעברים: לפי הגדרת איחוד והפרש ולפי חוק הפילוג."),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "sets_power_set", 9,
      r"תהיינה $A,B$ שתי קבוצות לא ריקות."
      "\n"
      r"(1) נסחו את ה-contrapositive של הטענה הבאה: "
      r"״אם $P(A)\cup P(B)=P(A\cup B)$, אז $B\subseteq A$ או $A\subseteq B$.״"
      "\n"
      "(2) הוכיחו את הטענה.",
      r"**(1)** אם $A\not\subseteq B$ וגם $B\not\subseteq A$, אז $P(A)\cup P(B)\ne P(A\cup B)$."
      "\n"
      r"**(2)** נניח ש-$A\not\subseteq B$ וגם $B\not\subseteq A$. "
      r"מ-$A\not\subseteq B$ נובע $\exists a\in A\ \&\ a\notin B$, ומ-$B\not\subseteq A$ נובע $\exists b\in B\ \&\ b\notin A$."
      "\n"
      r"$a\in A\ \&\ b\in B\Rightarrow\{a,b\}\subseteq A\cup B\Rightarrow\{a,b\}\in P(A\cup B)$."
      "\n"
      r"מצד שני, $\{a,b\}\not\subseteq A\iff\{a,b\}\notin P(A)$ ו-$\{a,b\}\not\subseteq B\iff\{a,b\}\notin P(B)$, "
      r"ולכן $\{a,b\}\notin P(A)\cup P(B)$."
      "\n"
      r"מכאן $P(A)\cup P(B)\ne P(A\cup B)$, ומסקנה: הטענה נכונה."
      "\n"
      r"או: אפשר להוכיח את ה-contrapositive, כלומר: אם $A\not\subseteq B$ וגם $B\not\subseteq A$, "
      r"אז $P(A)\cup P(B)\ne P(A\cup B)$, וזה מה שהוכחנו."),

    Q(4, "ב", "computation", "functions", 8,
      r"מצאו קבוצה $A$ כך שהפונקציה $f:\mathbb{N}^*\to A$ היא על, כאשר $f$ מוגדרת לפי הכלל "
      r"$f(x)=\gcd(12,x)$ לכל $x\in\mathbb{N}^*$.",
      r"תחילה נשים לב ש: $12=2^2\cdot 3$ לכל $x\in\mathbb{N}^*$:"
      "\n"
      r"1. אם $x\mid 2$ וגם $x\nmid 3$ וגם $x\nmid 2^2$ אז: $\gcd(12,x)=2$"
      "\n"
      r"2. אם $x\mid 2$ וגם $x\nmid 3$ וגם $x\mid 2^2$ אז: $\gcd(12,x)=4$"
      "\n"
      r"3. אם $x\mid 2$ וגם $x\mid 3$ וגם $x\nmid 2^2$ אז: $\gcd(12,x)=6$"
      "\n"
      r"4. אם $x\mid 2$ וגם $x\mid 3$ וגם $x\mid 2^2$ אז: $\gcd(12,x)=12$"
      "\n"
      r"5. אם $x\nmid 2$ וגם $x\mid 3$ וגם $x\nmid 2^2$ אז: $\gcd(12,x)=3$"
      "\n"
      r"6. אם $x\nmid 2$ וגם $x\nmid 3$ וגם $x\nmid 2^2$ אז: $\gcd(12,x)=1$"
      "\n"
      r"לכן על מנת שהפונקציה תהיה על הקבוצה $A$ צריכה להיות: $A=\{1,2,3,4,6,12\}$."
      "\n"
      "או:\n"
      r"המחלקים של $12$ הם $1,2,3,4,6,12$ ואז $f(x)\in\{1,2,3,4,6,12\}$ לכל $x\in\mathbb{N}^*$. "
      r"בנוסף: $f(1)=1,\ f(2)=2,\ f(3)=3,\ f(4)=4,\ f(6)=6,\ f(12)=12$ וגם $1,2,3,4,6,12\in\mathbb{N}^*$."
      "\n"
      r"לכן $f:\mathbb{N}^*\to\{1,2,3,4,6,12\}$ היא על."),

    Q(4, "ג", "proof", "number_theory_gcd", 8,
      "הוכיחו או הפריכו:\n"
      r"לא קיים מספר ראשוני $p$ כך ש: $p^2+3p+2$ מספר ראשוני.",
      r"טענה זו נכונה, לא קיים מספר ראשוני $p$ כך ש: $p^2+3p+2$ מספר ראשוני."
      "\n"
      r"נניח בשלילה שקיים מספר ראשוני $p$ כך ש: $p^2+3p+2$ מספר ראשוני. "
      r"כיוון ש: $p^2+3p+2$ הוא מספר ראשוני הגדול מ-2, אז $p^2+3p+2$ הוא אי-זוגי. "
      r"לכן $p^2+3p$ הוא גם כן אי-זוגי. כלומר $p(p+3)$ הוא מס׳ אי-זוגי. "
      r"לכן $p$ חייב להיות אי-זוגי, וגם $p+3$ חייב להיות אי זוגי. "
      r"אבל זה לא יתכן, כי אם $p$ אי-זוגי, אז $p+3$ חייב להיות זוגי. סתירה."
      "\n"
      "או:\n"
      r"**מקרה 1:** $p=2$ $\Rightarrow$ $p^2+3p+2=12$, שאינו מספר ראשוני."
      "\n"
      r"**מקרה 2:** $p>2$ $\Rightarrow$ $p$ אי-זוגי $\Rightarrow$ $p+3$ זוגי $\Rightarrow$ $p(p+3)$ זוגי "
      r"$\Rightarrow$ $p(p+3)+2$ זוגי וגדול מ-2."
      "\n"
      r"אז: ל-$p^2+3p+2$ יש לפחות 3 מחלקים: $1,\ 2,\ p^2+3p+2$, ולכן הוא לא ראשוני."),

    # ---------------- Q5 ----------------
    Q(5, "א", "truefalse", "modular_fermat_wilson", 9,
      "הוכיחו או הפריכו:\n"
      r"$$74\le\gcd(36^{36}+36!\ ,\ 7^{72}-1)$$",
      r"המספרים $7^{72}-1$ ו-$36^{36}+36!$ הם זוגיים, כלומר מתחלקים ב-2."
      "\n"
      r"$7^{72}-1=49^{36}-1=49^{37-1}-1$. כיוון ש-37 ראשוני ו-$37\nmid 49$, לפי Fermat מתקבל $37\mid(7^{72}-1)$."
      "\n"
      r"$36^{36}+36!=(36^{37-1}-1)+((37-1)!+1)\Rightarrow 37\mid(36^{36}+36!)$"
      "\n"
      r"כי: $37\nmid 36$ ו-37 ראשוני, ולכן $37\mid(36^{37-1}-1)$ (Fermat), "
      r"ומצד שני $37\mid((37-1)!+1)$ כי 37 ראשוני (Wilson)."
      "\n"
      r"כי $1=\gcd(2,37)$ נקבל ש: $74=2\cdot 37\mid(7^{72}-1)$ ו-$74=2\cdot 37\mid(36^{36}+36!)$."
      "\n"
      r"לכן $74\le\gcd(36^{36}+36!\ ,\ 7^{72}-1)$, כלומר המספרים $7^{72}-1$ ו-$36^{36}+36!$ מתחלקים ב-74. "
      "הטענה נכונה.",
      verdict=True),

    Q(5, "ב", "proof", "functions", 8,
      r"הראו שהפונקציה $f:\mathbb{Z}\to\mathbb{Z}\times\mathbb{Z}$ שמוגדרת לפי הכלל "
      r"$f(x)=(x+1,\ 2x+5)$ לכל $x\in\mathbb{Z}$, היא חד-חד-ערכית."
      "\n"
      r"האם $f$ הפיכה ?",
      r"**פתרון:** נניח $f(x_1)=f(x_2)$, כלומר $(x_1+1,\ 2x_1+5)=(x_2+1,\ 2x_2+5)$, ולכן:"
      "\n"
      r"$$\begin{cases}x_1+1=x_2+1\\ 2x_1+5=2x_2+5\end{cases}\Rightarrow x_1=x_2$$"
      "\n"
      r"לכן $f$ היא חח״ע."
      "\n"
      r"$f$ אינה על: אין $x\in\mathbb{Z}$ כך ש: $f(x)=(1,1)$, כי $x+1=1\Rightarrow x=0$ ו-$2x+5=1\Rightarrow x=-2$, "
      r"ו-$0\ne -2$. לכן $f$ לא הפיכה."),

    Q(5, "ג", "proof", "cardinality_sets", 8,
      r"הראו שהקבוצות $\mathbb{Q}\cap[1,2)$ ו-$\mathbb{Z}\cap\mathbb{R}$ שוות עוצמה.",
      r"$\aleph_0=|\mathbb{Z}|=|\mathbb{Z}\cap\mathbb{R}|\ \Leftarrow\ \mathbb{Z}\cap\mathbb{R}=\mathbb{Z}$"
      "\n"
      r"$|\mathbb{Q}\cap[1,2)|\le|\mathbb{Q}|\ \Leftarrow\ \mathbb{Q}\cap[1,2)\subseteq\mathbb{Q}$"
      "\n"
      r"$\{1,\ 1+\frac12,\ 1+\frac13,\ \dots,\ 1+\frac1n,\dots\}\subseteq\mathbb{Q}\cap[1,2)\Rightarrow$"
      "\n"
      r"$\Rightarrow\aleph_0=\left|\{1,\ 1+\frac12,\ 1+\frac13,\dots\}\right|\le|\mathbb{Q}\cap[1,2)|\le|\mathbb{Q}|=\aleph_0$"
      "\n"
      r"לכן: $|\mathbb{Z}\cap\mathbb{R}|=\aleph_0=|\mathbb{Q}\cap[1,2)|$."),
]

exam = {
    "examCode": "26A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ו, מועד א (03.02.2026)',
    "year": 2026,
    "examDate": "03.02.2026",
    "sourceFile": "26A-A exam with lecturer solution, pp.1-11",
    "solutionFile": "26A-A lecturer solution (handwritten and typed), pp.2-11",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
