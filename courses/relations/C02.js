/* relations, level 2 - equivalence classes and the quotient set. ai-verified (tools/verify/needhelp/relations/check.py) */
COURSE_LEVEL("relations", {
  id: "C02", order: 2, icon: "🕸️", title: "מחלקות שקילות וקבוצת מנה",
  goal: "אחרי השלב הזה אפשר לחשב מחלקת שקילות, לספור מחלקות ולכתוב את קבוצת המנה A/R.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>ביחס שקילות $R$ על $A$, <b>מחלקת השקילות</b> של $a$ היא כל האיברים הקשורים אליו: $[a]=\{b\in A:\ aRb\}$. <b>קבוצת המנה</b> $A/R$ היא קבוצה של מחלקות: $A/R=\{[a]:\ a\in A\}$, וכל מחלקה נרשמת פעם אחת.</p>
    <div class="lesson-rule">🔑 שלוש עובדות על מחלקות, לכל יחס שקילות:<br>
    1. $[a]=[b]\iff aRb$.<br>
    2. שתי מחלקות שונות הן <b>זרות</b>. מחלקות עם איבר משותף הן אותה מחלקה.<br>
    3. איחוד כל המחלקות הוא $A$ (כי $a\in[a]$).</div>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">על $A=\{1,2,\dots,6\}$ נגדיר $xRy\iff x\equiv y\pmod3$.<br>
    $[1]=\{1,4\}$, $[2]=\{2,5\}$, $[3]=\{3,6\}$.<br>
    $A/R=\{\{1,4\},\{2,5\},\{3,6\}\}$ ויש 3 מחלקות. $[1]=[4]$ היא מחלקה אחת ולא שתיים.</div>
    <div class="lesson-trap">⚠️ ב-$A/R$ כותבים כל מחלקה פעם אחת: $[1]=[4]$ הן אותה מחלקה, ולא שני איברים של $A/R$.</div>` },
  questions: [
    { id: "C02-Q1",
      step: { type: "numeric",
        prompt: String.raw`על $A=\{1,2,\dots,10\}$ מוגדר $xRy\iff x\equiv y\pmod3$. כמה איברים יש במחלקה $[1]$?`,
        answer: 4, tol: 0,
        explain: String.raw`$[1]$ כוללת את כל $x\in A$ ששארית החלוקה שלהם ב-3 היא 1: $\{1,4,7,10\}$. לכן 4 איברים.` },
      recap: String.raw`$[a]$ = כל האיברים שהיחס קושר ל-$a$.` },
    { id: "C02-Q2",
      step: { type: "numeric",
        prompt: String.raw`באותו יחס ($xRy\iff x\equiv y\pmod3$ על $\{1,\dots,10\}$) כמה איברים יש ב-$A/R$?`,
        answer: 3, tol: 0,
        explain: String.raw`המחלקות לפי שארית ב-3: $\{3,6,9\}$, $\{1,4,7,10\}$, $\{2,5,8\}$. שלוש מחלקות שונות, ולכן $|A/R|=3$. אין לספור איברים של $A$.` },
      recap: String.raw`$|A/R|$ סופר מחלקות, לא איברים של $A$.` },
    { id: "C02-Q3",
      question: String.raw`על $A=\{1,2,3,4\}$ נתון יחס השקילות $R=\{(1,1),(2,2),(3,3),(4,4),(1,2),(2,1),(3,4),(4,3)\}$. מהי $A/R$?`,
      options: [
        { id: "a", value: String.raw`$\{\{1,2,3\},\{4\}\}$` },
        { id: "b", value: String.raw`$\{\{1\},\{2\},\{3\},\{4\}\}$` },
        { id: "c", value: String.raw`$\{\{1,2\},\{3\},\{4\}\}$` },
        { id: "d", value: String.raw`$\{\{1,2\},\{3,4\}\}$` },
      ],
      correctId: "d",
      explanation: String.raw`$[1]=\{b:\ 1Rb\}=\{1,2\}$ ו-$[3]=\{3,4\}$, והמחלקות של 2 ושל 4 חוזרות עליהן. לכן $A/R=\{\{1,2\},\{3,4\}\}$. ארבעה סינגלטונים מתאימים ליחס הזהות. באפשרות עם $\{1,2,3\}$ האיבר $3$ אינו קשור ל-$1$, ובאפשרות עם $\{3\},\{4\}$ מופרדים $3$ ו-$4$ למרות ש-$3R4$.`,
      recap: String.raw`לכל איבר $a$ אוספים את כל $b$ עם $aRb$.` },
    { id: "C02-Q4",
      question: String.raw`$R$ יחס שקילות על $A$ ו-$(2,5)\in R$. מה בהכרח נכון?`,
      options: [
        { id: "a", value: String.raw`$[2]\cap[5]=\emptyset$` },
        { id: "b", value: String.raw`$[2]=[5]$` },
        { id: "c", value: String.raw`$2=5$` },
        { id: "d", value: String.raw`$[2]=\{2\}$ ו-$[5]=\{5\}$` },
      ],
      correctId: "b",
      explanation: String.raw`לפי $[a]=[b]\iff aRb$, מ-$2R5$ נובע $[2]=[5]$. מחלקות זרות הן רק של איברים שאינם קשורים, ואילו כאן יש איבר משותף ($5\in[2]$ ו-$5\in[5]$). $2=5$ אינו נובע (למשל ביחס $x\equiv y\pmod3$ מתקיים $2R5$). ושתי מחלקות עם איבר יחיד סותרות את $2R5$.`,
      recap: String.raw`$aRb\iff[a]=[b]$.` },
    { id: "C02-Q5",
      step: { type: "numeric",
        prompt: String.raw`על $A=\{1,2,\dots,20\}$ מוגדר $xRy\iff4\mid(x-y)$. כמה איברים יש במחלקה $[3]$?`,
        answer: 5, tol: 0,
        explain: String.raw`$[3]$ כוללת את המספרים ששארית החלוקה שלהם ב-4 היא 3: $\{3,7,11,15,19\}$. לכן 5 איברים.` },
      recap: String.raw`מחלקה של יחס מודולרי = כל המספרים באותה שארית.` },
  ],
});
