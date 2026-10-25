#!/usr/bin/env python3
"""Vergleicht die Repos auf GitHub mit den Projekten in script.js.

Aufruf:  python3 scripts/check-repos.py
Braucht nur Python 3 und Internet (GitHub-API ohne Login, 60 Anfragen/Stunde).
"""
import json
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = "bonbon08"
ROOT = Path(__file__).resolve().parent.parent
RECENT_DAYS = 60

script = (ROOT / "script.js").read_text(encoding="utf-8")
categories = script[script.index("const CATEGORIES"):script.index("const SOCIALS")]
on_site = set(re.findall(r'name: "([^"]+)"', categories))

ignored = {
    line.strip()
    for line in (ROOT / "scripts" / "ignored-repos.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
}

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json"},
)
with urllib.request.urlopen(req) as res:
    repos = [r for r in json.load(res) if not r["fork"]]
names = {r["name"] for r in repos}

def line(r):
    desc = r["description"] or "(keine Beschreibung)"
    return f"  - {r['name']:<28} {r['language'] or '-':<8} {r['pushed_at'][:10]}  {desc}"

new = [r for r in repos if r["name"] not in on_site | ignored]
gone = sorted(on_site - names)
cutoff = datetime.now(timezone.utc) - timedelta(days=RECENT_DAYS)
recent = [r for r in repos if datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00")) > cutoff
          and r["name"] not in ignored]

print(f"NEUE Repos (noch nicht auf der Website, nicht ignoriert): {len(new)}")
print("\n".join(map(line, new)) or "  –")
print(f"\nAUF DER WEBSITE, aber nicht (mehr) auf GitHub – gelöscht, privat oder umbenannt? {len(gone)}")
print("\n".join(f"  - {n}" for n in gone) or "  –")
print(f"\nZULETZT AKTIV (letzte {RECENT_DAYS} Tage) – Kandidaten für 'Aktuell arbeite ich an':")
print("\n".join(map(line, recent)) or "  –")
