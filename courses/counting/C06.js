/* counting, level 6 - inclusion-exclusion. ai-verified (tools/verify/needhelp/counting/check.py) */
COURSE_LEVEL("counting", {
  id: "C06", order: 6, icon: "⭕", title: "הכלה והדחה",
  goal: "אחרי השלב הזה אפשר לספור איחוד של קבוצות חופפות, ומספרים שאינם מתחלקים בכמה מספרים.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>כשמקרים יכולים לחפוף, החיבור הפשוט סופר פעמיים את החיתוך, וצריך לתקן.</p>
    <div class="lesson-rule">🔑 <b>שתי קבוצות:</b> $|A\cup B|=|A|+|B|-|A\cap B|$.<br>
    <b>שלוש קבוצות:</b> $|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$. הסימנים מתחלפים: מוסיפים יחידות, מחסרים זוגות, מוסיפים שלשה.</div>
    <div class="lesson-rule">🔑 <b>מתחלקים:</b> מספר השלמים ב-$\{1,\dots,N\}$ המתחלקים ב-$d$ הוא $\lfloor N/d\rfloor$. מתחלק ב-$d_1$ <i>וגם</i> ב-$d_2$ פירושו מתחלק ב-$\operatorname{lcm}(d_1,d_2)$ (שימו לב: לא ב-$d_1d_2$ אם יש להם גורם משותף).</div>
    <p><b>מתכון ל"לא מתחלק באף אחד":</b> מגדירים $A_i$ לפי מי שמתחלק ב-$d_i$, סופרים את האיחוד בהכלה והדחה, ומחסרים מ-$N$.</p>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">כמה מספרים מ-$\{1,\dots,30\}$ מתחלקים ב-2 או ב-3? $|A_2|=15$, $|A_3|=10$, $|A_2\cap A_3|=\lfloor30/6\rfloor=5$. האיחוד: $15+10-5=20$. ולכן $10$ מספרים אינם מתחלקים באף אחד מהם.</div>
    <div class="lesson-trap">⚠️ בחיתוך משלוש קבוצות מחשבים את ה-$\operatorname{lcm}$ של שלושתן (אם הוא גדול מ-$N$, החיתוך ריק). ואל תשכחו שהשלשה נכנסת בסימן <b>חיובי</b>.</div>` },
  questions: [
    { id: "C06-Q1",
      step: { type: "numeric",
        prompt: String.raw`כמה מספרים מ-$\{1,2,\dots,100\}$ מתחלקים ב-4 או ב-6?`,
        answer: 33, tol: 0,
        explain: String.raw`$|A_4|=25$, $|A_6|=16$. מתחלק בשניהם: מתחלק ב-$\operatorname{lcm}(4,6)=12$, כלומר $\lfloor100/12\rfloor=8$ (לא $24$ כמכפלה). האיחוד: $25+16-8=33$.` },
      recap: "חיתוך = lcm, לא מכפלה." },
    { id: "C06-Q2",
      step: { type: "numeric",
        prompt: String.raw`כמה מספרים מ-$\{1,2,\dots,90\}$ אינם מתחלקים באף אחד מהמספרים 2, 3 ו-5?`,
        answer: 24, tol: 0,
        explain: String.raw`$|A_2|=45$, $|A_3|=30$, $|A_5|=18$. זוגות: $|A_2\cap A_3|=15$, $|A_2\cap A_5|=9$, $|A_3\cap A_5|=6$. שלשה: $\lfloor90/30\rfloor=3$. האיחוד: $93-30+3=66$. הלא-מתחלקים: $90-66=24$.` },
      recap: "לא מתחלק באף אחד: $N$ פחות האיחוד." },
    { id: "C06-Q3",
      question: String.raw`כמה מספרים מ-$\{1,2,\dots,200\}$ מתחלקים ב-6 אך אינם מתחלקים ב-4?`,
      options: [
        { id: "a", value: String.raw`$17$` },
        { id: "b", value: String.raw`$33$` },
        { id: "c", value: String.raw`$16$` },
        { id: "d", value: String.raw`$50$` },
      ],
      correctId: "a",
      explanation: String.raw`מתחלקים ב-6: $\lfloor200/6\rfloor=33$. מתוכם מתחלקים גם ב-4, כלומר ב-$\operatorname{lcm}(4,6)=12$: $\lfloor200/12\rfloor=16$. נשארים $33-16=17$. התשובה $33$ שוכחת להוריד. $16$ הוא מספר אלה שכן מתחלקים ב-4. ו-$50$ הוא מספר המתחלקים ב-4 בלבד.`,
      recap: "A אך לא B: $|A|-|A\\cap B|$." },
    { id: "C06-Q4",
      step: { type: "numeric",
        prompt: String.raw`כמה מילים באורך 4 מהאותיות $\{a,b,c\}$ מכילות גם את $a$ וגם את $b$ (לפחות פעם כל אחת)?`,
        answer: 50, tol: 0,
        explain: String.raw`סופרים משלים בהכלה והדחה. הכול: $3^4=81$. בלי $a$: $2^4=16$. בלי $b$: $16$. בלי $a$ וגם בלי $b$ (רק $c$): $1$. מילים שחסר בהן $a$ או $b$: $16+16-1=31$. לכן $81-31=50$.` },
      recap: "משלים + הכלה והדחה על התנאים החסרים." },
    { id: "C06-Q5",
      step: { type: "numeric",
        prompt: String.raw`נתון $|A|=30$, $|B|=25$, $|C|=20$, $|A\cap B|=10$, $|A\cap C|=8$, $|B\cap C|=5$, $|A\cap B\cap C|=3$. כמה איברים ב-$A\cup B\cup C$?`,
        answer: 55, tol: 0,
        explain: String.raw`$30+25+20-10-8-5+3=55$. הסימן של השלשה חיובי.` },
      recap: "יחידות פלוס, זוגות מינוס, שלשה פלוס." },
  ],
});
