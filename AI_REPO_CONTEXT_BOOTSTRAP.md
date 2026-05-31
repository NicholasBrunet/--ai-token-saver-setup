# AI Repo Context Bootstrap Specification

## 0. Purpose

You are an AI coding agent operating inside a repository that contains a setup folder named:

```text
--ai-token-saver-setup/
```

Your task is to create a repository-specific AI context and token optimization runtime folder named:

```text
--ai-token-saver/
```

This is a one-time expensive initialization pass. Spend the tokens needed to understand the repository well enough to build durable project-specific tooling.

The generated runtime must let future AI agents work like this:

```text
casual user prompt
→ project-aware technical task string
→ preflight token/context estimate
→ route-based focused context generation
→ targeted file inspection
→ small complete edits
→ validation
→ token efficiency report
→ optional project memory update
```

This file is an operating contract. Do not merely summarize it. Build the system.

---

## 1. The Big Idea

Normal AI coding workflow often fails because the agent starts by broadly searching or reading the repository. That wastes tokens and causes weak, unrelated, or partial edits.

This bootstrap inverts that workflow:

1. Spend tokens once to understand the repo.
2. Generate a project-specific brain and routing system.
3. Generate scripts to create focused context for each future task.
4. Generate permanent future-agent instructions.
5. Measure whether the system saved tokens.
6. Update memory when mistakes reveal reusable lessons.

The generated system is not model fine-tuning. It is repo-specific operational memory and tooling.

---

## 2. Non-Negotiable Output Contract

You must create actual files. Do not stop at a plan.

Create this folder:

```text
--ai-token-saver/
```

Create these files/directories:

```text
--ai-token-saver/
  README.md
  project_brain.md
  project_systems.json
  context_routes.json
  known_patterns.md
  known_pitfalls.md
  editing_rules.md
  generated_agent_instructions.md
  generated_tools_manifest.json
  sessions/
    README.md
  reports/
    README.md
  context/
    README.md
  pyscripts/
    generate_ai_context.py
    report_token_efficiency.py
    update_project_memory.py
    inspect_ai_routes.py
```

If the repository already has a preferred scripts directory such as `pyscripts/`, `tools/`, or `scripts/`, you may also place shims or copies there. Still keep the generated runtime documented under:

```text
--ai-token-saver/generated_tools_manifest.json
```

Do not generate vague placeholder scripts. The scripts must be usable.

If you cannot fully implement a feature because the repository environment is missing a dependency, implement graceful fallback behavior and document the limitation.

---

## 3. Setup Folder Reading Contract

Before initializing the runtime system, read:

```text
--ai-token-saver-setup/AI_REPO_CONTEXT_BOOTSTRAP.md
--ai-token-saver-setup/README.md
--ai-token-saver-setup/schemas/context_routes.schema.json
--ai-token-saver-setup/schemas/project_systems.schema.json
--ai-token-saver-setup/schemas/token_report.schema.json
--ai-token-saver-setup/schemas/generated_tools_manifest.schema.json
--ai-token-saver-setup/examples/
--ai-token-saver-setup/templates/
--ai-token-saver-setup/docs/
```

The setup folder is reusable source material. Do not modify it unless the user asks.

The generated `--ai-token-saver/` folder is repository-specific and may be modified over time.

---

## 4. Parent Repository Ignore Contract

The parent repository should not commit these folders by default:

```gitignore
--ai-token-saver-setup/
--ai-token-saver/
```

If the parent `.gitignore` does not include them, either:

1. Tell the user to run the install helper, or
2. Add the ignore rules if the task allows editing `.gitignore`.

Helper scripts are in:

```text
--ai-token-saver-setup/scripts/install-parent-ignore.sh
--ai-token-saver-setup/scripts/install-parent-ignore.ps1
```

---

## 5. Initialization Pass Requirements

During initialization, do a broad but intelligent scan.

You must discover and document:

### Repository Basics

- repository name
- primary languages
- frameworks
- package/build systems
- test frameworks
- executable scripts
- source roots
- resource roots
- docs roots
- config files
- CI files
- runtime/generated folders
- binary/dependency folders

### Major Systems

