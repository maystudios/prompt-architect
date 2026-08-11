# Goal Prompt Template

Use these top-level sections in this order. Conditional sections must earn their place and must never be empty.

```markdown
# SETUP
# GOAL
# PROJECT TRUTH & DECISION LEDGER
# SCOPE
# FIRST ACTION
# WORKING METHOD
# ENGINE RULES — [resolved engine]                 (required for engine work)
# PLAYER EXPERIENCE & CREATIVE DIRECTION          (creative/main goals)
# STUDIO ORCHESTRATION & GOAL PACKETS             (main or multi-stream goals)
# PLANNING & VISUAL CONTROL PLANE                  (main/planning goals)
# ASSET & CREATIVE PIPELINE                        (media/content goals)
# TESTING, PLAYTESTING & EVIDENCE
# KNOWLEDGE & SECOND BRAINS
# MODEL ROUTING & PARALLELISM
# INTEGRATION & VERSION CONTROL
# AUTONOMY & HUMAN GATES
# DEFINITION OF DONE
```

## Section contract

**SETUP** — Work and report in English; repository/project location; executing host; detected tools; exact pinned engine version; immutable constraints; one-sentence instruction to verify time-sensitive capabilities before relying on them.

**GOAL** — One outcome, player/product reason, and observable final state. A main game is still one Goal, not an unbounded wish list.

**PROJECT TRUTH & DECISION LEDGER** — Resolved facts, decisions, rationale that constrains work, confidence/source distinctions, non-goals, unresolved risks. No interview transcript.

**SCOPE** — Included systems/artifacts and explicit exclusions. Separate required outcome from optional opportunity.

**FIRST ACTION** — Inspect the live project and persist a concise `GAME_PLAN.md` or equivalent canonical plan before changing implementation. For a child task, update its Goal Packet status rather than rebuilding the whole plan.

**WORKING METHOD** — Plan before implementation; one coherent job per isolated work unit; interface contracts before parallel work; placeholder-to-production progression; tests at every boundary; evidence-driven iteration; rollback only the failed unit.

**ENGINE RULES** — Compile only the selected engine profile and the user's explicit code/visual-scripting mode overrides.

**PLAYER EXPERIENCE & CREATIVE DIRECTION** — Player fantasy, feel targets, visual/audio language, color bible, reference and anti-reference, adjustable look-dev controls. Write testable traits, not taste adjectives alone.

**STUDIO ORCHESTRATION & GOAL PACKETS** — Adaptive roles, task/session boundary, dependency graph, child packet schema, messaging and integration queue.

**PLANNING & VISUAL CONTROL PLANE** — Canonical repo artifacts plus optional synchronized human-facing tools. Never make a rendered canvas the only source of truth.

**ASSET & CREATIVE PIPELINE** — Research, ideation variants, analysis, production conversion, provenance/rights, engine import, style/performance validation, rejection criteria.

**TESTING, PLAYTESTING & EVIDENCE** — Unit/integration/engine/build/playtest/visual/performance lanes selected by risk. Every requirement maps to evidence. Never report a result not observed.

**KNOWLEDGE & SECOND BRAINS** — Name both exact brain repository URLs in every Goal; detect or initialize the project brain; read both before work; return knowledge packets; run one single-writer curator even for a bounded task; apply correction and linking rules.

**MODEL ROUTING & PARALLELISM** — Discover current capabilities; route by task; use the cheapest model that clears the quality bar; escalate on evidence; isolate context; no invented model names or prices.

**INTEGRATION & VERSION CONTROL** — Worktree/branch ownership, commit contract, serial integration, testing branch, conflict ownership, generated/scratch/tooling cleanup, one clean landing state.

**AUTONOMY & HUMAN GATES** — Autonomous reversible execution and the exact four non-delegable gate classes.

**DEFINITION OF DONE** — Concrete artifacts, passing evidence, target-platform validation, brain curation complete, control plane reconciled, clean repository/integration state, no temporary pollution.

## Writing rules

- Use direct imperatives and concrete paths only when observed.
- State why a constraint exists when that prevents a plausible wrong implementation.
- Pair subjective qualities with references, measurable traits, comparison captures, or playtest questions.
- Do not prescribe a tool merely because it was mentioned. Prescribe its role and fallback.
- A fresh executor must not need this conversation.
