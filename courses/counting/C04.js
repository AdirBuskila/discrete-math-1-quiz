/* counting, level 4 - functions, relations and strictly monotone functions. ai-verified (tools/verify/needhelp/counting/check.py) */
COURSE_LEVEL("counting", {
  id: "C04", order: 4, icon: "🗺️", title: "פונקציות, יחסים וסדרות עולות",
  goal: "אחרי השלב הזה אפשר לספור פונקציות, יחסים ופונקציות עולות ממש.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>אותם כלים של בחירה וסידור סופרים גם עצמים מתמטיים.</p>
    <div class="lesson-rule">🔑 <b>פונקציות:</b> מספר הפונקציות $f:A\to B$ הוא $|B|^{|A|}$ (לכל איבר של $A$ בוחרים תמונה ב-$B$ באופן בלתי תלוי). <b>יחסים:</b> יחס על $A$ הוא תת-קבוצה כלשהי של $A\times A$, ולכן יש $2^{|A|^2}$ יחסים, ו-$\binom{|A|^2}{k}$ יחסים בגודל $k$ בדיוק.</div>
    <div class="lesson-rule">🔑 <b>פונקציה עולה ממש</b> $f(1)<f(2)<\dots<f(m)$ נקבעת באופן יחיד על ידי קבוצת התמונות שלה, כי אפשר לסדר כל קבוצה כזו בסדר עולה בדרך אחת בלבד. לכן מספר הפונקציות העולות ממש מ-$\{1,\dots,m\}$ ל-$B$ הוא $\binom{|B|}{m}$. אותו דבר ליורדות ממש.</div>
    <p>יחס $R\subseteq A\times A$ הוא פונקציה אם לכל $a\in A$ יש בדיוק $b$ אחד עם $(a,b)\in R$. "יחסים שאינם פונקציות" נספרים כמשלים: כל היחסים פחות הפונקציות.</p>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">כמה פונקציות עולות ממש מ-$\{1,2\}$ ל-$\{1,2,3,4\}$? בוחרים זוג תמונות: $\binom42=6$. כל זוג מסתדר פעם אחת בסדר עולה. (בין כל הפונקציות, $4^2=16$, רק 6 עולות ממש.)</div>
    <div class="lesson-trap">⚠️ פונקציה עולה ממש אינה "פונקציה חד-חד-ערכית כלשהי": חד-חד-ערכית נותנת $P(|B|,m)$ פונקציות, ועולה ממש רק אחת מכל $m!$ הסדרים.</div>` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`כמה פונקציות $f:\{1,2,3\}\to\{1,2,3,4,5\}$ יש?`,
        answer: 125, tol: 0,
        explain: String.raw`לכל אחד משלושת האיברים 5 תמונות אפשריות: $5^3=125$. (לא $3^5$: זה היה מספר הפונקציות בכיוון ההפוך.)` },
      recap: String.raw`פונקציות $A\to B$: $|B|^{|A|}$.` },
    { id: "C04-Q2",
      step: { type: "numeric",
        prompt: String.raw`כמה יחסים $R\subseteq A\times A$ יש על $A=\{1,2,3,4\}$?`,
        answer: 65536, tol: 0,
        explain: String.raw`$|A\times A|=16$, וכל יחס הוא תת-קבוצה של $A\times A$: $2^{16}=65536$.` },
      recap: String.raw`יחסים על $A$: $2^{|A|^2}$.` },
    { id: "C04-Q3",
      step: { type: "numeric",
        prompt: String.raw`כמה פונקציות עולות ממש $f:\{1,2,3\}\to\{1,2,\dots,7\}$ יש?`,
        answer: 35, tol: 0,
        explain: String.raw`פונקציה עולה ממש נקבעת על ידי קבוצת התמונות, שהיא תת-קבוצה בגודל 3 של $\{1,\dots,7\}$: $\binom73=35$.` },
      recap: String.raw`עולה ממש: $\binom{|B|}{|A|}$.` },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`כמה יחסים על $A=\{1,2,3\}$ מקיימים $|R|\le2$?`,
        answer: 46, tol: 0,
        explain: String.raw`$|A\times A|=9$. גודל 0: $\binom90=1$. גודל 1: $\binom91=9$. גודל 2: $\binom92=36$. סך הכול $1+9+36=46$. (שימו לב לגודל 0, היחס הריק.)` },
      recap: String.raw`טווח גדלים: מחברים את $\binom Nk$ לכל $k$ בטווח, כולל $0$.` },
    { id: "C04-Q5",
      question: String.raw`על $A=\{1,2,3\}$, כמה יחסים $R\subseteq A\times A$ אינם פונקציות?`,
      options: [
        { id: "a", value: String.raw`$485$` },
        { id: "b", value: String.raw`$512$` },
        { id: "c", value: String.raw`$27$` },
        { id: "d", value: String.raw`$509$` },
      ],
      correctId: "a",
      explanation: String.raw`כל היחסים: $2^9=512$. הפונקציות $A\to A$: $3^3=27$. אינם פונקציות: $512-27=485$. התשובה $512$ היא כל היחסים. $27$ הוא מספר הפונקציות עצמן. ו-$509=512-3$ שוכח שיש 27 פונקציות ולא 3.`,
      recap: String.raw`"לא פונקציות" = $2^{|A|^2}-|A|^{|A|}$.` },
  ],
});
