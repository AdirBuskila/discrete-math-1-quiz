# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-A.json -- discrete math 1, semester A 5784, moed A (18.03.2024).
4 mandatory questions of 25 points, parts (a)-(c). Key: the typed official solution printed after each question.
Run: PYTHONUTF8=1 py tools/gen/gen_24A-A.py
A part with numbered sub-claims ((1), (2)) is ONE item.
Slips of the typed key corrected while transcribing (listed in docs/ASK_ADIR.md): Q1c "f(x1)=f(x1)" -> "f(x1)=f(x2)",
Q3c "(100^5)^30-1=(10^7)^30-1" -> "(10^10)^30-1" (100^5 = 10^10)."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-A.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "lecturer-solution", "official": True, "confidence": "high"}
    q.update(kw)
    return q


INTRO = "בכל סעיף עליך להגדיר את המונח הרשום בסעיף ולענות על שאלה קצרה הקשורה אליו.\n"

questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "computation", "logic_propositional", 8,
      INTRO + "**המונח:** שקילות לוגית.\n"
      "**שאלה:** הוכיחו (באמצעות טבלת אמת) האם הפסוקים הבאים שקולים לוגית:\n"
      r"$$p\to(q\wedge r)\ \equiv\ (p\to q)\wedge(p\to r)$$",
      "**הגדרה:** שני פסוקים נקראים שקולים לוגית אם יש להם אותה טבלת אמת.\n"
      "טבלת אמת (T = אמת, F = שקר):\n"
      "```\n"
      "p q r | q∧r | p→(q∧r) | p→q | p→r | (p→q)∧(p→r)\n"
      "T T T |  T  |    T     |  T  |  T  |      T\n"
      "T T F |  F  |    F     |  T  |  F  |      F\n"
      "T F T |  F  |    F     |  F  |  T  |      F\n"
      "T F F |  F  |    F     |  F  |  F  |      F\n"
      "F T T |  T  |    T     |  T  |  T  |      T\n"
      "F T F |  F  |    T     |  T  |  T  |      T\n"
      "F F T |  F  |    T     |  T  |  T  |      T\n"
      "F F F |  F  |    T     |  T  |  T  |      T\n"
      "```\n"
      "שתי העמודות המודגשות ($p\\to(q\\wedge r)$ ו-$(p\\to q)\\wedge(p\\to r)$) זהות, ולכן הביטויים שקולים זה לזה."),

    Q(1, "ב", "computation", "sets_power_set", 8,
      INTRO + "**המונח:** קבוצת חזקה.\n"
      r"**שאלה:** חשב את $P\big(P(P(\emptyset))\big)$.",
      r"**הגדרה:** תהי $A$ קבוצה כלשהי. נסמן ב-$P(A)$ את **קבוצת החזקה** של $A$, אשר איבריה הם כל תתי-הקבוצות של $A$. "
      r"בסימול מתמטי: $P(A):=\{B:\ B\subseteq A\}$."
      "\n"
      r"$P(\emptyset)=\{\emptyset\}$"
      "\n"
      r"$P(P(\emptyset))=P(\{\emptyset\})=\{\emptyset,\{\emptyset\}\}$"
      "\n"
      r"$$P(P(P(\emptyset)))=P\big(\{\emptyset,\{\emptyset\}\}\big)=\big\{\emptyset,\{\emptyset\},\{\{\emptyset\}\},\{\emptyset,\{\emptyset\}\}\big\}$$"),

    Q(1, "ג", "proof", "functions", 9,
      INTRO + "**המונח:** פונקציה חד-חד-ערכית.\n"
      r"**שאלה:** תהי הפונקציה $f:\mathbb{R}\to\mathbb{R}$ המוגדרת כך: $f(x)=x^3$. הוכיחו שהפונקציה $f$ היא חד-חד-ערכית.",
      r"**הגדרה:** תהי $f:B\to A$ פונקציה. $f$ תקרא חח״ע אם״ם: $\forall x_1,x_2\in B:\ f(x_1)=f(x_2)\Rightarrow x_1=x_2$."
      "\n"
      r"יהיו $x_1,x_2\in\mathbb{R}$ כך ש-$f(x_1)=f(x_2)$. אז:"
      "\n"
      r"$$(x_1)^3=(x_2)^3\ \Rightarrow\ \sqrt[3]{(x_1)^3}=\sqrt[3]{(x_2)^3}\ \Rightarrow\ x_1=x_2$$"
      "\n"
      r"לכן $f$ היא חח״ע."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 11,
      r"הוכיחו באינדוקציה מתמטית שלכל $1\le n\in\mathbb{N}$ מתקיים:"
      "\n"
      r"$$(2n+1)+(2n+3)+(2n+5)+\dots+(4n-1)=3n^2$$",
      r"נסמן $P(n):\ (2n+1)+(2n+3)+(2n+5)+\dots+(4n-1)=3n^2$."
      "\n"
      r"**1. בסיס האינדוקציה:** נבדוק את הטענה עבור $P(1)$: $(2\cdot 1+1)=3=3\cdot 1^2\Rightarrow P(1)\equiv T$."
      "\n"
      r"**2. שלב האינדוקציה:** $\forall 1\le k\in\mathbb{N}$: $P(k)\equiv T\Rightarrow P(k+1)\equiv T$. נוכיח כי:"
      "\n"
      r"$P(k):\ (2k+1)+(2k+3)+(2k+5)+\dots+(4k-1)=3k^2$"
      "\n"
      r"$P(k+1):\ (2k+3)+(2k+5)+(2k+7)+\dots+(4k+3)=3(k+1)^2$"
      "\n"
      r"$$(2k+3)+(2k+5)+(2k+7)+\dots+(4k+3)=(2k+1)+(2k+3)+(2k+5)+(2k+7)+\dots+(4k-1)+(4k+1)+(4k+3)-(2k+1)$$"
      "\n"
      r"$$=3k^2+(4k+1)+(4k+3)-(2k+1)=3k^2+6k+3=3(k^2+2k+1)=3(k+1)^2\Rightarrow P(k+1)\equiv T$$"
      "\n"
      r"מסקנה: 1 ו-2 מתקיימים, לכן לפי משפט האינדוקציה המתמטית $\forall 1\le n\in\mathbb{N}:\ P(n)\equiv T$."),

    Q(2, "ב", "computation", "number_theory_gcd", 8,
      r"מצאו $x,y\in\mathbb{Z}$ בעזרת האלגוריתם המורחב של EUCLID כך ש: $\gcd(25,40)=25x+40y$.",
      "הטבלה של האלגוריתם המורחב (בכל שורה: $d$ הוא ה-gcd, ו-$x\\leftarrow y'$ ו-$y\\leftarrow x'-y'\\cdot\\lfloor a/b\\rfloor$ "
      "מחושבים מהשורה שמתחת):\n"
      "```\n"
      "  a    b    floor(a/b)   d    x    y\n"
      "  25   40        0        5   -3    2\n"
      "  40   25        1        5    2   -3\n"
      "  25   15        1        5   -1    2\n"
      "  15   10        1        5    1   -1\n"
      "  10    5        2        5    0    1\n"
      "   5    0       --        5    1    0\n"
      "```\n"
      r"$$\gcd(25,40)=5=25\cdot(-3)+40\cdot 2$$"),

    Q(2, "ג", "computation", "equivalence_relations", 6,
      r"תנו דוגמאות $R_1,R_2\subseteq\{1,2,3\}\times\{1,2,3\}$ של יחסים כך ש:"
      "\n"
      r"(1) $R_1$ הוא יחס שקילות."
      "\n"
      r"(2) $R_2$ הוא יחס סדר מלא.",
      r"**(1)** $R_1\subseteq\{1,2,3\}\times\{1,2,3\}$, $R_1=\{(1,1),(2,2),(3,3)\}$."
      "\n"
      r"**(2)** $R_2\subseteq\{1,2,3\}\times\{1,2,3\}$, $R_2=\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "proof", "sets_power_set", 10,
      r"נתונות 3 קבוצות: $A,B,C$."
      "\n"
      r"הוכיחו או הפריכו: $A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)$",
      r"מתקיים:"
      "\n"
      r"$$(A\setminus B)\cup(A\setminus C)=(A\cap B^c)\cup(A\cap C^c)=A\cap(B^c\cup C^c)=A\cap(B\cap C)^c=A\setminus(B\cap C)$$"
      "\n"
      r"ולכן הקביעה נכונה."),

    Q(3, "ב", "proof", "quantifiers_proofs", 6,
      r"הוכיחו את הטענה הבאה בשיטת ה-contrapositive:"
      "\n"
      r"אם $x,y\in\mathbb{Z}$ ו-$xy$ הוא מספר זוגי, אז לפחות אחד מהמספרים $x$ או $y$ הוא זוגי.",
      r"ראשית, צורת ה-contrapositive של הפסוק אותו אנו רוצים להוכיח היא:"
      "\n"
      r"$$(\exists k_1\in\mathbb{Z}:\ x=2k_1+1)\wedge(\exists k_2\in\mathbb{Z}:\ y=2k_2+1)\to(\exists k_3\in\mathbb{Z}:\ xy=2k_3+1)$$"
      "\n"
      r"נניח ש-$x=2k_1+1$ ו-$y=2k_2+1$. אזי:"
      "\n"
      r"$$xy=(2k_1+1)(2k_2+1)=4k_1k_2+2k_1+2k_2+1=2(2k_1k_2+k_1+k_2)+1=2k_3+1$$"
      "\n"
      r"כאשר $k_3=2k_1k_2+k_1+k_2$. בזאת הוכחה הגרירה."),

    Q(3, "ג", "proof", "modular_fermat_wilson", 9,
      r"הראו ש: $30\le\gcd(30!+1\ ,\ 100^{150}-1)$",
      r"כיוון ש-31 הוא ראשוני, לפי משפט וילסון $31\mid(30!+1)$. בנוסף, מתקיים"
      "\n"
      r"$$100^{150}-1=(100^5)^{30}-1=(10^{10})^{30}-1$$"
      "\n"
      r"ולפי המשפט הקטן של פרמה, מכיוון ש-$\gcd(10^{10},31)=1$ מתקיים $31\mid\big((10^{10})^{30}-1\big)$, כלומר $31\mid(100^{150}-1)$."
      "\n"
      r"מכאן:"
      "\n"
      r"$$\big(31\mid(30!+1)\big)\wedge\big(31\mid(100^{150}-1)\big)\Rightarrow 31\mid\gcd(30!+1,\ 100^{150}-1)$$"
      "\n"
      r"$$\Rightarrow 31\le\gcd(30!+1,\ 100^{150}-1)\Rightarrow 30\le 31\le\gcd(30!+1,\ 100^{150}-1)$$"),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "equivalence_relations", 14,
      r"נתון היחס $R\subseteq Z\times Z$ שמוגדר לפי הכלל הבא:"
      "\n"
      r"לכל $x,y\in Z$ מתקיים: $xRy\iff 4\mid(x+3y)$."
      "\n"
      r"הוכיחו ש: $R$ הוא יחס שקילות ומצאו את קבוצת המנה $A/R$."
      "\n"
      "האם $R$ הוא יחס סדר חלקי ?",
      r"**רפלקסיביות:** $\forall x\in\mathbb{Z},\ 4\mid 4x\Rightarrow 4\mid(x+3x)\Rightarrow(x,x)\in R$."
      "\n"
      r"**סימטריות:** $\forall x,y\in\mathbb{Z}:\ (x,y)\in R\Rightarrow 4\mid(x+3y)\Rightarrow 4\mid(4x+4y-3x-y)$"
      "\n"
      r"$\Rightarrow 4\mid\big(4(x+y)+(-3x-y)\big),\ (x+y)\in\mathbb{Z}\Rightarrow 4\mid\big(-(3x+y)\big)\Rightarrow 4\mid(3x+y)\Rightarrow(y,x)\in R$."
      "\n"
      r"**טרנזיטיביות:** $\forall x,y,z\in\mathbb{Z}:\ (x,y)\in R\wedge(y,z)\in R\Rightarrow 4\mid(x+3y)\wedge 4\mid(y+3z)$"
      "\n"
      r"$\Rightarrow 4\mid\big((x+3y)+(y+3z)\big)\Rightarrow 4\mid\big((x+3z)+4y\big),\ y\in\mathbb{Z}\Rightarrow 4\mid(x+3z)\Rightarrow(x,z)\in R$."
      "\n"
      r"מסקנה: $R$ הוא יחס רפלקסיבי, סימטרי וטרנזיטיבי ולכן הוא יחס שקילות."
      "\n"
      r"נחשב את מחלקות השקילות:"
      "\n"
      r"$[0]=\{x:\ x\in\mathbb{Z}\wedge xR0\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+0)\}=\{4k:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[1]=\{x:\ x\in\mathbb{Z}\wedge xR1\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+3)\}=\{4k-3:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[2]=\{x:\ x\in\mathbb{Z}\wedge xR2\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+6)\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+4+2)\}=\{4k-2:\ k\in\mathbb{Z}\}$"
      "\n"
      r"$[3]=\{x:\ x\in\mathbb{Z}\wedge xR3\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+9)\}=\{x:\ x\in\mathbb{Z}\wedge 4\mid(x+8+1)\}=\{4k-1:\ k\in\mathbb{Z}\}$"
      "\n"
      r"מכיוון ש-$[0]\cup[1]\cup[2]\cup[3]=\mathbb{Z}$ אין עוד מחלקות שקילות. לכן $\mathbb{Z}/R=\{[0],[1],[2],[3]\}$."
      "\n"
      r"$R$ אינו יחס סדר חלקי כי אינו אנטי-סימטרי לדוגמה: $(0,4)\in R$ וגם $(4,0)\in R$ אך $0\ne 4$."),

    Q(4, "ב", "computation", "logic_propositional", 6,
      r"מצאו את צורת ה-DNF של הפסוק הבא (באמצעות טבלת אמת):"
      "\n"
      r"$$(p\wedge q)\leftrightarrow(\neg q\vee r)$$",
      "טבלת אמת (T = אמת, F = שקר):\n"
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
      r"$$\mathrm{DNF}:\ (p\wedge q\wedge r)\vee(\neg p\wedge q\wedge\neg r)$$"),

    Q(4, "ג", "proof", "number_theory_gcd", 5,
      r"מצאו כל מספר ראשוני $p$ כך שגם $p^3-1$ הוא מספר ראשוני.",
      r"עבור $p=2$ נקבל $p^3-1=7$ מספר ראשוני."
      "\n"
      r"עבור $p=3$ נקבל $p^3-1=26$ ואינו מספר ראשוני."
      "\n"
      r"עבור $p>3$: אזי $p=2q+1$ כאשר $1<q\in\mathbb{N}$."
      "\n"
      r"$$p^3-1=8q^3+12q^2+6q+1-1=2(4q^3+6q^2+3q)$$"
      "\n"
      r"מכיוון ש-$1<4q^3+6q^2+3q\in\mathbb{N}$, למספר $p^3-1$ יש לפחות 3 מחלקים: $1,\ 2,\ p^3-1$, ולכן $p^3-1$ אינו מספר ראשוני."
      "\n"
      r"מסקנה: $p^3-1$ הוא ראשוני רק עבור $p=2$."),
]

exam = {
    "examCode": "24A-A",
    "examLabel": 'בדידה 1, סמסטר א\' תשפ"ד, מועד א (18.03.2024)',
    "year": 2024,
    "examDate": "18.03.2024",
    "sourceFile": "24A-A exam with typed official solution, pp.1-7",
    "solutionFile": "24A-A typed official solution, pp.2-7",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
