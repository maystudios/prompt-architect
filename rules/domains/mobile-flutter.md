# DOMAIN — Mobile / Flutter

**Trigger:** the task builds, extends, fixes, or polishes a Flutter mobile app — widgets, state, navigation, platform channels, or a store-bound release build.

## Role to assign
Senior Flutter engineer who ships to both the App Store and Play Store, not a web developer porting a layout.
Owns the app across its full lifecycle — cold start, background, resume, rotation, kill-and-relaunch — not just the screen currently open.
Treats iOS/Android divergence as a first-class design constraint, not an edge case to patch later.

## Work sequence
Refine the universal loop (inspect -> define done -> smallest step -> verify -> integrate) into these steps:
1. **Inspect the widget tree and state shape before writing a single widget.** Identify the current state-management pattern (Provider, Riverpod, Bloc, plain `setState`), the navigation setup, and any platform-channel boundaries the change touches.
2. **Define the step's done condition in device terms.** Name the exact screen, state transition, and platform (iOS, Android, or both) the step must satisfy, plus which size classes and text scale it must survive.
3. **Cut to the smallest vertical slice.** One widget, one state transition, or one platform-channel call at a time — never "the whole feature" as a single step.
4. **Settle the state model before the pixels that render it.** A widget bound to an undefined or partial state shape looks finished and breaks on the next rebuild.
5. **Implement the slice.**
6. **Verify on a real device or emulator, not just a clean compile.** `flutter analyze` passing proves nothing about resume, rotation, or async timing.
7. **Integrate against the real navigation stack, real theme (including dark mode), and real localization** — not an isolated widget harness.
8. **Re-run the full test surface before starting the next slice.** A green test for the new screen does not confirm the rest of the app still resumes cleanly.

## Decomposition hints
- **State model before widgets.** Decide how state flows (up/down, event/reducer, provider scope) before writing layout — widgets built against an undefined state model get rewritten once the shape is finally decided.
- **Navigation skeleton before screen content.** Wire routes and deep-link targets first; screens built in isolation quietly assume arguments or back-stack context that does not exist yet.
- **Platform-channel contract before either side of it.** Fix the method name, argument shape, and error contract before writing native or Dart code — writing the Dart side first invites silent argument drift on the native side.
- **Obvious-but-wrong: happy-path UI before empty/loading/error states.** Retrofitting error and empty states after the happy path is built usually means restructuring how the widget holds state, not just adding a branch.
- **Offline and slow-network behavior belongs in the first pass, not a final polish pass.** Deciding caching, retry, and optimistic-update behavior after the state shape is already committed forces a rewrite of that shape.
- **Design tokens (spacing, type scale, color roles) before screen-by-screen styling.** Styling screens one at a time without a shared token set produces visual drift no later pass fixes cheaply.
- **Lifecycle and resume handling is not a nice-to-have pass.** A screen that only works on first launch and breaks on backgrounding or rotation is unverified, not half-finished.
- **Plan both platforms from the start when the feature touches either.** iOS/Android divergence in permissions, back-button behavior, and safe areas is a decomposition axis, not an edge case to discover later.

## Verification surface
- **Static analysis.** `flutter analyze` clean with zero new warnings, not merely zero errors.
- **Unit and widget tests.** `flutter test` covering logic and state transitions.
- **End-to-end flow tests.** `integration_test` running real user flows on a real device or emulator, across screens, not single widgets in isolation.
- **Visual regression.** Golden tests for layout-sensitive widgets, pixel-diffed against a committed baseline image, never eyeballed.
- **Size-class pass.** Manual or emulator run at the smallest and largest supported screen size.
- **Text-scale pass.** Manual or emulator run at default and 200% text scale.
- **Dark-mode pass.** Every screen touched, not only the entry point.
- **Resume/lifecycle pass.** Background then foreground the app mid-flow (mid-form, mid-navigation) and confirm state survives or degrades safely.
- **Offline and throttled-network pass.** Airplane mode and a throttled connection, confirming a real state (cached data, retry affordance, explicit error) instead of an infinite spinner or crash.
- **Release-build pass.** The actual release configuration (signing, obfuscation/shrinking, permission manifest) completes a build, not just the debug configuration.
- **Platform round-trip test.** Both iOS and Android exercised when the change touches a platform channel, never one platform assumed to mirror the other.
- **Accessibility pass.** Screen-reader walkthrough (TalkBack/VoiceOver) confirming every interactive element has a correct semantic label and focus order.
- **Performance profiling pass.** Flutter DevTools timeline confirming frame build/raster time stays in budget and memory does not grow unbounded across a session.
- **Localization pass.** Every supported locale touched renders without truncation or overlap, including right-to-left layout where the app supports one.
- **Permission-flow pass.** Both the grant path and the deny path for any runtime permission are exercised, not the grant path alone.
- **Deep-link pass.** Cold start and warm start from the same link both land on the correct screen with the correct state.
- **Store-build metadata pass.** Icon, launch screen, and store metadata match the actual release build before submission, not a placeholder asset.
- **Cold-start timing pass.** Measure time-to-first-frame and time-to-interactive on a real device, not the emulator's typically-faster boot.

