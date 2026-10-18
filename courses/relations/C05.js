/* relations, level 5 - proving an arithmetic relation is an equivalence. ai-verified (tools/verify/needhelp/relations/check.py) */
COURSE_LEVEL("relations", {
  id: "C05", order: 5, icon: "🕸️", title: "הוכחת יחס שקילות",
  goal: "אחרי השלב הזה אפשר לכתוב הוכחה מסודרת שיחס חשבוני הוא רפלקסיבי, סימטרי וטרנזיטיבי, ולהפריך תכונה שנכשלת.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>ההוכחה היא שלושה חלקים, וכל חלק מתחיל ב-<b>איברים כלליים</b>, לא בדוגמה.</p>
    <div class="lesson-rule">🔑 <b>תבנית.</b> נתון $xRy\iff P(x,y)$.<br>
    <b>רפלקסיבי:</b> לכל $x$ מציבים $y=x$ ובודקים ש-$P(x,x)$ נכון.<br>
    <b>סימטרי:</b> לכל $x,y$: מניחים $P(x,y)$ ומראים $P(y,x)$. אם $P$ מתחלק ב-$n$, מחברים את שני הביטויים ומקבלים כפולה של $n$.<br>
    <b>טרנזיטיבי:</b> לכל $x,y,z$: מניחים $P(x,y)$ וגם $P(y,z)$, <b>מחברים</b> את שני התנאים כך ש-$y$ נשאר רק כפולה של $n$, ומבטלים אותו.</div>
    <h3>דוגמה קטנה</h3>
    <div class="lesson-ex">$xRy\iff3\mid(x+2y)$.<br>
    <b>רפלקסיבי:</b> $x+2x=3x$, מתחלק ב-3.<br>
    <b>סימטרי:</b> נניח $3\mid(x+2y)$. אז $(x+2y)+(y+2x)=3x+3y$ מתחלק ב-3. 3 מחלק גם את $x+2y$, ולכן הוא מחלק את ההפרש $y+2x$, כלומר $yRx$.<br>
    <b>טרנזיטיבי:</b> נניח $3\mid(x+2y)$ וגם $3\mid(y+2z)$. הסכום הוא $x+3y+2z$. מכיוון ש-$3\mid3y$, גם $3\mid(x+2z)$, כלומר $xRz$.</div>
    <div class="lesson-trap">⚠️ "בדקתי עבור $x=1,y=2$" אינה הוכחה. וכדי להפריך תכונה מספיק דוגמה נגדית אחת קונקרטית, כמו שרשרת שבה הטרנזיטיביות נכשלת.</div>` },
  questions: [
    { id: "C05-Q1",
      question: "איך מוכיחים שיחס $R$ הוא סימטרי?",
      options: [
        { id: "a", value: String.raw`מראים ש-$xRx$ לכל $x$` },
        { id: "b", value: String.raw`מניחים $xRy$ עבור $x,y$ כלליים, ומראים $yRx$` },
        { id: "c", value: String.raw`מניחים $xRy$ וגם $yRz$, ומראים $xRz$` },
        { id: "d", value: String.raw`בודקים כמה זוגות, למשל $x=1,y=2$` },
      ],
      correctId: "b",
      explanation: String.raw`סימטריה היא הטענה "אם $xRy$ אז $yRx$" לכל $x,y$. האפשרות שמראה $xRx$ מוכיחה רפלקסיביות, האפשרות עם $y,z$ מוכיחה טרנזיטיביות, ובדיקת כמה זוגות אינה הוכחה לכל הזוגות.`,
      recap: String.raw`סימטריה: מניחים $xRy$ כללי, מראים $yRx$.` },
    { id: "C05-Q2",
      step: { type: "order",
        prompt: String.raw`סדרו את הוכחת הטרנזיטיביות של היחס $xRy\iff5\mid(2x+3y)$.`,
        lines: [
          String.raw`נניח $xRy$ וגם $yRz$, כלומר $5\mid(2x+3y)$ וגם $5\mid(2y+3z)$.`,
          String.raw`סכום שני המספרים מתחלק ב-5: $5\mid(2x+3y)+(2y+3z)=2x+5y+3z$.`,
          String.raw`גם $5y$ מתחלק ב-5, ולכן 5 מחלק את ההפרש $(2x+5y+3z)-5y=2x+3z$.`,
          String.raw`קיבלנו $5\mid(2x+3z)$, כלומר $xRz$, ולכן $R$ טרנזיטיבי.`,
        ],
        explain: "קודם ההנחות, אחר כך הסכום שלהן, אחר כך ביטול $5y$, ובסוף המסקנה. כל שורה נשענת על הקודמת." },
      recap: "מניחים, מחברים, מבטלים את $y$, ומסיימים ב-$xRz$." },
    { id: "C05-Q3",
      step: { type: "findbug",
        prompt: String.raw`בהוכחת הסימטריה של $xRy\iff5\mid(2x+3y)$ נשתלה טעות בשורה אחת. איזו?`,
        lines: [
          String.raw`נניח $xRy$, כלומר $5\mid(2x+3y)$, ונראה $5\mid(2y+3x)$.`,
          String.raw`$(2x+3y)+(2y+3x)=5x+5y=5xy$, ולכן 5 מחלק את הסכום.`,
          String.raw`5 מחלק את הסכום וגם את $2x+3y$, ולכן הוא מחלק את ההפרש שלהם.`,
          String.raw`ההפרש הוא $2y+3x$, כלומר $5\mid(2y+3x)$ ו-$yRx$.`,
        ],
        bugIndex: 1,
        explain: String.raw`$5x+5y=5(x+y)$ ולא $5xy$. למשל ב-$x=2,y=3$ מקבלים $5x+5y=25$ ואילו $5xy=30$.` },
      recap: String.raw`$5x+5y=5(x+y)$, לא $5xy$.` },
    { id: "C05-Q4",
      question: String.raw`$xRy\iff|x-y|\le1$ על $\mathbb{Z}$. מה נכון?`,
      options: [
        { id: "a", value: String.raw`$R$ אינו טרנזיטיבי: $0R1$ ו-$1R2$ אבל לא $0R2$` },
        { id: "b", value: String.raw`$R$ אינו סימטרי: $0R1$ אבל לא $1R0$` },
        { id: "c", value: String.raw`$R$ אינו רפלקסיבי: לא מתקיים $0R0$` },
        { id: "d", value: String.raw`$R$ יחס שקילות` },
      ],
      correctId: "a",
      explanation: String.raw`$|0-1|=1$ ו-$|1-2|=1$ אבל $|0-2|=2>1$, ולכן הטרנזיטיביות נכשלת. $R$ רפלקסיבי ($|x-x|=0$) וסימטרי ($|x-y|=|y-x|$), ולכן שלוש האפשרויות האחרות שגויות.`,
      recap: String.raw`דוגמה נגדית לטרנזיטיביות: שרשרת $a,b,c$ שהזוג $(a,c)$ חסר בה.` },
    { id: "C05-Q5",
      question: String.raw`ביחס $xRy\iff4\mid(x+3y)$, בהוכחת הטרנזיטיביות מניחים $4\mid(x+3y)$ וגם $4\mid(y+3z)$. איזה צירוף שלהם מבטל את $y$ מודולו 4 ונותן $x+3z$ עד כדי כפולה של 4?`,
      options: [
        { id: "a", value: String.raw`$(x+3y)-(y+3z)$` },
        { id: "b", value: String.raw`$(x+3y)+(3y+z)$` },
        { id: "c", value: String.raw`$(x+3y)+(y+3z)$` },
        { id: "d", value: String.raw`$(x+3y)\cdot(y+3z)$` },
      ],
      correctId: "c",
      explanation: String.raw`$(x+3y)+(y+3z)=x+3z+4y$, ו-$4y$ כפולה של 4. ההפרש נותן $x+2y-3z$ (נשאר $y$ והמקדם של $z$ שגוי), הצירוף עם $3y+z$ אינו נובע מההנחות (הוא לא אחד מהתנאים), והמכפלה אינה קשורה לחיבור של התנאים.`,
      recap: String.raw`בטרנזיטיביות מחברים כך ש-$y$ נעלם או נשאר כפולה של $n$.` },
  ],
});
