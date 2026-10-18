/* counting, level 8 - binomial theorem sums and big-O. ai-verified (tools/verify/needhelp/counting/check.py) */
COURSE_LEVEL("counting", {
  id: "C08", order: 8, icon: "∑", title: "סכומי בינום ו-O",
  goal: "אחרי השלב הזה אפשר לחשב סכומים עם מקדמים בינומיים בצורה סגורה ולבדוק טענות מהצורה $f(n)=O(g(n))$.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>סכום עם $\binom nk$ הוא כמעט תמיד הבינום של ניוטון בהסוואה.</p>
    <div class="lesson-rule">🔑 <b>הבינום:</b> $(x+y)^n=\sum_{k=0}^n\binom nkx^ky^{n-k}$. הצבות שימושיות: $\sum_k\binom nk=2^n$ ($x=y=1$), ו-$\sum_k\binom nka^k=(a+1)^n$ ($x=a$, $y=1$). כשהחזקה מופיעה כ-$3^{2k}$, כותבים $9^k$.</div>
    <div class="lesson-rule">🔑 <b>עוד שלוש עובדות:</b> (1) מספר תתי-הקבוצות בגודל זוגי (וגם בגודל אי-זוגי) של קבוצה בת $n\ge1$ איברים הוא $2^{n-1}$. (2) $\sum_k k\binom nk=n\cdot2^{n-1}$ (גוזרים את $(1+x)^n$ ומציבים $x=1$). (3) לכן סכום הגדלים של כל תתי-הקבוצות של קבוצה בת $n$ איברים הוא $n\cdot2^{n-1}$, כי יש $\binom nk$ תתי-קבוצות בגודל $k$.</div>
    <div class="lesson-rule">🔑 <b>סימון $O$:</b> $f(n)=O(g(n))$ אם קיימים $c>0$ ו-$n_0$ כך ש-$f(n)\le c\,g(n)$ לכל $n\ge n_0$. סכום של שני מעריכיים: $f(n)=a^n+b^n\le2\max(a,b)^n$, ולכן $f=O(\max(a,b)^n)$. ומנגד אם $\left(\frac ab\right)^n$ לא חסום אז $a^n\ne O(b^n)$.</div>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">$\sum_{k=0}^n\binom nk\left(2^k+5^k\right)=(2+1)^n+(5+1)^n=3^n+6^n$. אז $f(n)\le2\cdot6^n$ ולכן $f=O(6^n)$.</div>
    <div class="lesson-trap">⚠️ $\sum_{k=0}^n\binom nka^k=(a+1)^n$ ולא $a^n$. וגם: כשהסכום מתחיל מ-$k=0$, תת-הקבוצה הריקה נכללת (ב-$\sum k\binom nk$ היא תורמת $0$).</div>` },
  questions: [
    { id: "C08-Q1",
      step: { type: "numeric",
        prompt: String.raw`חשבו את $\sum_{k=0}^{6}\binom6k2^k$.`,
        answer: 729, tol: 0,
        explain: String.raw`$\sum_k\binom6k2^k1^{6-k}=(2+1)^6=3^6=729$.` },
      recap: String.raw`$\sum_k\binom nka^k=(a+1)^n$.` },
    { id: "C08-Q2",
      question: String.raw`מהו $\sum_{k=0}^{n}\binom nk\left(2^k+3^k\right)$?`,
      options: [
        { id: "a", value: String.raw`$3^n+4^n$` },
        { id: "b", value: String.raw`$5^n$` },
        { id: "c", value: String.raw`$2^n+3^n$` },
        { id: "d", value: String.raw`$6^n$` },
      ],
      correctId: "a",
      explanation: String.raw`מפצלים לשני סכומים: $\sum\binom nk2^k=(2+1)^n=3^n$ ו-$\sum\binom nk3^k=(3+1)^n=4^n$, ולכן $3^n+4^n$. התשובה $5^n$ מחברת בתוך הבסיס. $2^n+3^n$ שוכחת את ה-$+1$. ו-$6^n$ מכפילה את הבסיסים.`,
      recap: String.raw`מפצלים, ומחליפים כל $a^k$ ב-$(a+1)^n$.` },
    { id: "C08-Q3",
      step: { type: "numeric",
        prompt: String.raw`כמה תתי-קבוצות בגודל זוגי יש לקבוצה $\{1,2,\dots,10\}$ (כולל הקבוצה הריקה)?`,
        answer: 512, tol: 0,
        explain: String.raw`חצי מכל תתי-הקבוצות: $2^{10}/2=2^9=512$.` },
      recap: String.raw`גודל זוגי: $2^{n-1}$.` },
    { id: "C08-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהו הסכום $\sum_{B\subseteq\{1,\dots,8\}}|B|$, כלומר סכום הגדלים של כל תתי-הקבוצות של $\{1,\dots,8\}$?`,
        answer: 1024, tol: 0,
        explain: String.raw`$\sum_k k\binom8k=8\cdot2^7=1024$.` },
      recap: String.raw`סכום גדלי תתי-הקבוצות: $n2^{n-1}$.` },
    { id: "C08-Q5",
      question: String.raw`נתון $f(n)=\sum_{k=0}^{n}\binom nk\left(4^k+2^k\right)=5^n+3^n$. איזו טענה נכונה?`,
      options: [
        { id: "a", value: String.raw`$f(n)=O(5^n)$` },
        { id: "b", value: String.raw`$f(n)=O(3^n)$` },
        { id: "c", value: String.raw`$f(n)=O(4^n)$` },
        { id: "d", value: String.raw`$f(n)=O(2^n)$` },
      ],
      correctId: "a",
      explanation: String.raw`$3^n\le5^n$ ולכן $f(n)\le2\cdot5^n$, כלומר $f=O(5^n)$. בשלוש האחרות $f(n)\ge5^n$ ולכן $\frac{f(n)}{3^n},\frac{f(n)}{4^n},\frac{f(n)}{2^n}\ge\left(\frac54\right)^n\to\infty$ לא חסום, ואין קבוע $c$ שמתאים.`,
      recap: "סכום מעריכיים: הבסיס הגדול קובע את ה-$O$." },
    { id: "C08-Q6",
      step: { type: "numeric",
        prompt: String.raw`חשבו את $\sum_{k=0}^{9}k\binom9k$.`,
        answer: 2304, tol: 0,
        explain: String.raw`$n\cdot2^{n-1}=9\cdot2^8=9\cdot256=2304$.` },
      recap: String.raw`$\sum k\binom nk=n2^{n-1}$.` },
  ],
});
