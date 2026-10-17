# ASK_ADIR - discrete-math-1

Open questions for Adir. One entry per item; the orchestrator moves it to Resolved when answered.

## Open

<!-- Entry format:
### <exam code> Q<number> - <short title>
- Path: <absolute file path>
- Page: <page number>
- Question: <what is unclear or missing>
- Needed: <what Adir must provide or decide>
- Status: hold
-->

### 26A-A Q1b - primality of the given Mersenne number
- Path: tools/raw/26A-A.json
- Page: p.2 (Q1 b)
- Question: the official answer (m is prime) rests on the printed premise that 2^136279841-1 is the largest known prime; the script cannot test that.
- Needed: nothing blocking, FYI only. The answer is kept as printed.
- Status: info

### 26A-A Q4 a(2) - first handwritten line partly unclear
- Path: tools/raw/26A-A.json
- Page: p.8 (Q4 a2)
- Question: the opening line of the handwritten proof is hard to read; it was transcribed as the assumption that A is not a subset of B and B is not a subset of A (the contrapositive).
- Needed: optional glance at the page if exact wording matters.
- Status: info

### 26A-A Q5 - duplicate part label
- Page: p.10-11
- Question: the printed paper labels two parts of Q5 as (b); the second is stored as part c.
- Status: info

### 25A-A Q3 a - official solution omits part (2)
- Path: tools/raw/25A-A.json
- Page: p.5 (Q3 a)
- Question: the official solution proves that R is symmetric and transitive but never answers (2) "is R a partial order?". (Computed: R is reflexive and symmetric, not antisymmetric since 0R5 and 5R0, so not a partial order.)
- Needed: route to the solver (no-key), or approve the computed answer.
- Status: hold

### 25A-A, 25A-B - solution authorship
- Path: tools/raw/25A-A.json, tools/raw/25A-B.json
- Page: pp.2-7
- Question: the solutions are handwritten and typed on the exam pages themselves (typed truth tables in the exam font); they were labelled lecturer-solution on that basis. Coloured "see lecture" notes beside each definition were not transcribed.
- Needed: nothing blocking; FYI.
- Status: info

### 25A-A Q1 c, Q2 a - slips in the handwritten key
- Path: tools/raw/25A-A.json
- Page: p.3 (Q1 c), p.3 (Q2 a)
- Question: the key writes "lcm(3,6)=6=f(3)" (transcribed as f(6)) and ends the induction with "0 <= n" (transcribed as 1 <= n, as printed in the question). Conclusions are unaffected.
- Needed: nothing blocking; FYI.
- Status: info

### 24A-A Q1 c, Q3 c - slips in the typed key
- Path: tools/raw/24A-A.json
- Page: p.3 (Q1 c), p.4 (Q3 c)
- Question: the key writes "f(x1)=f(x1)" (transcribed f(x2)) and "(100^5)^30-1=(10^7)^30-1" where 100^5 = 10^10 (script-checked; transcribed as (10^10)^30). The final answers are unchanged.
- Needed: confirm the corrected lines are acceptable, or tell the orchestrator to hold Q3c.
- Status: info

### 25A-B Q4 b(2) - stray bracket in the printed set
- Path: tools/raw/25A-B.json
- Page: p.6 (Q4 b2)
- Question: the printed B has an unmatched closing bracket "[0,5) U (13,25] ) U (30,75]"; transcribed without it.
- Needed: nothing blocking; FYI.
- Status: info

## Resolved
