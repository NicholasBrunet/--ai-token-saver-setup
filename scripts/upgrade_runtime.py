#!/usr/bin/env python3
from __future__ import annotations
import json, shutil
from datetime import datetime, timezone
from pathlib import Path

RUNTIME_DIR = "--ai-token-saver"
RUNTIME_SCHEMA_VERSION = "1"

PROJECT_MEMORY_FILES = {
    "project_brain.md", "project_systems.json", "context_routes.json",
    "known_patterns.md", "known_pitfalls.md", "editing_rules.md"
}

STALE_CONTEXT_SECTION = """
<!-- AI_TOKEN_SAVER_UPGRADE_STALE_CONTEXT_V0_2_0_START -->
## Stale Context Protection

Before trusting generated context files, verify that the context task and task hash match the current task.

If generated context references an older task:

1. Do not fall back to broad manual source reads.
2. Rerun the context generator for the current task.
3. Verify the new map/manifest task or task hash matches.
4. Only then inspect exact source files.

This prevents wasting tokens by rediscovering architecture when cached context is stale.
<!-- AI_TOKEN_SAVER_UPGRADE_STALE_CONTEXT_V0_2_0_END -->
""".strip()

def read_text(path: Path, default: str = "") -> str:
    try: return path.read_text(encoding="utf-8")
    except OSError: return default

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def read_json(path: Path) -> dict:
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return {}

def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def backup_file(path: Path, backup_root: Path) -> str | None:
    if not path.exists(): return None
    backup_root.mkdir(parents=True, exist_ok=True)
    target = backup_root / path.name
    shutil.copy2(path, target)
    return str(target)

def append_once(path: Path, section: str, marker: str) -> bool:
    text = read_text(path)
    if marker in text:
        return False
    if text and not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n" + section + "\n")
    return True

def main() -> None:
    setup_root = Path(__file__).resolve().parents[1]
    project_root = setup_root.parent
    runtime_root = project_root / RUNTIME_DIR
    setup_version = read_text(setup_root / "VERSION", "unknown").strip() or "unknown"

    print("AI Token Saver safe runtime upgrade")
    print("=" * 42)
    print(f"Project root: {project_root}")
    print(f"Setup root:   {setup_root}")
    print(f"Runtime root: {runtime_root}")
    print(f"Setup version: {setup_version}")
    print("")

    if not runtime_root.exists():
        print("Runtime folder is missing. Initialize first.")
        return

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    backup_root = runtime_root / "backups" / timestamp
    changed, backed_up = [], []

    for dirname in ["sessions", "reports", "context", "backups", "pyscripts"]:
        (runtime_root / dirname).mkdir(parents=True, exist_ok=True)

    runtime_version_path = runtime_root / "runtime_version.json"
    backup = backup_file(runtime_version_path, backup_root)
    if backup: backed_up.append(backup)

    data = read_json(runtime_version_path)
    data["setup_version"] = setup_version
    data["runtime_schema_version"] = data.get("runtime_schema_version", RUNTIME_SCHEMA_VERSION)
    data.setdefault("initialized_at", "")
    data["last_upgraded_at"] = datetime.now(timezone.utc).isoformat()
    notes = data.get("upgrade_notes", [])
    if not isinstance(notes, list): notes = []
    note = "Applied v0.2.0 stale context protection and runtime version metadata."
    if note not in notes: notes.append(note)
    data["upgrade_notes"] = notes
    write_json(runtime_version_path, data)
    changed.append(str(runtime_version_path.relative_to(runtime_root)))

    instructions_path = runtime_root / "generated_agent_instructions.md"
    backup = backup_file(instructions_path, backup_root)
    if backup: backed_up.append(backup)
    if append_once(instructions_path, STALE_CONTEXT_SECTION, "AI_TOKEN_SAVER_UPGRADE_STALE_CONTEXT_V0_2_0_START"):
        changed.append(str(instructions_path.relative_to(runtime_root)))

    report = []
    report.append("# AI Token Saver Runtime Upgrade Report\n")
    report.append(f"- Created at: `{datetime.now(timezone.utc).isoformat()}`")
    report.append(f"- Setup version: `{setup_version}`")
    report.append(f"- Runtime root: `{runtime_root}`")
    report.append(f"- Backup root: `{backup_root}`\n")
    report.append("## Changed Files\n")
    report.extend(f"- `{item}`" for item in changed)
    report.append("\n## Backups\n")
    report.extend(f"- `{item}`" for item in backed_up) if backed_up else report.append("- No backups needed.")
    report.append("\n## Preserved Project Memory Files\n")
    report.extend(f"- `{item}`" for item in sorted(PROJECT_MEMORY_FILES))
    report.append("\n## Full Reinitialization Recommendation\n")
    report.append("Full reinitialization is not automatically required for this upgrade.")
    report_path = runtime_root / "reports" / f"upgrade_report_{timestamp}.md"
    write_text(report_path, "\n".join(report))

    print("Upgrade complete.")
    print("Changed files:")
    for item in changed: print(f"  - {item}")
    print("")
    print(f"Report: {report_path}")

if __name__ == "__main__":
    main()
