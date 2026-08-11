# Knowledge and Second Brains

## Two-layer knowledge system

**Global game-development brain:** `https://github.com/maystudios/VaultGameDevelopment`

Use it for durable, cross-project knowledge about Unreal Engine, Unity, Godot, game design, testing, technical art, pipelines, performance, agent workflows, and recurring failures.

**Project brain foundation:** `https://github.com/maystudios/better-second-brain`

Initialize or detect a project-specific brain for the game, plugin, or tool. Use it for architecture, design decisions, lore, asset conventions, interfaces, experiments, performance baselines, build quirks, and project-specific corrections. Never overwrite an existing project brain blindly.

Every generated Goal must name both exact repository URLs above. Every Goal uses both layers: detect and query the project brain if it exists; otherwise initialize a project-local brain from the foundation without replacing project files or secrets. Keep initialization proportional, but do not silently omit the project layer for a bounded task.

## Read path

Before work, query both brains for the relevant graph neighborhood. Prefer project truth when it intentionally overrides a general pattern. Verify version-sensitive claims against the live project and current official documentation. Do not dump either entire vault into a Goal Packet.

## Write path

Workers do not write concurrently. They return a knowledge packet containing:

- claim or discovered technique;
- scope and engine/version/context;
- evidence type: official source, repository observation, engine run, benchmark, playtest, or controlled try-and-error;
- reproduction or falsification steps;
- confidence and known limits;
- notes likely superseded or contradicted;
- proposed graph links and why they are meaningful.

A single curator agent owns final writes. For a bounded task it runs once at the end as a lightweight subagent and may record that no durable change is warranted. For a long orchestrator Goal it may run periodically and at milestone completion. Workers never write either brain directly.

## Curation rules

- Empirical discoveries are valid knowledge. Label how they were observed and preserve reproduction conditions.
- Correct wrong notes in place; do not merely append a conflicting note.
- Preserve useful history when a rule changed by engine version, platform, or project context.
- Link causes, symptoms, systems, tools, constraints, tests, and alternatives—not just obvious category siblings.
- Check backlinks, orphaned nodes, duplicate concepts, broken sources, and graph reachability.
- Distinguish fact, hypothesis, preference, project convention, and deprecated guidance.
- Never promote secrets, credentials, private user data, licensed source assets, or unreviewed generated content.

The curator validates structure, source/provenance, contradictions, and link quality before completing the Goal.
