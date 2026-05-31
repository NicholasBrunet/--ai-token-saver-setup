# AI Token Saver Workflow

## Initialization

1. Clone setup repo into parent project.
2. Run parent ignore helper.
3. Optionally run initialization cost estimate.
4. Ask the AI agent to set up the repository.
5. Agent generates `--ai-token-saver/`.

## Future Tasks

1. User gives casual prompt.
2. Agent converts to technical task.
3. Agent runs preflight.
4. Agent verifies generated context task/hash.
5. Agent follows routes.
6. Agent edits exact relevant files.
7. Agent validates.
8. Agent reports token efficiency.
9. Agent updates memory if needed.

## Upgrade

1. `git -C --ai-token-saver-setup pull`
2. `python --ai-token-saver-setup/scripts/check_setup_version.py`
3. `python --ai-token-saver-setup/scripts/upgrade_runtime.py`
