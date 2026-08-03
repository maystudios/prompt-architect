# PRE-EMIT LINT CHECKLIST

Two gates. Run the deterministic one, then read the prompt cold as its executor.

## Gate 1 — the script

Write the prompt body to a file and run it:

```
python scripts/lint_prompt.py PROMPT_FILE --budget standard
python scripts/lint_prompt.py PROMPT_FILE --budget compact
python scripts/lint_prompt.py PROMPT_FILE --budget 6000
python scripts/lint_prompt.py PROMPT_FILE --phased        # PHASE-structured variant
```

**Errors — these block emission:**
character count over the budget ceiling · a required section missing or out of canonical order · a duplicate or empty section · any placeholder, angle-bracket slot or surviving `{{…}}` template slot · both bridge names in MODEL ROUTING · a missing Fable prohibition · a missing paid-latency prohibition · a missing English instruction in SETUP · a missing git end-state clause where SETUP has not declared the project unversioned · a missing evidence rule.

**Warnings — these need a reason, not a fix:**
length under the standard floor · a nested `##` heading · a heading that is not UPPERCASE · a FIRST ACTION that does not obviously persist the brief · a missing git clause where SETUP *has* declared no repository.

**What the script does not check**, so Gate 2 must: that a rail is actually present (it only rejects both bridges named together) · that the emitted rail matches the host the user chose · whether a DoD clause is genuinely checkable · whether the mission is unambiguous.

Never estimate the character count — the whole reason the script exists is that models cannot count. Note that it reports both body length and fenced length; compact is budgeted against the **body** ceiling of 3,950 so the fenced form still clears 4,000.

## Gate 2 — read it cold

The script cannot judge these. You have to.

**Coherence**
- Do MISSION, SCOPE, TESTING and DEFINITION OF DONE agree? Walk each mission requirement to its DoD clause and back.
- Could this prompt describe two different jobs? If yes, MISSION is not finished.
- Does anything contradict anything? Pass counts, autonomy, branch names, quality bars — these drift when sections are compiled independently.

**Evidence**
- Does every mandatory claim have an observable gate?
- Is there a DoD clause you could not check? Rewrite it or cut it.
- Is there an instruction the agent could satisfy without doing the work?

**Honesty**
- Is any capability asserted as present that was never verified? Plugins, MCP servers, bridges, CLIs — each needs either confirmation or a discovery step with a fallback.
- Are prices or model rosters stated? Then the date and the re-verify note travel with them.
- Does the prompt promise something the environment cannot deliver?

**Scope**
- Does the prompt ask its recipient to do anything outside SCOPE? Check the DoD and the test matrix especially — they leak.
- Did a domain module drag in its whole discipline where one slice was needed?
- Is there a second-brain mandate on a project with no second brain?

**Self-containment**
- Does anything assume knowledge from this conversation? Inline it.
- Are all paths, branches, commands and file names real and current? Read them from the repository, do not guess.
- Would a fresh agent know where to start, and how it will know it finished?

**Style**
- Any hedging left? "Consider", "try to", "if possible", "ideally".
- Any untranslated prestige adjective?
- Any section that repeats another?
- Bold used to carry the argument, or sprayed?

## Common failures, in order of frequency

1. **A DoD clause with no evidence.** "Code is clean." Rewrite with what you would look at.
2. **A vague mission that reads fine until you ask which two jobs it could mean.**
3. **Placeholders that survived** because the value was one `git branch` call away.
4. **Both rails emitted**, or a rail the user did not choose.
5. **A test matrix wider than the scope** — verification for surfaces the mission never touches.
6. **Repetition between WORKING METHOD and the domain module.** They overlap by design; deduplicate deliberately.
7. **A conditional section emitted because the shape looked incomplete without it.** Empty ceremony costs characters and credibility.
8. **The git end-state clause dropped under length pressure.** It is on the never-cut list.
