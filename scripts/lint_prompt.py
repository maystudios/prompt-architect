#!/usr/bin/env python3
"""Deterministic lint for a compiled prompt-architect prompt.

A model cannot count characters or reliably spot every leftover placeholder.
This can. Run it on the prompt body before emitting.

    python lint_prompt.py prompt.md
    python lint_prompt.py prompt.md --budget compact
    python lint_prompt.py prompt.md --budget 6000
    python lint_prompt.py prompt.md --phased        # PHASE-structured variant

Exit 0 = clean (warnings allowed). Exit 1 = at least one error.
Stdlib only.
"""

from __future__ import annotations

import argparse
import re
import sys

REQUIRED = [
    "SETUP",
    "MISSION",
    "SCOPE",
    "FIRST ACTION",
    "WORKING METHOD",
    "TESTING & VERIFICATION",
    "MODEL ROUTING & PARALLELISM",
    "SELF-IMPROVEMENT",
    "DEFINITION OF DONE",
]

# In the phase-structured variant (references/prompt-template.md) MISSION, SCOPE and
# FIRST ACTION fold into the phase bodies. SETUP stays first, the closing four stay last.
REQUIRED_PHASED = [
    "SETUP",
    "WORKING METHOD",
    "TESTING & VERIFICATION",
    "MODEL ROUTING & PARALLELISM",
    "SELF-IMPROVEMENT",
    "DEFINITION OF DONE",
]

# Body ceilings. The emitted prompt ships inside a fenced code block; "```markdown\n"
# plus "\n```" costs 16 characters. Compact must survive a user copying the fences
# into a field with a hard 4,000 limit, so the body ceiling is 3,950.
BUDGETS = {"compact": (0, 3950, 3850), "standard": (10000, 15000, 13000)}
FENCE_OVERHEAD = 16

PLACEHOLDERS = [
    # A TODO/FIXME opening a line, followed by punctuation or nothing, is leftover
    # scaffolding. "- TODO entries go in GOAL.md" is an instruction and must pass.
    (r"(?m)^\s*(?:[-*+]\s*|\d+\.\s*)?(?:TODO|FIXME)\s*(?::|$|\)|\.)", "leftover TODO/FIXME item"),
    (r"\bTBD\b", "TBD marker"),
    (r"\bXXX\b", "XXX marker"),
    # Only the isolated-token form. "Placeholder content masking real defects" is a
    # failure mode rules/domains/ui-ux.md requires compiling, and `::placeholder` is a
    # real CSS selector — banning the word outright blocks legitimate UI prompts.
    (r"(?m)^\s*(?:[-*+]\s*)?PLACEHOLDER\s*$", "isolated PLACEHOLDER token"),
    (r"\[insert\b", "[insert ...] slot"),
    (r"\bpath/to/", "path/to/ stub path"),
    (r"\byour[-_](project|app|repo|branch|file|framework)\b", "your-* stub"),
    (r"\bfoo\b|\bbaz\b|\bfoobar\b", "metasyntactic stub name"),
    (r"\blorem ipsum\b", "lorem ipsum"),
]

# Any angle-bracket slot, either case. The rail files ship `<N> agents in parallel`
# and `<Test-time compute: yes or no>`; a lowercase-only pattern cannot see those,
# and the rail template is the most likely thing to get pasted verbatim.
SLOT = re.compile(r"<[A-Za-z][^<>\n]{0,48}>")

# The rule files' compiled-form blocks mark their fill-in points with {{double braces}}.
# One surviving into an emitted prompt is a placeholder like any other.
BRACE_SLOT = re.compile(r"\{\{[^}\n]{1,60}\}\}")

FENCE = re.compile(r"```.*?```", re.S)

FABLE_BAN = re.compile(r"never\s+use\s+fable|never\s+fable|fable\s+is\s+barred", re.I)
LATENCY_BAN = re.compile(r"fast\s*mode|/fast|paid\s+latency|latency\s+tier|priority\s+tier", re.I)
EVIDENCE_RULE = re.compile(
    r"did ?n[o']t happen|not observed|have not (actually )?(looked|seen)|screenshot or it", re.I)
