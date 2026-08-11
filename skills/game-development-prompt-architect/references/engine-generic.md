# Generic and Custom Engine Rules

Use this profile only when no Unreal, Unity, or Godot profile applies, or when the engine is proprietary.

## Ground first

- Detect the engine, fork, exact commit/version, language, project format, supported platforms, build system, asset pipeline, editor/runtime boundary, and authoritative documentation.
- Prefer repository-text source and deterministic command-line automation. Use editor GUI automation only for states that cannot be represented or verified through code, data, or supported APIs.
- Do not assume another engine's scene, component, serialization, shader, physics, or import model transfers directly.

## Architecture

Keep gameplay rules independent of rendering/editor code where the engine permits. Define ownership, lifecycle, update/tick phase, data serialization, event flow, threading, memory, coordinate/unit, and deterministic/network boundaries before parallel implementation.

Build small editor or command-line adapters for repeatable imports, scene creation, validation, builds, tests, and captures. Durable adapters require tests and documentation; scratch automation follows the Tooling Lab and cleanup rules.

## Verification

Establish the engine's real test and automation surface from official/project sources. At minimum require a clean compile, representative content load, smoke gameplay path, target-platform build, relevant log scan, asset/reference validation, and performance sample. Record exact commands and observable artifacts in the Goal.

If the engine lacks adequate automation, create the smallest project-owned test harness possible and pair it with controlled engine captures. Do not claim headless support, hot reload, deterministic simulation, or plugin capabilities without observing them.
