# RULE 01 — INTAKE, GAPS AND THE QUESTION PROTOCOL

How a brief becomes a decided specification before a single line of prompt is written.

## 1. Parse

Extract, verbatim where possible:

- **Mission signal** — what outcome is wanted, in the user's own words.
- **Hard constraints** — anything phrased as must, never, only, stays, don't. A hard constraint is never downgraded to a suggestion during compilation.
- **Named artifacts** — files, paths, branches, specs, reference folders, screenshots, URLs, apps, levels, endpoints.
- **Prohibitions** — what must not change, not be touched, not be built now.
- **Quality bar** — every prestige adjective, listed for translation.
- **Environment signals** — repo or no repo, host, engine, framework, CLI, MCP servers, plugins.
- **Autonomy signal** — "just do it" vs "plan with me first".

Never reinterpret a hard constraint. If the user says "the map stays inside the plugin content", that sentence survives into SCOPE intact.

## 2. Classify

Along these axes. The classification decides which modules load.

| Axis | Values |
|---|---|
| Domain | ui-ux · web-frontend · mobile-flutter · backend-api · data-db · game-unreal · research-knowledge · creative-media · none of these |
| Shape | greenfield · rebuild · scoped slice · improvement pass · investigation · plan-only |
| Autonomy | autonomous to completion · plan then approval gate · approval per step |
| Quality type | objective (testable) · subjective (judged) · mixed |
| Size / risk | small-reversible · medium · large-or-irreversible |
| Environment | repo present · no repo · engine/editor · browser · none |
| Knowledge need | none · web research · second brain · both |

**Mixed is the normal case.** A backend change with a dashboard is objective plus subjective; load both verification tracks.

## 3. Interrogate before you ask

Run `rules/02-thinking.md` **before** the Frame round. Most apparent gaps dissolve under one level of decomposition, and the ones that survive are the questions actually worth a user's attention.

Concretely: for each gap, ask yourself *why* the answer would change the prompt. If you cannot name the two prompts that would result from the two plausible answers, it is not a question — it is a decision you are avoiding.

## 4. Classify every remaining gap

| Class | Definition | Action |
|---|---|---|
| **Inferable** | A senior professional in this domain would pick the same default without asking | Decide. Write it concretely. List in the preamble. |
| **Preference** | Several defensible answers, none changes the work materially | Decide. Mention only if non-obvious. |
| **Material** | Plausible answers produce substantially different work | Ask. |
| **Blocker** | The task cannot be represented coherently or safely without it | Ask. Do not generate until answered. |

"Inferable" is the default class. Reach for it. Friction on things a professional would just decide is the most common way this skill gets annoying.

## 5. The Frame round — one call, ≤4 questions

One `AskUserQuestion` call. Never a sequence of single questions. Skip anything already answered in the brief.

**Slot 1 — Execution host (always asked).**
> Which environment will run this prompt?
> · Claude Code · Codex

**Detection:** you are running inside one of them. Claude Code exposes its own tool surface and `~/.claude/`; Codex exposes `codex exec` and its own config. Use whichever you are demonstrably in as the pre-selected option and label it as detected. **When detection is not conclusive, pre-select Claude Code and say it was a guess** — do not silently pick.

Ask anyway, even when detection is certain: the user is often writing a prompt to paste into the *other* tool. This answer selects the single rail that gets emitted.

**Non-interactive invocation.** When `AskUserQuestion` is unavailable — a headless run, a piped invocation, a subagent — the Frame round cannot run. Do not stall and do not skip the decisions. Take this fallback set and list all four in the preamble as stated assumptions the user must check:

| Slot | Non-interactive default |
|---|---|
| Host | the detected host, or Claude Code when detection is inconclusive |
| Git landing | the current branch, by name, read from the repository |
| Second brain | none, unless a vault-shaped directory is present and the brief references it |
| Length | standard |

**Slot 2 — Git landing (asked whenever a repository is in play).**
> Where should the finished work end up?
> · On the current branch `{{actual current branch}}` · On a new branch cut from it · On a new branch off `{{actual base branch}}`, merged back when green

Read the real branch names first. Never offer generic ones.

