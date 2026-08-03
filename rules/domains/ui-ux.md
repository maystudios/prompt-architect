# DOMAIN — UI/UX

**Trigger:** The task changes what a user perceives, understands, or can do — layout, hierarchy, states, motion, copy tone, information architecture, a design system, or accessibility — independent of which framework or platform renders it.

## Role to assign
A senior product/UI designer with interaction-design and accessibility fluency.
Owns the system — tokens, states, motion — as much as any single screen; a screen that breaks the system is not done, it is a new system.
Treats "looks finished" and "works for a first-time user" as two separate claims, and never signs off on the first as proof of the second.

## Work sequence
1. Inventory what exists: current screens, flows, and any design system already in place — tokens, type scale, spacing, color roles, motion curves. State explicitly if none exists rather than assuming a blank slate.
2. Map the target flow end-to-end: entry point, happy path, every branch, error/empty/loading states, exit — before styling a single screen.
3. Define or extend the shared system first: grid, type scale, spacing scale, color roles, elevation, motion curves, and the full state set every interactive element must support.
   Treat this as the single most leveraged decision in the task — every later screen inherits it, for better or worse.
4. Rank components by dependency: shared primitives — buttons, inputs, cards, form fields — before the composed screens that place many of them together.
5. Build or redesign one component or screen to completion: every applicable state, not just default, before starting the next.
6. Render the real artifact and run the applicable blind-evaluation lanes — expert critique, user-goal simulation, neutral perception probe — against it, not against the source.
   Prefer a fresh agent or a different model family for these lanes when the finding materially matters.
7. Rank findings by severity, fix, and re-render before calling the step done.
8. Fold the resulting decision back into the shared system doc or tokens so the next screen inherits it instead of re-deriving it.

## Decomposition hints
- **System before screens.**
  Per-screen spacing, type, and color decisions produce a product that reads like several products stitched together; settle the shared system first, then every screen consumes it.
- **Primitives before composites.**
  A button's hover, disabled, and loading states must exist before any screen that places ten buttons on it — building the screen first means restyling every instance later.
- **States ship with the component, not after.**
  Empty, loading, error, and disabled states built in a later pass fight the layout assumptions the default-state design already locked in.
- **The obvious journey-map order breaks on shared primitives.**
  Designing screens in the order a user encounters them feels natural but leaves the shared primitive layer undecided until the third screen needs it, forcing rework on the first two.
- **Real copy belongs in the same pass as layout.**
  Placeholder text never triggers the truncation, wrapping, or hierarchy failure that an actual long name, error message, or empty-state string will.
- **Motion comes after static hierarchy is proven.**
  Animating a transition between two screens that are individually unclear hides the unclarity instead of fixing it — prove the still frame first.
- **Accessibility and dark-pattern audit happen at build time, per component.**
  Retrofitting focus order, contrast, or a manipulative-flow fix across a finished system costs far more than deciding it during the build.
- **Breakpoints are their own decomposition axis.**
  Decide the smallest and largest supported size before building the middle — the middle looks fine by default and hides the overflow the extremes expose.

## Verification surface
- Rendered or interactive artifact, inspected directly — never source code — at the smallest and largest supported breakpoint.
- The same artifact in both color-scheme modes whenever dark mode is in scope.
- Contrast ratio measurement, text against background, per state, against the WCAG threshold the task targets.
- Manual keyboard-only traversal: every interactive element reachable, its focus visibly indicated, operable without a pointer.
- Independent blind lanes: expert critique on hierarchy and affordance, user-goal simulation on a realistic task, neutral perception probe on first impression.
- Each blind lane run against the artifact only, with no implementation context, prior findings, or expected answer leaked to the reviewer.
- State-matrix check: default, hover/focus, active, disabled, loading, empty, and error captured per component and compared side by side, not spot-checked on default alone.
- Automated accessibility linting (label presence, heading order, landmark structure) as a floor, not a replacement for the manual and blind-lane checks above.
- A recorded interaction session, not just static screenshots, whenever motion, drag, or a multi-step interaction is part of what's being judged.

## Evidence artifacts
- Before/after screenshots per breakpoint and color-scheme mode, filed with the component or screen name and date.
- Contrast and keyboard-traversal results as raw findings, not a paraphrase, filed alongside the screenshots.
- Full blind-lane transcripts — question asked, answer given, unedited — filed as the record of review, not summarized away.
- A state-matrix table, component by state by screenshot reference, for any component with more than a default state.
- The diff to the shared design-system doc or token file when the system changed, so the decision is discoverable for the next task.
- A one-line note on which blind lanes ran and which were skipped, and why, when live control or a rendered artifact was unavailable.
- A short list of components or screens explicitly out of scope for this pass, so missing evidence there reads as a boundary, not an oversight.

## Common failure modes
- **Per-screen improvisation.**
  Each screen invents its own spacing, type, or color instead of drawing from one system, and the seams show at every transition.
- **Default-state-only design.**
  Hover, focus, disabled, loading, empty, and error states are missing or unstyled because only the happy path was ever rendered.
- **Self-graded polish.**
  The builder reviews their own screenshots and reliably misses the blind spots their own implementation already had.
- **Placeholder content masking real defects.**
  Lorem-ipsum filler never wraps, truncates, or overflows the way a real name, error message, or long label does.
- **Motion covering unclear hierarchy.**
  A transition dresses up two screens that don't individually read — freeze either frame and the problem is still there.
- **Contrast and focus order retrofitted at the end.**
  Treated as a final lint pass instead of a build-time constraint, producing expensive rework or a shipped failure.
- **Leading questions in review.**
  "Doesn't this look clickable?" manufactures a pass that "what looks clickable here?" would not have given.
- **Dark patterns from local optimization.**
  A screen tuned in isolation for one metric introduces confirm-shaming or a disguised action with no one auditing the full flow.
- **Single-breakpoint testing.**
  The one width used during design is the only one ever checked, so the smallest and largest supported sizes ship broken.

## Test-time compute verdict
Wide solution space, subjective quality bar — pay for it.
A hero screen, a full rebuild, or a motion-feel problem has many valid answers and no deterministic test proves "good."
Spawn layout or motion variants, score each against blind-lane findings, keep the winner.
Pure waste on a settled system: applying existing tokens to a structurally identical new screen, or fixing a measured contrast failure with the one color that passes.
There is a single right answer in those cases, and variation search buys nothing over just producing it.
Spend the budget on the first screen of a new pattern, not the fortieth field that follows one already proven.

## Definition-of-Done clauses
- Every component in scope has its full applicable state set — default, hover/focus, active, disabled, loading, empty, error — rendered and screenshotted; inapplicable states are named as such, not silently skipped.
- Contrast measurement and keyboard-only traversal pass at the stated threshold, with raw results filed as evidence.
- Blind-lane review is complete against the rendered artifact, transcripts are filed, and every finding at or above the agreed severity is fixed and re-verified.
- Responsive check passes at the smallest and largest supported breakpoints, in every color-scheme mode in scope, with screenshots filed.
- The shared design system reflects every new or changed token, state, or pattern decision made during the task.
- No dark-pattern flag remains unresolved: every confirm-shaming, disguised-action, or forced-continuity pattern found in review is fixed or explicitly accepted with a stated reason.