A "system" is a coherent feature area or architecture slice.

Examples:

- profile persistence
- generator placement
- auth flow
- inventory service
- invoice generation
- CSV analytics
- frontend settings page
- API client
- database migrations
- plugin bridge layer

For each system, record:

- system name
- purpose
- primary paths
- entrypoints
- data models
- persistence files
- API boundaries
- configs
- tests
- validation commands
- related systems
- notes
- known risks

Write this to:

```text
--ai-token-saver/project_systems.json
--ai-token-saver/project_brain.md
```

`project_systems.json` must follow:

```text
--ai-token-saver-setup/schemas/project_systems.schema.json
```

### Architecture Patterns

Identify reusable patterns, not just files.

Examples:

```text
model → DAO → migration → public static API → script bridge
controller → service → repository → schema
component → hook/store → API client → backend route
CLI command → parser → processor → output writer
```

Record these in:

```text
--ai-token-saver/known_patterns.md
```

### Pitfalls

Identify known or likely failure modes:

- generated folders that must not be scanned
- classloader/load-order issues
- migrations requiring multiple database flavors
- public API signatures that must stay stable
- null-safety requirements for scripting bridges
- rebuild/copy/restart requirements
- validation commands that must be run
- common stale-output traps
- files that look current but are generated

Record these in:

```text
--ai-token-saver/known_pitfalls.md
```

---

## 6. Project-Aware Prompt Conversion

Future users should not need to speak in script-optimized language.

Generated future-agent instructions must tell agents:

- Accept casual prompts.
- Convert them internally into technical task strings.
- Use generated routes to refine scope.
- Do not ask the user to rewrite their prompt unless truly ambiguous.

Examples:

```text
User: I want generators to save like profiles.
Task: generator database persistence model dao sql migration api script bridge profile-like storage
```

```text
User: fix the invoice output formatting
Task: invoice generation output formatting template row insertion spreadsheet export
```

```text
User: review what changed
Task: review current edits changed files validation regression risk
```

### "Like X" Rule

When the user says "like X", treat X as an existing repository pattern to inspect and reuse.

Examples:

```text
"like profiles"
→ inspect profile model, DAO, migrations, API, script bridge, commands/events, and copy the architectural pattern.

"save like orders"
→ inspect order persistence and adapt it.

"make this work like auth"
→ inspect auth entrypoints, middleware, data model, and tests.
```

This rule is critical.

Do not treat "like X" as vague wording when the repository can reveal what X means.

---

## 7. Foundation Pass Rule

For broad architecture migrations, prefer a foundation pass unless the user explicitly requests a complete rewrite.

A foundation pass means:

- create the core model/data shape
- create persistence layer
- add API boundary
- add initial integration points
- preserve compatibility where possible
- avoid rewriting every feature at once
- document follow-up work

Example:

```text
User: I want generators to save like profiles.
```

A good first pass may add:

- generator database model
- DAO/repository
- migrations
- API bridge methods
- minimal script calls
- fallback compatibility

It should not necessarily rewrite every admin/debug/UI flow unless required.

---

## 8. Context Routes

Generate:

```text
--ai-token-saver/context_routes.json
```

It must follow:

```text
--ai-token-saver-setup/schemas/context_routes.schema.json
```

Each route should include:

- `route_name`
- `description`
- `match_terms`
- `negative_match_terms`
- `task_terms`
- `recommended_scope`
- `include_paths`
- `avoid_paths`
- `related_systems`
- `validation_commands`
- `known_pitfalls`
- `confidence`

Routes must be project-specific.

Avoid generic routes if more precise routes exist.

Bad routes:

```text
backend
frontend
database
scripts
```

Better routes:

```text
profile_database_persistence
generator_database_persistence
skript_java_bridge
invoice_template_generation
csv_category_analytics
maven_dependency_bootstrap
minecraft_region_worker_transfer
```

Routes should be used by `generate_ai_context.py`.

---

## 9. Required Context Generator Script

Create:

```text
--ai-token-saver/pyscripts/generate_ai_context.py
```

This script is the per-task context planner/generator.

It must support at least:

