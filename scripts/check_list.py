"""Lint the list and check that every link resolves.

    python scripts/check_list.py            # format + links
    python scripts/check_list.py --offline  # format only

GitHub repositories are checked with `git ls-remote` (no API rate limits); other
links with an HTTP request.
"""
from __future__ import annotations

import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
ENTRY = re.compile(r"^- \[[^\]]+\]\((https?://[^)]+)\) - [A-Z0-9τ\"].+[.)]$")
LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
GITHUB_REPO = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)/?$")


def lint(text: str) -> list[str]:
    errs = []
    in_code = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("- [") and "](http" in line and not ENTRY.match(line):
            errs.append(f"line {i}: entries must look like '- [Name](url) - Why it matters.'")
    sections = re.split(r"^## ", text, flags=re.M)[1:]
    for s in sections:
        title, body = s.split("\n", 1)
        if not body.strip():
            errs.append(f"section '{title}' is empty")
        urls = [u for u in LINK.findall(body) if "AfnanAhmd004" not in u]
        dupes = {u for u in urls if urls.count(u) > 1}
        if dupes:
            errs.append(f"section '{title}' lists the same link twice: {sorted(dupes)}")
    toc = re.findall(r"\(#([a-z0-9-]+)\)", text)
    anchors = {re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-") for h in re.findall(r"^## (.+)$", text, flags=re.M)}
    errs += [f"table of contents points to missing section #{a}" for a in toc if a not in anchors]
    return errs


def check(url: str) -> tuple[str, bool]:
    m = GITHUB_REPO.match(url)
    if m:
        r = subprocess.run(["git", "ls-remote", f"https://github.com/{m[1]}/{m[2]}", "HEAD"],
                           capture_output=True, timeout=60, env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin"})
        return url, r.returncode == 0
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link-check)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return url, resp.status < 400
    except Exception:
        return url, False


def main(argv: list[str]) -> int:
    text = README.read_text()
    errs = lint(text)
    for e in errs:
        print("✗", e)
    if "--offline" not in argv:
        urls = sorted(set(LINK.findall(text)))
        with ThreadPoolExecutor(8) as pool:
            for url, ok in pool.map(check, urls):
                if not ok:
                    errs.append(url)
                    print("✗ broken link:", url)
        print(f"checked {len(urls)} links")
    print("ok" if not errs else f"{len(errs)} problem(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