# A git end-state clause needs both halves: something that names where the work lands,
# and something that names the cleanup. A bare "branch" anywhere in the DoD — "each
# redesign branch is covered by a golden test" — is not a git clause.
GIT_LANDS = re.compile(r"\bbranch\b|\bworktree\b|\bmerged?\b|\blands? on\b", re.I)
GIT_CLEANUP = re.compile(r"\bclean\b|\bdeleted?\b|\bremoved?\b|no stashes|no uncommitted|"
                         r"detached HEAD|\bmerged (back )?(in)?to\b", re.I)

# Exactly one rail may be emitted. Both rails legitimately name the other family through
# a bridge, so the bridge name — not the roster — is what identifies the rail.
RAIL_A_BRIDGE = re.compile(r"codex rescue", re.I)
RAIL_B_BRIDGE = re.compile(r"claude bridge", re.I)
FAMILY_A = re.compile(r"\bopus\b|\bsonnet\b", re.I)
FAMILY_B = re.compile(r"gpt-5\.6-sol|\bluna\b|\bterra\b", re.I)
NO_REPO = re.compile(
    r"no (version control|repository|git repo)\b(?!\s*(restructur|refactor|change|migration))"
    r"|not a git repositor|version control is not", re.I)


def strip_fences(text: str) -> str:
    """Blank out fenced blocks only.

    Inline code is deliberately kept: paths, branches and filenames live in backticks,
    which is exactly where a leftover slot like `<branch name>` hides. Stripping inline
    code would make the placeholder ban unenforceable on the values it most protects.
    """
    return FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def headings(text: str) -> list[tuple[int, str]]:
    out = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
        if m:
            out.append((i, m.group(1) + " " + m.group(2)))
    return out


