# WORKED EXAMPLES

Two compiled prompts. Read these for voice calibration before writing your first one.

Both pass `scripts/lint_prompt.py`. Neither contains a placeholder.

---

## Example A — standard length, Rail A (Claude Code), subjective UI work

**Brief received:** "Die Home-Seite unserer Haushalts-App ist langweilig, die spiegelt nur die anderen Tabs. Mach die besser. Nimm sinnvolle Defaults."

**Frame round answers:** Claude Code · stay on `feat/home-dashboard-uplift` · vault at `Vault/` · standard length.

**Assumptions preamble that went above the block** — this is half the output contract, so it is shown as it was actually written, in the user's language:

> Ich habe "besser" übersetzt in vier prüfbare Eigenschaften: ein Gesamtstatus aus allen fünf Bereichen statt fünf Zählern nebeneinander, alles Überfällige/Unzugewiesene/Heutige ohne Scrollen auf dem kleinsten Gerät, kein Element ohne eigenen Informationswert, und jeder Tap landet auf dem konkreten Eintrag statt auf dem Tab.
> Angenommen: die fünf Feature-Tabs sind fertig und bleiben unangetastet — der Prompt schließt sie explizit aus.
> Angenommen: kein Backend- oder Sync-Anteil. Die Aggregation liest nur aus den vorhandenen Repositories.
> Angenommen: deutsche UI-Texte bleiben deutsch; der Prompt selbst ist englisch, und er weist den Agent an, englisch zu arbeiten.
> Entschieden: `docs/product-direction.md` ist bindend für die Features, aber zur Home-Seite schweigt es — dieses Schweigen ist die Aufgabe, nicht eine Lücke zum Melden.
> Entschieden: Domänenprofil `ui-ux` plus `mobile-flutter`, Standardlänge, drei Blind-Lanes für die subjektive Bewertung.
> Nicht enthalten: Navigationsstruktur und Theming — sag Bescheid, falls das mit hineinsoll.

