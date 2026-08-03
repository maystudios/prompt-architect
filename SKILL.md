---
name: prompt-architect
description: Compile a task brief into one standalone, copy-ready execution prompt for another agent — house structure (SETUP / MISSION / SCOPE / FIRST ACTION / WORKING METHOD / TESTING & VERIFICATION / MODEL ROUTING & PARALLELISM / SELF-IMPROVEMENT / DEFINITION OF DONE), always in English, with exactly one routing rail matched to the executing host. Use when the user asks to build, write, design, generate, sharpen, shorten or compile a prompt, brief, mission, agent instruction set or execution plan for an AI agent — "bau mir ein Prompt", "erstelle einen Prompt für", "schreib mir einen Auftrag für den Agent", "write me a prompt to", "turn this into a brief". Generates the prompt only; never executes it.
---

# Prompt Architect

Compile a task brief into **one standalone execution prompt** for another agent, in the house structure and voice.

## The three invariants

1. **Generate, never execute.** You produce prompt text. You do not start the work it describes, do not create the branch it names, do not implement the feature it specifies. Reading the repository to *inform* the prompt is expected. Doing the job is not. If the user wants execution, they run the prompt afterwards — say so and stop.
2. **The artifact is always English.** Talk to the user in the user's language. Ask questions in the user's language. The emitted prompt is English, and it instructs its executor to work in English. Reason: English costs fewer tokens per unit of meaning, and the whole downstream run pays that tax.
3. **No placeholders.** Never emit `<slot>`, `TODO`, `path/to/file`, or any bracket the reader must fill. If a value is unknown, ask for it in the Frame round or infer it and say which. A prompt with a hole in it is not copy-ready.

## Pipeline

Run these in order. Each step names the rule file that governs it.

| # | Step | Governed by |
|---|---|---|
| 1 | **Parse** the brief: facts, constraints, artifacts, prohibitions, quality bar | `rules/01-intake.md` |
| 2 | **Classify** the task: domain, shape, autonomy, subjectivity, size, risk, environment | `rules/01-intake.md` |
| 3 | **Interrogate** the task — branch the decomposition before writing anything | `rules/02-thinking.md` |
| 4 | **Frame round** — one batched question call, ≤4 questions | `rules/01-intake.md` |
| 5 | **Assumption round** — only if material gaps remain, ≤3 questions | `rules/01-intake.md` |
| 6 | **Select** sections, rail, and domain profiles | `rules/03-sections.md` |
| 7 | **Compile** to the house structure at the chosen length budget | `rules/09-style-and-length.md` |
| 8 | **Lint** — deterministically, with the script | `references/lint-checklist.md` |
| 9 | **Emit** — assumptions above, prompt inside one code block | below |

## Rule map — load on demand

Do not load everything. Load what the task actually touches.

**Always:**
- `rules/00-core-contract.md` — what the skill is, output contract, prohibitions
- `rules/01-intake.md` — gap classification and the question protocol
- `rules/02-thinking.md` — task interrogation and decomposition doctrine
- `rules/03-sections.md` — the section catalog: presence, contents, activation
- `rules/06-verification.md` — the test matrix (Lane 1 applies to all work; blind lanes 2–4 load only for subjective outcomes)
- `rules/07-self-improvement.md` — 0–2 passes is a required section
- `rules/08-git-and-done.md` — the git end-state clause is required in every Definition of Done where a repository exists
- `rules/09-style-and-length.md` — voice, formatting, length budgets, compression ladder

**Model routing — always the core, plus exactly one rail:**
- `rules/04-model-routing.md` — rail-independent core, parallelism economics, test-time compute
- `rules/rails/claude-code.md` — emit when the executing host is Claude Code
- `rules/rails/codex.md` — emit when the executing host is Codex

**Conditional:**
- `rules/05-second-brain.md` — when a knowledge base exists, or the task is knowledge-heavy, or current facts matter
- `rules/domains/*.md` — load the 0–2 profiles the task actually falls into, never more. The classification-to-filename mapping is in `rules/03-sections.md`.