def section_bodies(text: str) -> dict[str, str]:
    """Map top-level heading title -> body text under it."""
    bodies: dict[str, str] = {}
    current, buf, in_fence = None, [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#\s+\S", line):
            if current is not None:
                bodies[current] = "\n".join(buf)
            current = re.sub(r"^#\s+", "", line).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        bodies[current] = "\n".join(buf)
    return bodies


def body_of(bodies: dict[str, str], prefix: str) -> str:
    return next((b for t, b in bodies.items() if t.upper().startswith(prefix)), "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--budget", default="standard",
                    help="compact | standard | an integer character ceiling")
    ap.add_argument("--phased", action="store_true",
                    help="PHASE-structured variant: MISSION, SCOPE and FIRST ACTION "
                         "fold into the phase bodies")
    args = ap.parse_args()

    try:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"ERROR  cannot read {args.file}: {exc}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    required = REQUIRED_PHASED if args.phased else REQUIRED

    # --- length -----------------------------------------------------------
    n = len(text)
    if args.budget in BUDGETS:
        low, high, target = BUDGETS[args.budget]
    else:
        try:
            high = int(args.budget)
        except ValueError:
            print(f"ERROR  --budget must be compact, standard, or an integer; got {args.budget!r}")
            return 1
        low, target = 0, int(high * 0.95)

    if n > high:
        errors.append(f"length {n} chars exceeds the {args.budget} ceiling of {high} "
                      f"(over by {n - high}) — apply the compression ladder in rules/09")
    elif low and n < low:
        warnings.append(
            f"length {n} chars is below the {args.budget} band floor of {low}. A small "
            f"single-surface task legitimately lands here — answer this with one sentence "
            f"in the preamble rather than padding or adding a conditional section")
    print(f"length: {n} chars body, {n + FENCE_OVERHEAD} fenced "
          f"(budget {args.budget}, target ~{target}, body ceiling {high})")

    # --- required sections ------------------------------------------------
    hs = headings(text)
    top_titles = [h[2:].strip() for _, h in hs if h.startswith("# ")]

    found_order: list[str] = []
    for req in required:
        hit = next((t for t in top_titles if t.upper().startswith(req)), None)
        if hit is None:
            errors.append(f"required section missing: # {req}")
        else:
            found_order.append(hit)

    canonical = [t for t in top_titles if any(t.upper().startswith(r) for r in required)]
    if canonical != found_order:
        errors.append("required sections are out of canonical order — see rules/03-sections.md")

    if args.phased and not any(t.upper().startswith("PHASE") for t in top_titles):
        errors.append("--phased was given but no # PHASE section exists")

    for d in sorted({t for t in top_titles if top_titles.count(t) > 1}):
        errors.append(f"duplicate top-level section: # {d}")

    # --- heading convention ----------------------------------------------
    for ln, h in hs:
        if h.startswith("## "):
            warnings.append(f"line {ln}: nested heading '{h}' — house style is flat `# UPPERCASE`; "
                            f"use a bold lead-in instead")
        elif h.startswith("# "):
            title = h[2:].strip()
            core = re.sub(r"\(.*?\)", "", title)   # "(mandatory)" is house style
            letters = [c for c in core if c.isalpha()]
            if letters and sum(c.isupper() for c in letters) / len(letters) < 0.6:
                warnings.append(f"line {ln}: heading '{title}' is not UPPERCASE house style")

    # --- empty sections ---------------------------------------------------
    bodies = section_bodies(text)
    for title, body in bodies.items():
        if not body.strip():
            errors.append(f"empty section: # {title} — never emit an empty heading")

    # --- placeholders -----------------------------------------------------
    for pat, label in PLACEHOLDERS:
        for m in re.finditer(pat, text, re.I):
            ln = text[:m.start()].count("\n") + 1
            errors.append(f"line {ln}: placeholder ({label}): {m.group(0).strip()!r}")

    stripped = strip_fences(text)
    for pat in (SLOT, BRACE_SLOT):
        for m in pat.finditer(stripped):
            ln = stripped[:m.start()].count("\n") + 1
            errors.append(f"line {ln}: unfilled slot {m.group(0)!r} — resolve it or ask for it")

    # --- routing invariants ----------------------------------------------
    routing = body_of(bodies, "MODEL ROUTING")
    # Rail identity is checked across the whole document: a rail leaking into WORKING
    # METHOD is just as wrong as two rails inside the routing section.
    a_bridge, b_bridge = bool(RAIL_A_BRIDGE.search(text)), bool(RAIL_B_BRIDGE.search(text))
    if a_bridge and b_bridge:
        errors.append("both bridges are named — exactly one rail may be emitted")
    elif not a_bridge and not b_bridge and FAMILY_A.search(text) and FAMILY_B.search(text):
        errors.append("models from both rails are named with no bridge between them — "
                      "the rail is ambiguous; emit one rail and reach the other side "
                      "through its bridge")
    if routing:
        if not FABLE_BAN.search(routing):
            errors.append("MODEL ROUTING is missing the Fable prohibition "
                          "(rules/09 §5 never-cut)")
        if not LATENCY_BAN.search(routing):
            errors.append("MODEL ROUTING is missing the paid-latency prohibition "
                          "(rules/09 §5 never-cut)")
    if re.search(r"\bfable\b", text, re.I) and not FABLE_BAN.search(text):
        errors.append("Fable is mentioned without the prohibition")

    # --- other never-cut invariants --------------------------------------
    setup = body_of(bodies, "SETUP")
    if setup and "english" not in setup.lower():
        errors.append("SETUP is missing the working-language instruction (work and report in English)")

    # The git end-state clause is mandatory unless SETUP itself declares there is no
    # repository. Scoped to SETUP on purpose: prose elsewhere ("no repository
    # restructuring") must not be able to switch the check off.
    no_repo = NO_REPO.search(setup)
    dod = body_of(bodies, "DEFINITION OF DONE")
    # Both halves must appear in the SAME clause. Matching them across separate bullets
    # lets "each redesign branch is covered by a golden test" plus an unrelated
    # "analyze clean" satisfy a check that neither line is.
    has_git_clause = any(GIT_LANDS.search(ln) and GIT_CLEANUP.search(ln)
                         for ln in dod.splitlines())
    if dod and not has_git_clause:
        if no_repo:
            warnings.append("DEFINITION OF DONE has no git clause; SETUP declares no repository, "
                            "so that is correct — confirm the declaration is deliberate")
        else:
            errors.append("DEFINITION OF DONE is missing the git end-state clause "
                          "(rules/08 §2, rules/09 §5 never-cut)")

    first = body_of(bodies, "FIRST ACTION")
    if first and not re.search(r"\.md\b|write|persist|record", first, re.I):
        warnings.append("FIRST ACTION does not clearly persist the brief to a durable file")

    if not EVIDENCE_RULE.search(text):
        errors.append("the evidence rule is absent — 'never report a result you have not "
                      "observed' (rules/09 §5 never-cut)")

    # --- report -----------------------------------------------------------
    for w in warnings:
        print(f"WARN   {w}")
    for e in errors:
        print(f"ERROR  {e}")

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
