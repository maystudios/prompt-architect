# DOMAIN — Backend / API

**Trigger:** the task designs or changes a service, an API, or the contract between services — endpoints, schemas, business logic, or data access.

## Role to assign
Senior backend engineer who owns the pager for what they ship — every contract change is a promise to every caller, not an isolated diff.
Treats the database and the network as adversarial: both will be slow, inconsistent, and hit concurrently, not just once in sequence.
Designs the failure and error case first, the happy path second.

## Work sequence
Refine the universal loop (inspect -> define done -> smallest step -> verify -> integrate) into these steps:
1. **Inspect the current contract and data model before changing either.** Read the schema, the API definition (OpenAPI/proto/GraphQL schema or existing endpoint behavior), and who actually calls it — a change that looks right against stale documentation breaks real callers.
2. **Define done as an observable contract, not a passing unit test.** Name the exact request/response shape, every status code, every declared error case, and the consistency guarantee the step must satisfy.
3. **Design the schema and contract change before the handler that implements it.** A schema decision made mid-implementation forces a second migration instead of one.
4. **Cut to the smallest independently-deployable slice.** One endpoint, one migration, or one internal boundary at a time — never "the whole service" as a single step.
5. **Implement against the full contract, including every declared error case.** A handler that only implements the success path is not a smaller version of done, it is an untested one.
6. **Verify against a real running instance of the service and its real dependencies, or a faithful containerized equivalent** — not mocks alone.
7. **Check idempotency, transaction boundaries, and concurrent-access behavior explicitly.** These are exactly the properties a single successful request never tests.
8. **Integrate: confirm the migration and the code depending on it can deploy in a safe order**, then re-run the full contract test suite before starting the next slice.

## Decomposition hints
- **Contract before handler, handler before internal refactor.** Agree the request/response shape and error taxonomy first; implementation details should never leak backward into the contract.
- **Schema and migration before the code that depends on it, and backward-compatible for one full deploy cycle.** Code and schema roll out at different times in a real deploy — a migration incompatible with the previous code version breaks the deploy window, not just the new feature.
- **Read path before write path when both change.** Verifying reads against the new shape first surfaces contract mistakes before write-side side effects compound them.
- **Obvious-but-wrong: business logic before the error taxonomy.** Bolting error handling onto finished logic produces inconsistent status codes and silently swallowed failures — decide what can fail and how it is reported first.
- **Authentication before authorization, both before business logic.** A handler that checks "is this allowed" before "who is this" leaks data in the gap between the two checks.
- **Idempotency key and retry contract before the client integration that depends on it.** Retrofitting idempotency after a client already retries naively means silently deduplicating or double-processing in production until it's caught.
- **Observability is a decomposition axis, not a final pass.** A step that ships without structured logs, metrics, or trace spans is unverifiable in production even after passing every test.
- **Cross-service contracts get versioned, never mutated in place.** Changing a shared contract's shape without a version bump breaks every other consumer at once — plan the deprecation window as part of the same step, not after.

## Verification surface
- **Integration tests against a real running instance.** Real database and queue, or a faithful containerized equivalent, never a mocked data layer.
- **End-to-end tests through real middleware.** Auth, rate limiting, and serialization exercised for every declared status code, including error cases.
- **Contract tests against the schema definition.** Catch drift between documented and actual shape (OpenAPI/proto/GraphQL).
- **Idempotency replay test.** Replay the same request or idempotency key and confirm no duplicate side effect occurs.
- **Concurrency test.** Concurrent writes to the same resource produce the declared consistency behavior (last-write-wins, conflict rejection, serialized) instead of a race-dependent outcome.
- **Migration dry run.** Run the migration against a copy of production-shaped data (volume and shape), confirm completion within an acceptable window.
- **Backward-compatibility check.** Confirm the previous code version still functions correctly during the migration's compatibility window.
- **Load and latency test.** Measured p50/p99 under realistic concurrent load against the stated budget, not a single-request timing.
- **Authn/authz test suite.** Assert every endpoint rejects unauthenticated and under-authorized requests, not only that it accepts valid ones.
- **Failure-injection test.** Force a dependency timeout or error on critical paths, confirm the declared degraded behavior actually triggers.
- **Schema/contract lint.** Automated diff against the previous contract version flags a breaking change before merge, not after a consumer complains.
- **Rate-limit test.** Confirm the declared limit actually triggers the declared response (429 or equivalent) instead of silently passing every request through.
- **Data-integrity test.** Real database constraints (unique, foreign key, check) are exercised, not bypassed by an in-memory fake.
- **Rollback test.** The migration's rollback path is executed against production-shaped data, not assumed to work because the forward path did.
- **Dependency-timeout test.** A slow or unavailable downstream dependency produces the declared timeout or circuit-breaker behavior, not an indefinite hang.
- **Tenant-isolation test.** When the service is multi-tenant, confirm one tenant's request cannot read or mutate another tenant's data.
- **Input-validation test.** Malformed, oversized, or adversarial input produces a declared error response, not a stack trace or a hang.
- **Documentation-sync check.** The published API reference (OpenAPI/proto/GraphQL doc) matches deployed behavior, verified by regenerating or diffing it, not assumed current.

