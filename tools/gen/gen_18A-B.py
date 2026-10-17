# -*- coding: utf-8 -*-
"""Generator for tools/raw/18A-B.json -- discrete math 1 (21166), semester A 5778, moed B (21.03.2018).
4 mandatory questions of 25 points (scan, read by vision). The handwritten key (author unknown) is student-solution.
Checks: tools/verify/18A-B/verify.py.
Run: PYTHONUTF8=1 py tools/gen/gen_18A-B.py
 - Q1a, Q1b (b1+b2), Q3a (a1-a4), Q4b (b1-b3) are ONE item each.
 - Q4c: the key answers 495 = C(12,4), the number of letter-count vectors, not the number of words; shipped with the
   correction label (solved, official false) and the script-checked word count."""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18A-B.json"


def Q(num, part, kind, topic, points, question, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points,
         "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


questions = [
    # ---------------- Q1 ----------------
    Q(1, "א", "computation", "combinatorics", 12,
      r"הגדירו את המושג של **תמורה אי-סדר מלא**. תנו 2 דוגמאות של תמורות של הקבוצה $A=\{1,2,3,4\}$, "
      r"כך שרק אחת היא תמורה אי-סדר מלא."
      "\n"
      r"כמה תמורות יש לקבוצה $A$? כמה תמורות אי-סדר מלא יש לקבוצה $A$?",
      r"**הגדרה:** התמורה $(k_1,k_2,\ldots,k_n)$ של הקבוצה $\{1,2,\ldots,n\}$ נקראת תמורה אי-סדר מלא אם: "
      r"$k_i\ne i$ לכל $i\in\{1,2,\ldots,n\}$."
      "\n"
      r"**דוגמאות:** אם $A=\{1,2,3,4\}$ אז:"
      "\n"
      r"$(2,1,4,3)$ היא תמורה אי-סדר מלא;"
      "\n"
      r"$(1,3,4,2)$ אינה תמורה אי-סדר מלא (כי $k_1=1$)."
      "\n"
      r"**מספר התמורות:** ל-$A=\{1,2,3,4\}$ יש $4!=24$ תמורות."
      "\n"
      r"**מספר תמורות אי-סדר מלא:** ל-$A=\{1,2,3,4\}$ יש $D_4=9$ תמורות אי-סדר מלא:"
      "\n"
      r"$$D_4=4!\left(\frac1{0!}-\frac1{1!}+\frac1{2!}-\frac1{3!}+\frac1{4!}\right)=24\left(\frac12-\frac16+\frac1{24}\right)=12-4+1=9$$"),

    Q(1, "ב", "proof", "cardinality_sets", 9,
      "הוכיחו או הפריכו:\n"
      r"**(1)** $|\mathbb{Q}\cap(0,1)|=|\mathbb{Z}|$."
      "\n"
      r"**(2)** $P(A\times B)=P(A)\times P(B)$ לכל 2 קבוצות $A,B$.",
      r"**(1)** הטענה נכונה, כי:"
      "\n"
      r"$\left\{\frac12,\frac1{2^2},\frac1{2^3},\ldots\right\}\subseteq\mathbb{Q}\cap(0,1)\subseteq\mathbb{Q}$, ולכן "
      r"$|\mathbb{Z}|=|\mathbb{N}|=\left|\left\{\frac12,\frac1{2^2},\ldots\right\}\right|\le|\mathbb{Q}\cap(0,1)|\le|\mathbb{Q}|=|\mathbb{Z}|$."
      "\n"
      r"לכן $\aleph_0=|\mathbb{Q}\cap(0,1)|=|\mathbb{Z}|$."
      "\n"
      r"**(2)** הטענה אינה נכונה. דוגמה נגדית: $A=\{1\}$, $B=\{2\}$."
      "\n"
      r"$(\{1\},\{2\})\in P(A)\times P(B)$, אך $(\{1\},\{2\})\notin P(A\times B)$,"
      "\n"
      r"כי $P(A\times B)=P(\{(1,2)\})=\{\varnothing,\{(1,2)\}\}$."),

    Q(1, "ג", "proof", "quantifiers_proofs", 4,
      "שלולו את הטענה:\n"
      "\"לכל $(x,y)\\in A\\times B$ קיים $z\\in C$, כך ש: $z\\le x+y$\" "
      "כך שבתשובתכם לא יופיע קשר השלילה.",
      r"השלילה: "
      "\"קיים $(x,y)\\in A\\times B$ כך שלכל $z\\in C$ מתקיים $z>x+y$\"."),

    # ---------------- Q2 ----------------
    Q(2, "א", "proof", "induction", 10,
      r"השתמשו באינדוקציה מתמטית כדי להוכיח את נכונות הטענה הבאה: "
      r"לכל $n\in\mathbb{N}$, $1\le n$, מתקיים: "
      r"$(2n+1)+(2n+3)+(2n+5)+\ldots+(4n+1)=3n^2+4n+1$, לכל $1\le n\in\mathbb{N}$.",
      r"$P(n):\ (2n+1)+(2n+3)+\ldots+(4n+1)=3n^2+4n+1$, לכל $n\in\mathbb{N}$, $n\ge1$."
      "\n"
      r"**I.** $P(1):\ 3+5=3+4+1\iff8=8$ — TRUE."
      "\n"
      r"**II.** נוכיח: אם $P(k)=\text{TRUE}$ עבור $k\ge1$, אז גם $P(k+1)=\text{TRUE}$."
      "\n"
      r"$P(k):\ (2k+1)+(2k+3)+\ldots+(4k+1)=3k^2+4k+1$"
      "\n"
      r"$P(k+1):\ (2k+3)+\ldots+(4k+1)+(4k+3)+(4k+5)=3(k+1)^2+4(k+1)+1$"
      "\n"
      r"לפי $P(k)=\text{TRUE}$, הסכום $(2k+3)+\ldots+(4k+1)$ שווה ל-$(3k^2+4k+1)-(2k+1)$, ולכן אגף שמאל של $P(k+1)$ הוא:"
      "\n"
      r"$$\left((3k^2+4k+1)-(2k+1)\right)+8k+8=3k^2+4k+1-2k-1+8k+8=3k^2+10k+8$$"
      "\n"
      r"אגף ימין: $$3(k+1)^2+4(k+1)+1=3(k^2+2k+1)+4k+5=3k^2+6k+3+4k+5=3k^2+10k+8$$"
      "\n"
      r"האגפים שווים, ולכן $P(k+1)=\text{TRUE}$."
      "\n"
      r"**III.** מ-I ו-II נובע ש-$P(n)=\text{TRUE}$ לכל $n\in\mathbb{N}$, $n\ge1$."),

    Q(2, "ב", "proof", "relations_properties", 5,
      r"הוכיחו או הפריכו: אם $\varnothing\ne A$ ו-$R_2,R_1\subseteq A\times A$ יחסים טרנזיטיביים, אז גם $R_2\cup R_1$ טרנזיטיבי.",
      r"הטענה אינה נכונה. דוגמה נגדית:"
      "\n"
      r"$A=\{1,2\}$, $R_1=\{(1,2)\}$, $R_2=\{(2,1)\}$. שני היחסים טרנזיטיביים."
      "\n"
      r"$R_1\cup R_2=\{(1,2),(2,1)\}$ אינו טרנזיטיבי, כי $(1,2),(2,1)\in R_1\cup R_2$ אך $(1,1)\notin R_1\cup R_2$."),

    Q(2, "ג", "proof", "equivalence_relations", 10,
      r"היחס $R\subseteq\mathbb{Z}\times\mathbb{Z}$ מוגדר לפי הכלל: לכל $x,y\in\mathbb{Z}$, מתקיים $xRy\iff3x+y$ הוא מספר זוגי."
      "\n"
      r"בדקו ש-$R$ הוא יחס שקילות מעל $\mathbb{Z}$ ומצאו את $\mathbb{Z}/R$."
      "\n"
      r"האם $R$ הוא יחס סדר חלקי? אם כן הוכיחו, אחרת תנו דוגמה נגדית.",
      r"**(1)** $R$ רפלקסיבי: לכל $x\in\mathbb{Z}$ נכון $(x,x)\in R$, כי $2\mid4x=3x+x$."
      "\n"
      r"$R$ סימטרי: לכל $x,y\in\mathbb{Z}$, אם $(x,y)\in R$ אז $(y,x)\in R$. "
      r"נניח $(x,y)\in R$, כלומר $2\mid3x+y$. נוכיח $2\mid3y+x$: "
      r"$2\mid4(x+y)=(3x+y)+(3y+x)$, ו-$2\mid3x+y$, ולכן $2\mid3y+x$, כלומר $(y,x)\in R$."
      "\n"
      r"$R$ טרנזיטיבי: לכל $x,y,z\in\mathbb{Z}$, אם $(x,y)\in R$ ו-$(y,z)\in R$ אז $(x,z)\in R$. "
      r"אכן, $2\mid3x+y$ ו-$2\mid3y+z$, ולכן $2\mid(3x+y)+(3y+z)=(3x+z)+4y$, ומכאן $2\mid3x+z$, כלומר $(x,z)\in R$."
      "\n"
      r"מסקנה: $R$ הוא יחס שקילות."
      "\n"
      r"מחלקות השקילות: $[0]=\{x\in\mathbb{Z}:(x,0)\in R\}=\{x\in\mathbb{Z}:(0,x)\in R\}=\{x\in\mathbb{Z}:2\mid3\cdot0+x\}=\{x\in\mathbb{Z}:2\mid x\}=\{2k:\ k\in\mathbb{Z}\}$."
      "\n"
      r"$[1]=\{x\in\mathbb{Z}:(1,x)\in R\}=\{x\in\mathbb{Z}:2\mid3+x\}=\{x\in\mathbb{Z}:x=2k+1,\ k\in\mathbb{Z}\}=\{2k+1:\ k\in\mathbb{Z}\}$ (זה בדיוק האי-זוגיים)."
      "\n"
      r"מסקנה: $\mathbb{Z}/R=\{[0],[1]\}$."
      "\n"
      r"**(2)** $R$ אינו יחס סדר חלקי, כי הוא אינו אנטי-סימטרי. דוגמה נגדית: $1\ne3$ אך $(1,3)\in R$ ו-$(3,1)\in R$, כי $2\mid3\cdot1+3=6$."),

    # ---------------- Q3 ----------------
    Q(3, "א", "computation", "modular_fermat_wilson", 12,
      r"תהי $A$ קבוצת כל המספרים הראשוניים והפונקציה $f:A\to\{0,1\}$ שמוגדרת לפי הכלל הבא: "
      r"$f(p)=\left((\varnothing\circ\varnothing)(p^2)\right)\pmod2$ לכל $p\in A$."
      "\n"
      r"**(1)** חשבו את: $f(2)+f(3)$."
      "\n"
      r"**(2)** מצאו את כל המספרים $p\in A$ המקיימים את התנאי: $f(p)=0$."
      "\n"
      r"**(3)** מצאו את כל המספרים $p\in A$ המקיימים את התנאי: $f(p)=1$."
      "\n"
      r"**(4)** מצאו את הקבוצה $B\subseteq A$ כך ש: $f:B\to\{0,1\}$ היא הפיכה.",
      r"**(1)** $f(2)=(\varnothing\circ\varnothing)(4)\bmod2=\varnothing(\varnothing(4))\bmod2=\varnothing(2)\bmod2=1\bmod2=1$."
      "\n"
      r"$f(3)=(\varnothing\circ\varnothing)(9)\bmod2=\varnothing(\varnothing(9))\bmod2$."
      "\n"
      r"$\varnothing(4)=\varnothing(2^2)=4\left(1-\frac12\right)=2$, "
      r"$\varnothing(9)=\varnothing(3^2)=9\left(1-\frac13\right)=6$, "
      r"$\varnothing(\varnothing(9))=\varnothing(6)=\varnothing(2\cdot3)=\varnothing(2)\varnothing(3)=1\cdot2=2$."
      "\n"
      r"לכן $f(3)=\varnothing(\varnothing(9))\bmod2=2\bmod2=0$, ו-$f(2)+f(3)=1$."
      "\n"
      r"**(2)** $f(2)=1\ne0$. עבור $3\le p\in A$:"
      "\n"
      r"$f(p)=(\varnothing\circ\varnothing)(p^2)=\varnothing(\varnothing(p^2))=\varnothing(p(p-1))=\varnothing(p)\varnothing(p-1)=(p-1)\varnothing(p-1)$ "
      r"(כי $\gcd(p,p-1)=1$)."
      "\n"
      r"$p$ אי-זוגי, ולכן $2\mid p-1$, ומכאן $f(p)=(p-1)\varnothing(p-1)\bmod2=0$."
      "\n"
      r"מסקנה: $f(p)=0$ לכל $3\le p\in A$."
      "\n"
      r"**(3)** לפי (1) ו-(2): $f(2)=1$ ו-$f(p)=0$ לכל $p\in A$, $p\ge3$. לכן $f(p)=1$ רק עבור $p=2$."
      "\n"
      r"**(4)** לפי (2) ו-(3), $B=\{2,3\}$: $f(2)=1$, $f(3)=0$, ולכן $f:\{2,3\}\to\{0,1\}$ היא הפיכה."),

    Q(3, "ב", "computation", "recurrence_sums", 13,
      r"מצאו את הצורה המפורשת של $(a_n)$, כאשר: $a_n=4a_{n-1}-4a_{n-2}+2\cdot3^n$, $a_0=20$, $a_1=54$.",
      r"המשוואה האופיינית: $r^2=4r-4\iff(r-2)^2=0$, ולכן $r_{1,2}=2$."
      "\n"
      r"פתרון הנוסחה ההומוגנית: $a_n^{(h)}=C_1\cdot2^n+C_2\cdot n\cdot2^n$."
      "\n"
      r"פתרון פרטי של הנוסחה הלא הומוגנית: $a_n^{(p)}=A\cdot3^n\cdot n^s$, כאשר $s=0$ כי $3\ne r_{1,2}=2$, ולכן $a_n^{(p)}=A\cdot3^n$."
      "\n"
      r"נציב במשוואה ונחלק ב-$3^{n-2}$:"
      "\n"
      r"$$A\cdot3^n=4A\cdot3^{n-1}-4A\cdot3^{n-2}+2\cdot3^n\ \Rightarrow\ 9A=12A-4A+18\ \Rightarrow\ A=18$$"
      "\n"
      r"הפתרון הכללי: $a_n=a_n^{(h)}+a_n^{(p)}=C_1\cdot2^n+C_2\cdot n\cdot2^n+18\cdot3^n$."
      "\n"
      r"$a_0=C_1+18=20\ \Rightarrow\ C_1=2$"
      "\n"
      r"$a_1=2C_1+2C_2+54=54\ \Rightarrow\ C_2=-C_1=-2$"
      "\n"
      r"מסקנה: $a_n=2\cdot2^n-2n\cdot2^n+18\cdot3^n$, לכל $n\in\mathbb{N}$."),

    # ---------------- Q4 ----------------
    Q(4, "א", "proof", "combinatorics", 5,
      r"חשבו את $f(n)=\sum_{k=0}^{n}\left(\binom{n}{k}\cdot\left(3^{2k}+2^{2k}\right)\right)$ והראו ש: $f(n)=O(10^n)$.",
      r"$f(n)=\sum_{k=0}^{n}\binom nk9^k+\sum_{k=0}^{n}\binom nk4^k=\sum_{k=0}^{n}\binom nk9^k1^{n-k}+\sum_{k=0}^{n}\binom nk4^k1^{n-k}$"
      "\n"
      r"$$=(9+1)^n+(4+1)^n=10^n+5^n$$"
      "\n"
      r"$f(n)=10^n+5^n\le10^n+10^n=2\cdot10^n$ לכל $n\in\mathbb{N}$, $n\ge0$."
      "\n"
      r"לכן, עבור $n_0=0\in\mathbb{N}$ ו-$c_0=2>0$ מתקיים: $f(n)\le c_0\cdot10^n$ לכל $n\in\mathbb{N}$, $n\ge0$."
      "\n"
      r"מסקנה: $f(n)=O(10^n)$."),

    Q(4, "ב", "computation", "combinatorics", 15,
      r"תהי הקבוצה $A=\{a,b,c,d,e,f\}$."
      "\n"
      r"**(1)** מצאו את מספר המילים ב-4 אותיות שניתן ליצור מ-$A$ כך שכל מילה מסתיימת ברצף “ef”;"
      "\n"
      r"**(2)** מצאו את מספר המילים ב-4 אותיות **שונות** שניתן ליצור מ-$A$ ללא חשיבות לסדר האותיות;"
      "\n"
      r"**(3)** מצאו את מספר המילים ב-6 אותיות **שונות** שניתן ליצור מ-$A$ כך שבכל מילה מופיע הרצף “abc” והאות הראשונה היא $a$ או $d$.",
      r"**(1)** כל מילה היא מהצורה: (אות)(אות)$ef$. לכל אחד משני המקומות הראשונים יש 6 אפשרויות: $6\cdot6=36$ מילים."
      "\n"
      r"**(2)** ללא חשיבות לסדר, כל מילה מתאימה לבחירה של 4 אותיות מתוך 6: "
      r"$\binom62=\frac{6\cdot5}{2}=15=\binom64$ (כי $|A|=6$)."
      "\n"
      r"מספר המילים: 15."
      "\n"
      r"**(3)** כל מילה בת 6 אותיות שונות, שבה מופיע הרצף “abc” והאות הראשונה היא $a$ או $d$:"
      "\n"
      r"אם המילה מתחילה ב-$a$: המילה היא “abc” ואחריה האותיות $d,e,f$ בסדר כלשהו: $3!=6$ אפשרויות."
      "\n"
      r"אם המילה מתחילה ב-$d$: אחרי $d$ מסדרים את “abc”, $e$ ו-$f$ (הרצף “abc” כיחידה אחת): $3!=6$ אפשרויות."
      "\n"
      r"לכן יש $12$ מילים מתאימות."),

    Q(4, "ג", "computation", "combinatorics", 5,
      r"תהי הקבוצה $A=\{a,b,c,d\}$."
      "\n"
      r"מצאו כמות המילים באורך 22 אותיות לכל היותר שניתן ליצור מ-$A$, כאשר בכל מילה תופיע:"
      "\n"
      r"האות $a$ לפחות 4 פעמים, האות $b$ לפחות 3 פעמים, האות $c$ לפחות 5 פעמים והאות $d$ לפחות 2 פעמים.",
      r"**הפתרון הרשמי עם תיקון:** הפתרון הרשמי מסתיים ב-$\binom{12}{4}=495$. זה מספר הווקטורים $(x_1,x_2,x_3,x_4)$ של מספר המופעים של כל אות "
      r"(כלומר מילים עד כדי סדר האותיות), ולא מספר המילים. השאלה מבקשת מילים, ולכן יש להוסיף את חשיבות הסדר: לכל וקטור מונים יש מספר מילים השווה למקדם המולטינומי. התוצאה נבדקה בסקריפט."
      "\n"
      r"**שלב רשמי (מספר וקטורי המונים):** נסמן ב-$x_1,x_2,x_3,x_4$ את מספר המופעים של $a,b,c,d$. נדרש: $x_1+x_2+x_3+x_4\le22$, $x_1\ge4$, $x_2\ge3$, $x_3\ge5$, $x_4\ge2$."
      "\n"
      r"נסמן $y_1=x_1-4$, $y_2=x_2-3$, $y_3=x_3-5$, $y_4=x_4-2$. אז $(y_1+4)+(y_2+3)+(y_3+5)+(y_4+2)\le22\iff y_1+y_2+y_3+y_4\le8$, $y_i\ge0$."
      "\n"
      r"נסמן $y_5=8-(y_1+y_2+y_3+y_4)$. נקבל: $y_1+y_2+y_3+y_4+y_5=8$, $y_i\in\mathbb{N}$. מספר הפתרונות: $D(5,8)=\binom{5-1+8}{5-1}=\binom{12}{4}=\frac{12\cdot11\cdot10\cdot9}{2\cdot3\cdot4}=495$."
      "\n"
      r"**התיקון (מספר המילים):** לכל וקטור $(x_1,x_2,x_3,x_4)$ כזה, עם $t=x_1+x_2+x_3+x_4$, יש $\frac{t!}{x_1!\,x_2!\,x_3!\,x_4!}$ מילים באורך $t$. לכן:"
      "\n"
      r"$$\sum_{\substack{x_1\ge4,\ x_2\ge3,\ x_3\ge5,\ x_4\ge2\\ x_1+x_2+x_3+x_4\le22}}\frac{(x_1+x_2+x_3+x_4)!}{x_1!\,x_2!\,x_3!\,x_4!}=10726916243718$$"
      "\n"
      r"מסקנה: מספר המילים הוא $10726916243718$ (ו-495 הוא מספר וקטורי המונים).",
      solutionSource="solved"),
]

exam = {
    "examCode": "18A-B",
    "examLabel": 'בדידה 1, סמסטר א\' תשע"ח, מועד ב (21.03.2018)',
    "year": 2018,
    "examDate": "21.03.2018",
    "sourceFile": "18A-B exam with handwritten solution, pp.1-11",
    "solutionFile": "18A-B handwritten solution (author unknown), pp.3-11",
    "contexts": {},
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
