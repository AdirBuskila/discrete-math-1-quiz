# Learn-mode coverage (discrete-math-1)

Built from the question text and solutions in `tools/raw/*.json` (242 shipped questions; re-checked against the full bank in QA). Brief files are in `docs/briefs/`.

| Concept | Brief section | Example question ids |
|---|---|---|
| Truth table, logical equivalence, tautology, contradiction | 01 logic_propositional: definitions, recipes | 24A-A-Q1a, 23A-B-Q1a, 25A-A-Q1a, 26A-A-Q1a, 22A-B-Q1a, 19A-A-Q1a |
| DNF and CNF from a truth table | 01: recipes | 24A-A-Q4b, 19A-B-Q1f, 23A-A-Q1a, 25A-B-Q1a, 22A-A-Q1a, 22A-A-Q5a |
| Compound proposition, definitions with examples | 01: definitions | 19A-B-Q1a |
| Negating quantifiers without a negation symbol | 02 quantifiers_proofs: recipes | 18A-A-Q1c, 19A-A-Q1g, 19A-B-Q1g |
| Contrapositive proof, proof by contradiction, counterexample | 02: definitions, recipes | 24A-A-Q3b, 25A-A-Q2b, 25A-B-Q4a, 26A-A-Q1b |
| Induction: sum identities | 03 induction: recipe, sums | 18A-A-Q2a, 24A-A-Q2a, 19A-B-Q2a, 22A-A-Q2a, 22A-A-Q6a, 23A-B-Q2a, 25A-A-Q2a, 26A-A-Q2a |
| Induction: inequalities with a later base | 03: recipe, inequalities | 19A-A-Q2a, 23A-A-Q2a, 22A-B-Q2a, 22A-B-Q6a |
| Induction: divisibility | 03: recipe, worked example | 25A-B-Q2a |
| Divisibility, remainder, Euclid, extended Euclid, Bezout | 04 number_theory_gcd: definitions, recipe table | 22A-A-Q1b, 22A-A-Q5b, 22A-B-Q1b, 22A-B-Q5b, 23A-A-Q2b, 23A-B-Q2b, 24A-A-Q2b, 25A-A-Q3b, 25A-B-Q3b, 26A-A-Q3b |
| gcd/lcm of expressions, gcd times lcm | 04: definitions, recipes | 23A-A-Q4b, 23A-B-Q4b |
| Primes, factoring to show non-primality | 04: recipes | 24A-A-Q4c, 25A-A-Q4b, 26A-A-Q4c, 26A-A-Q1b |
| Irrationality by contradiction, unique factorization | 04: recipes | 25A-A-Q2b, 25A-B-Q4a |
| Pigeonhole with remainders | 04: recipes, 13 combinatorics | 19A-A-Q5a |
| Euler phi, parity of phi | 04: definitions, traps; 05 | 19A-B-Q5a, 19A-B-Q5b, 20A-A-Q1b, 20A-A-Q6a, 18A-A-Q3a, 19A-B-Q4e |
| Congruence arithmetic, Fermat, Wilson | 05 modular_fermat_wilson | 22A-A-Q1c, 22A-A-Q5c, 22A-B-Q1c, 22A-B-Q5c, 23A-A-Q3c, 23A-B-Q3c, 24A-A-Q3c, 25A-A-Q1b, 25A-B-Q4b, 26A-A-Q5a, 19A-A-Q4e |
| Set identities, double inclusion, De Morgan | 06 sets_power_set | 24A-A-Q3a, 25A-A-Q3c, 25A-B-Q3c, 26A-A-Q3c, 23A-A-Q3a, 23A-B-Q3a, 19A-B-Q2d |
| Power set and its size, Cartesian product size | 06 | 19A-A-Q1b, 19A-B-Q1b, 24A-A-Q1b, 22A-A-Q2b, 22A-B-Q2b, 23A-B-Q3b, 19A-B-Q2b, 19A-A-Q2b |
| P(A) union P(B) vs P(A union B), contrapositive of set claims | 06 | 19A-A-Q2c, 25A-A-Q4a, 26A-A-Q4a, 22A-A-Q2c, 22A-B-Q2c, 25A-B-Q4c |
| Counting subsets with conditions | 06, 13 | 25A-B-Q1b, 26A-A-Q2b, 22A-A-Q4b, 22A-B-Q4b, 23A-B-Q4c, 19A-A-Q4d, 23A-A-Q4c |
| Cardinality: countable, continuum, Cantor-Bernstein | 07 cardinality_sets | 22A-A-Q4a, 22A-B-Q4a, 20A-A-Q6b, 25A-A-Q4c, 26A-A-Q5c, 19A-A-Q5b, 19A-B-Q5c, 18A-A-Q1b |
| Reflexive, symmetric, antisymmetric, transitive; closure under union, intersection, inverse | 08 relations_properties | 18A-A-Q2b, 23A-A-Q1b, 22A-B-Q3c, 22A-B-Q7c, 25A-A-Q2c, 26A-A-Q2c, 19A-B-Q1c |
| Proving a relation is an equivalence, finding Z/R | 09 equivalence_relations: recipes | 18A-A-Q2c, 19A-A-Q3a, 19A-B-Q3a, 22A-A-Q3a, 22A-B-Q3a, 23A-A-Q4a, 23A-B-Q4a, 24A-A-Q4a, 26A-A-Q3a |
| Partitions vs equivalence relations, size of R, Stirling and Bell numbers | 09: definitions | 19A-B-Q4c, 23A-A-Q2c, 19A-A-Q3b, 19A-B-Q3b, 19A-A-Q1c, 19A-A-Q3c |
| Equivalence plus order is the identity; union and intersection of equivalences | 09, 08 | 23A-B-Q1b, 26A-A-Q1c, 25A-B-Q2c, 24A-A-Q2c |
| Partial and total orders, max and min | 10 partial_orders | 19A-A-Q1d, 19A-B-Q1d, 19A-A-Q3d, 22A-A-Q3c, 22A-A-Q7c, 23A-B-Q2c, 25A-B-Q3a, 19A-B-Q4d |
| Injective, surjective, bijective; proofs and image | 11 functions | 24A-A-Q1c, 26A-A-Q5b, 23A-A-Q1c, 18A-A-Q1a, 22A-A-Q3b, 22A-B-Q3b, 25A-A-Q1c, 25A-B-Q1c, 26A-A-Q4b |
| Counting functions (all, injective, increasing, bijective), relations that are functions | 11, 13 | 19A-A-Q1e, 19A-B-Q1e, 19A-B-Q4a, 19A-A-Q4c, 19A-B-Q4b, 20A-A-Q4b |
| Linear recurrences: characteristic equation, double root, complex roots, particular solution | 12 recurrence_sums | 18A-A-Q3b, 19A-A-Q5c, 19A-B-Q5d, 20A-A-Q3b |
| Product, permutations, combinations, gluing | 13 combinatorics | 18A-A-Q4b, 20A-A-Q1a |
| Inclusion-exclusion | 13 | 20A-A-Q3a |
| Stars and bars with minimum counts | 13 | 20A-A-Q5b |
| Binomial theorem sums, even subsets, sum of sizes, big-O | 13 | 18A-A-Q4a, 19A-B-Q3c, 20A-A-Q4a, 20A-A-Q4c |
| Complement graph, degrees, Euler, Hamilton (Dirac), bipartite, diameter, degree sequences | 14 graphs_intro | 20A-A-Q1c, 20A-A-Q1d, 20A-A-Q3c, 20A-A-Q5a, 20A-A-Q5c, 20A-A-Q6c |
| Derangements, 1-before-2 in permutations | 13 combinatorics: recipes | 18A-B-Q1a, 20A-A-Q2a |
| Symmetric difference identities | 06: recipes | 19S-A-Q1b, 19S-A-Q1c |
| Fibonacci closed form (irrational roots) | 12: definitions | 19S-A-Q5c |
| Course-wide formula and theorem sheet | 15 cheat | all |

## Gaps
- No gap remains for a concept used by a shipped question, except as listed below.
- `20A-A-Q5c` and `20A-A-Q6c` rely on a figure of a specific graph. The brief teaches the method (degrees in the complement, Dirac, odd cycle, distance from extreme vertices) but cannot give the figure's numbers.
- `20A-A-Q5a` (degree sequence): taught as the "remove the largest-degree vertex" argument in 14, not as a named theorem (the sources do not name one).
- Questions that are held out of the bank (18A-A-Q4c, 20A-A-Q2, 22A-A-Q6b, 22A-A-Q7a, 22A-B-Q6b and 22A-B-Q7a, 25A-A-Q3a) are not linked by id. Their topics (counting words with minimum letter counts, adjacency in permutations, set counts, equivalence relations mod a prime) are covered by 13, 06 and 09.
- The class notes and the summary PDFs of the sources have a broken text layer (Hebrew does not extract), so the briefs rely on the formula sheet, the practice set structure and the exam solutions for terminology. The Notes screenshots (divisibility, primes) were not re-typed.

## Thin topics
- graphs_intro (one exam only, method-level), recurrence_sums (four questions, no steps), quantifiers_proofs (four questions).
