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

### 22A-B Q3a / Q3b / Q1b-c - key slips (FYI)
- Path: tools/raw/22A-B.json
- Page: p.10 (Q3 a, b); p.5 (form 2 Q1 b, c)
- Question: Q3a: the key never answers "is R a partial order" (added from a script, flagged in the text). Q3b: the summary line says f(5)=6, the key's own table gives f(5)=3 (line omitted). Form 2 Q1b: header written gcd(-84,-64), meant -68. Form 2 Q1c: key writes 60 where 6 is meant (6^40 = 6^(41-1)).
- Needed: nothing blocking.
- Status: info

### 22A-A Q3a / Q3b - handwriting slips (FYI)
- Path: tools/raw/22A-A.json
- Page: p.10 (Q3 a), p.11 (Q3 b)
- Question: Q3a symmetry: the key writes 3x+5y=2m-2k where 3y+5x=2m-2k is meant (transcribed as 3y+5x). Q3b f(5): the key shows gcd(2,6)/lcm(2,2) where gcd(2,5)/lcm(2,1) is meant; the value 3 is right.
- Needed: nothing blocking.
- Status: info

### 20A-A - exam-only file is a different version; other key notes (FYI)
- Path: tools/raw/20A-A.json
- Page: exam-only file pp.1-4; part 1 p.3 (Q1 d), part 2 p.6 (Q6 a)
- Question: the exam-only PDF prints different numbers/questions in Q1a, Q1e, Q3c, Q4b, Q5a-b, Q6a-c than the two solution PDFs; the solution PDFs were used as the sitting. Q1d: the key shows only n=2,3,4, nothing for n>=5 (script: only n=4 works for n<=12). Q6a: key writes (1-2/3) where (1-1/3) is meant; the result is right.
- Needed: nothing blocking.
- Status: info

### 18A-A Q3 a - slip in an intermediate line
- Path: tools/raw/18A-A.json
- Page: p.8 (Q3 a3)
- Question: the key writes phi(n)=n(1-1/n)=n*(n-1)/n=n; transcribed as =n-1 (the next line already uses n-1). Final answers unchanged.
- Status: info

### 19A-A Q1 b - final-answer error in the key, corrected
- Path: tools/raw/19A-A.json
- Page: p.5 (Q1 b)
- Question: the key's DNF omits the row p=T,q=F,r=T (it writes r->p = F there; T->T is T). Shipped as "official solution with correction", solutionSource solved, official false (script-checked: three true rows).
- Needed: confirm.
- Status: info

### 19A-A Q1 a2 - printed set braces partly unclear
- Path: tools/raw/19A-A.json
- Page: p.1 (Q1 a2)
- Question: the brace nesting of the printed set is hard to read on the scan (same set appears in 19A-B Q1 a2); transcribed as {{{{empty}}}, P({{{1}},empty}), {{empty}}}. Any plausible reading gives 3 distinct elements, so the key's answer is unaffected.
- Status: info

### 19A-A Q1 c - key's negation wording
- Path: tools/raw/19A-A.json
- Page: p.5 (Q1 c)
- Question: the key's negation is written with an inserted caret; transcribed as for all y in B and all z in C (the printed statement says "exist y in B and z in C").
- Status: info

### 19A-B Q2 a, Q2 b, Q3 b - slips in intermediate lines
- Path: tools/raw/19A-B.json
- Page: p.6 (Q2 a), p.7 (Q2 b), p.10 (Q3 b)
- Question: Q2a writes the inductive step for "k>=2" (printed n>=1; transcribed k>=1). Q2b swaps 7 and 11 in the restated definitions of A and B and titles the last line |P(A cap B)| (the printed set is A cup B); transcribed with the printed definitions. Q3b's first line says |C|=5,|B|=3, while the three cases use the printed |B|=5,|C|=3. Final answers unchanged.
- Status: info

