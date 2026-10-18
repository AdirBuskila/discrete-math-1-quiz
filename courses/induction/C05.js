/* induction, level 5 - sums of fractions (telescoping type). ai-verified */
COURSE_LEVEL("induction", {
  id: "C05", order: 5, icon: "➗", title: "סכומי שברים",
  goal: "אחרי השלב הזה אפשר להוכיח באינדוקציה זהות על סכום שברים עם מכנה שהוא מכפלה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>בסכום שברים הצעד הוא אותו צעד כמו קודם: (אגף ימין של $P(k)$) + (האיבר החדש). האלגברה היא שונה: צריך מכנה משותף, ואז לפרק את המונה כך שאחד הגורמים מצטמצם.</p>
    <div class="lesson-ex">$P(n)$: $\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\dots+\frac{1}{n(n+1)}=\frac{n}{n+1}$.<br>
    האיבר החדש: $\frac{1}{(k+1)(k+2)}$. מכנה משותף $(k+1)(k+2)$:<br>
    $\frac{k}{k+1}+\frac{1}{(k+1)(k+2)}=\frac{k(k+2)+1}{(k+1)(k+2)}=\frac{k^2+2k+1}{(k+1)(k+2)}=\frac{(k+1)^2}{(k+1)(k+2)}=\frac{k+1}{k+2}$,<br>
    וזה אגף ימין של $P(k+1)$.</div>
    <div class="lesson-rule">🔑 המכנה של האיבר החדש כבר מכיל את המכנה של אגף ימין של $P(k)$ (כאן $k+1$) כגורם. לכן המכנה המשותף הוא המכנה של האיבר החדש, והמונה הוא (מונה אגף ימין של $P(k)$) כפול הגורם החסר, ועוד 1. אחר כך מפרקים את המונה, והגורם המשותף מצטמצם.</div>
    <div class="lesson-trap">⚠️ לא מצמצמים לפני שמפרקים. כדי לצמצם, המונה צריך להתפרק לגורמים, ולכן כותבים אותו כמכפלה (למשל $k^2+2k+1=(k+1)^2$).</div>
    <p>בסיס: מציבים את הערך הראשון בשני האגפים. כאן, לפי $P(1)$: אגף שמאל $\frac{1}{1\cdot2}=\frac12$ ואגף ימין $\frac{1}{1+1}=\frac12$.</p>` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`$P(n)$: $\sum_{i=1}^{n}\frac{1}{(2i-1)(2i+1)}=\frac{n}{2n+1}$. ב-$P(1)$ אגף שמאל הוא $\frac{1}{d}$. מהו $d$?`,
        answer: 3, tol: 0,
        explain: String.raw`עבור $i=1$ המכנה הוא $(2\cdot1-1)(2\cdot1+1)=1\cdot3=3$. אגף ימין: $\frac{1}{2\cdot1+1}=\frac13$, ולכן הבסיס נכון.` },
      recap: "מציבים את האינדקס הראשון במכנה." },
    { id: "C05-Q2",
      step: { type: "numeric",
        prompt: String.raw`$P(n)$: $\sum_{i=1}^{n}\frac{1}{(2i-1)(2i+1)}=\frac{n}{2n+1}$. עבור $k=2$ חשבו את $\frac{k}{2k+1}+\frac{1}{(2k+1)(2k+3)}$ (עשרוני, בדיוק של שלוש ספרות אחרי הנקודה).`,
        answer: 0.428571, tol: 0.001,
        explain: String.raw`$\frac25+\frac{1}{5\cdot7}=\frac{14}{35}+\frac{1}{35}=\frac{15}{35}=\frac37\approx0.429$. זה גם אגף ימין של $P(3)$: $\frac{3}{2\cdot3+1}=\frac37$.` },
      recap: "מוסיפים את האיבר החדש לאגף ימין של $P(k)$ ומקבלים את אגף ימין של $P(k+1)$." },
    { id: "C05-Q3",
      question: String.raw`בצעד של הטענה מהשאלה הקודמת מגיעים למונה $k(2k+3)+1$. לאיזה מכפלה הוא שווה?`,
      options: [
        { id: "a", value: String.raw`$(2k+1)(k+1)$` },
        { id: "b", value: String.raw`$(2k+1)(k+2)$` },
        { id: "c", value: String.raw`$2(k+1)^2$` },
        { id: "d", value: String.raw`$(2k+3)(k+1)$` },
      ],
      correctId: "a",
      explanation: String.raw`$k(2k+3)+1=2k^2+3k+1=(2k+1)(k+1)$. הגורם $(2k+1)$ מצטמצם עם המכנה. $(2k+1)(k+2)=2k^2+5k+2$ ו-$2(k+1)^2=2k^2+4k+2$ ו-$(2k+3)(k+1)=2k^2+5k+3$ שונים מהמונה.`,
      recap: "מפרקים את המונה כך שהגורם $(2k+1)$ מצטמצם." },
    { id: "C05-Q4",
      step: { type: "order",
        prompt: String.raw`סדרו את הצעד בהוכחת $\sum_{i=1}^{n}\frac{1}{(2i-1)(2i+1)}=\frac{n}{2n+1}$.`,
        lines: [
          String.raw`נניח $\sum_{i=1}^{k}\frac{1}{(2i-1)(2i+1)}=\frac{k}{2k+1}$ עבור $k\ge1$.`,
          String.raw`$\sum_{i=1}^{k+1}\frac{1}{(2i-1)(2i+1)}=\frac{k}{2k+1}+\frac{1}{(2k+1)(2k+3)}$.`,
          String.raw`$=\frac{k(2k+3)+1}{(2k+1)(2k+3)}=\frac{2k^2+3k+1}{(2k+1)(2k+3)}$.`,
          String.raw`$=\frac{(2k+1)(k+1)}{(2k+1)(2k+3)}=\frac{k+1}{2k+3}$, אגף ימין של $P(k+1)$.`,
        ],
        explain: "ההנחה קודמת, אחר כך הוספת האיבר החדש, המכנה המשותף, ולבסוף הפירוק והצמצום." },
      recap: "הנחה, איבר חדש, מכנה משותף, פירוק וצמצום." },
    { id: "C05-Q5",
      step: { type: "findbug",
        prompt: String.raw`בהוכחת הצעד של $\frac{1}{1\cdot2}+\dots+\frac{1}{n(n+1)}=\frac{n}{n+1}$ נשתלה טעות בשורה אחת. איזו?`,
        lines: [
          String.raw`$\sum_{i=1}^{k+1}\frac{1}{i(i+1)}=\frac{k}{k+1}+\frac{1}{(k+1)(k+2)}$ לפי הנחת האינדוקציה.`,
          String.raw`$\frac{k}{k+1}+\frac{1}{(k+1)(k+2)}=\frac{k(k+2)+1}{(k+1)(k+2)}$.`,
          String.raw`$\frac{k(k+2)+1}{(k+1)(k+2)}=\frac{k^2+2k}{(k+1)(k+2)}$.`,
          String.raw`$k^2+2k+1=(k+1)^2$, ולכן המונה הוא $(k+1)^2$.`,
          String.raw`$\frac{(k+1)^2}{(k+1)(k+2)}=\frac{k+1}{k+2}$, אגף ימין של $P(k+1)$.`,
        ],
        bugIndex: 2,
        explain: String.raw`$k(k+2)+1=k^2+2k+1$ ולא $k^2+2k$: נשמט ה-$+1$ של האיבר החדש. למשל ב-$k=1$: $1\cdot3+1=4$ ואילו $1+2=3$.` },
      recap: "לא משמיטים את ה-$+1$ של האיבר החדש במונה." },
  ],
});
