# RULE 02 — INTERROGATION AND DECOMPOSITION

**This is the highest-leverage rule in the skill.** It governs two things at once: how *you* think while compiling the prompt, and what the compiled prompt demands of its executor. Both, always.

The premise: when a strong model fails repeatedly on a task, the cause is almost never insufficient intelligence. It is a task that was framed too widely, or cut along the wrong seam. Escalating the model is the expensive way to not fix that.

## 1. Interrogate the task before solving it

A brief is a description of a want, not a specification. The gap between them is where the work actually lives.

**For every vague word in the brief, ask what it means *here*.** Not in general — here, in this project, for this user, on this artifact. "Sensible", "clean", "intuitive", "better", "fast", "proper", "AAA", "production-ready" are all unspecified until answered locally.

Then ask the questions one step out from the task:

- **Why is it this way now?** Existing structure usually encodes a constraint nobody wrote down.
- **Why was this excluded, hidden, redacted, or left out?** The reason is often the rule you need.
- **Who produced this input, under what process?** The producer's process is a source of hard constraints the data itself never states.
- **What would make this task impossible?** If the answer is "nothing", the scope is probably too wide to see clearly.
- **What am I about to assume?** Name it. Then check whether it is true.

Worked shape, so the move is unmistakable: a table of aggregate figures has cells blacked out and the job is "solve it sensibly". The naive read is a constraint-satisfaction problem with infinitely many solutions, therefore unsolvable. The productive read starts one question earlier — *why were these particular cells redacted?* Because a cell covering few contributors would expose an individual. That single answer yields a suppression rule, which yields a lower bound on every suppressed cell, which combines with the hierarchical sums the table already publishes, which turns an unbounded search into a narrow one. And the same interrogation surfaces that the published figures do not reconcile perfectly, because different sources round differently — so "solve it" was never "find the exact answer", it was "find the best defensible answer and state the residual". **The redaction question was three steps away from the stated task and was the whole solution.**

Carry that habit into the prompt. An executor that only answers the question it was handed will produce a well-built wrong thing.

## 2. Branch the decomposition

Do not take the first cut. Expand each requirement into its sub-questions until you hit something you can actually build and check, then walk back up.

```
"clean architecture"
├─ which principles apply here?      → SOLID, KISS, DRY — which are actually violated today?
├─ what does maintainable mean here? → modular, honest names, boundaries a newcomer can find
│   └─ is this codebase modular?     → no: UI is written inline in the page classes
│       └─ then a refactor precedes the feature, and that reordering is the plan
└─ what proves it?                   → boundary tests, a dependency check, no cross-layer imports
```

The valuable output of that tree is the **reordering**: the feature was the task, the refactor turned out to be its prerequisite, and only the branching exposed it. Step back and re-plan the moment a branch reveals a prerequisite. Re-planning mid-task is correct behaviour, not a failure.

## 3. Cut along the right seam

- **Build in dependency order, not in reading order.** The page that aggregates everything is built after the things it aggregates. Building the home screen first guarantees a home screen that mirrors four of six sections and adds nothing — because when it was written, two sections did not exist yet.
- **A step is small enough when its done-condition is one observable fact.** If you cannot name what you will look at to confirm it, the step is still too big.
- **When a step cannot be finished now, write the TODO and say why it is blocked.** Do not assume the missing half and move on. An assumption made to avoid a blocker becomes a defect later.
- **Deliberately incomplete is a legitimate state; silently incomplete is not.** "Rough version now, full version after the remaining screens exist" is a plan. Pretending the rough version is the deliverable is a bug.
- **Stay in one domain per agent.** An agent that jumps between interface polish, migration scripts and test infrastructure does three things at 60%. Give each agent one discipline and one work surface.

## 4. Answering a subjective question with evidence

When the requirement is "what would be *good* here", do not guess and do not immediately implement. Choose a way to find out, then implement against the finding:

- **Ask the artifact.** Run it, capture it, look at it against the stated intent.
- **Ask a persona.** A fresh agent given a realistic user's situation and goal — never the intended click path — reveals what an interface actually affords.
- **Ask the record.** Search the second brain and the web for what an audience of this kind actually reacted well to. The conclusion usually exists only in the aggregate, not in any single source.
- **Ask by contrast.** Build two candidates and compare them on a fixed surface. Comparison is far more reliable than absolute judgement, for models and for people.

Then write down the conclusion, not just the sources. `rules/06-verification.md` runs this as a formal loop; `rules/05-second-brain.md` says where the conclusion is stored.

## 5. Escalation doctrine — put in every emitted prompt

When work stalls, diagnose in this order. Model escalation is last, not first.

1. **Scope** — is the task too wide to hold? Cut it and retry the piece.
2. **Framing** — is it cut along the wrong seam? Re-decompose from the requirement, not from the current attempt.
3. **Context** — does the agent lack a file, a spec, a log, a screenshot it needed? Supply it.
4. **Tooling** — is a capability missing, disabled, or being used wrongly? Verify it directly.
5. **Execution** — is it a plain bug in what was just written? Fix it.
6. **Capability** — only now consider a stronger model or higher effort.

**Two failures at the top effort tier means the task is mis-scoped, not under-powered.** Stop, re-cut, retry. Do not keep spending on the same framing — cost climbs, quality does not.

## 6. What this rule injects into the emitted prompt

Compile these into WORKING METHOD, condensed to fit the length budget:

- Interrogate the requirement before implementing it; name what each vague word means here.
- Decompose until every step has a single observable done-condition.
- Build in dependency order; the aggregating surface comes last.
- Re-plan when a branch exposes a prerequisite — that is expected, not a detour.
- Write the TODO when a step is genuinely blocked; never assume past a blocker.
- One agent, one domain, one work surface.
- On a stall, walk the escalation ladder: scope → framing → context → tooling → execution → capability.
