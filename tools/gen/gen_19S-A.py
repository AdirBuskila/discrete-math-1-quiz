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


# ---- steps / rubric / pitfalls (ai-draft); every expected value is recomputed in tools/verify/<CODE>/verify.py ----
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
            assert 2 <= len(rubric) <= 5 and 1 <= len(pitfalls) <= 3, (num_, part)
            q.update(rubric=rubric, rubricSource="ai-verified", pitfalls=pitfalls, steps=steps, stepsSource="ai-verified")
            return
    raise KeyError((num_, part))


put(1, "א",
    rub(("הגדרה: פסוק מורכב נבנה מפסוקים אטומיים וקשרים לוגיים", 2),
        ("דוגמה לפסוק מורכב (שני פסוקים אטומיים וקשר)", 2),
        ("דוגמה לפסוק אטומי (פסוק בסיסי בלי קשרים)", 1)),
    ["לתת כדוגמה לפסוק מורכב משפט שאין בו קשר לוגי.",
     "לתת כדוגמה לפסוק אטומי משפט שאינו פסוק, כמו שאלה."],
    [ch("איזה מהפסוקים הבאים הוא אטומי?",
        r"$p$", r"$p\wedge q$", r"$\neg p$", r"$p\to q$",
        explain="פסוק אטומי אינו כולל אף קשר לוגי."),
     num(r"כמה שורות יש בטבלת האמת של פסוק מורכב שבנוי משני פסוקים אטומיים שונים?", 4, r"$2^2=4$.")])

put(1, "ב",
    rub(("הגדרה: ההפרש הסימטרי $A\\Delta B=(A-B)\\cup(B-A)$", 2),
        (r"$B_1=A$ נותן $A\Delta A=\varnothing$", 1),
        (r"$B_2=\varnothing$ נותן $A\Delta\varnothing=A$", 1),
        ("מסקנה: קיימות קבוצות כאלה", 1)),
    [r"לבחור $B_1=\varnothing$: אז $A\Delta B_1=A\ne\varnothing$.",
     r"להחליף בין התפקידים של $B_1$ ו-$B_2$."],
    [ch(r"איזו קבוצה $B_1$ מקיימת $A\Delta B_1=\varnothing$ (לכל $A\ne\varnothing$)?",
        r"$B_1=A$", r"$B_1=\varnothing$", r"$B_1=A\cup\{a\}$ עבור $a\notin A$", r"$B_1=A-\{a\}$ עבור $a\in A$",
        explain=r"$A\Delta B=\varnothing$ בדיוק כש-$A=B$."),
     ch(r"איזו קבוצה $B_2$ מקיימת $A\Delta B_2=A$ (לכל $A\ne\varnothing$)?",
        r"$B_2=\varnothing$", r"$B_2=A$", r"$B_2=A\cup\{a\}$ עבור $a\notin A$", r"$B_2=A-\{a\}$ עבור $a\in A$",
        explain=r"$A\Delta B=A$ בדיוק כש-$B=\varnothing$."),
     num(r"מהו $|A\Delta B|$ עבור $A=\{1,2,3\}$ ו-$B=\{3,4\}$?", 3, r"$A\Delta B=\{1,2,4\}$.")])

put(1, "ג",
    rub(("הגדרה: יחס טרנזיטיבי", 1),
        (r"בחירת $R_1,R_2$ רפלקסיביים וטרנזיטיביים", 2),
        (r"חישוב $R_1\Delta R_2=\{(1,2),(2,1)\}$", 1),
        ("סימטרי אך לא אנטי-סימטרי", 1)),
    [r"לבחור $R_1=R_2$: אז $R_1\Delta R_2=\varnothing$, שהוא גם אנטי-סימטרי.",
     r"לבחור יחסים שאינם רפלקסיביים, או שאינם טרנזיטיביים."],
    [ch(r"איזה זוג יחסים על $\{1,2,3\}$ עונה על כל הדרישות?",
        r"$R_1=D\cup\{(1,2)\}$ ו-$R_2=D\cup\{(2,1)\}$, כאשר $D$ יחס הזהות",
        r"$R_1=R_2=D\cup\{(1,2)\}$",
        r"$R_1=D\cup\{(1,2)\}$ ו-$R_2=D\cup\{(1,2),(2,1)\}$",
        r"$R_1=D$ ו-$R_2=D\cup\{(1,3)\}$",
        explain=r"בשלוש האחרות ההפרש הסימטרי ריק, או לא סימטרי."),
     num(r"כמה זוגות יש ב-$R_1\Delta R_2$ בדוגמה הנכונה?", 2, r"$\{(1,2),(2,1)\}$.")])

