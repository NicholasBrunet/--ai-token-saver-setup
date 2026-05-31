# AI Token Saver Setup

A reusable bootstrap repository for creating project-specific AI context and token-optimization tooling.

This repository is meant to be cloned directly into another repository as a nested local repo:

```bash
git clone https://github.com/YOUR_NAME/--ai-token-saver-setup.git ./--ai-token-saver-setup
```

Then ask your AI coding agent:

```text
Look through --ai-token-saver-setup and set it up for this repository.
```

The AI agent should read this setup repo, perform a one-time expensive repository initialization pass, and generate:

```text
--ai-token-saver/
```

That generated folder contains project-specific memory, routing, scripts, reports, and permanent future-agent instructions.

## Folder Model

```text
your-project/
  .git/
  .gitignore

  --ai-token-saver-setup/      # nested setup repo, ignored by parent
    .git/
    README.md
    AI_REPO_CONTEXT_BOOTSTRAP.md
    initialization_cost.py
    schemas/
    examples/
    templates/
    docs/
    scripts/

  --ai-token-saver/            # generated project-specific runtime, ignored by parent
```

## Parent Repo Ignore Rules

The parent project should usually ignore both folders:

```gitignore
--ai-token-saver-setup/
--ai-token-saver/
```

Install helper:

PowerShell:

```powershell
.\--ai-token-saver-setup\scripts\install-parent-ignore.ps1
```

Linux/macOS/Git Bash:

```bash
./--ai-token-saver-setup/scripts/install-parent-ignore.sh
```

## Estimate Initialization Cost

Before asking the AI agent to perform the one-time setup, you can estimate the likely token cost.

From the parent project root:

```bash
python --ai-token-saver-setup/initialization_cost.py
```

PowerShell:

```powershell
python .\--ai-token-saver-setup\initialization_cost.py
```

From inside `--ai-token-saver-setup/`:

```bash
python initialization_cost.py
```

Write a report:

```bash
python --ai-token-saver-setup/initialization_cost.py --write-report
```

PowerShell:

```powershell
python .\--ai-token-saver-setup\initialization_cost.py --write-report
```

This writes:

```text
--ai-token-saver-setup/reports/initialization_cost.json
--ai-token-saver-setup/reports/initialization_cost.md
```

The script estimates:

```text
parent project readable source cost
+
--ai-token-saver-setup readable setup cost
=
estimated one-time initialization cost
```

It excludes common runtime, generated, dependency, binary, and cache folders by default. The estimate is useful for planning, but it is not exact billing data.

## What The AI Must Generate

At minimum:

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
  reports/
  context/
  pyscripts/
    generate_ai_context.py
    report_token_efficiency.py
    update_project_memory.py
    inspect_ai_routes.py
```

The exact implementation can be adapted to the repository, but the generated behavior must satisfy the bootstrap specification.

## Why This Exists

AI coding agents waste tokens and make worse edits when they broadly search a repository before understanding it.

This setup asks the AI to spend more once, then generate project-specific context tooling so future tasks become:

```text
casual user prompt
→ project-aware task conversion
→ preflight context estimate
→ focused route-based context
→ targeted exact file reads
→ small complete edit
→ validation
→ token efficiency report
→ memory update if useful
```

## Intended Agent Prompt

Use this exact prompt after cloning:

```text
Look through --ai-token-saver-setup and set it up for this repository.
```

## Important

This setup folder is generic and reusable.

The generated `--ai-token-saver/` folder is project-specific and should be regenerated or updated per repository.
