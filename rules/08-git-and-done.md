# RULE 08 — GIT DISCIPLINE AND DEFINITION OF DONE

## 1. Git during the work — permissive on purpose

Agents should use version control hard. Branching to try something, cutting a worktree to run an experiment in parallel, and **rolling back when a direction turns out wrong** are all correct behaviour. They are cheaper and safer than patching a bad direction in place.

Put this in the prompt explicitly, because agents under-use it:

- **Branch freely during the work.** Scratch branches and worktrees for experiments are encouraged, not tolerated.
- **Roll back rather than repair a wrong direction.** If the last three commits went the wrong way, `git reset`/`git revert` to the last good state and re-approach. Do not try to steer a wrong implementation back on course edit by edit.
- **Commit small and often, per verified step.** Parallel agents synchronise through commits, not through assumptions.
- **The branch stays green.** A commit that breaks the gates gets fixed or reverted before the next step.
- **Never commit directly to the protected base branch.**

## 2. Git at the end — strict on purpose

The permissiveness above has a price, and this is it. **The final state must be one clean, comprehensible integration point.** Twenty half-finished branches and three stale worktrees is a worse outcome than the work not being done, because now someone has to reconstruct which one is real.

Every prompt's DoD carries this, verbatim in substance:

- **The finished work is on the branch agreed in the Frame round**, named literally. That branch and no other.
- **Every branch created during the work is merged into it or deleted.** No scratch branches survive.
- **Every worktree created during the work is removed.**
- **The working tree is clean.** No uncommitted changes, no leftover stashes, no detached HEAD.
- **The target branch is green** — the named gates pass on it, not on some earlier branch.
- If the agreement was "merge back to the base branch when green", that merge is done and the feature branch is deleted. If the agreement was "leave it on the feature branch", it is on that branch and nowhere else.

The rule in one sentence for the prompt: **branch as much as the work needs, but land on exactly one branch and clean up everything else.**

## 2a. No repository — the exemption covers §1 too

When the project has no version control, **both §1 and §2 are replaced**, not just the end-state clause. Dropping only §2 leaves SETUP's mandatory commit cadence and §1's "branch freely, commit small and often" instructing an agent to use git that is not there.

Replace them with the discipline a no-VCS run actually needs, and put it in SETUP:

- **Edits are additive.** Never overwrite a file whose previous content is not recoverable.
- **Date what you supersede.** A revised document keeps the prior version beside it with a date, rather than replacing it in place.
- **Name the checkpoint.** Before a change large enough to want undoing, copy the working set to a dated folder — that is the rollback this project gets.
- SETUP carries one line stating no version control is present; DEFINITION OF DONE carries no git clause.

Do not invent a repository. Do not suggest running `git init` unless the user asked.

## 3. Building the Definition of Done

The DoD is the mission and scope translated into a finite, checkable contract. It is not a summary and not an aspiration.

**Construction:**

1. **One clause per MISSION requirement.** Walk MISSION line by line. Every requirement gets a clause, and every clause names the evidence that settles it.
2. **Add the domain clauses** from the loaded profile in `rules/domains/`.
3. **Add the git end-state clause** — in every prompt that has a repository. The only exception is a project with no version control, per §2.
4. **Add documentation state:** which files must be current — `GOAL.md`, the living spec, the second brain corrections.
5. **Add accepted residuals:** the known-and-accepted leftovers, named, with where they are recorded. An accepted warning with a reason is fine; an unexplained one is not.

**Every clause must be checkable.** Read each one and ask what you would look at to decide. If the answer is "judgement", either name whose judgement and on what artifact, or rewrite the clause.

| Instead of | Write |
|---|---|
| Code is clean | No cross-layer imports; the boundary test passes |
| UI is polished | Every action gives visible feedback; destructive actions are confirmed or undoable; verified on the captured state set |
| It is fast | Median response under the stated budget, measured at final data volume |
| Well tested | The named end-to-end and integration suites are green, and each new test was shown to fail once on purpose |
| Documentation updated | `GOAL.md` reflects the final scope, decisions and backlog; the living spec matches the shipped behaviour |

**Subjective clauses are allowed, and must still name their evidence.** "The interface reads as intended" is not a clause. "Blind expert review and neutral perception probe both identify the primary action unaided, on the captured state set" is.

## 4. Evidence taxonomy by task type

Pick from these; do not use all of them everywhere.

- **Backend, services, data:** end-to-end and integration suites green against a real running service; contract tests; migration rehearsed forward and backward; measured latency or throughput against the stated budget; error taxonomy exercised; documentation state.
- **Interface and interaction:** captured state set on a fixed surface; the applicable blind lanes from `rules/06-verification.md` reaching the stated conclusion; layout verified at the smallest and largest supported size and at increased text scale; every action gives feedback.
- **Engine, level and asset work:** the artifact walked or run end to end; the camera set captured and reviewed; zero validation errors; zero unexplained warnings; performance within budget at final density; automation lanes green from CLI.
- **Research and knowledge:** the question answered with the conclusion stated and its basis named; contradictions resolved or explicitly recorded as unresolved; currency of each load-bearing fact stated with its verification date. **Where a second brain exists**, add: updated with the conclusion and the corrections. Where none exists, the conclusion and its basis are recorded in the project's own documents — never emit a second-brain clause for a project without one.
- **Creative and media:** the artifact produced at the required specification for its target slot; selection recorded against the stated intent; files named and filed to convention.

## 5. Compiled section shape

```
# DEFINITION OF DONE
- {{mission requirement 1}} — proven by {{evidence}}.
- {{mission requirement 2}} — proven by {{evidence}}.
- {{domain clause}}.
- {{documentation state clause}}.
- Finished work is on `{{branch}}`; every branch and worktree created during the work is merged or removed; working tree clean, no stashes, no detached HEAD; the named gates are green on that branch.
- Accepted leftovers recorded as GOAL.md backlog with severity — nothing silently dropped.
```

Compact form: one line per mission requirement, the git clause, the documentation clause. **The git clause is never cut, at any length.**