**References:**
- `references/prompt-template.md` — the skeleton and section order
- `references/worked-examples.md` — one standard-length and one compact compiled prompt
- `references/lint-checklist.md` — the pre-emit gate
- `scripts/lint_prompt.py` — deterministic character count and structure check

## The Frame round — one call, ≤4 questions

Ask these together in a single `AskUserQuestion` call. Never ask them one at a time. Skip any the user already answered.

1. **Execution host** — Claude Code or Codex. Pre-select the detected host, but ask: the prompt may be written for the other one. This decides which rail is emitted. **Exactly one rail ever appears in the output.**
2. **Git landing** — which branch the finished work must end on. Offer the repository's real branch names: the current branch, a new branch off the current one, a new branch off the base branch. Never leave this to chance. **If there is no repository, drop this slot**, state in SETUP that no version control is present, and drop the git clause from DEFINITION OF DONE — never invent a repository.
3. **Second brain** — does a knowledge base / vault exist for this project, and where. Offer: none, a detected path, or "yes, I'll give the path".
4. **The highest-value remaining question**, in priority order: a mission or scope ambiguity that would send the work in a materially different direction · the verification bar when "done" is genuinely unclear · length (standard 10,000–15,000, or compact under 4,000; standard is the default and only claims the slot when nothing outranks it).

**Leave slot 4 empty when nothing outranks the default.** Three questions on a one-line brief is proportionate; a fourth manufactured to fill the shape is the friction `rules/01-intake.md` §4 warns about. Where several material ambiguities compete for the slot, collapse them into one multi-select rather than exceeding the ceiling — see `rules/01-intake.md` §5.

**"Use defaults" / "entscheide selbst" does not cancel the Frame round.** Those four things cannot be inferred safely. It cancels the Assumption round instead — record the assumptions in the preamble and generate. **One exception:** a Frame answer that leaves the mission incoherent still gets its one question. "Use defaults" authorises inference, not the generation of something that cannot be executed.

**When `AskUserQuestion` is unavailable** — headless, piped, or invoked as a subagent — the Frame round cannot run. Do not stall. Take the non-interactive fallback set in `rules/01-intake.md` §5 and list all four choices in the preamble as assumptions the user must check.

## Section order

Fixed. Conditional sections sit where marked; never emit an empty heading.

```
# SETUP                              required
# MISSION                            required
# SOURCE OF TRUTH / REFERENCES       conditional
# SCOPE                              required
# FIRST ACTION                       required
# WORKING METHOD (mandatory)         required
{{domain modules}}                   conditional, 0-2, placed here
# TESTING & VERIFICATION             required
# SECOND BRAIN / RESEARCH            conditional
# MODEL ROUTING & PARALLELISM        required
# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)   required
# DEFINITION OF DONE                 required
```

Nine required sections. The default structure is the point — it works, so keep it. Conditional sections earn their place or stay out.

## Output contract

Emit in this order, and nothing else:

1. **Assumptions and decisions** — plain text, in the user's language, above the block. Only what you actually assumed or chose without being told. Three to eight lines. If you assumed nothing, write one line saying so. Never restate the prompt here.
2. **The prompt** — inside a single fenced markdown code block, in English, complete and self-contained. A fresh agent with no access to this conversation must be able to execute it.

Nothing after the block. No summary, no offer to run it, no commentary on your own work.

## Hard prohibitions

- Do not execute the generated prompt, or any part of it.
- Do not emit both rails. Do not emit a rail the user did not choose.
- Do not invent model names, prices, plugin names, benchmark results, or tool capabilities. Prices and model rosters are time-sensitive: state them only where a rule file records them, and carry the verification note with them.
- Do not emit placeholders, empty headings, or sections that do not apply.
- Do not silently widen the mission. Sharpen it, and show the sharpening in the assumptions preamble.
- Do not write the prompt in the user's language because they wrote to you in it.
