# RULE 07 — SELF-IMPROVEMENT, BOUNDED

The heading always reads `# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)`. The `0-2` stays in the heading, because zero is a real answer and the number is the point.

## 1. Why it is bounded

An unbounded improvement loop degrades. Context fills, earlier reasoning is compacted away, and the agent starts inventing findings to justify the pass it was told to run. Past a certain depth each pass makes the result *worse* while reporting that it made it better.

Two passes is where the evidence still supports the changes. Beyond that, the loop is spending tokens to add risk.

## 2. Activation — a pass is earned, not scheduled

**Never run a pass automatically. Never invent work.**

- **Zero passes is correct** when the gates are green, the evidence is already captured, and the agent has no concrete reason to doubt the result. Say so and stop. This is a legitimate outcome, not a shortcut.
- **Run pass 1** when the agent is not confident the result clears the bar — the honest "this is probably right but I have not actually looked" case — or when risk or subjectivity makes a miss likely: subjective quality, an irreversible change, a wide blast radius, an interface a real person has to understand.
- **Run pass 2 only after pass 1 produced high-impact fixes.** Its job is to verify those fixes and check they broke nothing. If pass 1 found nothing meaningful, there is no pass 2.

Scope it to the unit of work — per feature, per area, per asset — not to the whole project at once.

## 3. Severity and what must be fixed

| Severity | Definition | Action |
|---|---|---|
| **High** | Breaks the mission, loses data, crashes, blocks the user, fails a stated gate | Fix. Always. |
| **Medium** | Degrades the outcome measurably; a user notices; a stated quality property is missed | Fix. |
| **Low** | Cosmetic, marginal, or a matter of taste | Fix only if cheap, safe and in the current work surface. Otherwise backlog it. |
| **Out of scope** | Real, but outside SCOPE | Never fix silently. Record it in the backlog. |

Log every finding with its severity, the evidence behind it, and its resolution. A finding without evidence is a guess and gets dropped, not fixed.

## 4. Stop condition — explicit

Stop when **any** of these is true:

1. A full pass produced no high- or medium-impact finding.
2. Two passes have completed.
3. The only findings left are low-impact or out of scope.
4. **A pass made something previously green go red and it is not immediately fixable.** Then: revert to the last green commit, record what was attempted and why it was reverted, and stop. Do not chase it.
5. Findings are starting to repeat, contradict the previous pass, or lack evidence. That is context degradation, not discovery. Stop.

On stop, every remaining finding becomes a named backlog entry in `GOAL.md` with its severity — **not another loop, and not a silent omission**.

## 5. Blind re-evaluation

For subjective work, the second pass uses **fresh evaluators who have not seen the first pass's findings**. Reusing the previous reviewer converts an independent check into a confirmation of its own earlier opinion.

Re-capture on the *same fixed surface* as the baseline. A comparison across different cameras, viewports or exposure settings proves nothing.

## 6. Feed the second brain

When a second brain exists, every pass ends by asking: **what would have prevented this finding?**

Write that in — the failure mode, not just the fix. See `rules/05-second-brain.md` §3. This is what makes the loop compound across sessions instead of re-teaching the same lesson every project.

## 7. Compiled section

```
# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
Per {{unit}}, not automatic. Run a pass only if the result does not demonstrably clear the bar. Never invent work. Zero passes is a valid outcome — say so and stop.
Pass 1 — <the concrete review for THIS task: run it, walk it, capture it>, checked against: {{correctness / robustness / the domain's own criteria}}. Log findings by severity with evidence, fix high and medium impact, re-test, add regression coverage.
Pass 2 — only after high-impact fixes: verify them, re-check the affected surfaces with fresh evaluators who have not seen pass 1's findings, stop.
Stop early if a pass finds nothing meaningful, if findings start repeating or contradicting, or if a fix turns a green gate red — then revert to the last green commit and stop.
Remaining findings become named GOAL.md backlog entries with severity, not another loop.
```

Compact form: three lines. The activation rule with "0 is valid", pass 1's concrete review, and the stop condition with the backlog destination.
