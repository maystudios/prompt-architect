# prompt-architect

A skill for **Claude Code** and **Codex** that turns a task brief into one standalone, copy-ready execution prompt for another agent.

It generates the prompt. It never executes it.

```
"bau mir ein Prompt, um die UI/UX meiner App zu verbessern"
        ↓
  three questions
        ↓
  a 14,000-character brief a fresh agent can execute
  with no access to the conversation that produced it
```

## Why

Agents fail less often because they lack intelligence than because they were handed a badly framed task. A prompt that says "improve the UI" produces a well-built wrong thing. A prompt that says *what needs attention right now is visible above the fold on the smallest supported device, proven by the captured screenshot set* produces the thing you wanted.

This skill does that translation, in one consistent structure, every time.

## What it produces

Nine required sections in a fixed order, plus conditional ones that have to earn their place:

```
# SETUP                        # TESTING & VERIFICATION
# MISSION                      # SECOND BRAIN / RESEARCH    (conditional)
# SOURCE OF TRUTH  (cond.)     # MODEL ROUTING & PARALLELISM
# SCOPE                        # SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
# FIRST ACTION                 # DEFINITION OF DONE
# WORKING METHOD
```

Principles the output enforces, whatever the task:

- **Every requirement carries its evidence.** "Code is clean" is not a completion criterion; "no cross-layer imports, the boundary test passes" is.
- **Never report a result you have not observed.** Screenshot, log line, measured number — or it did not happen.
- **Interrogate the task before solving it.** What does "sensible" mean *here*? Why is the existing thing shaped that way? The answer is often three steps from the stated task and is the whole solution.
- **One routing rail, matched to the host.** Claude Code or Codex — never both, never one the user did not pick.
- **Bounded self-improvement, 0–2 passes.** Zero is a valid outcome. Unbounded loops degrade.
- **Land on exactly one branch.** Branch and roll back freely while working; leave one clean integration point.
- **No placeholders.** No `<slot>`, no `TODO`, no `path/to/file`. A prompt with a hole is not copy-ready.
- **Always English**, and the prompt tells its executor to work in English — fewer tokens per unit of meaning, and every downstream turn pays that tax.

## Install

**Claude Code**

```bash
git clone https://github.com/maystudios/prompt-architect.git ~/.claude/skills/prompt-architect
```

**Codex**

```bash
git clone https://github.com/maystudios/prompt-architect.git ~/.codex/skills/prompt-architect
```

On Windows, clone to `%USERPROFILE%\.claude\skills\prompt-architect` or `%USERPROFILE%\.codex\skills\prompt-architect`.

## Use

Invoke it as `/prompt-architect`, or just ask — the description triggers on phrases like *"write me a prompt to…"*, *"bau mir ein Prompt für…"*, *"turn this into a brief"*.

It asks at most three or four questions in a single round:

1. **Which environment runs this prompt** — Claude Code or Codex. Decides the routing rail.
2. **Where the finished work lands** — offered with your repository's real branch names.
3. **Whether a knowledge base exists** for the project.
4. Only if something genuinely outranks it: a mission ambiguity, or the length.

Then it emits the assumptions it made, in your language, followed by the prompt in one code block, in English.

Say *"use defaults"* and the second round is skipped — the first is not, because those choices cannot be inferred safely.

## Length

| Mode | Body | Use |
|---|---|---|
| `standard` | 10,000–15,000 chars | the default |
| `compact` | ≤ 3,950 chars | fields with a hard 4,000-character limit |
| custom | any figure | interpolated between the two budgets |

The compact ceiling is 3,950 rather than 4,000 because the prompt ships inside a code fence, and someone copying the fences too must still clear the limit.

Character counts are **measured, not estimated** — a model cannot count characters, so a script does:

```bash
python scripts/lint_prompt.py your-prompt.md --budget compact
```

It errors on a missing or misordered section, a leftover placeholder, both rails named at once, a missing Fable or paid-latency prohibition, a missing English instruction, a missing git end-state clause, and a missing evidence rule. Thirteen fixtures verify it bites on each and stays quiet on legitimate content.

## Layout

```
SKILL.md                 router, pipeline, question protocol, output contract
rules/00…09              contract · intake · decomposition · sections · routing
                         second brain · verification · self-improvement · git+DoD · style
rules/rails/             claude-code.md · codex.md — exactly one is ever emitted
rules/domains/           ui-ux · web-frontend · mobile-flutter · backend-api
                         data-db · game-unreal · research-knowledge · creative-media
references/              template · worked examples · lint checklist
scripts/lint_prompt.py   deterministic character count and structure check
```

The split is deliberate: **a new model or a changed price touches exactly one rail file.** Model names never appear in the rail-independent core.

## Adapting it to your setup

The rail files describe one specific arrangement — a Claude-side and a Codex-side roster with a bridge between them. Yours will differ. Edit `rules/rails/claude-code.md` and `rules/rails/codex.md`; nothing else needs to change.

The rails carry **no price figures on purpose**. Pricing moves, and a stale number is worse than none because it produces a confident wrong choice. What they carry instead is the durable shape — the volume worker sits about an order of magnitude below the orchestrator — and an instruction to verify current rates before any decision turns on cost.

## License

MIT. See [LICENSE](LICENSE).
