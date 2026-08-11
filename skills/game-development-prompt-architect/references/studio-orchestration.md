# Studio Orchestration and Goal Packets

## Adaptive Studio Cell

Scale roles to independent risk, not to a theatrical org chart. A small feature may need one executor plus a final curator. A full game can use an orchestrator with focused sessions for gameplay, engine/tools, UI/UX, art/technical art, audio, narrative/content, QA/performance, build/release, and knowledge curation.

A role is a responsibility. Instantiate it as an in-process subagent for short, context-adjacent work; as an independent session/task for long, conflict-prone, or context-heavy work; or fold it into the orchestrator when separation adds no value.

## Main orchestrator duties

- maintain the Goal, Decision Ledger, dependency graph, interfaces, risk register, and integration queue;
- compile child Goal Packets with this skill before starting independent sessions;
- route models and tools dynamically from detected capabilities;
- enforce isolated branches/worktrees or the version-control equivalent;
- serialize merges into the testing/integration branch;
- reject unverified handoffs and temporary-project pollution;
- keep human-facing planning views synchronized with canonical repo state;
- run or delegate final project-brain curation through one writer.

## Goal Packet schema

Every independent session receives a self-contained packet with:

1. outcome and player/product rationale;
2. relevant Decision Ledger slice and non-goals;
3. owned files/systems and prohibited surfaces;
4. input/output interfaces and dependency commit IDs;
5. exact engine version, tools, branch/worktree, and execution host;
6. acceptance tests, visual/playtest evidence, and performance budgets;
7. knowledge sources to query and the knowledge-packet return format;
8. commit/handoff contract and the party responsible for integration.

No child session relies on parent chat history. Give it the smallest sufficient graph neighborhood rather than the whole project context.

## Parallelism

Parallelize only jobs with stable interfaces and non-overlapping ownership. Build interface contracts or thin vertical seams first. Keep tightly coupled scene, prefab, asset-database, map, or binary edits serialized.

Use a dependency graph with ready/blocked states. The orchestrator starts work only when inputs are available. If cross-session messaging exists, workers notify the orchestrator with commit, tests, artifacts, caveats, and knowledge packet. Otherwise use a committed handoff manifest as the durable protocol.

## Integration queue

One integrator at a time rebases or merges the next verified unit into a testing branch, reruns affected tests, inspects engine imports/serialization, and records the result. A later worker integrates against the new testing head. Git or Perforce resolves history; the integrator owns semantic conflict resolution.

Failed integration returns only that unit for repair. Do not roll back unrelated successful work. Main receives only a coherent, verified milestone according to the repository policy.

## Tooling hygiene

- Keep durable reusable developer tools in a dedicated sibling Tooling Lab repository when practical.
- Keep one-off scratch files outside production paths and remove them before handoff.
- Do not merge diagnostic dumps, duplicate converters, temporary captures, ad hoc agents, or generated caches into testing/main.
- If a useful tool is intentionally archived, record its source and purpose on a tooling branch or in the Tooling Lab; do not burden every new worktree with it.
