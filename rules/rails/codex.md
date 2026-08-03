# RAIL B — HOST IS CODEX

Emit this rail when the user answered "Codex" in the Frame round. Never emit it alongside Rail A.

**Facts recorded here are time-sensitive. Last recorded 2026-08-02, unverified since.** Do not update them from memory — edit this file deliberately when the roster or pricing changes. See `rules/04-model-routing.md` §8.

## Roster

- **`gpt-5.6-sol` — orchestrator, xhigh → max.** The strongest model on this rail. Architecture, planning, reconciling conflicting sources, adversarial critique, fanning out and supervising the worker swarm. Give it the genuinely hard thinking.
  - If xhigh fails twice, escalate to max. If max also fails, the task is mis-scoped, not under-powered. Re-cut it.
  - **Never `/fast`.** No paid latency tier, ever.
- **`luna` — max effort only, spawn freely.** The volume workhorse. Research sweeps, triage, extraction, inventory, lint scans, frontmatter and link repair, summarising for a merger, asset selection and filing. Small closed tasks with clear done-conditions; dozens at once is fine and under-spawning is the expensive mistake.
  - Its advantage evaporates on vague tasks — it burns retries. **Scope first, then spawn wide.**
- **`terra` — max effort only, by exception.** The deliberate middle voice, justified where a *third independent failure mode* is worth buying: planning cross-checks, capability tables, scoped production from a filled outline. Never a default. If you reach for Terra, write one line saying why Luna-max or Sol was not the answer.

**Never run Terra or Luna below max effort.** For any Terra effort level there is a Luna or Sol level that is more capable at the same cost, or equally capable for less. If max Luna cannot do it, escalate to Sol — do not step sideways into Terra.

## Cross-rail bridge

The Codex-side **Claude bridge plugin**. It launches **Opus 5** and **Sonnet 5** agents for the work the Anthropic models own:

- **Opus 5** — a second independent architecture read, hard merges, final review, the librarian role when one exists, and the other half of a paired plan.
- **Sonnet 5** — cleanup, reformatting, bulk web research, and cheap uncontaminated naive reviewers for blind evaluation lanes.
- **Fable stays banned here too.** See `rules/04-model-routing.md` §1.

**Bridge availability is not assumed.** The emitted prompt verifies the Claude bridge is installed before routing across it, and falls back to a second `gpt-5.6-sol` for the independent read and `luna` for the cheap lanes if it is not — noting the substitution in `GOAL.md`.

## Default posture

Around **4 Codex agents** at the orchestration tier, with Luna workers on top as the queue can feed them, plus Claude agents through the bridge and browser lanes where media work exists.

That is a ceiling, not a quota. `rules/04-model-routing.md` §2 governs: scale to ready independent work.

## Cost ordering

Cheapest capable lane wins. **Luna-max before Sonnet, Sonnet before Opus/Sol** for bulk sweeps, triage and reformatting.

**Verify current prices before any routing decision turns on cost.** Provider pricing moves, and a stale number is worse than none — it produces a confident wrong choice. Read the provider's current rate card; do not trust a figure written here, in a prompt, or in your own memory.

The durable part is the *shape*, not the numbers. On both rails the volume worker sits roughly an order of magnitude below the orchestrator, and the cheap general model sits between them. **That gap, not intuition, decides who gets the task** — but confirm the gap still holds before you lean on it.

Emit a price line only when the prompt's routing actually turns on relative cost, and carry the date you verified it.

## Non-interactive invocation

Hand each worker only the files its task needs:

```
codex exec -m gpt-5.6-luna   # volume lane
codex exec -m gpt-5.6-terra  # by exception only
```

Use `/model` when working interactively.

## Compiled form — standard length

```
# MODEL ROUTING & PARALLELISM
Max quality at the lowest token cost that delivers it. Longer runtime is fine; wasted tokens are not.
Never use Fable. Never use Sol Fast mode or any paid latency tier — throughput comes from parallelism, which is free.
- gpt-5.6-sol (xhigh; max only on escalation): {{the architecture, planning and hard analysis of THIS task}}.
- luna (max effort only, spawn freely): {{the volume work of THIS task}} — small closed tasks, each with a stated done-condition.
- terra (max, by exception): only where a third independent failure mode pays for itself; justify it in one line.
- Claude bridge — verify it is installed first; if absent, use a second gpt-5.6-sol for the independent read and luna for the cheap lanes, and note it in GOAL.md:
  - Opus 5: {{the second independent read or hard merge of THIS task}}.
  - Sonnet 5: {{cleanup, reformatting, bulk research}} and naive blind reviewers.
- {{N}} agents in parallel: {{the actual work surfaces, one per agent}}. No two agents write the same file.
- {{test-time compute verdict for this task, one or two lines}}.
Keep context tight: hand each worker only its files. Integrate through commits, not assumptions.
```

## Compiled form — compact length

```
# MODEL ROUTING & PARALLELISM
Max quality, min tokens. Never Fable, never Sol Fast or any paid latency tier.
gpt-5.6-sol (xhigh): {{architecture and hard analysis}}. luna (max only, spawn freely): {{volume work, closed tasks}}. terra only by exception.
Claude bridge if installed — Opus 5 for the independent read, Sonnet 5 for cleanup and naive reviewers; if absent, second Sol and luna instead.
{{N}} parallel lanes, one per work surface, no shared files. {{Test-time compute: yes or no, one clause.}}
```
