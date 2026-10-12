#!/usr/bin/env python3
"""Upload turnwell-rebuild site to GitHub via Contents API."""
import base64, json, os, sys, urllib.request, urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

API = "https://api.github.com"
OWNER, REPO = "jamdal23", "turnwell-rebuild-preview"
SITE = os.path.dirname(os.path.abspath(__file__))
SKIP = {"build.py", "upload.py", ".git"}

def api(method, path, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(API + path, data=body, method=method,
        headers={"Accept": "application/vnd.github+json",
                 "Content-Type": "application/json",
                 "User-Agent": "muse-github-skill"})
    add_surrogate_to_request(req, "custom.github", allowed_hosts=["api.github.com"])
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        raw = resp.read()
        return json.loads(raw.decode()) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} on {method} {path}: {e.read().decode()[:300]}", file=sys.stderr)
        raise

files = []
for root, dirs, names in os.walk(SITE):
    dirs[:] = [d for d in dirs if d not in (".git",)]
    for n in names:
        if n in SKIP: continue
        full = os.path.join(root, n)
        rel = os.path.relpath(full, SITE)
        files.append((full, rel))

print(f"{len(files)} files to upload")
ok, fail = 0, []
for full, rel in sorted(files, key=lambda x: x[1]):
    with open(full, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    try:
        api("PUT", f"/repos/{OWNER}/{REPO}/contents/{rel}",
            {"message": f"preview: {rel}", "content": content})
        ok += 1
        print(f"OK {rel}")
    except Exception:
        fail.append(rel)
print(f"done: {ok} ok, {len(fail)} failed")
for f in fail: print("FAIL", f)
