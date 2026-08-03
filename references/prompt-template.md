# PROMPT SKELETON

The order is fixed. Conditional sections sit exactly where marked. Never emit an empty heading, and never reorder.

```
# SETUP
Working language. Persistence. Branch reality. Commit cadence. Autonomy. Reporting.

# MISSION
The end state as a condition that is true or false. Quality words translated.
Whole job or named slice. Priority order when goals compete. Context marked as context.

# SOURCE OF TRUTH / REFERENCES          [conditional]
Binding vs directional. Intent, not literal shape. Contradiction handling.
Deviation log. Re-consultation cadence.

# SCOPE
In scope. Out of scope, named. Expansion rule. External side effects.

# FIRST ACTION
Write GOAL.md: mission, acceptance criteria per item, decisions, risks.
Persist supplied references into the repository. Capture the baseline.
Work against that file from here on.

# WORKING METHOD (mandatory)
The senior role. The loop: read first → define the done-condition and how you will see it →
order by dependency → one small complete step → verify → refactor and integrate → record.
Decomposition doctrine. Escalation ladder. The engineering bar.

{{DOMAIN MODULES}}                        [conditional, 0-2, named for the task]

# TESTING & VERIFICATION
Tests from the real failure surface. Named gates and commands. Error and edge states.
Evidence captured and filed. Never report what you have not observed.
Blind lanes, where the outcome is judged rather than measured.

# SECOND BRAIN / RESEARCH               [conditional]
Search order and phrasings. Adopt the vault's conventions. Correction mandate,
including how the failure arose. Expansion mandate. Topics to guarantee.

# MODEL ROUTING & PARALLELISM
Quality first, tokens second. Hard rules. Exactly one rail.
Parallel lanes mapped to this task's actual work surfaces. Test-time compute verdict.

# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
Earned, not scheduled; zero is valid. Pass 1 review criteria. Pass 2 only after
high-impact fixes, with fresh evaluators. Stop condition. Backlog destination.

# DEFINITION OF DONE
One clause per mission requirement, each naming its evidence.
Domain clauses. Documentation state. The git end-state clause. Accepted residuals.
```

## Section-name variants

The core nine keep their canonical names. Domain modules and the references section take task-specific names in the same style:

- `# REFERENCES — DIRECTION, NOT BLUEPRINT`
- `# ENGINE CONTROL — MCP IS THE INTERFACE`
- `# ASSET PIPELINE — BAKED STATIC MESHES, BUILT OUTSIDE`
- `# CAMERA RIG — THREE TIERS`
- `# UI/UX`
- `# API CONTRACT & MIGRATION SAFETY`
- `# GAP HUNT — ITS OWN PASS`

A qualifier after an em dash is house style when it carries the section's argument. `# CAMERA RIG` says what the section is about. `# CAMERA RIG — THREE TIERS` also says what it demands.

## Phase-structured variant

For approval-gated work, phases replace the flat middle while the frame stays:

```
# SETUP
# PHASE 1 — PLAN WITH ME (no code yet)
# PHASE 2 — SHIP THE SLICE
# WORKING METHOD (mandatory)
...
```

Keep SETUP first and the four closing sections — TESTING, MODEL ROUTING, SELF-IMPROVEMENT, DEFINITION OF DONE — last. MISSION and SCOPE fold into the phase bodies. FIRST ACTION folds into Phase 1.

**Lint this variant with `--phased`.** Without the flag the script requires `# MISSION`, `# SCOPE` and `# FIRST ACTION` as top-level headings and this shape fails on three errors. With it, the six remaining sections are required and at least one `# PHASE` heading must exist.
