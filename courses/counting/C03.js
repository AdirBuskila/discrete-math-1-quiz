/* counting, level 3 - choosing without order: binomial coefficients and subsets. ai-verified (tools/verify/needhelp/counting/check.py) */
COURSE_LEVEL("counting", {
  id: "C03", order: 3, icon: "🎯", title: "בחירה בלי סדר: תתי-קבוצות",
  goal: "אחרי השלב הזה אפשר להבדיל בין בחירה לסידור ולספור תתי-קבוצות עם תנאים.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>בחירה של קבוצה אין בה סדר: $\{1,2,3\}$ ו-$\{3,1,2\}$ הן אותה קבוצה. לעומת זאת בסידור בשורה הסדר חשוב.</p>
    <div class="lesson-rule">🔑 מספר תתי-הקבוצות בגודל $k$ של קבוצה בת $n$ איברים הוא $\binom nk=\frac{n!}{k!\,(n-k)!}$. הקשר לסידורים: $P(n,k)=\binom nk\cdot k!$ (קודם בוחרים, אחר כך מסדרים). סימטריה: $\binom nk=\binom n{n-k}$. סך כל תתי-הקבוצות: $2^n$.</div>
    <div class="lesson-rule">🔑 <b>תנאי על תת-קבוצה:</b> קובעים לכל איבר אם הוא נכנס, יוצא או חופשי. איבר שחייב להיכנס או חייב לצאת מוציאים מהספירה, ועל כל איבר חופשי יש 2 אפשרויות (נכנס או לא). אם התנאי קובע כמה איברים נכנסים מקבוצה קטנה, בוחרים אותם בנפרד ומכפילים בתתי-הקבוצות של השאר.</div>
    <h3>דוגמאות קטנות</h3>
    <div class="lesson-ex">כמה תתי-קבוצות של $\{1,\dots,9\}$ מכילות את 5 ולא מכילות את 6? ל-5 ול-6 נקבע הגורל, ול-7 האיברים הנותרים יש חופש: $2^7=128$.<br>
    מציאת $n$ מנתון: אם ל-$A$ יש 21 תתי-קבוצות בגודל 2, אז $\binom n2=21\Rightarrow n(n-1)=42\Rightarrow n=7$.</div>
    <div class="lesson-trap">⚠️ "ועדה" (בחירה) מול "יו"ר ומזכיר" (תפקידים שונים, כלומר סידור). אם בתפקידים יש משמעות להבדל בין שני האנשים, זה $P(n,k)$ ולא $\binom nk$.</div>` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהו $\binom83$?`,
        answer: 56, tol: 0,
        explain: String.raw`$\binom83=\frac{8\cdot7\cdot6}{3\cdot2\cdot1}=56$.` },
      recap: String.raw`$\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}$.` },
    { id: "C03-Q2",
      question: String.raw`מתוך 8 אנשים בוחרים יו"ר ומזכיר (שני אנשים שונים, והתפקידים שונים). בכמה דרכים?`,
      options: [
        { id: "a", value: String.raw`$56$` },
        { id: "b", value: String.raw`$28$` },
        { id: "c", value: String.raw`$64$` },
        { id: "d", value: String.raw`$16$` },
      ],
      correctId: "a",
      explanation: String.raw`התפקידים שונים, לכן הסדר חשוב: $8\cdot7=56$. התשובה $28=\binom82$ נכונה לבחירת שני אנשים לוועדה בלי תפקידים. $64=8^2$ מרשה שאותו אדם יהיה גם יו"ר וגם מזכיר. ו-$16=8\cdot2$ אינו מתאים לשום חישוב כאן.`,
      recap: "תפקידים שונים: סידור, לא בחירה." },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`כמה תתי-קבוצות בגודל 4 של $\{1,2,\dots,10\}$ מכילות את המספר $1$?`,
        answer: 84, tol: 0,
        explain: String.raw`המספר 1 כבר בפנים, ויש לבחור עוד 3 איברים מתוך 9 הנותרים: $\binom93=84$.` },
      recap: "איבר שחייב להיכנס: מורידים אותו מהספירה ומקטינים את גודל הבחירה." },
    { id: "C03-Q4",
      step: { type: "numeric",
        prompt: String.raw`לקבוצה $A=\{1,2,\dots,n\}$ יש 78 תתי-קבוצות בגודל 2. מהו $n$?`,
        answer: 13, tol: 0,
        explain: String.raw`$\binom n2=78\Rightarrow n(n-1)=156$. מחפשים שני מספרים עוקבים שמכפלתם 156: $13\cdot12=156$, לכן $n=13$.` },
      recap: String.raw`$\binom n2=m\Rightarrow n(n-1)=2m$.` },
    { id: "C03-Q5",
      step: { type: "numeric",
        prompt: String.raw`כמה תתי-קבוצות $B$ של $\{1,2,\dots,12\}$ מקיימות: $B\cap\{1,2,3\}=\varnothing$ וגם $12\in B$?`,
        answer: 256, tol: 0,
        explain: String.raw`האיברים $1,2,3$ מחוץ ל-$B$ והאיבר $12$ בפנים: 4 איברים שגורלם נקבע. נשארו $12-4=8$ איברים חופשיים, ולכל אחד שתי אפשרויות: $2^8=256$.` },
      recap: String.raw`$n$ איברים, $j$ מהם נקבעו: $2^{n-j}$.` },
    { id: "C03-Q6",
      step: { type: "numeric",
        prompt: String.raw`כמה תתי-קבוצות $B$ של $\{1,2,\dots,9\}$ מקיימות $|B\cap\{1,2,3,4,5\}|=1$?`,
        answer: 80, tol: 0,
        explain: String.raw`מהחמישייה $\{1,\dots,5\}$ נכנס בדיוק איבר אחד: 5 אפשרויות. מארבעת האיברים האחרים $\{6,7,8,9\}$ כל תת-קבוצה מותרת: $2^4=16$. עקרון הכפל: $5\cdot16=80$.` },
      recap: "תנאי על מספר האיברים בחלק אחד: בוחרים אותו, ומכפילים בתתי-הקבוצות של השאר." },
  ],
});