```markdown
# SETUP
Work, think and report in English. English costs fewer tokens per unit of meaning than German, and every agent turn in this run pays that tax. The one exception: user-facing strings in the app stay German.
Persist this brief as `GOAL.md` before touching code, then work against that file — not against this message. Long runs get compacted; the file will not.
You are on `feat/home-dashboard-uplift`, cut from `main`. Never commit directly to `main`. Small commits per verified step, branch always green.
Run autonomously to completion. Stop only for blocking ambiguity or an external side effect. Report compactly: what shipped, what is verified, what is next. No long recaps.

# MISSION
`lib/features/home/` currently renders a list of counters that repeat what the Kalender, Aufgaben, Einkauf, Essensplan and Notizen tabs already show. It adds nothing. Rebuild it so that a user opening the app knows **what needs their attention right now** without opening a single tab.

Concretely, the finished screen is done when all of these hold:
- It states an overall household status at a glance, derived from the five feature areas — not five separate numbers side by side.
- Anything overdue, unassigned, or happening today is visible above the fold on the smallest supported device without scrolling.
- Every element on the screen either tells the user something they could not get from a tab label, or routes them to the exact place that resolves it. Nothing is there to fill space.
- Tapping any element lands on the specific item, not on the tab root.

"Besser" means those four properties. It does not mean more content, more cards, or a redesign of the other tabs.

This is a slice: the home screen and the aggregation it needs. The five feature tabs are finished and stay as they are.

Priority when they compete: comprehension at a glance beats completeness, and completeness beats visual novelty.

# SOURCE OF TRUTH / REFERENCES
`docs/product-direction.md` is binding for what the five features do and what data exists. It is silent on the home screen — that silence is the work, not a gap to be reported.
The existing tab screens are directional: match their spacing scale, type scale and component vocabulary so the new screen reads as part of the same app. Do not copy their layout — the home screen has a different job.
Where the direction document and the shipped behaviour disagree, the shipped behaviour wins for this task, and the disagreement gets one line in `GOAL.md`.
Log every deliberate departure from the existing design language in `GOAL.md`: what the app does elsewhere, what you did here, why.

# SCOPE
In scope: `lib/features/home/`, a read-only aggregation layer over the five existing repositories, new shared widgets where a component genuinely recurs, and the tests for all of it.
Out of scope: the five feature tabs, the data model, the persistence layer, navigation structure, theming, and any backend or sync work. If the aggregation needs a repository method that does not exist, add the method — do not restructure the repository.
If the work turns out to require materially different changes, stop and ask. Do not silently expand.
No publishing, no store submission, no dependency additions without asking.

# FIRST ACTION
Read any existing `GOAL.md` first and append a dated section rather than replacing it. Record: the mission above, the four acceptance criteria as separate testable items, the aggregation rules you decide on, decisions taken, open risks.
Then capture the baseline before changing anything: run the app, screenshot the current home screen on the smallest and largest supported device sizes, in light and dark, at default and 200% text scale. File them under `docs/evidence/home-baseline/`. These are the before-shots the final comparison is made against.
Read the five feature repositories and write into `GOAL.md` exactly what data is available for aggregation. You cannot design the status logic before you know what it can be computed from.

# WORKING METHOD (mandatory)
Work as a senior product designer who writes the Flutter code themselves: spec-driven, evidence-driven, never ad hoc.

Per step:
1. Read `GOAL.md`, the relevant feature code, and the Vault first. Never build on assumption.
2. Define what done looks like for this step and how you will see it — which screenshot, which test.
3. Split into small steps; implement one at a time.
4. After every step: run it, capture it, look at it, judge it against the mission, fix it. Confirm before the next step.
5. Refactor as you go: honest names, no widget over 100 lines, no business logic in the widget tree.

**Interrogate before you implement.** "What belongs on a home screen" has no general answer — it has an answer for *this* household app, for *this* data. Decompose it: what does a person open this app to find out? What are they most often too late for? Which of the five areas actually produces urgency, and which is just a list? Answer those from the data and from the Vault before you place a single widget.

**Build in dependency order.** The aggregation rules come before the layout; the layout comes before the polish. A home screen designed before you know what it can compute is a home screen that mirrors tab labels — which is the bug you are fixing.

**Re-plan when a branch exposes a prerequisite.** If the aggregation needs a repository method or a shared widget that does not exist, build that first and record the reordering in `GOAL.md`. That is expected, not a detour.

**When a step is genuinely blocked, write the TODO in `GOAL.md` with the reason.** Never assume past a blocker.

On a stall, walk the ladder in order before reaching for a stronger model: scope → framing → context → tooling → execution → capability. Two failures at top effort means the task is mis-scoped, not under-powered — re-cut it.

# UI/UX
Build one system, then build every element against it. Do not improvise per card.
- **Status before detail.** The overall state reads first, the areas that need action read second, the individual items read third. Verify that order on a screenshot, not in your head.
- **Encode urgency in something pre-attentive** — colour, weight, position — not only in text. A user scanning for two seconds does not read labels.
- **Every element is a destination.** If tapping it does not go somewhere specific and useful, it should not be on this screen.
- **No dark patterns.** No manufactured urgency, no counts inflated to look busy, no nagging. If nothing needs attention, the screen says so calmly and looks finished — an empty state is a designed state, not a fallback.
- **States are part of the design:** loading, empty, all-clear, error, and stale data. Design all five. The all-clear state is the one users will see most often and the one that gets forgotten.
- Layout holds at the smallest and largest supported size, in light and dark, at 200% text scale, with no overflow.

# TESTING & VERIFICATION
- `flutter analyze` clean, zero warnings. `flutter test` green.
- Widget tests for the aggregation logic: overdue, due today, unassigned, all-clear, and empty-household. These are the rules the screen is built on — test the rules, not the pixels.
- An `integration_test` that opens the app, taps each element on the home screen, and asserts it lands on the specific item rather than a tab root.
- Golden tests for the five designed states, on one reference device size.
- Manual capture on the smallest and largest supported size, light and dark, default and 200% text scale, for each of the five states. File under `docs/evidence/home-final/`.
- **Never report a visual result you have not looked at. Screenshot or it did not happen.**
- Break each new test once on purpose to prove it bites, paste the failing output into `docs/evidence/`, and restore the test in the same commit.

Because "reads at a glance" is judged and not measured, run three independent evaluations on the captured screenshots, with fresh agents that have not seen the code or these instructions:
1. **Blind expert review** — a senior mobile product designer, screenshots only. Ask what reads first, second and third; what looks tappable; where hierarchy is unclear. Open questions before any specific one.
2. **Blind user simulation** — a persona running the real app: a parent with ten seconds before leaving the house who wants to know if anything is unhandled today. Give the situation and the goal, never the path. Record first-attempt success, missteps, hesitation, and whether they abandoned.
3. **Neutral perception probe** — one screenshot, no context, no persona. Ask what this screen is for, what the primary action is, and what looks inactive.
Do not tell any of them what you intended or what earlier reviewers found. Merge findings by severity and evidence.

# SECOND BRAIN / RESEARCH
Search `Vault/` before web search and before implementing — try 2-3 phrasings. Read how the Vault documents its own conventions and follow them.
The Vault is accumulated own knowledge: high quality, but frozen at the moment it was written. The web is broad, current and unverified. Consult both and form your own view — there is no fixed order.
Correction mandate: the Vault is NOT infallible. Wrong, outdated or version-mismatched → fix the note in place, corrected, sourced and concise, marked with the word `Corrected`, the date, the claim it replaced, the source, and the Flutter version verified against. Record **how the failure arose**, not only the fix — the failure mode prevents the whole class, the fix prevents one repetition.
Expansion mandate: a conclusion drawn is a note written. Thin topic → research it now, that is part of the job. Where the Vault documents only dark patterns, the calm counterpart belongs beside them. File the conclusion, not the link list.
Guarantee coverage for: dashboard and summary-screen patterns, glanceable information hierarchy, pre-attentive encoding of urgency, empty and all-clear state design, Flutter layout under large text scale.

# MODEL ROUTING & PARALLELISM
Max quality at the lowest token cost that delivers it. Longer runtime is fine; wasted tokens are not. Never use Fable. Never buy latency — no `/fast`, no priority tier; throughput comes from parallelism, which is free.
- **Opus** (high; xhigh for the aggregation design and the final merge): the aggregation rules, the information hierarchy, screenshot critique, and the final review.
- **Sonnet**: widget scaffolding, mechanical refactors, test boilerplate, and the blind reviewers — a naive reviewer must be uncontaminated, and a cheap fresh context is exactly right for that.
- **Codex Rescue bridge** — verify it is installed before routing across it. If it is absent, run these lanes on Sonnet and a second Opus and note the substitution in `GOAL.md`.
  - `gpt-5.6-sol` (xhigh): challenge the aggregation design once, before it is built. Cross-rail review beats same-rail review because the two families fail differently.
  - `luna` (max effort only): Vault sweeps and web research on dashboard patterns — small closed tasks, each with a stated done-condition.
- Three lanes in parallel: one on the aggregation layer, one on the widget system, one on research and tests. No two agents write the same file.
- **Test-time compute is worth it here, once.** Layout quality is subjective and the gate exists: build two candidate hierarchies, capture both on the identical device set, and run the blind lanes on both. Comparison is far more reliable than absolute judgement. Do not extend it past two candidates — beyond that you are paying for variation nobody can distinguish.
Keep context tight: hand each agent only its files. Integrate through commits, not assumptions.

# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
Not automatic. Run a pass only if the result does not demonstrably clear the bar. Never invent work. **Zero passes is a valid outcome** — if the gates are green and the blind lanes found nothing meaningful, say so and stop.
Pass 1 — run the app and review against: correctness (no analyzer warnings, all five states render, deep links land on the right item), layout (smallest and largest size, 200% text scale, dark mode, no overflow), UX (the reading order the blind lanes actually reported matches the intended one), robustness (correct on resume, offline, and with stale data). Log findings by severity with the evidence behind each, fix high and medium impact, re-test, add regression coverage.
Pass 2 — only after high-impact fixes: verify them, re-capture the same device set, re-run the blind lanes with **fresh evaluators who have not seen pass 1's findings**, stop.
Stop early if a pass finds nothing meaningful, if findings start repeating or contradicting each other, or if a fix turns a green gate red — then revert to the last green commit and stop.
Each pass ends by asking what would have prevented the finding, and writing that into `Vault/`.
Remaining findings become named `GOAL.md` backlog entries with severity — not another loop.

# DEFINITION OF DONE
- The home screen states an overall household status derived from all five areas — proven by the golden tests for the five states and by the final screenshot set.
- Everything overdue, unassigned or due today is above the fold on the smallest supported device — proven by the captured screenshots at that size, at default and 200% text scale.
- Every element routes to a specific item — proven by the green `integration_test` that taps each one and asserts the destination.
- Nothing on the screen merely repeats a tab label — proven by the blind expert review and the neutral perception probe, neither of which was told what the screen is for.
- The all-clear state is designed and reads as finished, not broken — proven by its golden test and its screenshot.
- `flutter analyze` clean and `flutter test` green on `feat/home-dashboard-uplift`.
- `GOAL.md` current: final scope, aggregation rules, decisions, deviations, backlog. Vault corrections applied where errors were found.
- The finished work is on `feat/home-dashboard-uplift` and nowhere else. Every branch and worktree created while exploring is merged into it or deleted; working tree clean, no stashes, no detached HEAD; the gates above are green on that branch.
- Accepted leftovers recorded in the `GOAL.md` backlog with severity. Nothing silently dropped.
```

