/* number_theory, level 2 - Fermat's little theorem. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C02", order: 2, icon: "🔁", title: "משפט פרמה הקטן",
  goal: "אחרי השלב הזה אפשר להפעיל את משפט פרמה: לדעת מתי מותר להשתמש בו ומה מתקבל.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <div class="lesson-formula">אם $p$ ראשוני ו-$p\nmid m$, אז $m^{p-1}\equiv1\pmod p$.</div>
    <p>במילים אחרות, $p\mid m^{p-1}-1$. שני התנאים חשובים: $p$ חייב להיות <b>ראשוני</b>, ו-$m$ <b>לא מתחלק</b> ב-$p$.</p>
    <div class="lesson-ex">$p=7$ ו-$m=3$: $3^6=729=104\cdot7+1$, ולכן $3^6\equiv1\pmod7$. אותו דבר ב-$p=11$ ו-$m=2$: $2^{10}=1024=93\cdot11+1$.</div>
    <div class="lesson-trap">⚠️ אם $p\mid m$ אז $m\equiv0$, ולכן גם $m^{p-1}\equiv0$ ולא $1$. למשל $22^{10}\equiv0\pmod{11}$.</div>
    <h3>שימוש במעריך שאינו $p-1$</h3>
    <p>פרמה נותן את המעריך $p-1$ בדיוק. כדי להשתמש בו כותבים את החזקה כחזקה של חזקה, כמו $2^{12}=(2^6)^2\equiv1^2=1\pmod7$.</p>` },
  questions: [
    { id: "C02-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $5^{12}$ בחלוקה ב-$13$?`,
        answer: 1, tol: 0,
        explain: String.raw`$13$ ראשוני ו-$13\nmid5$, ולכן $5^{13-1}\equiv1\pmod{13}$.` },
      recap: String.raw`$p\nmid m\Rightarrow m^{p-1}\equiv1\pmod p$.` },
    { id: "C02-Q2",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $4^{30}$ בחלוקה ב-$31$?`,
        answer: 1, tol: 0,
        explain: String.raw`$31$ ראשוני ו-$31\nmid4$, והמעריך הוא $31-1=30$. לכן $4^{30}\equiv1\pmod{31}$.` },
      recap: "מזהים את המעריך $p-1$ ומחליפים את החזקה ב-1." },
    { id: "C02-Q3",
      question: String.raw`עבור איזה מהמספרים $m$ אי אפשר להשתמש במשפט פרמה כדי להסיק $m^{10}\equiv1\pmod{11}$?`,
      options: [
        { id: "a", value: "$m=22$" },
        { id: "b", value: "$m=10$" },
        { id: "c", value: "$m=3$" },
        { id: "d", value: "$m=12$" },
      ],
      correctId: "a",
      explanation: String.raw`$22=2\cdot11$ מתחלק ב-$11$, ולכן $22^{10}\equiv0$ ולא $1$. כל האחרים אינם כפולות של $11$ ($10$, $3$ ו-$12$), ולכן פרמה חל עליהם.`,
      recap: String.raw`פרמה דורש $p\nmid m$.` },
    { id: "C02-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $22^{10}$ בחלוקה ב-$11$?`,
        answer: 0, tol: 0,
        explain: String.raw`$22\equiv0\pmod{11}$, ולכן $22^{10}\equiv0$. פרמה אינו חל כי $11\mid22$.` },
      recap: String.raw`כש-$p\mid m$ החזקה $\equiv0$.` },
    { id: "C02-Q5",
      step: { type: "order",
        prompt: String.raw`סדרו הוכחה ש-$7\mid2^{12}-1$.`,
        lines: [
          String.raw`$7$ ראשוני ו-$7\nmid2$, ולכן לפי פרמה $2^{6}\equiv1\pmod7$.`,
          String.raw`$2^{12}=(2^{6})^{2}\equiv1^{2}=1\pmod7$.`,
          String.raw`לכן $2^{12}-1\equiv0\pmod7$, כלומר $7\mid2^{12}-1$.`,
        ],
        explain: "קודם המשפט, אחר כך מפעילים אותו על החזקה הגדולה, ובסוף מסיקים את המחלק." },
      recap: String.raw`מפרקים חזקה גדולה ל-$(m^{p-1})^k$.` },
  ],
});
