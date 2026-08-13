#!/usr/bin/env python3
"""Lint a compiled Game Development Prompt Architect Goal prompt.

Usage:
    python lint_goal_prompt.py GOAL.md --engine unreal --main-goal
    python lint_goal_prompt.py GOAL.md --engine unity
    python lint_goal_prompt.py GOAL.md --engine unreal --requires-tool-bootstrap

Stdlib only. Exit 0 means no errors; warnings may remain.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED = [
    "SETUP",
    "GOAL",
    "PROJECT TRUTH & DECISION LEDGER",
    "SCOPE",
    "FIRST ACTION",
    "WORKING METHOD",
    "TESTING, PLAYTESTING & EVIDENCE",
    "KNOWLEDGE & SECOND BRAINS",
    "MODEL ROUTING & PARALLELISM",
    "INTEGRATION & VERSION CONTROL",
    "AUTONOMY & HUMAN GATES",
    "DEFINITION OF DONE",
]

ENGINE_TITLES = {
    "unreal": "UNREAL",
    "unity": "UNITY",
    "godot": "GODOT",
    "generic": "GENERIC",
}

PLACEHOLDERS = [
    (r"\b(?:TODO|TBD|FIXME|XXX)\b", "unfinished marker"),
    (r"\bpath/to/", "stub path"),
    (r"\[insert\b", "insert slot"),
    (r"\{\{[^}\n]+\}\}", "template slot"),
    (r"<[A-Za-z][^<>\n]{0,60}>", "angle-bracket slot"),
]

GLOBAL_BRAIN = "https://github.com/maystudios/VaultGameDevelopment"
PROJECT_BRAIN = "https://github.com/maystudios/better-second-brain"


def top_sections(text: str) -> list[tuple[str, str]]:
    """Return top-level heading and body pairs, ignoring fenced examples."""
    sections: list[tuple[str, str]] = []
    title: str | None = None
    body: list[str] = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced and re.match(r"^#\s+\S", line):
            if title is not None:
                sections.append((title, "\n".join(body).strip()))
            title = re.sub(r"^#\s+", "", line).strip()
            body = []
        elif title is not None:
            body.append(line)
    if title is not None:
        sections.append((title, "\n".join(body).strip()))
    return sections


def contains_all(text: str, terms: tuple[str, ...]) -> bool:
    low = text.lower()
    return all(term in low for term in terms)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--engine", choices=["auto", *ENGINE_TITLES], default="auto")
    parser.add_argument("--main-goal", action="store_true")
    parser.add_argument("--cross-engine", action="store_true")
    parser.add_argument(
        "--requires-tool-bootstrap",
        action="store_true",
        help="require safe inventory/install/configure/health-check instructions for creative tools",
    )
    parser.add_argument("--max-chars", type=int, default=0,
                        help="optional positive character ceiling; 0 means no arbitrary ceiling")
    args = parser.parse_args()

    try:
        text = args.file.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR  cannot read {args.file}: {exc}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    sections = top_sections(text)
    titles = [title for title, _ in sections]

    if args.max_chars > 0 and len(text) > args.max_chars:
        errors.append(f"length {len(text)} exceeds --max-chars {args.max_chars}")

    found: list[int] = []
    for required in REQUIRED:
        hits = [i for i, title in enumerate(titles) if title.upper().startswith(required)]
        if not hits:
            errors.append(f"required section missing: # {required}")
        elif len(hits) > 1:
            errors.append(f"duplicate section: # {required}")
        else:
            found.append(hits[0])
    if found != sorted(found):
        errors.append("required sections are out of canonical order")

    for title, body in sections:
        if not body:
            errors.append(f"empty section: # {title}")

    engine_sections = [title for title in titles if title.upper().startswith("ENGINE RULES")]
    if not engine_sections:
        errors.append("engine work requires one # ENGINE RULES section")
    if len(engine_sections) > 1 and not args.cross_engine:
        errors.append("multiple engine profiles require --cross-engine and an explicit cross-engine Goal")
    if args.engine != "auto" and engine_sections:
        expected = ENGINE_TITLES[args.engine]
        if not any(expected in title.upper() for title in engine_sections):
            errors.append(f"--engine {args.engine} does not match: {engine_sections}")

    if args.main_goal:
        for heading in ("STUDIO ORCHESTRATION & GOAL PACKETS", "PLANNING & VISUAL CONTROL PLANE"):
            if not any(title.upper().startswith(heading) for title in titles):
                errors.append(f"main Goal missing: # {heading}")

    bootstrap = next(
        (body for title, body in sections if title.upper().startswith("TOOLCHAIN BOOTSTRAP & HEALTH CHECK")),
        "",
    )
    if args.requires_tool_bootstrap:
        if not bootstrap:
            errors.append("tool-dependent Goal missing: # TOOLCHAIN BOOTSTRAP & HEALTH CHECK")
        else:
            bootstrap_low = bootstrap.lower()
            for alternatives, label in (
                (("inventory", "detect", "inspect"), "inventory before installation"),
                (("official", "publisher"), "official-source verification"),
                (("health", "diagnostic", "doctor"), "health check"),
                (("rollback", "uninstall", "remove"), "rollback"),
                (("secret", "credential", "api key", "token"), "secret handling"),
            ):
                if not any(term in bootstrap_low for term in alternatives):
                    errors.append(f"tool bootstrap omits: {label}")

            if "tripo" in bootstrap_low:
                tripo_requirements = (
                    ("npm install -g tripo-cli", "official Tripo CLI install command"),
                    ("tripo doctor", "Tripo health check"),
                    ("tripo mcp", "Tripo built-in MCP entry point"),
                )
                for term, label in tripo_requirements:
                    if term not in bootstrap_low:
                        errors.append(f"Tripo bootstrap omits: {label}")
                if "node" not in bootstrap_low or not re.search(r"\b20(?:\+|\s+or\s+(?:newer|later)|\s+and\s+newer)?\b", bootstrap_low):
                    errors.append("Tripo bootstrap must verify Node.js 20 or newer")
                if not any(term in bootstrap_low for term in ("credit", "paid", "approved budget", "cost")):
                    errors.append("Tripo bootstrap omits the paid-credit gate")
                if not re.search(
                    r"(?:never|do not|must not).{0,100}(?:api key|secret|credential|token)|"
                    r"(?:api key|secret|credential|token).{0,100}(?:never|do not|must not)",
                    bootstrap,
                    re.I | re.S,
                ):
                    errors.append("Tripo bootstrap must explicitly prohibit exposing credentials")

    if re.search(r"TRIPO_API_KEY\s*=\s*['\"]?[A-Za-z0-9_-]{16,}", text):
        errors.append("possible literal TRIPO_API_KEY secret in Goal")

    for pattern, label in PLACEHOLDERS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            line = text[: match.start()].count("\n") + 1
            errors.append(f"line {line}: {label}: {match.group(0)!r}")

    setup = next((body for title, body in sections if title.upper().startswith("SETUP")), "")
    if "english" not in setup.lower():
        errors.append("SETUP must instruct the executor to work and report in English")

    if GLOBAL_BRAIN not in text:
        errors.append("global game-development brain URL is missing or not exact")
    if PROJECT_BRAIN not in text:
        errors.append("project-brain foundation URL is missing or not exact")

    gates = next((body for title, body in sections if title.upper().startswith("AUTONOMY & HUMAN GATES")), "")
    gate_groups = (
        ("engine", "migrat"),
        ("cost", "subscription", "paid"),
        ("rights", "license", "provenance"),
        ("irreversible", "destructive"),
    )
    for alternatives in gate_groups:
        if not any(term in gates.lower() for term in alternatives):
            errors.append(f"human gates omit concept: {'/'.join(alternatives)}")

    if not re.search(r"never (?:report|claim).{0,80}(?:not observed|have not observed|unobserved)", text, re.I | re.S):
        errors.append("observed-evidence rule is missing")
    if not re.search(
        r"single[- ]writer\s+curator|one\s+curator.{0,80}(?:owns|writes|curates)|"
        r"curator.{0,80}(?:only|sole|single)\s+(?:writer|writes)",
        text,
        re.I | re.S,
    ):
        errors.append("one explicit single-writer curator is missing")
    if re.search(r"(?:no|without|skip)\s+(?:separate\s+|dedicated\s+)?curator", text, re.I):
        errors.append("Goal negates the required curator; bounded Goals still run one lightweight curator")
    if not contains_all(text, ("worktree", "testing branch")):
        warnings.append("Goal does not name both worktree isolation and a testing branch")
    if re.search(r"\b(?:latest|newest)\s+(?:engine|version|release)\b", text, re.I) and not re.search(
        r"verify.{0,100}(?:official|production-ready|stable)", text, re.I | re.S
    ):
        warnings.append("a floating latest/newest engine claim lacks an official verification instruction")

    print(f"length: {len(text)} chars; sections: {len(sections)}; engine sections: {len(engine_sections)}")
    for warning in warnings:
        print(f"WARN   {warning}")
    for error in errors:
        print(f"ERROR  {error}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
