/* number_theory, level 4 - "p divides X^e - 1" with Fermat. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C04", order: 4, icon: "🧩", title: "הראו ש-p מחלק חזקה פחות 1",
  goal: String.raw`אחרי השלב הזה אפשר להוכיח ש-$p\mid X^e-1$: לבחור את $p$, לכתוב את החזקה כ-$(X^k)^{p-1}$ ולהפעיל פרמה.`,
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>השאלה הקלאסית: "הראו שהראשוני $p$ מחלק את $X^{e}-1$". המתכון:</p>
    <ul>
      <li>בודקים ש-$p-1$ מחלק את $e$, ומחשבים $k=e/(p-1)$.</li>
      <li>כותבים $X^{e}=(X^{k})^{p-1}$.</li>
      <li>בודקים ש-$p\nmid X^{k}$ (בדרך כלל כי $p\nmid X$).</li>
      <li>לפי פרמה $(X^{k})^{p-1}\equiv1$, ולכן $p\mid X^{e}-1$.</li>
    </ul>
    <div class="lesson-ex">$7\mid5^{18}-1$: כאן $p-1=6$ ו-$18=3\cdot6$, לכן $5^{18}=(5^{3})^{6}=125^{6}$. מכיוון ש-$7\nmid125$ (כי $125=17\cdot7+6$), לפי פרמה $125^{6}\equiv1\pmod7$, ולכן $7\mid5^{18}-1$.</div>
    <div class="lesson-trap">⚠️ אם $p\mid X$ הטענה שקרית: $X^{e}\equiv0$ ולכן $X^e-1\equiv-1$. למשל $5\mid10^{8}-1$ אינו נכון, כי $10^{8}\equiv0\pmod5$.</div>
    <p>המעריך חייב להיות כפולה של $p-1$. אם הוא לא, אי אפשר לכתוב את החזקה בצורה הזאת ולכן צריך להסתכל על ראשוני אחר.</p>` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`רוצים להראות ש-$13\mid3^{36}-1$ ולכתוב $3^{36}=(3^{k})^{12}$. מהו $k$?`,
        answer: 3, tol: 0,
        explain: String.raw`$p-1=12$, ו-$36=3\cdot12$. לכן $3^{36}=(3^{3})^{12}=27^{12}$, ו-$13\nmid27$, ולכן פרמה חל.` },
      recap: String.raw`$k=e/(p-1)$.` },
    { id: "C04-Q2",
      question: String.raw`איזה מהמספרים מתחלק ב-$11$?`,
      options: [
        { id: "a", value: "$2^{20}-1$" },
        { id: "b", value: "$2^{15}-1$" },
        { id: "c", value: "$2^{25}-1$" },
        { id: "d", value: "$5^{14}-1$" },
      ],
      correctId: "a",
      explanation: String.raw`$20=2\cdot10$ וגם $11\nmid4$, ולכן $2^{20}=4^{10}\equiv1\pmod{11}$ לפי פרמה. באחרים המעריך אינו כפולה של $10$, ובפועל $2^{15}-1\equiv-2$, $2^{25}-1\equiv9$ ו-$5^{14}-1\equiv8$ מודולו $11$.`,
      recap: String.raw`המעריך חייב להיות כפולה של $p-1$.` },
    { id: "C04-Q3",
      question: String.raw`מדוע אי אפשר להסיק מפרמה ש-$5\mid10^{8}-1$?`,
      options: [
        { id: "a", value: String.raw`כי $5\mid10$, ולכן $10^{8}\equiv0$ ו-$10^{8}-1\equiv4$` },
        { id: "b", value: "כי $5$ אינו ראשוני" },
        { id: "c", value: String.raw`כי $8$ אינו כפולה של $5$` },
        { id: "d", value: String.raw`כי $10^{8}-1$ הוא מספר אי-זוגי` },
      ],
      correctId: "a",
      explanation: String.raw`פרמה דורש $p\nmid X$, ו-$5\mid10$. אז $10^{8}\equiv0\pmod5$ והמספר $10^8-1$ נותן שארית $4$, כלומר אינו מתחלק ב-$5$. $5$ כן ראשוני. המעריך צריך להיות כפולה של $p-1=4$, ו-$8$ הוא כזה, לא של $5$. ואי-זוגיות אינה קשורה.`,
      recap: String.raw`בודקים תמיד $p\nmid$ בסיס.` },
    { id: "C04-Q4",
      step: { type: "order",
        prompt: String.raw`סדרו הוכחה ש-$7\mid5^{18}-1$.`,
        lines: [
          String.raw`$p-1=6$ ו-$18=3\cdot6$, ולכן $5^{18}=(5^{3})^{6}=125^{6}$.`,
          String.raw`$7$ ראשוני ו-$7\nmid125$ (כי $125=17\cdot7+6$), ולכן לפי פרמה $125^{6}\equiv1\pmod7$.`,
          String.raw`לכן $5^{18}-1\equiv0\pmod7$, כלומר $7\mid5^{18}-1$.`,
        ],
        explain: String.raw`קודם כותבים את החזקה בצורה $(X^k)^{p-1}$, אחר כך בודקים את תנאי פרמה, מפעילים אותו ומסיקים.` },
      recap: String.raw`כותבים $(X^{k})^{p-1}$, בודקים $p\nmid X^k$, מפעילים פרמה.` },
    { id: "C04-Q5",
      step: { type: "findbug",
        prompt: String.raw`בהוכחה ש-$13\mid8^{24}-1$ נשתלה טעות בשורה אחת. איזו?`,
        lines: [
          String.raw`$13$ ראשוני ו-$8^{24}=(8^{2})^{12}=64^{12}$.`,
          String.raw`$13\nmid64$, כי $64=4\cdot13+12$.`,
          String.raw`לפי פרמה $64^{13}\equiv1\pmod{13}$.`,
          String.raw`לכן $64^{12}-1\equiv0$, כלומר $13\mid8^{24}-1$.`,
        ],
        bugIndex: 2,
        explain: String.raw`פרמה נותן $64^{p-1}=64^{12}\equiv1$, לא $64^{p}$. בפועל $64^{13}\equiv64\equiv12\pmod{13}$.` },
      recap: String.raw`פרמה: המעריך הוא $p-1$.` },
  ],
});
