# RULE 03 — SECTION CATALOG

Nine required sections, four conditional ones, fixed order. For each: what it must carry, when it appears, and how it compresses.

Headings are `# UPPERCASE`, exactly as written here. Sub-structure inside a section uses bold lead-ins and bullets, not deeper heading levels — the flat heading set is what makes these prompts scannable.

---

## `# SETUP` — required

**Carries:** execution mode, persistence, repository safety, language, autonomy, reporting cadence.

**Must contain:**
- **Working language.** "Work, think and report in English." One clause of justification: it costs fewer tokens per unit of meaning, and every turn pays that tax. Name the exception: user-facing product copy stays in its own language.
- **Persistence.** Where the brief itself is written down, and that the agent works against that file rather than against fading context.
- **Repository safety.** The real base branch name, the real working branch, and the rule that the base branch is never committed to *directly* — keep that word, or a later DoD clause requiring a merge into it reads as a contradiction. **Where there is no repository**, replace this and the commit cadence with one line stating that no version control is present, and drop the git clause from DEFINITION OF DONE. Never invent a repository.
- **Commit cadence.** Small commits per verified step; the branch stays green.
- **Autonomy.** Autonomous to completion, or a named approval gate. Say which questions warrant stopping — blocking ambiguity only, unless the brief is approval-gated.
- **Reporting.** Compact progress: what shipped, what is verified, what is next. No long recaps.

**Compact form:** three to four lines. Language, branch rule, commit cadence, autonomy. Persistence moves into FIRST ACTION.

---

## `# MISSION` — required

**Carries:** the single outcome, at maximum precision. See `rules/00-core-contract.md` §Precision.

**Must contain:**
- The end state, stated as a condition that is either true or false — not an activity.
- Every prestige adjective translated into an observable property, or deleted.
- Whole job vs named slice, explicitly.
- The priority order when goals compete (correctness over speed, composition over literal fidelity, and so on).
- Context that is *not* scope, marked as such, when the reader needs to know why.

**Never:** a mission that could describe two different jobs. Read it back and ask which two prompts a reader could produce from it. If there are two, it is not finished.

**Compact form:** stays proportionally the longest section. Cut context and priority order before cutting the end-state definition.

---

## `# SOURCE OF TRUTH / REFERENCES` — conditional

**Activate when:** a spec, existing code, reference images, standards, research notes or a living document materially guides the result.

**Must contain:**
- Which source is binding and which is directional. Say it in those words.
- The interpretation rule for directional sources: intent, not literal shape. Reference sketches contain real mistakes — geometry that does not line up, routes that do not connect, proportions that collapse at scale. Fix them in the source's spirit; a coherent result that reads like the reference beats a faithful copy of a flawed drawing.
- Contradiction handling: which source wins, and who decides.
- A deviation log: one line per deliberate departure — what the source showed, what was built, why.
- Re-consultation cadence: re-open the sources every pass, not once at the start.
- Whether the source is living, and who is allowed to sharpen it.

**Compact form:** binding vs directional, the deviation log, one line on contradictions.

---

## `# SCOPE` — required

**Carries:** the boundary, in both directions.

**Must contain:**
- In scope: the surfaces, files, systems and artifacts that may change.
- Out of scope: named explicitly. What exists but stays untouched is more useful than a list of what to build.
- Normal implementation work that the outcome requires is in scope by default — do not force a question for every obvious sub-step.
- Expansion rule: on discovering materially different work, stop and ask; do not silently expand.
- External side effects (publishing, sending, deploying, deleting, spending) always require confirmation unless the brief authorised them.

**Compact form:** one in-scope line, one out-of-scope line, the expansion rule.

---

## `# FIRST ACTION` — required

**Promoted from conditional to required.** The reason is mechanical: context gets compacted on long runs, and a mission that only exists in the opening turn is a mission that will be silently lost. Persist it before doing anything.

**Must contain:**
- **Write the brief to a durable file** — `GOAL.md` unless the project already has a convention — before any implementation. Mission, scope, acceptance criteria per item, decisions taken, open risks.
- **Read it first and append; never clobber.** `GOAL.md` is the single most likely file to already exist, often written by a previous prompt from this same skill. The instruction is "read any existing `GOAL.md`, then append a dated section" — never "write `GOAL.md`", which reads as an overwrite and will be executed as one.
- **Persist every supplied input** next to it: reference images, screenshots, links, specs. Copy them into the project's own directory tree — the repository where there is one, otherwise the folder SETUP names as the working root. Do not rely on them staying reachable.
- **Work against that file from then on.** Re-read it at the start of every work session and after every compaction.
- **Keep it living.** Sharpen it as understanding improves; record decisions and accepted deviations there.
- The task-appropriate baseline capture: inventory, current-state screenshots, a build and test run, a gap analysis — whatever establishes where things actually stand before they change.

**Compact form:** two lines. Write `GOAL.md` with mission, acceptance criteria and risks; capture the baseline named in the mission.

---

## `# WORKING METHOD` — required

**Carries:** the professional role, the loop, and the decomposition doctrine.

