# דף נוסחאות ומשפטים לכל הקורס

דף סיכום מהיר. כל סעיף מפנה לפרק המלא.

## לוגיקה ([[logic_propositional]])
- $p\to q\equiv\neg p\vee q\equiv\neg q\to\neg p$. $\neg(p\to q)\equiv p\wedge\neg q$.
- דה-מורגן: $\neg(p\wedge q)\equiv\neg p\vee\neg q$, $\neg(p\vee q)\equiv\neg p\wedge\neg q$.
- DNF: שורות אמת, צירוף ליטרלים כפי שהם. CNF: שורות שקר, פסוקית הפוכה.
- טאוטולוגיה = אמת בכל שורה. שקילות = אותה עמודה.

## כמתים והוכחות ([[quantifiers_proofs]])
- $\neg\forall\equiv\exists\neg$, $\neg\exists\equiv\forall\neg$.
- contrapositive: $(P\to Q)\equiv(\neg Q\to\neg P)$. סתירה: מניחים את השלילה.
- הפרכה = דוגמה נגדית אחת. הוכחת הכלה: "יהי $x\in X$".

## אינדוקציה ([[induction]])
- בסיס ($n=m$), צעד ($P(k)\Rightarrow P(k+1)$ לכל $k\ge m$), מסקנה. חזקה: מניחים את כל $P(m..k)$.
- התחלקות: $a^{k+1}-1=a(a^k-1)+(a-1)$.

## תורת המספרים ([[number_theory_gcd]])
- $a=bq+r$, $0\le r<|b|$. $\gcd(a,b)=\gcd(b,a\bmod b)$.
- Bezout: $\gcd(a,b)=au+bv$ (אוקלידס מורחב). $mn=\gcd(m,n)\operatorname{lcm}(m,n)$.
- אוקלידס: $p\mid ab\Rightarrow p\mid a\vee p\mid b$. פירוק יחיד לראשוניים: $\gcd$ = מינימום מעריכים, $\operatorname{lcm}$ = מקסימום.
- $\varphi(p^k)=p^{k-1}(p-1)$, $\varphi(n)=n\prod_{p\mid n}(1-\frac1p)$, $\varphi(mn)=\varphi(m)\varphi(n)$ כש-$\gcd(m,n)=1$.

## חשבון מודולרי ([[modular_fermat_wilson]])
- $a\equiv b\pmod n\iff n\mid(a-b)\iff$ אותה שארית. אפשר להציב שארית בחיבור ובכפל.
- פרמה: $p$ ראשוני, $p\nmid m\Rightarrow m^{p-1}\equiv1\pmod p$. אוילר: $\gcd(m,n)=1\Rightarrow m^{\varphi(n)}\equiv1\pmod n$.
- וילסון: $n$ ראשוני $\iff(n-1)!\equiv-1\pmod n$.
- $p\mid$ שני הביטויים $\Rightarrow p\le\gcd$.

## קבוצות ([[sets_power_set]])
- $|P(A)|=2^{|A|}$, $|A\times B|=|A||B|$. $|P(A\times B)|=2^{|A||B|}$.
- $P(A)\cup P(B)\subseteq P(A\cup B)$, שוויון $\iff A\subseteq B\vee B\subseteq A$.
- $A-(B\cap C)=(A-B)\cup(A-C)$, $A-(B\cup C)=(A-B)\cap(A-C)$. $A\times(B\cap C)=(A\times B)\cap(A\times C)$.
- תתי-קבוצות של $A$ שמכילות $S\subseteq A$: $2^{|A|-|S|}$.

## עוצמות ([[cardinality_sets]])
- $|\mathbb{N}|=|\mathbb{Z}|=|\mathbb{Q}|=|\mathbb{N}\times\mathbb{N}|=\aleph_0<|\mathbb{R}|=|(0,1)|=\mathfrak{c}$. כל קטע = $\mathfrak{c}$.
- $|A|\le|B|$ אם יש חד-חד-ערכית $A\to B$. קנטור-ברנשטיין: $\le$ בשני הכיוונים נותן $=$. קנטור: $|A|<|P(A)|$.

## יחסים ([[relations_properties]], [[equivalence_relations]], [[partial_orders]])
- רפלקסיבי $(a,a)$; סימטרי; אנטי-סימטרי ($aRb\wedge bRa\Rightarrow a=b$); טרנזיטיבי.
- שקילות = רפלקסיבי+סימטרי+טרנזיטיבי; $A/R$ חלוקה; $|R|=\sum|B_i|^2$. סדר חלקי = רפלקסיבי+אנטי-סימטרי+טרנזיטיבי; מלא = כל זוג ניתן להשוואה.
- שקילות וגם סדר = זהות. שומרים תחת חיתוך: הכל; תחת איחוד: רפלקסיבי וסימטרי בלבד.
- $S(n,1)=S(n,n)=1$, $S(n,k)=S(n-1,k-1)+kS(n-1,k)$. על 3 איברים 5 יחסי שקילות.

## פונקציות ([[functions]])
- חד-חד-ערכית: $f(x)=f(y)\Rightarrow x=y$. על: $f(A)=B$. הפיכה = שתיהן.
- $n^m$ פונקציות $A\to B$ ($|A|=m,|B|=n$); $P(n,m)$ חד-חד-ערכיות; $\binom nm$ עולות ממש; $n!$ הפיכות.
- $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$.

## נסיגות וסכומים ([[recurrence_sums]])
- שורשים שונים: $C_1r_1^n+C_2r_2^n$. כפול: $(C_1+C_2n)r^n$. מרוכבים: $\rho^n(C_1\cos n\theta+C_2\sin n\theta)$.
- פרטי ל-$c\,s^n$: $A\,s^n\,n^k$, כש-$k$ הוא הריבוי של $s$. קבועים מתנאי ההתחלה על הפתרון המלא.
- $\sum k=\frac{n(n+1)}2$, $\sum k^2=\frac{n(n+1)(2n+1)}6$, $\sum_{k=0}^nr^k=\frac{r^{n+1}-1}{r-1}$.

## קומבינטוריקה ([[combinatorics]])
- $n^k$ עם חזרות; $P(n,k)=\frac{n!}{(n-k)!}$; $\binom nk$.
- $(x+y)^n=\sum\binom nkx^ky^{n-k}$; $\sum\binom nk=2^n$; זוגיים $=2^{n-1}$; $\sum k\binom nk=n2^{n-1}$.
- הכלה והדחה. כוכבים וקווים: $x_1+..+x_r=n$, $x_i\ge0$: $\binom{n+r-1}{r-1}$. מורידים את המינימום מראש.
- שובך יונים: $n+1$ פריטים ב-$n$ תאים.

## גרפים ([[graphs_intro]])
- $\sum\deg=2|E|$. משלים: $\binom n2-|E|$ צלעות, דרגה $n-1-\deg$. $\overline{K_{m,n}}=K_m\cup K_n$.
- אוילר: קשיר ודרגות זוגיות; מסלול: שני אי-זוגיים. דיראק: $\deg\ge n/2$ נותן המילטוני. דו-צדדי: אין מעגל אי-זוגי.