---

## Example B — compact, under 4,000 characters, Rail B (Codex), objective backend work

**Brief received:** "Prompt für Codex: der Bestell-Endpoint macht doppelte Bestellungen wenn das Handy im Tunnel den Request wiederholt. Fix das. Kurz halten, unter 4000 Zeichen."

**Frame round answers:** Codex · new branch off `main`, merged back when green · no second brain · compact.

**Assumptions preamble that went above the block:**

> Angenommen: der Idempotenz-Key kommt vom Client als Header — der Prompt lässt die Wahl zwischen Client-Key und Payload-Fingerprint aber bewusst offen und verlangt, die Entscheidung mit Begründung zu protokollieren, weil das die eigentliche Designfrage ist.
> Entschieden: die Nebenläufigkeit wird über einen Unique-Constraint in der Datenbank gelöst, nicht per Check-then-Insert. Das steht als harte Vorgabe drin.
> Entschieden: kein Test-time compute — hier gibt es genau eine richtige Antwort.
> Nicht enthalten: Aufräumen abgelaufener Keys als eigenes Feature; der Prompt verlangt nur, dass Ablauf und Cleanup geprüft werden.
> Unter 4.000 Zeichen gebracht durch Kürzung der Begründungen, nicht der Gates: alle neun Sektionen und die Git-Endzustandsklausel sind vollständig.

