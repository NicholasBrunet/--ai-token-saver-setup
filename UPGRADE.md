# Upgrade Guide

Update the nested setup repo:

```bash
git -C --ai-token-saver-setup pull
```

PowerShell:

```powershell
git -C .\--ai-token-saver-setup pull
```

Check runtime version:

```bash
python --ai-token-saver-setup/scripts/check_setup_version.py
```

Apply safe runtime upgrade:

```bash
python --ai-token-saver-setup/scripts/upgrade_runtime.py
```

## Upgrade Philosophy

The setup repo is reusable and updateable.

The runtime folder is project-specific and must not be blindly overwritten.

Preserve:

```text
--ai-token-saver/project_brain.md
--ai-token-saver/context_routes.json
--ai-token-saver/known_patterns.md
--ai-token-saver/known_pitfalls.md
--ai-token-saver/editing_rules.md
```

Safe upgrade targets include:

```text
--ai-token-saver/runtime_version.json
--ai-token-saver/generated_agent_instructions.md
--ai-token-saver/generated_tools_manifest.json
--ai-token-saver/reports/
--ai-token-saver/backups/
```

Scripts can be upgraded, but should be backed up first.

## When Full Reinitialization Is Worth It

Only consider full reinitialization if:

- setup schemas changed in a breaking way
- generated runtime scripts are missing or unusable
- project routes are low quality
- project brain is mostly empty or generic
- a new setup version provides major discovery improvements

The upgrade script should report whether full reinitialization is recommended.
