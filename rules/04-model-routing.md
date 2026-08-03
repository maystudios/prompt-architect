# RULE 04 — MODEL ROUTING & PARALLELISM (RAIL-INDEPENDENT CORE)

This file holds everything true on both rails. The host-specific roster lives in `rules/rails/claude-code.md` and `rules/rails/codex.md`. **Exactly one of those is ever emitted.**

Update discipline: when a model appears, disappears or changes price, edit the rail file. This core file should survive that untouched.

## 1. Hard rules — emit these in every prompt

- **Never use Fable.** Not as host, not as spawned agent, not through a bridge, not as reviewer. The margin over the strongest default model does not repay the price, and the cases where it would are rarer than the cases where the real problem was a mis-scoped task.
- **Never buy latency.** No `/fast`, no `priority` tag, no paid speed tier that doubles the rate. Longer runtime is fine. We buy throughput with parallelism, which costs nothing extra.
- **Longer runtime is fine; wasted tokens are not; idle capacity is the real waste.**
- **Split by file ownership.** No two agents write the same file at once. Integrate through frequent commits, not through assumptions.
- **Keep context tight.** No redundant file re-reads, no restated plans, hand each agent only the files its task needs.

### The Fable escape hatch — off by default

Do not emit it unless the user explicitly asks for it.

When they do, it **replaces** the "Never use Fable" line — it never sits beside it. Two lines saying "never" and "only after" in the same section is a contradiction, and an executing agent reading fast will resolve it in whichever direction suits the moment. One line, one rule.

The replacement reads exactly like this and no looser:

> **Fable is barred from normal routing.** It becomes available only after the escalation ladder in WORKING METHOD has been walked in full, the task has been re-cut at least once, and the top effort tier of the default strongest model has failed twice on the re-cut task. One attempt, never in a loop. If Fable also fails, the task is mis-scoped — stop, decompose further, and retry without it.

## 2. Quality first, tokens second

Both matter, in that order. They collide less often than they appear to.

- **Route by capability, then by cost.** When two agents do a job equally well, the cheaper one gets it. Bulk sweeps, triage, extraction and reformatting leave the expensive lane by default.
- **Spawning is not free and not automatically better.** Ask the actual question: would fifty agents deliver something two would not? Usually not — they deliver the same answer fifty times and the merge cost is real. Spawn to cover *independent* work, not to feel thorough.
- **Under-spawning cheap workers on genuinely parallel, well-scoped work is the opposite mistake.** Where the queue holds many small closed tasks with clear done-conditions, fill it.
- **Vague tasks destroy cheap workers.** They burn retries and the cost advantage evaporates. Scope first, then spawn wide.
- **Adaptive, not fixed.** Scale the pool to the ready independent work. A task with one work surface gets one agent, and that is the correct answer, not a missed opportunity.

## 3. Test-time compute — when brute force is right

Test-time compute means: spawn many attempts, score each against a hard gate, keep the winner, retry with variation on failure. It is a real technique with a real bill.

**Worth it when** the solution space is wide and quality is subjective or empirical, and a gate exists that can actually rank attempts:
- interface and interaction quality, where "better" only emerges from comparing variants
- performance work with a fixed output contract and a measurable target
- greenfield exploration where the shape of the answer is not yet known

**Waste when** the task is well-solved and repetitive, or a documented path already exists:
- project scaffolding — use the framework's own generator
- a documented CLI flow, a mechanical refactor, a rename, a format migration
- anything where the first correct answer is the only correct answer

**Prerequisite:** if you cannot state the gate that ranks attempts, you do not have test-time compute — you have a loop that burns money and picks by vibes. Define the gate first.

Put the judgement in the emitted prompt as a judgement, not a table. The executing agent decides per task; give it the frame and the two failure modes.

## 4. Delegation contract

Every spawned agent gets, in writing:

- **Objective** and its done-condition, as one observable fact.
- **Allowed files** — the exact set it may write. Nothing else.
- **Inputs** — the files, screenshots or specs it needs, handed over directly.
- **Dependencies** — what must be finished first.
- **Output** — the artifact, and the form it comes back in.
- **Verification** — how it proves its own work before reporting.
- **Non-goals** — what it must not touch, especially adjacent things it will be tempted by.

