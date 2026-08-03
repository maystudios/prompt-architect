# RULE 06 — TESTING & VERIFICATION

Two tracks. Objective work gets deterministic gates. Subjective work gets independent blind evaluation. Most real tasks get both.

## 1. Universal rules — every prompt

- **Choose tests from the real failure surface**, not from a coverage number. Ask where this actually breaks, then test there.
- **Integration and end-to-end over trivial unit tests.** Unit tests to pin a detail or unblock a change, not to inflate a count.
- **Exercise error, empty, loading and edge states.** The happy path is the part that was never going to fail.
- **Name the gates.** The exact command, the exact assertion, the exact measurement. "Tests pass" is not a gate; `flutter test && flutter analyze` with zero warnings is.
- **Never report a result you have not observed.** Screenshot, log line, test output, measured number — or it did not happen.
- **Break every new test once on purpose.** A test that has never failed has not been shown to bite. **Require the failing output as evidence and the restoration in the same commit** — otherwise the instruction costs nothing to claim and leaves the branch red if it was actually followed.
- **Retain the evidence.** File it where the DoD can point at it.

## 2. Choosing the evidence type

Match the evidence to what the requirement actually is. Most prompts need two or three of these, not all five.

| Requirement type | Evidence that settles it |
|---|---|
| Behaviour is correct | End-to-end and integration tests, green, named |
| A number must hold | The measurement, the budget, and the reading at final conditions |
| Something must look or feel right | Captured artifacts on a fixed surface plus independent blind review |
| A contract must not break | Contract or schema test, plus the migration rehearsal |
| A state must be reachable and recoverable | The scenario walked end to end, including the failure and the recovery |
| Nothing regressed | The baseline, re-run, diffed against the recorded one |

**Depth scales with size, risk and reversibility, not with ambition.** A one-file reversible change does not need a four-lane evaluation. An irreversible migration needs more than a green test run.

## 3. Subjective outcomes — the four blind lanes

Use these when the requirement is judged rather than measured: hierarchy, clarity, affordance, polish, composition, perceived quality, "does this feel right".

They are heuristic evidence. **Simulated personas do not replace human usability research** — say so in the prompt rather than overclaiming.

### Integrity rules — these are what make the lanes worth running

- Evaluate the **real artifact**: the running build, real screenshots, real video. Never a description of it.
- **Fresh agent context for every blind lane.** A reviewer that watched the work is not blind.
- Give each lane **the minimum context its role requires**, and nothing more.
- **Never expose** source code, implementation rationale, the desired diagnosis, prior findings, or the answer you expect.
- **Open questions before targeted ones.** Record what the reviewer found unaided before asking about a specific element — the order is the experiment.
- Give user simulators **a goal and a situation, never a click path**.
- **Keep the surface fixed across iterations**: same cameras, same states, same viewport, same exposure. Comparability is the whole point.
- **Use different model families for high-impact independent reviews** where available. Same-family reviewers share blind spots.

### Lane 1 — Primary self-review
Full context. Run the real result, capture every relevant state, compare against the mission, write concrete defects. Fast and implementation-aware. **Known bias: the author knows the intended interaction and unconsciously fills in missing cues.** That bias is exactly why lanes 2–4 exist.

### Lane 2 — Blind expert review
Visual and behavioural artifacts only. No code, no repository access. Persona: a task-appropriate senior specialist.
Ask, in this order: What reads first, second, third? What appears interactive, editable, selected, disabled? Where is hierarchy unclear? Which interactions lack visible feedback? Which choices violate platform convention? Does this meet the stated bar, and why not?

### Lane 3 — Blind user simulation
Black-box control of the running artifact. No code, no documentation. Persona: a realistic target user under plausible conditions, given a situation and a desired result.
Record: first-attempt success, the actual step sequence, misclicks and failed gestures, hesitation and backtracking, expectation mismatches, help needed, recovery from error, final success or abandonment.

### Lane 4 — Neutral perception probe
A small artifact set, almost no context, no persona.
Ask: What is this for? What is the primary action? What can be clicked, dragged, edited? What looks inactive? What would you expect next? What is ambiguous?
This isolates raw visual discoverability from expert interpretation and from task completion.

### Lane routing

| Situation | Lanes |
|---|---|
| Mechanical or non-visual change | Objective gates + Lane 1 |
| Static visual change | 1, 2, 4 |
| Interactive UI change with live control | All four |
| No runnable UI | 1, 2, 4 — replace Lane 3 with scenario-based artifact analysis, and state the limitation in the prompt |
| High-impact experience | Duplicate the critical blind lanes across model families |

## 4. The bounded evaluation loop

1. Capture baseline evidence on the fixed surface.
2. Run the applicable lanes and gates.
3. Merge findings by severity, confidence and supporting evidence.
4. Fix high and medium impact.
5. Add deterministic regression coverage wherever the finding can be pinned by a test.
6. Re-capture the same surfaces.
7. Re-run with **fresh evaluators who have not seen the earlier findings**.
8. Stop at the bound in `rules/07-self-improvement.md`. Record accepted leftovers as backlog.

## 5. Compiled section

Name the actual commands, the actual surfaces, the actual measurements for this task. Generic verification language is worth nothing — "run the tests" tells the executor nothing it did not already assume.

Compact form: the named gates, the "or it did not happen" rule, and one line naming which blind lanes apply.
