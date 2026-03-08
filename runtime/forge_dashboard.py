#!/usr/bin/env python3
from pathlib import Path
import html
import os
import subprocess
from datetime import datetime, timezone

HOME = Path.home()
ATLAS_ENV_FILE = HOME / "atlas.env"
HEADER_FILE = HOME / ".neuro_forge_header"
WATCHER_FILE = HOME / "forge_watcher.py"
OUTPUT_DIR = HOME / "public_html" / "big-brother"
OUTPUT_FILE = OUTPUT_DIR / "index.html"

def load_env_file(path: Path):
    env = {}
    if not path.exists():
        return env
    for line in path.read_text(errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"')
    return env

def run_watcher():
    if not WATCHER_FILE.exists():
        return {
            "raw": "forge_watcher.py not found",
            "watcher": "GRAY",
            "message": "forge_watcher.py not found",
            "library": "Unknown",
            "workbench": "Unknown",
            "mms": "Unknown",
            "bridge": "Unknown",
        }

    try:
        result = subprocess.run(
            ["python3", str(WATCHER_FILE)],
            capture_output=True,
            text=True,
            timeout=15,
        )
        raw = (result.stdout or result.stderr).strip()
    except Exception as exc:
        raw = f"Watcher execution failed: {exc}"

    parsed = {
        "raw": raw,
        "watcher": "GRAY",
        "message": "Unknown state",
        "library": "Unknown",
        "workbench": "Unknown",
        "mms": "Unknown",
        "bridge": "Unknown",
    }

    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith("WATCHER :"):
            parsed["watcher"] = stripped.split()[-1]
        elif stripped.startswith("Message :"):
            parsed["message"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Library :"):
            parsed["library"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Workbench:"):
            parsed["workbench"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("MMS     :"):
            parsed["mms"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Bridge  :"):
            parsed["bridge"] = stripped.split(":", 1)[1].strip()

    return parsed

def watcher_color(state: str):
    return {
        "NEXUS": "#111111",
        "GENESIS": "#f5f5f5",
        "BLUE": "#3b82f6",
        "YELLOW": "#facc15",
        "ORANGE": "#fb923c",
        "GREEN": "#22c55e",
        "PURPLE": "#a855f7",
        "RED": "#ef4444",
        "GRAY": "#9ca3af",
    }.get(state, "#9ca3af")

def badge_text_color(state: str):
    return "#111111" if state in {"YELLOW", "GENESIS"} else "#ffffff"

def main():
    atlas = load_env_file(ATLAS_ENV_FILE)
    watcher = run_watcher()

    author = atlas.get("ATLAS_AUTHOR", "J.K. Marchand")
    role = atlas.get("ATLAS_ROLE", "Cryptographic Publisher")
    status = atlas.get("ATLAS_STATUS", "Developer • Graphic Designer")
    authority = atlas.get("ATLAS_AUTHORITY", "© Design Orchard LLC")
    runtime = atlas.get("ATLAS_RUNTIME", "🔬 DrMarchand’s Lab⚛︎ratory™")
    archive = atlas.get("ATLAS_ARCHIVE", "📚 DrMarchand’s ⚛︎ Library™")
    workbench = atlas.get("ATLAS_WORKBENCH", "🪑 DrMarchand’s ⚛︎ Workbench™")
    bridge_name = atlas.get("ATLAS_BRIDGE", "☁ Cloud Bridge")

    library_path = atlas.get("ATLAS_LIBRARY_PATH", "/Volumes/LAB_8TB/LIB_2TB")
    workbench_path = atlas.get("ATLAS_WORKBENCH_PATH", "/Volumes/LAB_8TB/WORKBENCH")
    remote_host = atlas.get("ATLAS_VAULT_HOST_REMOTE", "69.137.2.215")

    icloud_root = atlas.get("ATLAS_ICLOUD_ROOT", "$HOME/iCloudDrive")
    gdrive_root = atlas.get("ATLAS_GDRIVE_ROOT", "$HOME/GoogleDrive")
    onedrive_root = atlas.get("ATLAS_ONEDRIVE_ROOT", "$HOME/OneDrive")
    dropbox_root = atlas.get("ATLAS_DROPBOX_ROOT", "$HOME/Dropbox")

    notice = atlas.get("ATLAS_NOTICE", "Independent professional framework.")
    safety_1 = atlas.get("ATLAS_SAFETY_1", "Self-taught. Not a doctor.")
    safety_2 = atlas.get("ATLAS_SAFETY_2", "Not an architect. Not licensed.")

    state = watcher["watcher"]
    state_bg = watcher_color(state)
    state_fg = badge_text_color(state)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Big Brother Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {{
      --bg: #0b1020;
      --panel: #141b34;
      --panel-2: #10172c;
      --text: #e8edf8;
      --muted: #aab4d0;
      --line: #26304f;
      --accent: {state_bg};
      --accentText: {state_fg};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .wrap {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px;
    }}
    .hero, .panel {{
      background: linear-gradient(180deg, var(--panel), var(--panel-2));
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 20px;
      margin-bottom: 18px;
    }}
    .hero h1 {{
      margin: 0 0 10px 0;
      font-size: 28px;
    }}
    .sub {{
      color: var(--muted);
      margin: 0 0 14px 0;
    }}
    .badge {{
      display: inline-block;
      background: var(--accent);
      color: var(--accentText);
      padding: 8px 12px;
      border-radius: 999px;
      font-weight: 700;
      margin-top: 6px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 18px;
    }}
    .k {{
      color: var(--muted);
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: .06em;
      margin-bottom: 6px;
    }}
    .v {{
      font-size: 18px;
      font-weight: 600;
      word-break: break-word;
    }}
    .mono {{
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 13px;
      white-space: pre-wrap;
      color: var(--muted);
    }}
    .list {{
      margin: 0;
      padding-left: 18px;
      color: var(--muted);
    }}
    .footer {{
      color: var(--muted);
      font-size: 13px;
      text-align: center;
      margin-top: 20px;
    }}
    a {{ color: #93c5fd; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <h1>⚙︎ Nɛuro-Forge Engine™ :: Big Brother Dashboard</h1>
      <p class="sub">{html.escape(author)} • {html.escape(role)} • {html.escape(status)}</p>
      <div class="badge">WATCHDOG {html.escape(state)}</div>
    </div>

    <div class="grid">
      <div class="panel">
        <div class="k">Authority</div>
        <div class="v">{html.escape(authority)}</div>
      </div>
      <div class="panel">
        <div class="k">Runtime</div>
        <div class="v">{html.escape(runtime)}</div>
      </div>
      <div class="panel">
        <div class="k">Archive</div>
        <div class="v">{html.escape(archive)}</div>
      </div>
      <div class="panel">
        <div class="k">Workbench</div>
        <div class="v">{html.escape(workbench)}</div>
      </div>
    </div>

    <div class="grid">
      <div class="panel">
        <div class="k">Watcher Message</div>
        <div class="v">{html.escape(watcher["message"])}</div>
      </div>
      <div class="panel">
        <div class="k">Library</div>
        <div class="v">{html.escape(watcher["library"])}</div>
      </div>
      <div class="panel">
        <div class="k">Workbench</div>
        <div class="v">{html.escape(watcher["workbench"])}</div>
      </div>
      <div class="panel">
        <div class="k">Bridge</div>
        <div class="v">{html.escape(watcher["bridge"])}</div>
      </div>
    </div>

    <div class="grid">
      <div class="panel">
        <div class="k">Reserve Path</div>
        <div class="v mono">{html.escape(library_path)}</div>
      </div>
      <div class="panel">
        <div class="k">Workbench Path</div>
        <div class="v mono">{html.escape(workbench_path)}</div>
      </div>
      <div class="panel">
        <div class="k">Remote Vault Host</div>
        <div class="v mono">{html.escape(remote_host)}</div>
      </div>
      <div class="panel">
        <div class="k">MMS</div>
        <div class="v">{html.escape(watcher["mms"])}</div>
      </div>
    </div>

    <div class="panel">
      <div class="k">{html.escape(bridge_name)}</div>
      <ul class="list">
        <li>iCloud Drive → {html.escape(icloud_root)}</li>
        <li>Google Drive → {html.escape(gdrive_root)}</li>
        <li>OneDrive → {html.escape(onedrive_root)}</li>
        <li>Dropbox → {html.escape(dropbox_root)}</li>
      </ul>
    </div>

    <div class="panel">
      <div class="k">Notice</div>
      <div class="v">{html.escape(notice)}</div>
      <div class="k" style="margin-top:14px;">Safety</div>
      <div class="v">{html.escape(safety_1)} {html.escape(safety_2)}</div>
    </div>

    <div class="panel">
      <div class="k">Raw Watcher Output</div>
      <div class="mono">{html.escape(watcher["raw"])}</div>
    </div>

    <div class="footer">
      Generated {html.escape(generated)} • Big Brother Observer Dashboard
    </div>
  </div>
</body>
</html>
"""
    OUTPUT_FILE.write_text(html_doc, encoding="utf-8")
    print(f"Dashboard written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
