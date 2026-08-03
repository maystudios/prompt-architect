# RULE 09 — VOICE, FORMATTING AND LENGTH

## 1. Voice

**Decisive imperative.** "Do X." Never "you should do X", "consider doing X", "it may be helpful to X", "try to X". If it is worth writing, it is worth commanding.

- **Concrete verbs, named artifacts.** `L_Showcase`, `flutter analyze`, `feat/checkout-rework`, `docs/product-direction.md`. A prompt full of "the relevant files" instructs nobody.
- **Contrast clauses kill failure modes.** They are the highest-value sentence type in this style. Build them task-specifically: *screenshot or it did not happen* · *direction, not blueprint* · *a coherent result that reads like the reference beats a faithful copy of a flawed drawing* · *no batching twenty edits and one screenshot at the end* · *that judgement is the work; the geometry is the consequence*.
- **Translate every prestige adjective.** "AAA", "production-ready", "intuitive", "native", "clean", "robust", "polished" carry no instruction. Replace each with the observable property, or delete it. When the user used one, translate it and keep their word beside the translation so they recognise their own brief.
- **Numbers over adjectives.** "under 200 ms at final data volume" beats "fast". "4 orbit angles in 45° steps" beats "several angles".
- **Arrow chains for loops:** `change → save → capture → look → one line of critique → fix or explicitly accept → commit`.
- **Em dash for the sharp turn** — the clause that flips the expectation. Do not scatter them.
- **Short paragraphs. Specific bullets.** No paragraph over four lines.
- **State prohibitions explicitly** where they prevent a known failure. "No stubs, no mocks, no TODO later" is worth its characters.

**Never:** hedging, throat-clearing, "as you know", restating the brief back, meta-commentary about the prompt itself, apologising for length.

## 2. Formatting

**Headings.** Flat, single level, `# UPPERCASE`. An em-dash qualifier is house style where it carries meaning:

```
# WORKING METHOD (mandatory)
# REFERENCES — DIRECTION, NOT BLUEPRINT
# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
# MODEL ROUTING & PARALLELISM
```

Never `##` or deeper. Sub-structure comes from bold lead-ins and bullets. The flat heading set is what makes these documents scannable at a glance, and nesting destroys it.

**Bold.** Bold the load-bearing phrase at the **start** of a bullet, where the bullet has one. Roughly one in three to one in five bullets — enough that the eye can skim the section and get the argument, sparse enough that bold still means something. Never bold two consecutive bullets in full. Never bold a whole sentence.

**Numbered lists** for ordered procedure. **Bullets** for everything else. **Tables** only where there are genuinely three or more columns of parallel data; a table with two columns is a bullet list wearing a costume.

**Inline code** for every path, command, branch, identifier, file and flag. Always.

## 3. Length budgets

Ask for the budget in the Frame round when it is in play. Default is standard.

### Standard — 10,000 to 15,000 characters

| Section | Target chars |
|---|---|
| SETUP | 500 |
| MISSION | 1,600 |
| SOURCE OF TRUTH / REFERENCES | 1,000 |
| SCOPE | 700 |
| FIRST ACTION | 700 |
| WORKING METHOD | 1,600 |
| Domain modules (0–2) | 2,500 |
| TESTING & VERIFICATION | 1,500 |
| SECOND BRAIN / RESEARCH | 1,000 |
| MODEL ROUTING & PARALLELISM | 1,300 |
| SELF-IMPROVEMENT — BOUNDED | 900 |
| DEFINITION OF DONE | 1,400 |

Required sections alone land near 10,200. With conditionals and domain modules, near 14,700. That is the band, and it falls out of the structure rather than being padded to.

### Compact — body ceiling 3,950

Some Claude Code fields will not accept more than 4,000 characters. **The body ceiling is 3,950, not 4,000**, because the prompt is emitted inside a fenced code block: ` ```markdown ` plus the closing fence costs 16 characters, and a user who copies the block *with* its fences must still land under 4,000. Verified by the script — never estimated.

These numbers are **measured from the compact prompt in `references/worked-examples.md`**, which sits at 3,939 body / 3,955 fenced. There is no slack. Nine sections plus a rail block genuinely fill the budget, and a first draft lands near 4,600.

| Section | Measured chars |
|---|---|
| SETUP | 320 |
| MISSION | 440 |
| SCOPE | 270 |
| FIRST ACTION | 235 |
| WORKING METHOD | 590 |
| TESTING & VERIFICATION | 450 |
| MODEL ROUTING & PARALLELISM | 480 |
| SELF-IMPROVEMENT — BOUNDED | 400 |
| DEFINITION OF DONE | 520 |
| Headings and whitespace | 190 |

**WORKING METHOD is where compact prompts overrun.** It carries the role, the loop, the decomposition doctrine and the escalation ladder. It is the first place to cut, and the escalation ladder compresses to a single clause — *on a stall, re-cut the task before escalating the model* — before anything else goes.

**Compact rules:**
- All nine required sections still appear. The structure is not what gets cut.
- **A conditional section does not fit.** The compact `SECOND BRAIN / RESEARCH` form in `rules/05-second-brain.md` §8 alone is roughly 750 characters — 19% of the whole budget — and no required section can donate that. If the task genuinely needs a conditional section, **say so and offer the user 4,700 instead of 4,000**. Do not quietly amputate a required section to make room.
- Domain knowledge is compressed into WORKING METHOD and DEFINITION OF DONE rather than getting its own section.
- Use the compact rail form from the rail file.

### Custom

The user may name any figure. Interpolate: scale the standard table proportionally above 4,000, use the compact table below it. Under 2,000 characters, say plainly that the nine sections will be one line each and confirm that is what they want.

### Below the standard floor

A small, single-surface, low-risk task legitimately compiles to under 10,000 characters, and the script warns rather than errors there. **Answer the warning with one sentence in the preamble** — "this is a two-file change, so the prompt is proportionally short". Do not pad it, and do not add a conditional section to reach the floor: padding violates §1 and a ceremonial section is failure #7 in `references/lint-checklist.md`.

## 4. Compression ladder

Cut in this order. Stop as soon as you are under budget.

1. **Repetition across sections.** Say it once, in the section that owns it. This alone usually recovers 15%.
2. **Justification.** Keep the instruction, drop the "because" — except where the reason prevents a predictable rationalisation, like the English-language rule.
3. **Examples.** Keep the one that disambiguates. Cut the rest.
4. **Context that is not scope.**
5. **Priority-order clauses** in MISSION, when nothing actually competes.
6. **Conditional sections**, lowest value first.
7. **Domain module depth.** Keep the failure modes and the DoD clauses; drop the work sequence into WORKING METHOD.
8. **Routing detail** down to the compact rail form.

## 5. Never cut, at any budget

- The MISSION end-state definition.
- The named verification gates.
- The git end-state DoD clause — unless SETUP declares the project has no version control, per `rules/08` §2a.
- The evidence rule — *never report a result you have not observed*.
- The hard routing rules — no Fable, no paid latency tier.
- The working-language instruction in SETUP.
- The FIRST ACTION persistence instruction.

If the budget cannot hold these, the budget is wrong. Say so rather than dropping one.

## 6. Self-check before emitting

Read the compiled prompt once as the executing agent would, cold:

- Could this describe two different jobs? Fix MISSION.
- Is there a requirement with no evidence attached? Fix DEFINITION OF DONE.
- Is there an instruction I could satisfy without doing the work? Fix the gate.
- Does any section repeat another? Cut one.
- Does anything here assume knowledge from the conversation? Inline it.

Then run `scripts/lint_prompt.py`. A model cannot count characters reliably; the script can.