put(1, "ד",
    rub(("הגדרה: סדר חלקי", 2),
        (r"בחירת $R=\{(1,1),(2,2)\}$ על $A=\{1,2\}$", 1),
        ("בדיקת רפלקסיבי, אנטי-סימטרי וטרנזיטיבי", 1),
        ("הסבר שאינו מלא: 1 ו-2 אינם ניתנים להשוואה", 1)),
    ["לבחור יחס שהוא סדר מלא.",
     r"לבחור יחס שמכיל את $(1,2)$ ואת $(2,1)$: אינו אנטי-סימטרי."],
    [ch(r"איזה יחס על $\{1,2\}$ הוא סדר חלקי שאינו סדר מלא?",
        r"$\{(1,1),(2,2)\}$", r"$\{(1,1),(2,2),(1,2)\}$", r"$\{(1,1),(2,2),(2,1)\}$", r"$\{(1,1),(2,2),(1,2),(2,1)\}$",
        explain=r"האפשרויות האמצעיות הן סדרים מלאים, והאחרונה אינה אנטי-סימטרית."),
     num(r"כמה יחסי סדר חלקי יש על $\{1,2\}$?", 3, r"יחס הזהות, ועוד כל אחד משני הזוגות $(1,2)$ או $(2,1)$."),
     num(r"כמה מהם הם סדר מלא?", 2, r"אלה שמכילים את אחד הזוגות $(1,2)$, $(2,1)$.")])

put(1, "ה",
    rub(("הגדרה: פונקציה על", 1),
        ("על בקבוצה סופית מעצמה לעצמה שקול להפיכה", 1),
        (r"$2!$ אפשרויות על $\{1,2\}$", 1),
        (r"$3!$ אפשרויות על $\{3,4,5\}$", 1),
        (r"כפל: $2!\cdot3!=12$", 1)),
    ["לשכוח ש-$f(\\{3,4,5\\})=\\{3,4,5\\}$ נובע מההפיכות.",
     r"לחשב $5!=120$ בלי התנאי, או לחבר במקום להכפיל."],
    [num(r"כמה דרכים יש להגדיר את $f$ על $\{1,2\}$ כך ש-$f(\{1,2\})=\{1,2\}$ (ו-$f$ הפיכה)?", 2, r"$2!=2$."),
     num(r"כמה דרכים יש להגדיר את $f$ על $\{3,4,5\}$ בהתאם?", 6, r"$3!=6$."),
     num(r"כמה פונקציות על מקיימות את התנאי?", 12, r"$2\cdot6=12$.")])

put(1, "ו",
    rub(("בניית טבלת אמת בת 8 שורות עם עמודות ביניים", 2),
        ("זיהוי שתי השורות שבהן הפסוק אמת", 1),
        ("כתיבת מונח צירופי לכל שורה", 1),
        ("חיבור שני המונחים בדיסיונקציה", 1)),
    [r"לטעות בטבלת האמת של $\leftrightarrow$: היא אמת כששני האגפים שווים, גם כששניהם שקר.",
     r"לפספס את השורה $p=F,q=T,r=F$ שבה שני האגפים שקריים.",
     "במונח של שורה לשכוח לשלול משתנה ששערכו שקר."],
    [num(r"בכמה מ-8 ההשמות הפסוק $(p\wedge q)\leftrightarrow(\neg q\vee r)$ אמת?", 2, "בדיקת כל 8 השורות."),
     ch(r"איזו השמה מספקת את הפסוק $(p\wedge q)\leftrightarrow(\neg q\vee r)$?",
        r"$p=F,\ q=T,\ r=F$", r"$p=T,\ q=T,\ r=F$", r"$p=T,\ q=F,\ r=T$", r"$p=F,\ q=F,\ r=F$",
        explain="בהשמה הראשונה שני האגפים שקריים; בשאר האגפים שונים."),
     ch(r"מהו המונח ב-DNF שמתאים להשמה $p=F,\ q=T,\ r=F$?",
        r"$\neg p\wedge q\wedge\neg r$", r"$p\wedge q\wedge r$", r"$\neg p\wedge\neg q\wedge\neg r$", r"$p\vee\neg q\vee r$",
        explain="משתנה ששערכו שקר נכתב בשלילה, ומשתנה ששערכו אמת נכתב כמו שהוא.")])

