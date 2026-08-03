# RAIL A — HOST IS CLAUDE CODE

Emit this rail when the user answered "Claude Code" in the Frame round. Never emit it alongside Rail B.

**Facts recorded here are time-sensitive. Last recorded 2026-08-02, unverified since.** Do not update them from memory — edit this file deliberately when the roster or pricing changes. See `rules/04-model-routing.md` §8.

## Roster

- **Opus — 1–2 instances.** Architecture and fact ownership, resolving contradictions, writing the hard pages, merging parallel work, judging quality, final review, and the librarian role when one exists. One of these is usually the orchestrator already running.
  - Effort: **high by default. xhigh for architecture and hard merges.** Max is an escalation for a genuinely hard problem or a demonstrably stuck agent — never a posture.
  - If xhigh fails twice, escalate to max. If max also fails, the task is mis-scoped, not under-powered. Re-cut it.
- **Sonnet — the cheap lane.** Cleanup, reformatting, mechanical refactors, small scoped edits, bulk web research, and cheap uncontaminated naive reviewers for blind evaluation lanes.
- **Fable — banned.** See `rules/04-model-routing.md` §1.

## Cross-rail bridge

**Codex Rescue** (plugin). From inside Claude Code it launches Codex agents — `gpt-5.6-sol`, `terra`, `luna` — fires Codex reviews, and drives the rest of the Codex surface including image generation.

Use it for:
- **`gpt-5.6-sol` (xhigh → max)** — adversarial critique of the architecture, reconciling conflicting sources, the second half of a paired plan, hard analysis where a different failure mode is worth paying for. A first-class worker, not a second opinion.
- **`luna` (max effort only, spawn freely)** — the volume workhorse. Research sweeps, triage, extraction, inventory, lint scans, link and frontmatter repair, summarising for a merger. Small closed tasks with clear done-conditions; dozens at once is fine.
- **`terra` (max effort only, by exception)** — a third independent failure mode where that is genuinely worth buying: planning cross-checks, capability tables, scoped production from a filled outline. If you reach for Terra, write one line saying why Luna-max or Sol was not the answer.

**Never run Terra or Luna below max effort.**

**Bridge availability is not assumed.** The emitted prompt verifies Codex Rescue is installed before routing across it, and falls back to Sonnet for the cheap lanes and a second Opus for the adversarial read if it is not — noting the substitution in `GOAL.md`.

## Default posture

Around **6 Claude agents** running at once, plus Codex workers on top as the queue can feed them, plus browser lanes where media work exists.

That is a ceiling, not a quota. `rules/04-model-routing.md` §2 governs: scale to ready independent work. A single-surface task correctly runs one agent.

## Cost ordering

Cheapest capable lane wins. **Luna-max before Sonnet, Sonnet before Opus** for bulk sweeps, triage and reformatting.

**Verify current prices before any routing decision turns on cost.** Provider pricing moves, and a stale number is worse than none — it produces a confident wrong choice. Read the provider's current rate card; do not trust a figure written here, in a prompt, or in your own memory.

The durable part is the *shape*, not the numbers. On both rails the volume worker sits roughly an order of magnitude below the orchestrator, and the cheap general model sits between them. **That gap, not intuition, decides who gets the task** — but confirm the gap still holds before you lean on it.

Emit a price line only when the prompt's routing actually turns on relative cost, and carry the date you verified it.

## Compiled form — standard length

```
# MODEL ROUTING & PARALLELISM
Max quality at the lowest token cost that delivers it. Longer runtime is fine; wasted tokens are not.
Never use Fable. Never buy latency — no /fast, no priority tier. Throughput comes from parallelism, which is free.
- Opus (high; xhigh for architecture and hard merges; max only on escalation): {{the hard work of THIS task}}.
- Sonnet: {{the cheap scoped work of THIS task}} and bulk web research.
- Codex Rescue bridge — verify it is installed first; if absent, run these lanes on Sonnet and a second Opus, and note it in GOAL.md:
  - gpt-5.6-sol (xhigh): {{the adversarial or cross-rail work of THIS task}}.
  - luna (max only, spawn freely): {{the volume work of THIS task}}.
- {{N}} agents in parallel: {{the actual work surfaces, one per agent}}. No two agents write the same file.
- {{test-time compute verdict for this task, one or two lines}}.
Keep context tight: hand each agent only its files. Integrate through commits, not assumptions.
```

## Compiled form — compact length

```
# MODEL ROUTING & PARALLELISM
Max quality, min tokens. Never Fable, never paid latency tiers.
Opus (high, xhigh for architecture): {{hard work}}. Sonnet: {{cheap scoped work}}.
Codex Rescue if installed — luna (max) for {{volume work}}, gpt-5.6-sol (xhigh) to challenge the plan; if absent, stay on Sonnet and Opus.
{{N}} parallel lanes, one per work surface, no shared files. {{Test-time compute: yes or no, one clause.}}
```
