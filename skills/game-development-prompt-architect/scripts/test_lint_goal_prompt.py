#!/usr/bin/env python3
"""Self-tests for lint_goal_prompt.py."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
LINTER = HERE / "lint_goal_prompt.py"

VALID = """# SETUP
Work and report in English. Verify current official stable capabilities.
# GOAL
Deliver a playable movement slice.
# PROJECT TRUTH & DECISION LEDGER
Godot is pinned by the project manifest.
# SCOPE
Movement only.
# FIRST ACTION
Inspect the project and write GAME_PLAN.md.
# WORKING METHOD
Use one coherent tested unit at a time.
# ENGINE RULES — GODOT
Use the pinned Godot version.
# TESTING, PLAYTESTING & EVIDENCE
Never report a result not observed. Run an engine smoke test.
# KNOWLEDGE & SECOND BRAINS
Query https://github.com/maystudios/VaultGameDevelopment and initialize from https://github.com/maystudios/better-second-brain when absent. Use a single-writer curator.
# MODEL ROUTING & PARALLELISM
Discover current capabilities and route by risk.
# INTEGRATION & VERSION CONTROL
Use an isolated worktree and merge verified work serially into the testing branch.
# AUTONOMY & HUMAN GATES
Ask before engine migration, new cost or paid subscription, unclear rights/license/provenance, or irreversible destructive external action.
# DEFINITION OF DONE
The slice passes observed engine and target build tests and the repository is clean.
"""

VALID_MAIN = VALID.replace(
    "# TESTING, PLAYTESTING & EVIDENCE",
    "# STUDIO ORCHESTRATION & GOAL PACKETS\n"
    "Compile self-contained child packets and isolate independent sessions.\n"
    "# PLANNING & VISUAL CONTROL PLANE\n"
    "Keep GAME_PLAN.md canonical and synchronize optional planning views.\n"
    "# TESTING, PLAYTESTING & EVIDENCE",
)

VALID_TRIPO = VALID.replace(
    "# ENGINE RULES — GODOT",
    "# TOOLCHAIN BOOTSTRAP & HEALTH CHECK\n"
    "Inventory the existing host and MCP registrations before installation. Verify the official publisher and current compatibility. "
    "Require Node.js 20 or newer; when missing, install with `npm install -g tripo-cli`. Authenticate with the official browser flow and never expose an API key, credential, token, or secret in chat, config, logs, or the repository. "
    "Register the built-in `tripo mcp` route for the detected host, run `tripo doctor`, inspect MCP tools, and use only a no-cost diagnostic smoke test. "
    "Paid generation and credits require an approved budget. Record exact versions and evidence in TOOLCHAIN.md; include rollback and `npm uninstall -g tripo-cli`.\n"
    "# ENGINE RULES — GODOT",
)


def run(text: str, *args: str) -> int:
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / "goal.md"
        path.write_text(text, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(LINTER), str(path), *args],
            check=False,
            capture_output=True,
            text=True,
        )
        return result.returncode


def main() -> int:
    cases = [
        ("valid", VALID, ("--engine", "godot"), 0),
        ("placeholder", VALID.replace("Movement only.", "TODO: decide movement."), ("--engine", "godot"), 1),
        ("missing brain", VALID.replace("https://github.com/maystudios/VaultGameDevelopment", "missing"), ("--engine", "godot"), 1),
        ("negated curator", VALID.replace("Use a single-writer curator.", "Use no separate curator."), ("--engine", "godot"), 1),
        ("wrong engine", VALID, ("--engine", "unity"), 1),
        ("valid main", VALID_MAIN, ("--engine", "godot", "--main-goal"), 0),
        ("main without studio", VALID, ("--engine", "godot", "--main-goal"), 1),
        ("valid Tripo bootstrap", VALID_TRIPO, ("--engine", "godot", "--requires-tool-bootstrap"), 0),
        (
            "Tripo bootstrap missing doctor",
            VALID_TRIPO.replace("run `tripo doctor`, ", ""),
            ("--engine", "godot", "--requires-tool-bootstrap"),
            1,
        ),
        ("missing tool bootstrap section", VALID, ("--engine", "godot", "--requires-tool-bootstrap"), 1),
        (
            "literal Tripo secret",
            VALID_TRIPO.replace("Register the built-in", "TRIPO_API_KEY=abcdefghijklmnop Register the built-in"),
            ("--engine", "godot", "--requires-tool-bootstrap"),
            1,
        ),
    ]
    failed = []
    for name, text, args, expected in cases:
        actual = run(text, *args)
        print(f"{'PASS' if actual == expected else 'FAIL'}  {name}: exit {actual}, expected {expected}")
        if actual != expected:
            failed.append(name)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
