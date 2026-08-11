# prompt-architect

Two independently invocable skills that compile rough intent into one standalone, copy-ready prompt for another agent. They generate prompts; they never execute them.

## Included skills

| Skill | Package path | Use |
|---|---|---|
| `prompt-architect` | repository root | General software, research, design, and execution prompts |
| `game-development-prompt-architect` | `skills/game-development-prompt-architect` | Game, engine, gameplay, plugin, tool, UI, asset-pipeline, and studio-orchestrator Goal prompts |

The generic skill remains at the repository root for backward-compatible installs. The game-development skill is self-contained and has no runtime dependency on the generic skill.

## Game-development edition

The game skill turns a small feature request or a full game concept into exactly one autonomous English Goal prompt. Its scale adapts to the work:

- a clear subtask compiles immediately;
- an ambiguous feature gets one focused question round;
- a full game gets a logically sequenced Director Interview whose answers are compressed after every round into a contradiction-free Decision Ledger;
- a main Goal can orchestrate independent sessions and recursively use the skill to compile fresh child Goal Packets.

There is no arbitrary maximum question count. Interviewing stops when another answer would no longer materially change player experience, scope, architecture, production routing, evidence, or risk.

The compiled Goal can include:

- current official workflows for Unreal Engine, Unity, Godot, or a custom engine;
- C++-first/Blueprint-friendly Unreal defaults with explicit Blueprint-only and C++-only overrides;
- adaptive Studio Cells, isolated branches/worktrees, session messaging, integration queues, and clean tooling boundaries;
- capability-first model routing with cost-aware escalation and fresh-session context control;
- creative ideation and production pipelines for image, video, audio, voice, music, shaders, and 3D assets;
- free-first visual planning with repository-native Mermaid/D2, draw.io, optional HacknPlan Personal, and Pencil;
- a strict Pencil MCP, Atomic Design, token, script, and real-GLSL workflow for game UI;
- autonomous knowledge curation across a global game-development brain and a project-specific graph brain;
- engine tests, packaged builds, playtests, visual/audio comparison, performance evidence, and target-platform gates.

Human approval remains mandatory for engine migrations, new costs/subscriptions, unclear rights or provenance, and irreversible external actions.

## Install

### Install the repository bundle

Clone the repository into a source directory, then copy or link the desired package directories into the host's skill directory.

Codex locations:

```text
%USERPROFILE%\.codex\skills\prompt-architect
%USERPROFILE%\.codex\skills\game-development-prompt-architect
```

Claude Code locations:

```text
%USERPROFILE%\.claude\skills\prompt-architect
%USERPROFILE%\.claude\skills\game-development-prompt-architect
```

For `prompt-architect`, install the repository root. For `game-development-prompt-architect`, install only `skills/game-development-prompt-architect`. The game package contains its own `SKILL.md`, metadata, references, and linter.

### Git sparse install of only the game skill

```powershell
git clone --filter=blob:none --no-checkout https://github.com/maystudios/prompt-architect.git prompt-architect-source
Set-Location prompt-architect-source
git sparse-checkout init --cone
git sparse-checkout set skills/game-development-prompt-architect
git checkout main
Copy-Item -Recurse skills/game-development-prompt-architect "$env:USERPROFILE\.codex\skills\game-development-prompt-architect"
```

Use the analogous `.claude\skills` destination for Claude Code. A normal clone still contains both packages and is the simplest development setup.

## Use

Invoke the general compiler as `$prompt-architect` or `/prompt-architect`.

Invoke the game compiler as `$game-development-prompt-architect` or `/game-development-prompt-architect`, for example:

```text
Use $game-development-prompt-architect to turn this cooperative survival-game concept into an autonomous Codex orchestrator Goal.
```

The emitted artifact is English, contains no fill-in placeholders, and is self-contained for a fresh executor. Conversation and interview questions remain in the user's language.

## Knowledge system

Game Goals reference two exact repositories:

- global game-development brain: <https://github.com/maystudios/VaultGameDevelopment>
- project-brain foundation: <https://github.com/maystudios/better-second-brain>

Workers query both but return knowledge packets. One curator writes, corrects stale claims in place, records empirical engine discoveries with reproduction conditions, and maintains meaningful graph links.

## Validation

General prompt:

```powershell
python scripts/lint_prompt.py prompt.md --budget standard
```

Game Goal:

```powershell
python skills/game-development-prompt-architect/scripts/lint_goal_prompt.py GOAL.md --engine unreal --main-goal
python skills/game-development-prompt-architect/scripts/test_lint_goal_prompt.py
```

The game linter checks required section order, engine-profile selection, unresolved placeholders, both exact brain repositories, the single-writer curator, observed-evidence language, version-control isolation, and all four human gate classes.

## Repository layout

```text
SKILL.md                                      generic prompt-architect package
rules/                                        generic rules and host rails
references/                                   generic templates and examples
scripts/lint_prompt.py                        generic deterministic linter
skills/game-development-prompt-architect/
  SKILL.md                                    game compiler and interview workflow
  agents/openai.yaml                          Codex UI metadata
  references/                                 engine, studio, knowledge, creative rules
  scripts/lint_goal_prompt.py                 deterministic Goal linter
content/Video Ia dev.txt                      provided research source, not shipped at runtime
```

## Design provenance

The game workflow incorporates the durable lessons from the supplied video description in `content/Video Ia dev.txt`: plan before production, isolate one coherent job per fresh session, end every job with a test, roll back only the failed unit, establish a visual/color bible, progress from placeholders to verified assets, keep procedural source scripts authoritative, and optimize game systems from measurements.

Time-sensitive engine and tool claims are separately verified against official documentation and recorded in the relevant engine references.

## License

MIT. See [LICENSE](LICENSE).
