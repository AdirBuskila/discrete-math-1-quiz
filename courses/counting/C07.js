/* counting, level 7 - stars and bars, and the vectors-versus-words trap. ai-verified (tools/verify/needhelp/counting/check.py) */
COURSE_LEVEL("counting", {
  id: "C07", order: 7, icon: "⭐", title: "כוכבים וקווים: פתרונות של משוואה",
  goal: "אחרי השלב הזה אפשר לספור פתרונות שלמים של משוואה עם חסמים, ולהבדיל בין מילים עד כדי סדר לבין מילים רגילות.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>שאלה טיפוסית: כמה דרכים לחלק $n$ פריטים זהים ל-$r$ תאים?</p>
    <div class="lesson-rule">🔑 <b>כוכבים וקווים:</b> מספר הפתרונות השלמים הלא-שליליים של $x_1+\dots+x_r=n$ הוא $\binom{n+r-1}{r-1}$.</div>
    <div class="lesson-rule">🔑 <b>חסמים תחתונים:</b> אם $x_i\ge l_i$, מציבים $y_i=x_i-l_i\ge0$, וזה מקטין את הסכום ב-$\sum l_i$. "יותר מ-4" פירושו $x\ge5$. <b>אי-שוויון</b> $x_1+\dots+x_r\le n$: מוסיפים משתנה עודף $x_{r+1}\ge0$, ומקבלים משוואה עם $r+1$ משתנים.</div>
    <div class="lesson-rule">🔑 <b>מילים:</b> כוכבים וקווים סופר <i>וקטורי מונים</i> $(x_1,\dots,x_r)$ (כמה פעמים כל אות), כלומר מילים "בלי חשיבות לסדר האותיות". אם הסדר חשוב, לכל וקטור יש $\frac{n!}{x_1!\cdots x_r!}$ מילים.</div>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">כמה פתרונות ל-$x_1+x_2+x_3=8$ עם $x_1\ge2$ ו-$x_2,x_3\ge0$? מציבים $y_1=x_1-2$: $y_1+x_2+x_3=6$, ולכן $\binom{6+3-1}{2}=\binom82=28$.<br>
    מילים באורך 3 מ-$\{a,b\}$, בלי חשיבות לסדר: וקטורים $x_a+x_b=3$, כלומר $\binom41=4$. מילים רגילות: $2^3=8$.</div>
    <div class="lesson-trap">⚠️ קוראים היטב: "מילים" או "בלי חשיבות לסדר"? ובחסם "פחות מ" או "לכל היותר"? ($x<5$ זה $x\le4$.)</div>` },
  questions: [
    { id: "C07-Q1",
      step: { type: "numeric",
        prompt: String.raw`כמה פתרונות שלמים לא-שליליים יש למשוואה $x_1+x_2+x_3=10$?`,
        answer: 66, tol: 0,
        explain: String.raw`$\binom{10+3-1}{3-1}=\binom{12}{2}=66$.` },
      recap: String.raw`$\binom{n+r-1}{r-1}$.` },
    { id: "C07-Q2",
      step: { type: "numeric",
        prompt: String.raw`כמה פתרונות שלמים יש ל-$x_1+x_2+x_3+x_4=14$ כאשר כל $x_i\ge1$?`,
        answer: 286, tol: 0,
        explain: String.raw`מציבים $y_i=x_i-1\ge0$: $y_1+\dots+y_4=14-4=10$. מספר הפתרונות: $\binom{10+4-1}{3}=\binom{13}{3}=286$.` },
      recap: "כל $x_i\\ge l_i$: מורידים $\\sum l_i$ מהסכום." },
    { id: "C07-Q3",
      step: { type: "numeric",
        prompt: String.raw`כמה פתרונות שלמים יש ל-$x_1+x_2+x_3=14$ כאשר $x_1\ge2$, $x_2\ge3$, $x_3\ge4$?`,
        answer: 21, tol: 0,
        explain: String.raw`סכום החסמים $2+3+4=9$, לכן הסכום החדש הוא $14-9=5$. מספר הפתרונות: $\binom{5+3-1}{2}=\binom72=21$.` },
      recap: "החסמים מקטינים את $n$ בסכומם." },
    { id: "C07-Q4",
      step: { type: "numeric",
        prompt: String.raw`כמה פתרונות שלמים לא-שליליים יש לאי-שוויון $x_1+x_2+x_3\le6$?`,
        answer: 84, tol: 0,
        explain: String.raw`מוסיפים משתנה עודף $x_4=6-(x_1+x_2+x_3)\ge0$ וכך $x_1+x_2+x_3+x_4=6$. מספר הפתרונות: $\binom{6+4-1}{3}=\binom93=84$.` },
      recap: String.raw`"$\le$": משתנה עודף, ו-$r$ גדל באחד.` },
    { id: "C07-Q5",
      step: { type: "numeric",
        prompt: String.raw`כמה מילים באורך 4 מהאותיות $\{a,b,c\}$ מכילות את $a$ פעמיים, את $b$ פעם אחת ואת $c$ פעם אחת?`,
        answer: 12, tol: 0,
        explain: String.raw`יש וקטור מונים אחד, $(2,1,1)$, ולו $\frac{4!}{2!\,1!\,1!}=12$ מילים (סידורים של האותיות).` },
      recap: String.raw`מילים עם מונים נתונים: $\frac{n!}{x_1!\cdots x_r!}$.` },
    { id: "C07-Q6",
      question: String.raw`כמה מילים באורך 5 מהאותיות $\{a,b\}$ יש, אם אין חשיבות לסדר האותיות במילה?`,
      options: [
        { id: "a", value: String.raw`$6$` },
        { id: "b", value: String.raw`$32$` },
        { id: "c", value: String.raw`$10$` },
        { id: "d", value: String.raw`$5$` },
      ],
      correctId: "a",
      explanation: String.raw`בלי חשיבות לסדר, מילה נקבעת רק על ידי מספר ה-$a$ (מ-0 עד 5): $x_a+x_b=5$ יש $\binom{6}{1}=6$ פתרונות. $32=2^5$ סופר מילים רגילות, כשהסדר חשוב. $10=\binom52$ בוחר מקומות ל-$a$ כשהסדר חשוב. ו-$5$ שוכח את המקרה $x_a=0$.`,
      recap: "בלי חשיבות לסדר = וקטורי מונים = כוכבים וקווים." },
  ],
});
