/* number_theory, level 6 - Euler's phi function. ai-verified (tools/verify/needhelp/number_theory/check.py) */
COURSE_LEVEL("number_theory", {
  id: "C06", order: 6, icon: "φ", title: "פונקציית אוילר",
  goal: "אחרי השלב הזה אפשר לחשב \φ(n) מהפירוק לראשוניים ולהשתמש בה במשפט אוילר.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>$\varphi(n)$ הוא מספר המספרים $1\le m\le n$ שזרים ל-$n$ (כלומר $\gcd(m,n)=1$). למשל $\varphi(10)=4$: המספרים $1,3,7,9$.</p>
    <div class="lesson-formula">$\varphi(p)=p-1$ לראשוני, $\varphi(p^{a})=p^{a}-p^{a-1}=p^{a}\left(1-\frac1p\right)$, ובכללי $\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)$.</div>
    <p>המכפלה רצה על הראשוניים <b>השונים</b> שמחלקים את $n$, פעם אחת כל אחד. הפונקציה כפלית: אם $\gcd(a,b)=1$ אז $\varphi(ab)=\varphi(a)\varphi(b)$.</p>
    <div class="lesson-ex">$\varphi(120)$: $120=2^3\cdot3\cdot5$, ולכן $\varphi(120)=120\cdot\frac12\cdot\frac23\cdot\frac45=32$.</div>
    <div class="lesson-trap">⚠️ $\varphi(n)=n-1$ רק כש-$n$ ראשוני. ו-$\varphi(ab)=\varphi(a)\varphi(b)$ רק כשהם זרים: $\varphi(4)=2$ אבל $\varphi(2)\varphi(2)=1$.</div>
    <h3>משפט אוילר</h3>
    <p>אם $\gcd(m,n)=1$ אז $m^{\varphi(n)}\equiv1\pmod n$. פרמה הוא המקרה $n=p$.</p>` },
  questions: [
    { id: "C06-Q1",
      step: { type: "numeric",
        prompt: String.raw`חשבו $\varphi(13)$.`,
        answer: 12, tol: 0,
        explain: String.raw`$13$ ראשוני, ולכן $\varphi(13)=13-1=12$.` },
      recap: String.raw`$\varphi(p)=p-1$.` },
    { id: "C06-Q2",
      step: { type: "numeric",
        prompt: String.raw`חשבו $\varphi(36)$.`,
        answer: 12, tol: 0,
        explain: String.raw`$36=2^2\cdot3^2$, ולכן $\varphi(36)=36\cdot\frac12\cdot\frac23=12$.` },
      recap: "מפרקים לראשוניים ומכפילים בכל $(1-1/p)$." },
    { id: "C06-Q3",
      step: { type: "numeric",
        prompt: String.raw`חשבו $\varphi(100)$.`,
        answer: 40, tol: 0,
        explain: String.raw`$100=2^2\cdot5^2$, ולכן $\varphi(100)=100\cdot\frac12\cdot\frac45=40$.` },
      recap: "כל ראשוני נספר פעם אחת, בלי קשר לחזקה." },
    { id: "C06-Q4",
      step: { type: "numeric",
        prompt: String.raw`חשבו $\varphi(32)\cdot\varphi(9)$. (שני המספרים זרים, ולכן זה בדיוק $\varphi(288)$.)`,
        answer: 96, tol: 0,
        explain: String.raw`$\varphi(32)=2^5-2^4=16$ ו-$\varphi(9)=3^2-3=6$, ולכן המכפלה היא $96$. בדיקה: $288=2^5\cdot3^2$ ו-$288\cdot\frac12\cdot\frac23=96$.` },
      recap: String.raw`$\varphi(p^a)=p^a-p^{a-1}$, ו-$\varphi$ כפלית על זרים.` },
    { id: "C06-Q5",
      question: String.raw`יהיו $p\ne q$ ראשוניים. מהו $\varphi(pq)$?`,
      options: [
        { id: "a", value: "$(p-1)(q-1)$" },
        { id: "b", value: "$pq-1$" },
        { id: "c", value: "$p+q-2$" },
        { id: "d", value: "$(p-1)+(q-1)+1$" },
      ],
      correctId: "a",
      explanation: String.raw`$p$ ו-$q$ זרים, ולכן $\varphi(pq)=\varphi(p)\varphi(q)=(p-1)(q-1)$. למשל $\varphi(15)=2\cdot4=8$. התשובה $pq-1=14$ מתאימה רק לראשוני. $p+q-2=6$ ו-$(p-1)+(q-1)+1=7$ נותנות מספרים אחרים.`,
      recap: String.raw`$\varphi(pq)=(p-1)(q-1)$.` },
    { id: "C06-Q6",
      step: { type: "numeric",
        prompt: String.raw`מהי השארית של $7^{\varphi(10)}$ בחלוקה ב-$10$? ($7$ ו-$10$ זרים.)`,
        answer: 1, tol: 0,
        explain: String.raw`$\varphi(10)=4$, ו-$\gcd(7,10)=1$, ולכן לפי משפט אוילר $7^{4}\equiv1\pmod{10}$. אכן $7^4=2401$.` },
      recap: String.raw`$\gcd(m,n)=1\Rightarrow m^{\varphi(n)}\equiv1\pmod n$.` },
  ],
});