An agent without allowed-files and a done-condition will expand its own scope. Every time.

## 5. Ownership and the librarian

**Exclusive ownership** for anything two agents would otherwise write at once: shared indexes, schemas, migrations, central configuration, baselines, editor instances, lockfiles.

**File ownership is not enough — the git index is shared too.** Three agents on disjoint files in one working tree still contend on `.git/index.lock`, and they interleave commits that contain each other's half-written work, which makes "the branch stays green" unverifiable. Pick one of two and write it into the prompt:

- **A worktree per concurrent writer**, each on its own branch, integrated by merge at the end. Costs disk, buys real isolation.
- **One committer.** Workers hand back patches or finished files; a single lane stages and commits. Simpler, and correct when the lanes are short.

Never emit parallel lanes without saying which of the two applies.

**The librarian is conditional.** Emit it only when the project actually maintains shared knowledge files that several agents would write — an index, a running log, a `CLAUDE.md` or equivalent. Then: one librarian agent, and only the librarian writes those files. Every other agent emits index entries and log lines as patch blocks for the librarian to apply. Single ownership is what keeps the branch clean.

Do not emit a librarian for a project with no shared knowledge files. It is overhead with nothing to own.

## 6. Paired planning and cross-rail review

**When the plan will drive more than a handful of downstream agents, write it twice — once per rail, in parallel, neither planner seeing the other's draft first.** Then swap: each hunts the other's mistakes — missing constraints, invented capabilities, unowned files, steps that cannot actually run in parallel. Merge into one plan, and reconcile every disagreement explicitly in `GOAL.md`. An unresolved disagreement is a blocker, not a footnote.

The same pairing is the default for architecture decisions and final review. **Cross-rail review beats same-rail review, because the two model families fail differently.**

Sometimes the plan is the deliverable and the implementation is trivial. Pay for the pair at planning time and save it at execution time.

Skip the pair for small, single-surface, reversible work. It is a real cost and it does not pay for itself on a two-file change.

## 7. Bridges and availability

Both rails can reach the other side. The rail decides who the *primary* agents are, never which capabilities exist.

**Every emitted routing section that depends on a bridge, plugin or MCP server carries a discovery line and a fallback:**

> Verify the bridge is available before routing across it. If it is not, run those lanes on this rail's own models and note the substitution in `GOAL.md` — do not stall, and do not silently drop the work.

Never assert a plugin exists. Never invent one.

**Effort tiers need the same treatment.** Every emitted routing section commands effort levels — high, xhigh, max — and an executing agent frequently cannot set the effort tier of the agents it spawns. Left unaddressed, it reports routing compliance it never performed and the whole section becomes decorative. So: **state which lanes depend on an effort tier, and what to do when the tier cannot be set programmatically** — raise it to the operator, or name the lane that degrades and say so in `GOAL.md`. A routing instruction with no mechanism behind it is worse than none, because it manufactures false confidence.

## 8. Prices

Prices move. They are data with a date attached, not knowledge.

- Emit a price line **only** when a routing decision in the prompt actually turns on relative cost.
- **Look the figure up before you state it**, and carry the date you verified it into the prompt.
- Never state a price from memory, and never "correct" one that looks stale — both produce a confident wrong number. The rail files deliberately carry no figures for exactly this reason; they describe the *gap* between tiers, which is durable, rather than the amounts, which are not.

## 9. What the emitted section looks like

```
# MODEL ROUTING & PARALLELISM
<one line: quality first, tokens second, longer runtime is fine>
<hard rules: no Fable, no paid latency, file ownership, tight context>
{{the chosen rail's roster and effort tiers — one rail only}}
<parallelism rule for THIS task: how many lanes, which surfaces, who owns what>
{{test-time compute verdict for THIS task, one or two lines}}
{{bridge discovery + fallback, if a bridge is used}}
```

Tailor the parallelism line to the actual work surfaces of this task. A generic "run agents in parallel" is worth nothing; "one agent per area, one per asset lab, one on tests — no two agents in the same editor instance" is worth a lot.
