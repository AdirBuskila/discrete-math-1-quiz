# STATUS - discrete-math-1

Resume here: phase 7 - ship (awaiting Adir: gate 2 never ticked by Adir, gate 3 = OK to go public; deck redesign check first)
Opus sessions: 0 of 2
Engine: open   Format: open (computation + proof + true/false)   Cutoff: 2018 (see factory GATE1.md)

Triage material (private, names students, never copied into this repo): C:\Users\Adir\Desktop\Coding\Dev\course-factory\courses\discrete-math-1ormat_triage.md

Gates 1, 2 and 7 always stop for Adir.

- [x] Phase 0 - intake
  - [x] registry entry exists (registry.py list: discrete-math-1 triaged)
  - [x] source folder exists and is non-empty (tools/raw/*-SRC etc. built from it)
- [x] Phase 1 - triage
  - [x] triager run per subfolder (factory courses/discrete-math-1/triage/)
  - [x] format_triage.md merged
  - [x] approved under the autonomy grant (factory GATE1.md); Adir can override
  - [x] config.overlay.json written, app scaffolded
- [ ] Phase 2 - flagship  (GATE 2: Adir tries it in the browser)
  - [x] topic taxonomy chosen (course.config.json topics)
  - [x] flagship sitting transcribed + validated (26A-A, lecturer solution, 15 items, script checks in tools/verify/26A-A)
  - [x] steps + refuter pass (tools/raw/_verify_26A-A.json)
  - [x] verify_dom green (QA run; smoke n/a for open engine)
  - [ ] Adir tried it
- [x] Phase 3 - bank
  - [x] all in-scope sittings transcribed (15 files in tools/raw, 242 questions)
  - [x] validate.py clean (0 problems, QA run)
  - [x] solver run (solved items, official:false)
  - [x] refuter: non-official
  - [x] arbiter / ASK_ADIR (docs/ASK_ADIR.md)
  - [x] completeness check per exam (tools/verify/*/verify.py)
- [x] Phase 4 - steps
  - [x] step-author batches done (813 steps, build_report.md)
  - [x] rubricSource / stepsSource labeled (0 ai-draft stripped)
  - [x] refuter on every steps block (tools/raw/_verify_*.json)
- [x] Phase 5 - learn
  - [x] learn-writer per topic (15 briefs in docs/briefs)
  - [x] coverage report re-checked against 242 questions (docs/learn_coverage.md)
- [x] Phase 5b - need help
  - [x] 4 course areas in course.config.json needHelp
  - [x] lessons + level questions (courses/*/C*.js, 33 levels)
  - [x] course_lint --strict clean, refuter + checkers (tools/verify/needhelp/*)
  - [x] tools/redact.txt filled, validate.py clean
- [x] Phase 6 - QA
  - [x] validate, build_questions, build_learn, verify_dom, verify_learn, course_lint green
  - [x] shoot.js screenshots taken (tools/raw/shots, 390 + 1000, both themes)
  - [x] screenshot sweep read by hand; bidi findings in Notes
- [ ] Phase 7 - ship  (GATE 3: Adir OKs going public)
  - [ ] deck redesign done (else stop and tell Adir)
  - [ ] .gitignore excludes raw PNGs, favicon, GoatCounter, .nojekyll (all four present locally; recheck at ship)
  - [ ] year range checked against data
  - [ ] Adir OK to go public
  - [ ] GitHub repo + Pages live
  - [ ] deck tile added
  - [ ] registry status = live

## Notes
- QA 2026-10-18: 242 questions (118 computation, 120 proof, 4 truefalse, 0 held), 15 learn chapters, 4 guided courses / 33 levels. Open bidi issues: Hebrew-line math ordering, parenthesised question-id chips in learn briefs; Latin option labels fixed by another agent.