```bash
python --ai-token-saver/pyscripts/generate_ai_context.py --task "<task>"
python --ai-token-saver/pyscripts/generate_ai_context.py --preflight --task "<task>"
python --ai-token-saver/pyscripts/generate_ai_context.py --profile changed --task "review current edits"
python --ai-token-saver/pyscripts/generate_ai_context.py --include path --exclude path --task "<task>"
```

You may adapt flag names, but generated agent instructions must show the exact commands.

### Context Generator Responsibilities

The script must:

1. Load `--ai-token-saver/context_routes.json`.
2. Convert or accept a technical task string.
3. Match routes.
4. Identify candidate files.
5. Exclude runtime/generated/binary/dependency folders.
6. Estimate token costs.
7. Generate map/context/manifest files.
8. Recommend narrower routes when broad context is expensive.
9. Snapshot original preflight baseline.
10. Preserve enough metadata for token efficiency reporting.

### Required Generated Context Files

The script should write:

```text
--ai-token-saver/context/map.md
--ai-token-saver/context/task_context.md
--ai-token-saver/context/context.md       # only when safe or explicitly forced
--ai-token-saver/context/manifest.md
```

If the repository uses `.codex/`, optionally mirror:

```text
.codex/map.md
.codex/task_context.md
.codex/context.md
.codex/manifest.md
```

### Required Preflight Baseline Files

On `--preflight`, write:

```text
--ai-token-saver/sessions/latest_baseline.json
--ai-token-saver/sessions/preflight_map.md
--ai-token-saver/sessions/preflight_manifest.md
```

If the repository uses `.codex/`, also mirror:

```text
.codex/session_baseline.json
.codex/preflight_map.md
.codex/preflight_manifest.md
```

### Baseline Rule

The original preflight baseline must not be replaced by a later `--profile changed` refresh.

Token reporting must compare against the original baseline.

### Risk Levels

Use approximate risk levels:

```text
safe       <= 25,000 tokens
moderate   <= 60,000 tokens
expensive  <= 100,000 tokens
dangerous   > 100,000 tokens
```

These thresholds may be configurable.

### Token Counting

Prefer `tiktoken` when available.

If `tiktoken` is missing:

- tell the user if accurate token estimation is required
- optionally fall back to a rough estimate such as `len(text) / 4`
- mark fallback estimates clearly

Do not crash without explanation.

### Candidate File Scoring

The context generator should prioritize:

1. Changed files
2. Exact task matches in path
3. Exact route include paths
4. Exact symbol/class/function matches
5. Exact content matches
6. Dependency/import neighbors
7. Same-folder files
8. build/config/migration files
9. docs that explain the system

It should penalize:

- runtime folders
- generated outputs
- binary files
- dependency caches
- logs
- huge files unless directly relevant

### Manifest Requirements

The manifest should include:

- task
- selected routes
- candidate files
- token estimates
- risk level
- included files
- skipped files/reasons
- recommended command
- recommendation reason
- exact read order
- baseline snapshot path

### Map Requirements

The map should be useful without reading every source file.

It should include:

- project summary
- selected routes
- top files
- symbol summaries when possible
- relevant systems
- warnings/pitfalls
- recommended next action

---

## 10. Required Token Efficiency Reporter

Create:

```text
--ai-token-saver/pyscripts/report_token_efficiency.py
```

It must support at least:

```bash
python --ai-token-saver/pyscripts/report_token_efficiency.py --task "<task>"
python --ai-token-saver/pyscripts/report_token_efficiency.py --task "<task>" --used-file path/to/file
python --ai-token-saver/pyscripts/report_token_efficiency.py --task "<task>" --include-context
python --ai-token-saver/pyscripts/report_token_efficiency.py --task "<task>" --write-report
```

### Reporter Responsibilities

The reporter must:

1. Prefer `--ai-token-saver/sessions/latest_baseline.json`.
2. Fall back to context manifest only if no baseline exists.
3. Count generated context files used.
4. Count explicit inspected files passed via `--used-file`.
5. Include broad context only when `--include-context` is passed.
6. Estimate actual optimized token usage.
7. Estimate saved tokens.
8. Estimate improvement percentage.
9. Write report JSON and Markdown under `--ai-token-saver/reports/`.
10. Clearly state estimates are not billing data.

