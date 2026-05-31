#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

RUNTIME_DIR = "--ai-token-saver"
SETUP_DIR = "--ai-token-saver-setup"

def read_text(path: Path, default: str = "") -> str:
    try: return path.read_text(encoding="utf-8").strip()
    except OSError: return default

def read_json(path: Path) -> dict:
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return {}

def main() -> None:
    setup_root = Path(__file__).resolve().parents[1]
    project_root = setup_root.parent
    runtime_root = project_root / RUNTIME_DIR
    setup_version = read_text(setup_root / "VERSION", "unknown")
    runtime_data = read_json(runtime_root / "runtime_version.json")
    runtime_setup_version = runtime_data.get("setup_version", "missing")
    runtime_schema_version = runtime_data.get("runtime_schema_version", "missing")

    print("AI Token Saver setup/runtime version check")
    print("=" * 48)
    print(f"Project root: {project_root}")
    print(f"Setup root:   {setup_root}")
    print(f"Runtime root: {runtime_root}")
    print(f"Setup repo version:     {setup_version}")
    print(f"Runtime setup version:  {runtime_setup_version}")
    print(f"Runtime schema version: {runtime_schema_version}")
    print("")

    if not runtime_root.exists():
        print("Status: runtime folder missing.")
        print('Action: ask the AI agent: "Look through --ai-token-saver-setup and set it up for this repository."')
    elif runtime_setup_version != setup_version:
        print("Status: setup/runtime versions differ or runtime metadata is missing.")
        print(f"Action: python {SETUP_DIR}/scripts/upgrade_runtime.py")
    else:
        print("Status: runtime version matches setup version.")
        print("Action: no upgrade required.")

if __name__ == "__main__":
    main()
