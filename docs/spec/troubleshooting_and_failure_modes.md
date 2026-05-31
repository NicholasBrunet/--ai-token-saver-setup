# Troubleshooting And Failure Modes

## Stale Context

If generated map/manifest references an older task, rerun context generation. Do not manually read many files.

## Negative Token Savings

Usually caused by:
- wrong baseline
- changed-files manifest used as baseline
- too many source files counted
- task genuinely required broad edits

## Weak Runtime

If generated files are generic, rerun initialization with stronger project-specific requirements.

## Upgrade Safety

Upgrade scripts must preserve project memory and create backups before changing runtime instructions or scripts.
