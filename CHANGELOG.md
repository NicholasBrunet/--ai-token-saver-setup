# Changelog

## 0.2.0

### Added

- Upgrade lifecycle for nested setup repo updates.
- `VERSION` file.
- `UPGRADE.md`.
- `scripts/check_setup_version.py`.
- `scripts/upgrade_runtime.py`.
- Required generated `--ai-token-saver/runtime_version.json`.
- Stale context protection requirement:
  - context map/manifest must include task and task hash
  - agents must rerun context generation if current task does not match manifest task/hash
  - agents must not fall back to broad manual file reads when context is stale
- Bootstrap instructions for preserving project-specific runtime memory during upgrades.
- `runtime_version.schema.json`.

### Improved

- README now documents update and upgrade commands.
- Bootstrap now explicitly requires stale context validation.
- Bootstrap now states upgrades must not blindly overwrite project memory files.

### Runtime Upgrade Impact

No full reinitialization should be required for existing runtimes.

Expected meaningful difference:
- Future agents should detect stale context map/manifest files and rerun context generation instead of manually reading many files.
- Future token reports should continue using the original preflight baseline.
- Runtime metadata will record the setup version used.

## 0.1.0

Initial bootstrap system:
- setup repo structure
- bootstrap spec
- schemas
- examples
- templates
- initialization cost estimator
- parent ignore scripts
