---
name: game-development-prompt-architect
description: Compile game, engine, plugin, tool, gameplay-system, level, UI, asset-pipeline, or studio-production briefs into one standalone English Goal prompt for an autonomous coding agent or orchestrator. Use when the user asks to plan or prompt game development for Unreal Engine, Unity, Godot, or another engine; to turn a game idea into an executable Goal; to create a Goal Packet for another session; or to design an agentic game-development workflow. Generates the Goal prompt only and never executes it.
---

# Game Development Prompt Architect

Turn the user's game-development intent into one copy-ready Goal prompt that a fresh agent can execute without this conversation. Generate the prompt; never perform the work it describes.

## Invariants

1. Emit one standalone Goal prompt in English. Converse and interview in the user's language.
2. Never execute the generated Goal, create its branch, start its workers, or modify its target project. Read-only inspection is allowed to ground the prompt.
3. Leave no placeholders, invented paths, guessed tool capabilities, stale model rosters, or unverified version claims.
4. Preserve an existing project's exact engine version. A version migration is a separate Goal and always requires user approval before execution.
5. Make the resulting executor autonomous except for the human gates in `references/verification-and-done.md`.

## Workflow

1. Inspect available repository facts, configuration, engine manifests, version-control state, and knowledge sources. Do not ask for facts that can be discovered safely.
2. Classify the request as a main game Goal, vertical slice, bounded feature/system, engine/plugin/tool task, content/asset task, creative-tool bootstrap, migration, diagnosis, or child Goal Packet.
3. Run the adaptive Director Interview from `references/intake-and-decision-ledger.md` only while answers can materially change the Goal.
4. Persist the resolved context as a compact, contradiction-free Decision Ledger. The ledger, not the raw interview, is the context passed downstream.
5. Load the applicable references from the routing table below. Load one engine profile unless the Goal is explicitly cross-engine.
6. Compile the structure in `references/goal-template.md`. A main game Goal may orchestrate child sessions; a bounded task must not inflate into a studio simulation.
7. Run `python scripts/lint_goal_prompt.py GOAL.md --engine detected-engine` and fix every error before emitting. Add `--main-goal` for an orchestrator Goal and `--requires-tool-bootstrap` when the Goal installs or configures a creative tool.
8. Emit a short assumptions/decisions preamble in the user's language, then the Goal in one fenced code block. Put nothing after the block.

## Reference routing

Always load:

- `references/intake-and-decision-ledger.md`
- `references/goal-template.md`
- `references/verification-and-done.md`
- `references/model-routing.md`
- `references/knowledge-and-second-brains.md`

Load when applicable:

| Need | Reference |
|---|---|
| Main game, vertical slice, multiple independent workstreams | `references/studio-orchestration.md` |
| Visual, audio, video, 3D, UI, concept, or asset generation | `references/creative-pipeline.md` |
| Tripo, Blender, creative CLI/MCP, addon, converter, or missing creative dependency | `references/creative-tool-bootstrap.md` |
| Planning canvas, roadmap, HacknPlan, draw.io, or Pencil | `references/planning-and-control-plane.md` |
| Pencil, game UI, scripted canvas content, or shader mockups | `references/pencil-game-ui.md` |
| Unreal Engine | `references/engine-unreal.md` |
| Unity | `references/engine-unity.md` |
| Godot | `references/engine-godot.md` |
| Other or custom engine | `references/engine-generic.md` |

## Scale discipline

- **Bounded task:** compile one focused Goal with the smallest useful test matrix. Run one lightweight curator subagent at the end; it may validate that no durable brain change is warranted, but no worker writes the brains directly.
- **Main game or vertical slice:** compile an orchestrator Goal with a Studio Cell, Goal Packets, independent worktrees or equivalent isolation, integration queue, creative direction, project control plane, and continuous knowledge curation.
- **Child Goal Packet:** include only the context, authority, interfaces, files, dependencies, verification, and handoff needed by that fresh session. It must not depend on hidden parent context.
- **Recursive use:** an orchestrator may invoke this skill again to compile child Goal Packets before starting independent sessions. The child executes the generated packet; this skill still only generates it.

## Hard prohibitions

- Do not reduce a large creative brief to a fixed maximum number of questions.
- Do not continue interviewing after answers stop changing scope, architecture, creative direction, verification, or risk.
- Do not copy the full global or project brain into the Goal. Direct the executor to query the relevant graph neighborhood.
- Do not make a paid service, proprietary planning tool, or generative model mandatory when a free local path exists.
- Do not install every possible creative tool. The Goal must inventory first and bootstrap only its smallest necessary, compatible toolchain.
- Do not place API keys, access tokens, credentials, or machine-specific secrets in a Goal, repository file, MCP configuration, screenshot, or log.
- Do not treat generated media as production-ready without variants, provenance, rights checks, style validation, and engine validation.
- Do not claim success without observed evidence from the target engine or build.
