# Adaptive Director Interview and Decision Ledger

## Purpose

Ask enough questions to make the Goal correct, not enough to simulate progress. Large games may need many questions; clear subtasks may need none.

## Before asking

Inspect read-only context first:

- engine and exact version from project manifests;
- repository, current/base/testing branches, worktrees, CI, package/plugin manifests;
- existing GDD, roadmap, issue tracker, design system, screenshots, reference media;
- global and project second-brain locations;
- detected host capabilities, installed tools, MCP servers, and available model families.

Never ask the user to repeat a discoverable fact. Never infer an engine migration from a preference for a newer version.

## Interview modes

**Immediate compile:** Use when the task, target, constraints, and proof of done are already clear; for a complete child Goal Packet; or when the user says to decide autonomously. Record safe assumptions and compile.

**Focused round:** Use for a bounded feature with one or two material forks. Ask the competing decisions together.

**Director Interview:** Use for a main game, vertical slice, new project, or ambiguous creative brief. Ask coherent rounds, update the ledger after each, then ask the next round from what remains unresolved.

## Round order

Skip resolved topics. Do not ask all rounds mechanically.

1. **North star:** player fantasy, audience, platform, genre, session shape, success and failure experience.
2. **Creative identity:** visual language, tone, camera, interaction feel, audio identity, references and anti-references.
3. **Product boundary:** prototype/vertical slice/full production, must-haves, non-goals, business model, accessibility, localization, performance targets.
4. **Technical frame:** engine, exact version, language preference, target hardware, networking, persistence, build and distribution constraints.
5. **Production frame:** team/autonomy level, planning surface, milestones, source control, asset provenance, knowledge bases, integration policy.
6. **Proof:** automated tests, engine validation, playtest evidence, visual/audio acceptance, performance budgets, shippable artifacts.

Within a round, order questions so each answer narrows the next. Offer concrete mutually exclusive choices when they clarify tradeoffs, while allowing a free-form answer. Prefer questions that eliminate whole solution branches.

## Spoken interview delivery

When the user has requested spoken questions and the host exposes `$generate-voice-audio`, present every actual question round in accessible text and generate the same round with the user's selected Supertonic 3 iGPU path according to that skill. Batch the round into one coherent audio artifact rather than one file per sentence. Do not synthesize filler, status updates, or a question that the intake rules say to skip; voice changes delivery, not the information-gain stop rule.

## Decision Ledger

After every round, internally replace raw answers with a compact ledger:

| Field | Content |
|---|---|
| Decision | A resolved fact or explicit autonomous choice |
| Why | Player, product, technical, or risk rationale |
| Consequences | Constraints this creates downstream |
| Evidence/source | User statement, detected file, observed project state, or cited research |
| Confidence | confirmed, observed, inferred, or provisional |

Maintain separate lists for non-goals, unresolved risks, and human gates. Detect contradictions immediately and ask one reconciliation question only when the conflict materially changes execution.

The Goal receives the final ledger, not the transcript. Phrase it as direct project truth. Remove duplicate rationale and conversational history.

## Stop rule

Stop interviewing when the next plausible answer would not materially change at least one of:

- player experience or creative direction;
- scope or non-goals;
- engine architecture or implementation mode;
- workstream decomposition or model/tool routing;
- acceptance evidence or release risk;
- a non-delegable human gate.

Do not ask preference trivia. If two options are reversible and cheap, authorize the executor to test both and keep the evidence-backed winner.

## Non-interactive fallback

When questions cannot be asked, inspect first, choose reversible defaults, mark them as inferred in the preamble, and compile. Never bypass engine migration, new-cost, unclear-rights, or irreversible external-action gates.
