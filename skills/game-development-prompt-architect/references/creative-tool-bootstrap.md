# Creative Tool Bootstrap

Use this reference when the Goal needs a creative CLI, MCP server, DCC application, generator, converter, or missing asset-pipeline dependency. Bootstrap only the smallest toolchain that the accepted workflow actually needs. Never install every named tool speculatively.

## Bootstrap contract

The generated Goal must direct the executor to:

1. Inventory the host, project, PATH, package managers, installed versions, MCP registrations, engine importers, credentials state, and applicable organization policy before changing anything.
2. Select one primary route and one explicit fallback. Prefer maintained official tools, existing compatible installations, free/local options, user- or project-scoped configuration, and portable installs over administrator-wide changes.
3. Recheck the official publisher, package name, current stable version, system requirements, license, pricing, data handling, and host-specific configuration immediately before installation. Pin the resolved version in the project tool manifest; do not freeze a version from this reference.
4. Install missing free and reversible dependencies autonomously when they are necessary and allowed by the host. Do not reinstall, silently upgrade, downgrade, or duplicate a working toolchain. Treat elevation, policy prompts, and security controls as real host boundaries.
5. Keep authentication user-attended. Open the provider's official browser/device flow when needed; never ask the user to paste an API key into chat and never write credentials to the repository, Goal, screenshots, command history, generated manifests, or logs.
6. Run a version check, diagnostics, MCP discovery, and the smallest non-destructive smoke test. A smoke test must not consume paid credits unless the Goal already contains an approved budget.
7. Record the final tool, exact version, official source, install scope, configuration location, health-check evidence, capability/fallback, and removal path in `GAME_PLAN.md` or a repository-owned `TOOLCHAIN.md`. Record no secrets and do not commit machine-specific caches.

## Preferred Tripo route: CLI with built-in MCP

Use the current official Tripo CLI as the default agentic interface. Its documented prerequisites and commands must still be verified at execution time.

1. Confirm Node.js 20 or newer and a working npm global-prefix/PATH. If Node is missing or incompatible, install a current supported Node release through the host's trusted package path before Tripo.
2. Check whether `tripo` already resolves and is healthy. If missing, install the official package:

   ```text
   npm install -g tripo-cli
   ```

3. Verify the executable and run `tripo doctor`. Diagnose authentication, network, region, balance, and configuration failures instead of treating installation alone as success.
4. If sign-in is required, run `tripo login` and let the user complete the official browser/device authorization. Prefer Tripo profiles or environment-variable references for automation; never embed `TRIPO_API_KEY` values in MCP configuration or committed files.
5. Before composing generation commands, let the executor read the CLI's bundled agent documentation with `tripo docs --llm` and the relevant topic, such as `tripo docs --topic examples/game-asset` or `tripo docs --topic commands/make`.
6. Prefer the CLI's built-in STDIO MCP entry point, `tripo mcp`. Configure it only in the executing host and only if no equivalent `tripo` server is already registered:

   - Codex: `codex mcp add tripo -- tripo mcp`, then verify with `codex mcp list` and the host's MCP UI or tool discovery.
   - Claude Code: `claude mcp add --transport stdio --scope user tripo -- tripo mcp`, then verify with `claude mcp get tripo`, `claude mcp list`, and `/mcp` where available.

   Recheck current host CLI help and official documentation before executing these commands. Use user scope for a personal global CLI by default. Use project scope only when the team intentionally wants shared repository configuration, has reviewed the generated config, and no secret or machine-specific path will be committed.
7. Confirm that the MCP server starts, exposes the expected tools, and completes a diagnostic/read-only call. Do not generate a paid model merely to prove connectivity.

Official starting points:

- Tripo CLI: <https://developers.tripo3d.ai/en/docs/cli>
- Codex MCP: <https://learn.chatgpt.com/docs/extend/mcp?surface=cli>
- Claude Code MCP: <https://code.claude.com/docs/en/mcp>

## Optional live Blender integration

Do not install the separate `VAST-AI-Research/tripo-mcp` route merely because it exists. It is a distinct, alpha Blender-integration path and may overlap the CLI's built-in MCP.

Use it only when the task needs live Tripo control inside Blender, the current official compatibility matrix supports the selected Blender version, and the built-in `tripo mcp` route cannot satisfy the workflow. Then:

- verify the current official repositories, release or pinned commit, Python/`uv` requirements, Blender version, and addon compatibility;
- install the official Tripo Blender addon in a dedicated user or portable Blender profile, enable only the required addon, and keep its credentials outside the project;
- use an isolated Python environment or `uvx tripo-mcp` according to the current official instructions;
- register it under a distinct MCP name, document why it is required, and disable the overlapping route if duplicate tools would make routing ambiguous;
- validate connectivity in Blender and remove or disable the addon and MCP registration as the rollback path.

Official starting points:

- Tripo MCP: <https://github.com/VAST-AI-Research/tripo-mcp>
- Tripo for Blender: <https://github.com/VAST-AI-Research/tripo-3d-for-blender>

## Blender bootstrap and automation

- Preserve an existing project's known-good Blender version unless incompatibility is proven. For a new toolchain, resolve a current stable or LTS release that is compatible with the required addon and engine exporter.
- If Blender is required and absent, install that resolved release autonomously through the official installer, a trusted native package source, or an official portable archive appropriate to the host; then verify the executable and bundled Python before enabling addons.
- Download only from official Blender channels and verify the available signature or checksum. Prefer a portable, side-by-side user installation when it avoids administrator changes and version collisions.
- Distinguish a Blender Extension package from a legacy addon ZIP before choosing UI, command-line, or scripted installation. Never feed an unverified ZIP to an extension command.
- Treat Blender Python and addons as unrestricted code. Do not enable automatic execution for untrusted files, scripts, or drivers. Inspect third-party addon source and provenance before activation.
- Run reproducible automation with Blender's bundled Python in background mode. Keep the source script authoritative, pass a non-zero Python exit code on failure, save editable `.blend` sources and deterministic exports, and capture command/output evidence.
- Define units, axes, scale, origin/pivot, naming, collections, materials, texture color spaces, UVs, topology, skeleton, collision, LODs, and export format before engine import.

Official starting points:

- Blender installation: <https://docs.blender.org/manual/en/latest/getting_started/installing/index.html>
- Blender command line: <https://docs.blender.org/manual/en/latest/advanced/command_line/index.html>
- Blender scripting security: <https://docs.blender.org/manual/en/latest/advanced/scripting/security.html>

## Tripo-to-engine production workflow

1. Write an asset brief with gameplay purpose, target engine/platform, style traits, silhouette, scale, poly/texture budgets, rig/animation needs, and rejection criteria. Use concept or multiview references when they improve control and their rights permit upload.
2. Estimate the provider cost. If credits are not already approved, stop at the non-paid preparation boundary and request the cost gate. Otherwise generate several materially different candidates within the approved budget; never accept the first output by default.
3. Preserve task metadata such as `task.json`, prompts, reference provenance, provider/model/settings, timestamps, license terms, and generated previews without secrets.
4. Inspect silhouette, proportions, topology, manifold state, normals, UVs, materials, texture artifacts, rig weights, animations, and recognizable protected content. Reject candidates that cannot economically meet the brief.
5. Use authoritative Blender scripts for cleanup, retopology/decimation, UV/material repair, rigging, collision, LODs, naming, and export. Rerun the source instead of relying on undocumented hand edits.
6. Export a pinned engine-compatible GLB/glTF, FBX, or other justified format; import with reproducible settings; then test scale, axes, pivots, materials, skeleton, collision, LOD transitions, animation, memory, frame cost, and target-platform build behavior.
7. Compare in-engine captures against the Creative Direction Pack. Accept only production candidates that pass provenance, rights, style, gameplay, technical, and performance gates. Archive or delete rejected generated outputs according to project policy so the repository remains clean.

## Cost, rollback, and failure behavior

- Installing a necessary free, reversible tool is autonomous. A new charge, subscription, credit purchase, or generation outside an already approved budget remains a human gate.
- Provider login is a user-attended prerequisite, not a request for secrets. Continue all independent preparation while waiting when possible.
- On authentication, rate-limit, network, policy, insufficient-credit, or generation failure, retain diagnostic evidence, avoid blind retries, and use the documented fallback or stop at the relevant gate.
- Make setup idempotent. A rollback must name how to unregister the MCP server, disable/remove the addon, remove project configuration, and uninstall the CLI (for example `npm uninstall -g tripo-cli`) without deleting user assets or credentials unrelated to this Goal.
- Apply the same detect, official-source, minimal-install, secure-authentication, health-check, manifest, cost-gate, and rollback contract to any other image, video, audio, voice, 3D, DCC, conversion, or engine-bridge tool selected by the Goal.