## Evidence artifacts
- **Screenshot or recording per state.** One per changed screen, per theme (light/dark), per extreme size class — filed as an image or video, not described in prose.
- **Raw tool output.** `flutter analyze` and `flutter test` output captured verbatim, not summarized as "tests pass."
- **Golden-test images.** Diff image on failure, committed baseline image on pass.
- **Integration run log.** `integration_test` log for the covered user flow.
- **Device identifier.** Device or emulator model and OS version used for the manual pass, recorded next to the screenshots — "verified on device" without naming the device is not evidence.
- **Lifecycle recording.** Screen recording of the resume and offline passes, since a static screenshot cannot show state surviving backgrounding.
- **Crash/ANR log.** Filed for any failure hit during verification, even after the fix, so the fix has a reproduction record.
- **Performance trace.** DevTools timeline or memory snapshot filed for any change touched by the performance-profiling pass.
- **Accessibility recording.** Screen-reader walkthrough capture or semantics-tree dump proving the accessibility pass actually happened.
- **Localization screenshot set.** One image per supported locale touched, including an RTL locale where the app supports one.
- **Permission-flow recording.** Both the grant and deny paths captured, not just the happy path.
- **App-size record.** Release binary size noted for any change touched by the performance-profiling pass, compared against the previous release build.
- **Cold-start timing record.** Time-to-first-frame and time-to-interactive noted per device tested, alongside the device identifier.

## Common failure modes
- **Claiming "it works" from source review alone.** Widget code that compiles and reads correctly can still rebuild in a loop, leak a controller, or dead-end a navigation stack — only a run proves it.
- **Rebuild storms from state scoped too high.** A `setState` or provider scope wrapping more of the tree than the changed data requires re-renders far outside the visible symptom.
- **Fixing the platform under test and shipping a regression on the other.** An iOS safe-area fix or an Android back-button fix verified on one platform only ships blind on the other.
- **Testing only the happy path at default text scale and light mode.** The most common agent-shipped regression is a layout overflow at 200% text scale or a contrast break in dark mode — because it was never rendered that way.
- **Treating analyzer-clean as done.** Analyzer-clean code with an unguarded async gap (`setState` after unmount, an unhandled `Future` error) fails silently in production, not in CI.
- **Skipping the resume path entirely.** Bugs that only appear after backgrounding — lost form state, duplicated network calls, stale providers — are invisible in a fresh-launch-only test pass.
- **Platform-channel argument drift.** Changing an argument's shape or name on one side without updating the other compiles cleanly and fails only at the call site, at runtime.
- **Mocking every network call and never once running against a real or realistic backend.** Widget tests with mocked responses pass while the real API's error shape or latency breaks the screen.
- **Silent scope creep into adjacent visual polish while fixing one widget.** Touching styling on nearby screens "while in there" turns a one-widget fix into an unreviewable diff.

## Test-time compute verdict
**Spend variation-search budget on new-screen visual layout and micro-interaction feel** — motion curves, spacing, empty-state copy — where several layouts pass every functional test but differ only in feel. Score candidates against a screenshot-based rubric or a blind review pass, keep the best, discard the rest.
**Spend it on jank and frame-time tuning** too, since the fix is empirical: try several rebuild-scope or widget-tree changes, measure frame time on a real device, keep the fastest.
**Spend it on onboarding and empty-state copy** when tone and conversion matter and several genuinely different phrasings are plausible — generate a few, check them against the same screenshot rubric.
**Do not spend it on scaffolding a new screen from an existing pattern, wiring a documented navigation route, a standard form-plus-validation screen, or a mechanical widget rename.** Those have one correct shape already fixed by the codebase's own convention — repeated attempts return the same answer at extra cost.
**Do not spend it on platform-channel plumbing** either — the method signature and error contract have one correct shape once decided; variation search there just multiplies debugging surface.
Default to a single careful attempt for anything a sibling screen in the same app already answers.

## Definition-of-Done clauses
- **Static analysis and tests pass clean** — `flutter analyze` and `flutter test` run with zero new warnings or failures, raw output attached.
- **Device matrix verified** — every changed screen checked on-device or emulator at the smallest and largest supported size, at 200% text scale, and in dark mode, one screenshot per state.
- **Lifecycle and connectivity proven** — the flow survives backgrounding and resuming mid-flow, and behaves correctly offline and on a throttled connection, each shown by a screen recording.
- **Real user flow covered** — `integration_test` exercises the actual flow touched by this change and passes against a real or realistic backend, not a mock-only harness.
- **Release build completes** — the release configuration (signing, shrinking/obfuscation, permission manifest) produces a finished build artifact, not just a passing config-file inspection.
- **Accessibility and localization checked** — a screen-reader walkthrough and a locale pass (including RTL where supported) are both recorded for every changed screen.
