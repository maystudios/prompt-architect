# Godot Rules

Research snapshot: 2026-08-11. Godot 4.7.1-stable was the current official stable release on that date; 4.8 was still development. Verify again at Goal-compilation time and pin the exact editor plus matching export templates.

Official release: [Godot 4.7.1-stable](https://godotengine.org/download/archive/4.7.1-stable/).

## Version and language

- Existing project: preserve the detected exact version and its GDScript/.NET choice.
- New project: verify the current stable release and target-platform support, then pin it. Do not choose a preview build for production automation by default.
- Prefer GDScript for a new agent-driven project because it is tightly integrated with Godot, fast to parse/run, and well suited to small coherent source files. Use C# when the project already uses .NET, an actual .NET library/requirement justifies it, or the user asks for it.
- Do not mix GDScript and C# casually. C# needs the .NET editor and SDK; verify platform limits before choosing it, especially web and mobile.

Official sources: [GDScript/C# overview](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/scripting_languages.html) and [C# platform support](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/index.html).

## Text-first agentic workflow

Edit authoritative sources such as `project.godot`, `.gd`, `.cs`, text `.tscn`/`.tres`, source assets, and `export_presets.cfg`. Do not commit `.godot/` caches or `export_credentials.cfg` secrets. Version `.sln`/`.csproj` when using C#.

Before automation, execute the detected binary's `--version` and `--help`; Godot command availability varies by binary type and unknown arguments may be silently ignored. Prefer explicit `--path`, `--headless`, `--log-file`, and deterministic exit codes.

After asset, scene, importer, or plugin changes, run an explicit headless import before tests or export. Use CLI scripts that extend `SceneTree`/`MainLoop` for batch validation and terminate with a meaningful success/failure code.

Official sources: [command-line tutorial](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html), [version-control guidance](https://docs.godotengine.org/en/4.7/tutorials/best_practices/version_control_systems.html), and [SceneTree](https://docs.godotengine.org/en/4.7/classes/class_scenetree.html).

## Editor tools and plugins

Use `@tool`/`[Tool]`, `EditorScript`, and `EditorPlugin` only for work that truly requires editor state or reusable editor integration. Tool scripts are privileged: they can make persistent changes without undo/redo and can destabilize the editor. Save/commit first, scope mutations, and verify their exact result.

Prefer a headless project script for repeatable batch work. Use recovery mode before opening a broken or untrusted project when supported so tool scripts, plugins, and extensions cannot immediately execute. The executor may install, enable, or build a project plugin when pinned, licensed, reversible, and tested.

Official sources: [running code in the editor](https://docs.godotengine.org/en/4.7/tutorials/plugins/running_code_in_the_editor.html) and [making editor plugins](https://docs.godotengine.org/en/4.7/tutorials/plugins/editor/making_plugins.html).

## Test and export ladder

1. Run import and syntax/parse checks for changed scripts and text resources.
2. Build the C# solution when applicable.
3. Run a project-owned headless test harness with assertions, timeout, logs, and nonzero failure exit. Godot's documented `--test` command is for a specially compiled engine's own C++ tests, not a built-in user-project unit-test runner. Treat third-party test frameworks as explicit pinned dependencies.
4. Launch affected scenes and the game smoke route; scan logs and validate resource references.
5. Run non-headless visual/audio/gameplay captures. Headless disables display/audio drivers and cannot prove rendered or mixed output.
6. Profile representative content with the relevant debugger, monitors, script/physics/network and visual profiler views; distinguish CPU and GPU evidence.
7. Export through the editor binary with matching export templates and a versioned preset. Store build artifacts outside source paths and smoke-test the exported target.

Official sources: [command-line testing and export](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html), [exporting projects](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_projects.html), and [debugger/profiler](https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/debugger_panel.html).

## MCP and external agents

Do not claim that Godot has an official MCP server: none was verified in the official 4.7 documentation. Officially documented agent-friendly surfaces are the text project format, CLI, GDScript language server, and debug adapter. A third-party MCP may be used only after its source, permissions, version, compatibility, license, and fallback are verified; it must never be the sole route or sole proof of success.

Official source: [external editor, LSP and DAP](https://docs.godotengine.org/en/4.7/tutorials/editor/external_editor.html).
