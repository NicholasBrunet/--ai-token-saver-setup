# AI Repo Context Bootstrap Specification

## 0. Purpose

You are an AI coding agent operating inside a repository that contains:

```text
--ai-token-saver-setup/
```

Your task is to create a repository-specific AI context and token optimization runtime:

```text
--ai-token-saver/
```

This setup uses one expensive initialization pass to create durable project-specific tooling. Future tasks should avoid broad repository scanning by using generated routes, generated context, and permanent agent instructions.

The generated runtime system must support:

```text
casual user prompt
→ project-aware technical task string
→ preflight token/context estimate
→ stale context validation
→ route-based focused context generation
→ targeted file inspection
→ small complete edits
→ validation
→ token efficiency report
→ optional project memory update
```

This file is an operating contract. Do not merely summarize it. Build the system.

## 1. Non-Negotiable Output Contract

Create:

```text
--ai-token-saver/
  README.md
  runtime_version.json
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
  backups/
    README.md
  pyscripts/
    generate_ai_context.py
    report_token_efficiency.py
    update_project_memory.py
    inspect_ai_routes.py
```

Do not create vague placeholder scripts. If a feature cannot be fully implemented, implement graceful fallback behavior and document the limitation.

## 2. Required Setup Files To Read

Before initialization, read:

```text
--ai-token-saver-setup/README.md
--ai-token-saver-setup/VERSION
--ai-token-saver-setup/CHANGELOG.md
--ai-token-saver-setup/UPGRADE.md
--ai-token-saver-setup/AI_REPO_CONTEXT_BOOTSTRAP.md
--ai-token-saver-setup/schemas/
--ai-token-saver-setup/examples/
--ai-token-saver-setup/templates/
--ai-token-saver-setup/docs/
```

Do not modify setup files unless the user explicitly asks.

## 3. Parent Ignore Contract

The parent repository should ignore:

```gitignore
--ai-token-saver-setup/
--ai-token-saver/
```

## 4. Initialization Discovery Requirements

Discover and document:

- repository name
- languages
- frameworks
- package/build tools
- test frameworks
- executable scripts
- source roots
- resource roots
- config files
- CI files
- runtime/generated folders
- binary/dependency folders
- major systems/domains
- architecture patterns
- validation commands
- known pitfalls

For each major system, record:

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

Write this to:

```text
--ai-token-saver/project_systems.json
--ai-token-saver/project_brain.md
```

## 5. Architecture Pattern Discovery

Do not only list files. Infer reusable patterns.

Examples:

```text
model → DAO → migration → public static API → script bridge
controller → service → repository → schema
component → hook/store → API client → backend route
CLI command → parser → processor → output writer
```

Write these to:

```text
--ai-token-saver/known_patterns.md
```

## 6. Project-Aware Prompt Conversion

Future users should not need script-optimized prompts.

Generated agent instructions must tell agents to convert casual prompts into technical task strings.

Examples:

```text
User: I want generators to save like profiles.
Task: generator database persistence model dao sql migration api script bridge profile-like storage

User: migrate Claims from CSV like profiles/generators.
Task: claim database persistence migrate csv model dao api migration script bridge profile generator pattern

User: review what changed.
Task: review current edits changed files validation regression risk
```

### "Like X" Rule

When the user says "like X", treat X as an existing project pattern to inspect and reuse.

Do not treat "like profiles" or "save like X" as vague wording if repository context can reveal what X means.

## 7. Foundation Pass Rule

For broad architecture migrations, prefer a foundation pass unless the user explicitly asks for a full rewrite.

A foundation pass should create or update:

```text
model/data shape
→ persistence layer
→ migration/schema
→ public API boundary
→ minimal integration layer
→ validation
→ follow-up notes
```

## 8. Context Routes

Generate:

```text
--ai-token-saver/context_routes.json
```

Routes must be project-specific and follow the context routes schema.

Each route should include:

- route name
- description
- match terms
- negative match terms
- expanded task terms
- recommended scope/profile
- include paths
- avoid paths
- related systems
- validation commands
- known pitfalls
- confidence

Good examples:

```text
profile_database_persistence
generator_database_persistence
claim_database_persistence
skript_java_bridge
invoice_template_generation
csv_category_analytics
maven_dependency_bootstrap
```

Avoid vague routes like `backend`, `frontend`, or `database` when more specific routes are possible.

## 9. Required Context Generator

Create:

```text
--ai-token-saver/pyscripts/generate_ai_context.py
```

It must support:

```bash
python --ai-token-saver/pyscripts/generate_ai_context.py --task "<task>"
python --ai-token-saver/pyscripts/generate_ai_context.py --preflight --task "<task>"
python --ai-token-saver/pyscripts/generate_ai_context.py --profile changed --task "review current edits"
python --ai-token-saver/pyscripts/generate_ai_context.py --include path --exclude path --task "<task>"
```

It must:

1. Load `--ai-token-saver/context_routes.json`.
2. Match routes to the task.
3. Identify candidate files.
4. Exclude runtime/generated/binary/dependency folders.
5. Estimate token costs.
6. Generate map/context/manifest files.
7. Recommend narrower routes if broad context is expensive.
8. Snapshot original preflight baseline.
9. Include current task and task hash in map/manifest.
10. Detect stale context files.
11. Preserve metadata for token efficiency reporting.