### 19S-A Q2 a - heading range of the induction
- Path: tools/raw/19S-A.json
- Page: p.8 (Q2 a)
- Question: the key's P(n) heading reads "n>=2" while the printed claim and the conclusion use n>=1; transcribed with n>=1.
- Status: info

### 18A-A, 19A-A, 19A-B, 19S-A - solution authorship
- Path: tools/raw/18A-A.json, 19A-A.json, 19A-B.json, 19S-A.json
- Page: pp.3-18
- Question: all four keys are handwritten, no author printed (19A-A's is titled with the date 3.3.19; 19S-A is in blue ink); labelled student-solution, official false, confidence med. 19A-A has no printed exam date (taken from the key title); 19A-B has none (only the year).
- Needed: nothing blocking; FYI.
- Status: info

### 18A-B Q4 c - key counts letter-count vectors, not words (shipped with correction label)
- Path: tools/raw/18A-B.json
- Page: p.11 (Q4 c)
- Question: the key answers 495 = C(12,4), the number of vectors (x1..x4) with sum <= 22 and the lower bounds, i.e. words up to letter order. The printed question asks for words of length at most 22; the number of words is 10726916243718 (script-checked, two methods). Shipped as solved, official false, with the correction prefix. Same pattern as 18A-A Q4 c (now shipped the same way).
- Needed: nothing blocking; confirm the intended reading if you know it.
- Status: info

### 18A-B, 18B-A - slips and gaps in the keys
- Path: tools/raw/18A-B.json, tools/raw/18B-A.json
- Page: p.4 (18A-B Q2 a), p.8 (18A-B Q3 a 4), p.5 (18B-A Q2 b 2), p.3 (18B-A Q1 c)
- Question: 18A-B Q2a writes "3(k+1)^2+4(k+1)=1" for "+1" and an extra "+4k+5" line; transcribed with the correct lines, final answer unchanged. 18A-B Q3a(4) answers B={2,3}; any B={2,p} with p an odd prime also works (the key gives one example). 18B-A Q2b(2) never mentions n=0 (a_0=0 is not prime); transcribed as in the key. 18B-A Q1c negates "exists x in A or exists y in B" as "for all x and all y" (same convention as 18A-A and 19A-A).
- Status: info

### 18A-B, 18B-A - cover page and authorship
- Path: tools/raw/18A-B.json, tools/raw/18B-A.json
- Page: p.1, pp.3-11
- Question: the 18B-A cover (08.07.2018) reads "semester A, moed B" (a copy of the March cover); labelled semester B, moed A by the date and folder. Both keys are handwritten with no author (18B-A in blue ink): student-solution, official false, confidence med.
- Status: info

## Resolved

### 25A-A Q3 a - official solution omits part (2)
- Path: tools/raw/25A-A.json
- Page: p.5 (Q3 a)
- Question: the official solution proves that R is symmetric and transitive but never answers (2) "is R a partial order?". (Computed: R is reflexive and symmetric, not antisymmetric since 0R5 and 5R0, so not a partial order.)
- Needed: route to the solver (no-key), or approve the computed answer.
- Status: resolved (2026-10-17)
- Ruling: solver: shipped solved, official false; (1) transcribed from the key (its transitivity line 5(k+q-2) fixed to 5(k+q-2b), slip), (2) added: not a partial order (0R5, 5R0). verify.py asserts.

### 22A-B Q6b (form 2 Q2b) - printed key disagrees with its own computation
- Path: tools/raw/22A-B.json
- Page: p.8 (form 2 Q2 b)
- Question: the key ends with "232 + 2^1210"; the expression is |A u B| + |P(AxB)| + |P(A-B)|, which is 121 + 2^1210 + 2^111 (script-checked).
- Needed: confirm the intended answer.
- Status: resolved (2026-10-17)
- Ruling: standing typo rule: shipped 121 + 2^1210 + 2^111 with the correction prefix (key put |A-B|=111 where |P(A-B)|=2^111 belongs), solved, official false. verify.py asserts.

### 22A-B Q7a (form 2 Q3a) - no key
- Path: tools/raw/22A-B.json
- Page: p.11 (form 2 Q3 a)
- Question: the key covers form 1 only (9x+5y); form 2 uses 3x+7y and has no solution.
- Needed: nothing, route to the solver.
- Status: resolved (2026-10-17)
- Ruling: solver: full solution written for 3x+7y (equivalence, Z/R = {evens, odds}, not a partial order: 0R2, 2R0), solved, official false. verify.py asserts.

### 22A-A Q6b (form 2 Q2b) - printed key disagrees with its own sizes
- Path: tools/raw/22A-A.json
- Page: p.9 (form 2 Q2 b)
- Question: the key writes |A|*|B| = 300*300 = 90000, but |A|=|B|=900 (it also writes |A-B| = 30*30-30 = 870). Expected 870 + 2^810000 + 2^30 (script-checked); the key gives 870 + 2^90000 + 2^30.
- Needed: confirm the intended answer.
- Status: resolved (2026-10-17)
- Ruling: standing typo rule: shipped 870 + 2^810000 + 2^30 with the prefix naming 300*300 -> 900*900, solved, official false. verify.py asserts.

### 22A-A Q7a (form 2 Q3a) - key says only "same as form 1"
- Path: tools/raw/22A-A.json
- Page: p.12 (form 2 Q3 a)
- Question: form 2 uses 3x+7y; the key only says it is like form 1 and gives no worked answer.
- Needed: nothing, route to the solver.
- Status: resolved (2026-10-17)
- Ruling: solver: derived for form 2's 3x+7y (equivalence, two classes, not a partial order: 1R3, 3R1), solved, official false. verify.py asserts.

### 20A-A Q2a - key arithmetic slip
- Path: tools/raw/20A-A.json
- Page: part 1 p.5 (Q2 a)
- Question: (1) 720 = 3!*5! is right. (2) the key writes C(7,2)*5! = 7!/2 = 2560, but both equal 2520.
- Needed: confirm 2520 is the intended answer.
- Status: resolved (2026-10-17)
- Ruling: standing typo rule: shipped (1) 720, (2) 2520 with the prefix naming 2560 -> 2520, solved, official false. verify.py brute-forces S7.

### 20A-A Q2b - key answers (1) as if letters cannot repeat
- Path: tools/raw/20A-A.json
- Page: part 1 pp.5-6 (Q2 b)
- Question: (1) asks for 7-letter sequences, first 4 letters from A and the rest from B; the key answers 144 = 3!*4! (each letter once). Part (2) then adds "every letter appears once", so (1) seems to allow repeats (4^4*3^3 = 6912). (2) = 72 matches the key.
- Needed: which reading is intended.
- Status: resolved (2026-10-17)
- Ruling: arbiter: read on the page (part 1 pp.5-6). A course 'sequence' allows repeats (a permutation is defined as a sequence without repeats) and (2) adds 'each letter appears once' as a new condition on sequences from (1), so the printed wording supports repeats in (1). Keyed 4^4*3^3 = 6912 with the correction prefix; the key's no-repeat reading (144) is solved alongside; (2) = 72 under both readings. Solved, official false. verify.py brute-forces both. Override if the lecturer meant no repeats.

### 20A-A Q2c - key's formula for phi(n) is not valid
- Path: tools/raw/20A-A.json
- Page: part 1 p.6 (Q2 c)
- Question: (1) phi(1)=1=phi(2) is fine. In (2) the key writes phi(n) = 3^a 5^b m (1-1/3)(1-1/5) phi(m), which has stray factors m and phi(m); the last line 2*4*3^(a-1)*5^(b-1)*phi(m) and the claim 8 | phi(n) are right.
- Needed: nothing blocking; decide whether to ship with a corrected derivation or send to the solver.
- Status: resolved (2026-10-17)
- Ruling: intermediate slip, fixed silently: the line is transcribed as phi(n) = 3^a(1-1/3)*5^b(1-1/5)*phi(m) = 2*4*3^(a-1)*5^(b-1)*phi(m); final answer unchanged, stays student-solution. verify.py asserts the identity for n = 15..5985.

### 18A-A Q4 c - key counts letter-count vectors, not words
- Path: tools/raw/18A-A.json
- Page: p.4 (printed), p.12 (key)
- Question: the printed question asks how many 25-letter words over {a,b,c,d} contain a at least 4 times, b at least 3, c at least 5, d at least 2. The key answers C(14,3)=364, which counts only the letter-count vectors. The number of words is 746544967234440 (script-checked).
- Needed: decide whether to ship the printed question with the computed word count (solved) or keep it held.
- Status: resolved (2026-10-17)
- Ruling: standing typo rule, same as 18A-B Q4c: shipped 746544967234440 words with the correction prefix, keeping the key's 364 as the letter-count-vector step; solved, official false. verify.py checks two methods (multinomial sum, EGF).

### 19A-A Q3 b2 - formula double counts at n=8
- Path: tools/raw/19A-A.json
- Page: p.9 (Q3 b)
- Question: the key's C(n,2)*C(n-2,3) is right for n>=9; at n=8 the remaining block also has 3 elements and every relation is counted twice (280 vs 560, script-checked). Shipped as printed in the key with a visible note. The key also labels its two answers (1b)/(2b) in swapped order; matched by content.
- Needed: nothing blocking.
- Status: resolved (2026-10-17)
- Ruling: converted from a note to the standing typo rule: prefix names the n=8 correction (280, not 560); answer C(n,2)C(n-2,3) for n>=9, 280 for n=8; solved, official false. verify.py counts distinct relations for n=8,9,10.

### 23A-B Q1c - key swaps the coordinates of f(m,n)
- Path: tools/raw/23A-B.json
- Page: Q1 c (key)
- Question: f(m,n)=2^n(2m+1), but the key writes f(alpha_1,m)=q and f(0,m)=q; the preimages are (m,alpha_1) and (m,0).
- Needed: nothing, final claim (f is onto) is unaffected.
- Status: resolved (2026-10-18)
- Ruling: intermediate slip, fixed silently in the solution and the rubric (f(m,alpha_1), f(m,0)); stays lecturer-solution, official. verify.py checks the preimages by brute force.

### 20A-A Q1a, Q1c, Q3c, Q4b, Q5a, Q5c, Q6a, Q6b - the keys answer a different version than the printed exam
- Path: tools/raw/20A-A.json
- Page: exam-only file tools/raw/20A-A-ex pp.1-4 versus the handwritten keys (20A-A-p1, 20A-A-p2)
- Question: the keys answer other numbers than the printed exam (Q1a permutations vs 4-subsets containing 1,2; Q1c edge count vs bipartite complement; Q3c P_15 vs all n; Q4b strictly increasing/injective {1..4}->{1..6} vs increasing/onto {1..6}->{1..4}; Q5a 9-entry vs 8-entry degree sequence; Q5c has a 4th part (isomorphism); Q6b other intervals). Q5b and Q6a/Q6b point values also follow the print (8, 11, 8).
- Needed: nothing blocking.
- Status: resolved (2026-10-18)
- Ruling: the printed exam wins. Question text re-transcribed from the print; each item re-solved by script (brute force / networkx-free graph checks), solutionSource solved, official false. Conventions chosen: Q3c takes n>=2 and a path with exactly 2 odd vertices (the inclusive reading gives the same n); Q4b reads "עולה" as non-decreasing (strictly increasing is impossible from 6 to 4 elements); Q6a does not print the domain of n, so n>=1 is added to the text and noted in the solution; Q5c(4) is 3 points as printed (2+3+3+3 read left to right).

### 20A-A Q2c step 0, step order and 2c/other steps
- Status: resolved (2026-10-18)
- Ruling: step 0 explanation rewritten (phi(3)=phi(4)=phi(6)=2 also coincide; the options are checkably different); the borderline order step merged into 3 blocks. Intermediate steps only, no student-facing label.
