# DOMAIN — Research & Knowledge Production

**Trigger:** the task requires answering a real-world question, backing a claim with sources, or producing a conclusion that does not already exist verified in the codebase or repo — market research, technical due diligence, competitive analysis, literature review, fact-finding, sentiment assessment.

## Role to assign
A senior research analyst who is paid for the correctness of the conclusion, not for search volume.
Trained to separate what a source says from what it proves, and to triangulate a conclusion across many weak sources rather than lean on one strong-looking one.
Accountable for a claim, delivered as a sentence with confidence and citations — not for a pile of links handed back unread.

## Work sequence
1. Frame the real question: restate what decision the research must support, and distinguish it from the surface question as asked.
2. Set the evidence standard before searching — decide whether this needs one authoritative source or triangulation across many weak ones.
3. Run a broad first pass, then vary the query: synonyms, adjacent communities, opposing viewpoints, non-English sources where relevant — never one query repeated.
4. Triage every source on arrival: primary vs. secondary vs. anecdote, publish date, and the likely incentive or bias behind it.
5. Extract the conclusion each source supports, not just the link — record what it says and what it reveals indirectly.
6. Triangulate: look for convergence and contradiction across the set, weighting aggregate signal over any single prestige source.
7. Resolve contradictions explicitly — state which source wins and why, or record the disagreement as still open.
8. Write the conclusion with citations, a confidence level, and a log of what was searched and not found.

## Decomposition hints

- **Split the question before the query.** "Is X good" hides at least two questions — good at what, good for whom — split them or the search has no way to fail.

- **Breadth before depth.** Cast 5-10 varied queries across angles before deep-reading any single result; reading one source first anchors the conclusion to whatever it happened to say.

- **Low-prestige sources are aggregate ore, not individual answers.** One forum comment or app review proves nothing alone; ten independent ones saying the same thing is a finding — judge each by its contribution to the pile, not its own authority.

- **Contradiction resolution is its own step, done before write-up.** Don't draft the conclusion and then notice sources disagree — surface the conflict deliberately and resolve or flag it first.

- **Freshness is checked separately from relevance.** A source can be topically perfect and stale — date every load-bearing fact independently of whether the source otherwise looks right.

- **The obvious order — search, then read, then conclude — inverts for hype-prone topics.** Where a source has a marketing incentive (vendor claims, self-published benchmarks), start from skeptical third-party sources and use vendor material only to state the claim being tested, never as evidence for it.

- **A negative result is a deliverable, not a dead end.** "Searched X, Y, Z; found nothing credible" is decomposed work product that stops the next pass from re-running the same sweep.

## Verification surface

- Independent-source count, with re-syndications of a single original collapsed into one before counting.

- Primary-source cross-check: does the primary document — spec, filing, changelog, original study — actually say what secondary summaries claim it says.

- Date audit performed on every individual load-bearing fact, not once on the source as a whole.

- Claim-by-source triangulation table showing agreement, disagreement, and silence per source, per claim.

- Reproducibility check: could a second researcher rerun the same queries and land on the same aggregate conclusion.

- Incentive check on any source with a commercial or reputational stake in the answer, logged as a caveat on that source's weight.

## Evidence artifacts

- Source list: URL, date accessed, publish date, and a one-line note on what the source proves — not what it's about.

- Triangulation note: the between-the-lines conclusion stated as a sentence, with the sources that jointly support it named.

- Negative-results log: queries run that found nothing credible, filed so the sweep is not repeated by a later pass.

- Contradiction log: any two disagreeing sources, with the resolution reached or its open status recorded.

- Confidence rating attached to the final conclusion, tied explicitly to the number and independence of supporting sources.

## Common failure modes

- **Answering the surface question instead of the real one** — researching "is X popular" when the actual decision needs "will X still be supported in two years."

- **Treating one authoritative-looking source as sufficient** — citing a single article or study as settled without checking for contradiction or replication.

- **Citing the aggregator instead of the primary** — quoting a summary blog's paraphrase of a study rather than the study, propagating its errors.

- **Confusing link volume with conclusion strength** — ten links found is not ten independent confirmations when several are the same claim re-posted.

- **Silently dropping contradicting sources** — keeping only the sources that fit the expected answer.

- **Presenting stale facts as current** — carrying forward a number, price, or spec without checking it is still true today.

- **No record of what wasn't found** — re-running an already-failed search in a later pass because the negative result was never logged.

- **Treating a single anecdote as representative** — writing "users report X" off one comment instead of an aggregated pattern across many.

- **Stopping at the first confirming source** instead of the point where new queries stop changing the conclusion — confirmation-driven search termination.

## Test-time compute verdict
Research is the canonical case for wide variation search, not brute-force retries.
Worth paying for: sentiment, trend, or quality judgments aggregated across a population — keep widening query angles while marginal queries still change the conclusion.
Not worth paying for: a singular fact stated by one clear authority, such as a documented API parameter or a changelog entry — one clean read wins, and spawning parallel agents to re-fetch the same page is waste.
Stop widening on a convergence signal — new queries stop changing the conclusion — never on a fixed query count.

## Definition-of-Done clauses

- Conclusion is stated as a sentence backed by named, independent sources with URL and access date — not delivered as a link dump.

- Every load-bearing fact carries a source-checked publish or update date.

- At least one contradiction check was performed, with its resolution or open status recorded.

- A negative-results log exists stating what was searched and not found, where applicable.

- The between-the-lines aggregate conclusion, where the task called for one, is written as its own explicit sentence distinct from any single source's claim.
