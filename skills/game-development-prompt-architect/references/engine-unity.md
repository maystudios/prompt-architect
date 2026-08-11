# Unity Rules

Research snapshot: 2026-08-11. Verify Unity release support, the exact Editor revision, packages, CLI, Pipeline package, target modules, and licenses again when compiling the Goal.

## Version and code

- Existing project: preserve the exact revision in `ProjectSettings/ProjectVersion.txt` and the resolved packages in `Packages/manifest.json` plus `packages-lock.json`. Never migrate implicitly.
- New project: choose from Unity's current production-ready releases according to stage. Unity recommends Update releases for new and mid-cycle production and LTS for live games or projects locking production. Pin a full revision rather than `latest` or `lts` aliases after setup.
- Use C# as the authoritative gameplay, systems, editor-tooling, test, and build language. Keep MonoBehaviours thin where practical, separate pure logic for fast tests, and define assembly boundaries with `.asmdef` files when they materially improve compile/test ownership.

Official sources: [Unity 6 release support](https://unity.com/releases/unity-6/support) and [Unity project manifest](https://docs.unity3d.com/Manual/upm-manifestPrj.html).

## Official Unity CLI and Pipeline

Unity CLI is an official standalone command-line tool for managing Editors, modules, projects, authentication, and structured automation output. It is **Experimental**. Detect and pin its actual version; use exact Editor revisions and modules rather than floating aliases in reproducible workflows. The older Hub CLI is deprecated for new automation.

The official Unity Pipeline package exposes a local HTTP API to a running Unity Editor and allows Unity CLI commands, status queries, custom commands, builds/tests, and C# evaluation such as `unity eval`. It requires Unity 6.0 or later and installation into the project. Treat both CLI and Pipeline as privileged experimental tooling: bind locally, scope commands, protect credentials, prefer structured output/exit codes, and retain standard Editor batchmode fallbacks.

Do not claim an official Unity MCP unless current Unity documentation explicitly provides one; none was verified in this research. A third-party MCP must be separately pinned, permission-scoped, licensed, and optional.

Official sources: [Unity CLI](https://docs.unity.com/en-us/unity-cli/unity-cli), [Unity CLI release notes](https://docs.unity.com/en-us/unity-cli/release-notes), [Unity Pipeline package](https://docs.unity.com/en-us/unity-production-pipeline/local-tools-cli/unity-pipeline-package), and [deprecated Hub CLI](https://docs.unity.com/en-us/hub/hub-cli-reference).

## Editor and package automation

- Keep repeatable editor mutations in tested C# Editor code, custom commands, or a project/package tool with a stable interface. Avoid dependence on selection, window focus, or manual Inspector state.
- Use the Editor executable with `-batchmode`, explicit `-projectPath`, `-logFile`, `-executeMethod`, and `-quit` as the durable CI fallback. Use `-nographics` only when the job does not need rendering/GPU validation.
- Let Unity own `.meta` files; never separate an asset from its metadata. Prefer visible text serialization and verify scene/prefab/scriptable-object changes after import.
- Add or enable packages/plugins only through a versioned project manifest, embedded/local package, or documented native-plugin layout. Pin versions and transitive resolution; record licensing, platform binaries, importer settings, and domain-reload/restart effects.
- Keep `Library`, `Temp`, `Logs`, build outputs, and other regenerated state out of production commits according to project policy.

Official sources: [Editor command-line arguments](https://docs.unity3d.com/Manual/CommandLineArguments.html), [creating custom Editor tools](https://docs.unity3d.com/Manual/editor-CustomEditors.html), and [Unity Package Manager](https://docs.unity3d.com/Manual/Packages.html).

## Test and build ladder

1. Let the Editor import and compile in batchmode; fail on compiler errors and inspect the full log, not only console summary.
2. Run Unity Test Framework EditMode tests for pure/editor logic and PlayMode tests for runtime behavior; execute relevant tests on the target player when platform behavior matters. Persist NUnit-compatible result XML.
3. Collect code coverage when useful, but do not optimize coverage percentage instead of behavior and risk.
4. Run scene/prefab/addressable/resource validation, missing-reference checks, package validation, shader compilation, and representative play-mode smoke routes.
5. Build through a source-controlled C# build entry point or verified Build Profile and `BuildPipeline`, with deterministic output, platform modules, scripting backend, scenes, and options.
6. Launch and smoke-test the produced player. Capture visual, audio, input, networking, save/load, and performance evidence on representative target hardware.

Official sources: [automated testing](https://docs.unity3d.com/Manual/testing-editortestsrunner.html), [Test Framework command line](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/reference-command-line.html), [Code Coverage package](https://docs.unity3d.com/Packages/com.unity.testtools.codecoverage@latest), [Build Profiles](https://docs.unity3d.com/Manual/build-profiles.html), and [BuildPipeline API](https://docs.unity3d.com/ScriptReference/BuildPipeline.html).

## Parallel ownership and integration

Assign scenes, prefabs, ScriptableObjects, materials/graphs, project settings, and package manifests to one workstream at a time even when they are text-serialized; semantic merges remain fragile. Parallelize C# assemblies and isolated assets behind defined APIs. Use UnityYAMLMerge only as an aid, then open/import/test the merged result in the pinned Editor.

Do not run multiple writers against the same Unity project/Library. Give each independent session its own worktree and local generated state, then serialize verified integration into the testing branch.

Official source: [Smart Merge](https://docs.unity3d.com/Manual/SmartMerge.html).