put(1, "ז",
    rub(("שלילת \"לכל $x$\": הופך ל\"קיים $x$\"", 1),
        ("שלילת \"קיים זוג $(y,z)$\": הופך ל\"לכל זוג $(y,z)$\"", 2),
        (r"שלילת הגוף: $x>y+z$ הופך ל-$x\le y+z$", 2)),
    ["להפוך רק חלק מהכמתים.",
     r"לכתוב $x<y+z$ ולשכוח את מקרה השוויון."],
    [ch("מהי שלילת הטענה, ללא קשר השלילה?",
        r"קיים $x\in A$ כך שלכל זוג $(y,z)\in B\times C$ מתקיים $x\le y+z$",
        r"לכל $x\in A$ ולכל זוג $(y,z)\in B\times C$ מתקיים $x\le y+z$",
        r"קיים $x\in A$ כך שקיים זוג $(y,z)\in B\times C$ עם $x\le y+z$",
        r"קיים $x\in A$ כך שלכל זוג $(y,z)\in B\times C$ מתקיים $x<y+z$",
        explain="כל הכמתים מתהפכים וגם הגוף נשלל במדויק."),
     ch(r"מהי שלילת $x>y+z$?",
        r"$x\le y+z$", r"$x<y+z$", r"$x\ge y+z$", r"$x=y+z$",
        explain=r"הערכים שבהם $x>y+z$ שקרי הם $x<y+z$ וגם $x=y+z$.")])

_si = [r"אגף שמאל של $P(k+1)$ לפי $P(k)$: $\frac k{4k+1}+\frac1{(4k+1)(4k+5)}$",
       r"$=\frac{k(4k+5)+1}{(4k+1)(4k+5)}$",
       r"$=\frac{4k^2+5k+1}{(4k+1)(4k+5)}$",
       r"$=\frac{(4k+1)(k+1)}{(4k+1)(4k+5)}$",
       r"$=\frac{k+1}{4k+5}$, כלומר $P(k+1)$ נכון"]
put(2, "א",
    rub(("בדיקת בסיס $n=1$: $\\frac15=\\frac15$", 2),
        (r"ניסוח הנחת האינדוקציה $P(k)$ והוספת האיבר $\frac1{(4k+1)(4k+5)}$ לאגף שלה", 3),
        (r"מכנה משותף ופישוט עד $\frac{4k^2+5k+1}{(4k+1)(4k+5)}$", 2),
        (r"פירוק $4k^2+5k+1=(4k+1)(k+1)$ וצמצום", 2),
        ("מסקנה לפי עקרון האינדוקציה", 1)),
    [r"להוסיף את האיבר הלא נכון: האיבר החדש הוא $\frac1{(4k+1)(4k+5)}$ ולא $\frac1{(4k+5)(4k+9)}$.",
     "לא לצמצם את הגורם $4k+1$ ולהיתקע בביטוי מורכב.",
     "להשתמש ב-$P(k+1)$ בהוכחה שלו."],
    [ch(r"מהו הערך של האגף השמאלי עבור $n=2$?",
        r"$\frac29$", r"$\frac15$", r"$\frac14$", r"$\frac19$",
        explain=r"$\frac1{1\cdot5}+\frac1{5\cdot9}=\frac15+\frac1{45}=\frac{10}{45}=\frac29$, כמו $\frac n{4n+1}$."),
     ch(r"לאיזה מכפלה מתפרק $4k^2+5k+1$?",
        r"$(4k+1)(k+1)$", r"$(4k+5)(k+1)$", r"$(4k+1)(k+5)$", r"$(2k+1)^2$",
        explain=r"$(4k+1)(k+1)=4k^2+5k+1$."),
     order("סדרו את שלבי הצעד.", _si, "הנחה, מכנה משותף, פתיחה, פירוק וצמצום."),
     bug("בגרסה הבאה של הצעד שורה אחת שגויה. מצאו אותה.", mutate(_si, 3, r"$=\frac{(4k+5)(k+1)}{(4k+1)(4k+5)}$"), 3,
         r"$4k^2+5k+1=(4k+1)(k+1)$ ולא $(4k+5)(k+1)$.")])