Three environment states, not two:
- **Repository present** — offer its actual branch names. On a freshly `git init`ed project with no commits, `git branch` returns nothing and `HEAD` is unborn; read it with `git symbolic-ref --short HEAD` and offer that.
- **No repository** — drop this slot, state in SETUP that no version control is present, and drop the git clause from DEFINITION OF DONE.
- **Environment not located** — the brief names an app or project you cannot find on disk. Do not claim there is no version control, and do not offer invented branch names. Use the described-role escape in `rules/00-core-contract.md` §Placeholder ban: write the prompt against "the repository's default branch" and require FIRST ACTION to discover and record the literal name.

**Slot 3 — Second brain (asked whenever unspecified).**
> Is there a knowledge base / second brain for this project?
> · No · Yes — at a path I'll give you · Yes — `{{detected vault path}}`

Look for an obvious vault, `docs/`, `notes/`, `.obsidian/` or similar before offering. A detected path as a concrete option is worth far more than an open question.

**When an answer contradicts the brief, the answer wins — and you say so.** The Frame round is later in time and more specific than the brief, so treat it as a correction, not a conflict. But never absorb it silently: name the contradiction in the assumptions preamble as *from → to*, and check what else it invalidates. An answer of "Codex" against a brief that named Claude Code changes the whole routing section; an answer of "no second brain" against a brief that referenced vault notes means those notes are ordinary files, not a knowledge base.

If the contradiction makes the mission itself incoherent — not merely different — that is a blocker. Ask one question in the Assumption round rather than generating something that cannot be executed.

**Slot 4 — the highest-value remaining question.** In priority order:
1. A mission or scope ambiguity that would send the work in a materially different direction.
2. The verification bar, when the task's "done" is genuinely unclear.
3. Length: standard (10,000–15,000 characters) or compact (under 4,000).

Length defaults to standard and only claims the slot when nothing outranks it, or when the user hinted at a size constraint.

**When several Material gaps compete for slot 4** — and a brief like "verbessere die UI/UX" produces four at once: which surface, which app, what "besser" means, what the bar is — do not exceed the four-question ceiling and do not generate on an unresolved Material gap. **Collapse them into one multi-select** naming the competing readings, take the answer, and decide the rest yourself with each decision listed in the preamble. One question that resolves the branch beats four that resolve the wording.

## 6. The Assumption round — only when it earns itself

Run **at most one** further round, ≤3 questions, and only when material gaps survived the Frame round.

Frame it as assumptions, not as an interview. State what you would otherwise assume, and let the user confirm or redirect:

> I'd otherwise assume: the existing state layer stays and only the widget tree is rebuilt. Confirm, or say what changes.

**Skip this round entirely when** the user said "use defaults", "entscheide selbst", "sinnvolle Defaults", or equivalent — **with two exceptions**:

1. **A blocker under §5.** A Frame answer that makes the mission incoherent still gets its one question.
2. **A Frame slot whose own preconditions failed.** Slot 2 needs real branch names to offer them; if the project could not be located, the slot could not be posed properly and the gap survives into a round "use defaults" would otherwise cancel. Ask it.

"Use defaults" authorises inference. It does not authorise generating something that cannot be executed, and it cannot retroactively answer a question the Frame round was unable to pose.

**Two rounds is the hard ceiling.** After the second round, decide everything remaining and generate. A third round is a failure of the first two.

## 7. Minimum viable brief

A mission signal is enough — one sentence naming a desired outcome — provided the Frame round runs.

Below that: no mission signal at all, or a request whose object cannot be identified. Then ask one question: what is the outcome you want. Nothing else.

## 8. Preamble contents

Everything you decided rather than were told, in the user's language, above the code block:

- inferred defaults that materially shape the prompt
- the sharpening you applied to a vague mission, stated as *from → to*
- capabilities the prompt assumes and how it verifies them
- anything deliberately left out of scope
- the length budget used, and what was compressed to hit it

Three to eight lines **when the brief was specific**. Where a vague brief required extensive sharpening, the sharpening is listed in full and the other categories compress to one line each — on a one-sentence brief the sharpening *is* most of the work, and hiding it under a line cap defeats the point of showing it. The ceiling protects the user from a wall of restated prompt, not from the decisions you made on their behalf.

This is the user's chance to catch a wrong turn before running a long job — make it scannable, not exhaustive.
