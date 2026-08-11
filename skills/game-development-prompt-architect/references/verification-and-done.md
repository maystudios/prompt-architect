# Verification, Autonomy, and Done

## Evidence matrix

Select lanes by risk and map every requirement to at least one observed artifact:

1. **Static:** compile, syntax, schema, serialization, dependency, import, asset-validation, and linter results.
2. **Unit/component:** deterministic logic, calculations, state machines, data validation, editor utilities.
3. **Engine integration:** scene/map/prefab/actor lifecycle, physics, animation, shaders/materials, save/load, input, networking, editor/runtime boundaries.
4. **Build/runtime:** clean build/package/export, cold boot, target platform, logs free of relevant errors, smoke route.
5. **Playtest:** player can understand, perform, recover, and enjoy the intended loop; record task, cohort or agent, build, observations, and decision.
6. **Visual/audio:** fixed-camera/state captures, reference comparison, contrast/readability, temporal behavior, mix/spatial checks, variant rejection evidence.
7. **Performance:** representative content and target hardware; frame-time, memory, loading, package size, network, and platform budgets.

Every work unit ends with its smallest relevant automated test. A failed test returns or rolls back that unit, not unrelated history. Never report success from an unobserved test, screenshot, build, engine state, or playtest.

## Autonomous authority

The executor may autonomously inspect, plan, implement, create or enable plugins, add tests, run tools, generate variants, start isolated workers, commit, integrate into the designated testing branch, correct project knowledge, and choose reversible implementation details within the Goal and existing policy.

## Human gates

Stop and ask before:

1. migrating or upgrading the project's engine version;
2. creating new costs, subscriptions, paid API usage, or material cloud spend not already authorized;
3. accepting assets, datasets, code, models, voices, likenesses, or media with unclear rights, provenance, or commercial-use permission;
4. performing irreversible or materially destructive external actions, releases, purchases, account changes, or deletion beyond clearly authorized recoverable cleanup.

Do not turn ordinary implementation preferences into approval gates. When a gate is reached, present evidence, options, impact, rollback/migration plan, and a recommendation.

## Version policy

- Existing project: detect and pin the exact engine/editor version. Recommend a migration separately when agentic tooling, support, platform, or security materially benefits; never perform it without approval.
- New project: verify current official production-ready releases at execution time, then pin an exact version in repository configuration. Prefer stability appropriate to project stage, not a floating "latest".
- Migration Goal: inventory plugins/packages/assets/platforms, establish backups and rollback, clone/branch, migrate incrementally, run full regression and target builds, then request the required approval for adoption.

## Definition of Done minimum

- requested player/product outcome works in the target engine and platform;
- all selected evidence lanes pass and artifacts are stored or linked;
- no relevant warnings, broken imports, missing references, temporary placeholders, or unreviewed generated assets remain;
- performance and accessibility budgets are met or explicitly blocked with evidence;
- Decision Ledger, project plan, production board views, and project brain agree;
- curator has processed knowledge packets and corrected contradictions;
- one verified integration state exists, with clean worktrees/branches according to policy and no scratch/tooling pollution in production branches.