### Negative Savings Case

If optimized tokens exceed baseline, do not hide it.

Report it clearly and explain likely causes:

- baseline was too narrow
- user inspected many source files
- broad context was not the true alternative
- baseline was overwritten or missing
- task required many edits

This exact failure mode must be defended against:

```text
post-edit changed-files context accidentally used as original baseline
```

### Report Fields

The report should include:

- task
- baseline source
- baseline tokens
- optimized tokens
- estimated saved tokens
- improvement percentage
- used original baseline
- included context files
- inspected files
- notes
- created timestamp

It must follow:

```text
--ai-token-saver-setup/schemas/token_report.schema.json
```

---

## 11. Required Memory Updater

Create:

```text
--ai-token-saver/pyscripts/update_project_memory.py
```

It should help agents update:

```text
--ai-token-saver/known_patterns.md
--ai-token-saver/known_pitfalls.md
--ai-token-saver/context_routes.json
--ai-token-saver/project_brain.md
```

The script should support adding notes like:

```bash
python --ai-token-saver/pyscripts/update_project_memory.py --pitfall "Skript-facing Java APIs must guard null values."
python --ai-token-saver/pyscripts/update_project_memory.py --pattern "Profile persistence uses model -> DAO -> migration -> API bridge -> Skript wrapper."
```

It must avoid destructive overwrites.

If it cannot safely update JSON routes, it should write a pending suggestion file under:

```text
--ai-token-saver/reports/memory_update_suggestions.md
```

---

## 12. Required Route Inspector

Create:

```text
--ai-token-saver/pyscripts/inspect_ai_routes.py
```

It should help humans/agents inspect available routes:

```bash
python --ai-token-saver/pyscripts/inspect_ai_routes.py
python --ai-token-saver/pyscripts/inspect_ai_routes.py --match "generator database"
```

It should print:

- route name
- description
- match terms
- task terms
- include paths
- validation commands
- pitfalls

---

## 13. Generated Agent Instructions

Create:

```text
--ai-token-saver/generated_agent_instructions.md
```

This is one of the most important files.

It must be directly usable as permanent context/instructions for future AI coding agents.

It must be repository-specific.

It must include:

1. Automatically use the AI Token Saver workflow for repository tasks.
2. Do not wait for the user to mention the context system.
3. Convert casual user prompts into technical task strings.
4. Treat "like X" as a pattern to inspect and reuse.
5. Run preflight before broad reading.
6. Read generated map/manifest before source files.
7. Follow route recommendations.
8. Preserve original preflight baseline.
9. Avoid runtime/generated folders.
10. Inspect exact source files only when needed.
11. Make smallest complete edits.
12. Prefer foundation passes for broad migrations.
13. Validate after edits.
14. Report full relative file paths.
15. Run token efficiency reporting at the end.
16. Update memory when reusable lessons are learned.
17. If compiler/log output identifies an exact file, still use the workflow unless the task is purely explanatory and no edit is needed.
18. For tiny obvious compiler fixes, use a focused task and narrow changed/plugin scope.

Use the template:

```text
--ai-token-saver-setup/templates/generated_agent_instructions.template.md
```

as a starting point, but make the final file much more specific to the repository.

---

## 14. Editing Rules

Create:

```text
--ai-token-saver/editing_rules.md
```

It must include general rules and repository-specific rules.

General rules:

- Identify relevant files before editing.
- Make the smallest complete change.
- Prefer targeted edits over full-file rewrites.
- Do not rewrite unrelated files.
- Do not create placeholder files unless requested.
- Preserve existing APIs unless the task requires changing them.
- Do not manually edit generated context files except through generated tooling.
- Explain when a new dependency becomes relevant mid-task.
- Validate after editing.
- Report full relative paths.

Repository-specific rules should be inferred.

Examples:

- If adding a DB field, update model, DAO, migrations, API, tests.
- If changing a Skript Java bridge, update Java API and Skript calls.
- If changing a CLI flag, update help text and docs.
- If changing a spreadsheet generator, preserve formatting unless asked otherwise.

---

