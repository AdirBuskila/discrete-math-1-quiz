/* relations, level 4 - arithmetic relations on Z: reduce to a congruence, read off Z/R. ai-verified (tools/verify/needhelp/relations/check.py) */
COURSE_LEVEL("relations", {
  id: "C04", order: 4, icon: "🕸️", title: "יחסים חשבוניים ומחלקות",
  goal: "אחרי השלב הזה אפשר לפשט תנאי חשבוני של התחלקות לתנאי קונגרואנציה ולמצוא את מחלקות השקילות.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>ביחס על $\mathbb{Z}$ מהצורה $xRy\iff n\mid(ax+by)$ כדאי קודם לפשט את התנאי. המטרה היא להגיע ל-$x\equiv y\pmod m$, ואז המחלקות הן המספרים באותה שארית ב-$m$ ו-$\mathbb{Z}/R=\{[0],[1],\dots,[m-1]\}$.</p>
    <div class="lesson-rule">🔑 <b>מתכון.</b> אם $b\equiv-a\pmod n$ אז $ax+by\equiv a(x-y)\pmod n$.<br>
    אם $\gcd(a,n)=1$ התנאי שקול ל-$n\mid(x-y)$, כלומר $x\equiv y\pmod n$, ויש $n$ מחלקות.<br>
    אם $d=\gcd(a,n)>1$ מחלקים ב-$d$: התנאי שקול ל-$\frac nd\mid(x-y)$, ויש $\frac nd$ מחלקות.</div>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">$xRy\iff7\mid(2x+5y)$. מכיוון ש-$5\equiv-2\pmod7$, מתקיים $2x+5y\equiv2(x-y)$. ו-$7$ ראשוני ואינו מחלק את $2$, לכן $7\mid2(x-y)\iff7\mid(x-y)$.<br>
    כלומר $xRy\iff x\equiv y\pmod7$ ו-$\mathbb{Z}/R=\{[0],[1],\dots,[6]\}$, שבע מחלקות.</div>
    <div class="lesson-trap">⚠️ מותר לצמצם גורם רק כשהוא זר למודול. ב-$6\mid2(x-y)$ אי אפשר לצמצם את $2$ למודול $6$: מחלקים את שניהם ב-2 ומקבלים $3\mid(x-y)$.</div>
    <p>תנאי זוגיות הוא אותו עיקרון עם $n=2$: למשל $x+y+1$ אי-זוגי שקול ל-$x+y$ זוגי, כלומר $x\equiv y\pmod2$, ואז יש שתי מחלקות: הזוגיים והאי-זוגיים.</p>` },
  questions: [
    { id: "C04-Q1",
      question: String.raw`$xRy\iff4\mid(x+3y)$ על $\mathbb{Z}$. איזה תנאי שקול לו?`,
      options: [
        { id: "a", value: String.raw`$x\equiv y\pmod4$` },
        { id: "b", value: String.raw`$x\equiv-y\pmod4$` },
        { id: "c", value: String.raw`$x\equiv y\pmod2$` },
        { id: "d", value: String.raw`$x\equiv y+2\pmod4$` },
      ],
      correctId: "a",
      explanation: String.raw`$3\equiv-1\pmod4$, לכן $x+3y\equiv x-y$ ו-$4\mid(x+3y)\iff4\mid(x-y)$. הדוגמה $x=1,y=3$ מפריכה את $x\equiv-y$: $1+9=10$ אינו מתחלק ב-4. הדוגמה $x=0,y=2$ מפריכה את $x\equiv y\pmod2$ כשקול: $0+6=6$ אינו מתחלק ב-4. והדוגמה $x=y=0$ מפריכה את $x\equiv y+2$.`,
      recap: String.raw`$b\equiv-a\pmod n\Rightarrow ax+by\equiv a(x-y)$.` },
    { id: "C04-Q2",
      step: { type: "numeric",
        prompt: String.raw`$xRy\iff5\mid(4x+y)$ על $\mathbb{Z}$ הוא יחס שקילות. כמה איברים יש ב-$\mathbb{Z}/R$?`,
        answer: 5, tol: 0,
        explain: String.raw`$y\equiv-4x\equiv x\pmod5$, ולכן $4x+y\equiv y-x$ ו-$5\mid(4x+y)\iff x\equiv y\pmod5$. יש חמש מחלקות: $[0],[1],[2],[3],[4]$.` },
      recap: String.raw`$n\mid ax+by$ עם $\gcd(a,n)=1$ ו-$b\equiv-a$: $n$ מחלקות.` },
    { id: "C04-Q3",
      question: String.raw`$xRy\iff2\mid(3x+5y)$ על $\mathbb{Z}$. מהי המחלקה $[0]$?`,
      options: [
        { id: "a", value: "כל המספרים האי-זוגיים" },
        { id: "b", value: "כל הכפולות של 3" },
        { id: "c", value: String.raw`כל המספרים הזוגיים` },
        { id: "d", value: String.raw`כל $\mathbb{Z}$` },
      ],
      correctId: "c",
      explanation: String.raw`$3x+5y\equiv x+y\equiv x-y\pmod2$, ולכן $xRy$ בדיוק כש-$x,y$ באותה זוגיות. $[0]=\{y:\ 0Ry\}=\{y:\ 2\mid5y\}$ וזה כל הזוגיים. אי-זוגיים אינם קשורים ל-$0$, ($3\cdot0+5\cdot1=5$ אי-זוגי), ו-$\mathbb{Z}/R$ כולל שתי מחלקות, לא אחת.`,
      recap: String.raw`תנאי זוגיות: $[0]$ = הזוגיים, ויש שתי מחלקות.` },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`$xRy\iff6\mid(2x+4y)$ על $\mathbb{Z}$ הוא יחס שקילות. כמה איברים יש ב-$\mathbb{Z}/R$?`,
        answer: 3, tol: 0,
        explain: String.raw`$4\equiv-2\pmod6$, ולכן $2x+4y\equiv2(x-y)$. התנאי $6\mid2(x-y)$ שקול ל-$3\mid(x-y)$ (מחלקים ב-2). לכן $x\equiv y\pmod3$ ויש 3 מחלקות, לא 6.` },
      recap: String.raw`כשהמקדם לא זר למודול מצמצמים: מודול $\frac nd$.` },
    { id: "C04-Q5",
      step: { type: "numeric",
        prompt: String.raw`$xRy\iff4\mid(x+3y)$. המחלקה $[7]$ היא $\{4k+r:\ k\in\mathbb{Z}\}$ עם $0\le r\le3$. מהו $r$?`,
        answer: 3, tol: 0,
        explain: String.raw`היחס שקול ל-$x\equiv y\pmod4$. $7=4\cdot1+3$, לכן $[7]=\{4k+3\}$ ו-$r=3$.` },
      recap: String.raw`שם המחלקה נקבע לפי השארית במודול.` },
  ],
});
