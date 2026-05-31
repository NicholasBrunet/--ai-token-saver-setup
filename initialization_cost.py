#!/usr/bin/env python3
"""
initialization_cost.py

Estimate the token cost of setting up AI Token Saver in a target project.

Intended location:
    --ai-token-saver-setup/initialization_cost.py

Typical usage from the parent project root:
    python --ai-token-saver-setup/initialization_cost.py

Typical usage from inside --ai-token-saver-setup:
    python initialization_cost.py

What it estimates:
    1. Parent project initialization cost
    2. Setup folder reading cost
    3. Combined one-time setup cost

The parent project root is detected automatically as the parent directory of
--ai-token-saver-setup, unless --project-root is provided.

This script is only an estimator. It is not exact billing data.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable


# ============================================================
# Defaults
# ============================================================

SETUP_DIR_NAME = "--ai-token-saver-setup"
RUNTIME_DIR_NAME = "--ai-token-saver"

DEFAULT_MODEL = "gpt-5.3-codex"
DEFAULT_MAX_FILE_SIZE_KB = 768
DEFAULT_TOP_FILES = 30

SAFE_TOKENS = 25_000
MODERATE_TOKENS = 60_000
EXPENSIVE_TOKENS = 100_000


# ============================================================
# Exclusions
# ============================================================

EXCLUDED_DIR_NAMES: set[str] = {
    ".git",
    ".idea",
    ".vscode",
    ".gradle",
    ".mvn",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".tox",
    "node_modules",
    "build",
    "target",
    "dist",
    "out",
    "logs",
    "log",
    "tmp",
    "temp",
    ".next",
    ".nuxt",
    ".turbo",
    ".cache",
    "coverage",
    ".coverage",
    ".VSCodeCounter",
    RUNTIME_DIR_NAME,
}

# Project-specific/common runtime paths that are expensive and rarely useful
# for initial source-code architecture discovery.
EXCLUDED_PATH_PREFIXES: tuple[str, ...] = (
    "dev-server/world/",
    "dev-server/world_nether/",
    "dev-server/world_the_end/",
    "dev-server/libraries/",
    "dev-server/versions/",
    "dev-server/cache/",
    "dev-server/plugins/.paper-remapped/",
    "dev-server/plugins/FastAsyncWorldEdit/",
    "dev-server/plugins/Multiverse-Core/",
    "dev-server/plugins/ViaVersion/",
    "dev-server/plugins/ProtocolLib/",
    "dev-server/plugins/SkBee/",
    "dev-server/plugins/spark/",
    "dev-server/plugins/bStats/",
    "dev-server/crash-reports/",
)

BINARY_EXTENSIONS: set[str] = {
    ".jar",
    ".zip",
    ".gz",
    ".tar",
    ".rar",
    ".7z",
    ".class",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".mca",
    ".dat",
    ".dat_old",
    ".db",
    ".sqlite",
    ".lock",
    ".pdf",
    ".mp3",
    ".mp4",
    ".mov",
    ".avi",
    ".wav",
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
}

TEXT_EXTENSIONS: set[str] = {
    ".java",
    ".kt",
    ".kts",
    ".gradle",
    ".gradle.kts",
    ".groovy",
    ".sk",
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".scss",
    ".sass",
    ".vue",
    ".svelte",
    ".json",
    ".jsonl",
    ".yml",
    ".yaml",
    ".toml",
    ".ini",
    ".cfg",
    ".properties",
    ".xml",
    ".sql",
    ".md",
    ".txt",
    ".rst",
    ".csv",
    ".sh",
    ".bash",
    ".bat",
    ".ps1",
    ".dockerfile",
    ".gitignore",
    ".gitattributes",
}

IMPORTANT_FILENAMES: set[str] = {
    "README",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    ".gitignore",
    ".gitattributes",
    "Dockerfile",
    "Makefile",
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "settings.gradle",
    "settings.gradle.kts",
    "gradle.properties",
    "plugin.yml",
    "config.yml",
    "pyproject.toml",
    "requirements.txt",
}


# ============================================================
# Data
# ============================================================

@dataclass(frozen=True)
class FileCost:
    relative_path: str
    group: str
    size_bytes: int
    line_count: int
    tokens: int


@dataclass(frozen=True)
class GroupCost:
    group: str
    root: str
    files: int
    bytes: int
    lines: int
    tokens: int


@dataclass(frozen=True)
class CostReport:
    created_at: str
    project_root: str
    setup_root: str
    tokenizer: str
    estimate_mode: str
    max_file_size_kb: int
    project: GroupCost
    setup: GroupCost
    combined_tokens: int
    combined_files: int
    combined_bytes: int
    combined_lines: int
    risk_level: str
    top_files: list[FileCost]
    skipped_files: list[str]
    notes: list[str]


# ============================================================
# Token counting
# ============================================================

def load_token_counter(model: str) -> tuple[str, str, Callable[[str], int]]:
    try:
        import tiktoken  # type: ignore

        try:
            encoding = tiktoken.encoding_for_model(model)
            tokenizer = f"encoding_for_model:{model}"
        except KeyError:
            encoding = tiktoken.get_encoding("o200k_base")
            tokenizer = "fallback:o200k_base"

        def count_tokens(text: str) -> int:
            return len(encoding.encode(text))

        return tokenizer, "tiktoken", count_tokens

    except ImportError:
        def rough_count(text: str) -> int:
            return max(1, int(len(text) / 4))

        return "rough:characters_divided_by_4", "rough", rough_count


# ============================================================
# Helpers
# ============================================================

def to_posix(path: Path) -> str:
    return path.as_posix()


def count_lines(text: str) -> int:
    if not text:
        return 0
    return text.count("\n") + 1


def risk_for_tokens(tokens: int) -> str:
    if tokens <= SAFE_TOKENS:
        return "safe"
    if tokens <= MODERATE_TOKENS:
        return "moderate"
    if tokens <= EXPENSIVE_TOKENS:
        return "expensive"
    return "dangerous"


def format_int(value: int) -> str:
    return f"{value:,}"


def format_bytes(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    kb = size_bytes / 1024
    if kb < 1024:
        return f"{kb:.1f} KB"
    return f"{kb / 1024:.2f} MB"


def normalize_extension(path: Path) -> str:
    name = path.name

    if name in {".gitignore", ".gitattributes"}:
        return name

    if name == "Dockerfile":
        return ".dockerfile"

    if name.endswith(".gradle.kts"):
        return ".gradle.kts"

    return path.suffix.lower()


def is_probably_text_file(path: Path) -> bool:
    extension = normalize_extension(path)

    if extension in BINARY_EXTENSIONS:
        return False

    if extension in TEXT_EXTENSIONS:
        return True

    if path.name in IMPORTANT_FILENAMES:
        return True

    return False


def is_binary_by_sample(path: Path, sample_size: int = 4096) -> bool:
    try:
        with path.open("rb") as file:
            sample = file.read(sample_size)
        return b"\0" in sample
    except OSError:
        return True


def should_ignore_dir(dirname: str, include_hidden: bool) -> bool:
    if dirname in EXCLUDED_DIR_NAMES:
        return True

    if dirname.startswith("-") and dirname not in {SETUP_DIR_NAME, RUNTIME_DIR_NAME}:
        return True

    if not include_hidden and dirname.startswith("."):
        return True

    return False


def starts_with_any(path_text: str, prefixes: Iterable[str]) -> bool:
    clean_path = path_text.replace("\\", "/")
    for prefix in prefixes:
        clean_prefix = prefix.replace("\\", "/")
        if clean_path.startswith(clean_prefix):
            return True
    return False


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def resolve_roots(project_root_arg: str | None, setup_dir_arg: str) -> tuple[Path, Path]:
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent

    if script_dir.name == SETUP_DIR_NAME:
        detected_setup_root = script_dir
        detected_project_root = script_dir.parent
    else:
        # This also supports running a copied script from the parent project root.
        cwd = Path.cwd().resolve()
        possible_setup = cwd / setup_dir_arg
        if possible_setup.exists() and possible_setup.is_dir():
            detected_setup_root = possible_setup
            detected_project_root = cwd
        else:
            detected_setup_root = script_dir
            detected_project_root = cwd

    project_root = Path(project_root_arg).resolve() if project_root_arg else detected_project_root
    setup_root = (project_root / setup_dir_arg).resolve()

    if not setup_root.exists() or not setup_root.is_dir():
        # Fallback to script dir when the script itself is inside setup.
        if detected_setup_root.exists() and detected_setup_root.is_dir():
            setup_root = detected_setup_root

    return project_root, setup_root


def should_skip_path(
    root: Path,
    path: Path,
    setup_root: Path,
    include_setup_in_project_scan: bool,
) -> str | None:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return "outside root"

    relative_text = to_posix(relative)

    if path.is_dir():
        return None

    # Avoid double-counting the setup folder as part of the parent project scan.
    if not include_setup_in_project_scan:
        try:
            path.relative_to(setup_root)
            return "setup folder counted separately"
        except ValueError:
            pass

    if starts_with_any(relative_text, EXCLUDED_PATH_PREFIXES):
        return "excluded runtime/generated path"

    if not is_probably_text_file(path):
        return "binary or unsupported extension"

    return None


# ============================================================
# Collection
# ============================================================

def collect_group_costs(
    *,
    root: Path,
    group: str,
    setup_root: Path,
    include_setup_in_project_scan: bool,
    include_hidden: bool,
    max_file_size_kb: int,
    count_tokens: Callable[[str], int],
) -> tuple[list[FileCost], list[str]]:
    root = root.resolve()
    files: list[FileCost] = []
    skipped: list[str] = []

    if not root.exists() or not root.is_dir():
        skipped.append(f"{group}: root does not exist: {root}")
        return files, skipped

    for current_root, dirnames, filenames in os.walk(root):
        current_path = Path(current_root)

        kept_dirs: list[str] = []
        for dirname in sorted(dirnames):
            full_dir = current_path / dirname

            if should_ignore_dir(dirname, include_hidden):
                continue

            if not include_setup_in_project_scan:
                try:
                    full_dir.resolve().relative_to(setup_root)
                    continue
                except ValueError:
                    pass

            try:
                rel_dir = full_dir.resolve().relative_to(root)
                if starts_with_any(to_posix(rel_dir) + "/", EXCLUDED_PATH_PREFIXES):
                    continue
            except ValueError:
                pass

            kept_dirs.append(dirname)

        dirnames[:] = kept_dirs

        for filename in sorted(filenames):
            path = (current_path / filename).resolve()

            skip_reason = should_skip_path(
                root=root,
                path=path,
                setup_root=setup_root,
                include_setup_in_project_scan=include_setup_in_project_scan,
            )
            if skip_reason:
                try:
                    rel = to_posix(path.relative_to(root))
                except ValueError:
                    rel = str(path)
                skipped.append(f"{group}: {rel} skipped: {skip_reason}")
                continue

            try:
                size_bytes = path.stat().st_size
            except OSError:
                skipped.append(f"{group}: {path} skipped: stat failed")
                continue

            if size_bytes > max_file_size_kb * 1024:
                try:
                    rel = to_posix(path.relative_to(root))
                except ValueError:
                    rel = str(path)
                skipped.append(
                    f"{group}: {rel} skipped: above max file size {max_file_size_kb} KB"
                )
                continue

            if is_binary_by_sample(path):
                try:
                    rel = to_posix(path.relative_to(root))
                except ValueError:
                    rel = str(path)
                skipped.append(f"{group}: {rel} skipped: binary sample")
                continue

            try:
                text = read_text(path)
            except OSError:
                skipped.append(f"{group}: {path} skipped: read failed")
                continue

            try:
                relative_text = to_posix(path.relative_to(root))
            except ValueError:
                relative_text = str(path)

            tokens = count_tokens(text)
            files.append(
                FileCost(
                    relative_path=relative_text,
                    group=group,
                    size_bytes=size_bytes,
                    line_count=count_lines(text),
                    tokens=tokens,
                )
            )

    files.sort(key=lambda item: (-item.tokens, item.relative_path))
    return files, skipped


def summarize_group(group: str, root: Path, files: list[FileCost]) -> GroupCost:
    return GroupCost(
        group=group,
        root=str(root),
        files=len(files),
        bytes=sum(item.size_bytes for item in files),
        lines=sum(item.line_count for item in files),
        tokens=sum(item.tokens for item in files),
    )


# ============================================================
# Output
# ============================================================

def render_report(report: CostReport) -> str:
    lines: list[str] = []

    lines.append("# AI Token Saver Initialization Cost Estimate")
    lines.append("")
    lines.append(f"- Created at: `{report.created_at}`")
    lines.append(f"- Project root: `{report.project_root}`")
    lines.append(f"- Setup root: `{report.setup_root}`")
    lines.append(f"- Tokenizer: `{report.tokenizer}`")
    lines.append(f"- Estimate mode: `{report.estimate_mode}`")
    lines.append(f"- Max file size: `{report.max_file_size_kb} KB`")
    lines.append(f"- Risk level: `{report.risk_level}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Group | Files | Size | Lines | Tokens |")
    lines.append("|---|---:|---:|---:|---:|")
    lines.append(
        f"| Parent project | {format_int(report.project.files)} | {format_bytes(report.project.bytes)} | "
        f"{format_int(report.project.lines)} | {format_int(report.project.tokens)} |"
    )
    lines.append(
        f"| Setup folder | {format_int(report.setup.files)} | {format_bytes(report.setup.bytes)} | "
        f"{format_int(report.setup.lines)} | {format_int(report.setup.tokens)} |"
    )
    lines.append(
        f"| Combined | {format_int(report.combined_files)} | {format_bytes(report.combined_bytes)} | "
        f"{format_int(report.combined_lines)} | {format_int(report.combined_tokens)} |"
    )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "This estimates the one-time cost for an AI agent to read the setup system and enough "
        "of the parent project to build a project-specific `--ai-token-saver/` runtime."
    )
    lines.append("")
    lines.append("Risk thresholds:")
    lines.append("")
    lines.append("- safe: <= 25,000 tokens")
    lines.append("- moderate: <= 60,000 tokens")
    lines.append("- expensive: <= 100,000 tokens")
    lines.append("- dangerous: > 100,000 tokens")
    lines.append("")
    lines.append("## Largest Counted Files")
    lines.append("")
    lines.append("| Group | Tokens | Size | Lines | Path |")
    lines.append("|---|---:|---:|---:|---|")

    for file in report.top_files:
        lines.append(
            f"| {file.group} | {format_int(file.tokens)} | {format_bytes(file.size_bytes)} | "
            f"{format_int(file.line_count)} | `{file.relative_path}` |"
        )

    if report.notes:
        lines.append("")
        lines.append("## Notes")
        lines.append("")
        for note in report.notes:
            lines.append(f"- {note}")

    if report.skipped_files:
        lines.append("")
        lines.append("## Skipped Files")
        lines.append("")
        for skipped in report.skipped_files[:300]:
            lines.append(f"- {skipped}")

        if len(report.skipped_files) > 300:
            lines.append(f"- ... {len(report.skipped_files) - 300} more skipped entries omitted")

    lines.append("")
    return "\n".join(lines)


def print_console_report(report: CostReport) -> None:
    print("AI Token Saver initialization cost estimate")
    print("=" * 48)
    print(f"Project root: {report.project_root}")
    print(f"Setup root:   {report.setup_root}")
    print(f"Tokenizer:    {report.tokenizer}")
    print(f"Mode:         {report.estimate_mode}")
    print(f"Risk level:   {report.risk_level}")
    print("")
    print("Summary:")
    print(
        f"  Parent project: {format_int(report.project.tokens)} tokens "
        f"({format_int(report.project.files)} files, {format_bytes(report.project.bytes)})"
    )
    print(
        f"  Setup folder:   {format_int(report.setup.tokens)} tokens "
        f"({format_int(report.setup.files)} files, {format_bytes(report.setup.bytes)})"
    )
    print(
        f"  Combined:       {format_int(report.combined_tokens)} tokens "
        f"({format_int(report.combined_files)} files, {format_bytes(report.combined_bytes)})"
    )
    print("")
    print("Largest counted files:")
    for file in report.top_files[:10]:
        print(
            f"  {format_int(file.tokens):>8} tokens  "
            f"{file.group:<14}  {file.relative_path}"
        )

    if report.notes:
        print("")
        print("Notes:")
        for note in report.notes:
            print(f"  - {note}")


# ============================================================
# CLI
# ============================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate AI Token Saver one-time initialization token cost."
    )

    parser.add_argument(
        "--project-root",
        default=None,
        help="Parent project root. Defaults to parent directory of --ai-token-saver-setup.",
    )
    parser.add_argument(
        "--setup-dir",
        default=SETUP_DIR_NAME,
        help=f"Setup directory name/path relative to project root. Defaults to {SETUP_DIR_NAME}.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Tokenizer model name. Defaults to {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--max-file-size-kb",
        type=int,
        default=DEFAULT_MAX_FILE_SIZE_KB,
        help=f"Skip individual files above this size. Defaults to {DEFAULT_MAX_FILE_SIZE_KB}.",
    )
    parser.add_argument(
        "--top-files",
        type=int,
        default=DEFAULT_TOP_FILES,
        help=f"Number of largest files to show. Defaults to {DEFAULT_TOP_FILES}.",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden directories except hard-excluded names.",
    )
    parser.add_argument(
        "--include-setup-in-project-scan",
        action="store_true",
        help="Count setup folder inside project scan too. Usually false to avoid double-counting.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON report instead of human-readable console output.",
    )
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="Write markdown and JSON reports into --ai-token-saver-setup/reports/.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    project_root, setup_root = resolve_roots(args.project_root, args.setup_dir)

    tokenizer, estimate_mode, count_tokens = load_token_counter(args.model)

    project_files, project_skipped = collect_group_costs(
        root=project_root,
        group="project",
        setup_root=setup_root,
        include_setup_in_project_scan=args.include_setup_in_project_scan,
        include_hidden=args.include_hidden,
        max_file_size_kb=args.max_file_size_kb,
        count_tokens=count_tokens,
    )

    setup_files, setup_skipped = collect_group_costs(
        root=setup_root,
        group="setup",
        setup_root=setup_root,
        include_setup_in_project_scan=True,
        include_hidden=args.include_hidden,
        max_file_size_kb=args.max_file_size_kb,
        count_tokens=count_tokens,
    )

    project_summary = summarize_group("project", project_root, project_files)
    setup_summary = summarize_group("setup", setup_root, setup_files)

    combined_tokens = project_summary.tokens + setup_summary.tokens
    combined_files = project_summary.files + setup_summary.files
    combined_bytes = project_summary.bytes + setup_summary.bytes
    combined_lines = project_summary.lines + setup_summary.lines

    all_files = sorted(project_files + setup_files, key=lambda item: (-item.tokens, item.group, item.relative_path))
    top_files = all_files[: max(0, args.top_files)]

    notes: list[str] = []

    if estimate_mode == "rough":
        notes.append("tiktoken is not installed; token counts use a rough characters/4 estimate.")

    if not setup_root.exists():
        notes.append("Setup directory was not found. Setup folder cost may be incomplete.")

    notes.append("The setup folder is counted separately from the parent project to avoid double-counting.")
    notes.append("Runtime/generated/dependency folders are excluded by default.")

    report = CostReport(
        created_at=datetime.now(timezone.utc).isoformat(),
        project_root=str(project_root),
        setup_root=str(setup_root),
        tokenizer=tokenizer,
        estimate_mode=estimate_mode,
        max_file_size_kb=args.max_file_size_kb,
        project=project_summary,
        setup=setup_summary,
        combined_tokens=combined_tokens,
        combined_files=combined_files,
        combined_bytes=combined_bytes,
        combined_lines=combined_lines,
        risk_level=risk_for_tokens(combined_tokens),
        top_files=top_files,
        skipped_files=project_skipped + setup_skipped,
        notes=notes,
    )

    if args.write_report:
        report_dir = setup_root / "reports"
        report_dir.mkdir(parents=True, exist_ok=True)

        json_path = report_dir / "initialization_cost.json"
        md_path = report_dir / "initialization_cost.md"

        json_path.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
        md_path.write_text(render_report(report), encoding="utf-8")

        notes.append(f"Wrote JSON report: {json_path}")
        notes.append(f"Wrote Markdown report: {md_path}")

    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print_console_report(report)


if __name__ == "__main__":
    main()
