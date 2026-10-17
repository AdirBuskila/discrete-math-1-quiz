# -*- coding: utf-8 -*-
"""Generator for tools/raw/19S-A.json -- discrete math 1 (20066), moed A, semester B 5779 (01.07.2019).
5 questions of 25 points: Q1 mandatory (its part a: choose 3 of 5 concept items), Q2-Q5: choose 3 of 4 (scan).
The handwritten key (blue ink, author unknown) is student-solution. Checks: tools/verify/19S-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_19S-A.py
 - Printed sub-part labels (a1, c2, ...) become sequential Hebrew letters (the validator wants one letter);
   the printed label is shown at the top of the stem.
 - Q2b (three asks) and Q2c (compute + decide) are ONE item each."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19S-A.json"

SEQ = {(1, "א1"): "א", (1, "א2"): "ב", (1, "א3"): "ג", (1, "א4"): "ד", (1, "א5"): "ה", (1, "ב"): "ו", (1, "ג"): "ז",
       (3, "ג1"): "ג", (3, "ג2"): "ד",
       (4, "א1"): "א", (4, "א2"): "ב", (4, "א3"): "ג", (4, "ב"): "ד", (4, "ג1"): "ה", (4, "ג2"): "ו"}


def Q(num, part, kind, topic, points, question, solution, **kw):
    if (num, part) in SEQ:
        if any(ch.isdigit() for ch in part):
            question = "**(" + part + ")** " + question
        part = SEQ[(num, part)]
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


INTRO = "יש לבחור 3 סעיפים מתוך ה-5 הבאים. בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א1", "proof", "logic_propositional", 5,
      INTRO + "**המונח:** פסוק מורכב.\n**שאלה:** תנו דוגמה לפסוק מורכב ודוגמה לפסוק אטומי/בסיסי.",
      "**הגדרה:** פסוק מורכב הוא פסוק שנוצר על ידי שימוש בפסוקים (אטומיים) ובקשרים לוגיים שמחברים בין הפסוקים האטומיים."
      "\n"
      "**דוגמה לפסוק מורכב:** \"1+1=2\" וגם \"3<5\"."
      "\n"
      "**דוגמה לפסוק אטומי (בסיסי):** \"היום יום א'\"."),

    Q(1, "א2", "proof", "sets_power_set", 5,
      INTRO + "**המונח:** הפרש סימטרי של קבוצות.\n"
      r"**שאלה:** תהי $A\ne\varnothing$. האם קיימות קבוצות $B_1,B_2$ כך ש: $A\Delta B_2=A$, $A\Delta B_1=\varnothing$ ? אם כן, רשמו דוגמה להן.",
      r"**הגדרה:** ההפרש הסימטרי של הקבוצות $A$ ו-$B$ הוא $A\Delta B=(A-B)\cup(B-A)$."
      "\n"
      r"**תשובה:** כן. נבחר $B_1=A$ ו-$B_2=\varnothing$."
      "\n"
      r"$A\Delta B_1=A\Delta A=(A-A)\cup(A-A)=\varnothing$, ו-$A\Delta B_2=A\Delta\varnothing=(A-\varnothing)\cup(\varnothing-A)=A\cup\varnothing=A$."
      "\n"
      r"מסקנה: קיימות קבוצות $B_1,B_2$ המתאימות."),

    Q(1, "א3", "proof", "relations_properties", 5,
      INTRO + "**המונח:** יחס טרנזיטיבי.\n"
      r"**שאלה:** תנו דוגמה לשני יחסים ששניהם טרנזיטיביים ורפלקסיביים $R_1,R_2\subset\{1,2,3\}\times\{1,2,3\}$ "
      r"כך ש: $R_1\Delta R_2$ הוא יחס סימטרי, אך לא אנטי-סימטרי.",
      r"**הגדרה:** תהי $A$ קבוצה, $R\subseteq A\times A$. נאמר כי $R$ יחס טרנזיטיבי אם מקיים התנאי: לכל $x,y,z\in A$, אם $xRy$ וגם $yRz$, אז $xRz$."
      "\n"
      r"**דוגמה:**"
      "\n"
      r"$R_1=\{(1,1),(2,2),(3,3),(1,2)\}$"
      "\n"
      r"$R_2=\{(1,1),(2,2),(3,3),(2,1)\}$"
      "\n"
      r"$R_1\Delta R_2=\{(1,2),(2,1)\}$"),

    Q(1, "א4", "proof", "partial_orders", 5,
      INTRO + "**המונח:** יחס סדר חלקי.\n"
      r"**שאלה:** תנו דוגמה ליחס סדר חלקי על הקבוצה $A=\{1,2\}$ שאינו יחס סדר מלא.",
      r"**הגדרה:** תהי $A$ קבוצה ו-$R\subseteq A\times A$. $R$ נקרא יחס סדר חלקי אם $R$ הוא רפלקסיבי, אנטי-סימטרי וטרנזיטיבי על $A$."
      "\n"
      r"**דוגמה:** $A=\{1,2\}$ ו-$R=\{(1,1),(2,2)\}$ הוא יחס סדר חלקי שאינו מלא (אין קשר בין 1 ל-2)."),

    Q(1, "א5", "computation", "functions", 5,
      INTRO + "**המונח:** פונקציה על.\n"
      r"**שאלה:** כמה פונקציות $f:\{1,2,3,4,5\}\to\{1,2,3,4,5\}$ ניתן להגדיר כך שכל פונקציה $f$ היא על וגם מקיימת את התנאי $f(\{1,2\})=\{1,2\}$ ?",
      r"**הגדרה:** תהי $f:A\to B$ פונקציה. $f$ נקראת על אם לכל $b\in B$ קיים $a\in A$ כך ש: $f(a)=b$, כלומר $f(A)=B$."
      "\n"
      r"מכיוון ש-$\{1,2,3,4,5\}=A=B$ ו-$|A|=|B|=5<\infty$, $f:A\to B$ על $\iff f$ חד-חד-ערכית $\iff f$ הפיכה."
      "\n"
      r"מ-$f(\{1,2\})=\{1,2\}$ נובע שיש $2!$ אפשרויות עבור $f$ על $\{1,2\}$; ו-$f(\{3,4,5\})=\{3,4,5\}$, ולכן יש $3!$ אפשרויות עבור $\{3,4,5\}$."
      "\n"
      r"לפי כלל המכפלה: $12=2!\cdot3!$ פונקציות מתאימות."),

    Q(1, "ב", "computation", "logic_propositional", 5,
      r"בנו צורת DNF עבור הפסוק: $(p\wedge q)\leftrightarrow(\neg q\vee r)$. העזר בטבלת אמת לפתרון השאלה.",
      "טבלת האמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | p∧q | ¬q | ¬q∨r | (p∧q)↔(¬q∨r)\n"
      "T T T |  T  |  F |   T   |       T\n"
      "T T F |  T  |  F |   F   |       F\n"
      "T F T |  F  |  T |   T   |       F\n"
      "T F F |  F  |  T |   T   |       F\n"
      "F T T |  F  |  F |   T   |       F\n"
      "F T F |  F  |  F |   F   |       T\n"
      "F F T |  F  |  T |   T   |       F\n"
      "F F F |  F  |  T |   T   |       F\n"
      "```\n"
      r"לכן צורת ה-DNF היא:"
      "\n"
      r"$$(p\wedge q\wedge r)\vee(\neg p\wedge q\wedge\neg r)$$"),

    Q(1, "ג", "proof", "quantifiers_proofs", 5,
      "שלולו את הטענה: “לכל $x\\in A$, קיים זוג $(y,z)\\in B\\times C$, כך ש: $x>y+z$” "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      "השלילה: “קיים $x\\in A$ כך שלכל זוג $(y,z)\\in B\\times C$ מתקיים: $x\\le y+z$”."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 10,
      r"הוכיחו באינדוקציה שלכל $1\le n\in\mathbb{N}$ מתקיים: "
      r"$\dfrac1{1\cdot5}+\dfrac1{5\cdot9}+\dfrac1{9\cdot13}+\ldots+\dfrac1{(4n-3)\cdot(4n+1)}=\dfrac n{4n+1}$",
      r"$P(n):\ \dfrac1{1\cdot5}+\dfrac1{5\cdot9}+\ldots+\dfrac1{(4n-3)(4n+1)}=\dfrac n{4n+1}$, לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ \dfrac1{1\cdot5}=\dfrac1{4+1}$ — הטענה נכונה."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $1\le k$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ \dfrac1{1\cdot5}+\ldots+\dfrac1{(4k-3)(4k+1)}=\dfrac k{4k+1}$"
      "\n"
      r"$P(k+1):\ \dfrac1{1\cdot5}+\ldots+\dfrac1{(4k-3)(4k+1)}+\dfrac1{(4k+1)(4k+5)}=\dfrac{k+1}{4k+5}$"
      "\n"
      r"לפי $P(k)$, הסכום עד $\dfrac1{(4k-3)(4k+1)}$ שווה ל-$\dfrac k{4k+1}$, ולכן אגף שמאל של $P(k+1)$ הוא:"
      "\n"
      r"$$\frac k{4k+1}+\frac1{(4k+1)(4k+5)}=\frac{k(4k+5)+1}{(4k+1)(4k+5)}=\frac{4k^2+5k+1}{(4k+1)(4k+5)}=\frac{4k^2+4k+k+1}{(4k+1)(4k+5)}=\frac{4k(k+1)+(k+1)}{(4k+1)(4k+5)}$$"
      "\n"
      r"$$=\frac{(4k+1)(k+1)}{(4k+1)(4k+5)}=\frac{k+1}{4k+5}$$"
      "\n"
      r"לכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**מסקנה:** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $1\le n\in\mathbb{N}$."),

    Q(2, "ב", "computation", "sets_power_set", 9,
      r"יהיו הקבוצות: $A=\{2^n\cdot3^m:\ m,n\in\{0,1,2,\ldots,9\}\}$, $B=\{2^n:\ n\in\{0,1,2,\ldots,9\}\}$ ו-$C=\{3^n:\ n\in\{0,1,2,\ldots,9\}\}$."
      "\n"
      r"חשבו: $|(B\times C)-(B\cup C)|$, $|B\Delta C|$, $|P(A\times B)\times C|$.",
      r"ההצבות: $|A|=10\cdot10=100$, $|B|=|C|=10$."
      "\n"
      r"$|P(A\times B)\times C|=|P(A\times B)|\cdot|C|=2^{|A\times B|}\cdot|C|=2^{|A|\cdot|B|}\cdot|C|=2^{100\cdot10}\cdot10=10\cdot2^{1000}$."
      "\n"
      r"$B\Delta C=(B-C)\cup(C-B)$, ו-$B\cap C=\{2^0\}=\{1\}=\{3^0\}$. לכן $|B\Delta C|=|B-C|+|C-B|=9+9=18$."
      "\n"
      r"$(B\times C)-(B\cup C)=B\times C$, כי איברי $B\times C$ הם זוגות סדורים ואיברי $B\cup C$ הם מספרים, ולכן $(B\times C)\cap(B\cup C)=\varnothing$. "
      r"לכן $|(B\times C)-(B\cup C)|=|B\times C|=|B|\cdot|C|=100$."),

    Q(2, "ג", "computation", "combinatorics", 6,
      r"חשבו את הסכום $f(n)=\sum_{k=0}^{n}\binom nk4^k$. האם $f(n)=O(4^n)$ ?",
      r"$f(n)=\sum_{k=0}^{n}\binom nk4^k=\sum_{k=0}^{n}\binom nk4^k1^{n-k}=(4+1)^n=5^n$."
      "\n"
      r"האם $f(n)=5^n=O(4^n)$ ? נניח בשלילה ש-$5^n=O(4^n)$: אז קיימים $c_0>0$ ו-$n_0\in\mathbb{N}$ כך ש-$5^n\le c_0\cdot4^n$ לכל $n_0\le n\in\mathbb{N}$, "
      r"כלומר $\dfrac{5^n}{4^n}\le c_0$ לכל $n_0\le n\in\mathbb{N}$."
      "\n"
      r"אך $\lim_{n\to\infty}\left(\dfrac54\right)^n=\infty\le c_0$, סתירה."
      "\n"
      r"מסקנה: $f(n)\ne O(4^n)$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "equivalence_relations", 8,
      r"יהי נתון היחס $R\subseteq(\mathbb{Z}-\{0\})\times(\mathbb{Z}-\{0\})$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}-\{0\}$, מתקיים $x\cdot y>0\iff xRy$."
      "\n"
      r"הוכיחו ש: $R$ הוא יחס שקילות ומצאו את קבוצת המנה $(\mathbb{Z}-\{0\})/R$.",
      r"**(1) $R$ רפלקסיבי:** לכל $x\in\mathbb{Z}-\{0\}$ מתקיים $xRx$. הטענה נכונה כי $xRx\iff x\cdot x>0$, ולכן $x\ne0$."
      "\n"
      r"**(2) $R$ סימטרי:** לכל $x,y\in\mathbb{Z}-\{0\}$, אם $xRy$ אז $yRx$, כי $xRy\iff x\cdot y>0\iff y\cdot x>0\iff yRx$."
      "\n"
      r"**(3) $R$ טרנזיטיבי:** לכל $x,y,z\in\mathbb{Z}-\{0\}$, אם $xRy$ ו-$yRz$ אז $xRz$. אכן, $xy>0\iff xRy$ ו-$yz>0\iff yRz$, ולכן $x\cdot y^2\cdot z>0$. "
      r"מכיוון ש-$y\ne0$, $y^2>0$, ולכן $xz>0$, כלומר $xRz$."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}-\{0\}\wedge x\cdot1>0\}=\{x:\ x\in\mathbb{Z}-\{0\},\ x>0\}$"
      "\n"
      r"$[-1]=\{x:\ x\in\mathbb{Z}-\{0\}\wedge x\cdot(-1)>0\}=\{x:\ x\in\mathbb{Z}-\{0\},\ x<0\}$"
      "\n"
      r"$[-1]\cup[1]=\mathbb{Z}-\{0\}$ ו-$[-1]\cap[1]=\varnothing$, ולכן $(\mathbb{Z}-\{0\})/R=\{[-1],[1]\}$."),

    Q(3, "ב", "proof", "sets_power_set", 8,
      "נסחו את ה-contrapositive של הטענה הבאה: "
      "“תהיינה $A,B$ שתי קבוצות לא ריקות. אם $P(A\\cup B)=P(A)\\cup P(B)$, אז $A\\subseteq B$ או $B\\subseteq A$.” "
      "הוכיחו את הטענה.",
      "ה-contrapositive הוא: “תהיינה $A,B$ שתי קבוצות לא ריקות. אם $B\\not\\subseteq A$ וגם $A\\not\\subseteq B$, אז $P(A\\cup B)\\ne P(A)\\cup P(B)$.”"
      "\n"
      r"**הוכחה** (נבדוק את ה-contrapositive): $B\not\subseteq A$ וגם $A\not\subseteq B$ גורר שקיימים $b\in B-A$ וגם $a\in A-B$."
      "\n"
      r"$\{a,b\}\subseteq A\cup B$, כלומר $\{a,b\}\in P(A\cup B)$."
      "\n"
      r"$\{a,b\}\not\subseteq A$ (כי $b\notin A$) ו-$\{a,b\}\not\subseteq B$ (כי $a\notin B$), ולכן $\{a,b\}\notin P(A)\cup P(B)$."
      "\n"
      r"מסקנה: $P(A\cup B)\ne P(A)\cup P(B)$."),

    Q(3, "ג1", "computation", "combinatorics", 3,
      r"נתונים $n\ge10$ ו-$A=\{1,2,3,\ldots,n\}$. חשבו את $\left|\{B:\ B\in P(A)\wedge\{1,2,3,4\}\cap B=\varnothing\wedge7\in B\}\right|$.",
      r"לפי ההגדרה: $B=\{7\}\cup C$, כאשר $C\subseteq\{5,6,8,\ldots,n\}$, כלומר $C\in P(\{5,6,8,\ldots,n\})$."
      "\n"
      r"מספר ה-$B$-ים שווה למספר ה-$C$-ים: $|P(\{5,6,8,\ldots,n\})|=2^{|\{5,6,8,\ldots,n\}|}=2^{n-5}$, כי $|\{5,6,8,\ldots,n\}|=|\{1,2,\ldots,n\}-\{1,2,3,4,7\}|=n-5$."),

    Q(3, "ג2", "computation", "modular_fermat_wilson", 6,
      r"תהי $S$ קבוצה בת 8 איברים. חשבו את $\varnothing(m^2)$, כאשר $\varnothing$ היא פונקציית Euler ו-$m$ הוא מספר תתי-הקבוצות בגודל 4 של הקבוצה $S$.",
      r"נתון: $S$ היא קבוצה בת 8 איברים, ולכן $m=\binom84$ הוא מספר תתי-הקבוצות בגודל 4."
      "\n"
      r"$m=\dfrac{8!}{4!\,4!}=\dfrac{5\cdot6\cdot7\cdot8}{2\cdot3\cdot4}=70=2\cdot5\cdot7$."
      "\n"
      r"$\varnothing(m^2)=\varnothing(70^2)=\varnothing(2^2\cdot5^2\cdot7^2)=70^2\left(1-\frac12\right)\left(1-\frac15\right)\left(1-\frac17\right)=70\cdot70\cdot\frac12\cdot\frac45\cdot\frac67=70\cdot24=1680$."),

    # ---------------- Q4 ----------------
    Q(4, "א1", "computation", "functions", 3,
      r"$F$ מסומנת ב-$F$ קבוצת כל הפונקציות $f:\{1,2,3,4\}\to\{1,2,3,4,5,6\}$. כמה פונקציות יש ב-$F$ ?",
      r"$f$ היא פונקציה $\iff$ נבחר את $f(1),f(2),f(3),f(4)$: $f(1)\in\{1,\ldots,6\}$ — 6 אפשרויות, וכן הלאה לכל אחד מארבעת האיברים."
      "\n"
      r"מסקנה: $|F|=6^4$."),

    Q(4, "א2", "computation", "combinatorics", 3,
      r"$F$ היא קבוצת כל הפונקציות $f:\{1,2,3,4\}\to\{1,2,3,4,5,6\}$. כמה פונקציות מ-$F$ הן יורדות ממש?",
      r"$f\in F$ יורדת ממש $\iff f(1)>f(2)>f(3)>f(4)$. כל תת-קבוצה של $\{1,2,\ldots,6\}$ בגודל 4 מגדירה פונקציה אחת בלבד שיורדת ממש: $\{f(1),f(2),f(3),f(4)\}$."
      "\n"
      r"לכן מספר הפונקציות היורדות ממש הוא $\binom64=\binom62=\dfrac{6\cdot5}{1\cdot2}=15$."),

    Q(4, "א3", "computation", "functions", 4,
      r"$F$ היא קבוצת כל הפונקציות $f:\{1,2,3,4\}\to\{1,2,3,4,5,6\}$. כמה פונקציות מ-$F$ הן חד-חד-ערכיות ומקיימות $f(\{1,2\})=\{1,2\}$ ?",
      r"עבור $f\in F$ חד-חד-ערכית עם $f(\{1,2\})=\{1,2\}$: יש $2!$ אפשרויות עבור $f$ על $\{1,2\}$; ועבור $f(3),f(4)$ — $P(4,2)$ אפשרויות "
      r"(שני ערכים שונים מתוך $\{3,4,5,6\}$)."
      "\n"
      r"לפי כלל המכפלה: $24=4!=2!\cdot\dfrac{4!}{2!}$ פונקציות מתאימות."),

    Q(4, "ב", "computation", "combinatorics", 7,
      r"כמה תתי-קבוצות $S$ של $\{2,3,\ldots\}$ מקיימות את התנאים הבאים: $S=\{a,b,c\}$ וגם $a\cdot b\cdot c=3\cdot5\cdot7\cdot11\cdot13$ ?",
      r"דוגמה: $S=\{15,7,143\}\iff a=3\cdot5,\ b=7,\ c=11\cdot13$, כלומר $\{\{3,5\},\{7\},\{11,13\}\}$ היא חלוקה של $\{3,5,7,11,13\}$ ל-3 קבוצות."
      "\n"
      r"כל חלוקה של $\{3,5,7,11,13\}$ ל-3 קבוצות מגדירה בדיוק קבוצה $S$ אחת, ולהפך. לכן מספר הקבוצות $S$ שווה למספר STIRLING:"
      "\n"
      r"$S(5,3)$, כאשר $S(n,n)=S(n,1)=1$ ו-$S(n,k)=S(n-1,k-1)+k\cdot S(n-1,k)$."
      "\n"
      r"$S(3,2)=S(2,1)+2S(2,2)=1+2\cdot1=3$"
      "\n"
      r"$S(4,2)=S(3,1)+2S(3,2)=1+2\cdot3=7$"
      "\n"
      r"$S(4,3)=S(3,2)+3S(3,3)=3+3\cdot1=6$"
      "\n"
      r"$S(5,3)=S(4,2)+3S(4,3)=7+3\cdot6=7+18=25$"),

    Q(4, "ג1", "computation", "combinatorics", 4,
      r"תהי $A=\{1,2,3,4,5,6\}$. כמה מספרים זוגיים בעלי 4 ספרות שונות ניתן ליצור מ-$A$ ?",
      r"הספרה האחרונה צריכה להיות 2, 4 או 6: 3 אפשרויות. לספרה הראשונה 5 אפשרויות, לשנייה 4 ולשלישית 3."
      "\n"
      r"מסקנה: ניתן ליצור $5\cdot4\cdot3\cdot3=180$ מספרים מתאימים."),

    Q(4, "ג2", "computation", "combinatorics", 4,
      r"תהי $A=\{1,2,3,4,5,6\}$. מהו מספר התמורות של $A$ שבהן המספרים $1,2,3$ נמצאים בסמיכות?",
      r"נתייחס לבלוק $1,2,3$ כאל יחידה אחת: יש $4!$ סידורים של 4 היחידות ($1,2,3$ כבלוק, $4,5,6$), ו-$3!$ סידורים פנימיים של הבלוק."
      "\n"
      r"לכן מספר התמורות הוא $144=24\cdot6=4!\cdot3!$."),

    # ---------------- Q5 ----------------
    Q(5, "א", "proof", "modular_fermat_wilson", 10,
      r"אם $3<n\in\mathbb{N}$ הוא מספר שמקיים $3\mid n$, הראו ש: $3\cdot\varnothing(n)=\varnothing(3n)$, כאשר $\varnothing$ היא פונקציית Euler. "
      r"רמז: היעזרו בנוסחת אוילר ל-$n$ כללי.",
      r"$3\mid n\iff n=3^\alpha\cdot m$ עבור $1\le\alpha$ ו-$\gcd(3,m)=1$."
      "\n"
      r"$\varnothing(n)=\varnothing(3^\alpha)\cdot\varnothing(m)=3^\alpha\left(1-\frac13\right)\varnothing(m)=3^{\alpha-1}\cdot2\cdot\varnothing(m)$."
      "\n"
      r"$\varnothing(3n)=\varnothing(3^{\alpha+1}\cdot m)=\varnothing(3^{\alpha+1})\varnothing(m)=3^{\alpha+1}\left(1-\frac13\right)\varnothing(m)=3\cdot3^{\alpha-1}\cdot2\cdot\varnothing(m)=3\varnothing(n)$."
      "\n"
      r"מסקנה: $\varnothing(3n)=3\varnothing(n)$."),

    Q(5, "ב", "proof", "cardinality_sets", 7,
      r"הוכיחו ש: $\left|(\mathbb{Q}\cap[1,5])\cup(\mathbb{Z}\cap[20.5,100.5])\right|=|\mathbb{Z}|$.",
      r"נסמן $A=(\mathbb{Q}\cap[1,5])\cup(\mathbb{Z}\cap[20.5,100.5])$."
      "\n"
      r"מכיוון ש-$A\subseteq\mathbb{Q}$, $|A|\le|\mathbb{Q}|$."
      "\n"
      r"ב-$A$ יש תת-קבוצה אינסופית שניתנת לסידור בסדרה של $\mathbb{N}$: $B=\left\{1+\frac12,\ 1+\frac13,\ 1+\frac14,\ \ldots,\ 1+\frac1n,\ \ldots\right\}$."
      "\n"
      r"$|\mathbb{Z}|=|\mathbb{N}|=|B|\le|A|\le|\mathbb{Q}|=|\mathbb{N}|=|\mathbb{Z}|$."
      "\n"
      r"מסקנה: $|A|=|\mathbb{Z}|$."),

    Q(5, "ג", "computation", "recurrence_sums", 8,
      r"מצאו את הצורה המפורשת של $(F_n)$, כאשר: $F_0=0$, $F_1=1$ ו-$F_n=F_{n-1}+F_{n-2}$, $n\ge2$.",
      r"נציב $F_n=r^n$: $r^n=r^{n-1}+r^{n-2}$, ונחלק ב-$r^{n-2}$: $r^2-r-1=0$."
      "\n"
      r"$r_{1,2}=\dfrac{1\pm\sqrt5}2$, כלומר $r_1=\dfrac{1-\sqrt5}2$ ו-$r_2=\dfrac{1+\sqrt5}2$, $r_1\ne r_2$."
      "\n"
      r"$F_n=C_1r_1^n+C_2r_2^n$."
      "\n"
      r"$F_0=C_1+C_2=0\Rightarrow C_1=-C_2$, ו-$F_1=C_1r_1+C_2r_2=1$, ולכן $C_2(r_2-r_1)=1$, כלומר $C_2=\dfrac1{r_2-r_1}=\dfrac1{\sqrt5}$ ו-$C_1=\dfrac{-1}{\sqrt5}$."
      "\n"
      r"מסקנה: $F_n=-\dfrac1{\sqrt5}\left(\dfrac{1-\sqrt5}2\right)^n+\dfrac1{\sqrt5}\left(\dfrac{1+\sqrt5}2\right)^n$, לכל $n\in\mathbb{N}$."),
]

exam = {
    "examCode": "19S-A",
    "examLabel": 'בדידה 1, סמסטר ב\' תשע"ט, מועד א (01.07.2019)',
    "year": 2019,
    "examDate": "01.07.2019",
    "sourceFile": "19S-A exam with handwritten solution, pp.1-18",
    "solutionFile": "19S-A handwritten solution (author unknown), pp.4-18",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
