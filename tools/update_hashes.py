#!/usr/bin/env python3
"""Adds/refreshes skin_sha256 + cape_sha256 in presets/index.json (run before every commit)."""
import hashlib, json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent / "presets"
idx = root / "index.json"
data = json.loads(idx.read_text(encoding="utf-8"))
ids = set()
for e in data["presets"]:
    if not re.fullmatch(r"[a-z0-9_\-]{1,64}", e["id"]):
        sys.exit(f"bad id (use a-z 0-9 _ - only): {e['id']}")
    if e["id"] in ids:
        sys.exit(f"duplicate id: {e['id']}")
    ids.add(e["id"])
    for kind in ("skin", "cape"):
        rel = e.get(kind)
        if not rel:
            continue
        if not re.fullmatch(r"[A-Za-z0-9_\-]+(/[A-Za-z0-9_\-]+)*\.png", rel):
            sys.exit(f"bad path for {e['id']}: {rel}")
        f = root / rel
        if not f.is_file():
            sys.exit(f"missing file: {f}")
        e[kind + "_sha256"] = hashlib.sha256(f.read_bytes()).hexdigest()
idx.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print(f"OK: {len(ids)} presets")
