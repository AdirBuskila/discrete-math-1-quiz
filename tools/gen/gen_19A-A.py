# -*- coding: utf-8 -*-
"""Generator for tools/raw/19A-A.json -- discrete math 1 (20066), moed A 5779 (the key is titled 3.3.19).
5 questions of 25 points (scan, read by vision). Q1 is the mandatory concept question (5 x 3 + 5 + 5).
The handwritten key (author unknown) is student-solution.
Checks: tools/verify/19A-A/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_19A-A.py
 - Q1a is split into five items (a1-a5), Q3b into b1/b2, Q4a into a1/a2, Q4b into b1/b2 (each has its own point value).
 - Q2c (c1+c2) and Q3a are ONE item each.
 - Q1b: the key's DNF misses a row (final-answer error) -> corrected, official=False, solutionSource solved."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19A-A.json"


SEQ = {(1, "א1"): "א", (1, "א2"): "ב", (1, "א3"): "ג", (1, "א4"): "ד", (1, "א5"): "ה", (1, "ב"): "ו", (1, "ג"): "ז",
       (3, "ב1"): "ב", (3, "ב2"): "ג", (3, "ג"): "ד",
       (4, "א1"): "א", (4, "א2"): "ב", (4, "ב1"): "ג", (4, "ב2"): "ד", (4, "ג"): "ה"}


def Q(num, part, kind, topic, points, question, solution, **kw):
    # the validator wants one letter per part: printed sub-part labels (א1, ב2) become sequential letters,
    # and the printed label stays visible at the top of the stem
    if (num, part) in SEQ:
        if part not in ("ב", "ג") or num == 1:
            pass
        letter = SEQ[(num, part)]
        if any(ch.isdigit() for ch in part):
            question = "**(" + part + ")** " + question
        part = letter
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


INTRO = "לפניך חמישה סעיפים. בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א1", "proof", "logic_propositional", 3,
      INTRO + "**המונח:** סתירה.\n**שאלה:** תנו דוגמה למשפט בשפה העברית שהינו סתירה.",
      "**הגדרה:** סתירה היא פסוק שלא משנה מה הערך של המשתנים שלו, ערך האמת של הפסוק הוא שקר."
      "\n"
      "**דוגמה:** חוה אוכלת תפוח וגם לא אוכלת תפוח."),

    Q(1, "א2", "computation", "sets_power_set", 3,
      INTRO + "**המונח:** קבוצת החזקה.\n"
      r"**שאלה:** כמה איברים בקבוצה $P(\{\{\{\{\varnothing\}\}\},\ P(\{\{\{1\}\},\varnothing\}),\ \{\{\varnothing\}\}\})$ ?",
      r"**הגדרה:** תהי $A$ קבוצה. קבוצת החזקה של $A$ היא קבוצת כל תתי-הקבוצות של $A$, כלומר $P(A)=\{X\mid X\subseteq A\}$."
      "\n"
      r"הקבוצה שאנו לוקחים לה את קבוצת החזקה היא בעלת 3 איברים (שונים זה מזה). לכן מספר האיברים בקבוצת החזקה הוא $2^3=8$."),

    Q(1, "א3", "computation", "equivalence_relations", 3,
      INTRO + "**המונח:** יחס שקילות.\n"
      r"**שאלה:** כמה יחסי שקילות ניתן להגדיר מעל הקבוצה $\{1,2,3\}$ ?",
      r"**הגדרה:** תהי $A\ne\varnothing$ קבוצה ויהי $R$ יחס מעל $A$. נאמר כי $R$ יחס שקילות אם $R$ יחס רפלקסיבי, סימטרי וטרנזיטיבי."
      "\n"
      r"השאלה שקולה למציאת מספר החלוקות השונות של הקבוצה $\{1,2,3\}$, כלומר 5."),

    Q(1, "א4", "proof", "partial_orders", 3,
      INTRO + "**המונח:** יחס סדר חלקי.\n"
      "**שאלה:** תנו דוגמה ליחס סדר חלקי שאינו ריק שהוא גם יחס שקילות (יש לציין גם את הקבוצה עליה מוגדר היחס).",
      r"**הגדרה:** תהי $A\ne\varnothing$ קבוצה ויהי $R$ יחס מעל $A$. נאמר כי $R$ יחס סדר חלקי אם $R$ יחס רפלקסיבי, אנטי-סימטרי וטרנזיטיבי."
      "\n"
      r"**דוגמה:** נבחר $A=\{1,2,3\}$, $R=\{(1,1),(2,2),(3,3)\}$."),

    Q(1, "א5", "computation", "functions", 3,
      INTRO + "**המונח:** פונקציה חד-חד-ערכית.\n"
      r"**שאלה:** כמה פונקציות חד-חד-ערכיות ניתן להגדיר מהקבוצה $\{1,2,3\}$ לקבוצה $\{1,2,3,4,5\}$ ?",
      r"**הגדרה:** תהיינה $A,B\ne\varnothing$ קבוצות לא ריקות. נאמר כי הפונקציה $f:A\to B$ חד-חד-ערכית אם לכל $a_1,a_2\in A$ מתקיים: "
      r"אם $f(a_1)=f(a_2)$ אז $a_1=a_2$."
      "\n"
      r"מספר הפונקציות: $\dfrac{5!}{2!}=P(5,3)=5\cdot4\cdot3=60$."),

    Q(1, "ב", "computation", "logic_propositional", 5,
      r"בנו את צורת DNF עבור הפסוק: $p\wedge(r\to p)\wedge(q\to r)$. העזר בטבלת אמת לפתרון השאלה.",
      "הפתרון הרשמי עם תיקון: בטבלת האמת של הפתרון הרשמי, בשורה $p=T,\\ q=F,\\ r=T$ נכתב $r\\to p=F$, אך $T\\to T=T$. "
      "לכן הפסוק אמת גם בשורה זו, והיא מתווספת לצורת ה-DNF."
      "\n"
      "טבלת האמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | q→r | r→p | p∧(r→p)∧(q→r)\n"
      "T T T |  T  |  T  |        T\n"
      "T T F |  F  |  T  |        F\n"
      "T F T |  T  |  T  |        T\n"
      "T F F |  T  |  T  |        T\n"
      "F T T |  T  |  F  |        F\n"
      "F T F |  F  |  T  |        F\n"
      "F F T |  T  |  F  |        F\n"
      "F F F |  T  |  T  |        F\n"
      "```\n"
      r"הפסוק אמת בשלוש שורות, ולכן צורת ה-DNF היא:"
      "\n"
      r"$$(p\wedge q\wedge r)\vee(p\wedge\neg q\wedge r)\vee(p\wedge\neg q\wedge\neg r)$$",
      solutionSource="solved"),

    Q(1, "ג", "proof", "quantifiers_proofs", 5,
      "שלולו את הטענה:\n"
      "\"לכל $x\\in A$, קיימים $y\\in B$ וגם $z\\in C$, כך ש: $x=y+z$\" "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      "השלילה: \"קיים $x\\in A$ כך שלכל $y\\in B$ ולכל $z\\in C$ מתקיים $x\\ne y+z$\"."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 10,
      r"הוכיחו באינדוקציה: $n^2<2^n$ לכל $5\le n\in\mathbb{N}$.",
      r"**בסיס האינדוקציה:** $n=5$: $5^2<2^5$, כלומר $25<32$ ✓."
      "\n"
      r"**הנחת האינדוקציה:** $n^2<2^n$ לכל $5\le n\in\mathbb{N}$."
      "\n"
      r"**צעד האינדוקציה:** נוכיח $(n+1)^2<2^{n+1}$."
      "\n"
      r"**הוכחה:**"
      "\n"
      r"$$(n+1)^2=n^2+2n+1<n^2+3n<n^2+n^2=2n^2<2\cdot2^n=2^{n+1}$$"
      "\n"
      r"כאשר: $n^2+2n+1<n^2+3n$ כי $n>1$; $n^2+3n<n^2+n^2$ כי $n>3$; ו-$2n^2<2\cdot2^n$ לפי הנחת האינדוקציה."
      "\n"
      r"**מסקנה סופית:** הטענה נכונה לכל $5\le n\in\mathbb{N}$."),

    Q(2, "ב", "computation", "sets_power_set", 8,
      r"תהיינה הקבוצות $A=\{3^n\cdot5^n\cdot7^m:\ m,n\in\{0,1,2,\ldots,99\}\}$ ו-$B=\{3^n\cdot5^m\cdot7^m:\ m,n\in\{0,1,2,\ldots,99\}\}$."
      "\n"
      r"מצאו את $A\cap B$ וגם חשבו את $|P(A\cap B)|$. נמקו תשובתכם!",
      r"$A\cap B=\{3^n\cdot5^n\cdot7^n\mid n\in\{0,\ldots,99\}\}$."
      "\n"
      r"**נימוק:** איבר כללי נראה כך: $x=3^\alpha5^\beta7^\gamma$."
      "\n"
      r"$\alpha=\beta\iff x\in A$ ו-$\beta=\gamma\iff x\in B$."
      "\n"
      r"לכן $x\in A\cap B\iff\alpha=\beta=\gamma$."
      "\n"
      r"מסקנה: $|A\cap B|=100$, ולכן $|P(A\cap B)|=2^{100}$."),

    Q(2, "ג", "proof", "sets_power_set", 7,
      r"**(1)** הוכיחו: לכל שתי קבוצות לא ריקות ושונות $A,B$ מתקיים: $P(A)\cup P(B)\subseteq P(A\cup B)$."
      "\n"
      r"**(2)** הראו שקיימות שתי קבוצות לא ריקות ושונות $A,B$ כך ש: $P(A\cup B)\not\subseteq P(A)\cup P(B)$.",
      r"**(1)** הוכחה: תהי $C\in P(A)\cup P(B)$. לפי הגדרת האיחוד, $C\in P(A)$ או $C\in P(B)$. "
      r"לפי הגדרת קבוצת החזקה, $C\subseteq A$ או $C\subseteq B$, ולכן בהכרח $C\subseteq A\cup B$. "
      r"לכן לפי הגדרת קבוצת החזקה $C\in P(A\cup B)$."
      "\n"
      r"**(2)** דוגמה: נבחר $A=\{1\}$, $B=\{2\}$."
      "\n"
      r"$\{1,2\}\in P(A\cup B)$, אך $\{1,2\}\notin P(A)$ וגם $\{1,2\}\notin P(B)$, ולכן $\{1,2\}\notin P(A)\cup P(B)$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "equivalence_relations", 12,
      r"יהי היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ שמוגדר לפי הכלל הבא: לכל $x,y\in\mathbb{Z}$, מתקיים $xRy\iff 2\mid(7x+y)$."
      "\n"
      r"הוכיחו ש: $R$ הוא יחס שקילות ומצאו את קבוצת המנה $\mathbb{Z}/R$.",
      r"**$R$ הוא יחס רפלקסיבי:** יהי $x\in\mathbb{Z}$. אז $2\mid(7x+x)$, כי $7x+x=8x$ מתחלק ב-2."
      "\n"
      r"**$R$ הוא יחס סימטרי:** יהיו $x,y\in\mathbb{Z}$. נניח $2\mid(7x+y)$. נניח בשלילה כי $2\nmid(7y+x)$. אז $7y+x$ הוא מספר אי-זוגי, ו-$7x+y$ הוא מספר זוגי, "
      r"ולכן הסכום $(7y+x)+(7x+y)$ הוא מספר אי-זוגי. אך $(7y+x)+(7x+y)=8x+8y=8(x+y)$ הוא מספר זוגי. סתירה. לכן $2\mid(7y+x)$."
      "\n"
      r"**$R$ הוא יחס טרנזיטיבי:** יהיו $x,y,z\in\mathbb{Z}$. נניח $2\mid(7x+y)$ וגם $2\mid(7y+z)$. אז $7x+y$ ו-$7y+z$ הם מספרים זוגיים, ולכן הסכום "
      r"$(7x+y)+(7y+z)=7x+8y+z=(7x+z)+8y$ הוא מספר זוגי. מכיוון ש-$8y$ זוגי, גם $7x+z$ זוגי, כלומר $2\mid(7x+z)$."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"**קבוצת המנה:**"
      "\n"
      r"$[0]=\{x\mid x\in\mathbb{Z}\wedge 0Rx\}=\{x\mid x\in\mathbb{Z}\wedge2\mid(7\cdot0+x)\}=\{x\mid x\in\mathbb{Z}\wedge2\mid x\}=\{2k\mid k\in\mathbb{Z}\}=\{\ldots,-2,0,2,\ldots\}$"
      "\n"
      r"$[1]=\{x\mid x\in\mathbb{Z}\wedge 1Rx\}=\{x\mid x\in\mathbb{Z}\wedge2\mid(7\cdot1+x)\}=\{x\mid x\in\mathbb{Z}\wedge2\nmid x\}=\{2k+1\mid k\in\mathbb{Z}\}=\{\ldots,-1,1,\ldots\}$"
      "\n"
      r"מכיוון ש-$[0]\cup[1]=\mathbb{Z}$, נקבל $\mathbb{Z}/R=\{[0],[1]\}$."),

    Q(3, "ב1", "computation", "equivalence_relations", 4,
      r"תהי $A=\{1,2,3,\ldots,n\}$, כאשר $7<n\in\mathbb{N}$. יהי $R\subseteq A\times A$ יחס שקילות שמקיים את התנאים הבאים: "
      r"$A/R=\{B,C,D\}$, $|B|=2$ וגם $|C|=3$. חשבו את $|R|$.",
      r"נסמן $D=A-(B\cup C)$, ו-$|D|=n-5$."
      "\n"
      r"$B\times B\subseteq R$ כי $[b_1]=[b_2]=B$ כאשר $B=\{b_1,b_2\}$; $C\times C\subseteq R$ כי $[c_1]=[c_2]=[c_3]=C$ כאשר $C=\{c_1,c_2,c_3\}$; "
      r"$D\times D\subseteq R$ כי $[d_i]=D$ כאשר $D=\{d_1,\ldots\}=A-(B\cup C)$."
      "\n"
      r"מסקנה: $R=(B\times B)\cup(C\times C)\cup(D\times D)$, ולכן $|R|=|B|^2+|C|^2+|D|^2=4+9+(n-5)^2$."),

    Q(3, "ב2", "computation", "combinatorics", 4,
      r"תהי $A=\{1,2,3,\ldots,n\}$, כאשר $7<n\in\mathbb{N}$. מהו מספר יחסי השקילות $R\subseteq A\times A$ המקיימים את התנאים הבאים: "
      r"$A/R=\{B,C,D\}$, $|B|=2$ וגם $|C|=3$.",
      r"$B\subseteq A$ ו-$|B|=2$, ולכן יש $\binom n2$ אפשרויות לבחור את $B$."
      "\n"
      r"$C\subseteq A-B$ ו-$|C|=3$, ולכן יש $\binom{n-2}{3}$ אפשרויות לבחור את $C$."
      "\n"
      r"אז $D=A-(B\cup C)$ נקבעת באופן יחיד."
      "\n"
      r"מסקנה: מספר היחסים הוא $\binom n2\cdot\binom{n-2}{3}$."
      "\n"
      r"**הערה:** עבור $n=8$ הקבוצה $D$ היא גם בעלת 3 איברים, ולכן כל יחס נספר פעמיים (פעם עם כל אחת משתי הקבוצות בנות 3 האיברים בתפקיד $C$), "
      r"ומספר היחסים הוא $\frac12\binom82\binom63=280$. עבור $n\ge9$ הנוסחה נכונה."),

    Q(3, "ג", "proof", "partial_orders", 5,
      r"יהי $R\subseteq\{1,2\}\times\{1,2\}$ יחס רפלקסיבי ולא סימטרי. הוכיחו ש: $R$ הוא יחס סדר מלא.",
      r"$R$ רפלקסיבי, ולכן $(1,1),(2,2)\in R$."
      "\n"
      r"$R$ לא סימטרי, ולכן יש 2 אפשרויות: $(1,2)\in R$, ואז $R_1=\{(1,1),(2,2),(1,2)\}$, או $(2,1)\in R$, ואז $R_2=\{(1,1),(2,2),(2,1)\}$."
      "\n"
      r"$R_1$ רפלקסיבי, אנטי-סימטרי וטרנזיטיבי, וכך גם $R_2$; לכן $R=R_1$ או $R=R_2$ הוא יחס סדר חלקי."
      "\n"
      r"בנוסף, לכל $x,y\in\{1,2\}$ כך ש-$x\ne y$: $(1,2)\in R_1$, $(2,1)\in R_2$, כלומר $(x,y)\in R$ או $(y,x)\in R$."
      "\n"
      r"מסקנה: $R_1$ ו-$R_2$ הם יחסי סדר מלא."),

    # ---------------- Q4 ----------------
    Q(4, "א1", "computation", "combinatorics", 5,
      r"תהי הקבוצה $A=\{1,2,3,\ldots,20\}$. מהו מספר היחסים $R\subseteq A\times A$ שהם לא פונקציות ?",
      r"כל יחס $R$ הוא תת-קבוצה של $A\times A$, ולכן מספר היחסים הכולל הוא $|P(A\times A)|=2^{|A\times A|}=2^{400}$."
      "\n"
      r"מספר הפונקציות $R:A\to A$ הוא $|A|^{|A|}=20^{20}$."
      "\n"
      r"לכן מספר היחסים שאינם פונקציות הוא $2^{400}-20^{20}$."
      "\n"
      r"**מקרה כללי:** תהיינה $A,B$ קבוצות, $|A|=m$ ו-$|B|=n$. מספר הפונקציות $f:A\to B$ הוא $|B|^{|A|}=n^m$. "
      r"הסבר: לכל פונקציה $f:A\to B$ מוגדרת על ידי $f(a_1),f(a_2),\ldots,f(a_m)$, וכל אחד מהם הוא איבר ב-$B$ ($n$ אפשרויות), "
      r"כלומר ניתן לבחור את $f(a_i)\in B$ ב-$n$ דרכים לכל $i$, ולכן מספר הפונקציות הוא $n^m$."),

    Q(4, "א2", "computation", "combinatorics", 5,
      r"תהי הקבוצה $A=\{1,2,3,\ldots,20\}$. מהו מספר היחסים $R\subseteq A\times A$ שמקיימים התנאי: $3\le|R|\le5$ ?",
      r"בהינתן $|A\times A|=|A|\cdot|A|=20^2=400$, נקבל:"
      "\n"
      r"מספר היחסים בגודל 3 הוא $\binom{400}{3}$, בגודל 4 הוא $\binom{400}{4}$, ובגודל 5 הוא $\binom{400}{5}$."
      "\n"
      r"מסקנה: מספר היחסים הוא $\binom{400}{3}+\binom{400}{4}+\binom{400}{5}$."),

    Q(4, "ב1", "computation", "functions", 5,
      r"תהי $B=\{0,1,2,\ldots,9\}$. כמה פונקציות הפיכות $f:B\to B$ מקיימות: $f(\{0,1,2\})=\{0,1,2\}$ וגם $f(\{3,4,5,6\})=\{3,4,5,6\}$ ?",
      r"מכיוון ש-$f$ הפיכה, היא חח״ע ועל, ולכן גם $f(\{7,8,9\})=\{7,8,9\}$."
      "\n"
      r"מספר האפשרויות עבור $f(\{0,1,2\})=\{0,1,2\}$ הוא $3!$; עבור $f(\{3,4,5,6\})=\{3,4,5,6\}$ הוא $4!$; עבור $f(\{7,8,9\})=\{7,8,9\}$ הוא $3!$."
      "\n"
      r"מסקנה: מספר הפונקציות המתאימות הוא $3!\cdot4!\cdot3!$."),

    Q(4, "ב2", "computation", "sets_power_set", 5,
      r"כמה תתי-קבוצות של $B=\{0,1,2,\ldots,9\}$ מכילות את כל המספרים הזוגיים של $B$ ?",
      r"נבחר $C=\{0,2,4,6,8\}\cup D$, כאשר $D\subseteq\{1,3,5,7,9\}$ תת-קבוצה כלשהי."
      "\n"
      r"מספר תתי-הקבוצות $C$ שווה למספר תתי-הקבוצות $D$ של $\{1,3,5,7,9\}$, כלומר $|P(\{1,3,5,7,9\})|=2^5$."
      "\n"
      r"מסקנה: מספר תתי-הקבוצות של $B$ שמכילות את כל המספרים הזוגיים הוא $2^5=32$."),

    Q(4, "ג", "proof", "modular_fermat_wilson", 5,
      r"תהי $D$ קבוצה בעלת $2^{10}=1024$ תתי-קבוצות בגודל זוגי. חשבו את $m=|D|$ והראו ש: $11\mid\left(\varnothing(m)^{\varnothing(m)}-1\right)$."
      "\n"
      r"שימו לב: הסימן $\varnothing$ מסמל את הפונקציה $\varphi$, “פי של אוילר”.",
      r"נתון: אם $|D|=n$, אז מספר תתי-הקבוצות של $D$ בגודל זוגי הוא $2^{n-1}$."
      "\n"
      r"כאן: $2^{n-1}=2^{10}\Rightarrow n=11$, כלומר $m=|D|=11$, ולכן $\varphi(m)=10$."
      "\n"
      r"נשאר להראות ש: $11\mid\left(10^{10}-1\right)$."
      "\n"
      r"מכיוון ש-$11\nmid10$, לפי משפט FERMAT: $10^{10}-1=10^{11-1}-1$, ולכן $11\mid\left(10^{11-1}-1\right)\iff11\mid\left(10^{10}-1\right)$."),

    # ---------------- Q5 ----------------
    Q(5, "א", "proof", "number_theory_gcd", 10,
      r"תהי הקבוצה $A=\{a_1,a_2,\ldots,a_{101}\}\subset\mathbb{N}$. הראו שקיימים $a_i,a_j\in A$ כך ש: $1\le i<j\le101$ וגם $100\mid(a_i-a_j)$.",
      r"נתאים לכל המספרים ב-$A$ את שאריותיהם מודולו 100, ונקבל 101 שאריות:"
      "\n"
      r"$(*)\quad a_1\pmod{100},\ a_2\pmod{100},\ \ldots,\ a_{101}\pmod{100}$."
      "\n"
      r"מכיוון שלכל $n\in\mathbb{Z}$ השארית $n\pmod{100}$ היא מספר שמקיים $0\le n\pmod{100}\le99$, כלומר יש 100 ערכים אפשריים בלבד, "
      r"אז לפי עקרון שובך היונים בסדרה $(*)$ חייבים להיות שני מספרים שווים (לפחות)."
      "\n"
      r"כלומר קיימים $a_i,a_j\in A$ כך ש-$a_i\ne a_j$ ו-$a_i\pmod{100}=a_j\pmod{100}$, ולכן $100\mid(a_i-a_j)$."),

    Q(5, "ב", "proof", "cardinality_sets", 7,
      r"הוכיחו ש: $|\mathbb{Q}\cap(0,1)|=|\mathbb{Z}|$.",
      r"**מבחן:** מספיק להוכיח ש-$|\mathbb{Q}\cap(0,1)|=|\mathbb{Q}|$, כי $|\mathbb{Q}|=|\mathbb{Z}|$."
      "\n"
      r"**טענה I:** $|\mathbb{Q}\cap(0,1)|\le|\mathbb{Q}|$, כי $\mathbb{Q}\cap(0,1)\subseteq\mathbb{Q}$."
      "\n"
      r"**טענה II:** $|\mathbb{Q}|\le|\mathbb{Q}\cap(0,1)|$. נבחר $A=\left\{\frac12,\frac13,\frac14,\ldots,\frac1n,\ldots\right\}$. "
      r"אז $|A|=|\mathbb{N}|=|\mathbb{Q}|$ וגם $A\subseteq\mathbb{Q}\cap(0,1)$, ולכן $|\mathbb{Q}|=|A|\le|\mathbb{Q}\cap(0,1)|$."
      "\n"
      r"**מסקנה:** מ-I ו-II נקבל $|\mathbb{Q}|=|\mathbb{Q}\cap(0,1)|$."),

    Q(5, "ג", "computation", "recurrence_sums", 8,
      r"מצאו את הצורה המפורשת של $(a_n)$, כאשר: $a_n=5a_{n-1}-6a_{n-2}$ ($n\ge2$), $a_0=7$ ו-$a_1=15$.",
      r"המשוואה האופיינית: $r^2-5r+6=0\to r_1=2,\ r_2=3$. לכן $a_n=C_1\cdot2^n+C_2\cdot3^n$."
      "\n"
      r"$a_0=C_1+C_2=7$"
      "\n"
      r"$a_1=2C_1+3C_2=15$"
      "\n"
      r"נקבל $C_2=1$, $C_1=6$."
      "\n"
      r"מסקנה: $a_n=6\cdot2^n+3^n$, לכל $n\in\mathbb{N}$."),
]

exam = {
    "examCode": "19A-A",
    "examLabel": 'בדידה 1, תשע"ט, מועד א (2019)',
    "year": 2019,
    "examDate": "03.03.2019",
    "sourceFile": "19A-A exam with handwritten solution, pp.1-17",
    "solutionFile": "19A-A handwritten solution (author unknown, titled 3.3.19), pp.3-17",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
