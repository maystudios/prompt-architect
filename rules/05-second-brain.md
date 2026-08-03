# RULE 05 — SECOND BRAIN & RESEARCH

Activate `# SECOND BRAIN / RESEARCH` when a knowledge base exists, or the task is knowledge-heavy, or current facts matter. Omit the section entirely when there is no knowledge base *and* no research need — a hollow research section is worse than none.

The second brain question is a Frame-round slot. Never assume one exists, and never assume one does not.

## 1. What a second brain is, and why it outranks a search

Two sources, two different natures:

- **The web** is broad knowledge, current, and largely unverified. Anyone can publish. It moves.
- **The second brain** is accumulated own knowledge: conclusions drawn, failures survived, patterns confirmed or refuted in this project's actual conditions. It is frozen at the moment it was last written, and its quality is far above the average of the web — because it was earned, not found.

**There is no fixed search order.** Consult both, and form your own view from the pair. The vault knows what worked here; the web knows what changed since. Neither alone is the answer, and treating one as authoritative is how both get misused.

The exception that is not an exception: for the current API surface of a library or engine, official documentation is a first-rate source even when the vault is silent. Judge the source by what it is, not by which pile it came from.

## 2. Adopt the vault's own conventions first

Before writing a single note: read how the vault is organised and how it says it wants to be used. Most maintained knowledge bases document their own structure — naming, folder meaning, note templates, tagging, linking, status markers.

**If it documents its conventions, follow them.** A correct fact filed in the wrong shape degrades the vault. Match the existing form before adding to it.

## 3. Correction mandate

**The vault is not infallible.** It is a snapshot of what was believed at the time, and some of it is wrong, outdated, version-mismatched or simply nonsense that survived because nobody checked.

When the work contradicts a note — a documented approach that reliably produces an error, a pattern that no longer holds, a claim the evidence refutes:

- **Fix the note in place.** Corrected, sourced, concise. Do not add a second note beside the wrong one; that leaves a landmine.
- **Mark the correction** on one line, in this order: the word `Corrected`, the date, the claim it replaced, the source, and the version or condition it was verified against. Describe those fields in prose rather than shipping a bracketed template — the placeholder ban has no exemptions, and that is what keeps it enforceable.
- **Record how the error arose, not only the fix.** This is the part that usually gets skipped and it is the more valuable half. "Do it this way" prevents one repetition. "This looks correct and fails because the lifecycle runs before the binding exists" prevents the whole class. Write the failure mode down.

A wrong note that keeps sending agents into the same wall is the single most expensive thing a second brain can contain.

## 4. Expansion mandate

The vault grows as a side effect of the work. A topic being absent is not a reason to leave it absent.

Write back when:

- **A search produced a conclusion.** Not the links — the conclusion. What you now believe, why, and what it rests on.
- **A topic is thin and the work needed it.** Research it, then file it.
- **An experiment produced a fact the web does not have.** Your own code failing in a specific way on a specific version is primary evidence that exists nowhere else.
- **A neighbouring topic is missing.** Where the vault documents only the negative case, the positive counterpart belongs beside it — the anti-patterns of a documented pattern are part of the same subject, and their absence makes the existing note read as more absolute than it is.

**Relevance test, not topic-match test.** Ask whether it strengthens, refutes, extends or contextualises something the vault is *for* — not whether a section for it already exists. A conclusion drawn from a product launch outside the project's domain can be exactly the right entry in a design vault, if what it explains is why an audience accepted something. Judge by what it teaches, not by where it came from.

Do not file everything. A source that contributed nothing beyond an already-recorded fact does not need an entry. The bar is: does the vault get better at answering a future question.

## 5. Sources — wide, and judged individually

All of these are legitimate:

- official documentation and specifications
- the web at large — articles, blogs, release notes
- forums and community threads, including consumer-facing ones
- video, analysed through a video-capable model rather than watched by proxy
- **your own experiments** — code you wrote, ran, and observed failing
- the existing codebase and its history