```markdown
# SETUP
Work, think and report in English — fewer tokens per unit of meaning, and every turn pays it.
Cut `fix/order-idempotency` from an up-to-date `main`; never commit directly to `main`; small verified commits, branch green.
Persist this brief to `GOAL.md` and work against it. Autonomous; stop only for blocking ambiguity.

# MISSION
`POST /orders` duplicates an order when a client retries after a network timeout. Make it idempotent: a retry of the same logical order returns the original order and status code, and creates nothing.
Done means one row in `orders` for two identical keyed requests, concurrent duplicates resolving to one winner, and a different order from the same client never collapsed. A fix, not a redesign — request and response shapes are unchanged.

# SCOPE
In: the order creation path, its idempotency storage, its tests, the client contract docs.
Out: other endpoints, the payment integration, the order state machine, any schema change beyond what idempotency needs. Ask before anything materially different. No deploys.

# FIRST ACTION
Append to `GOAL.md`, never replace it: mission, acceptance criteria, key strategy, decisions, risks. Then reproduce the bug — a failing test that creates two orders from one retry. You have not understood it until it fails on demand.

# WORKING METHOD (mandatory)
Senior backend engineer: contract-first, test-first. Read the endpoint, its storage and its tests first; define each step's done-condition and the test that shows it; one step at a time; keep idempotency out of the handler.
**Interrogate first.** Decide what makes two requests "the same" — client key or payload fingerprint — name the failure each still allows, and record why. Guessing it is how idempotency bugs come back.
Enforce it in the database with a unique constraint, never check-then-insert: a race two processes interleave is not fixed by reading before writing.
On a stall, re-cut the task before escalating the model.

# TESTING & VERIFICATION
Integration tests against a real service and database, not mocks: reproduction green; same key twice returns one order and the original status; different keys create two orders; replay after expiry rejected; simultaneous duplicates resolve to one winner. Migration applied and rolled back on production data.
Break each new test once on purpose, paste the failing output, restore it in the same commit. Never report a result you have not observed.

# MODEL ROUTING & PARALLELISM
Max quality, min tokens. Never Fable, never Sol Fast or any paid latency tier.
`gpt-5.6-sol` (xhigh): key strategy, concurrency guarantee, migration plan. `luna` (max only, spawn freely): test scaffolding, log triage, docs. `terra` by exception.
Claude bridge if installed: Opus 5 for an independent read of the concurrency argument; else a second Sol.
Two lanes, implementation and tests, separate worktrees, one committer. **No test-time compute** — one correct answer exists.

# SELF-IMPROVEMENT — BOUNDED (0-2 PASSES)
Not automatic; zero passes is valid when every gate is green. Pass 1 only if confidence is short: re-read the concurrency path for interleavings the tests miss; check expiry and cleanup. Fix high and medium impact, re-test. Pass 2 only after high-impact fixes: verify, stop. If a fix turns a green gate red, revert to the last green commit and stop. Leftovers become `GOAL.md` backlog, not another loop.

# DEFINITION OF DONE
- A retried request yields one order row and returns the original response and status; concurrent duplicates resolve to one order; distinct orders never collapse — each proven by its own integration test.
- Migration applies and rolls back on production data — proven by the rehearsal output.
- `GOAL.md` and the contract docs state the key rules and expiry.
- Work is on `fix/order-idempotency`, merged to `main` green, feature branch deleted; every scratch branch and worktree removed; working tree clean, no stashes.
```