put(2, "ב",
    rub((r"$|A|=100$ ו-$|B|=|C|=10$", 1),
        (r"$B\cap C=\{1\}$", 1),
        (r"$|B\Delta C|=9+9=18$", 2),
        (r"$B\times C$ מכיל זוגות סדורים ו-$B\cup C$ מספרים, ולכן $(B\times C)-(B\cup C)=B\times C$ בגודל 100", 3),
        (r"$|P(A\times B)\times C|=2^{|A||B|}\cdot|C|=10\cdot2^{1000}$", 2)),
    [r"לחשב $|B\Delta C|=20$ בלי להפחית את האיבר המשותף $1$.",
     r"לחסר 10 או 19 מ-$|B\times C|$ בחיסור $B\cup C$: איבריהן מסוגים שונים.",
     r"לכתוב $|P(X)|=|X|^2$ במקום $2^{|X|}$."],
    [num(r"כמה איברים משותפים יש ל-$B$ ול-$C$?", 1, r"רק $1=2^0=3^0$."),
     num(r"מהו $|B\Delta C|$?", 18, r"$9+9=18$."),
     num(r"מהו $|(B\times C)-(B\cup C)|$?", 100, r"$|B\times C|=10\cdot10$."),
     ch(r"מהו $|P(A\times B)\times C|$?",
        r"$10\cdot2^{1000}$", r"$10\cdot2^{100}$", r"$2^{1000}+10$", r"$2^{10000}$",
        explain=r"$|A\times B|=100\cdot10=1000$, ולכן $|P(A\times B)|=2^{1000}$ וכופלים ב-$|C|=10$.")])

put(2, "ג",
    rub((r"משפט הבינום: $\sum\binom nk4^k1^{n-k}=(4+1)^n=5^n$", 2),
        ("הנחת השלילה: קיימים $c_0,n_0$ כך ש-$5^n\\le c_0 4^n$", 1),
        (r"$(5/4)^n\le c_0$ לכל $n\ge n_0$", 1),
        (r"$\lim(5/4)^n=\infty$, סתירה", 1),
        (r"מסקנה: $f(n)\ne O(4^n)$", 1)),
    [r"לחשב $(4+1)^n$ בלי לזהות את הבינום, או לכתוב $4^n$.",
     "להסיק $5^n=O(4^n)$ כי הבסיסים קרובים: היחס בין החזקות גדל בלי גבול."],
    [num(r"מהו $\sum_{k=0}^{3}\binom3k4^k$?", 125, r"$(4+1)^3=125$."),
     ch(r"באיזו שיטה משתמש הפתרון כדי להראות ש-$5^n\ne O(4^n)$?",
        r"בשלילה: מניחים $5^n\le c_0\cdot4^n$ ומראים ש-$(5/4)^n$ אינו חסום",
        r"מראים ש-$\lim4^n/5^n=\infty$", "אינדוקציה על $n$", r"מוצאים $c_0=1$ ו-$n_0=1$",
        explain=r"הגבול של $4^n/5^n$ הוא $0$ ולא $\infty$."),
     num(r"מהו ה-$n$ הקטן ביותר שעבורו $(5/4)^n>100$?", 21, r"$1.25^{20}\approx86.7$ ו-$1.25^{21}\approx108.4$.")])

_t19s = [r"נניח $xy>0$ וגם $yz>0$",
         r"נכפיל: $(xy)(yz)=xz\cdot y^2>0$, ומכיוון ש-$y\ne0$ מתקיים $y^2>0$",
         r"מחלקים ב-$y^2$ ומקבלים $xz>0$, כלומר $xRz$"]
