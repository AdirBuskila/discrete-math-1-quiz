/* relations, level 7 - boss: real exam questions. ai-verified (tools/verify/needhelp/relations/check.py) */
COURSE_LEVEL("relations", {
  id: "C07", order: 7, icon: "🏆", title: "בוס: שאלות מבחן אמיתיות", boss: true,
  goal: "אחרי השלב הזה אפשר לפתור שאלות יחסי שקילות מהמבחנים: הוכחה חשבונית, חלוקות, חישוב |R| והפרכה או הוכחה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>חמש שאלות אמיתיות. מזכירים את הדרך:</p>
    <div class="lesson-rule">🔑 <b>יחס חשבוני:</b> מפשטים לקונגרואנציה, מוכיחים רפלקסיבי / סימטרי / טרנזיטיבי עם איברים כלליים, ורושמים את המחלקות. אינו סדר חלקי אלא אם הוא יחס הזהות.<br>
    <b>חלוקות:</b> בודקים שהבלוקים לא ריקים, זרים ומכסים את $A$, ו-$|R|=\sum|B_i|^2$.<br>
    <b>הוכח או הפרך:</b> מזהים מה הטענה אומרת על הדוגמה הקטנה ביותר, ורק אז מכריעים.</div>` },
  questions: [
    { bankId: "26A-A-Q3a", recap: String.raw`מפשטים ל-$x\equiv y\pmod5$, מוכיחים שלוש תכונות ורושמים חמש מחלקות.` },
    { bankId: "23A-A-Q4a", recap: String.raw`$x+y+1$ אי-זוגי $\iff x\equiv y\pmod2$: שתי מחלקות, ויש מחלקה עם שני איברים, ולכן אינו סדר חלקי.` },
    { bankId: "23A-A-Q2c", recap: String.raw`מוודאים שזו חלוקה, ואז $|R|=1+9+4=14$.` },
    { bankId: "25A-B-Q2c", recap: String.raw`היחס קובע את מחלקת $B$ לפי $B\cap\{1\}$: שתי מחלקות.` },
    { bankId: "26A-A-Q1c", recap: String.raw`יחס הזהות הוא יחס שקילות המוכל בכל יחס שקילות, ולכן החיתוך הוא הזהות.` },
  ],
});