**Must contain:**
- **The role.** A named senior professional appropriate to the domain — "senior level designer and engine architect", "senior backend engineer", "product designer". Roles change what an agent notices.
- **The universal loop:** read the spec, code and notes first, never build on assumption → define this step's done-condition and how it will be observed → order by dependency → implement one small complete step → verify before continuing → refactor and integrate continuously → record decisions, risks and accepted deviations.
- **The decomposition doctrine** from `rules/02-thinking.md`, condensed: interrogate the requirement, branch it, build in dependency order, re-plan when a prerequisite surfaces, write the TODO instead of assuming past a blocker.
- **The escalation ladder:** scope → framing → context → tooling → execution → capability.
- Domain practice, from the loaded profile in `rules/domains/`.
- For code: the engineering bar. Clean boundaries, honest naming, the better-engineered solution over the quick one, refactor first when the current structure blocks the change.

**Compact form:** role, the five-step loop as one numbered run, two lines of decomposition doctrine.

---

## Domain modules — conditional, 0–2, placed after WORKING METHOD

Load by the classification value from `rules/01-intake.md` §2. The mapping is exact — do not guess a filename:

| Classification | File |
|---|---|
| ui-ux | `rules/domains/ui-ux.md` |
| web-frontend | `rules/domains/web-frontend.md` |
| mobile-flutter | `rules/domains/mobile-flutter.md` |
| backend-api | `rules/domains/backend-api.md` |
| data-db | `rules/domains/data-db.md` |
| game-unreal | `rules/domains/game-unreal.md` |
| research-knowledge | `rules/domains/research-knowledge.md` |
| creative-media | `rules/domains/creative-media.md` |

Each profile carries eight fixed headings: role, work sequence, decomposition hints, verification surface, evidence artifacts, common failure modes, test-time compute verdict, and Definition-of-Done clauses. Those last two feed `MODEL ROUTING & PARALLELISM` and `DEFINITION OF DONE` directly.

**Load at most two.** A task in three domains is usually a task that was not decomposed.

**When the platform is undetermined** — the brief names an app you cannot locate, so ui-ux, web-frontend and mobile-flutter are indistinguishable — **load `ui-ux` alone** and phrase its verification surface platform-neutrally. "The smallest and largest size the app supports" rather than "breakpoint"; "keyboard-only or switch-only traversal" rather than "keyboard-only". Guessing the platform imports a whole discipline's vocabulary that may be wrong.

Emit as their own `# UPPERCASE` sections with task-specific names — `# UI/UX`, `# ENGINE CONTROL — MCP IS THE INTERFACE`, `# ASSET PIPELINE`, `# CAMERA RIG`.

**Never emit a whole profile.** Take the parts the task touches. A profile is a source to compile from, not a block to paste. When no profile fits, emit no domain module — the universal loop in WORKING METHOD is sufficient on its own.

---

## `# TESTING & VERIFICATION` — required

**Carries:** what will prove the work, concretely.

**Must contain:**
- Tests chosen from the real failure surface, not from a coverage target. Integration and end-to-end over trivial unit tests; unit tests to pin a detail or unblock.
- The exact commands or gates that must be green, named.
- Error, empty, loading and edge states exercised, not just the happy path.
- Evidence: what gets captured, in what form, where it is filed.
- **Never report a result you have not observed.** Screenshot, log line, test output — or it did not happen.
- For subjective outcomes: the applicable blind lanes from `rules/06-verification.md`.
- Where a new test is added, break it once on purpose to prove it bites — **then paste the failing output into the evidence and restore the test in the same commit.** Without those two clauses the instruction is unfalsifiable and leaves the branch red; it is the one thing in a prompt an agent can claim to have done at zero cost.

**Compact form:** the named gates, the evidence rule, one line on subjective lanes if they apply.

---

## `# SECOND BRAIN / RESEARCH` — conditional

**Activate when:** a knowledge base exists, or the task is knowledge-heavy, or current facts matter. Governed by `rules/05-second-brain.md`.

**Omit entirely when** the user answered "no second brain" *and* the task needs no research. Do not emit a hollow research section to fill the shape.

**Activation is an OR, so a knowledge-heavy task activates this section even with no vault.** In that case the heading is `# RESEARCH`, not `# SECOND BRAIN / RESEARCH` — do not promise a knowledge base that does not exist — and the content comes from `rules/05-second-brain.md` §9, not §8. Every line of §8 is vault-conditional and yields nothing here. Drop the second-brain clause from DEFINITION OF DONE too; `rules/08-git-and-done.md` §4 makes it conditional.

---

## `# MODEL ROUTING & PARALLELISM` — required

**Carries:** exactly one rail, the routing economics, and the parallelism rule. Governed by `rules/04-model-routing.md` plus one file from `rules/rails/`.

Never both rails. Never a rail the user did not choose.

---

## `# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)` — required

**Carries:** the bounded improvement loop. Governed by `rules/07-self-improvement.md`.

The `0-2` in the heading is deliberate and stays in the heading. Zero passes is a legitimate, correct outcome.

---

## `# DEFINITION OF DONE` — required

**Carries:** the completion contract. Governed by `rules/08-git-and-done.md`.

**Must contain:**
- One clause per requirement in MISSION, each naming the evidence that settles it.
- The domain's own DoD clauses from the loaded profile.
- **The git end-state clause. Always.** Non-negotiable, in every prompt, even for a one-file change.
- Documentation state: which files must be current.
- Accepted residual work, named and located — backlog entries, not a hidden second loop.

**Never:** a DoD clause with no way to check it. "Code is clean" is not a clause. "No cross-layer imports; the boundary test passes" is.

**Compact form:** one line per mission requirement, plus the git clause. The git clause is never cut.