put(3, "א",
    rub((r"רפלקסיביות ($x\cdot x>0$ כי $x\ne0$) וסימטריה ($xy=yx$)", 2),
        (r"טרנזיטיביות: מכפלת ההנחות $xzy^2>0$ ולכן $xz>0$", 2),
        ("מסקנה: יחס שקילות", 1),
        (r"מחלקות $[1]$ (החיוביים) ו-$[-1]$ (השליליים)", 2),
        (r"קבוצת המנה $\{[1],[-1]\}$", 1)),
    [r"לשכוח ש-$0$ אינו בתחום, ולכן $x^2>0$.",
     "לבדוק רק שתיים משלוש התכונות.",
     "לטעות במספר המחלקות: אין מחלקה לכל מספר שלם."],
    [ch(r"מהי מחלקת השקילות $[1]$?",
        r"$\{x\in\mathbb{Z}-\{0\}:\ x>0\}$", r"$\{x\in\mathbb{Z}-\{0\}:\ x<0\}$", r"$\{1\}$", r"$\mathbb{Z}-\{0\}$",
        explain=r"$1Rx\iff x>0$."),
     num(r"כמה מחלקות שקילות יש ב-$(\mathbb{Z}-\{0\})/R$?", 2, "החיוביים והשליליים."),
     order("סדרו את שלבי הוכחת הטרנזיטיביות.", _t19s, "הנחות, כפל, חילוק."),
     bug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", mutate(_t19s, 1, r"נכפיל: $(xy)(yz)=xz\cdot y>0$, ומכיוון ש-$y\ne0$ מתקיים $y^2>0$"), 1,
         r"$(xy)(yz)=xz\cdot y^2$ ולא $xz\cdot y$.")])

_cp = [r"קיימים $b\in B-A$ וגם $a\in A-B$, כי $B\not\subseteq A$ וגם $A\not\subseteq B$",
       r"$\{a,b\}\in P(A\cup B)$, אך $\{a,b\}\notin P(A)\cup P(B)$ (כי $b\notin A$ וגם $a\notin B$)",
       r"לכן $P(A\cup B)\ne P(A)\cup P(B)$"]
put(3, "ב",
    rub(("ניסוח ה-contrapositive: שלילת המסקנה גוררת שלילת ההנחה", 3),
        (r"בחירת $a\in A-B$ ו-$b\in B-A$", 2),
        (r"$\{a,b\}\in P(A\cup B)$ אך לא ב-$P(A)\cup P(B)$", 2),
        ("מסקנה: אי-השוויון בין הקבוצות", 1)),
    ["להחליף את ה-contrapositive בהיפוך (converse) של הטענה.",
     r"לשכוח שהשלילה של ”$A\subseteq B$ או $B\subseteq A$\" היא ”וגם” בין שני אי-ההכלות."],
    [ch("מהו ה-contrapositive של הטענה?",
        r"אם $B\not\subseteq A$ וגם $A\not\subseteq B$, אז $P(A\cup B)\ne P(A)\cup P(B)$",
        r"אם $A\subseteq B$ או $B\subseteq A$, אז $P(A\cup B)=P(A)\cup P(B)$",
        r"אם $P(A\cup B)\ne P(A)\cup P(B)$, אז $B\not\subseteq A$ וגם $A\not\subseteq B$",
        r"אם $B\not\subseteq A$ או $A\not\subseteq B$, אז $P(A\cup B)\ne P(A)\cup P(B)$",
        explain="ה-contrapositive של \"אם P אז Q\" הוא \"אם לא Q אז לא P\"; בשלילת \"או\" מקבלים \"וגם\"."),
     num(r"עבור $A=\{1,2\}$ ו-$B=\{2,3\}$: בכמה איברים $P(A\cup B)$ גדולה מ-$P(A)\cup P(B)$?", 2,
         r"$8-6=2$: הקבוצות $\{1,3\}$ ו-$\{1,2,3\}$."),
     order("סדרו את שלבי ההוכחה של ה-contrapositive.", _cp, "בחירת איברים, הצבעה על קבוצה, מסקנה.")])

put(3, "ג",
    rub((r"$B=\{7\}\cup C$ כאשר $C$ מוכלת ב-$\{5,6,8,\ldots,n\}$", 1),
        (r"גודל $\{5,6,8,\ldots,n\}$ הוא $n-5$", 1),
        (r"$2^{n-5}$", 1)),
    [r"לשכוח שגם $7$ מוצא מהאיברים החופשיים: חופשיים $n-5$ ולא $n-4$.",
     r"לספור $n-5$ במקום $2^{n-5}$."],
    [num(r"כמה קבוצות $B$ מקיימות את התנאים כש-$n=10$?", 32, r"$2^{10-5}=32$."),
     ch(r"כמה קבוצות $B$ מקיימות את התנאים?",
        r"$2^{n-5}$", r"$2^{n-4}$", r"$2^{n-6}$", r"$n-5$",
        explain=r"האיברים $1,2,3,4$ נאסרים ו-$7$ חייב להיכלל; $n-5$ איברים חופשיים.")])

