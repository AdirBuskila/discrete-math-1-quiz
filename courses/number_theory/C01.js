/* number_theory, level 1 - remainders and reducing before computing. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C01", order: 1, icon: "🔢", title: "שאריות וצמצום חזקות",
  goal: "אחרי השלב הזה אפשר לחשב שארית של ביטוי על ידי החלפת כל איבר בשארית שלו, כולל מספרים שליליים וחזקות עם מחזור.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>$a\equiv b\pmod n$ אומר ש-$n\mid(a-b)$, כלומר ל-$a$ ול-$b$ אותה שארית בחלוקה ב-$n$. השארית היא מספר בין $0$ ל-$n-1$.</p>
    <div class="lesson-rule">🔑 שקילות שומרת על חיבור וכפל: אם $a\equiv a'$ ו-$b\equiv b'$ אז $a+b\equiv a'+b'$ וגם $a\cdot b\equiv a'\cdot b'$. לכן אפשר <b>להחליף כל איבר בשארית שלו לפני שמחשבים</b>, ובסוף להוריד שוב.</div>
    <div class="lesson-ex">$(26\cdot 31+4)\bmod 5$: $26\equiv1$, $31\equiv1$, ולכן $26\cdot31+4\equiv1\cdot1+4=5\equiv0$.</div>
    <h3>שליליים</h3>
    <p>$-3\equiv n-3\pmod n$. למשל $-3\equiv 4\pmod 7$, כי $7\mid(-3-4)=-7$.</p>
    <h3>חזקות: מחפשים מחזור</h3>
    <p>מחשבים את $a^1,a^2,a^3,\dots$ מודולו $n$ ועוצרים כשחוזרים ל-$1$. מרגע זה הכול חוזר על עצמו, ולכן מצמצמים את המעריך לפי אורך המחזור.</p>
    <div class="lesson-ex">$3^k\bmod 10$ הוא $3,9,7,1,3,9,7,1,\dots$ במחזור של אורך $4$. כי $27\equiv7$ ו-$21\equiv1$. לכן $3^{50}$: $50=4\cdot12+2$, ושארית המעריך היא $2$, ולכן $3^{50}\equiv3^2=9\pmod{10}$.</div>
    <div class="lesson-trap">⚠️ הדרך הזאת עובדת רק כשהמחזור חוזר ל-$1$. אם הבסיס מתחלק ב-$n$ או שיש לו גורם משותף עם $n$, אפשר להגיע ל-$0$ או למחזור שלא מתחיל ב-$a^0$.</div>` },
  questions: [
    { id: "C01-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $123$ בחלוקה ב-$7$?`,
        answer: 4, tol: 0,
        explain: String.raw`$123=17\cdot7+4$, כלומר $119=17\cdot7$ ונשארות $4$.` },
      recap: String.raw`שארית: מחסירים את הכפולה הגדולה ביותר של $n$ שאינה עוברת את המספר.` },
    { id: "C01-Q2",
      question: String.raw`איזה מהמספרים שקול ל-$3$ מודולו $8$?`,
      options: [
        { id: "a", value: "$35$" },
        { id: "b", value: "$29$" },
        { id: "c", value: "$41$" },
        { id: "d", value: "$18$" },
      ],
      correctId: "a",
      explanation: String.raw`$35=4\cdot8+3$, ולכן $8\mid(35-3)=32$. אבל $29=3\cdot8+5$ נותן שארית $5$, ב-$41=5\cdot8+1$ השארית $1$, וב-$18=2\cdot8+2$ השארית $2$.`,
      recap: String.raw`$a\equiv b\pmod n$ כש-$n\mid(a-b)$.` },
    { id: "C01-Q3",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $17\cdot23+8$ בחלוקה ב-$5$? (אפשר להחליף כל גורם בשארית שלו.)`,
        answer: 4, tol: 0,
        explain: String.raw`$17\equiv2$ ו-$23\equiv3$, ולכן $17\cdot23+8\equiv2\cdot3+8=14\equiv4\pmod5$. בדיקה ישירה: $17\cdot23+8=399=79\cdot5+4$.` },
      recap: "מחליפים כל איבר בשארית שלו ורק אז מחשבים." },
    { id: "C01-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $-17$ בחלוקה ב-$5$? (השארית היא מספר בין $0$ ל-$4$.)`,
        answer: 3, tol: 0,
        explain: String.raw`$-17=-20+3$, והמספר $-20$ מתחלק ב-$5$. לכן $-17\equiv3\pmod5$. השארית $-2$ אינה בטווח $0..4$.` },
      recap: String.raw`שארית של שלילי: מוסיפים כפולה של $n$ עד שנכנסים לטווח $0..n-1$.` },
    { id: "C01-Q5",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $7^{100}$ בחלוקה ב-$10$?`,
        answer: 1, tol: 0,
        explain: String.raw`החזקות של $7$ מודולו $10$ הן $7,9,3,1$ ואז חוזרות (מחזור באורך $4$). מכיוון ש-$100=4\cdot25$, מקבלים $7^{100}=(7^4)^{25}\equiv1^{25}=1$.` },
      recap: "מוצאים את המחזור של החזקות ומצמצמים את המעריך לפי אורכו." },
  ],
});