## 15. Validation Rules

Discover validation commands.

Examples:

```text
Gradle:
./gradlew build

Maven:
mvn test

Python:
python -m pytest

Node:
npm test
npm run build

Rust:
cargo test
```

Write known commands to:

```text
--ai-token-saver/project_brain.md
--ai-token-saver/editing_rules.md
--ai-token-saver/generated_agent_instructions.md
```

If no validation command is known, say so explicitly and record the gap.

---

## 16. Full Relative Path Rule

Future agents must always report full relative paths.

Bad:

```text
Profile.java
SkDatabaseAPI.java
```

Good:

```text
BanknoteLib/src/main/java/me/k9lil/banknotelib/database/model/Profile.java
BanknoteLib/src/main/java/me/k9lil/banknotelib/SkDatabaseAPI.java
```

This rule applies to:

- changed files
- relevant files
- inspected files
- errors
- reports

---

## 17. Runtime / Generated Folder Avoidance

The generated system must avoid broad reading of:

- `.git/`
- `.idea/`
- `.vscode/`
- `.gradle/`
- `.mvn/`
- `.venv/`
- `venv/`
- `env/`
- `node_modules/`
- `build/`
- `target/`
- `dist/`
- `out/`
- logs
- caches
- generated reports
- server worlds
- binary dependencies
- `.codex/context.md` unless needed
- `--ai-token-saver/context/context.md` unless needed

The initialization may inspect enough metadata to know these folders exist, but future context generation should not pack them.

---

## 18. Lessons From Prototype To Preserve

The generated system should defend against the exact lessons learned during prototype development:

### Lesson: Hardcoded Generic Routing Is Weak

Better:
- create project-specific route JSON from actual repository systems
- use "like X" pattern interpretation
- update routes when mistakes reveal gaps

### Lesson: Preflight Baseline Must Be Preserved

Bad:
- report token efficiency against a post-edit changed-files manifest

Good:
- snapshot original preflight baseline
- reporter prefers session baseline

### Lesson: Broad Context May Be Unsafe

If context is expensive/dangerous:
- stop broad reading
- report risk
- recommend narrower command/route
- do not use force unless user approves

### Lesson: Compiler Errors Can Be Exact But Still Need Workflow

If compiler output identifies an exact file:
- convert error into focused task
- use narrow route/profile
- edit exact file
- validate
- report token efficiency

### Lesson: Script-Facing APIs Need Defensive Boundaries

If a dynamic scripting layer can call Java/Python/host APIs:
- validate null/none/blank inputs
- avoid throwing low-level exceptions for expected missing values
- preserve compatibility

### Lesson: Generated Runtime Must Have Permanent Instructions

The setup is incomplete unless it outputs future-agent instructions that users can copy into future coding agents.

### Lesson: Human Prompts Stay Human

Do not require the user to say:
- run preflight
- use context system
- inspect DAO
- make a foundation pass
- report token efficiency

The generated agent instructions must enforce that automatically.

---

## 19. README For Generated Runtime

Create:

```text
--ai-token-saver/README.md
```

It must explain:

- what the folder is
- how to run preflight
- how to generate context
- how to report token efficiency
- how to inspect routes
- how to update memory
- how future agents should use generated instructions

---

## 20. Generated Tools Manifest

Create:

```text
--ai-token-saver/generated_tools_manifest.json
```

It must follow:

```text
--ai-token-saver-setup/schemas/generated_tools_manifest.schema.json
```

It should list each generated script:

- name
- path
- purpose
- commands
- inputs
- outputs
- dependencies
- notes

---

## 21. Final Initialization Report

After creating files, report:

1. Generated runtime folder path.
2. Generated files.
3. Generated scripts.
4. Major discovered systems.
5. Generated routes.
6. Avoided runtime/generated folders.
7. Validation commands.
8. Path to generated agent instructions.
9. How the user should prompt future agents.
10. Any limitations or dependencies.

Do not claim success unless the files exist.

---

## 22. Intended User Command

The intended command from the user is:

```text
Look through --ai-token-saver-setup and set it up for this repository.
```

That should be enough.

The user should not need to provide any additional bootstrap explanation.
