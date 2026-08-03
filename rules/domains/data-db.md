# DOMAIN — Data & Databases

**Trigger:** the task touches schema design, migrations, data pipelines, backfills, or the correctness of data at rest or in transit — including reconciliation across systems that disagree.

## Role to assign
A senior data engineer + DBA who owns schema evolution, pipeline correctness, and data integrity end to end. Treats production data as a liability to protect, not a fixture to assume. Ships every migration so the on-call DBA could roll it back at 3am without reading the ticket.

## Work sequence
1. Inspect the current schema, migration history, and the live data's actual shape — row counts, null rates, cardinality, the types actually stored versus the types declared. Never assume the schema doc matches the table.
2. Identify the source of truth for every field touched: which system originates it, which systems merely cache or derive it, and what reconciles them when they disagree.
3. Define the target state and the invariant it must hold — uniqueness, referential integrity, non-null, range, idempotency key — together with the tolerance for cross-source disagreement, before writing a migration.
4. Sequence the rollout: additive schema change, then dual-write or backfill, then validation, then cutover of reads, then removal of the old path. Never collapse these into one step against a live table.
5. Write the smallest reversible migration for the current step. Every migration ships with a tested down-migration or an explicit, logged reason one is impossible.
6. Run it against a representative copy — production-shaped volume and production-dirty data, never a clean fixture — verify with row-level checks, then apply.
7. Reconcile: compare source and destination by count, checksum, and sampled row-level diff. Silence is not proof; a matching total is not proof either.
8. Record the invariant, the rollout order, and any accepted data inconsistency in the living spec before starting the next change.

## Decomposition hints
- **Schema before pipeline.** A pipeline written against a schema that will still change is rework waiting to happen; freeze the shape first.
- **Backfill after dual-write starts, never before.** New rows already land in the new shape, so the backfill only has to fix history, not chase a moving target.
- **Additive and destructive migrations never ship together.** Add a column in one deploy, drop the old one in a later deploy after a soak period — collapsing them removes the rollback window.
- **The "obvious" order — pipeline, then backfill, then add the constraint — is backwards.** Add the constraint last, once the backfill has proven the data already satisfies it; adding it first turns every in-flight write from an unmigrated caller into an outage.
- **Decide the tolerance before running the diff.** What counts as close enough (rounding, re-keying, timing skew across sources) and the tie-break rule when sources disagree (latest-wins, source-priority, manual queue) get decided before reconciliation runs, not after it produces an unreviewable wall of mismatches.
- **Idempotency key before retry logic.** Design the dedupe key first; retry and replay logic built on an unstable key just launders duplicates faster.
- **Cut the read-path migration from the write-path migration.** Moving readers and writers in the same step hides which one caused a regression.
- **Reconciliation runs at every stage, not once at the end** — after the backfill, after dual-write starts, and after cutover, each a separate checkpoint.

## Verification surface
- **Row-level constraint checks** — NOT NULL, unique, foreign key, check constraints — run against the actual post-migration table, not the migration file.
- **Reconciliation pass** — source-vs-destination row counts, an aggregate checksum over sorted column concatenation, and a random sample diffed field by field.
- **Idempotency test** — replay the identical batch or event twice; assert no duplicate rows and no double-counted aggregate.
- **Reversibility test** — apply, verify, roll back, verify original state restored, all against a non-empty representative dataset, not an empty table.
- **Backward-compatibility test** — old application code reading the new schema during the dual-write window, and new code reading data still in the old shape.
- **Production-shaped test data** — real volume, real dirtiness (nulls, encoding variants, out-of-range values) — never a hand-built ten-row fixture that can't fail the way the real table can.
- **Zero-downtime rehearsal** — the full rollout sequence run and timed against a staging copy sized like production before it touches the real table.
- **Consumer/contract check** — downstream readers (services, BI dashboards, reports) run against the new shape in staging before cutover; a change no one verified against its actual consumers is not verified.
- **Concurrency and lock-contention test** — the migration run under simulated production write load to catch lock waits, deadlocks, and long-running transaction blocking before they happen live.

## Evidence artifacts
- Migration files with explicit up and down steps, committed with the schema diff they produce (before/after `\d table_name` or the equivalent).
- A reconciliation report — counts, checksum, and sample-diff results — saved with a timestamp and the exact query used to produce it.
- A backfill run log: rows processed, rows skipped with reason, rows failed with reason, and the checkpoint it can resume from if interrupted.
- Rollback rehearsal output proving the down-migration actually ran once, not merely that it was written.
- An updated invariant list or data dictionary: what each constraint guarantees, and what it deliberately does not.
- A pre-migration backup or snapshot reference with a confirmed restore test, for anything irreversible or high-risk.
- A short changelog entry visible to downstream consumer teams: what changed, and by when the old path disappears.

## Common failure modes
- **Migration and backfill collapsed into one deploy** against a live table with no read-path fallback, so any mid-backfill failure takes the table down.
- **Constraint added before the backfill finishes**, so in-flight writes from unmigrated callers start failing in production.
- **Reconciliation checks totals only** and misses that duplicate rows and missing rows canceled each other out.
- **No idempotency key**, so a retried job or replayed event silently double-inserts or double-sums.
- **Perfect agreement demanded instead of the best supportable match.** Government and finance feeds round, truncate, and re-key differently per source; a solver that requires them to agree exactly stalls forever instead of reconciling to a logged, tolerated residual.
- **Down-migration untested or absent**, discovered for the first time during an actual incident.
- **Type or precision silently narrowed** — timestamp truncation, float rounding, string truncation — with no validation catching the diff before cutover.
- **Dry run against a clean fixture** with none of the real table's nulls, duplicates, or encoding issues, so the migration passes staging and fails on row one in production.
- **Schema change and application deploy coupled**, so rolling back one without the other breaks compatibility in both directions.

## Test-time compute verdict
Low value by default: schema migrations and backfills are mechanical and repetitive — one correct rollout order exists, and searching over script variants wastes budget better spent on reconciliation coverage. Pure waste on scaffolding a standard migration file, a documented backfill loop, or a mechanical column rename. Worth paying for on genuinely ambiguous reconciliation logic against inconsistent multi-source data, where matching several fuzzy-join or precedence heuristics against known-good samples and keeping the best-scoring one is the actual method — and on backfill performance tuning, where batch size, index use, and lock contention trade off empirically. Default to one well-reasoned attempt with strong verification; escalate to multi-attempt search only where a reconciliation heuristic's quality is genuinely unresolved by reasoning alone.

## Definition-of-Done clauses
- Every migration has a tested down-migration, verified by an actual rollback-and-restore run against representative data, or a documented and approved reason none exists.
- The reconciliation report shows source and destination agreeing within a stated, pre-declared tolerance, backed by a manually inspected row-level sample — not counts alone.
- The backfill is proven idempotent by a replay-the-same-batch test showing no duplication, and resumable from a checkpoint after interruption.
- Constraints went live only after the backfill was confirmed complete and reconciled; no window existed where partially migrated data could have violated them.
- The full rollout sequence — additive change, dual-write, backfill, validation, cutover, cleanup — is executed and logged in order, not partially applied and assumed safe.
- Known cross-source inconsistencies are documented with the resolution rule actually applied, rather than silently dropped or left blocking.
