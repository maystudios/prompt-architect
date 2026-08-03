# DOMAIN — Creative Media Production

**Trigger:** the task produces an image, video, audio clip, or other visual/creative artifact meant for an audience or a specific placement — thumbnail, hero image, trailer, voiceover, loop — rather than for internal debugging.

## Role to assign
A senior creative director who ships to a brief and a slot, not to personal taste.
Accountable for whether the artifact fits its intended placement and reads correctly to a cold viewer in the first second.
Trained to judge a batch against stated criteria before anyone's preference enters the decision.

## Work sequence
1. Extract the brief: subject, mood, audience, and the one sentence of intent the artifact must satisfy.
2. Define the target slot before generating anything — aspect ratio, resolution, duration, file format, and where it will sit.
3. Fix the comparison surface: hold prompt scaffold and settings constant except the one axis under test, so results are comparable.
4. Generate in batches, not one-at-a-time re-prompts — produce a real spread (four to eight or more) per iteration.
5. Score the batch against the stated intent, not personal preference, and eliminate on named criteria.
6. Iterate only the losing axis — change one dimension (composition, lighting, voice tone) per pass so the cause of improvement stays traceable.
7. Verify the selected candidate in situ at the target slot — actual crop, compression, loop point, audio level — before calling it done.
8. File and name the asset per project convention, keeping or discarding the rejected variants per that same convention.

## Decomposition hints

- **Slot before style.** Fix aspect ratio, duration, and resolution before writing the creative prompt — a striking 16:9 image is a defect if the slot is a 9:16 thumbnail.

- **Brief before batch.** Do not generate until subject, mood, audience, and the one-sentence goal are written down — otherwise selection has no criteria to select against.

- **Variation before refinement.** Generate a spread first; refining one candidate through many small re-prompts before seeing the spread anchors on a possibly-weak seed.

- **Fix the comparison axis.** Changing prompt and seed and model settings between attempts destroys the ability to know what caused an improvement — vary exactly one axis per pass.

- **The obvious order — generate, then judge, then place — is backwards for tight slots.** For placements with hard technical constraints (loop points, safe-zone text, broadcast loudness), check the technical fit first; a beautiful asset that fails the technical gate is a redo, not a finalist.

- **Selection is a gate, not a preference vote.** Score against the brief's stated criteria before taste enters; taste breaks ties among assets that already passed the gate, it does not replace the gate.

- **Audio and video sync is its own decomposed step.** Do not treat "generate video" and "generate matching audio" as one atomic step when timing alignment between the two is required.

## Verification surface

- Side-by-side grid of the full batch at actual target size and aspect ratio, never a single zoomed preview.

- In-situ placement check: the asset dropped into the real layout, timeline, or page to see it at intended scale and surrounding context.

- Technical spec check, measured rather than eyeballed: resolution, aspect ratio, file size and format, duration, loop-point continuity, audio loudness.

- Fresh-eyes read: a viewer who has not seen the brief judges whether the intent reads without explanation.

- Cross-device or cross-context check where the slot spans contexts (light and dark background, mobile and desktop crop).

## Evidence artifacts

- The brief itself — subject, mood, audience, one-sentence intent, target slot spec — saved alongside the output.

- The full batch of variations, not just the winner, named with a shared prefix and an index, filed in the project asset folder.

- A one-line selection rationale per winner: which named criteria it won on, which finalists it beat.

- An in-situ screenshot or clip showing the asset placed in its real context, not an isolated render.

## Common failure modes

- **Generating before defining the slot** — producing a striking image at the wrong aspect ratio, forcing a crop that ruins the composition.

- **Single re-prompt loop instead of batch variation** — iterating serially on one candidate, mistaking small local edits for exploring the space.

- **Judging on a zoomed single preview** — approving an asset that breaks down at actual thumbnail size or inside a crowded layout.

- **Changing multiple axes between attempts** — new prompt, new seed, and new model all at once, so no one can tell which change produced the improvement.

- **No named criteria, taste-only selection** — picking a "favorite" with no traceable link back to the brief, satisfying the creator instead of the audience.

- **Treating technical spec as an afterthought** — a gorgeous loop with a visible seam, or a voiceover that clips at broadcast loudness, discovered only after calling it done.

- **Losing the batch** — deleting or failing to file the rejected variations, forcing a later revision to regenerate from zero instead of promoting a runner-up.

- **Skipping the fresh-eyes read** — the only judge is the person who wrote the brief and already knows what it's supposed to look like, so a confusing result passes unnoticed.

## Test-time compute verdict
Creative generation is the canonical case for wide variation search: composition, mood, and voice are subjective and cheap to sample, so generate batches and gate on the brief instead of accepting the first output.
Worth paying for: hero images, thumbnails, key art, voice takes — anything a cold audience judges in under a second, where the space is wide and the bar is empirical.
Not worth paying for: mechanical format conversion (resize, re-encode, silence-trim), a placeholder never shown to users, or a brief that already fully specifies the exact output.
Where the brief is exact, generate once and verify against spec — don't multiply attempts at a fixed target.

## Definition-of-Done clauses

- Asset matches the target slot spec exactly — aspect ratio, resolution, duration, format — measured, not estimated.

- The winner was selected from a generated batch against named criteria tied to the brief, with the rationale recorded.

- Asset was verified in situ at real placement and scale, not only as an isolated preview.

- File is named and filed per project convention, with rejected variants retained or intentionally discarded per that convention.
