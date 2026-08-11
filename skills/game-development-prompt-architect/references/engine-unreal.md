# Unreal Engine Rules

Research snapshot: 2026-08-11. Verify official documentation again when compiling a Goal because versions and experimental tools can change.

## Version and implementation mode

- Existing project: pin its exact UE build. Never migrate implicitly.
- New project: verify the current stable UE 5.8-or-newer release and installed toolchain, then pin the exact build. UE 5.8 is officially available; do not guess the latest 5.8.x hotfix.
- Default to **C++ first, Blueprint friendly**: durable systems, performance-critical loops, data-heavy logic, integrations, and test seams in C++; expose narrow documented Blueprint APIs for designer iteration.
- Respect explicit `Blueprint-only` or `C++-only` requirements. Blueprint-only still requires source-control ownership, automated tests where supported, and engine evidence. C++-only must not silently create Blueprint dependencies.

Official sources: [UE 5.8 documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-documentation) and [Blueprint versus C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus).

## Agentic editor workflow

Unreal MCP is Epic's official Unreal Editor MCP server. Its plugin identifier is `ModelContextProtocol`; it is Experimental, incomplete, and API/data-format unstable. Detect availability before enabling it. Use it only on local loopback, never expose its unauthenticated server remotely, and assume tool calls run serially on the game thread. Enable only required toolsets, read state before mutation, make one focused change, save, inspect, and test.

Do not make the experimental MCP the only path. Maintain C++, commandlet, Python, UAT, and test automation fallbacks. Put durable custom MCP tools and editor automation in a versioned project plugin rather than patching the engine installation.

Official sources: [Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor), [ModelContextProtocol API](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/ModelContextProtocol), and [plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine).

## Code, content, and automation

- Use Python for editor/content/asset/level automation, not runtime gameplay. Prefer `UnrealEditor-Cmd` with an explicit project, script, map when required, logs, and exit condition.
- Commandlets run without a normal interactive world; explicitly load required content and never assume editor selection/state.
- Make repeatable content changes through source-controlled scripts or project plugins. Rerun the source after changes rather than hand-fixing only generated assets.
- The executor may enable or create required project plugins when compatible, reversible, licensed, and verified. Record descriptor/module changes and restart requirements.

Official sources: [Python editor scripting](https://dev.epicgames.com/documentation/unreal-engine/scripting-the-unreal-editor-using-python), [command-line arguments](https://dev.epicgames.com/documentation/unreal-engine/command-line-arguments-in-unreal-engine), and [Commandlet API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UCommandlet).

## Build and test ladder

1. Compile affected targets and project plugins with the pinned toolchain.
2. Run focused Automation Framework tests through command line and persist reports with explicit export paths.
3. Load affected maps/assets and scan logs for relevant errors, warnings, invalid references, shader/Blueprint compilation, and cook issues.
4. Use Gauntlet/`RunUAT RunUnreal` for boot, packaged target, device, networking, and session tests. Gauntlet tests supplied builds; it does not replace build creation.
5. Express repeatable build/cook/test/package dependencies in BuildGraph and run through UAT. Preserve logs and artifacts.
6. Capture representative PIE/standalone/packaged visual, gameplay, and performance evidence on target hardware.

Official sources: [Automation Framework](https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine), [run automation tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/run-automation-tests-in-unreal-engine), [Gauntlet](https://dev.epicgames.com/documentation/en-us/unreal-engine/gauntlet-automation-framework-overview-in-unreal-engine), [RunUnreal](https://dev.epicgames.com/documentation/en-us/unreal-engine/running-gauntlet-tests-in-unreal-engine), and [BuildGraph](https://dev.epicgames.com/documentation/unreal-engine/buildgraph-for-unreal-engine).

## Parallel ownership and source control

Treat `.uasset` and `.umap` files as non-textual, conflict-prone ownership units. Lock or assign them exclusively per workstream; do not rely on Git to semantically merge binary assets. Parallelize C++ and text/config files only behind stable interfaces. Serialize map, Blueprint, material graph, Data Asset, and other shared binary edits through the integration queue.

Use the repository's existing Git, Perforce, or other policy. Keep engine-generated directories and local caches out of production commits. Official source-control guidance: [Source Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/source-control-in-unreal-engine) and [Perforce workflow](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine).