put(3, "ד",
    rub((r"$m=\binom84=70$", 2),
        (r"פירוק $70^2=2^2\cdot5^2\cdot7^2$", 1),
        ("נוסחת Euler עם הגורמים הראשוניים", 2),
        (r"$\varphi(m^2)=1680$", 1)),
    [r"לחשב $\varphi(m^2)=\varphi(m)^2$: הנוסחה הנכונה היא $m\cdot\varphi(m)$.",
     r"לחשב $\binom84=\frac{8!}{4!}$ בלי לחלק גם ב-$4!$ השני."],
    [num(r"מהו $m=\binom84$?", 70, r"$\frac{8!}{4!\,4!}=70$."),
     num(r"מהו $\varphi(70)$?", 24, r"$70\cdot\frac12\cdot\frac45\cdot\frac67=24$."),
     num(r"מהו $\varphi(m^2)$?", 1680, r"$70\cdot24=1680$.")])

put(4, "א",
    rub(("בחירת $f(1),f(2),f(3),f(4)$ בלתי תלויה", 1),
        ("לכל ערך 6 אפשרויות", 1),
        (r"$6^4=1296$", 1)),
    [r"לחשב $4^6$: מספר הפונקציות הוא (גודל הטווח) בחזקת (גודל התחום).",
     r"לחשב $6\cdot4=24$."],
    [num(r"כמה פונקציות יש ב-$F$?", 1296, r"$6^4=1296$."),
     ch(r"איזה ביטוי נותן את מספר הפונקציות מקבוצה בת 4 איברים לקבוצה בת 6 איברים?",
        r"$6^4$", r"$4^6$", r"$6\cdot4$", r"$\binom64$",
        explain="לכל אחד מארבעת האיברים בוחרים אחד מ-6 ערכים.")])

put(4, "ב",
    rub(("פונקציה יורדת ממש: $f(1)>f(2)>f(3)>f(4)$", 1),
        ("התאמה חד-חד-ערכית ועל בין פונקציות יורדות ממש לתתי-קבוצות בגודל 4", 1),
        (r"$\binom64=15$", 1)),
    ["לספור $6^4$ או $P(6,4)$.",
     "לחשוב שלכל תת-קבוצה יש כמה פונקציות יורדות: יש בדיוק אחת."],
    [num(r"כמה פונקציות יורדות ממש יש ב-$F$?", 15, r"$\binom64=15$."),
     num(r"כמה פונקציות יורדות ממש מקבלות בדיוק את הערכים $\{2,3,4,5\}$?", 1, "סידור הערכים בסדר יורד קובע את הפונקציה.")])

put(4, "ג",
    rub((r"$f$ על $\{1,2\}$: $2!$ אפשרויות", 1),
        (r"$f(3),f(4)$ מתוך $\{3,4,5,6\}$ ללא חזרה: $4\cdot3=12$", 2),
        (r"כפל: $2\cdot12=24$", 1)),
    [r"לאפשר ל-$f(3)$ ו-$f(4)$ לקבל את הערכים $1,2$: זה מפר חד-חד-ערכיות.",
     "לשכוח שהערכים של $f(3),f(4)$ חייבים להיות שונים."],
    [num(r"כמה דרכים יש לבחור את $f(1),f(2)$ כך ש-$f(\{1,2\})=\{1,2\}$?", 2, r"$2!=2$."),
     num(r"כמה דרכים יש לבחור את $f(3),f(4)$ שונים מתוך $\{3,4,5,6\}$?", 12, r"$4\cdot3=12$."),
     num(r"כמה פונקציות חד-חד-ערכיות מקיימות את התנאי?", 24, r"$2\cdot12=24$.")])

