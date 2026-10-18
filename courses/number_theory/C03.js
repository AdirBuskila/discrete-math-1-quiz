/* number_theory, level 3 - reducing the exponent mod p-1. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C03", order: 3, icon: "📉", title: "צמצום מעריך מודולו p-1",
  goal: "אחרי השלב הזה אפשר לחשב שארית של חזקה גדולה מודולו ראשוני, וגם סכום של כמה חזקות.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>אם $p$ ראשוני ו-$p\nmid m$, אז $m^{p-1}\equiv1$. לכן אפשר לכתוב את המעריך כ-$e=q(p-1)+r$ ולקבל</p>
    <div class="lesson-formula">$m^{e}=(m^{p-1})^{q}\cdot m^{r}\equiv m^{r}\pmod p$, כאשר $r=e\bmod(p-1)$.</div>
    <div class="lesson-ex">$2^{100}\bmod7$: $p-1=6$ ו-$100=16\cdot6+4$, ולכן $2^{100}\equiv2^4=16\equiv2\pmod7$.</div>
    <div class="lesson-rule">🔑 סדר הפעולות: (1) מורידים את הבסיס מודולו $p$, (2) מצמצמים את המעריך מודולו $p-1$, (3) מחשבים את החזקה הקטנה.</div>
    <div class="lesson-trap">⚠️ המעריך מצטמצם מודולו $p-1$ ולא מודולו $p$. והבסיס מצטמצם מודולו $p$.</div>
    <h3>בסיס שלילי ובסיס שנהיה קטן</h3>
    <p>$38\equiv12\equiv-1\pmod{13}$, ולכן $38^{25}\equiv(-1)^{25}=-1\equiv12\pmod{13}$. בסיס $\pm1$ הוא הקל ביותר.</p>
    <h3>סכום חזקות</h3>
    <p>מחשבים כל חזקה בנפרד ומחברים את השאריות. הדרך שימושית גם כשהבסיס הוא חזקה בעצמו, כמו $16=4^2$.</p>` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`כדי לחשב את $2^{100}\bmod7$ מצמצמים את המעריך $100$ מודולו $p-1=6$. מהו המעריך המצומצם?`,
        answer: 4, tol: 0,
        explain: String.raw`$100=16\cdot6+4$, ולכן המעריך המצומצם הוא $4$.` },
      recap: String.raw`המעריך מצטמצם מודולו $p-1$.` },
    { id: "C03-Q2",
      question: String.raw`מחשבים $5^{100}\bmod7$. מודולו איזה מספר מצמצמים את המעריך $100$?`,
      options: [
        { id: "a", value: "$6$" },
        { id: "b", value: "$7$" },
        { id: "c", value: "$5$" },
        { id: "d", value: "$100$" },
      ],
      correctId: "a",
      explanation: String.raw`פרמה אומר $5^{6}\equiv1\pmod7$, ולכן המעריך חוזר כל $6$. מודולו $7$ מצמצמים רק את הבסיס, לא את המעריך. מודולו $5$ אין סיבה. ו-$100$ הוא המעריך עצמו.`,
      recap: String.raw`מעריך: מודולו $p-1$. בסיס: מודולו $p$.` },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $5^{100}$ בחלוקה ב-$7$?`,
        answer: 2, tol: 0,
        explain: String.raw`$100\equiv4\pmod6$, ולכן $5^{100}\equiv5^4=625$. מכיוון ש-$625=89\cdot7+2$, השארית היא $2$.` },
      recap: "מצמצמים את המעריך ואז מחשבים חזקה קטנה." },
    { id: "C03-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $2^{100}$ בחלוקה ב-$13$?`,
        answer: 3, tol: 0,
        explain: String.raw`$p-1=12$ ו-$100=8\cdot12+4$, ולכן $2^{100}\equiv2^4=16\equiv3\pmod{13}$.` },
      recap: String.raw`$e\bmod(p-1)$ ואז חזקה קטנה.` },
    { id: "C03-Q5",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $38^{25}$ בחלוקה ב-$13$?`,
        answer: 12, tol: 0,
        explain: String.raw`$38=3\cdot13-1\equiv-1\pmod{13}$, ולכן $38^{25}\equiv(-1)^{25}=-1\equiv12\pmod{13}$.` },
      recap: String.raw`בסיס שקול ל-$-1$ נותן $\pm1$ לפי זוגיות המעריך.` },
    { id: "C03-Q6",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $16^{15}+7^{60}+37$ בחלוקה ב-$31$? (רמז: $16=4^2$ ו-$7^2=49$.)`,
        answer: 8, tol: 0,
        explain: String.raw`$16^{15}=4^{30}\equiv1$ לפי פרמה ($31$ ראשוני ו-$31\nmid4$). $7^{60}=49^{30}\equiv1$ כי $31\nmid49$. לכן הסכום $\equiv1+1+37=39\equiv8\pmod{31}$.` },
      recap: "כל חזקה מצטמצמת בנפרד, ובסוף מחברים ומורידים." },
  ],
});
