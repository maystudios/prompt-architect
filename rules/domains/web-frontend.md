# DOMAIN — Web Frontend

**Trigger:** The task builds or changes how a web UI is implemented — component structure, state management, routing, data fetching, rendering or hydration strategy, or the bundle and performance budget — regardless of whether the visual design is final.

## Role to assign
A senior frontend engineer fluent in the target framework's rendering model, state management patterns, and browser performance characteristics.
Treats "it renders" and "it is correct under real data, real network conditions, and a real browser" as two separate claims.
Owns the boundary between server state, client state, and URL state as a design decision, not an accident of where a variable was first declared.

## Work sequence
1. Inspect the existing component tree, routing structure, state layer, and data-fetching pattern before adding code — new code that ignores the existing convention creates a second, competing one.
2. Define the slice's done condition as a rendered, interactive state plus a passing test, not "it compiles."
3. Decide data ownership before writing components: server state (fetched, cached, revalidated) versus client or URL state (open/closed, selected, form draft, current route param).
   This single decision prevents most of the stale-data and duplicate-fetch bugs that otherwise surface later.
4. Build the smallest vertical slice — one route or component wired to real data end-to-end — before generating sibling routes or components from it as a template.
5. Wire loading, error, and empty states for every async boundary the slice introduces, alongside the success path, not after it.
6. Verify the slice: unit test for logic, component test for render and interaction, real browser check for actual behavior — console, network tab, visual state.
7. Measure the slice's bundle and Core Web Vitals impact before merging, not after several slices have compounded the regression.
   A regression caught here costs one slice to fix; caught three slices later it costs a rewrite of the shared shell.
8. Extract a shared hook or component only once the pattern repeats a second time, not preemptively on the first instance.

## Decomposition hints
- **Data layer before components.**
  Decide the fetch, cache, and revalidate strategy before writing the component that consumes it — building the component first locks in an ad hoc fetch call that later has to be ripped out.
- **Layout shell and routing before nested pages.**
  Shared navigation, layout, and route structure exist before individual pages, or every page reimplements its own shell.
- **State ownership decided before it is split across components.**
  The obvious order — build the component, lift state up once it's needed elsewhere — produces prop-drilling and duplicate-source-of-truth bugs; decide server/client/URL ownership up front instead.
- **Tokens and styles are consumed, never re-derived.**
  Implementation pulls spacing, type, and color from the design system; it does not invent a parallel scale mid-component.
- **Error and loading states are built with the component.**
  Retrofitting a loading skeleton after the happy-path layout is done means reworking layout that assumed data was already present.
- **Rendering and hydration strategy is decided before component authoring.**
  Server/client boundaries, streaming, and static-vs-dynamic segments constrain what a component is even allowed to do — deciding this after the fact surfaces as a hydration-mismatch warning in production, not a compile error.
- **Shared abstraction is extracted after the second repetition, never before the first.**
  A hook or wrapper generalized from one caller guesses the wrong shape; wait for a real second use.
- **Bundle-affecting dependencies are vetted before adding.**
  A heavy library pulled in for one component is far cheaper to reject at import time than to code-split back out after it ships.

## Verification surface
- Unit tests for pure logic: reducers, selectors, utility functions.
- Component tests asserting behavior through what a user can see or do, not internal state, using a component-testing library.
- End-to-end browser tests for the critical flows across the touched routes.
- Real browser session: dev tools open, zero new console errors or warnings.
- Network tab inspected for actual requests fired — count, waterfall, duplicate fetches.
- Automated performance audit against the stated Core Web Vitals budget — LCP, INP, CLS.
- Bundle analyzer output for the change's size delta, initial load and route-level chunk.
- Type checker at zero new errors, where the codebase is typed.
- Performance trace captured under a throttled network/CPU profile matching the target device class, not an idle localhost run.
- Visual regression check on the touched routes whenever the change could shift layout, even unintentionally.

## Evidence artifacts
- Test run output — actual pass/fail counts — filed with the change, not a status claim.
- Performance report, raw numbers before and after, filed alongside the change.
- Bundle size delta, before and after, per route or chunk, recorded in the change description.
- Screenshot or short recording of the real browser session showing the feature working end-to-end, with a clean console visible.
- Network waterfall screenshot whenever data-fetching behavior is the subject of the change.
- A short note on the state-ownership decision (server, client, or URL) for any new state introduced.
- A note on which rendering or hydration mode (static, server, streaming, client) the touched route uses and why.
- The failing-then-passing test output when the change was test-driven, so the regression it prevents stays legible later.

## Common failure modes
- **Compiles-and-renders treated as done.**
  The component rendered once in isolation but was never exercised against real, loading, error, or empty data.
- **Duplicate source of truth.**
  The same value lives in server-cache state and local component state, drifting out of sync after a mutation.
- **Fetch-on-every-render.**
  A missing dependency array or absent caching fires the same request repeatedly, invisible until the network tab is actually checked.
- **Hydration mismatch.**
  Server- and client-rendered markup diverge — locale or date formatting, random IDs, a browser-only API called during render — and it surfaces as a runtime warning, not a compile error.
- **Prop-drilling papered over by a global store.**
  Reaching for global state to avoid passing three props down two levels adds indirection without fixing the coupling.
- **Unaudited imports inflating the bundle.**
  A full utility library imported for one function, or a component library added without checking tree-shaking, silently inflates every route's first load.
- **Loading and error states skipped.**
  Only the success path was ever exercised, so the first real network failure in production is the first time the error state is seen at all.
- **Focus and semantics left undone.**
  Route changes don't move focus, interactive elements render as unlabeled divs, and no design fix can repair that without a markup rewrite.

## Test-time compute verdict
Narrower than a visual-design task: most implementation questions have one correct answer.
A route either fetches the right data with the right cache behavior or it doesn't; a bundle either fits the budget or doesn't.
Brute-force variation is waste on scaffolding a route from an established pattern, wiring a documented API client, or a mechanical rename across components.
It earns its cost on genuinely wide problems: choosing a rendering or hydration strategy for a new app shell, closing a Core Web Vitals regression with no single obvious cause, or reproducing an intermittent race condition.
Spawn variations, gate each against the measured metric or the actual passing test, keep the winner.
Treat a flaky, hard-to-reproduce defect as license to spend more, not as an excuse to guess once and move on.

## Definition-of-Done clauses
- Every async boundary introduced has a working loading, error, and empty state, verified in a real browser session, not just the success path.
- Unit, component, and end-to-end tests for the changed surface pass, with the actual pass/fail count recorded.
- Core Web Vitals and bundle-size deltas are measured against the stated budget and filed as evidence; any regression is justified or reverted, not silently accepted.
- Zero new console errors, warnings, or hydration mismatches in a real browser session.
- State ownership — server, client, or URL — is documented at the point it was decided, not left implicit in whichever component needed it first.
- Type checker, linter, and build all pass clean on the changed surface, with no newly suppressed error.