put(4, "ד",
    rub(("התאמה בין קבוצות $S$ לחלוקות של $\\{3,5,7,11,13\\}$ לשלוש קבוצות", 3),
        ("מספר Stirling $S(5,3)$ ונוסחת הנסיגה", 2),
        (r"חישוב ערכי הביניים $S(3,2),S(4,2),S(4,3)$", 1),
        (r"$S(5,3)=7+3\cdot6=25$", 1)),
    [r"לספור תמורות (120) במקום חלוקות לא סדורות.",
     r"לשכוח את הגורם $k$ בנוסחת הנסיגה $S(n,k)=S(n-1,k-1)+kS(n-1,k)$."],
    [ch(r"איזה אובייקט מתאים במדויק לכל קבוצה $S=\{a,b,c\}$ עם $abc=3\cdot5\cdot7\cdot11\cdot13$?",
        r"חלוקה של $\{3,5,7,11,13\}$ לשלוש קבוצות לא ריקות", r"תמורה של $\{3,5,7,11,13\}$", r"תת-קבוצה בגודל 3 של $\{3,5,7,11,13\}$", r"פונקציה מ-$\{3,5,7,11,13\}$ ל-$\{a,b,c\}$",
        explain="כל גורם ראשוני שייך לבדיוק אחד מהמספרים a, b, c."),
     num(r"מהו $S(4,3)$?", 6, r"$S(3,2)+3S(3,3)=3+3=6$."),
     num(r"מהו $S(5,3)$?", 25, r"$S(4,2)+3S(4,3)=7+18=25$.")])

put(4, "ה",
    rub(("הספרה האחרונה זוגית: 3 אפשרויות", 1),
        (r"הספרות האחרות: $5\cdot4\cdot3$", 2),
        (r"כפל: $3\cdot60=180$", 1)),
    ["להתחיל מהספרה הראשונה ולשכוח את אילוץ הזוגיות של הספרה האחרונה.",
     "לאפשר חזרה על ספרות."],
    [num(r"כמה אפשרויות יש לספרה האחרונה?", 3, "2, 4 או 6."),
     num(r"כמה מספרים זוגיים בעלי 4 ספרות שונות אפשר ליצור?", 180, r"$3\cdot5\cdot4\cdot3=180$.")])

put(4, "ו",
    rub(("בלוק $\\{1,2,3\\}$ נחשב כיחידה אחת", 1),
        (r"סידור 4 היחידות: $4!$", 1),
        (r"סידור פנימי של הבלוק: $3!$", 1),
        (r"כפל: $24\cdot6=144$", 1)),
    [r"לשכוח את הסידור הפנימי של הבלוק, ולקבל $4!=24$.",
     r"לחשב $6!=720$ בלי האילוץ."],
    [num(r"כמה סידורים יש ל-4 היחידות (הבלוק, 4, 5, 6)?", 24, r"$4!=24$."),
     num(r"כמה סידורים פנימיים יש לבלוק $1,2,3$?", 6, r"$3!=6$."),
     num(r"כמה תמורות של $A$ מקיימות שהמספרים $1,2,3$ בסמיכות?", 144, r"$24\cdot6=144$.")])

_phi = [r"כותבים $n=3^\alpha m$ עם $\alpha\ge1$ ו-$\gcd(3,m)=1$",
        r"$\varphi(n)=\varphi(3^\alpha)\varphi(m)=2\cdot3^{\alpha-1}\varphi(m)$ וגם $\varphi(3n)=\varphi(3^{\alpha+1})\varphi(m)=2\cdot3^{\alpha}\varphi(m)$",
        r"לכן $\varphi(3n)=3\cdot\left(2\cdot3^{\alpha-1}\varphi(m)\right)=3\varphi(n)$"]
