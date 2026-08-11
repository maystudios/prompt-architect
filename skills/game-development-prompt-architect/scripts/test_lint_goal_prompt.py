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