**Judge each source on what it contributes, not on its prestige.** A source that is worthless in isolation can be load-bearing inside an aggregate.

**The aggregate conclusion is the prize.** Sweeping many weak sources — forum threads, comment sections, consumer coverage — to establish what an audience on average actually responded well to produces a finding that exists in no single one of them. That finding is exactly what belongs in the vault and exactly what a future search will not re-derive cheaply. Record the conclusion and what it rests on; do not just file the links.

**Confirmation and refutation are equally valuable.** Sweeping opinion on an interaction pattern the vault documents, and finding it broadly accepted, strengthens the note — say so, with the evidence. Finding it broadly rejected means the vault is carrying a wrong belief — correct it, with the evidence. Both outcomes are a successful pass; only "I found sources" is a failed one.

## 6. Interconnection

The value compounds when notes are linked, not merely accumulated. When new evidence bears on an existing note, connect them explicitly — the confirming or refuting relationship is itself the information, and it is exactly the kind of thing that cannot be reconstructed from a search later.

## 7. Feed the improvement loop back in

`rules/07-self-improvement.md` produces findings. Those findings are second-brain input, not just bug fixes.

At the end of every improvement pass, ask what was learned that would have prevented the finding, and write that in. The point is not bookkeeping — it is that the vault is the agent's memory across sessions. A person who spends three hours on a problem remembers the shape of the trap. An agent only does if it wrote it down.

## 8. Compiled section

```
# SECOND BRAIN / RESEARCH
Search {{vault path}} before web search and before implementing — try 2-3 phrasings. Read how the vault documents its own conventions and follow them.
The vault is accumulated own knowledge, high quality but frozen; the web is broad, current and unverified. Consult both and form your own view — there is no fixed order.
Correction mandate: it is NOT infallible. Wrong, outdated or version-mismatched -> fix the note in place, corrected, sourced and concise, marked with the word `Corrected`, the date, the claim it replaced, the source, and the version verified against. Record how the failure arose, not only the fix — the failure mode prevents the whole class, the fix prevents one repetition.
Expansion mandate: a conclusion drawn is a note written. Thin topic -> research it now, that is part of the job. Missing counterpart of a documented pattern -> add it. File the conclusion, not the link list.
Sources: docs, web, forums, video via a video-capable model, and your own failing experiments. Judge each on what it contributes to the conclusion, not on prestige — a weak source can be load-bearing in the aggregate.
Guarantee coverage for: {{the topics THIS task actually depends on}}. Empty topic = research it now.
```

Compact form: the search instruction, the correction mandate with the failure-mode clause, the expansion mandate. Three lines.

## 9. Research with no second brain

The activation test is an OR — a knowledge-heavy task activates the section even when the user answered "no vault". Every line of §8 above is vault-conditional and yields nothing here, so compile this instead:

```
# RESEARCH
Frame the real question before searching: name what a correct answer would look like and what would falsify it.
Run 2-3 phrasings per question, not one. Weigh each source on what it contributes to the conclusion, not on prestige — a weak source can be load-bearing inside an aggregate, and the finding that matters usually exists in no single source.
Separate what a source says from what it proves. Where sources conflict, say which you followed and why; where they cannot be reconciled, record the disagreement rather than picking silently.
Check currency explicitly: state the date each load-bearing fact was verified, and name what would make it stale.
File the conclusion, not the link list — what you now believe, why, and what it rests on. Record negative results too: what was searched and not found, so the same sweep is not repeated.
Stop when a further sweep changes no conclusion. Say so.
```

Name the section `# RESEARCH`, not `# SECOND BRAIN / RESEARCH`, when there is no vault — the heading should not promise a knowledge base that does not exist.

**And drop the second-brain clause from DEFINITION OF DONE.** `rules/08-git-and-done.md` §4 lists "the second brain updated with the conclusion and the corrections" under research work; that clause is conditional on a vault existing. Without one, the DoD clause is that the conclusion and its basis are recorded in the project's own documents.
