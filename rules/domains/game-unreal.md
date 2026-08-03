# DOMAIN — Unreal Engine & Game Development

**Trigger:** the task involves Unreal Engine level, asset, or content work driven through the editor — blockouts, detail passes, lighting and atmosphere, asset creation, or level-scoped content dressing.

## Role to assign
A senior level designer + engine architect: spec-driven, iterative, never ad hoc. Owns composition and silhouette as much as the geometry that produces them — whether a shot reads as deliberately art-directed or as machine-placed is the actual work; the geometry is only the consequence.

## Work sequence
1. Read the living spec, any reference images, the existing level, and the studio's knowledge base first — never build on assumption.
2. Inventory the current state: open the map, screenshot every existing area from every existing camera, and set those side by side with the references. Write the gap analysis before touching geometry.
3. Define what "done" looks like for the current step and how it will be checked — which camera, which test, which threshold.
4. Split into the smallest verifiable step — one area, one asset, one pass — never the whole level at once.
5. Build the step through the engine MCP, save, screenshot the affected cameras, look at the result, judge it, fix it before moving to the next step.
6. Refactor continuously: honest naming (`SM_`, `M_`, `BP_`, `SS_`), folders and data layers per area, instanced meshes where things repeat, no orphan actors.
7. Run Map Check and asset validation after every content change; scrape the session log for errors and warnings before moving on.
8. Record decisions, accepted deviations, and open risks in the living spec before starting the next step.

## Decomposition hints
- **Camera rig before geometry.** Cameras are instruments, not decoration; build the rig first so every later change has something to be judged against.
- **Vertical slice first, not horizontal coverage.** Take one area to final quality — geometry, assets, lighting, atmosphere, gap-free — before starting the next. A level 40% finished everywhere proves nothing about whether the target is reachable.
- **Assets are built outside the main map.** Model in a dedicated lab map, verify in isolation from every angle, promote only when proven — never model directly inside the level being assembled.
- **Massing, then detail, then lighting, then atmosphere, then post-process — in that order.** Each pass needs the previous one settled, or it polishes something about to change.
- **The "obvious" order — texture and light as you go — is wrong for a blockout.** Grid material stays uniform across the whole build; the read has to come from silhouette, composition, and light alone, proven on locked-camera screenshots before any higher-fidelity pass is justified.
- **Grid-snap what gameplay depends on; break everything else off-grid deliberately.** Floors, doorways, and platform heights stay locked; natural forms that stay axis-aligned read as machine-placed.
- **Gap hunting is its own scheduled pass, after geometry and lighting settle** — not something noticed incidentally while doing other work.
- **One editor instance per parallel agent, one map or lab per agent.** Two agents in the same map or the same running editor corrupt each other's state; integrate through committed assets, not shared live sessions.

## Verification surface
- **Locked screenshot comparison** across the full camera rig (overview, path, reverse, detail, hero) — fixed transform, fixed FOV, fixed manual exposure — diffed against a baseline with deliberate tolerance.
- **Reverse cameras** at every path position: open backfaces, unmet geometry, and light leaks show up here, not from the forward view.
- **Detail cameras** at every seam: wall-to-floor junctions, asset-to-terrain contact, doorframes, corners — small mistakes only exist at this distance.
- **Functional Tests** for traversal: spawn a pawn, walk the full route, assert it arrives, never falls through, never gets stuck; include a wall-hugging variant.
- **Automation Spec tests** for asset validation: pivot at base, collision present and sane, LODs generated, lightmap UVs valid, naming convention, material slots, scale checked against the reference mannequin.
- **Two CLI automation lanes, both gating:** headless logic (`-unattended -nullrhi -ExecCmds="Automation RunTests ...;Quit"`) and a rendering lane (`-renderoffscreen`, since `-nullrhi` cannot produce screenshots).
- **Performance measurement** — `stat unit`, `stat gpu`, draw calls, light complexity, overdraw — captured per area as density rises, not only once at the end.
- **Packaged-build load check** — the map loads clean outside the editor. Verify it; a working editor session does not generalize on its own.

## Evidence artifacts
- Reference/screenshot pairs per area, filed in the living spec, with every deliberate deviation logged as one line: what the reference showed, what got built, why.
- Full camera-rig screenshot sets (overview, path, reverse, detail, hero) captured per pass and kept as the regression baseline for the next pass.
- Automation test results from both CLI lanes, headless and rendered, with pass/fail named per test.
- Map Check output and session log excerpts showing zero errors, with any accepted warning listed alongside its justification.
- Per-asset lab verification: four to six angle screenshots plus a ground-contact shot, and for moving parts, one screenshot per state.
- Performance capture (`stat unit` / `stat gpu` output) per area at final density, compared against the stated budget.

## Common failure modes
- **Reporting a visual result that was never actually screenshotted** — a described shot is not a verified shot.
- **Auto-exposure left on**, making before/after and pass-to-pass comparisons meaningless because the metering shifted between shots.
- **A camera framing empty air or a wall** because look-at was eyeballed instead of computed from target bounds.
- **Assets modeled directly inside the main map**, so a bad mesh iteration pollutes level history and can't be isolated for testing.
- **Hard 90° seams where geometry meets ground** — the single fastest tell that a level is machine-placed rather than art-directed.
- **The same mesh placed at the same rotation and scale repeatedly**, producing visible tiling or mirroring instead of organic variation.
- **Polishing lighting or post-process on geometry about to be replaced**, burning a pass on work the next step invalidates.
- **Gap hunt skipped or folded into the build pass**, so holes, floating assets, and z-fighting ship because no one looked through the reverse camera.
- **Two agents editing the same map or sharing one editor instance**, corrupting unsaved state or racing on the same asset.

## Test-time compute verdict
High value on subjective, wide-solution-space work: organic terrain silhouette, rock and cliff composition, hero-shot framing, lighting mood, and greenfield massing from ambiguous reference art all benefit from generating multiple variants, screenshotting each, and keeping the one that wins the composition critique — quality here is a judged property, not a computed one. Low value on mechanical asset-pipeline steps: baking a mesh to spec, generating LODs, setting up collision to a known convention, naming and folder discipline — these have one correct answer, and searching over variants wastes budget better spent on more composition passes. Default to search-and-select for anything judged by a screenshot; default to single-pass correctness for anything judged by a validator.

## Definition-of-Done clauses
- Every area reaches the quality bar set by the first area taken to completion, proven by area-by-area screenshot sets plus reference/screenshot pairs and the deviation log.
- Gap hunt shows zero holes, seams, floating geometry, or z-fighting on any reverse or detail camera; the route is walkable end to end in PIE and in a packaged build, including wall-hugging.
- All placed assets are baked static meshes with correct pivot, collision, LODs, and lightmap UVs, verified from every angle in their lab, with moving parts tested in every state.
- Lighting, atmosphere, and post-process are in place per area with manual exposure locked; hero shots hold up against the reference intent.
- Zero Map Check errors, zero unexplained log warnings, performance within budget at final density.
- Both automation lanes — headless logic and rendered screenshot — pass from CLI, unattended, with current screenshot baselines committed.
