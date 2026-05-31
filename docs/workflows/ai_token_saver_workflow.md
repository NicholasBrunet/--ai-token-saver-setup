# AI Token Saver Workflow

## Setup-Time Workflow

1. User clones `--ai-token-saver-setup` into a project.
2. User tells agent: `Look through --ai-token-saver-setup and set it up for this repository.`
3. Agent reads the bootstrap, schemas, examples, docs, and templates.
4. Agent performs one expensive repo discovery pass.
5. Agent generates `--ai-token-saver/`.
6. Agent reports generated files, routes, validation commands, and permanent instructions.

## Future Task Workflow

1. User gives casual prompt.
2. Agent converts it to a technical task string.
3. Agent runs context preflight.
4. Agent reads generated map/manifest.
5. Agent follows route recommendation.
6. Agent reads focused context.
7. Agent inspects exact source files only when needed.
8. Agent edits smallest complete set of files.
9. Agent validates.
10. Agent runs token efficiency report.
11. Agent updates memory if it learned a reusable pitfall or pattern.