Required outputs:

```text
--ai-token-saver/context/map.md
--ai-token-saver/context/task_context.md
--ai-token-saver/context/context.md       # only when safe or forced
--ai-token-saver/context/manifest.md
```

Preflight outputs:

```text
--ai-token-saver/sessions/latest_baseline.json
--ai-token-saver/sessions/preflight_map.md
--ai-token-saver/sessions/preflight_manifest.md
```

## 10. Stale Context Protection

Mandatory.

Every generated map and manifest must include:

```text
task
task_hash
created_at
selected_routes
baseline_path
```

Before trusting existing context, future agents must verify:

1. the task matches the current task, or
2. the task hash matches the current task hash.

If map/manifest is stale:

```text
Do not fall back to broad manual file reads.
Rerun the context generator for the current task.
Verify the new task/hash matches.
Only then inspect exact source files.
```

## 11. Required Token Efficiency Reporter

Create:

```text
--ai-token-saver/pyscripts/report_token_efficiency.py
```

It must:

1. Prefer `--ai-token-saver/sessions/latest_baseline.json`.
2. Fall back to current manifest only if no baseline exists.
3. Count generated context files used.
4. Count explicit inspected files passed by `--used-file`.
5. Include broad context only when `--include-context` is passed.
6. Estimate saved tokens and improvement percentage.
7. Write JSON and Markdown reports under `--ai-token-saver/reports/`.
8. Clearly state estimates are not billing data.

It must defend against using a post-edit changed-files manifest as the original baseline.

## 12. Required Memory Updater

Create:

```text
--ai-token-saver/pyscripts/update_project_memory.py
```

It should support:

```bash
python --ai-token-saver/pyscripts/update_project_memory.py --pitfall "Skript-facing Java APIs must guard null values."
python --ai-token-saver/pyscripts/update_project_memory.py --pattern "Profile persistence uses model -> DAO -> migration -> API bridge -> Skript wrapper."
```

If JSON route updates are unsafe, write suggestions under:

```text
--ai-token-saver/reports/memory_update_suggestions.md
```

## 13. Required Route Inspector

Create:

```text
--ai-token-saver/pyscripts/inspect_ai_routes.py
```

It should support:

```bash
python --ai-token-saver/pyscripts/inspect_ai_routes.py
python --ai-token-saver/pyscripts/inspect_ai_routes.py --match "claim database"
```

## 14. Required Generated Agent Instructions

Create:

```text
--ai-token-saver/generated_agent_instructions.md
```

It must be repository-specific and include:

- automatically use the workflow for repository tasks
- do not wait for the user to request the context system
- convert casual prompts into technical task strings
- treat "like X" as an existing project pattern
- run preflight before broad reading
- verify context task/hash is not stale
- follow route recommendations
- preserve original baseline
- avoid runtime/generated folders
- inspect exact source files only when needed
- make smallest complete edits
- prefer foundation passes for broad migrations
- validate after edits
- report full relative file paths
- run token efficiency reporting
- update memory after reusable lessons
- use narrow workflow even for compiler/log errors that identify exact files

## 15. Upgrade Lifecycle

The setup repo may be updated with:

```bash
git -C --ai-token-saver-setup pull
```

The generated runtime must include:

```text
--ai-token-saver/runtime_version.json
```

with:

```json
{
  "setup_version": "0.2.0",
  "runtime_schema_version": "1",
  "initialized_at": "...",
  "last_upgraded_at": "..."
}
```

Future agents and scripts should use:

```bash
python --ai-token-saver-setup/scripts/check_setup_version.py
python --ai-token-saver-setup/scripts/upgrade_runtime.py
```

Upgrade rules:

- never blindly overwrite project memory
- preserve `project_brain.md`
- preserve `context_routes.json`
- preserve `known_patterns.md`
- preserve `known_pitfalls.md`
- preserve `editing_rules.md`
- back up before changing generated instructions/scripts/metadata
- report whether full reinitialization is recommended
- only recommend full reinitialization if expected improvement is meaningful

## 16. Runtime / Generated Folder Avoidance

Avoid broad reads of:

```text
.git/
.idea/
.vscode/
.gradle/
.mvn/
.venv/
venv/
env/
node_modules/
build/
target/
dist/
out/
logs/
caches/
generated reports/
server worlds/
binary dependencies/
--ai-token-saver/context/context.md unless needed
```

## 17. Full Relative Path Rule

Always report full relative paths.

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

## 18. Final Initialization Report

After creating files, report:

1. Runtime folder path.
2. Generated files.
3. Generated scripts.
4. Major systems discovered.
5. Routes generated.
6. Avoided folders.
7. Validation commands.
8. Generated agent instructions path.
9. How future users should prompt agents.
10. Limitations or dependencies.

Do not claim completion unless files exist.

## 19. Intended User Command

This should be enough:

```text
Look through --ai-token-saver-setup and set it up for this repository.
```
