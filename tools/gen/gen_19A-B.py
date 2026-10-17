# -*- coding: utf-8 -*-
"""Generator for tools/raw/19A-B.json -- discrete math 1 (20066), moed B 5779 (2019, date not printed).
5 questions of 25 points (scan, read by vision). Q1 is the mandatory concept question (5 x 3 + 5 + 5).
The handwritten key (author unknown) is student-solution. Checks: tools/verify/19A-B/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_19A-B.py
 - Printed sub-part labels (a1, c2, ...) become sequential Hebrew letters (the validator wants one letter);
   the printed label is shown at the top of the stem.
 - Q2b (three asks) and Q3b (three cases) are ONE item each.
 - Slips in intermediate lines of the key were corrected (see docs/ASK_ADIR.md)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19A-B.json"

SEQ = {(1, "א1"): "א", (1, "א2"): "ב", (1, "א3"): "ג", (1, "א4"): "ד", (1, "א5"): "ה", (1, "ב"): "ו", (1, "ג"): "ז",
       (2, "ג1"): "ג", (2, "ג2"): "ד",
       (4, "א1"): "א", (4, "א2"): "ב", (4, "ב1"): "ג", (4, "ב2"): "ד", (4, "ג"): "ה",
       (5, "א1"): "א", (5, "א2"): "ב", (5, "ב"): "ג", (5, "ג"): "ד"}


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


INTRO = "לפניך חמישה סעיפים. בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"
SET1 = r"\{\{\{\{\varnothing\}\}\},\ P(\{\{\{1\}\},\varnothing\}),\ \{\{\varnothing\}\}\}"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א1", "proof", "logic_propositional", 3,
      INTRO + "**המונח:** פסוק מורכב.\n**שאלה:** תנו דוגמה למשפט בשפה העברית שהינו פסוק מורכב.",
      "**הגדרה:** פסוק מורכב הוא פסוק שנוצר על ידי שימוש בפסוקים אטומיים וקשרים לוגיים שמחברים בין הפסוקים האטומיים."
      "\n"
      "**דוגמה:** אני אוכל גלידה וגם קורא עיתון."),

    Q(1, "א2", "computation", "sets_power_set", 3,
      INTRO + "**המונח:** מכפלה קרטזית.\n"
      r"**שאלה:** כמה איברים בקבוצה $" + SET1 + r"\times\{1,P(\{1,2\})\}$ ?",
      r"**הגדרה:** תהיינה $A$ ו-$B$ קבוצות. הקבוצה $A\times B$ שמוגדרת לפי הכלל $A\times B=\{(a,b):\ a\in A\wedge b\in B\}$ נקראת המכפלה הקרטזית של הקבוצות $A$ ו-$B$."
      "\n"
      r"הקבוצה הראשונה (משמאל ל-$\times$) כוללת 3 איברים, והקבוצה $\{1,P(\{1,2\})\}$ כוללת 2 איברים."
      "\n"
      r"לכן בקבוצה $\{\ldots\}\times\{\ldots\}$ יש $6=3\cdot2$ איברים."),

    Q(1, "א3", "computation", "relations_properties", 3,
      INTRO + "**המונח:** יחס סימטרי.\n"
      r"**שאלה:** כמה יחסים סימטריים ניתן להגדיר מעל הקבוצה $\{1,2\}$ ?",
      r"**הגדרה:** תהי $A$ קבוצה. היחס $R\subseteq A\times A$ נקרא סימטרי אם לכל $x,y\in A$ מתקיים: אם $xRy$ אז $yRx$ "
      r"(כלומר: לכל $x,y\in A$, אם $(x,y)\in R$ אז $(y,x)\in R$)."
      "\n"
      r"**תשובה:** 8. היחסים הם:"
      "\n"
      r"$\varnothing$, $\{(1,1)\}$, $\{(2,2)\}$, $\{(1,1),(2,2)\}$, $\{(1,2),(2,1)\}$, $\{(1,1),(1,2),(2,1)\}$, $\{(2,2),(1,2),(2,1)\}$, $\{(1,1),(2,2),(1,2),(2,1)\}$."),

    Q(1, "א4", "proof", "partial_orders", 3,
      INTRO + "**המונח:** יחסי סדר מלא.\n"
      "**שאלה:** תנו דוגמה ליחס סדר מלא שיש בו איבר מקסימום אבל אין לו איבר מינימום.",
      r"**הגדרה:** תהי $A$ קבוצה ו-$R\subseteq A\times A$. $R$ הוא יחס סדר מלא אם $R$ הוא יחס סדר חלקי (כלומר רפלקסיבי, אנטי-סימטרי וטרנזיטיבי) "
      r"ומתקיים: לכל $a,b\in A$, אם $(a,b)\in R$ או $(b,a)\in R$."
      "\n"
      r"**דוגמה:** $R\subseteq(0,1]\times(0,1]$, כאשר $x\le y\iff(x,y)\in R$. ל-$R$ יש איבר מקסימום (1), אך אין לו איבר מינימום."),

    Q(1, "א5", "computation", "functions", 3,
      INTRO + "**המונח:** פונקציה על.\n"
      r"**שאלה:** כמה פונקציות על ניתן להגדיר מהקבוצה $\{1,2,3\}$ לקבוצה $\{1,2,3\}$ ?",
      r"**הגדרה:** תהיינה $A,B$ קבוצות ו-$f:A\to B$ פונקציה. $f$ נקראת פונקציה על אם לכל $b\in B$ קיים $a\in A$ כך ש: $f(a)=b$, כלומר $f(A)=B$."
      "\n"
      r"מכיוון ש-$|\{1,2,3\}|=3=|\{1,2,3\}|$, כל $f$ על היא גם חד-חד-ערכית ולכן גם הפיכה. "
      r"כלומר: $f$ על $\iff f$ מתאימה בין איברי $\{1,2,3\}$ בצורה חד-חד-ערכית."
      "\n"
      r"**תשובה:** $3!=6$."),

    Q(1, "ב", "computation", "logic_propositional", 5,
      r"בנו את צורת DNF עבור הפסוק: $(p\wedge q)\leftrightarrow(\neg q\vee r)$. העזר בטבלת אמת לפתרון.",
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
      r"הפסוק אמת בשתי שורות, ולכן צורת ה-DNF היא:"
      "\n"
      r"$$(p\wedge q\wedge r)\vee(\neg p\wedge q\wedge\neg r)$$"),

    Q(1, "ג", "proof", "quantifiers_proofs", 5,
      "שלולו את הטענה: “לכל $x\\in A$ ולכל $y\\in B$, קיים $z\\in C$, כך ש: $y+z<x$” "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      "השלילה: “קיים $x\\in A$ וקיים $y\\in B$ כך שלכל $z\\in C$ מתקיים $y+z\\ge x$”."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 9,
      r"הוכיחו ש: $(n+1)+(n+2)+\ldots+(2n-1)+(2n)=n(3n+1)/2$ לכל $1\le n\in\mathbb{N}$.",
      r"$P(n):\ (n+1)+(n+2)+\ldots+(2n-1)+(2n)=n(3n+1)/2$, לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ 1+1=1\cdot(3+1)/2\iff2=2$ — TRUE."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $k\ge1$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ (k+1)+(k+2)+\ldots+(2k-1)+(2k)=k(3k+1)/2$"
      "\n"
      r"$P(k+1):\ (k+2)+\ldots+(2k)+(2k+1)+(2k+2)=(k+1)(3k+4)/2$"
      "\n"
      r"לפי $P(k)=\text{TRUE}$, הסכום $(k+2)+\ldots+(2k)$ שווה ל-$k(3k+1)/2-(k+1)$, ולכן אגף שמאל של $P(k+1)$ הוא:"
      "\n"
      r"$$\frac{k(3k+1)}2-(k+1)+(2k+1)+(2k+2)=\frac{k(3k+1)}2+3k+2=\frac{3k^2+7k+4}2$$"
      "\n"
      r"ואגף ימין: $\dfrac{(k+1)(3k+4)}2=\dfrac{3k^2+4k+3k+4}2=\dfrac{3k^2+7k+4}2$."
      "\n"
      r"לכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**III.** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $n\in\mathbb{N}$, $n\ge1$."),

    Q(2, "ב", "computation", "sets_power_set", 6,
      r"נתונות הקבוצות: $A=\{2^m\cdot5^n\cdot11^q:\ m,n,q\in\{0,1,2,\ldots,19\}\}$ ו-$B=\{3^m\cdot5^n\cdot7^q:\ m,n,q\in\{0,1,2,\ldots,19\}\}$."
      "\n"
      r"מצאו את $A\cap B$ וחשבו את $|A\cup B|$ וגם $|P(A\cup B)|$.",
      r"$x\in A\iff x=2^m5^n11^q$ ו-$x\in B\iff x=3^{m'}5^{n'}7^{q'}$. לפי יחידות הפירוק לגורמים ראשוניים:"
      "\n"
      r"$x\in A\cap B\iff m=0,\ q=0,\ m'=0,\ q'=0,\ n=n'\in\{0,1,\ldots,19\}$."
      "\n"
      r"לכן $A\cap B=\{5^n:\ n\in\{0,1,\ldots,19\}\}$, ו-$|A\cap B|=20$."
      "\n"
      r"$|A|=|B|=20^3$, ולכן $|A\cup B|=|A|+|B|-|A\cap B|=20^3+20^3-20=2\cdot20^3-20$."
      "\n"
      r"נסמן $M=|A\cup B|=2\cdot20^3-20$. אז $|P(A\cup B)|=2^{|A\cup B|}=2^M=2^{2\cdot20^3-20}$."),

    Q(2, "ג1", "proof", "sets_power_set", 2,
      r"הוכיחו או הפריכו: לא קיימות קבוצות שונות $A,B$ כך שמתקיים $A\times B=B\times A$.",
      r"הטענה אינה נכונה. דוגמה נגדית: $A=\varnothing$, $B=\{1\}$ — קבוצות שונות, ו-$A\times B=\varnothing=B\times A$."),

    Q(2, "ג2", "proof", "sets_power_set", 8,
      r"הוכיחו או הפריכו: לכל 3 קבוצות לא ריקות ושונות $A,B,C$ מתקיים: $A\times(B\cap C)=(A\times B)\cap(A\times C)$.",
      r"הטענה נכונה."
      "\n"
      r"**I.** נבדוק ש: $A\times(B\cap C)\subseteq(A\times B)\cap(A\times C)$."
      "\n"
      r"לכל $(x,y)\in A\times(B\cap C)$: $x\in A$ ו-$y\in B\cap C$, ולכן $(x\in A\wedge y\in B)$ וגם $(x\in A\wedge y\in C)$, "
      r"כלומר $(x,y)\in A\times B$ וגם $(x,y)\in A\times C$, ולכן $(x,y)\in(A\times B)\cap(A\times C)$."
      "\n"
      r"**II.** נבדוק ש: $(A\times B)\cap(A\times C)\subseteq A\times(B\cap C)$."
      "\n"
      r"לכל $(x,y)\in(A\times B)\cap(A\times C)$: $(x,y)\in A\times B$ וגם $(x,y)\in A\times C$, כלומר $(x\in A\wedge y\in B)$ וגם $(x\in A\wedge y\in C)$, "
      r"ולכן $x\in A$ ו-$y\in B\cap C$, כלומר $(x,y)\in A\times(B\cap C)$."
      "\n"
      r"מסקנה: הטענה נכונה."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "equivalence_relations", 12,
      r"יהי היחס $R\subseteq(\mathbb{Q}-\{0\})\times(\mathbb{Q}-\{0\})$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Q}-\{0\}$, מתקיים $0<(x\cdot y)\iff xRy$ "
      r"(הסימן $\cdot$ הוא כפל)."
      "\n"
      r"הוכיחו ש: $R$ הוא יחס שקילות ומצאו את קבוצת המנה $(\mathbb{Q}-\{0\})/R$.",
      r"**(1) $R$ רפלקסיבי:** לכל $x\in\mathbb{Q}-\{0\}$, $xRx\iff0<x\cdot x=x^2$. הטענה נכונה כי $x\ne0$."
      "\n"
      r"**(2) $R$ סימטרי:** לכל $x,y\in\mathbb{Q}-\{0\}$, אם $xRy$ אז $yRx$, כי $xRy\iff x\cdot y>0\iff y\cdot x>0\iff yRx$."
      "\n"
      r"**(3) $R$ טרנזיטיבי:** לכל $x,y,z\in\mathbb{Q}-\{0\}$, אם $xRy$ ו-$yRz$ אז $xRz$. "
      r"אכן, $0<xy\iff xRy$ ו-$0<yz\iff yRz$, ולכן $0<(x\cdot z)\cdot y^2=(xy)\cdot(yz)$. מכיוון ש-$y\ne0$, $0<y^2$, ולכן $xz>0$, כלומר $xRz$."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Q}-\{0\}\wedge x\cdot1>0\}=\{x\in\mathbb{Q}-\{0\}:\ x>0\}$"
      "\n"
      r"$[-1]=\{x:\ x\in\mathbb{Q}-\{0\}\wedge x\cdot(-1)>0\}=\{x\in\mathbb{Q}-\{0\}:\ x<0\}$"
      "\n"
      r"$[1]\cup[-1]=\mathbb{Q}-\{0\}$, ולכן $(\mathbb{Q}-\{0\})/R=\{[1],[-1]\}$."),

    Q(3, "ב", "computation", "equivalence_relations", 5,
      r"תהי הקבוצה $A=\{1,2,3,\ldots,12\}$. יהיו $R\subseteq A\times A$ יחס שקילות וגם $a\in A$. הקבוצה $A/R=\{B,C,D\}$ מקיימת $|B|=5$ וגם $|C|=3$. "
      r"חשבו את מספר הזוגות מ-$R$ שכוללים את $a$. שימו לב שיש מספר מקרים.",
      r"$|D|=|A|-(3+5)=4$. מספר הזוגות ב-$R$ שכוללים את $a$ תלוי במחלקה שבה $a$ נמצא:"
      "\n"
      r"**מקרה 1:** $a\in C$ ($[a]=C$, $|C|=3$). אז $(a,a)\in R$, ולכל $x\in C-\{a\}$ מתקיים $(a,x),(x,a)\in R$. סה״כ $1+2\cdot2=5$ זוגות ב-$R$."
      "\n"
      r"**מקרה 2:** $a\in B$ ($[a]=B$, $|B|=5$). אז $(a,a)\in R$, ולכל $x\in B-\{a\}$ מתקיים $(a,x),(x,a)\in R$. סה״כ $1+4+4=9$ זוגות ב-$R$."
      "\n"
      r"**מקרה 3:** $a\in D$ ($[a]=D$, $|D|=4$). אז $(a,a)\in R$, ולכל $x\in D-\{a\}$ מתקיים $(a,x),(x,a)\in R$. סה״כ $1+3+3=7$ זוגות ב-$R$."),

    Q(3, "ג", "computation", "combinatorics", 8,
      r"יהי $1<n\in\mathbb{N}$. חשבו את הסכום: $f(n)=\sum_{k=0}^{n}\left(\binom nk\cdot\left(3^{2k}+2^{2k}\right)\right)$.",
      r"$f(n)=S_1+S_2$, כאשר $S_1=\sum_{k=0}^{n}\binom nk3^{2k}$ ו-$S_2=\sum_{k=0}^{n}\binom nk2^{2k}$."
      "\n"
      r"$S_1=\sum_{k=0}^{n}\binom nk9^k=\sum_{k=0}^{n}\binom nk9^k1^{n-k}=(9+1)^n=10^n$"
      "\n"
      r"$S_2=\sum_{k=0}^{n}\binom nk4^k=\sum_{k=0}^{n}\binom nk4^k1^{n-k}=(4+1)^n=5^n$"
      "\n"
      r"מסקנה: $f(n)=10^n+5^n$."),

    # ---------------- Q4 ----------------
    Q(4, "א1", "computation", "functions", 5,
      r"תהיינה הקבוצות $A=\{1,2,3,\ldots,10\}$ וגם $B=\{1,2,\ldots,20\}$. מהו מספר היחסים $R\subseteq A\times A$ שהם פונקציות, אך לא חד-חד-ערכיות ?",
      r"מספר הפונקציות $f:A\to A$ הוא $10^{10}$, כי לכל אחד מ-10 האיברים $f(1),\ldots,f(10)\in A$ יש 10 אפשרויות, וכל אחת מהפונקציות מגדירה יחס."
      "\n"
      r"$f:A\to A$ היא חד-חד-ערכית $\iff f$ הפיכה, כי $A$ סופית, ומספר הפונקציות הללו הוא $10\cdot9\cdot8\cdots1=10!$ "
      r"($f(1)\in A$: 10 אפשרויות, $f(2)\in A-\{f(1)\}$: 9 אפשרויות, ... , $f(10)\in A-\{f(1),\ldots,f(9)\}$: אפשרות אחת)."
      "\n"
      r"מסקנה: מספר היחסים $R\subseteq A\times A$ שהם פונקציות אך לא חד-חד-ערכיות הוא $10^{10}-10!$."),

    Q(4, "א2", "computation", "combinatorics", 5,
      r"תהיינה הקבוצות $A=\{1,2,3,\ldots,10\}$ וגם $B=\{1,2,\ldots,20\}$. מהו מספר הפונקציות $f:A\to B$ שהן עולות ממש?",
      r"$f$ עולה ממש $\iff f(1)<f(2)<\ldots<f(10)\iff\{f(1),f(2),\ldots,f(10)\}$ היא תת-קבוצה בגודל 10 של $B$."
      "\n"
      r"הנימוק: אם $\{b_1,\ldots,b_{10}\}\in P(B)$, כך ש-$b_1<b_2<\ldots<b_{10}$, אז ניתן להבנות פונקציה $f:A\to B$ אחת בלבד שעולה ממש."
      "\n"
      r"מסקנה: מספר הפונקציות $f:A\to B$ העולות ממש שווה למספר תתי-הקבוצות בגודל 10 של $B$, כלומר $\binom{20}{10}$."),

    Q(4, "ב1", "proof", "equivalence_relations", 5,
      r"נתון $C=\{1,2,3,4,5\}$ ו-$\Omega=\{\{1,2\},\{3\},\{4,5\}\}$. הראו כי קיים יחס שקילות $R\subseteq C\times C$ כך ש: $\Omega=C/R$.",
      r"נסמן $\Omega=\{A_1,A_2,A_3\}$, כאשר $A_1=\{1,2\}$, $A_2=\{3\}$, $A_3=\{4,5\}$. $\Omega$ היא חלוקה של $C$, כי:"
      "\n"
      r"(1) $A_i\ne\varnothing$ לכל $i$; (2) $A_i\cap A_j=\varnothing$ לכל $i\ne j$; (3) $A_1\cup A_2\cup A_3=C$."
      "\n"
      r"לכן קיים יחס שקילות $R\subseteq C\times C$ כך ש-$C/R=\Omega$."),

    Q(4, "ב2", "proof", "partial_orders", 5,
      r"נתון $C=\{1,2,3,4,5\}$ ו-$\Omega=\{\{1,2\},\{3\},\{4,5\}\}$, ו-$R\subseteq C\times C$ יחס שקילות כך ש: $\Omega=C/R$. מצאו את הקבוצה $R$. האם $R$ הוא יחס סדר חלקי ?",
      r"מתקיים $C/R=\{\{1,2\},\{3\},\{4,5\}\}$, ולכן:"
      "\n"
      r"$[1]=[2]=\{1,2\}\iff(1,1),(2,2),(1,2),(2,1)\in R$"
      "\n"
      r"$[3]=\{3\}\iff(3,3)\in R$"
      "\n"
      r"$[4]=[5]=\{4,5\}\iff(4,4),(5,5),(4,5),(5,4)\in R$"
      "\n"
      r"מסקנה: $R=\{(1,1),(2,2),(3,3),(4,4),(5,5),(1,2),(2,1),(4,5),(5,4)\}$."
      "\n"
      r"$R$ אינו יחס סדר חלקי, כי $(1,2),(2,1)\in R$ ו-$1\ne2$ (אינו אנטי-סימטרי)."),

    Q(4, "ג", "proof", "modular_fermat_wilson", 5,
      r"יהיו $2<p<q$ מספרים ראשוניים. הוכיחו ש: $n\pmod{pq}\equiv0$, כאשר "
      r"$n=\left(\varnothing(p)^{\varnothing(q)}-1\right)\cdot\left(\left(1+\varnothing(q)\right)^{\varnothing(p)}-1\right)$."
      "\n"
      r"שימו לב: $\varnothing$ מסמנת את פונקציית Euler.",
      r"מכיוון ש-$p$ ראשוני, $\varnothing(p)=p-1$. מכיוון ש-$q$ ראשוני, $\varnothing(q)=q-1$."
      "\n"
      r"$\varnothing(p)^{\varnothing(q)}-1=(p-1)^{q-1}-1$. מכיוון ש-$p<q$, $q\nmid(p-1)$, ולכן לפי משפט Fermat: $q\mid\left((p-1)^{q-1}-1\right)$."
      "\n"
      r"$\left(1+\varnothing(q)\right)^{\varnothing(p)}-1=(1+q-1)^{p-1}-1=q^{p-1}-1$. מכיוון ש-$p,q$ ראשוניים ו-$p<q$, $p\nmid q$, ולכן לפי משפט Fermat: $p\mid\left(q^{p-1}-1\right)$."
      "\n"
      r"לכן $(p\cdot q)\mid n$, כלומר $n\pmod{pq}\equiv0$, כאשר $n=\left((p-1)^{q-1}-1\right)\left(q^{p-1}-1\right)$."),

    # ---------------- Q5 ----------------
    Q(5, "א1", "proof", "number_theory_gcd", 5,
      r"אם $\varnothing$ פונקציית Euler, הוכיחו או הפריכו: לכל שני מספרים שונים $m,n\in\mathbb{N}-\{0\}$, לפחות אחד מהמספרים $\varnothing(m),\varnothing(n)$ הוא זוגי.",
      r"הטענה לא נכונה: $1,2\in\mathbb{N}-\{0\}$ ו-$\varnothing(1)=\varnothing(2)=1$, מספר אי-זוגי."),

    Q(5, "א2", "proof", "number_theory_gcd", 5,
      r"אם $\varnothing$ פונקציית Euler, הוכיחו או הפריכו: לכל 3 מספרים שונים זה מזה $m,n,q\in\mathbb{N}-\{0\}$, לפחות אחד מהמספרים $\varnothing(m),\varnothing(n),\varnothing(q)$ הוא זוגי.",
      r"הטענה נכונה. בין שלושה מספרים שונים ב-$\mathbb{N}-\{0\}$ יש לפחות אחד, נסמנו $q$, כך ש-$2<q$ (רק $1,2$ אינם גדולים מ-2). נראה שעבור כל $2<q\in\mathbb{N}$ מתקיים $2\mid\varnothing(q)$."
      "\n"
      r"נכתוב $q=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k}$ (*), כאשר $p_i$ ראשוני ו-$1\le\alpha_i\in\mathbb{N}$ לכל $i$. אז:"
      "\n"
      r"$$\varnothing(q)=p_1^{\alpha_1}\cdots p_k^{\alpha_k}\left(1-\frac1{p_1}\right)\cdots\left(1-\frac1{p_k}\right)=p_1^{\alpha_1-1}p_2^{\alpha_2-1}\cdots p_k^{\alpha_k-1}(p_1-1)\cdots(p_k-1)$$"
      "\n"
      r"**מקרה 1:** בפירוק (*) קיים $p_i$ עם $2<p_i$. אז $2\mid(p_i-1)$ ו-$(p_i-1)\mid\varnothing(q)$, ולכן $2\mid\varnothing(q)$."
      "\n"
      r"**מקרה 2:** בפירוק (*) אין $2<p_i$, כלומר $q=2^{\alpha_1}$, ומכיוון ש-$2<q$ מתקיים $2\le\alpha_1$. אז $\varnothing(q)=2^{\alpha_1}\left(1-\frac12\right)=2^{\alpha_1-1}$, ו-$\alpha_1-1\ge1$, ולכן $2\mid\varnothing(q)$."),

    Q(5, "ב", "proof", "cardinality_sets", 7,
      r"הוכיחו ש: $|\mathbb{Q}\cap(1,5]|=|\mathbb{N}\times\mathbb{N}|$.",
      r"**טענה 1:** $|\mathbb{Q}|=|\mathbb{N}\times\mathbb{N}|=|\mathbb{N}|$."
      "\n"
      r"**טענה 2:** $|\mathbb{Q}\cap(1,5]|\le|\mathbb{Q}|$, כי $\mathbb{Q}\cap(1,5]\subseteq\mathbb{Q}$."
      "\n"
      r"**טענה 3:** $\mathbb{Q}\cap(1,5]$ היא קבוצה אינסופית: $B=\left\{1+\frac12,\ 1+\frac13,\ 1+\frac14,\ \ldots,\ 1+\frac1n,\ \ldots\right\}\subseteq\mathbb{Q}\cap(1,5]$, ולכן $|\mathbb{N}|=|B|\le|\mathbb{Q}\cap(1,5]|$."
      "\n"
      r"**מסקנה:** $|\mathbb{N}|=|B|\le|\mathbb{Q}\cap(1,5]|\le|\mathbb{Q}|=|\mathbb{N}|$, ולכן $|\mathbb{Q}\cap(1,5]|=|\mathbb{N}|=|\mathbb{N}\times\mathbb{N}|$."),

    Q(5, "ג", "computation", "recurrence_sums", 8,
      r"מצאו את הצורה המפורשת של $(a_n)$, כאשר: $a_n=6a_{n-1}-9a_{n-2}$ לכל $2\le n\in\mathbb{N}$, $a_0=5$, $a_1=21$.",
      r"המשוואה האופיינית: $r^2-6r+9=0$, ולכן $r_1=r_2=3$. לכן $a_n=C_1\cdot3^n+C_2\cdot n\cdot3^n$."
      "\n"
      r"$a_0=C_1=5$"
      "\n"
      r"$a_1=3C_1+3C_2=21\ \Rightarrow\ C_1+C_2=7$"
      "\n"
      r"נקבל $C_1=5$, $C_2=2$."
      "\n"
      r"מסקנה: $a_n=5\cdot3^n+2\cdot n\cdot3^n$, לכל $n\in\mathbb{N}$."),
]

exam = {
    "examCode": "19A-B",
    "examLabel": 'בדידה 1, תשע"ט, מועד ב (2019)',
    "year": 2019,
    "examDate": "2019",
    "sourceFile": "19A-B exam with handwritten solution, pp.1-16",
    "solutionFile": "19A-B handwritten solution (author unknown), pp.3-16",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
