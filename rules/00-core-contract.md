# RULE 00 — CORE CONTRACT

The non-negotiables. Every other rule file operates inside these.

## What this skill produces

One standalone execution prompt, in English, in the house structure, ready to paste into a fresh agent session with no other context.

The test: **hand the prompt to an agent that has never seen this conversation. If it needs to ask what the mission is, what "done" means, where the work lands, or which models to use, the prompt failed.**

## What this skill never does

- **Never executes the prompt.** Not partially, not "just the first step", not "just to check it works". Generation and execution are separate operations run by separate invocations.
- **Never creates the branch, file, or artifact the prompt describes.** Writing the prompt to a file is fine when the user asks for it. Doing the work is not.
- **Never emits both routing rails.** One host, one rail.
- **Never emits a placeholder.** See below.
- **Never claims a capability it has not established.** If the prompt depends on a plugin, MCP server, bridge or CLI, either the user confirmed it exists, or the prompt carries a discovery step that checks and states what to do when it is missing.

**The boundary is a principle, not a list.** Any **read-only observation that informs authorship** is allowed — reading the repository, the spec, the code and the reference images, and equally: running a build or the test suite to learn its exact command, launching the app to learn its real supported size range, and searching the web to check that a time-sensitive fact the prompt will state is still current. `rules/06-verification.md` demands the prompt name exact gates and `rules/00` §Time-sensitive demands current facts; neither is possible without looking.

What is forbidden is **anything that creates, modifies or publishes an artifact the prompt describes**: writing the feature, creating the branch, editing the spec, filing the assets, opening the PR. The test is not "did I run a command" — it is "did I change something the prompt was supposed to change".

The awkward case is real and worth naming: the first step of the described work is often also legitimate research. Running the test suite to learn its name is research; running it to fix the failures is execution. Stop at the observation.

## Language contract

- **Conversation:** the user's language. German in, German out.
- **Artifact:** English. Always. No exception for German briefs, German codebases, German-facing products.
- **Inside the artifact:** the prompt instructs its executor to work and report in English.
- **Exception, and only this one:** literal strings the product must display in another language — UI copy, error messages, seed data — stay in that language, quoted, and marked as user-facing copy.

The reason goes in the prompt so the executor does not "helpfully" switch: English costs fewer tokens per unit of meaning, and every downstream agent pays that tax on every turn.

## Placeholder ban

An emitted prompt contains **no** `<angle-bracket-slot>`, `TODO`, `TBD`, `XXX`, `FIXME`, `[insert …]`, `path/to/…`, `your-project`, `<name>`, or any other blank the reader must fill.

Three ways out, in order of preference:

1. **Read it.** The branch name, the file path, the framework, the test command — most of these are discoverable in the repository. Go look.
2. **Ask it.** If it is one of the four Frame-round questions, or it materially changes the work, ask.
3. **Decide it, and say so.** Pick the sensible professional default, write it concretely into the prompt, and list it in the assumptions preamble.

A concrete wrong-but-stated default beats a hole. The user can correct a stated decision; they cannot correct a blank.

**Fourth way out — describe the role, and make the prompt discover the value.** Some values are facts about an environment you cannot reach: the base branch name of a repository you have never seen, the exact test command of an unlocated project, the supported device range of an app you cannot run. Reading fails, deciding is a guess with real consequences — a wrong base branch makes the prompt's own "never commit to X" point at the wrong branch — and asking may not fit the Frame round.

Then: **write the prompt against the described role, and require FIRST ACTION to discover and record the literal value.** "Never commit directly to the repository's default branch; record its actual name in `GOAL.md` as the first action." That is a complete, executable instruction with no hole in it. It is the same discovery-plus-fallback pattern `rules/04-model-routing.md` §7 uses for bridges, applied to values rather than capabilities.

This is not a placeholder. A placeholder asks the *reader* to fill a blank before the prompt works; a described role tells the *executor* what to look up as step one.

**Template slots in the rule files use `{{double braces}}`, never angle brackets.** The compiled-form blocks in `rules/04`, `rules/05`, `rules/07`, `rules/08` and the rail files are sources to compile from, not text to paste — and if they used `<angle brackets>` a compiler that copied one would ship two blocking lint errors. Every `{{…}}` is a slot you fill; **none may survive into the emitted prompt**, and the linter errors on them exactly as it does on angle brackets.

**There is still no exemption for runtime templates.** When the executing agent must fill a value in a format you specify — a correction date, a measured number, a commit hash — describe the fields in prose: "mark it with the word `Corrected`, the date, and the source". Do not ship a bracketed template like `Corrected <date> — <source>`. An exemption category would make the ban unenforceable, and the linter cannot tell an intentional template from a hole you forgot to fill.

## Precision contract

**MISSION carries the highest precision requirement in the document.** The worst outcome this skill can produce is a well-executed wrong task. Everything else is recoverable.

In MISSION:
- Name the outcome as an end state, not an activity. "The route is walkable end to end in a packaged build" — not "improve traversal".
- Every quality word is translated. "Production-ready", "AAA", "intuitive", "native", "clean", "robust" are not requirements; they are placeholders wearing a suit. Replace each with the observable property it stands for, or delete it.
- State explicitly whether the job is the whole thing or a named slice.
- State explicitly whether the agent proceeds autonomously or stops for approval, and at which gate.
- If the brief was vague and you sharpened it, the sharpened version goes in MISSION and the sharpening goes in the assumptions preamble. Never sharpen silently.

## Time-sensitive facts

Model names, effort tiers, prices, plugin names, concurrency ceilings and benchmark claims move. Treat them as data, not knowledge.

- State them only where a rule file records them.
- Carry the recorded date and the verification note into the emitted prompt when the prompt depends on the number.
- Never update a price or model roster from memory. Never "correct" one because it looks stale.
- When a prompt's routing depends on a model the user has not confirmed is available, the routing section carries a one-line fallback.

## Scope of the emitted prompt

The prompt must not ask its recipient to do work outside the stated scope. Common leaks to check before emitting:

- A DoD clause that requires an artifact SCOPE excluded.
- A test matrix that covers surfaces the mission never touches.
- A domain module that drags in its whole discipline when the task needed one slice of it.
- A second-brain mandate on a project with no second brain.
- A parallelism instruction that implies work nobody asked for.
