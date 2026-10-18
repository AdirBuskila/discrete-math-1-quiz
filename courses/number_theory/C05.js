/* number_theory, level 5 - Wilson's theorem and factorials. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C05", order: 5, icon: "❗", title: "משפט וילסון ועצרת",
  goal: "אחרי השלב הזה אפשר להשתמש בוילסון כדי לחשב שארית של עצרת, ולדעת איזה ראשוני מחלק עצרת.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <div class="lesson-formula">אם $p$ ראשוני אז $(p-1)!\equiv-1\pmod p$, כלומר $p\mid(p-1)!+1$.</div>
    <div class="lesson-ex">$p=7$: $6!=720=102\cdot7+6\equiv-1$, ולכן $7\mid6!+1=721=7\cdot103$.</div>
    <div class="lesson-trap">⚠️ וילסון הוא על $(p-1)!$ ולא על $p!$. מכיוון ש-$p$ הוא אחד הגורמים של $p!$, מתקבל $p!\equiv0\pmod p$.</div>
    <h3>מי מחלק עצרת</h3>
    <p>אם $m\le n$ אז $m\mid n!$ (כי $m$ הוא אחד הגורמים של המכפלה $1\cdot2\cdots n$). לכן $41\mid42!$ אבל $41\nmid40!$: ראשוני $p$ מחלק את $n!$ בדיוק כש-$p\le n$.</p>
    <div class="lesson-rule">🔑 כדי לחשב $(p-1)!+c$ מודולו $p$, מציבים $(p-1)!\equiv-1$ ומקבלים $c-1$. הביטוי מתחלק ב-$p$ בדיוק כש-$p\mid c-1$.</div>
    <p>הכתיבה הרגילה בהוכחה היא פירוק: $(p-1)!+c=\big((p-1)!+1\big)+(c-1)$, ואז לוילסון יש תפקיד בסוגריים הראשונים.</p>` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $10!$ בחלוקה ב-$11$? (השארית היא מספר בין $0$ ל-$10$.)`,
        answer: 10, tol: 0,
        explain: String.raw`$11$ ראשוני, ולכן לפי וילסון $10!\equiv-1\equiv10\pmod{11}$.` },
      recap: String.raw`$(p-1)!\equiv-1\equiv p-1$.` },
    { id: "C05-Q2",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $12!$ בחלוקה ב-$13$?`,
        answer: 12, tol: 0,
        explain: String.raw`$13$ ראשוני, ולכן $12!=(13-1)!\equiv-1\equiv12\pmod{13}$.` },
      recap: "מזהים ש-12 הוא p-1 ומפעילים וילסון." },
    { id: "C05-Q3",
      question: String.raw`איזה מהמספרים מתחלק ב-$11$?`,
      options: [
        { id: "a", value: "$10!+1$" },
        { id: "b", value: "$11!+1$" },
        { id: "c", value: "$10!-1$" },
        { id: "d", value: "$9!+1$" },
      ],
      correctId: "a",
      explanation: String.raw`$10!=(11-1)!\equiv-1$, ולכן $10!+1\equiv0$. אבל $11!\equiv0$ ולכן $11!+1\equiv1$. $10!-1\equiv-2\equiv9$. ו-$9!\equiv1\pmod{11}$ (כי $10\cdot9!\equiv-1$ ו-$10\equiv-1$), ולכן $9!+1\equiv2$.`,
      recap: String.raw`רק $(p-1)!+1$ מתחלק ב-$p$.` },
    { id: "C05-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $12!+20$ בחלוקה ב-$13$?`,
        answer: 6, tol: 0,
        explain: String.raw`$12!\equiv-1\pmod{13}$, ולכן $12!+20\equiv-1+20=19\equiv6$.` },
      recap: String.raw`$(p-1)!+c\equiv c-1\pmod p$.` },
    { id: "C05-Q5",
      question: String.raw`איזה מהמספרים הראשוניים מחלק את $30!$?`,
      options: [
        { id: "a", value: "$29$" },
        { id: "b", value: "$31$" },
        { id: "c", value: "$37$" },
        { id: "d", value: "$41$" },
      ],
      correctId: "a",
      explanation: String.raw`$29\le30$ הוא אחד הגורמים של $30!$. הראשוניים $31$, $37$ ו-$41$ גדולים מ-$30$, ולכן אינם גורמים של המכפלה $1\cdot2\cdots30$ ואינם מחלקים אותה (ראשוני מחלק מכפלה רק אם הוא מחלק אחד הגורמים).`,
      recap: String.raw`ראשוני $p$ מחלק את $n!$ בדיוק כש-$p\le n$.` },
    { id: "C05-Q6",
      step: { type: "findbug",
        prompt: String.raw`בהוכחה ש-$17\mid16!+18$ נשתלה טעות בשורה אחת. איזו?`,
        lines: [
          String.raw`$17$ ראשוני, ולכן לפי וילסון $17\mid17!+1$.`,
          String.raw`$16!+18=(16!+1)+17$.`,
          String.raw`$17\mid17$.`,
          String.raw`סכום של שני מספרים שמתחלקים ב-$17$ מתחלק ב-$17$, ולכן $17\mid16!+18$.`,
        ],
        bugIndex: 0,
        explain: String.raw`וילסון הוא על $(p-1)!=16!$ ולא על $17!$. בפועל $17!\equiv0$, ולכן $17!+1\equiv1$ ואינו מתחלק ב-$17$. השורה הנכונה: $17\mid16!+1$.` },
      recap: String.raw`וילסון: $p\mid(p-1)!+1$.` },
  ],
});