put(5, "א",
    rub((r"כתיבת $n=3^\alpha m$ עם $\gcd(3,m)=1$", 2),
        (r"כפליות $\varphi$ על מספרים זרים", 2),
        (r"חישוב $\varphi(n)=2\cdot3^{\alpha-1}\varphi(m)$", 2),
        (r"חישוב $\varphi(3n)=2\cdot3^\alpha\varphi(m)$", 2),
        (r"מסקנה: $\varphi(3n)=3\varphi(n)$", 2)),
    [r"להשתמש בכפליות בלי שהמספרים זרים: $\varphi(3^\alpha m)=\varphi(3^\alpha)\varphi(m)$ דורש $\gcd(3,m)=1$.",
     r"לשכוח ש-$3\mid n$ משנה את החזקה: ב-$3n$ החזקה היא $\alpha+1$.",
     r"לטעון $\varphi(3n)=\varphi(3)\varphi(n)=2\varphi(n)$."],
    [ch(r"באיזה תנאי מותר לכתוב $\varphi(ab)=\varphi(a)\varphi(b)$?",
        r"כש-$\gcd(a,b)=1$", "תמיד", r"כש-$a=b$", r"כש-$a,b$ זוגיים",
        explain=r"למשל $\varphi(2\cdot2)=2$ ואילו $\varphi(2)\varphi(2)=1$."),
     num(r"מהו $\varphi(12)$?", 4, r"$12\cdot\frac12\cdot\frac23=4$."),
     num(r"מהו $\varphi(36)$?", 12, r"$3\cdot\varphi(12)=12$, כי $3\mid12$."),
     order("סדרו את שלבי ההוכחה.", _phi, "פירוק, שני החישובים, מסקנה.")])

put(5, "ב",
    rub((r"$A\subseteq\mathbb{Q}$ ולכן $|A|\le|\mathbb{Q}|$", 2),
        (r"תת-קבוצה אינסופית $B=\{1+\frac1n\}$ של $A$", 2),
        (r"שרשרת $|\mathbb{Z}|=|\mathbb{N}|=|B|\le|A|\le|\mathbb{Q}|=|\mathbb{Z}|$", 2),
        (r"מסקנה: $|A|=|\mathbb{Z}|$", 1)),
    [r"להתעלם מהחלק $\mathbb{Z}\cap[20.5,100.5]$: הוא סופי ואינו משפיע, אבל צריך לציין זאת.",
     "להראות רק אחד משני אי-השוויונות."],
    [ch("באיזו שיטה משתמש הפתרון?",
        "חסם מלמעלה בהכלה ב-$\\mathbb{Q}$ וחסם מלמטה בתת-קבוצה אינסופית בת-מנייה, ואז שוויון",
        "בניית התאמה מפורשת בין $A$ ל-$\\mathbb{Z}$", "טיעון אלכסוני של קנטור", "אינדוקציה",
        explain="שני אי-שוויונות בין עוצמות נותנים שוויון."),
     ch(r"איזו תת-קבוצה אינסופית של $A$ בוחר הפתרון?",
        r"$\{1+\frac12,1+\frac13,1+\frac14,\ldots\}$", r"$\{1-\frac12,1-\frac13,1-\frac14,\ldots\}$", r"$\{21,22,\ldots,100\}$", r"$\{5+\frac12,5+\frac13,\ldots\}$",
        explain=r"השנייה והרביעית מחוץ ל-$A$, והשלישית סופית.")])

put(5, "ג",
    rub((r"הצבת $F_n=r^n$ ומשוואה אופיינית $r^2-r-1=0$", 2),
        (r"שורשים $r_{1,2}=\frac{1\pm\sqrt5}2$ ופתרון כללי", 2),
        (r"מערכת מ-$F_0=0$, $F_1=1$: $C_1=-C_2$ ו-$C_2=\frac1{\sqrt5}$", 2),
        ("הנוסחה הסופית", 2)),
    [r"לשכוח ש-$r_1\ne r_2$ ולכן אין צורך בגורם $n$.",
     r"לטעות בסימן של $C_1$: מ-$F_0=0$ מקבלים $C_1=-C_2$."],
    [ch("מהם שורשי המשוואה האופיינית?",
        r"$\frac{1\pm\sqrt5}2$", r"$\frac{-1\pm\sqrt5}2$", r"$\pm\sqrt5$", r"$1$ ו-$-1$",
        explain=r"$r^2-r-1=0$ נותן $r=\frac{1\pm\sqrt5}2$."),
     ch(r"מהו $C_2$ (המקדם של $\left(\frac{1+\sqrt5}2\right)^n$)?",
        r"$\frac1{\sqrt5}$", r"$-\frac1{\sqrt5}$", r"$\frac12$", r"$1$",
        explain=r"$C_2(r_2-r_1)=1$ ו-$r_2-r_1=\sqrt5$."),
     num(r"מהו $F_{10}$?", 55, r"סדרת Fibonacci: $0,1,1,2,3,5,8,13,21,34,55$.")])


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