## Evidence artifacts
- **Request/response captures.** HTTP traces for each declared status code and error case, filed with the test run, not described as "handles errors."
- **Migration run log.** Timing and row counts against production-shaped data, filed before the migration is considered safe.
- **Load-test report.** Actual p50/p99 latency numbers against the stated budget, not a pass/fail claim alone.
- **Contract-test output.** Schema definition validated against real request/response bodies.
- **Trace/log excerpt.** One request's structured log lines and trace span end-to-end, proving observability exists rather than that logging code was added.
- **Concurrency-test output.** The actual outcome of simultaneous conflicting requests, not an assumption about lock behavior.
- **Compatibility-window result.** Previous code version tested against the new schema, filed alongside the migration log.
- **Schema-diff report.** Automated diff output showing any breaking change was caught, or confirming none exists.
- **Rate-limit test output.** Captured response showing the throttling behavior actually triggered at the declared threshold.
- **Rollback run log.** Timing and outcome of executing the migration's rollback path against production-shaped data.
- **Dependency-failure test output.** Captured response or log showing the timeout or circuit-breaker behavior under a simulated dependency failure.
- **Tenant-isolation test output.** Captured proof that a cross-tenant access attempt was rejected, for multi-tenant services.
- **Input-validation test output.** Captured responses for malformed, oversized, or adversarial inputs, showing a declared error rather than a crash.
- **Documentation-diff output.** Regenerated schema or doc diffed against the previously published version, filed to prove it matches deployed behavior.

## Common failure modes
- **Verifying against mocks only, never a real running service.** A handler passing against a mocked repository can still fail on real constraint violations, connection limits, or serialization differences.
- **Treating "the happy path returns 200" as done.** Error cases, partial failures, and edge inputs are the actual failure surface in production; skipping them is skipping verification, not deferring it.
- **Silent breaking changes to a shared contract.** Renaming a field or changing a type on an endpoint other services call, without a version bump or deprecation window, breaks every consumer at once.
- **Assuming a single request proves idempotency or concurrency safety.** Both properties are only visible under replay and concurrent access — one successful call proves neither.
- **Migrations tested only against an empty or tiny local database.** A migration that runs instantly on a seed database can lock a production-sized table for minutes.
- **Checking authorization after fetching the resource instead of before.** Fetching first and checking permission on the same code path as returning the data tends to leak existence or content in the gap.
- **No observability added until after an incident.** A change shipped without structured logs, metrics, or trace spans is unverifiable in production regardless of pre-deploy test coverage.
- **Scope creep into unrelated internal boundaries "while in there."** Touching shared modules under the guise of a small fix produces an unreviewable diff and an untested blast radius.
- **Reporting "tests pass" without naming which layer.** Unit tests passing says nothing about integration or contract correctness — name the layer that was actually exercised.

## Test-time compute verdict
**Spend variation-search budget on performance and concurrency tuning under real, measured load** — try several indexing, caching, or locking strategies, score each against the actual p50/p99 budget and correctness under concurrent access, keep the winner.
**Spend it on schema and contract design** too, when multiple shapes satisfy the same requirement but trade off differently under real access patterns — generate a few candidates, load-test or query-plan each, decide by evidence, not preference.
**Spend it on error-taxonomy and status-code design** too, when a genuinely ambiguous case has multiple defensible mappings — pick by testing real client handling, not by preference.
**Do not spend it on a documented CRUD endpoint, a migration matching an existing pattern already in the codebase, DTO/mapping boilerplate, or wiring an already-decided auth middleware.** One correct shape exists for each of those, fixed by existing convention — repeated attempts return the same answer at extra cost.
**Do not spend it on a standard health-check or readiness endpoint** either — the shape is fixed by platform convention, not a design decision.
Default to a single careful attempt for anything a sibling endpoint in the same service already answers.

## Definition-of-Done clauses
- **Every declared endpoint and status code covered** — success and error, by an integration or contract test running against a real service instance, output attached.
- **Idempotency and concurrency proven, not asserted** — verified by replay and concurrent-request tests, not claimed from code review.
- **Migration verified safe** — run successfully against production-shaped data with timing recorded, and the previous code version still functions during the compatibility window.
- **Latency budget met** — measured p50/p99 under realistic load meets the stated budget, evidenced by a load-test report.
- **Authn/authz enforced both ways** — tests confirm every endpoint rejects invalid access as well as accepting valid access.
- **Observability demonstrated, not just present** — structured logs, metrics, or trace spans shown by a captured log or trace excerpt, not by the presence of logging code alone.
